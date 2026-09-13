#!/usr/bin/env python3
"""Strict, dependency-aware verification of the B124/D4 package."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import stat


PACKAGE = Path(__file__).resolve().parents[1]
MANIFEST = PACKAGE / "P23_B124_D4_UPSTREAM_RECONSTRUCTION_V1_SHA256SUMS.txt"
INDEX = PACKAGE / "UPSTREAM_DEPENDENCY_INDEX.json"
LINE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def regular_files() -> set[str]:
    answer: set[str] = set()
    for path in PACKAGE.rglob("*"):
        relative = path.relative_to(PACKAGE).as_posix()
        mode = path.lstat().st_mode
        assert not stat.S_ISLNK(mode), ("symlink", relative)
        if stat.S_ISREG(mode):
            answer.add(relative)
        elif not stat.S_ISDIR(mode):
            raise AssertionError(("special path", relative))
    return answer


def parse_manifest() -> dict[str, str]:
    rows: dict[str, str] = {}
    lines = MANIFEST.read_text(encoding="utf-8").splitlines()
    assert lines == sorted(lines), "manifest is not sorted"
    for raw in lines:
        match = LINE.fullmatch(raw)
        assert match, ("malformed manifest row", raw)
        digest, relative = match.groups()
        candidate = Path(relative)
        assert not candidate.is_absolute()
        assert relative == candidate.as_posix()
        assert relative not in {"", "."}
        assert all(part not in {"", ".", ".."} for part in candidate.parts)
        assert relative not in rows, ("duplicate", relative)
        assert relative != MANIFEST.name, "manifest must be self-excluding"
        rows[relative] = digest
    return rows


def main() -> None:
    rows = parse_manifest()
    actual = regular_files() - {MANIFEST.name}
    assert actual == set(rows), {
        "missing_from_manifest": sorted(actual-set(rows)),
        "missing_from_tree": sorted(set(rows)-actual),
    }
    for relative, expected in rows.items():
        path = PACKAGE / relative
        assert sha256(path) == expected, relative

    index = json.loads(INDEX.read_text(encoding="utf-8"))
    assert index["schema"] == "p23_B124_D4_upstream_dependency_index_v1"
    assert index["target"] == "D4=P4-P1"
    assert index["base_divisor"] == ["P1", "P2", "P4"]
    assert index["prime"] == 23
    assert index["precisions"] == [8, 10]
    indexed = set()
    for node in index["nodes"]:
        relative = node["path"]
        indexed.add(relative)
        assert relative in rows, ("indexed path not manifested", relative)
        assert node["sha256"] == rows[relative]
        assert (PACKAGE / relative).stat().st_size == node["bytes"]
    assert set(index["load_bearing_paths"]) <= indexed

    certificate_root = PACKAGE / (
        "repository/results/2026-08-31_p23_alternative_km_base_chart_screen_v1/"
        "certificates"
    )
    expected_statuses = {
        "p23_B124_graded_product_lattices_final_v1.json":
            "PASS_COMPATIBLE_PRODUCT_GENERATED_V2_THROUGH_V7_LATTICES",
        "p23_B124_tensor_function_reduction_audit_v1.json":
            "PASS_ALL_CACHED_TENSOR_ROWS_AS_REDUCED_FUNCTION_IDENTITIES",
        "p23_B124_finite_KM_addflip_v1.json":
            "PASS_FINITE_FIELD_KM_EQUALITY_NEGATION_ADDFLIP",
        "p23_B124_sage_KM_crosscheck_v1.json":
            "PASS_NATIVE_SAGE_KM_GROUP_LAW_ORDER_75_AND_CACHE_BASE_CHANGE",
        "p23_B124_UnitKM_native_tensor_audit_v1.json":
            "PASS_UNITKM_HELPER_ON_NATIVE_SAGE_TENSORS",
        "p23_B124_scalar75_v1.json":
            "PASS_CACHED_KM_EXACT_REDUCTION_ORDER_75_TWO_CHAINS",
        "p23_B124_padic_tensor_lift_v1.json":
            "PASS_EXACT_PRODUCT_TENSOR_LIFT_MOD_23_POWER_8_AND_10",
        "p23_B124_padic_KM_scalar75_v1.json":
            "PASS_PADIC_KM_GROUP_LAW_AND_75D_AT_23_POWER_8_AND_10",
        "p23_B124_75D_formal_chart_decode_v1.json":
            "PASS_75D_THREE_POINT_FORMAL_CHART_NEWTON_AT_23_POWER_8_AND_10",
        "p23_B124_first_branchwise_log_v1.json":
            "PASS_FIRST_BRANCHWISE_ABELIAN_LOG_COLUMN_AT_23_POWER_8_AND_10",
        "p23_s4_full_log_matrix_v1.json":
            "PASS_ALL_FOUR_S4_BRANCHWISE_LOG_COLUMNS_AT_23_POWER_8_AND_10",
    }
    for name, status in expected_statuses.items():
        payload = json.loads((certificate_root / name).read_text(encoding="utf-8"))
        assert payload["status"] == status, name
    scalar = json.loads(
        (certificate_root / "p23_B124_scalar75_v1.json").read_text(encoding="utf-8")
    )
    assert scalar["exact_order"] == 75

    print(
        "P23_B124_D4_UPSTREAM_PACKAGE_VERIFY="
        f"PASS_EXACT_CLOSED_TREE_{len(rows)}_FILES"
    )
    print("DEPENDENCY_DAG=PASS_CANONICAL_TO_GRADED_TO_TENSOR_TO_75D_TO_CHART_TO_D4")


if __name__ == "__main__":
    main()
