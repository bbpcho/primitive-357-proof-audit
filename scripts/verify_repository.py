#!/usr/bin/env python3
"""Fast structural checks for the proof-audit control repository."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
HEX64 = re.compile(r"[0-9a-f]{64}\Z")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def verify_asset_index() -> None:
    data = json.loads((ROOT / "evidence/assets.json").read_text())
    assert data["schema"] == "primitive_357_release_asset_index_v1"
    assets = data["assets"]
    names = [item["filename"] for item in assets]
    ids = [item["id"] for item in assets]
    assert len(names) == len(set(names)) == len(ids) == len(set(ids))
    for item in assets:
        assert Path(item["filename"]).name == item["filename"]
        assert HEX64.fullmatch(item["sha256"])
        assert isinstance(item["bytes"], int) and item["bytes"] > 0
        rel = Path(item["source_path_from_workspace"])
        assert not rel.is_absolute() and ".." not in rel.parts

    checksum_lines = [
        line for line in
        (ROOT / "evidence/checksums/RELEASE_ASSETS_SHA256.txt")
        .read_text()
        .splitlines()
        if line
    ]
    expected = [f"{item['sha256']}  {item['filename']}" for item in assets]
    assert checksum_lines == expected


def verify_status() -> None:
    status = json.loads((ROOT / "audit/status.json").read_text())
    assert status["schema"] == "primitive_357_audit_status_v1"
    assert status["proof_complete"] is False
    assert status["public_proof_release_authorized"] is False
    gates = {gate["id"]: gate for gate in status["gates"]}
    assert gates["mordell_weil_rank_upper_bound_and_composition"]["state"] == "open"
    assert gates["saturation_calculations"]["state"].startswith("pass_")
    assert gates["split_23_global_logarithms"]["state"].startswith("pass_")
    assert gates["final_theorem_composition"]["state"] == "blocked_by_rank_gate"
    assert gates["public_proof_release"]["state"] == "blocked"


def verify_tracked_manifest() -> None:
    manifest_path = ROOT / "evidence/TRACKED_SNAPSHOT_SHA256.txt"
    lines = manifest_path.read_text().splitlines()
    seen: set[str] = set()
    ordered_paths: list[str] = []
    for line in lines:
        digest, separator, rel_text = line.partition("  ")
        assert separator == "  " and HEX64.fullmatch(digest)
        rel = Path(rel_text)
        assert not rel.is_absolute() and ".." not in rel.parts
        assert rel_text not in seen
        seen.add(rel_text)
        ordered_paths.append(rel_text)
        path = ROOT / rel
        assert path.is_file() and not path.is_symlink()
        assert sha256(path) == digest

    assert ordered_paths == sorted(ordered_paths)

    actual = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.relative_to(ROOT).parts
        and path != manifest_path
        and "build" not in path.relative_to(ROOT).parts
        and "__pycache__" not in path.relative_to(ROOT).parts
    }
    assert seen == actual, (
        f"tracked snapshot coverage mismatch: missing={sorted(actual-seen)}, "
        f"extra={sorted(seen-actual)}"
    )


def main() -> int:
    required = [
        "README.md",
        "paper/manuscript.tex",
        "paper/manuscript-v3.pdf",
        "docs/PROOF_STATUS.md",
        "docs/RANK_GAP.md",
        "evidence/assets.json",
        "audit/status.json",
    ]
    for rel in required:
        path = ROOT / rel
        if not path.is_file() or path.is_symlink():
            raise SystemExit(f"missing required regular file: {rel}")

    verify_asset_index()
    verify_status()
    verify_tracked_manifest()
    print("REPOSITORY_VERIFICATION=PASS_STRICT_CONTROL_PLANE_AND_OPEN_RANK_GATE")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, KeyError, json.JSONDecodeError) as exc:
        print(f"REPOSITORY_VERIFICATION=FAIL {exc}", file=sys.stderr)
        sys.exit(1)
