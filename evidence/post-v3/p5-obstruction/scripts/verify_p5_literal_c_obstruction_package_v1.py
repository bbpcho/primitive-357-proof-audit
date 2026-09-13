#!/usr/bin/env python3
"""Strict tree, manifest, and mathematical-interface verification."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import stat


PACKAGE = Path(__file__).resolve().parents[1]
REPOSITORY = PACKAGE / "repository"
MANIFEST = PACKAGE / "P5_LITERAL_C_OBSTRUCTION_DEPENDENCY_CLOSURE_V1_SHA256SUMS.txt"
INDEX = PACKAGE / "DECLARED_DEPENDENCY_INDEX.json"
LINE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$")


def sha256(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            result.update(block)
    return result.hexdigest()


def parse_strict_manifest() -> dict[str, str]:
    rows: dict[str, str] = {}
    raw_rows = MANIFEST.read_text().splitlines()
    assert raw_rows == sorted(raw_rows), "package manifest not sorted"
    for raw in raw_rows:
        match = LINE.fullmatch(raw)
        assert match, ("malformed row", raw)
        expected, relative = match.groups()
        candidate = Path(relative)
        assert not candidate.is_absolute()
        assert relative == candidate.as_posix()
        assert all(part not in {"", ".", ".."} for part in candidate.parts)
        assert relative != MANIFEST.name
        assert relative not in rows
        rows[relative] = expected
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


def verify_historical_manifest(relative: str, expected_count: int) -> None:
    manifest = REPOSITORY / relative
    old_root = Path("/home/pcho/Documents/Codex/beal_357")
    count = 0
    for number, raw in enumerate(manifest.read_text().splitlines(), 1):
        match = LINE.fullmatch(raw)
        assert match, (relative, number, "syntax")
        expected, name = match.groups()
        candidate = Path(name)
        if candidate.is_absolute():
            target = REPOSITORY / candidate.relative_to(old_root)
        elif name.startswith("results/") or name.startswith("beal_357_"):
            target = REPOSITORY / candidate
        else:
            target = manifest.parent / candidate
        assert target.is_file(), (relative, number, "missing", target)
        assert sha256(target) == expected, (relative, number, target)
        count += 1
    assert count == expected_count, (relative, count, expected_count)


def main() -> None:
    rows = parse_strict_manifest()
    assert regular_tree() - {MANIFEST.name} == set(rows)
    for relative, expected in rows.items():
        assert sha256(PACKAGE / relative) == expected, relative

    index = json.loads(INDEX.read_text())
    assert index["schema"] == "p5_literal_c_obstruction_dependency_closure_v1"
    assert index["declared_hash_edges"] == 119
    assert index["declared_unique_targets"] == 93
    assert len(index["portable_replay_support_files_beyond_declared_hash_edges"]) == 2
    for relative in index["portable_replay_support_files_beyond_declared_hash_edges"]:
        assert relative in rows
    assert index["arithmetic_result"] == {
        "both_nonzero": True,
        "carrier_bits_root_00": [1, 0, 1],
        "carrier_bits_root_11": [0, 1, 0],
        "carrier_signs_root_00": [-1, 1, -1],
        "coordinate_root_00": [1, 0],
        "coordinate_root_11": [0, 1],
    }
    for node in index["nodes"]:
        relative = node["path"]
        assert rows[relative] == node["sha256"]
        assert (PACKAGE / relative).stat().st_size == node["bytes"]

    verify_historical_manifest(
        "results/2026-08-25_source_class_bridge_resume/summaries/"
        "P7_ORBIT42_56_COHERENT_COCYCLE_V4_RESUME1_FROZEN_SHA256SUMS.txt",
        74,
    )
    verify_historical_manifest(
        "results/2026-08-25_source_class_bridge_resume/certificates/"
        "p7_orbit42_56_coherent_cocycle_v4_resume1.SHA256SUMS.txt",
        12,
    )

    anchors = index["named_anchors"]
    for value in anchors.values():
        assert sha256(PACKAGE / value["path"]) == value["sha256"]

    auditor = REPOSITORY / (
        "results/2026-08-26_literal_c_a26_p5_conditional_rejection_independent_audit/"
        "scripts/audit_declared_hash_closure_v1.py"
    )
    spec = importlib.util.spec_from_file_location("packaged_p5_closure", auditor)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # The frozen coherent certificate records the producer host's absolute
    # root.  Preserve the historical auditor byte-for-byte, but redirect that
    # one path dialect into the extracted repository for portable replay.
    old_root = Path("/home/pcho/Documents/Codex/beal_357")
    original_resolve = module.resolve
    def portable_resolve(path: str, base=module.ROOT):
        candidate = Path(path)
        if candidate.is_absolute():
            try:
                return module.ROOT / candidate.relative_to(old_root)
            except ValueError:
                return candidate
        return original_resolve(path, base)
    module.resolve = portable_resolve
    module.main()
    assert len(module.EDGES) == 119
    assert len({path for _, path, _ in module.EDGES}) == 93

    theorem = json.loads((REPOSITORY / (
        "results/2026-08-26_literal_c_a26_residual_bits/certificates/"
        "p5_literal_c_a26_conditional_rejection_theorem_v1.json"
    )).read_text())
    exact = theorem["exact_evidence"]
    assert exact["root_00"]["carrier_bits"] == [1, 0, 1]
    assert exact["root_00"]["coordinate_in_rq1_rq2_basis"] == [1, 0]
    assert exact["root_11"]["carrier_bits"] == [0, 1, 0]
    assert exact["root_11"]["coordinate_in_rq1_rq2_basis"] == [0, 1]
    assert exact["root_00"]["nonzero"] and exact["root_11"]["nonzero"]

    p5_manifest = json.loads((REPOSITORY / (
        "results/2026-08-26_literal_c_a26_residual_bits/certificates/"
        "p5_literal_c_a26_candidate_late_v2_manifest.json"
    )).read_text())
    assert p5_manifest["exact_padic_signs_on_physical_carriers"] == {
        "rq_1": -1, "rq_2": 1, "rq_3": -1
    }
    assert p5_manifest["exact_finite_character_relation"] == (
        "chi_rq_1 = chi_rq_3 != chi_rq_2; rank 2"
    )

    coherent = json.loads((REPOSITORY / (
        "results/2026-08-25_source_class_bridge_resume/certificates/"
        "p7_orbit42_56_coherent_cocycle_v4_resume1.json"
    )).read_text())
    serialized = json.dumps(coherent, sort_keys=True, separators=(",", ":"))
    assert "combined_global_orbit_sign_solutions" in serialized
    assert "[[0,0],[1,1]]" in serialized

    required = {
        "results/2026-08-25_source_class_bridge_resume/inputs/p7_target42_tau_relative_root_v1.bin":
            "9de7000696dbe254b0bc06bf47e21e9f0f9ce846809bbc1d25a32498ec011acd",
        "results/2026-08-22_discovery_engine/checkpoints/degree42_contact_cross_matrices_v6.bin":
            "ee5a608769d29dd88cfcff4800609996df745c7fb736b1a259c808570f80b9fa",
        "results/2026-08-22_discovery_engine/checkpoints/degree42_contact_crt_exact_candidate_batch4_v1_after_128.bin":
            "daa64b9d2fffd5d0c6021f8b47f76d6982c4c07fef80c339d6cd2fff12463f95",
        "results/2026-08-22_discovery_engine/checkpoints/degree42_horner_one_element_v3.bin":
            "9bf02783c7d5daf222dd9d5e8d26f8563d1fd9836fa8929471376201f60b813b",
        "results/2026-08-22_discovery_engine/checkpoints/degree42_contact_v4_lineY.bin":
            "7377aa1221050c0f40c5a8c5e02d5793833d83a5eb08ae885429520a5912ea73",
        "results/2026-08-22_discovery_engine/checkpoints/degree42_line_contact_reduced_L_v3.bin":
            "5d93c3bac5f19a210836ec310265031f442392b91c91734594e9452f1ea46daf",
    }
    for relative, expected in required.items():
        assert sha256(REPOSITORY / relative) == expected

    print(f"PACKAGE_TREE=PASS_{len(rows)}_MANIFESTED_FILES")
    print("DECLARED_HASH_CLOSURE=PASS_119_EDGES_93_UNIQUE_TARGETS")
    print("TARGET42_AND_CONTACT_CHECKPOINTS=PASS_EXACT_HASHES")
    print("P5_OBSTRUCTION=PASS_SIGNS_MINUS_PLUS_MINUS_COORDINATES_10_AND_01_NONZERO")
    print("CLAIM_BOUNDARY=CONDITIONAL_A26_IMPLICATION_ONLY")


if __name__ == "__main__":
    main()
