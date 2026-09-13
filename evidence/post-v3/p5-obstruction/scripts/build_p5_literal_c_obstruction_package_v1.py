#!/usr/bin/env python3
"""Copy the exact declared closure and build a deterministic release ZIP."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import stat
import zipfile


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[1]
REPOSITORY = PACKAGE / "repository"
INDEX = PACKAGE / "DECLARED_DEPENDENCY_INDEX.json"
MANIFEST = PACKAGE / "P5_LITERAL_C_OBSTRUCTION_DEPENDENCY_CLOSURE_V1_SHA256SUMS.txt"
ARCHIVE = PACKAGE.parent / (PACKAGE.name + ".zip")
ARCHIVE_SHA = ARCHIVE.with_suffix(ARCHIVE.suffix + ".sha256")
OLD_ROOT = Path("/home/pcho/Documents/Codex/beal_357")

CLOSURE_AUDITOR = Path(
    "results/2026-08-26_literal_c_a26_p5_conditional_rejection_independent_audit/"
    "scripts/audit_declared_hash_closure_v1.py"
)
COHERENT_SOURCE_MANIFEST = Path(
    "results/2026-08-25_source_class_bridge_resume/summaries/"
    "P7_ORBIT42_56_COHERENT_COCYCLE_V4_RESUME1_FROZEN_SHA256SUMS.txt"
)
COHERENT_OUTPUT_MANIFEST = Path(
    "results/2026-08-25_source_class_bridge_resume/certificates/"
    "p7_orbit42_56_coherent_cocycle_v4_resume1.SHA256SUMS.txt"
)
PARTITION_MANIFEST = Path(
    "results/2026-08-26_literal_c_a26_p7_partition_gauge/"
    "LITERAL_C_P7_PARTITION_GAUGE_THEOREM_V1_SHA256SUMS.txt"
)
TRUE_LIFT_MANIFEST = Path(
    "results/2026-08-26_literal_c_a26_true_lift_gate/"
    "LITERAL_C_BPS_A26_TRUE_LIFT_GATE_V1_SHA256SUMS.txt"
)
REPLAY_SUPPORT = (
    Path("results/2026-08-21_descent_galois/scripts/certify_bad_decomposition_subgroups.py"),
    Path("results/2026-08-21_descent_galois/scripts/certify_bad_local_rvee_corrections.py"),
)
LINE = re.compile(r"^([0-9a-f]{64})  (.+)$")


def sha256(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            result.update(block)
    return result.hexdigest()


def relative_to_root(path: Path) -> Path:
    path = path.resolve()
    try:
        return path.relative_to(ROOT.resolve())
    except ValueError:
        return path.relative_to(OLD_ROOT)


def parse_manifest(path: Path) -> list[tuple[str, Path]]:
    answer: list[tuple[str, Path]] = []
    for number, raw in enumerate((ROOT / path).read_text().splitlines(), 1):
        match = LINE.fullmatch(raw)
        if not match:
            raise AssertionError((path, number, "syntax"))
        expected, name = match.groups()
        candidate = Path(name)
        if candidate.is_absolute():
            source = candidate
        elif name.startswith("results/") or name.startswith("beal_357_"):
            source = ROOT / candidate
        else:
            source = ROOT / path.parent / candidate
        source = source.resolve()
        if not source.is_file() or sha256(source) != expected:
            raise AssertionError((path, number, source, expected))
        answer.append((expected, source))
    return answer


def declared_closure() -> tuple[dict[Path, str], dict[str, int]]:
    module_path = (ROOT / CLOSURE_AUDITOR).resolve()
    spec = importlib.util.spec_from_file_location("p5_declared_closure", module_path)
    if spec is None or spec.loader is None:
        raise AssertionError("cannot import declared closure auditor")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.main()
    files: dict[Path, str] = {}
    categories: dict[str, int] = {}
    for category, path, expected in module.EDGES:
        relative = relative_to_root(path)
        previous = files.setdefault(relative, expected)
        if previous != expected:
            raise AssertionError((relative, previous, expected))
        categories[category] = categories.get(category, 0) + 1
    if len(files) != 93:
        raise AssertionError(("declared unique closure", len(files)))
    return files, categories


def add_file(files: dict[Path, str], source: Path) -> None:
    source = source.resolve()
    relative = relative_to_root(source)
    expected = sha256(source)
    previous = files.setdefault(relative, expected)
    if previous != expected:
        raise AssertionError((relative, previous, expected))


def collect() -> tuple[dict[Path, str], dict[str, int], dict[str, int]]:
    files, categories = declared_closure()
    manifest_counts = {}
    for manifest in (COHERENT_SOURCE_MANIFEST, COHERENT_OUTPUT_MANIFEST):
        rows = parse_manifest(manifest)
        manifest_counts[manifest.as_posix()] = len(rows)
        for _, source in rows:
            add_file(files, source)
        add_file(files, ROOT / manifest)
    for manifest in (PARTITION_MANIFEST, TRUE_LIFT_MANIFEST):
        add_file(files, ROOT / manifest)
    # The frozen declared-hash auditor authenticates the target-character
    # replay script but did not recurse into its two import-only modules.
    # Carry them explicitly so the arithmetic replay really is portable.
    for support in REPLAY_SUPPORT:
        add_file(files, ROOT / support)
    for directory in (
        ROOT / "results/2026-08-26_literal_c_a26_residual_bits",
        ROOT / "results/2026-08-26_literal_c_a26_p5_conditional_rejection_independent_audit",
    ):
        for source in directory.rglob("*"):
            if (source.is_file() and "__pycache__" not in source.parts
                    and source.suffix not in {".pyc", ".pyo"}):
                add_file(files, source)
    return files, categories, manifest_counts


def copy_files(files: dict[Path, str]) -> None:
    REPOSITORY.mkdir(parents=True, exist_ok=True)
    for relative, expected in sorted(files.items(), key=lambda item: item[0].as_posix()):
        source = ROOT / relative
        if sha256(source) != expected:
            raise AssertionError((relative, expected, sha256(source)))
        target = REPOSITORY / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)


def role(relative: str) -> str:
    if relative.endswith("p7_target42_tau_relative_root_v1.bin"):
        return "target42-root"
    if "degree42_contact" in relative or "degree42_horner" in relative or "degree42_line_contact" in relative:
        return "contact-checkpoint"
    if "p7_orbit42_56_coherent" in relative or "p7_degree56_completion" in relative:
        return "coherent-cocycle"
    if "p5_literal_c" in relative or "p5_target_character" in relative:
        return "p5-obstruction"
    if "partition_gauge" in relative:
        return "partition-gauge"
    if relative.endswith("certify_bad_decomposition_subgroups.py") or relative.endswith("certify_bad_local_rvee_corrections.py"):
        return "target-character-replay-support"
    if "true_lift_gate" in relative:
        return "A26-gate"
    return "declared-dependency"


def build_index(files: dict[Path, str], categories: dict[str, int], manifest_counts: dict[str, int]) -> None:
    nodes = []
    for relative, expected in sorted(files.items(), key=lambda item: item[0].as_posix()):
        packaged = REPOSITORY / relative
        nodes.append({
            "path": "repository/" + relative.as_posix(),
            "sha256": expected,
            "bytes": packaged.stat().st_size,
            "role": role(relative.as_posix()),
        })
    payload = {
        "schema": "p5_literal_c_obstruction_dependency_closure_v1",
        "scope": "exact checkpoint-to-obstruction closure for carrier signs and quotient coordinates",
        "named_anchors": {
            "p5_manifest": {
                "path": "repository/results/2026-08-26_literal_c_a26_residual_bits/certificates/p5_literal_c_a26_candidate_late_v2_manifest.json",
                "sha256": "119a96d68bb75a9b90ecbd09f353887f8c490c397c973aef94195acce3236db0",
            },
            "coherent_cocycle": {
                "path": "repository/results/2026-08-25_source_class_bridge_resume/certificates/p7_orbit42_56_coherent_cocycle_v4_resume1.json",
                "sha256": "93aa36c5595f7d735591ccba1a8b8b759f2d4b1679ba356cace426befaaffb64",
            },
            "target42_root": {
                "path": "repository/results/2026-08-25_source_class_bridge_resume/inputs/p7_target42_tau_relative_root_v1.bin",
                "sha256": "9de7000696dbe254b0bc06bf47e21e9f0f9ce846809bbc1d25a32498ec011acd",
            },
            "contact_cross_matrix": {
                "path": "repository/results/2026-08-22_discovery_engine/checkpoints/degree42_contact_cross_matrices_v6.bin",
                "sha256": "ee5a608769d29dd88cfcff4800609996df745c7fb736b1a259c808570f80b9fa",
            },
        },
        "declared_hash_edges": 119,
        "declared_unique_targets": 93,
        "portable_replay_support_files_beyond_declared_hash_edges": [
            "repository/" + path.as_posix() for path in REPLAY_SUPPORT
        ],
        "declared_edge_categories": categories,
        "coherent_manifest_rows": manifest_counts,
        "union_file_count": len(files),
        "nodes": nodes,
        "arithmetic_result": {
            "carrier_signs_root_00": [-1, 1, -1],
            "carrier_bits_root_00": [1, 0, 1],
            "coordinate_root_00": [1, 0],
            "carrier_bits_root_11": [0, 1, 0],
            "coordinate_root_11": [0, 1],
            "both_nonzero": True,
        },
        "claim_boundary": "conditional A.26 implication only; no broader Selmer or Diophantine conclusion",
        "software": {"pari_gp": "2.15.4", "python": "3.12"},
    }
    INDEX.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def package_files() -> list[Path]:
    result = []
    for path in PACKAGE.rglob("*"):
        mode = path.lstat().st_mode
        if stat.S_ISLNK(mode):
            raise AssertionError(("symlink", path))
        if stat.S_ISREG(mode):
            result.append(path)
        elif not stat.S_ISDIR(mode):
            raise AssertionError(("special path", path))
    return sorted(result, key=lambda path: path.relative_to(PACKAGE).as_posix())


def build_manifest() -> None:
    rows = [
        f"{sha256(path)}  {path.relative_to(PACKAGE).as_posix()}"
        for path in package_files() if path != MANIFEST
    ]
    MANIFEST.write_text("\n".join(sorted(rows)) + "\n")


def build_archive() -> None:
    if ARCHIVE.exists():
        ARCHIVE.unlink()
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as target:
        for path in package_files():
            name = f"{PACKAGE.name}/{path.relative_to(PACKAGE).as_posix()}"
            info = zipfile.ZipInfo(name)
            info.date_time = (2026, 9, 13, 12, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 & 0xFFFF) << 16
            target.writestr(info, path.read_bytes(), compresslevel=9)
    ARCHIVE_SHA.write_text(f"{sha256(ARCHIVE)}  {ARCHIVE.name}\n")


def main() -> None:
    files, categories, counts = collect()
    copy_files(files)
    build_index(files, categories, counts)
    build_manifest()
    build_archive()
    print(f"DEPENDENCY_UNION_FILES={len(files)}")
    print(f"PACKAGE_REGULAR_FILES={len(package_files())}")
    print(f"ARCHIVE_SHA256={sha256(ARCHIVE)}")


if __name__ == "__main__":
    main()
