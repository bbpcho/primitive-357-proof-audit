#!/usr/bin/env python3
"""Build the exact pre-dyadic and second-dyadic dependency closure."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import shutil
import stat
import zipfile


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[1]
REPOSITORY = PACKAGE / "repository"
INDEX = PACKAGE / "DEPENDENCY_INDEX.json"
MANIFEST = PACKAGE / "CORRECTED66_PREDYADIC_AND_P2_PLACE2_DEPENDENCY_CLOSURE_V1_SHA256SUMS.txt"
ARCHIVE = PACKAGE.parent / f"{PACKAGE.name}.zip"
ARCHIVE_SHA = ARCHIVE.with_suffix(".zip.sha256")
LINE = re.compile(r"^([0-9a-f]{64})  (.+)$")

GLOBAL = Path("results/2026-08-26_p29_global_dependency_replay")
HNF = Path("results/2026-08-26_p29_geometric_fibre_repair")
HNF_PACKET = HNF / "certificates/p29_hnf22_squareclass_packet_v1_package"
DYADIC = Path("results/2026-08-25_dyadic_stopping")
STRICT66 = Path("results/2026-08-26_corrected_quotient_coordinates_strict_adversarial_audit")
GLOBAL_CERT = GLOBAL / "certificates/p29_corrected_relaxed_global_intersection_v1.json"
STRICT66_MANIFEST = STRICT66 / "INDEPENDENT_CORRECTED_QUOTIENT_COORDINATES_STRICT_ADVERSARIAL_AUDIT_V1_SHA256SUMS.txt"
HNF_SOURCE_MANIFEST = HNF / "manifests/P29_HNF22_GEOMETRIC_FIBRE_REPAIR_V1_SOURCE_SHA256SUMS.txt"

SPLIT_PRIMES = [
    19163, 23431, 29059, 38189, 96989, 114073,
    117329, 120899, 128291, 147457, 169493, 177601,
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def add(files: dict[Path, str], relative: Path, expected: str | None = None) -> None:
    if relative.is_absolute() or ".." in relative.parts:
        raise AssertionError(("unsafe path", relative))
    source = ROOT / relative
    if not source.is_file() or source.is_symlink():
        raise AssertionError(("missing/nonregular", relative))
    actual = sha256(source)
    if expected is not None and actual != expected:
        raise AssertionError((relative, expected, actual))
    previous = files.setdefault(relative, actual)
    if previous != actual:
        raise AssertionError(("digest conflict", relative, previous, actual))


def add_tree(files: dict[Path, str], relative: Path) -> None:
    for source in (ROOT / relative).rglob("*"):
        if source.is_symlink():
            raise AssertionError(("symlink", source))
        if not source.is_file() or "__pycache__" in source.parts or source.suffix in {".pyc", ".pyo"}:
            continue
        add(files, source.relative_to(ROOT))


def add_manifest(files: dict[Path, str], relative: Path, base: Path | None = None) -> int:
    manifest = ROOT / relative
    count = 0
    for number, raw in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not raw or raw.startswith("#"):
            continue
        match = LINE.fullmatch(raw)
        if not match:
            raise AssertionError((relative, number, "syntax", raw))
        expected, name = match.groups()
        candidate = Path(name)
        if candidate.is_absolute():
            candidate = candidate.relative_to(ROOT)
        elif name.startswith("results/") or name.startswith("beal_357_"):
            pass
        elif base is not None:
            candidate = base / candidate
        else:
            candidate = relative.parent / candidate
        add(files, candidate, expected)
        count += 1
    add(files, relative)
    return count


def collect() -> tuple[dict[Path, str], dict[str, int]]:
    files: dict[Path, str] = {}
    counts: dict[str, int] = {}

    # Producer outputs, source, certificates, and human audit records.
    for directory in (GLOBAL, HNF, DYADIC, STRICT66):
        add_tree(files, directory)

    # Every input consumed by the exact 66-column intersection is named and
    # hashed in the frozen producer certificate.
    certificate = json.loads((ROOT / GLOBAL_CERT).read_text(encoding="utf-8"))
    for name, expected in certificate["input_hashes"].items():
        add(files, Path(name), expected)
    counts["global_intersection_declared_inputs"] = len(certificate["input_hashes"])

    # Inputs needed one stage earlier to reconstruct the corrected columns.
    rebuild_extras = [
        Path("beal_357_spark_handover_2026-08-20/checkpoint/p7_f42_bitangent_bnf.bin"),
        Path("results/2026-08-20_descent_support/checkpoints/tower_exact.bin"),
        Path("results/2026-08-21_descent_galois/checkpoints/local_condition_3.bin"),
        Path("results/2026-08-21_descent_galois/checkpoints/local_condition_5.bin"),
        Path("results/2026-08-21_descent_galois/checkpoints/local_condition_7_v2.bin"),
    ]
    rebuild_extras.extend(
        Path(f"results/2026-08-21_descent_galois/inputs/split_prime_geometry_homogeneous_{prime}_v1.json")
        for prime in SPLIT_PRIMES
    )
    for relative in rebuild_extras:
        add(files, relative)

    counts["hnf_source_manifest_rows"] = add_manifest(files, HNF_SOURCE_MANIFEST)
    counts["strict_66_witness_manifest_rows"] = add_manifest(files, STRICT66_MANIFEST)

    # The second-dyadic finite-module program imports these two source modules.
    for relative in (
        Path("results/2026-08-21_descent_galois/scripts/certify_p2_local_subgroups.py"),
        Path("results/2026-08-25_source_class_bridge_resume/scripts/certify_p7_full315_completion_attack_v1.py"),
        Path("results/2026-08-26_p29_corrected_dyadic_replay/scripts/rebuild_corrected_dyadic_restrictions_v1.gp"),
    ):
        add(files, relative)

    # Bind every input named by the production second-dyadic certificate.
    p2 = json.loads((ROOT / DYADIC / "checkpoints/p2_place2_local_stopping_v1.json").read_text())
    for name, expected in p2["hashes"].items():
        add(files, Path(name), expected)
    counts["p2_place2_declared_inputs"] = len(p2["hashes"])
    return files, counts


def copy_files(files: dict[Path, str]) -> None:
    if REPOSITORY.exists():
        shutil.rmtree(REPOSITORY)
    for relative, expected in sorted(files.items(), key=lambda item: item[0].as_posix()):
        source = ROOT / relative
        if sha256(source) != expected:
            raise AssertionError((relative, "changed before copy"))
        target = REPOSITORY / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)


def role(path: str) -> str:
    if "corrected_relaxed_basis_after_p7_without_p29_p2" in path or "corrected_after_p7_basis_consumed" in path:
        return "named-18-dimensional-anchor"
    if "corrected_displayed_norm_matrix" in path or "displayed_norm_matrix_hnf22" in path:
        return "corrected-norm-condition"
    if "corrected_split_global" in path or "corrected_nonsplit_global" in path or "corrected_local_global" in path:
        return "corrected-global-local-map"
    if "local_allowed" in path or "local_image_split" in path or "nonsplit_local_augmented" in path:
        return "local-allowed-subspace"
    if "p29_hnf22" in path:
        return "corrected-66-squareclass-witness"
    if "p2_place2" in path or "mask11_augmented" in path or "full315_target_characters" in path:
        return "second-dyadic-nonzero-correction"
    if "degree42_" in path or "p7_target_tetrad_orbit" in path:
        return "second-dyadic-carrier-input"
    return "transitive-input-or-audit"


def build_index(files: dict[Path, str], counts: dict[str, int]) -> None:
    nodes = []
    for relative, expected in sorted(files.items(), key=lambda item: item[0].as_posix()):
        target = REPOSITORY / relative
        nodes.append({
            "path": "repository/" + relative.as_posix(),
            "sha256": expected,
            "bytes": target.stat().st_size,
            "role": role(relative.as_posix()),
        })
    payload = {
        "schema": "corrected66_predyadic_and_p2_place2_dependency_closure_v1",
        "scope": "construction of the corrected pre-dyadic 18-space and the nonzero second-dyadic fake-kernel correction",
        "named_anchors": {
            "global_18_basis": {
                "path": "repository/results/2026-08-26_p29_global_dependency_replay/inputs/corrected_relaxed_basis_after_p7_without_p29_p2_v1.txt",
                "sha256": "1672118ec7db07a100811fd4cba97de962c03349e82029d9361a1a93144d8c07",
            },
            "dyadic_consumed_copy": {
                "path": "repository/results/2026-08-26_p29_corrected_dyadic_replay/inputs/corrected_after_p7_basis_consumed_v1.txt",
                "sha256": "842dc043bcc430a4a7a4961f173eb4e873aa6809bbccd935cc1b55ef781b77bf",
            },
            "global_intersection_certificate": {
                "path": "repository/results/2026-08-26_p29_global_dependency_replay/certificates/p29_corrected_relaxed_global_intersection_v1.json",
                "sha256": "3771c4e499644de48f5dc94e3558269edee409caa2fd17ba81a3d0984cbaa085",
            },
            "second_dyadic_checkpoint": {
                "path": "repository/results/2026-08-25_dyadic_stopping/checkpoints/p2_place2_local_stopping_v1.json",
                "sha256": "77950ca3d5f2105c9b03531e662f6a939dbfdba0337c0a9d494d3d5e24f64040",
            },
            "second_dyadic_independent": {
                "path": "repository/results/2026-08-25_dyadic_stopping/certificates/independent_p2_place2_local_stopping_v1.json",
                "sha256": "b185b788bb52c966a647e70c76f772fdd23f583b0c6b09ecaca04f9402212cd9",
            },
            "second_dyadic_theorem": {
                "path": "repository/results/2026-08-25_dyadic_stopping/summaries/P2_PLACE2_AUGMENTED_LOCAL_STOPPING_THEOREM.md",
                "sha256": "3268de83b18fc6cbddd9988c053bf6443c2eb9f95375b4cba6d5ceacef5cd769",
                "relevant_lines": [112, 171],
            },
        },
        "construction": {
            "displayed_squareclass_coordinates": 66,
            "basis": "28 ordinary units plus 38 principal support-prime generators; first 62 inherited, last 4 replaced by HNF-22 p=29 generators",
            "pre_dyadic_conditions_in_order": [
                "12 split-good local conditions",
                "corrected 7-row norm condition",
                "57 admitted nonsplit-good local conditions",
                "p=3 allowed subspace",
                "p=5 allowed subspace",
                "p=7 allowed subspace",
            ],
            "constraint_ranks": [43, 43, 44, 46, 47, 48],
            "kernel_dimensions": [23, 23, 22, 20, 19, 18],
            "dyadic_conditions_excluded_from_named_18_space": True,
            "dyadic_consumed_serialization": {
                "relation": "the exact same 18-by-66 integer matrix",
                "byte_identity": False,
                "reason": "the downstream PARI/GP producer reads the upstream matrix and writes it with GP whitespace serialization",
                "source_gate": "rebuild_corrected_dyadic_restrictions_v1.gp reads the upstream path and writes Rafter to Paths[7]",
            },
        },
        "second_dyadic_result": {
            "production_relation": [1, 1, -10],
            "independent_relation": [1, 0, 2],
            "production_and_independent_correction_profile": [0, 1],
            "nonzero_correction_rank_lower_bound": 1,
            "local_stopping_tuple": [4, 2, 3, 1, 1],
        },
        "counts": counts,
        "union_file_count": len(files),
        "nodes": nodes,
        "software": {"python": "3.12", "pari_gp": "2.15.4"},
        "claim_boundary": "exact on the frozen displayed 66-generator and second-dyadic local inputs; theoretical BPS identifications remain imported as stated in the historical reports",
    }
    INDEX.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def package_files() -> list[Path]:
    answer = []
    for path in PACKAGE.rglob("*"):
        mode = path.lstat().st_mode
        if stat.S_ISLNK(mode):
            raise AssertionError(("symlink", path))
        if stat.S_ISREG(mode):
            answer.append(path)
        elif not stat.S_ISDIR(mode):
            raise AssertionError(("special", path))
    return sorted(answer, key=lambda value: value.relative_to(PACKAGE).as_posix())


def build_manifest() -> None:
    rows = [
        f"{sha256(path)}  {path.relative_to(PACKAGE).as_posix()}"
        for path in package_files() if path != MANIFEST
    ]
    MANIFEST.write_text("\n".join(sorted(rows)) + "\n", encoding="utf-8")


def build_archive() -> None:
    if ARCHIVE.exists():
        ARCHIVE.unlink()
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as output:
        for path in package_files():
            name = f"{PACKAGE.name}/{path.relative_to(PACKAGE).as_posix()}"
            info = zipfile.ZipInfo(name)
            info.date_time = (2026, 9, 13, 18, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 & 0xFFFF) << 16
            output.writestr(info, path.read_bytes(), compresslevel=9)
    ARCHIVE_SHA.write_text(f"{sha256(ARCHIVE)}  {ARCHIVE.name}\n", encoding="utf-8")


def main() -> None:
    files, counts = collect()
    copy_files(files)
    build_index(files, counts)
    build_manifest()
    build_archive()
    print(f"DEPENDENCY_UNION_FILES={len(files)}")
    print(f"PACKAGE_REGULAR_FILES={len(package_files())}")
    print(f"ARCHIVE_SHA256={sha256(ARCHIVE)}")


if __name__ == "__main__":
    main()
