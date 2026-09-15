#!/usr/bin/env python3
"""Validate the complete control snapshot and the recorded release decision.

This is an integrity/status check, not an arithmetic replay. All checks use
ordinary runtime conditions and remain active under python -O and -OO.
"""
from __future__ import annotations

import os
from pathlib import Path
import stat
import sys
from verification_common import (asset_index, digest_value, manifest_rows, read_json,
    regular_file, relative_path, require, sha256, unique_records)

ROOT = Path(__file__).resolve().parents[1]
TAG = "verified-2026-09-14.1"
MANIFEST = "evidence/TRACKED_SNAPSHOT_SHA256.txt"
ASSET_ID = "PRIMITIVE_357_VERIFIED_RELEASE_2026_09_14_V1"
PRIOR_GROUPS = ["exports", "rawdyadic", "foundation", "fiveplace", "p5", "logs", "finite_maps"]
GATES = {"paper_build", "hecke_ambient_coverage", "p5_obstruction_dependency_closure",
    "corrected66_predyadic_dependency_closure", "p7_complete_local_image",
    "p2_place2_fake_kernel_correction_dependency_closure",
    "mordell_weil_rank_upper_bound_and_composition", "saturation_calculations",
    "split_23_global_logarithms", "final_theorem_composition",
    "published_and_magma_premises", "fresh_integrated_replay", "public_proof_release"}


def bound_json(root, row):
    path = regular_file(root, row["path"])
    require(sha256(path) == digest_value(row["sha256"]), "bound file digest mismatch: " + row["path"])
    return read_json(path), path


def verify_replay(binding_path, assets):
    binding = read_json(regular_file(ROOT, binding_path))
    require(binding.get("schema") == "primitive357_replay_binding_v1", "replay binding schema")
    require(binding.get("release_tag") == TAG and binding.get("asset_id") == ASSET_ID,
            "wrong release identity in replay binding")
    asset = unique_records(assets).get(ASSET_ID)
    require(asset is not None, "verified release asset is not indexed")
    require(binding["asset_sha256"] == asset["sha256"] and binding["asset_bytes"] == asset["bytes"],
            "replay binding and sealed asset index disagree")
    result, result_path = bound_json(ROOT, binding["replay_result"])
    tested, tested_path = bound_json(ROOT, binding["tested_manifest"])
    proof, _ = bound_json(ROOT, binding["proof_inputs"])
    final, _ = bound_json(ROOT, binding["final_manifest"])
    tested_rows, final_rows = manifest_rows(tested), manifest_rows(final)
    require(result.get("schema") == "primitive357_integrated_replay_v1"
            and result.get("status") == "PASS_FRESH_INTEGRATED_REPLAY", "fresh integrated replay is not PASS")
    require(result["input_manifest"] == {"files": len(tested_rows), "manifest_sha256": sha256(tested_path)},
            "fresh replay was not run on the indexed tested manifest")
    components = unique_records(result["components"])
    markers = {"prior": "PASS_SELECTED_PRIOR_GROUPS", "rank_local": "PASS_FRESH_RANK_LOCAL_COMPONENT",
               "sectors": "PASS_FRESH_TEN_SECTORS_AND_INTERFACES"}
    require(set(components) == set(markers), "missing or extra replay component")
    for name, row in components.items():
        require(type(row["exit_code"]) is int and row["exit_code"] == 0, "failed replay component: " + name)
        log = regular_file(result_path.parent, row["log"])
        require(sha256(log) == digest_value(row["sha256"]), "component log digest: " + name)
        require(sum(line.strip() == markers[name] for line in log.read_text().splitlines()) == 1,
                "missing or repeated component success marker: " + name)
    require(result["prior_groups"] == PRIOR_GROUPS, "prior replay group coverage")
    require(result["rank_conclusions"].get("equals_B_plus_literal_c") is True, "rank join missing")
    require(proof.get("schema") == "primitive357_proof_inputs_v1" and proof.get("release_tag") == TAG,
            "proof-input index schema/tag")
    proof_rows = manifest_rows({"schema": "primitive357_verified_release_manifest_v1", "files": proof["files"]})
    require(set(proof_rows) == set(tested_rows), "proof-input index does not cover every tested input")
    for path, row in tested_rows.items():
        identity = {key: row[key] for key in ("path", "sha256", "bytes")}
        require(proof_rows[path] == identity, "proof-input identity mismatch: " + path)
        require(path in final_rows and all(final_rows[path][key] == value for key, value in identity.items()),
                "tested input changed or disappeared from the final release: " + path)


def verify_status(assets):
    status = read_json(regular_file(ROOT, "audit/status.json"))
    require(status.get("schema") == "primitive_357_audit_status_v2", "audit status schema")
    require(status.get("release_tag") == TAG and status.get("release_asset_id") == ASSET_ID, "status release identity")
    gates = unique_records(status["gates"])
    require(set(gates) == GATES, "gate coverage mismatch")
    for name, gate in gates.items():
        require(gate.get("mandatory") is True, "mandatory gate disabled: " + name)
        regular_file(ROOT, gate["evidence"])
        expected = "imported" if name == "published_and_magma_premises" else "pass"
        if name not in {"fresh_integrated_replay", "public_proof_release"}:
            require(gate.get("state") == expected, "mathematical gate is not complete: " + name)
    work = read_json(regular_file(ROOT, status["rank_workplan"]))
    require(work.get("schema") == "primitive_357_rank_gap_workplan_v2" and work.get("overall_state") == "pass",
            "rank workplan is not complete")
    packages = unique_records(work["packages"])
    require(set(packages) == {"R" + str(i) for i in range(1, 8)}, "rank package coverage")
    for key, row in packages.items():
        require(row["state"] == "pass", "rank package is not pass: " + key)
        deps = row["depends_on"]
        require(isinstance(deps, list) and len(deps) == len(set(deps))
                and all(d in packages and d < key for d in deps), "invalid rank package dependencies")
        regular_file(ROOT, row["evidence"])
    phase = status["release_state"]
    require(phase in {"pending_fresh_replay", "verified"}, "unsupported release state")
    verified = phase == "verified"
    require(status["proof_complete"] is verified and status["public_proof_release_authorized"] is verified,
            "release flags disagree with release state")
    for key in ("fresh_integrated_replay", "public_proof_release"):
        require(gates[key]["state"] == ("pass" if verified else "pending"), "release gate state mismatch")
    fresh = status["fresh_replay"]
    if verified:
        require(fresh["state"] == "pass", "fresh replay has not passed")
        verify_replay(fresh["binding"], assets)
    else:
        require(fresh == {"state": "pending", "binding": None}, "pending release must not assert a replay")
    return phase


def inventory():
    # Only these top-level generated/private directories are excluded. A nested
    # data/build or data/.git directory is evidence, not an automatic exclusion.
    result = set()
    def visit(directory, parts):
        for entry in os.scandir(directory):
            name_parts = parts + (entry.name,)
            name = "/".join(name_parts)
            mode = entry.stat(follow_symlinks=False).st_mode
            require(not stat.S_ISLNK(mode), "symlink in repository snapshot: " + name)
            if not parts and entry.name in {".git", "build"}:
                require(stat.S_ISDIR(mode), "excluded root must be a directory: " + name)
                continue
            if stat.S_ISDIR(mode):
                visit(entry.path, name_parts)
            else:
                require(stat.S_ISREG(mode), "non-regular repository entry: " + name)
                bytecode = len(name_parts) > 1 and name_parts[-2] == "__pycache__" and entry.name.endswith((".pyc", ".pyo"))
                if name != MANIFEST and not bytecode:
                    result.add(name)
    visit(ROOT, ())
    return result


def verify_tracked_manifest():
    lines = regular_file(ROOT, MANIFEST).read_text().splitlines()
    require(bool(lines), "empty tracked manifest")
    seen = []
    for line in lines:
        digest, separator, name = line.partition("  ")
        require(separator == "  " and name != MANIFEST, "invalid manifest line")
        digest_value(digest)
        path = regular_file(ROOT, name)
        require(sha256(path) == digest, "tracked digest mismatch: " + name)
        seen.append(name)
    require(seen == sorted(set(seen)), "duplicate or unsorted tracked manifest")
    actual = inventory()
    require(set(seen) == actual, "tracked snapshot coverage mismatch: " + repr(sorted(set(seen) ^ actual)))


def main():
    for name in ("README.md", "paper/manuscript.tex", "paper/rank-proof.tex", "paper/manuscript.pdf",
                 "docs/PROOF_STATUS.md", "docs/RANK_GAP.md", "docs/EVIDENCE.md", "docs/H0_H1_CORRIGENDUM.md"):
        regular_file(ROOT, name)
    assets = asset_index(ROOT)
    phase = verify_status(assets)
    verify_tracked_manifest()
    from verify_current_distribution import verify_current_distribution
    from verify_current_publication import verify_current_publication
    status = read_json(regular_file(ROOT, "audit/status.json"))
    distribution = verify_current_distribution(ROOT, status)
    publication = verify_current_publication(ROOT, status)
    print("CURRENT_DISTRIBUTION_VERIFICATION=" + distribution["status"])
    print("CURRENT_PUBLICATION_VERIFICATION=" + publication["status"])
    print("REPOSITORY_VERIFICATION=PASS_CONTROL_SNAPSHOT_" + phase.upper())


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print("REPOSITORY_VERIFICATION=FAIL " + str(exc), file=sys.stderr)
        sys.exit(1)
