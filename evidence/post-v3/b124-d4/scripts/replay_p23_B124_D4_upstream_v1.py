#!/usr/bin/env python3
"""Clean cached-boundary replay of the formerly omitted B124/D4 chain."""

from __future__ import annotations

import argparse
import contextlib
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time


PACKAGE = Path(__file__).resolve().parents[1]
SOURCE_REPOSITORY = PACKAGE / "repository"
PORTABLE = PACKAGE / "scripts/portable_python.py"
DEFAULT_SAGE = Path("/tmp/beal357-p23-sage-runtime-v1/env/bin/python")
ORIGINAL_ROOT = "/home/pcho/Documents/Codex/beal_357"
RELATIVE_PACKAGE = Path(
    "results/2026-08-31_p23_alternative_km_base_chart_screen_v1"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize(value, repository: Path):
    if isinstance(value, dict):
        return {
            key: normalize(item, repository)
            for key, item in value.items()
            if key not in {
                "wall_seconds", "elapsed_seconds", "output_cache", "padic_cache"
            }
        }
    if isinstance(value, list):
        return [normalize(item, repository) for item in value]
    if isinstance(value, str):
        return value.replace(str(repository), "<REPOSITORY>").replace(
            ORIGINAL_ROOT, "<REPOSITORY>"
        )
    return value


def clean_env(repository: Path, sage: Path) -> dict[str, str]:
    answer = {
        "PATH": "/usr/bin:/bin",
        "HOME": "/tmp",
        "DOT_SAGE": "/tmp/p23-B124-D4-upstream-dot-sage",
        "TMPDIR": "/tmp",
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONINTMAXSTRDIGITS": "0",
        "BEAL357_REPOSITORY_ROOT": str(repository),
        "BEAL357_SAGE_PYTHON": str(sage),
    }
    if os.environ.get("PYTHONPATH"):
        answer["PYTHONPATH"] = os.environ["PYTHONPATH"]
    return answer


def sage_load_check(repository: Path, sage: Path) -> str:
    evidence = repository / RELATIVE_PACKAGE / "evidence"
    program = r'''
from sage.all import GF, ZZ, Zmod, load
from pathlib import Path
import sys
p = Path(sys.argv[1])
finite = load(str(p / "p23_B124_graded_product_lattices_v1.sobj"))
assert finite["schema"] == "p23_B124_graded_product_lattices_cache_v1"
assert finite["base_divisor"] == ["P1", "P2", "P4"]
assert finite["target"] == "D=P4-P1"
assert {int(k): len(v) for k, v in finite["bases"].items()} == {2:10,3:16,4:22,5:28,6:34,7:40}
assert int(finite["base_matrices_mod23"]["w0"].rank()) == 10
assert int(finite["base_matrices_mod23"]["wD"].rank()) == 10
tensor = load(str(p / "p23_B124_padic_tensors_mod23power10_v1.sobj"))
assert tensor["schema"] == "p23_B124_padic_tensors_mod23power10_v1"
assert tensor["precisions"] == [8, 10]
classes = load(str(p / "p23_B124_padic_75D_classes_v1.sobj"))
assert classes["schema"] == "p23_B124_padic_75D_classes_v1"
assert classes["target"] == "D=P4-P1"
assert classes["precisions"] == [8, 10]
points = load(str(p / "p23_B124_75D_formal_chart_points_v1.sobj"))
assert points["schema"] == "p23_B124_75D_formal_chart_points_v1"
assert points["target"] == "75D where D=P4-P1"
assert points["precisions"] == [8, 10]
first = load(str(p / "p23_B124_first_branchwise_log_v1.sobj"))
assert first["schema"] == "p23_B124_first_branchwise_log_v1"
assert first["divisor"] == "D=P4-P1"
assert first["precisions"] == [8, 10]
print("SAGE_SERIALIZED_BOUNDARY=PASS_GRADED_TENSORS_75D_CHART_D4")
'''
    completed = subprocess.run(
        [str(sage), "-B", "-c", program, str(evidence)],
        cwd=repository,
        env=clean_env(repository, sage),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=300,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError(completed.stdout)
    return completed.stdout


def run_stage(repository: Path, sage: Path, source_relative: str,
              outputs: list[str], marker: str, timeout: int) -> str:
    package = repository / RELATIVE_PACKAGE
    source = package / "scripts" / source_relative
    originals = {package / relative: (package / relative).read_bytes()
                 for relative in outputs}
    started = time.monotonic()
    try:
        completed = subprocess.run(
            [str(sage), "-B", str(PORTABLE), "-B", str(source)],
            cwd=repository,
            env=clean_env(repository, sage),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
        if completed.returncode != 0 or marker not in completed.stdout:
            raise AssertionError((source_relative, completed.returncode,
                                  marker, completed.stdout))
        comparisons = []
        for output, original in originals.items():
            if output.suffix == ".json":
                old = json.loads(original.decode("utf-8"))
                new = json.loads(output.read_text(encoding="utf-8"))
                assert normalize(new, repository) == normalize(old, repository), output
                comparisons.append(output.name + "=INVARIANT_JSON_EXACT")
            else:
                assert output.stat().st_size > 0
                comparisons.append(
                    output.name + ("=CACHE_BYTES_EXACT" if output.read_bytes() == original
                                   else "=CACHE_REGENERATED_JSON_BINDS_MATHEMATICS")
                )
        return (
            f"STAGE={source_relative} EXIT=0 WALL_SECONDS={time.monotonic()-started:.6f}\n"
            + completed.stdout
            + "COMPARISONS=" + ",".join(comparisons) + "\n"
        )
    finally:
        for output, original in originals.items():
            output.write_bytes(original)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--load-check-only", action="store_true")
    parser.add_argument(
        "--start-stage",
        choices=("tensor", "scalar", "chart", "log"),
        default="tensor",
        help="resume the clean replay at an authenticated stage boundary",
    )
    parser.add_argument("--log")
    args = parser.parse_args()
    sage = Path(os.environ.get("BEAL357_SAGE_PYTHON", str(DEFAULT_SAGE))).resolve()
    if not sage.is_file():
        raise SystemExit("SageMath Python not found; set BEAL357_SAGE_PYTHON")
    transcript = io.StringIO()
    with contextlib.redirect_stdout(transcript):
        with tempfile.TemporaryDirectory(prefix="p23-B124-D4-upstream-") as temporary:
            repository = Path(temporary) / "repository"
            shutil.copytree(SOURCE_REPOSITORY, repository, symlinks=False)
            print("ORIGINAL_WORKSPACE_USED=false")
            print("SAGE_PYTHON=" + str(sage))
            print(sage_load_check(repository, sage), end="")
            if not args.load_check_only:
                stages = [
                    (
                        "build_p23_B124_padic_tensor_lift_v1.sage",
                        ["certificates/p23_B124_padic_tensor_lift_v1.json",
                         "evidence/p23_B124_padic_tensors_mod23power10_v1.sobj"],
                        "P23_B124_PADIC_TENSOR_STATUS=PASS_EXACT_PRODUCT_TENSOR_LIFT_MOD_23_POWER_8_AND_10",
                        1800,
                    ),
                    (
                        "replay_p23_B124_padic_KM_scalar75_v1.sage",
                        ["certificates/p23_B124_padic_KM_scalar75_v1.json",
                         "evidence/p23_B124_padic_75D_classes_v1.sobj"],
                        "P23_B124_PADIC_KM_STATUS=PASS_PADIC_KM_GROUP_LAW_AND_75D_AT_23_POWER_8_AND_10",
                        1800,
                    ),
                    (
                        "decode_p23_B124_75D_formal_chart_v1.sage",
                        ["certificates/p23_B124_75D_formal_chart_decode_v1.json",
                         "evidence/p23_B124_75D_formal_chart_points_v1.sobj"],
                        "P23_B124_FORMAL_DECODE_STATUS=PASS_75D_THREE_POINT_FORMAL_CHART_NEWTON_AT_23_POWER_8_AND_10",
                        1800,
                    ),
                    (
                        "compute_p23_B124_first_branchwise_log_v1.sage",
                        ["certificates/p23_B124_first_branchwise_log_v1.json",
                         "evidence/p23_B124_first_branchwise_log_v1.sobj"],
                        "P23_B124_FIRST_LOG_STATUS=PASS_FIRST_BRANCHWISE_ABELIAN_LOG_COLUMN_AT_23_POWER_8_AND_10",
                        1800,
                    ),
                ]
                start = {"tensor": 0, "scalar": 1, "chart": 2, "log": 3}[args.start_stage]
                print("REPLAY_START_STAGE=" + args.start_stage)
                for stage in stages[start:]:
                    print(run_stage(repository, sage, *stage), end="")
                if start == 0:
                    print("UPSTREAM_RECONSTRUCTION=PASS_TENSOR_75D_CLASS_FORMAL_CHART_D4_LOG")
                else:
                    print(
                        "UPSTREAM_RECONSTRUCTION="
                        f"PASS_AUTHENTICATED_BOUNDARY_FROM_{args.start_stage.upper()}_THROUGH_D4_LOG"
                    )
    rendered = transcript.getvalue()
    print(rendered, end="")
    if args.log:
        destination = Path(args.log).resolve()
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
