#!/usr/bin/env python3
"""Conservative Hecke-coverage certificate for the mod-7 terminal step.

The historical packet logs were computed after eighteen necessary local-trace
filters; they are not the full cusp spaces.  The companion filter audit finds
that the archived ell=131 polynomial omits an allowed level-lowering trace.
Here we compile an in-memory one-site conservative repair (x^49-x, hence no
filter at 131), rebuild all four relevant filtered ambient spaces, enumerate
every T_2-compatible packet, and check that every resulting T_29 annihilator
is already among the six terminal factors.  No old/new subtraction is used.
"""

from __future__ import annotations

import ast
import hashlib
import os
from pathlib import Path
import re
import runpy
import subprocess
import sys
import tempfile


HERE = Path(__file__).resolve()
if os.environ.get("BEAL357_REPOSITORY_ROOT"):
    REPOSITORY = Path(os.environ["BEAL357_REPOSITORY_ROOT"]).resolve()
elif (HERE.parents[1] / "repository").is_dir():
    REPOSITORY = (HERE.parents[1] / "repository").resolve()
else:
    REPOSITORY = HERE.parents[3]
PROJECT = REPOSITORY / "beal_357_spark_handover_2026-08-20/project"
PROJECT_MANIFEST = PROJECT / "SHA256SUMS_357.txt"
PROJECT_MANIFEST_SHA256 = "6621e1217bda1859c5ba90b1862ad25c0b512b36e95c1542e7c84358793fc1a1"
LEVELS = ("22", "23", "32", "33")
ELLS = (11, 13, 17, 19, 29, 31, 41, 59, 61, 71,
        79, 89, 101, 109, 131, 139, 149, 151, 7, 2)
EXPECTED = {
    "22": (9, 8, 4),
    "23": (39, 38, 14),
    "32": (29, 28, 12),
    "33": (99, 98, 24),
}
ORIGINAL_C_SHA256 = "ea5a509f854c00966171021151163c1db143d4aea2d7b38187c78bf0c8a91920"
SAFE_C_SHA256 = "b90f6fb5aa1cff02348fa19c72965c8769e3701c9131620be9ac094693c728ca"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_project_rows() -> None:
    assert sha256(PROJECT_MANIFEST) == PROJECT_MANIFEST_SHA256
    rows = {}
    for line in PROJECT_MANIFEST.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  \./([^\x00\r\n]+)", line)
        assert match, line
        digest, relative = match.groups()
        assert relative not in rows
        rows[relative] = digest
    assert rows["p7_level33_mod7_intersection.c"] == ORIGINAL_C_SHA256
    assert sha256(PROJECT / "p7_level33_mod7_intersection.c") == ORIGINAL_C_SHA256
    local = "p7_odd_branch_local2_certificate.py"
    assert rows[local] == "71857eeedcd09eac374fed20613ac6fed72c94e7bc2efc3dbd97f81e34a47ab6"
    assert sha256(PROJECT / local) == rows[local]


def parse_level(level: str, text: str):
    assert "all 190 pairwise integer Hecke commutativity checks: PASS" in text
    assert "all restricted Hecke commutativity checks: PASS" in text
    full = int(re.search(
        r"after ell=151 \(degree 49\): full intersection=(\d+)", text
    ).group(1))
    cusp = int(re.search(r"exact mass-kernel cusp dimension: (\d+)", text).group(1))
    assert (full, cusp) == EXPECTED[level][:2]
    packets = []
    seen = set()
    for line in text.splitlines():
        match = re.match(r"joint packet f=(\d+) m=(\d+) signature: (.*)", line)
        if not match:
            continue
        signature = tuple(
            tuple(ast.literal_eval(item))
            for item in re.findall(r"\[[^]]*\]", match.group(3))
        )
        assert len(signature) == len(ELLS) and signature not in seen
        seen.add(signature)
        packets.append((int(match.group(1)), int(match.group(2)), signature))
    assert sum(degree * multiplicity for degree, multiplicity, _ in packets) == cusp
    assert len(packets) == EXPECTED[level][2]
    return packets


def safe_source() -> str:
    text = (PROJECT / "p7_level33_mod7_intersection.c").read_text()
    old_degrees = "33,7,7,34,35,42,38,37,39,43,44,47,48,48,48,49,49,49"
    new_degrees = "33,7,7,34,35,42,38,37,39,43,44,47,48,48,49,49,49,49"
    old_route = "A101,A109,A131,A139,A139,A139"
    new_route = "A101,A109,A139,A139,A139,A139"
    assert text.count(old_degrees) == text.count(old_route) == 1
    repaired = text.replace(old_degrees, new_degrees).replace(old_route, new_route)
    assert hashlib.sha256(repaired.encode()).hexdigest() == SAFE_C_SHA256
    return repaired


def command_for(level: str) -> list[str]:
    if level == "33":
        return [sys.executable, "-B", "p7_level33_quaternion_certificate.py",
                "--sparse-all-inert"]
    return [sys.executable, "-B", "p7_lower_levels_quaternion_certificate.py",
            level, "--with-inert"]


def rebuild_safe_spaces() -> dict[str, str]:
    prefix = Path(os.environ.get(
        "BEAL357_FLINT_PREFIX", "/tmp/beal357-p23-sage-runtime-v1/env"
    ))
    assert (prefix / "include/flint/flint.h").is_file()
    assert (prefix / "lib/libflint.so").is_file()
    with tempfile.TemporaryDirectory(prefix="primitive357-safe-hecke-") as temporary:
        root = Path(temporary)
        source = root / "p7_level33_mod7_intersection_coverage_safe.c"
        binary = root / "p7_level33_mod7_intersection_coverage_safe"
        source.write_text(safe_source(), encoding="utf-8", newline="\n")
        compile_command = [
            "/usr/bin/cc", "-O2", "-std=gnu11",
            "-I" + str(prefix / "include"), str(source),
            "-L" + str(prefix / "lib"),
            "-Wl,-rpath," + str(prefix / "lib"),
            "-o", str(binary), "-lflint", "-lgmp",
        ]
        compiled = subprocess.run(
            compile_command, check=False, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        assert compiled.returncode == 0, compiled.stdout
        environment = {
            "PATH": "/usr/bin:/bin", "HOME": "/tmp",
            "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8",
            "PYTHONDONTWRITEBYTECODE": "1",
            "LD_LIBRARY_PATH": str(prefix / "lib"),
        }
        outputs = {}
        for level in LEVELS:
            generator = subprocess.Popen(
                command_for(level), cwd=PROJECT, env=environment,
                stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            assert generator.stdout is not None
            consumer = subprocess.Popen(
                [str(binary)], cwd=PROJECT, env=environment,
                stdin=generator.stdout, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, text=True,
            )
            generator.stdout.close()
            output, consumer_error = consumer.communicate(timeout=1800)
            generator_error = generator.stderr.read().decode("utf-8", "replace")
            generator_status = generator.wait(timeout=30)
            assert generator_status == 0 and consumer.returncode == 0
            assert not generator_error and not consumer_error
            outputs[level] = output
        return outputs


def evaluates_to_zero(poly, value: int) -> bool:
    return sum(coefficient * pow(value, exponent, 7)
               for exponent, coefficient in enumerate(poly)) % 7 == 0


def local_t2_traces() -> tuple[int, int]:
    module = runpy.run_path(str(PROJECT / "p7_odd_branch_local2_certificate.py"))
    x_even = module["frobenius_data"]("X-even")
    y_even = module["frobenius_data"]("Y-even")
    assert x_even == (3, 7, (1, 0, 1, 0, 4), (1, 2, 9, 8, 16))
    assert y_even == (3, 5, (1, 0, 0, 0, 4), (1, 0, 8, 0, 16))
    return -1, 0


def determinant_bareiss(matrix):
    values = [list(row) for row in matrix]
    previous, sign = 1, 1
    for k in range(len(values) - 1):
        if values[k][k] == 0:
            swap = next(i for i in range(k + 1, len(values)) if values[i][k])
            values[k], values[swap] = values[swap], values[k]
            sign *= -1
        pivot = values[k][k]
        for i in range(k + 1, len(values)):
            for j in range(k + 1, len(values)):
                numerator = values[i][j] * pivot - values[i][k] * values[k][j]
                assert numerator % previous == 0
                values[i][j] = numerator // previous
        previous = pivot
    return sign * values[-1][-1]


def resultant(f, g):
    m, n = len(f) - 1, len(g) - 1
    fd, gd = list(reversed(f)), list(reversed(g))
    size = m + n
    rows = []
    for i in range(n):
        rows.append([0] * i + fd + [0] * (size - i - len(fd)))
    for i in range(m):
        rows.append([0] * i + gd + [0] * (size - i - len(gd)))
    return determinant_bareiss(rows)


def main() -> None:
    verify_project_rows()
    traces = local_t2_traces()
    outputs = rebuild_safe_spaces()
    selected_counts = {}
    ambient_q29 = set()
    for level in LEVELS:
        print(f"===== BEGIN CONSERVATIVE FILTERED AMBIENT LEVEL {level} =====")
        print(outputs[level], end="" if outputs[level].endswith("\n") else "\n")
        print(f"===== END CONSERVATIVE FILTERED AMBIENT LEVEL {level} =====")
        packets = parse_level(level, outputs[level])
        selected_counts[level] = {}
        for trace in traces:
            selected = [row for row in packets if evaluates_to_zero(row[2][19], trace)]
            selected_counts[level][str(trace)] = len(selected)
            ambient_q29.update(row[2][4] for row in selected)
    assert selected_counts == {
        "22": {"-1": 1, "0": 2},
        "23": {"-1": 2, "0": 10},
        "32": {"-1": 2, "0": 3},
        "33": {"-1": 5, "0": 11},
    }
    expected_ambient = {
        (0, 1), (0, 0, 1), (2, 1), (2, 5, 1), (4, 3, 1),
    }
    assert ambient_q29 == expected_ambient

    # The last two factors are the independently enumerated reducible branch.
    annihilators = [(0, 1), (0, 0, 1), (2, 5, 1), (4, 3, 1), (-2, 1), (-5, 1)]
    curves = [(6, 6, 1), (4, 6, 1), (4, 0, 1), (3, 2, 1)]
    matrix = [[resultant(curve, test) % 7 for test in annihilators] for curve in curves]
    assert matrix == [[6, 1, 5, 1, 1, 5],
                      [4, 2, 3, 1, 6, 3],
                      [4, 2, 6, 1, 1, 1],
                      [3, 2, 6, 2, 4, 3]]
    assert all(value for row in matrix for value in row)

    print("HECKE_LEVEL_LOWERING_TARGETS=FOUR_NEWSPACES_AT_LEVELS_22_23_32_33")
    print("COVERAGE_METHOD=CONSERVATIVELY_FILTERED_AMBIENT_SUPERSET_NO_OLD_NEW_SUBTRACTION")
    print("ELL_131_FILTER=X49_MINUS_X_ALL_F49_TRACES")
    print("FILTERED_PACKET_DIMENSION_COVERAGE=PASS_SUM_PACKET_DIMENSIONS_EQUALS_FILTERED_CUSP_AT_ALL_FOUR_LEVELS")
    print("LOCAL_T2_TRACES=X_EVEN_MINUS1_Y_EVEN_ZERO")
    print("AMBIENT_SELECTED_PACKET_OCCURRENCES=36")
    print("AMBIENT_Q29_ANNIHILATORS=T,T2,T_PLUS_2,T2_PLUS_5T_PLUS_2,T2_PLUS_3T_PLUS_4")
    print("REDUCIBLE_Q29_ANNIHILATORS=T_MINUS_2,T_MINUS_5")
    print("AMBIENT_T_PLUS_2_EQUALS_EXISTING_TERMINAL_T_MINUS_5_MOD_7")
    print("RESULTANT_MATRIX=PASS_24_OF_24_NONZERO_MOD_7")
    print("PASS_HILBERT_HECKE_CONSERVATIVE_FILTERED_AMBIENT_COVERAGE_NO_NEWSPACE_SUBTRACTION")


if __name__ == "__main__":
    main()
