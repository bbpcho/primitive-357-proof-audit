"""Shared, optimization-independent validation for the control repository."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat

HEX64 = re.compile(r"[0-9a-f]{64}\Z")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def relative_path(value):
    require(isinstance(value, str) and value and "\\" not in value
            and all(ord(c) >= 32 for c in value), "malformed relative path")
    rel = PurePosixPath(value)
    require(not rel.is_absolute() and ".." not in rel.parts
            and str(rel) == value and value != ".", "unsafe relative path: " + value)
    return rel


def regular_file(root, value):
    rel = relative_path(value)
    path = root
    for i, part in enumerate(rel.parts):
        path = path / part
        mode = path.lstat().st_mode
        require(not stat.S_ISLNK(mode), "symlink in file path: " + str(path))
        require(stat.S_ISREG(mode) if i == len(rel.parts) - 1 else stat.S_ISDIR(mode),
                "not a regular file/directory path: " + str(path))
    return path


def read_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key: " + key)
            result[key] = value
        return result
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs)


def digest_value(value):
    require(isinstance(value, str) and HEX64.fullmatch(value), "invalid SHA-256")
    return value


def unique_records(rows, name="id"):
    require(isinstance(rows, list) and rows, "empty or invalid record list")
    result = {}
    for row in rows:
        require(isinstance(row, dict), "record must be an object")
        key = row[name]
        require(isinstance(key, str) and key and key not in result,
                "empty or duplicate " + name + ": " + repr(key))
        result[key] = row
    return result


def asset_index(root):
    data = read_json(regular_file(root, "evidence/assets.json"))
    require(data.get("schema") == "primitive_357_release_asset_index_v1", "asset schema")
    assets = data["assets"]
    unique_records(assets)
    unique_records(assets, "filename")
    for item in assets:
        require(len(relative_path(item["filename"]).parts) == 1, "unsafe asset filename")
        digest_value(item["sha256"])
        require(type(item["bytes"]) is int and item["bytes"] > 0, "invalid asset byte size")
        relative_path(item["source_path_from_workspace"])
    lines = regular_file(root, "evidence/checksums/RELEASE_ASSETS_SHA256.txt").read_text().splitlines()
    require(lines == [f"{item['sha256']}  {item['filename']}" for item in assets],
            "asset checksum list does not equal the indexed asset list")
    return assets


def manifest_rows(data):
    require(data.get("schema") == "primitive357_verified_release_manifest_v1", "release manifest schema")
    rows = unique_records(data["files"], "path")
    require(list(rows) == sorted(rows), "release manifest is not sorted")
    for path, row in rows.items():
        relative_path(path)
        digest_value(row["sha256"])
        require(type(row["bytes"]) is int and row["bytes"] >= 0, "invalid manifest byte size")
    return rows
