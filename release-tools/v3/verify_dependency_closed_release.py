#!/usr/bin/env python3
"""Verify the dependency-closed primitive (3,5,7) research release."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time


RELEASE = Path(__file__).resolve().parents[1]
REPOSITORY = RELEASE / "repository"
INDEX = RELEASE / "inputs/DEPENDENCY_CLOSURE_INDEX_V2.json"
BASE_INDEX = RELEASE / "inputs/BASE_EVIDENCE_MANIFEST_INDEX_V1.json"
ROOT_MANIFEST = RELEASE / "manifests/PRIMITIVE_357_DEPENDENCY_CLOSED_RELEASE_V2_SHA256SUMS.txt"
PORTABLE = RELEASE / "scripts/portable_python.py"
SECTOR_INDEX = RELEASE / "inputs/SECTOR_REPLAY_INDEX_V2.json"
UPSTREAM = RELEASE / "third_party/GFE-5p3"
ROW = re.compile(r"([0-9a-f]{64})  ([^\x00\r\n]+)")
ORIGINAL_ROOT = Path("/home/pcho/Documents/Codex/beal_357")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or not path.parts or ".." in path.parts:
        raise AssertionError(("unsafe relative path", value))
    return path


def parse_manifest(path: Path, sorted_required: bool = False) -> list[tuple[str, str]]:
    rows = []
    seen = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        match = ROW.fullmatch(line)
        if not match:
            raise AssertionError(("malformed manifest row", path, line))
        digest, relative = match.groups()
        safe_relative(relative)
        if relative in seen:
            raise AssertionError(("duplicate manifest row", path, relative))
        seen.add(relative)
        rows.append((digest, relative))
    if sorted_required and [relative for _, relative in rows] != sorted(seen):
        raise AssertionError(("unsorted manifest", path))
    return rows


def verify_root_manifest(preseal: bool) -> set[Path]:
    if preseal:
        return set()
    expected = {ROOT_MANIFEST.resolve()}
    for digest, relative in parse_manifest(ROOT_MANIFEST, sorted_required=True):
        target = RELEASE / safe_relative(relative)
        if not target.is_file() or target.is_symlink() or sha256(target) != digest:
            raise AssertionError(("release manifest mismatch", relative))
        expected.add(target.resolve())
    actual = {path.resolve() for path in RELEASE.rglob("*") if path.is_file()}
    if any(path.is_symlink() for path in RELEASE.rglob("*")):
        raise AssertionError("release contains a symbolic link")
    if actual != expected:
        raise AssertionError(("release exact-set mismatch", actual - expected, expected - actual))
    return expected


def resolve_historical_row(manifest: Path, digest: str, relative: str, dialect: str) -> Path:
    row = safe_relative(relative)
    if dialect == "repository":
        target = REPOSITORY / row
    elif dialect == "package":
        target = manifest.parents[1] / row
    else:
        raise AssertionError(("unknown manifest dialect", dialect))
    if not target.is_file() or target.is_symlink() or sha256(target) != digest:
        raise AssertionError(("historical payload mismatch", manifest, relative))
    return target.resolve()


def verify_repository() -> tuple[int, int]:
    base = json.loads(BASE_INDEX.read_text(encoding="utf-8"))
    closure = json.loads(INDEX.read_text(encoding="utf-8"))
    expected: set[Path] = set()
    historical_rows = 0
    for entry in base["manifests"]:
        manifest = REPOSITORY / safe_relative(entry["path"])
        if sha256(manifest) != entry["sha256"]:
            raise AssertionError(("base manifest identity", entry["path"]))
        rows = parse_manifest(manifest)
        if len(rows) != entry["rows"]:
            raise AssertionError(("base manifest row count", entry["path"]))
        expected.add(manifest.resolve())
        for digest, relative in rows:
            expected.add(resolve_historical_row(manifest, digest, relative, entry["base"]))
            historical_rows += 1
    for entry in base["geometry_supplement"]:
        target = REPOSITORY / safe_relative(entry["path"])
        if not target.is_file() or target.is_symlink() or sha256(target) != entry["sha256"]:
            raise AssertionError(("base geometry identity", entry["path"]))
        expected.add(target.resolve())

    for entry in closure["added_files"]:
        target = REPOSITORY / safe_relative(entry["path"])
        if not target.is_file() or target.is_symlink() or sha256(target) != entry["sha256"]:
            raise AssertionError(("dependency addition mismatch", entry["path"]))
        expected.add(target.resolve())
    actual = {path.resolve() for path in REPOSITORY.rglob("*") if path.is_file()}
    if any(path.is_symlink() for path in REPOSITORY.rglob("*")):
        raise AssertionError("repository contains a symbolic link")
    if actual != expected:
        raise AssertionError(("repository exact-set mismatch", actual - expected, expected - actual))
    if len(actual) != closure["repository_file_count"]:
        raise AssertionError("repository file count mismatch")
    return len(actual), historical_rows


def verify_composition_interfaces() -> None:
    graph_path = REPOSITORY / (
        "results/2026-09-10_complete_primitive_357_proof_v3/"
        "inputs/complete_primitive_357_proof_graph_v3.json"
    )
    certificate_path = REPOSITORY / (
        "results/2026-09-10_complete_primitive_357_proof_v3/"
        "certificates/COMPLETE_PRIMITIVE_357_PROOF_CERTIFICATE_V3.json"
    )
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    sectors = {tuple(row) for row in graph["exhaustive_decomposition"]["global_factor_degree_sectors"]}
    if sectors != {(7,), (1, 6), (2, 5), (3, 4)}:
        raise AssertionError("four-sector decomposition mismatch")
    if not graph["claim_boundary"]["all_global_sectors_empty"]:
        raise AssertionError("proof graph leaves a sector open")
    dependencies = {row["id"]: row["sha256"] for row in graph["authenticated_dependencies"]}
    if certificate["authenticated_dependencies"] != dependencies:
        raise AssertionError("composition dependency mismatch")
    for row in graph["authenticated_dependencies"]:
        target = REPOSITORY / safe_relative(row["manifest"])
        if sha256(target) != row["sha256"]:
            raise AssertionError(("composition dependency identity", row["id"]))


def verify_upstream_snapshot() -> int:
    origin = json.loads((UPSTREAM / "UPSTREAM_ORIGIN.json").read_text())
    assert origin["commit"] == "e88f914c577ab6cf9a45e5cdd82c1993477fb423"
    manifest = UPSTREAM / "UPSTREAM_SHA256SUMS.txt"
    expected = {manifest.resolve()}
    for digest, relative in parse_manifest(manifest, sorted_required=True):
        target = UPSTREAM / safe_relative(relative)
        if not target.is_file() or target.is_symlink() or sha256(target) != digest:
            raise AssertionError(("upstream snapshot mismatch", relative))
        expected.add(target.resolve())
    actual = {path.resolve() for path in UPSTREAM.rglob("*") if path.is_file()}
    if actual != expected:
        raise AssertionError(("upstream snapshot exact-set mismatch", actual ^ expected))
    return len(actual)


def verify_sector_index() -> None:
    index = json.loads(SECTOR_INDEX.read_text(encoding="utf-8"))
    assert index["schema"] == "primitive_357_sector_replay_index_v2"
    assert index["original_workspace_must_be_absent"] is True
    indexed = [row["id"] for row in index["replays"]]
    actual = [row[0] for row in replay_commands()]
    assert indexed == actual
    for row in index["replays"]:
        base = RELEASE if row.get("base") == "release" else REPOSITORY
        source = base / safe_relative(row["source"])
        assert source.is_file() and not source.is_symlink()
        assert sha256(source) == row["sha256"]


def clean_env() -> dict[str, str]:
    environment = {
        "PATH": "/usr/bin:/bin",
        "HOME": "/tmp",
        "DOT_SAGE": "/tmp/primitive357-dependency-closed-dot-sage",
        "TMPDIR": "/tmp",
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONINTMAXSTRDIGITS": "0",
        "BEAL357_REPOSITORY_ROOT": str(REPOSITORY),
        "BEAL357_SAGE_PYTHON": os.environ.get(
            "BEAL357_SAGE_PYTHON",
            "/tmp/beal357-p23-sage-runtime-v1/env/bin/python",
        ),
        "BEAL357_DOT_SAGE": "/tmp/primitive357-dependency-closed-dot-sage",
        "BEAL357_FLINT_PREFIX": os.environ.get(
            "BEAL357_FLINT_PREFIX", "/tmp/beal357-p23-sage-runtime-v1/env"
        ),
    }
    if os.environ.get("PYTHONPATH"):
        environment["PYTHONPATH"] = os.environ["PYTHONPATH"]
    return environment


def replay_commands() -> list[tuple[str, list[str], str, int]]:
    prefix = [str(PORTABLE), "-B"]
    return [
        (
            "signed-global-algebra",
            prefix + [str(REPOSITORY / "results/2026-09-09_signed_global_algebra_superselection_audit_v8/scripts/verify_signed_global_algebra_superselection_audit_v8.py")],
            "PASS_SIGNED_GLOBAL_ALGEBRA_SUPERSELECTION_AUDIT_V8",
            600,
        ),
        (
            "rational-factor-sector",
            prefix + [str(REPOSITORY / "results/2026-09-10_rational_factor_proposition_6_1_composition_v2/scripts/verify_rational_factor_proposition_6_1_checkpoint_v2.py")],
            "PASS_RATIONAL_FACTOR_PROPOSITION_6_1_CHECKPOINT_REPLAY_V2_PROJECTIVE_BOUNDARY_REPAIRED",
            1800,
        ),
        (
            "quadratic-factor-router",
            prefix + [str(REPOSITORY / "results/2026-09-09_quadratic_factor_router_2_5_v1/scripts/verify_quadratic_factor_router_2_5.py")],
            "QUADRATIC_FACTOR_ROUTER_2_5=PASS_EXACT_DATABASE_FREE",
            900,
        ),
        (
            "quadratic-factor-terminal",
            prefix + [str(REPOSITORY / "results/2026-09-09_quadratic_factor_2_5_reconstruction_v1/scripts/verify_quadratic_factor_2_5_reconstruction.py")],
            "VERIFY_STATUS=PASS_QUADRATIC_FACTOR_2_5_RECONSTRUCTION",
            1800,
        ),
        (
            "cubic-quartic-section7-sector",
            prefix + [str(REPOSITORY / "results/2026-09-10_section7_proposition_7_1_closure_v2_model_intrinsic/scripts/verify_section7_proposition_7_1_closure_v2.py")],
            "SECTION7_PROPOSITION_7_1_CLOSURE_V2=PASS_ROUTER_LEMMAS_7_3_7_4_MODEL_INTRINSIC_7_5_AND_TERMINAL",
            12000,
        ),
        (
            "rational-parameter-sieve-and-lifts",
            prefix + [str(REPOSITORY / "results/2026-09-08_mixed_rational_t_signature_357_closure_v1/scripts/verify_mixed_rational_t_signature_357_closure_v1.py")],
            "PASS_MIXED_RATIONAL_T_SIGNATURE_357_CLOSURE_EXACT_FIVE_BRANCH_POINTS",
            7200,
        ),
        (
            "irreducible-septic-sector",
            prefix + [str(REPOSITORY / "results/2026-09-10_irreducible_degree7_sector_closure_v1/scripts/verify_irreducible_degree7_sector_closure_v1.py")],
            "IRREDUCIBLE_DEGREE7_SECTOR_CLOSURE=PASS_EXACT_PUTZ_SEVEN_FIELDS_PURE_RATIONAL_PARAMETER_AND_EXCEPTIONAL_Q29",
            18000,
        ),
        (
            "hilbert-hecke-filter-coverage",
            [sys.executable, "-B", str(RELEASE / "scripts/verify_hilbert_hecke_filter_coverage.py")],
            "PASS_HILBERT_HECKE_FILTER_AUDIT_WITH_REQUIRED_ELL131_CONSERVATIVE_REPAIR",
            120,
        ),
        (
            "hilbert-hecke-ambient-coverage",
            [sys.executable, "-B", str(RELEASE / "scripts/verify_hilbert_hecke_ambient_coverage.py")],
            "PASS_HILBERT_HECKE_CONSERVATIVE_FILTERED_AMBIENT_COVERAGE_NO_NEWSPACE_SUBTRACTION",
            1800,
        ),
        (
            "putz-pvt-interface",
            prefix + [str(REPOSITORY / "results/2026-09-10_pvt_putz_interface_audit_v2/scripts/verify_pvt_putz_interface_v2_package.py")],
            "PACKAGE_REPLAY=PASS_PVT_PUTZ_INTERFACE_AUDIT_V2",
            3600,
        ),
    ]


def run_sector_replays() -> None:
    for label, command, marker, timeout in replay_commands():
        started = time.monotonic()
        environment = clean_env()
        minimum_child_timeout = ""
        if label == "cubic-quartic-section7-sector":
            minimum_child_timeout = "1800"
            environment["BEAL357_MINIMUM_CHILD_TIMEOUT"] = minimum_child_timeout
        completed = subprocess.run(
            command,
            cwd=REPOSITORY,
            env=environment,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
        )
        elapsed = time.monotonic() - started
        print(f"===== BEGIN {label} =====")
        print("COMMAND=" + " ".join(command))
        if minimum_child_timeout:
            print("PORTABLE_MINIMUM_CHILD_TIMEOUT=" + minimum_child_timeout)
        print(f"EXIT={completed.returncode} WALL_SECONDS={elapsed:.6f}")
        print(completed.stdout, end="" if completed.stdout.endswith("\n") else "\n")
        print(f"===== END {label} =====")
        if completed.returncode != 0 or marker not in completed.stdout:
            raise AssertionError((label, completed.returncode, marker))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preseal", action="store_true")
    parser.add_argument("--run-sector-replays", action="store_true")
    parser.add_argument("--require-original-workspace-absent", action="store_true")
    args = parser.parse_args()
    if args.require_original_workspace_absent:
        if ORIGINAL_ROOT.exists():
            raise AssertionError("original workspace is visible inside clean replay")
        print("ORIGINAL_WORKSPACE_PATH_VISIBLE=0")
    verify_root_manifest(args.preseal)
    files, rows = verify_repository()
    verify_composition_interfaces()
    upstream_files = verify_upstream_snapshot()
    verify_sector_index()
    if args.run_sector_replays:
        run_sector_replays()
    print(
        "PRIMITIVE_357_DEPENDENCY_CLOSED_RELEASE=PASS "
        f"REPOSITORY_FILES={files} HISTORICAL_MANIFEST_ROWS={rows} "
        f"UPSTREAM_FILES={upstream_files} "
        f"SECTOR_REPLAYS={int(args.run_sector_replays)} PRESEAL={int(args.preseal)}"
    )


if __name__ == "__main__":
    main()
