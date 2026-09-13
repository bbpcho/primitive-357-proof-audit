#!/usr/bin/env python3
"""Verify that every preceding Hecke filter is a sound Frey-trace superset.

The Brandt consumer first intersects with eighteen allowed-polynomial
kernels.  This verifier reconstructs those eighteen polynomials from the
authors' complete Data.txt, rather than assuming that the final packet logs
are full ambient cusp spaces.  It also checks the exact upstream source
snapshot and the exhaustive loops which generate the ordinary and two
degenerate local cases.  The mathematical use of those three cases plus the
level-lowering case is the published Mazur-method trichotomy.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


HERE = Path(__file__).resolve()
RELEASE = HERE.parents[1]
if (RELEASE / "repository").is_dir():
    REPOSITORY = RELEASE / "repository"
else:
    REPOSITORY = HERE.parents[3]
PROJECT = REPOSITORY / "beal_357_spark_handover_2026-08-20/project"
UPSTREAM = RELEASE / "third_party/GFE-5p3"
P = 7
ELLS = (11, 13, 17, 19, 29, 31, 41, 59, 61, 71,
        79, 89, 101, 109, 131, 139, 149, 151)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def trim(a: tuple[int, ...]) -> tuple[int, ...]:
    values = list(value % P for value in a)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return trim(tuple(
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(max(len(a), len(b)))
    ))


def mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % P
    return trim(tuple(out))


def scale(a: tuple[int, ...], c: int) -> tuple[int, ...]:
    return trim(tuple(c * value for value in a))


def divmod_poly(a: tuple[int, ...], b: tuple[int, ...]):
    a = list(trim(a)); b = trim(b)
    assert b != (0,)
    quotient = [0] * max(1, len(a) - len(b) + 1)
    inverse = pow(b[-1], -1, P)
    while len(a) >= len(b) and any(a):
        degree = len(a) - len(b)
        coefficient = a[-1] * inverse % P
        quotient[degree] = coefficient
        for i, value in enumerate(b):
            a[degree + i] = (a[degree + i] - coefficient * value) % P
        while len(a) > 1 and a[-1] == 0:
            a.pop()
    return trim(tuple(quotient)), trim(tuple(a))


def monic(a: tuple[int, ...]) -> tuple[int, ...]:
    a = trim(a)
    return scale(a, pow(a[-1], -1, P))


def gcd_poly(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    while trim(b) != (0,):
        _, remainder = divmod_poly(a, b)
        a, b = b, remainder
    return monic(a)


def lcm_poly(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    divisor = gcd_poly(a, b)
    quotient, remainder = divmod_poly(a, divisor)
    assert remainder == (0,)
    return monic(mul(quotient, b))


def squarefree_part(a: tuple[int, ...]) -> tuple[int, ...]:
    derivative = trim(tuple(i * a[i] for i in range(1, len(a))))
    if derivative == (0,):
        raise AssertionError(("inseparable p-th-power filter", a))
    divisor = gcd_poly(a, derivative)
    quotient, remainder = divmod_poly(a, divisor)
    assert remainder == (0,)
    return monic(quotient)


def compose_quadratic(poly: tuple[int, ...], constant: int) -> tuple[int, ...]:
    """Return poly(x^2 + constant) over F_7."""
    base = (constant % P, 0, 1)
    result = (0,)
    for coefficient in reversed(poly):
        result = add(mul(result, base), (coefficient,))
    return monic(result)


def order_mod(a: int, modulus: int) -> int:
    value = 1
    for exponent in range(1, 100):
        value = value * a % modulus
        if value == 1:
            return exponent
    raise AssertionError((a, modulus))


def verify_upstream_snapshot() -> None:
    origin = json.loads((UPSTREAM / "UPSTREAM_ORIGIN.json").read_text())
    assert origin["commit"] == "e88f914c577ab6cf9a45e5cdd82c1993477fb423"
    manifest = UPSTREAM / "UPSTREAM_SHA256SUMS.txt"
    seen = set()
    for line in manifest.read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\x00\r\n]+)", line)
        assert match, line
        digest, relative = match.groups()
        path = Path(relative)
        assert not path.is_absolute() and ".." not in path.parts and relative not in seen
        seen.add(relative)
        target = UPSTREAM / path
        assert target.is_file() and not target.is_symlink() and sha256(target) == digest
    actual = {
        path.relative_to(UPSTREAM).as_posix()
        for path in UPSTREAM.rglob("*") if path.is_file()
    }
    assert actual == seen | {"UPSTREAM_SHA256SUMS.txt"}


def verify_data_reduction() -> str:
    command = [
        sys.executable, "-B", str(PROJECT / "verify_p7_data_mod7.py"),
        str(UPSTREAM / "Outputs/Data.txt"),
        str(PROJECT / "p7_level23_data_mod7.m"),
    ]
    completed = subprocess.run(
        command, check=False, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    assert completed.returncode == 0, completed.stdout
    marker = "PASS: 6253 polynomials at 37 primes independently parsed"
    assert marker in completed.stdout
    return completed.stdout.strip()


def parse_candidates() -> dict[int, list[list[tuple[int, ...]]]]:
    text = (PROJECT / "p7_level23_data_mod7.m").read_text()
    records = {}
    record_re = re.compile(r"^<(\d+),(.*)>[,]?$", re.MULTILINE)
    group_re = re.compile(
        r"\[(?:R7!\[[0-6](?:,[0-6])*\](?:,R7!\[[0-6](?:,[0-6])*\])*)?\]"
    )
    poly_re = re.compile(r"R7!\[([0-6](?:,[0-6])*)\]")
    for record in record_re.finditer(text):
        ell = int(record.group(1))
        groups = []
        for group_text in group_re.findall(record.group(2)):
            groups.append([
                tuple(map(int, coefficients.split(",")))
                for coefficients in poly_re.findall(group_text)
            ])
        assert len(groups) == 3 and ell not in records
        records[ell] = groups
    assert len(records) == 37
    return records


def parse_consumer_arrays() -> dict[str, tuple[int, ...]]:
    text = (PROJECT / "p7_level33_mod7_intersection.c").read_text()
    arrays = {}
    for name, body in re.findall(
        r"static const unsigned char (A\w+)\[\]=\{(.*?)\};", text, re.DOTALL
    ):
        arrays[name] = tuple(map(int, re.findall(r"\d+", body)))
    return arrays


def allowed_polynomial(ell: int, groups) -> tuple[int, ...]:
    if ell % 5 not in (1, 4):
        # At an inert rational prime the K-rational trace lies in F_7.
        return (0, 6, 0, 0, 0, 0, 0, 1)  # x^7-x
    relative_degree = order_mod(ell % 15, 15)
    assert relative_degree in (1, 2)
    factors = list(groups[0])
    for group in groups[1:]:
        for polynomial in group:
            factors.append(
                polynomial if relative_degree == 1
                else compose_quadratic(polynomial, -2 * ell)
            )
    qplus = (ell + 1) % P
    factors.extend(((-qplus % P, 1), (qplus, 1)))
    answer = (1,)
    for factor in factors:
        answer = lcm_poly(answer, squarefree_part(monic(factor)))
    return answer


def verify_generation_loops() -> None:
    source = (UPSTREAM / "Codes/GPcode.gp").read_text()
    required = (
        "parfor(i=2,p-1,algdep(p^f*hgm(i,",
        "for(i=2,5,\nA=algdep(Jacobi2",
        "for(i=2,3,\nA=algdep(Jacobi3",
        "MagmaInput(P)=",
        "Candidates(P[i]),Degenerate0(P[i])",
        "concat(Degenerateoo(P[i]),\">\")",
    )
    for literal in required:
        assert literal in source, literal


def main() -> None:
    verify_upstream_snapshot()
    reduction_output = verify_data_reduction()
    verify_generation_loops()
    candidates = parse_candidates()
    arrays = parse_consumer_arrays()
    names = {
        11: "A11", 13: "AF7", 17: "AF7", 19: "A19", 29: "A29",
        31: "A31", 41: "A41", 59: "A59", 61: "A61", 71: "A71",
        79: "A79", 89: "A89", 101: "A101", 109: "A109",
        131: "A131", 139: "A139", 149: "A139", 151: "A139",
    }
    degrees = {}
    for ell in ELLS:
        obtained = allowed_polynomial(ell, candidates[ell])
        expected = arrays[names[ell]]
        if ell == 131:
            # The archived consumer omitted the level-lowering trace 1 and
            # admitted 4 instead.  It is not a sound superset at this prime.
            evaluate = lambda poly, value: sum(
                coefficient * pow(value, exponent, P)
                for exponent, coefficient in enumerate(poly)
            ) % P
            assert obtained != expected
            assert evaluate(obtained, 1) == 0
            assert evaluate(expected, 1) != 0
            assert (-(ell + 1)) % P == 1
        else:
            assert obtained == expected, (ell, len(obtained) - 1, obtained, expected)
        degrees[str(ell)] = len(obtained) - 1
    assert degrees == {
        "11": 33, "13": 7, "17": 7, "19": 34, "29": 35,
        "31": 42, "41": 38, "59": 37, "61": 39, "71": 43,
        "79": 44, "89": 47, "101": 48, "109": 48,
        "131": 48, "139": 49, "149": 49, "151": 49,
    }
    print(reduction_output)
    print("UPSTREAM_GFE_5P3_SNAPSHOT=PASS_COMMIT_E88F914C577AB6CF9A45E5CDD82C1993477FB423")
    print("LOCAL_CASE_TRICHOTOMY=ORDINARY_T0_TINFINITY_PLUS_LEVEL_LOWERING")
    print("GENERATOR_LOOPS=PASS_ALL_T_IN_FELL_MINUS_0_1_AND_ALL_5_PLUS_3_DEGENERATE_CHARACTER_VALUES")
    print("ARCHIVED_PRECEDING_FILTERS=17_EXACT_1_UNSOUND_AT_ELL_131")
    print("ELL_131_DEFECT=ARCHIVED_FILTER_OMITS_LEVEL_LOWERING_TRACE_1_MOD_7")
    print("COVERAGE_REPAIR=REPLACE_ELL_131_FILTER_BY_X49_MINUS_X_NO_FILTER")
    print("FILTER_SOUNDNESS_SCOPE=PUBLISHED_LOCAL_TRACE_FORMULAS_AND_LEVEL_LOWERING_CONGRUENCE_IMPORTED")
    print("PASS_HILBERT_HECKE_FILTER_AUDIT_WITH_REQUIRED_ELL131_CONSERVATIVE_REPAIR")


if __name__ == "__main__":
    main()
