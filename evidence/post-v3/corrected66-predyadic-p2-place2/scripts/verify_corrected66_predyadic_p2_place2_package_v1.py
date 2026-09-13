#!/usr/bin/env python3
"""Strict tree, dependency, and exact finite-interface verification."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess


PACKAGE = Path(__file__).resolve().parents[1]
REPOSITORY = PACKAGE / "repository"
INDEX = PACKAGE / "DEPENDENCY_INDEX.json"
MANIFEST = PACKAGE / "CORRECTED66_PREDYADIC_AND_P2_PLACE2_DEPENDENCY_CLOSURE_V1_SHA256SUMS.txt"
LINE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_gp_matrix(path: Path) -> list[list[int]]:
    """Parse the final GP matrix in a text artifact, ignoring whitespace."""
    text = path.read_text(encoding="utf-8").strip()
    if "]\n[" in text:
        text = "[" + text.rsplit("]\n[", 1)[1]
    assert text.startswith("[") and text.endswith("]"), path
    rows = [
        [int(entry.strip()) for entry in row.split(",")]
        for row in text[1:-1].split(";")
    ]
    return rows


def parse_package_manifest() -> dict[str, str]:
    rows: dict[str, str] = {}
    raw_rows = MANIFEST.read_text(encoding="utf-8").splitlines()
    assert raw_rows == sorted(raw_rows)
    for raw in raw_rows:
        match = LINE.fullmatch(raw)
        assert match, ("malformed package row", raw)
        expected, name = match.groups()
        path = Path(name)
        assert not path.is_absolute() and path.as_posix() == name
        assert all(part not in {"", ".", ".."} for part in path.parts)
        assert name != MANIFEST.name and name not in rows
        rows[name] = expected
    return rows


def regular_tree() -> set[str]:
    answer = set()
    for path in PACKAGE.rglob("*"):
        relative = path.relative_to(PACKAGE).as_posix()
        mode = path.lstat().st_mode
        assert not stat.S_ISLNK(mode), ("symlink", relative)
        if stat.S_ISREG(mode):
            answer.add(relative)
        elif not stat.S_ISDIR(mode):
            raise AssertionError(("special path", relative))
    return answer


def historical_target(manifest: Path, name: str, base: Path | None) -> Path:
    candidate = Path(name)
    if candidate.is_absolute():
        old = Path("/home/pcho/Documents/Codex/beal_357")
        return REPOSITORY / candidate.relative_to(old)
    if name.startswith("results/") or name.startswith("beal_357_"):
        return REPOSITORY / candidate
    if base is not None:
        return REPOSITORY / base / candidate
    return manifest.parent / candidate


def verify_historical_manifest(relative: str, base: str | None = None) -> int:
    manifest = REPOSITORY / relative
    count = 0
    for number, raw in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not raw or raw.startswith("#"):
            continue
        match = LINE.fullmatch(raw)
        assert match, (relative, number, "syntax")
        expected, name = match.groups()
        target = historical_target(manifest, name, Path(base) if base else None)
        assert target.is_file(), (relative, number, "missing", target)
        assert sha256(target) == expected, (relative, number, target)
        count += 1
    return count


def main() -> None:
    rows = parse_package_manifest()
    assert regular_tree() - {MANIFEST.name} == set(rows)
    for relative, expected in rows.items():
        assert sha256(PACKAGE / relative) == expected, relative

    index = json.loads(INDEX.read_text(encoding="utf-8"))
    assert index["schema"] == "corrected66_predyadic_and_p2_place2_dependency_closure_v1"
    assert len(index["nodes"]) == index["union_file_count"]
    for node in index["nodes"]:
        assert rows[node["path"]] == node["sha256"]
        assert (PACKAGE / node["path"]).stat().st_size == node["bytes"]
    for anchor in index["named_anchors"].values():
        assert sha256(PACKAGE / anchor["path"]) == anchor["sha256"]

    assert verify_historical_manifest(
        "results/2026-08-26_p29_global_dependency_replay/certificates/"
        "P29_CORRECTED_GLOBAL_DEPENDENCY_REPLAY_CHECKPOINT_V1_SHA256SUMS.txt"
    ) == 13
    assert verify_historical_manifest(
        "results/2026-08-26_corrected_quotient_coordinates_strict_adversarial_audit/"
        "INDEPENDENT_CORRECTED_QUOTIENT_COORDINATES_STRICT_ADVERSARIAL_AUDIT_V1_SHA256SUMS.txt"
    ) == 44
    assert verify_historical_manifest(
        "results/2026-08-26_p29_geometric_fibre_repair/manifests/"
        "P29_HNF22_GEOMETRIC_FIBRE_REPAIR_V1_SOURCE_SHA256SUMS.txt"
    ) == 20
    assert verify_historical_manifest(
        "results/2026-08-26_p29_geometric_fibre_repair/certificates/"
        "p29_hnf22_squareclass_packet_v1_package/manifests/"
        "P29_HNF22_GEOMETRIC_FIBRE_REPAIR_V1_FINAL_SHA256SUMS.txt",
        "results/2026-08-26_p29_geometric_fibre_repair/certificates/"
        "p29_hnf22_squareclass_packet_v1_package",
    ) == 67

    global_cert = json.loads((REPOSITORY / (
        "results/2026-08-26_p29_global_dependency_replay/certificates/"
        "p29_corrected_relaxed_global_intersection_v1.json"
    )).read_text())
    assert len(global_cert["input_hashes"]) == 222
    for name, expected in global_cert["input_hashes"].items():
        assert sha256(REPOSITORY / name) == expected
    assert global_cert["relaxed_without_p29"]["constraint_rank"] == 47
    assert global_cert["relaxed_without_p29"]["kernel_dimension"] == 19
    assert global_cert["after_p7_still_without_p29_or_p2"]["constraint_rank"] == 48
    assert global_cert["after_p7_still_without_p29_or_p2"]["kernel_dimension"] == 18
    first = REPOSITORY / (
        "results/2026-08-26_p29_global_dependency_replay/inputs/"
        "corrected_relaxed_basis_after_p7_without_p29_p2_v1.txt"
    )
    consumed = REPOSITORY / (
        "results/2026-08-26_p29_corrected_dyadic_replay/inputs/"
        "corrected_after_p7_basis_consumed_v1.txt"
    )
    first_matrix = parse_gp_matrix(first)
    assert len(first_matrix) == 18 and all(len(row) == 66 for row in first_matrix)
    assert first_matrix == parse_gp_matrix(consumed)
    assert sha256(first) == "1672118ec7db07a100811fd4cba97de962c03349e82029d9361a1a93144d8c07"
    assert sha256(consumed) == "842dc043bcc430a4a7a4961f173eb4e873aa6809bbccd935cc1b55ef781b77bf"
    downstream = (REPOSITORY / (
        "results/2026-08-26_p29_corrected_dyadic_replay/scripts/"
        "rebuild_corrected_dyadic_restrictions_v1.gp"
    )).read_text(encoding="utf-8")
    assert 'read("results/2026-08-26_p29_global_dependency_replay/inputs/' \
        'corrected_relaxed_basis_after_p7_without_p29_p2_v1.txt")' in downstream
    assert 'Str(Base,"/inputs/corrected_after_p7_basis_consumed_v1.txt")' in downstream
    assert "write(Paths[7],Rafter)" in downstream

    environment = {
        "PATH": "/usr/bin:/bin",
        "HOME": "/tmp",
        "LANG": "C",
        "LC_ALL": "C",
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    audit_script = REPOSITORY / (
        "results/2026-08-26_p29_global_dependency_replay/scripts/"
        "independent_audit_corrected_global_dependency_replay_v1.py"
    )
    replay = subprocess.run(
        ["/usr/bin/python3", "-B", str(audit_script)],
        cwd=REPOSITORY, env=environment, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        timeout=300, check=False,
    )
    assert replay.returncode == 0, replay.stdout
    reconstructed = json.loads(replay.stdout)
    assert reconstructed["status"] == "PASS"
    assert reconstructed["exact"]["stage_constraint_ranks"] == {
        "split": 43, "norm": 43, "nonsplit": 44,
        "p3": 46, "p5": 47, "p7": 48,
    }
    assert reconstructed["exact"]["fresh_basis_ranks"] == {"relaxed": 19, "after_p7": 18}

    p2 = json.loads((REPOSITORY / (
        "results/2026-08-25_dyadic_stopping/checkpoints/"
        "p2_place2_local_stopping_v1.json"
    )).read_text())
    independent = json.loads((REPOSITORY / (
        "results/2026-08-25_dyadic_stopping/certificates/"
        "independent_p2_place2_local_stopping_v1.json"
    )).read_text())
    assert p2["theorem"]["P2_fake_kernel_relation"] == [1, 1, -10]
    assert p2["theorem"]["P5_fake_kernel_relation"] == [1, 0, 2]
    assert p2["theorem"]["augmented_character_profile"] == [0, 1]
    assert p2["theorem"]["correction_rank_lower"] == 1
    assert p2["theorem"]["stopping_product"] == 16
    assert independent["reconstruction"]["fake_kernel_relation"] == [1, 0, 2]
    assert independent["reconstruction"]["augmented_profile_at_precision_140"] == [0, 1]

    theorem = (REPOSITORY / (
        "results/2026-08-25_dyadic_stopping/summaries/"
        "P2_PLACE2_AUGMENTED_LOCAL_STOPPING_THEOREM.md"
    )).read_text()
    assert "[mask, C0-bit, diagonal] = [1, 1, -10]" in theorem
    assert "[mask, C0-bit, diagonal] = [1, 0, 2]" in theorem
    assert "(0,1)" in theorem

    print(f"PACKAGE_TREE=PASS_{len(rows)}_MANIFESTED_FILES")
    print("CORRECTED66_DECLARED_INPUTS=PASS_222")
    print("PREDYADIC_RECONSTRUCTION=PASS_RANKS_43_43_44_46_47_48_DIMENSION_18")
    print("PREDYADIC_CONSUMED_COPY=PASS_EXACT_18X66_MATRIX_GP_RESERIALIZATION")
    print("P2_PLACE2_NONZERO_CORRECTION=PASS_RELATIONS_AND_PROFILE_0_1")
    print("CLAIM_BOUNDARY=DISPLAYED_66_SPACE_AND_SECOND_DYADIC_LOCAL_THEOREM")


if __name__ == "__main__":
    main()
