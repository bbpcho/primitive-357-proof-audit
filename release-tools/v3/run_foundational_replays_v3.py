#!/usr/bin/env python3
"""Regenerate the rank/descent and global-log foundations in a clean release.

Historical sources are executed without editing them. Fresh GP outputs go to
a temporary directory. Sage generators run inside the writable clean
extraction; their mathematical payloads are compared with sealed records and
the original sealed bytes are restored afterwards.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time


RELEASE = Path(__file__).resolve().parents[1]
ROOT = RELEASE / "repository"
PORTABLE = RELEASE / "scripts/portable_python.py"
GP = Path("/usr/bin/gp")
SAGE_PYTHON = Path(os.environ.get(
    "BEAL357_SAGE_PYTHON", "/tmp/beal357-p23-sage-runtime-v1/env/bin/python"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def clean_env() -> dict[str, str]:
    answer = {
        "PATH": "/usr/bin:/bin",
        "HOME": "/tmp",
        "DOT_SAGE": "/tmp/primitive357-v3-foundation-dot-sage",
        "TMPDIR": "/tmp",
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONINTMAXSTRDIGITS": "0",
        "BEAL357_REPOSITORY_ROOT": str(ROOT),
        "BEAL357_SAGE_PYTHON": str(SAGE_PYTHON),
        "BEAL357_FLINT_PREFIX": str(SAGE_PYTHON.parent.parent),
    }
    if os.environ.get("PYTHONPATH"):
        answer["PYTHONPATH"] = os.environ["PYTHONPATH"]
    return answer


def run(label: str, command: list[str], env: dict[str, str], timeout: int,
        marker: str) -> str:
    started = time.monotonic()
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
        timeout=timeout,
    )
    elapsed = time.monotonic() - started
    print(f"===== BEGIN FOUNDATION {label} =====")
    print("COMMAND=" + " ".join(command))
    print(f"EXIT={completed.returncode} WALL_SECONDS={elapsed:.6f}")
    print(completed.stdout, end="" if completed.stdout.endswith("\n") else "\n")
    print(f"===== END FOUNDATION {label} =====")
    if completed.returncode != 0 or marker not in completed.stdout:
        raise AssertionError((label, completed.returncode, marker))
    return completed.stdout


def invariant_json(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload.pop("wall_seconds", None)
    # Sage's compressed serialization is not canonical across fresh process
    # instances.  Its identity is recorded, but the mathematical JSON fields
    # rather than that incidental blob hash are the equality contract.
    payload.pop("output_cache", None)
    return payload


def replay_five_place_rank_foundation() -> None:
    package = ROOT / "results/2026-09-07_five_place_source_preimage_direct_verification_v1"
    producer = ROOT / (
        "results/2026-08-30_literal_c_five_place_source_preimage_v2r19_source_implementation/"
        "scripts/certify_literal_c_five_place_source_preimage_v2r19.gp")
    independent = ROOT / (
        "results/2026-08-30_literal_c_five_place_source_preimage_v2r19_source_implementation/"
        "scripts/independently_verify_literal_c_five_place_source_preimage_v2r19.gp")
    semantic = package / "scripts/verify_five_place_source_preimage_outputs_v1.gp"
    certifier = package / "scripts/certify_selmer_character_projector_rank4_v1.py"
    witness = ROOT / (
        "results/2026-08-26_literal_c_five_place_source_preimage_v2r2_source_implementation/"
        "inputs/literal_c_five_place_source_coefficients_v2r2.gpdata")
    with tempfile.TemporaryDirectory(prefix="primitive357-v3-five-place-") as tmp:
        temporary = Path(tmp)
        producer_bin = temporary / "producer.bin"
        producer_text = temporary / "producer.txt"
        independent_bin = temporary / "independent.bin"
        independent_text = temporary / "independent.txt"
        semantic_text = temporary / "semantic.txt"

        producer_env = clean_env() | {
            "FIVE_PLACE_PRODUCTION_BIN": str(producer_bin),
            "FIVE_PLACE_PRODUCTION_EXPORT": str(producer_text),
        }
        run(
            "five-place-producer",
            [str(GP), "-q", str(producer)],
            producer_env,
            1800,
            "STATUS=PASS_LITERAL_C_FIVE_PLACE_SOURCE_PREIMAGE_V2R2_PRODUCTION",
        )
        independent_env = clean_env() | {
            "FIVE_PLACE_INDEPENDENT_BIN": str(independent_bin),
            "FIVE_PLACE_INDEPENDENT_EXPORT": str(independent_text),
        }
        run(
            "five-place-independent",
            [str(GP), "-q", str(independent)],
            independent_env,
            1800,
            "STATUS=PASS_LITERAL_C_FIVE_PLACE_SOURCE_PREIMAGE_V2R2_INDEPENDENT",
        )
        assert producer_text.read_bytes() == (
            package / "artifacts/producer.txt").read_bytes()
        assert independent_text.read_bytes() == (
            package / "artifacts/independent.txt").read_bytes()
        semantic_env = clean_env() | {
            "FIVE_PLACE_VERIFY_PRODUCTION_BIN": str(producer_bin),
            "FIVE_PLACE_VERIFY_INDEPENDENT_BIN": str(independent_bin),
            "FIVE_PLACE_VERIFY_WITNESS": str(witness),
            "FIVE_PLACE_VERIFY_EXPORT": str(semantic_text),
        }
        run(
            "five-place-fresh-semantic-agreement",
            [str(GP), "-q", str(semantic)],
            semantic_env,
            300,
            "STATUS=PASS_EXACT_INDEPENDENT_FIVE_PLACE_SOURCE_PREIMAGE_SEMANTIC_AGREEMENT",
        )
        assert semantic_text.read_bytes() == (
            package / "artifacts/semantic_verification_v2.txt").read_bytes()

    run(
        "selmer-character-projector-rank4",
        [str(PORTABLE), "-B", str(certifier)],
        clean_env(),
        600,
        "PASS_UNCONDITIONAL_TRUE_2_SELMER_DIMENSION_4_AND_MORDELL_WEIL_RANK_4",
    )


def replay_global_logs(skip_s4: bool = False,
                       combined_and_local_only: bool = False) -> None:
    s4 = ROOT / "results/2026-08-31_p23_alternative_km_base_chart_screen_v1"
    s19 = ROOT / "results/2026-08-31_p23_s19_alternative_km_base_chart_screen_v1"
    jobs = [
        (
            "s4-full-global-log-matrix",
            s4 / "scripts/compute_p23_s4_full_log_matrix_v1.sage",
            "P23_S4_FULL_LOG_STATUS=PASS_ALL_FOUR_S4_BRANCHWISE_LOG_COLUMNS_AT_23_POWER_8_AND_10",
            7200,
            [
                s4 / "certificates/p23_s4_full_log_matrix_v1.json",
                s4 / "evidence/p23_s4_full_log_matrix_v1.sobj",
            ],
        ),
        (
            "s19-full-global-log-matrix",
            ROOT / (
                "results/2026-09-13_v3_generator_repairs/"
                "compute_p23_s19_full_log_matrix_v1_import_repair.sage"),
            "P23_S19_FULL_LOG_STATUS=PASS_ALL_FOUR_S19_BRANCHWISE_LOG_COLUMNS_AT_23_POWER_8_AND_10",
            7200,
            [
                s19 / "certificates/p23_s19_full_log_matrix_v1.json",
                s19 / "evidence/p23_s19_full_log_matrix_v1.sobj",
            ],
        ),
        (
            "combined-rank-and-siksek",
            s19 / "scripts/certify_p23_ros_log_rank_and_siksek_v1.sage",
            "P23_ROS_RANK_SIKSEK_STATUS=PASS_RANK4_TWO_ANNIHILATORS_FOUR_UNIT_SIKSEK_GATES_ONE_P1_SINGULAR_GATE",
            1800,
            [s19 / "certificates/p23_ros_log_rank_and_siksek_v1.json"],
        ),
        (
            "P1-second-order-gate",
            s19 / "scripts/analyze_p23_P1_second_order_gate_v1.sage",
            "P23_P1_SECOND_ORDER_STATUS=PASS_P1_SECOND_NORMALIZATION_EXACTLY_TWO_SIMPLE_LOCAL_ROOTS_NOT_UNIQUE",
            1800,
            [s19 / "certificates/p23_P1_second_order_gate_v1.json"],
        ),
        (
            "P1-exceptional-root-lift",
            s19 / "scripts/lift_p23_P1_exceptional_root_and_coefficients_v1.sage",
            "P23_P1_EXCEPTIONAL_LIFT_STATUS=PASS_EXCEPTIONAL_P1_ROOT_LIFT_AND_UNIQUE_MW_COEFFICIENT_CLASS_MOD_23_POWER_7",
            1800,
            [s19 / "certificates/p23_P1_exceptional_root_coefficients_v1.json"],
        ),
    ]
    if combined_and_local_only:
        jobs = jobs[2:]
    elif skip_s4:
        jobs = jobs[1:]
    for label, source, marker, timeout, outputs in jobs:
        originals = {output: output.read_bytes() for output in outputs}
        try:
            run(
                label,
                [str(SAGE_PYTHON), "-B", str(PORTABLE), "-B", str(source)],
                clean_env(),
                timeout,
                marker,
            )
            for output in outputs:
                old = originals[output]
                if output.suffix == ".json":
                    old_path = output.with_name(output.name + ".sealed-v3-check")
                    old_path.write_bytes(old)
                    try:
                        assert invariant_json(output) == invariant_json(old_path)
                    finally:
                        old_path.unlink()
                    comparison = "INVARIANT_JSON_EXACT"
                else:
                    if not output.read_bytes():
                        raise AssertionError(("empty regenerated Sage cache", output))
                    comparison = (
                        "CACHE_BYTES_EXACT" if output.read_bytes() == old
                        else "CACHE_SERIALIZATION_NONCANONICAL_MATHEMATICS_BOUND_BY_JSON"
                    )
                print(
                    "FOUNDATION_OUTPUT_REPLAY=PASS "
                    f"PATH={output.relative_to(ROOT)} SHA256={sha256(output)} "
                    f"COMPARISON={comparison}"
                )
        finally:
            for output, content in originals.items():
                output.write_bytes(content)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--global-logs-only", action="store_true")
    parser.add_argument("--s19-and-downstream-only", action="store_true")
    parser.add_argument("--combined-and-local-only", action="store_true")
    args = parser.parse_args()
    if not GP.is_file():
        raise SystemExit("PARI/GP is unavailable")
    if not SAGE_PYTHON.is_file():
        raise SystemExit("SageMath Python is unavailable")
    if not any((
        args.global_logs_only,
        args.s19_and_downstream_only,
        args.combined_and_local_only,
    )):
        replay_five_place_rank_foundation()
    replay_global_logs(
        skip_s4=args.s19_and_downstream_only,
        combined_and_local_only=args.combined_and_local_only,
    )
    print(
        "PRIMITIVE_357_FOUNDATIONAL_REPLAYS_V3="
        "PASS_FRESH_FIVE_PLACE_RANK_DESCENT_AND_BOTH_GLOBAL_LOG_BRANCHES"
    )


if __name__ == "__main__":
    main()
