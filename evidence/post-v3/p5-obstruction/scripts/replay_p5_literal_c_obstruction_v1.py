#!/usr/bin/env python3
"""Clean-extraction arithmetic replay of the p=5 obstruction signs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time


PACKAGE = Path(__file__).resolve().parents[1]
ANSI = re.compile(r"\x1b\[[0-9;]*m")
SOURCE_REPOSITORY = PACKAGE / "repository"
PRODUCER = Path(
    "results/2026-08-26_literal_c_a26_residual_bits/scripts/"
    "certify_p5_literal_c_a26_candidate_late_v2.gp"
)
VERIFIER = Path(
    "results/2026-08-26_literal_c_a26_residual_bits/scripts/"
    "independent_verify_p5_literal_c_residue_bits_v2.gp"
)
FROZEN_PRODUCTION = Path(
    "results/2026-08-26_literal_c_a26_residual_bits/checkpoints/"
    "p5_literal_c_a26_candidate_late_v2.bin"
)
FROZEN_INDEPENDENT = Path(
    "results/2026-08-26_literal_c_a26_residual_bits/checkpoints/"
    "independent_p5_literal_c_a26_replay_v2.bin"
)
SPAN_SCRIPT = Path(
    "results/2026-08-26_literal_c_a26_residual_bits/scripts/"
    "independent_verify_p5_target_character_span_v1.py"
)
FROZEN_SPAN = Path(
    "results/2026-08-26_literal_c_a26_residual_bits/certificates/"
    "independent_p5_target_character_span_v1.json"
)


def sha256(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            result.update(block)
    return result.hexdigest()


def run(command: list[str], repository: Path, environment: dict[str, str], timeout: int) -> tuple[str, float]:
    started = time.monotonic()
    completed = subprocess.run(
        command,
        cwd=repository,
        env=environment,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=False,
    )
    elapsed = time.monotonic() - started
    if completed.returncode != 0:
        raise AssertionError((command, completed.returncode, completed.stdout))
    return ANSI.sub("", completed.stdout), elapsed


def compare_gp_objects(gp: Path, repository: Path, left: Path, right: Path,
                       environment: dict[str, str], label: str) -> str:
    program = (
        f'A=read("{left}");B=read("{right}");'
        f'if(A!=B,error("{label}"));print("{label}=EXACT_GP_OBJECT");quit\n'
    )
    completed = subprocess.run(
        [str(gp), "-q", "-f"], cwd=repository, env=environment,
        input=program, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, timeout=300, check=False,
    )
    if completed.returncode != 0:
        raise AssertionError((label, completed.stdout))
    return ANSI.sub("", completed.stdout)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log")
    parser.add_argument("--gp", default="/usr/bin/gp")
    args = parser.parse_args()
    gp = Path(args.gp)
    if not gp.is_file():
        raise SystemExit("PARI/GP not found; pass --gp PATH")

    with tempfile.TemporaryDirectory(prefix="p5-obstruction-clean-") as temporary:
        repository = Path(temporary) / "repository"
        shutil.copytree(SOURCE_REPOSITORY, repository, symlinks=False)
        output = Path(temporary) / "production.bin"
        independent = Path(temporary) / "independent.bin"
        span_output = Path(temporary) / "target-character-span.json"
        common = {
            "PATH": "/usr/bin:/bin",
            "HOME": "/tmp",
            "LANG": "C",
            "LC_ALL": "C",
        }
        producer_env = dict(common)
        producer_env["P5_LITERAL_C_OUTPUT"] = str(output)
        producer_stdout, producer_wall = run(
            [str(gp), "-q", str(repository / PRODUCER)], repository,
            producer_env, 3600,
        )
        assert "STATUS=PASS_P5_LITERAL_C_A26_CANDIDATE_LATE_V2" in producer_stdout
        production_comparison = compare_gp_objects(
            gp, repository, output, repository / FROZEN_PRODUCTION,
            common, "PRODUCTION_RECORD",
        )

        verifier_env = dict(common)
        verifier_env["P5_LITERAL_C_PRODUCTION"] = str(output)
        verifier_env["P5_LITERAL_C_VERIFY_OUTPUT"] = str(independent)
        verifier_stdout, verifier_wall = run(
            [str(gp), "-q", str(repository / VERIFIER)], repository,
            verifier_env, 3600,
        )
        assert "STATUS=PASS_INDEPENDENT_P5_LITERAL_C_A26_REPLAY_V2" in verifier_stdout
        independent_comparison = compare_gp_objects(
            gp, repository, independent, repository / FROZEN_INDEPENDENT,
            common, "INDEPENDENT_RECORD",
        )
        assert "P5_LITERAL_C_SIGNS=[-1, 1, -1]" in producer_stdout
        assert "INDEPENDENT_P5_LITERAL_C_SIGNS=[-1, 1, -1]" in verifier_stdout
        span_stdout, span_wall = run(
            ["/usr/bin/python3", "-B", str(repository / SPAN_SCRIPT),
             "--output", str(span_output)],
            repository, common, 900,
        )
        assert "STATUS=PASS_INDEPENDENT_P5_TARGET_CHARACTER_SPAN_V1" in span_stdout
        assert json.loads(span_output.read_text()) == json.loads(
            (repository / FROZEN_SPAN).read_text()
        )

        rendered = (
            "ORIGINAL_WORKSPACE_USED=false\n"
            f"PARI_GP={gp}\n"
            f"PRODUCER_WALL_SECONDS={producer_wall:.6f}\n"
            + producer_stdout
            + f"INDEPENDENT_WALL_SECONDS={verifier_wall:.6f}\n"
            + verifier_stdout
            + production_comparison
            + independent_comparison
            + f"TARGET_CHARACTER_SPAN_WALL_SECONDS={span_wall:.6f}\n"
            + span_stdout
            + "TARGET_CHARACTER_RECORD=EXACT_JSON_TO_FROZEN\n"
            + "P5_OBSTRUCTION_REPLAY=PASS_ROOT00_10_ROOT11_01_BOTH_NONZERO\n"
        )
        print(rendered, end="")
        if args.log:
            destination = Path(args.log).resolve()
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(rendered)


if __name__ == "__main__":
    main()
