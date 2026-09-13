#!/usr/bin/env python3
"""Generate the dependency index, strict manifest, and deterministic ZIP."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import stat
import zipfile


PACKAGE = Path(__file__).resolve().parents[1]
INDEX = PACKAGE / "UPSTREAM_DEPENDENCY_INDEX.json"
MANIFEST = PACKAGE / "P23_B124_D4_UPSTREAM_RECONSTRUCTION_V1_SHA256SUMS.txt"
ARCHIVE = PACKAGE.parent / "2026-09-13_p23_B124_D4_upstream_reconstruction_package_v1.zip"
ARCHIVE_DIGEST = ARCHIVE.with_suffix(ARCHIVE.suffix + ".sha256")
REPOSITORY = PACKAGE / "repository"
B124 = (
    "repository/results/2026-08-31_p23_alternative_km_base_chart_screen_v1/"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def node(relative: str, role: str, stage: str) -> dict:
    path = PACKAGE / relative
    return {
        "path": relative,
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
        "role": role,
        "stage": stage,
    }


def build_index() -> None:
    named = [
        node(
            "repository/beal_357_spark_handover_2026-08-20/project/"
            "p7_f42_canonical_exact.json.gz",
            "exact canonical plane-quartic input",
            "model",
        ),
        node(
            "repository/results/2026-08-27_p23_branchwise_km_small_s4_probe_v1/"
            "scripts/replay_small_KM_group_law_and_75D.sage",
            "source-only UnitKM and unit-pivot helper provider; top level not executed",
            "algorithm-source",
        ),
        node(B124 + "scripts/build_p23_B124_graded_product_lattices_v1.sage",
             "producer for exact B124 section spaces and product lattices", "graded"),
        node(B124 + "evidence/p23_B124_graded_product_lattices_v1.sobj",
             "sealed exact graded-lattice and finite tensor cache", "graded"),
        node(B124 + "certificates/p23_B124_graded_product_lattices_final_v1.json",
             "graded-lattice completion certificate", "graded"),
        node(B124 + "scripts/audit_p23_B124_tensor_function_reduction_v1.sage",
             "independent reduction-of-functions tensor audit", "finite"),
        node(B124 + "certificates/p23_B124_tensor_function_reduction_audit_v1.json",
             "finite tensor audit certificate", "finite"),
        node(B124 + "scripts/replay_p23_B124_finite_KM_addflip_v1.sage",
             "finite KM equality, negation, and addflip replay", "finite"),
        node(B124 + "certificates/p23_B124_finite_KM_addflip_v1.json",
             "finite KM replay certificate", "finite"),
        node(B124 + "scripts/certify_p23_B124_scalar75_v1.sage",
             "finite exact-order-75 producer", "finite-scalar"),
        node(B124 + "certificates/p23_B124_scalar75_v1.json",
             "finite exact-order-75 certificate", "finite-scalar"),
        node(B124 + "scripts/build_p23_B124_padic_tensor_lift_v1.sage",
             "B124 tensor-lift producer modulo 23^8 and 23^10", "tensor-lift"),
        node(B124 + "evidence/p23_B124_padic_tensors_mod23power10_v1.sobj",
             "lifted multiplication tensors and base matrices", "tensor-lift"),
        node(B124 + "certificates/p23_B124_padic_tensor_lift_v1.json",
             "p-adic tensor-lift certificate", "tensor-lift"),
        node(B124 + "scripts/replay_p23_B124_padic_KM_scalar75_v1.sage",
             "two-route p-adic KM scalar-75 producer", "75D-class"),
        node(B124 + "evidence/p23_B124_padic_75D_classes_v1.sobj",
             "75D class matrices at precisions 8 and 10", "75D-class"),
        node(B124 + "certificates/p23_B124_padic_KM_scalar75_v1.json",
             "p-adic group-law and 75D certificate", "75D-class"),
        node(B124 + "scripts/decode_p23_B124_75D_formal_chart_v1.sage",
             "three-point formal-chart Newton decoder", "formal-chart"),
        node(B124 + "evidence/p23_B124_75D_formal_chart_points_v1.sobj",
             "decoded formal-chart points at precisions 8 and 10", "formal-chart"),
        node(B124 + "certificates/p23_B124_75D_formal_chart_decode_v1.json",
             "formal-chart decoding certificate", "formal-chart"),
        node(B124 + "scripts/compute_p23_B124_first_branchwise_log_v1.sage",
             "D4 branchwise abelian-log producer", "D4-log"),
        node(B124 + "evidence/p23_B124_first_branchwise_log_v1.sobj",
             "saved D4 logarithm column used by the four-column replay", "D4-log"),
        node(B124 + "certificates/p23_B124_first_branchwise_log_v1.json",
             "D4 logarithm certificate", "D4-log"),
        node(B124 + "scripts/compute_p23_s4_full_log_matrix_v1.sage",
             "downstream four-column s=4 log producer and D4 consumer", "consumer"),
        node(B124 + "certificates/p23_s4_full_log_matrix_v1.json",
             "four-column s=4 log-matrix certificate", "consumer"),
        node(B124 + "evidence/p23_s4_full_log_matrix_v1.sobj",
             "four-column s=4 global-log cache", "consumer"),
    ]
    payload = {
        "schema": "p23_B124_D4_upstream_dependency_index_v1",
        "scope": (
            "closed upstream reconstruction of the D4=P4-P1 s=4 logarithm "
            "from the exact quartic through B124 tensors, 75D, and the formal chart"
        ),
        "prime": 23,
        "embedding": "sqrt(-7) congruent to 4 modulo 23",
        "base_divisor": ["P1", "P2", "P4"],
        "target": "D4=P4-P1",
        "reduction_order": 75,
        "precisions": [8, 10],
        "nodes": named,
        "load_bearing_paths": [item["path"] for item in named],
        "edges": [
            {"from": "model", "to": "graded", "claim": "construct L(nD0) and product lattices"},
            {"from": "graded", "to": "finite", "claim": "reduce exact products and validate KM maps"},
            {"from": "finite", "to": "finite-scalar", "claim": "certify D4 has exact order 75 over F_23"},
            {"from": "graded+finite-scalar", "to": "tensor-lift", "claim": "solve exact product coordinates over Z/23^8 and Z/23^10"},
            {"from": "tensor-lift", "to": "75D-class", "claim": "compute 75D by two KM routes and compare precisions"},
            {"from": "75D-class", "to": "formal-chart", "claim": "Newton-decode 75D into three unit-disk points"},
            {"from": "formal-chart", "to": "D4-log", "claim": "integrate the three regular differentials and divide by 75"},
            {"from": "D4-log", "to": "consumer", "claim": "supply the D4 column of the s=4 four-column matrix"},
        ],
        "closure_note": (
            "Every file from the historical B124 package is carried under repository/. "
            "The only reads outside that directory are the canonical quartic and the "
            "source-only historical UnitKM script, both included and hash-bound here."
        ),
        "software": {
            "sage": "10.9",
            "python": "3.12",
            "replay_model": "clean temporary copy; original workspace inaccessible to the portable launcher",
        },
    }
    INDEX.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


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
    return sorted(result, key=lambda item: item.relative_to(PACKAGE).as_posix())


def build_manifest() -> None:
    paths = [path for path in package_files() if path != MANIFEST]
    rows = sorted(
        f"{sha256(path)}  {path.relative_to(PACKAGE).as_posix()}"
        for path in paths
    )
    MANIFEST.write_text("\n".join(rows) + "\n", encoding="utf-8")


def build_archive() -> None:
    if ARCHIVE.exists():
        ARCHIVE.unlink()
    prefix = PACKAGE.name
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED,
                         compresslevel=9) as target:
        for path in package_files():
            relative = path.relative_to(PACKAGE).as_posix()
            info = zipfile.ZipInfo(f"{prefix}/{relative}")
            info.date_time = (2026, 9, 13, 12, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 & 0xFFFF) << 16
            target.writestr(info, path.read_bytes(), compresslevel=9)
    ARCHIVE_DIGEST.write_text(
        f"{sha256(ARCHIVE)}  {ARCHIVE.name}\n", encoding="utf-8"
    )


def main() -> None:
    build_index()
    build_manifest()
    build_archive()
    print(f"PACKAGE_FILES={len(package_files())}")
    print(f"ARCHIVE={ARCHIVE}")
    print(f"ARCHIVE_SHA256={sha256(ARCHIVE)}")


if __name__ == "__main__":
    main()
