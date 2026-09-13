#!/usr/bin/env python3
"""Clean-extraction replay of both newly supplied dependency chains."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time


PACKAGE = Path(__file__).resolve().parents[1]
SOURCE = PACKAGE / "repository"
GLOBAL = Path("results/2026-08-26_p29_global_dependency_replay")
DYADIC = Path("results/2026-08-25_dyadic_stopping")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_gp_matrix(path: Path) -> list[list[int]]:
    text = path.read_text(encoding="utf-8").strip()
    if "]\n[" in text:
        text = "[" + text.rsplit("]\n[", 1)[1]
    assert text.startswith("[") and text.endswith("]"), path
    rows = [
        [int(entry.strip()) for entry in row.split(",")]
        for row in text[1:-1].split(";")
    ]
    return rows


def run(command: list[str], cwd: Path, environment: dict[str, str], timeout: int) -> tuple[str, float]:
    started = time.monotonic()
    completed = subprocess.run(
        command, cwd=cwd, env=environment, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        timeout=timeout, check=False,
    )
    elapsed = time.monotonic() - started
    if completed.returncode != 0:
        raise AssertionError((command, completed.returncode, completed.stdout[-4000:]))
    return completed.stdout, elapsed


def without_elapsed(value: dict) -> dict:
    value = dict(value)
    value.pop("elapsed_seconds", None)
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log")
    parser.add_argument("--gp", default="/usr/bin/gp")
    args = parser.parse_args()
    gp = Path(args.gp)
    if not gp.is_file():
        raise SystemExit("PARI/GP is required; pass --gp PATH")

    with tempfile.TemporaryDirectory(prefix="corrected66-p2-place2-clean-") as temporary:
        repository = Path(temporary) / "repository"
        shutil.copytree(SOURCE, repository, symlinks=False)
        common = {
            "PATH": "/usr/bin:/bin",
            "HOME": "/tmp",
            "LANG": "C",
            "LC_ALL": "C",
            "PYTHONDONTWRITEBYTECODE": "1",
        }

        global_cert_path = repository / GLOBAL / "certificates/p29_corrected_relaxed_global_intersection_v1.json"
        frozen_global = json.loads(global_cert_path.read_text())
        frozen_hashes = {
            name: expected for name, expected in frozen_global["input_hashes"].items()
            if name.startswith(str(GLOBAL / "inputs/corrected_"))
        }
        frozen_bytes = {}
        frozen_matrices = {}
        for name, expected in frozen_hashes.items():
            target = repository / name
            assert sha256(target) == expected, name
            frozen_bytes[name] = target.read_bytes()
            if "basis_" not in Path(name).name:
                frozen_matrices[name] = parse_gp_matrix(target)
        rebuild_checkpoint = repository / GLOBAL / "checkpoints/p29_corrected_nondyadic_columns_v1.bin"
        rebuild_certificate = repository / GLOBAL / "certificates/p29_corrected_nondyadic_columns_v1.gpdata"
        frozen_checkpoint = Path(temporary) / "frozen_p29_corrected_nondyadic_columns_v1.bin"
        frozen_checkpoint.write_bytes(rebuild_checkpoint.read_bytes())
        frozen_rebuild_certificate = rebuild_certificate.read_bytes()
        # GP's writebin/write calls append to existing targets.  Remove only
        # these clean-extraction outputs so this is a genuine reconstruction.
        rebuild_checkpoint.unlink()
        rebuild_certificate.unlink()
        rebuild_env = dict(common)
        rebuild_env["P29_GLOBAL_REPLAY_OUTPUT_BASE"] = str(GLOBAL)
        rebuild_out, rebuild_wall = run(
            [str(gp), "-q", "-f", str(repository / GLOBAL / "scripts/rebuild_corrected_nondyadic_columns_v1.gp")],
            repository, rebuild_env, 900,
        )
        assert "STATUS=PASS_P29_CORRECTED_NONDYADIC_COLUMNS_V1" in rebuild_out
        for name, expected_matrix in frozen_matrices.items():
            assert parse_gp_matrix(repository / name) == expected_matrix, name
        compare_checkpoint = Path(temporary) / "compare_rebuilt_checkpoint.gp"
        compare_checkpoint.write_text(
            f'a=read("{frozen_checkpoint}");'
            f'b=read("{rebuild_checkpoint}");'
            'eq=vector(#a,i,a[i]==b[i]);'
            'if(#a==16&&vecsum(eq)==16,'
            'print("REBUILT_CHECKPOINT_SEMANTIC_EQUAL=PASS_16_COMPONENTS");quit(0),'
            'print("REBUILT_CHECKPOINT_COMPONENT_EQUALITY=",eq);quit(2))\n',
            encoding="utf-8",
        )
        checkpoint_out, checkpoint_wall = run(
            [str(gp), "-q", "-f", str(compare_checkpoint)],
            repository, common, 120,
        )
        assert "REBUILT_CHECKPOINT_SEMANTIC_EQUAL=PASS_16_COMPONENTS" in checkpoint_out, checkpoint_out
        assert b"".join(rebuild_certificate.read_bytes().split()) == b"".join(
            frozen_rebuild_certificate.split()
        )
        # GP's text serialization is environment-sensitive.  The arithmetic
        # objects above are exact; restore the frozen serialization before the
        # historical intersection so its input-hash certificate also replays.
        for name, content in frozen_bytes.items():
            (repository / name).write_bytes(content)
            assert sha256(repository / name) == frozen_hashes[name], name
        rebuild_checkpoint.write_bytes(frozen_checkpoint.read_bytes())
        rebuild_certificate.write_bytes(frozen_rebuild_certificate)
        assert sha256(rebuild_checkpoint) == "b8783a3620c5c7172f369430dd21daf620d07258308513d6b1f866ae14fc803d"
        assert sha256(rebuild_certificate) == "812bd1acffbebe4f4bedd259c90fc42edbabdc7fa46cfd8b02122f2bb348eaf0"

        intersect_out, intersect_wall = run(
            ["/usr/bin/python3", "-B", str(repository / GLOBAL / "scripts/intersect_corrected_relaxed_global_v1.py")],
            repository, common, 300,
        )
        assert "corrected after-p7 rank/dimension without p29,p2: 48 18" in intersect_out
        assert sha256(global_cert_path) == "3771c4e499644de48f5dc94e3558269edee409caa2fd17ba81a3d0984cbaa085"
        basis = repository / GLOBAL / "inputs/corrected_relaxed_basis_after_p7_without_p29_p2_v1.txt"
        assert sha256(basis) == "1672118ec7db07a100811fd4cba97de962c03349e82029d9361a1a93144d8c07"

        norm_out, norm_wall = run(
            ["/usr/bin/python3", "-B", str(repository / GLOBAL / "scripts/certify_norm_transported19_sensitivity_v1.py")],
            repository, common, 120,
        )
        assert "status: PASS_P29_NORM_TRANSPORTED19_SENSITIVITY_V1" in norm_out
        assert sha256(repository / GLOBAL / "certificates/p29_norm_transported19_sensitivity_v1.json") == (
            "6f66f6fe558f89a01b93ccfd8ffaee6c5d8bf12d372514ce01c11abec302ea62"
        )
        audit_out, audit_wall = run(
            ["/usr/bin/python3", "-B", str(repository / GLOBAL / "scripts/independent_audit_corrected_global_dependency_replay_v1.py")],
            repository, common, 300,
        )
        assert json.loads(audit_out)["status"] == "PASS"
        consumed = repository / "results/2026-08-26_p29_corrected_dyadic_replay/inputs/corrected_after_p7_basis_consumed_v1.txt"
        basis_matrix = parse_gp_matrix(basis)
        assert len(basis_matrix) == 18 and all(len(row) == 66 for row in basis_matrix)
        assert basis_matrix == parse_gp_matrix(consumed)
        assert sha256(consumed) == "842dc043bcc430a4a7a4961f173eb4e873aa6809bbccd935cc1b55ef781b77bf"

        frozen_production_path = repository / DYADIC / "checkpoints/p2_place2_local_stopping_v1.json"
        frozen_independent_path = repository / DYADIC / "certificates/independent_p2_place2_local_stopping_v1.json"
        frozen_production = json.loads(frozen_production_path.read_text())
        frozen_independent = json.loads(frozen_independent_path.read_text())
        production_output = repository / "replay-output/p2-place2-production.json"
        production_output.parent.mkdir(parents=True, exist_ok=True)
        production_env = dict(common)
        production_env["P2_PLACE2_STOPPING_OUT"] = str(production_output)
        production_out, production_wall = run(
            ["/usr/bin/python3", "-B", str(repository / DYADIC / "scripts/certify_p2_place2_local_stopping_v1.py")],
            repository, production_env, 3600,
        )
        assert "STATUS=PASS_SECOND_DYADIC_LOCAL_STOPPING" in production_out
        regenerated_production = json.loads(production_output.read_text())
        assert without_elapsed(regenerated_production) == without_elapsed(frozen_production)

        frozen_independent_path.unlink()
        independent_out, independent_wall = run(
            ["/usr/bin/python3", "-B", str(repository / DYADIC / "scripts/independent_verify_p2_place2_local_stopping_v1.py")],
            repository, common, 3600,
        )
        assert "STATUS=PASS_INDEPENDENT_SECOND_DYADIC_LOCAL_STOPPING" in independent_out
        regenerated_independent = json.loads(frozen_independent_path.read_text())
        assert without_elapsed(regenerated_independent) == without_elapsed(frozen_independent)

        rendered = (
            "ORIGINAL_WORKSPACE_USED=false\n"
            f"PARI_GP={gp}\n"
            f"GLOBAL_COLUMN_REBUILD_WALL_SECONDS={rebuild_wall:.6f}\n"
            + rebuild_out
            + f"GLOBAL_CHECKPOINT_COMPARISON_WALL_SECONDS={checkpoint_wall:.6f}\n"
            + checkpoint_out
            + "GLOBAL_COLUMN_REBUILD=EXACT_MATRICES_AND_GP_OBJECTS_WITH_SERIALIZATION_NORMALIZED\n"
            + f"GLOBAL_INTERSECTION_WALL_SECONDS={intersect_wall:.6f}\n"
            + intersect_out
            + f"NORM_SENSITIVITY_WALL_SECONDS={norm_wall:.6f}\n"
            + norm_out
            + f"INDEPENDENT_GLOBAL_AUDIT_WALL_SECONDS={audit_wall:.6f}\n"
            + "INDEPENDENT_GLOBAL_AUDIT=PASS\n"
            + "PREDYADIC_BASIS=EXACT_18X66_MATRIX_EQUAL_TO_GP_RESERIALIZED_DYADIC_CONSUMED_COPY\n"
            + f"P2_PLACE2_PRODUCTION_WALL_SECONDS={production_wall:.6f}\n"
            + production_out
            + "P2_PLACE2_PRODUCTION=EXACT_JSON_EXCEPT_ELAPSED_SECONDS\n"
            + f"P2_PLACE2_INDEPENDENT_WALL_SECONDS={independent_wall:.6f}\n"
            + independent_out
            + "P2_PLACE2_INDEPENDENT=EXACT_JSON_EXCEPT_ELAPSED_SECONDS\n"
            + "P2_PLACE2_CORRECTION=PASS_PROFILE_0_1_NONZERO\n"
        )
        print(rendered, end="")
        if args.log:
            destination = Path(args.log).resolve()
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
