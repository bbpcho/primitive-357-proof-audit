#!/usr/bin/env python3
"""Verify every indexed immutable asset. No check depends on Python asserts."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys
from verification_common import asset_index, regular_file, require, sha256

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--assets-dir", type=Path)
    source.add_argument("--workspace-root", type=Path)
    parser.add_argument("--asset-id", action="append", dest="asset_ids",
                        help="verify this indexed asset ID; repeat for several (default: every asset)")
    args = parser.parse_args()
    assets = asset_index(ROOT)
    if args.asset_ids is not None:
        require(len(args.asset_ids) == len(set(args.asset_ids)), "duplicate --asset-id selection")
        selected = set(args.asset_ids)
        require(selected <= {item["id"] for item in assets},
                "unknown --asset-id selection: " + repr(sorted(selected - {item["id"] for item in assets})))
        assets = [item for item in assets if item["id"] in selected]
    supplied = args.assets_dir if args.assets_dir is not None else args.workspace_root
    require(supplied.is_dir() and not supplied.is_symlink(), "asset root must be a regular directory")
    root = supplied.resolve()
    for item in assets:
        rel = item["filename"] if args.assets_dir is not None else item["source_path_from_workspace"]
        path = regular_file(root, rel)
        require(path.stat().st_size == item["bytes"], "size mismatch: " + item["filename"])
        require(sha256(path) == item["sha256"], "digest mismatch: " + item["filename"])
        print(f"PASS {item['sha256']} {item['bytes']} {item['filename']}")
    print(f"ASSET_VERIFICATION=PASS_{len(assets)}_FILES")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print("ASSET_VERIFICATION=FAIL " + str(exc), file=sys.stderr)
        sys.exit(1)
