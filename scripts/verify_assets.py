#!/usr/bin/env python3
"""Verify large release assets without placing them in ordinary Git history."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys


HEX64 = re.compile(r"[0-9a-f]{64}\Z")
ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--assets-dir", type=Path)
    source.add_argument("--workspace-root", type=Path)
    args = parser.parse_args()

    index = json.loads((ROOT / "evidence/assets.json").read_text())
    if index.get("schema") != "primitive_357_release_asset_index_v1":
        raise SystemExit("unsupported asset-index schema")

    seen_names: set[str] = set()
    for item in index["assets"]:
        name = item["filename"]
        expected = item["sha256"]
        if name != Path(name).name or name in seen_names:
            raise SystemExit(f"unsafe or duplicate asset name: {name}")
        if not HEX64.fullmatch(expected):
            raise SystemExit(f"invalid SHA-256 for {name}")
        seen_names.add(name)

        if args.assets_dir is not None:
            path = args.assets_dir.resolve() / name
        else:
            rel = Path(item["source_path_from_workspace"])
            if rel.is_absolute() or ".." in rel.parts:
                raise SystemExit(f"unsafe workspace path for {name}")
            path = args.workspace_root.resolve() / rel

        if not path.is_file() or path.is_symlink():
            raise SystemExit(f"missing regular asset: {path}")
        size = path.stat().st_size
        if size != item["bytes"]:
            raise SystemExit(f"size mismatch for {name}: {size}")
        actual = digest(path)
        if actual != expected:
            raise SystemExit(f"digest mismatch for {name}: {actual}")
        print(f"PASS {expected} {size} {name}")

    print(f"ASSET_VERIFICATION=PASS_{len(seen_names)}_FILES")
    return 0


if __name__ == "__main__":
    sys.exit(main())
