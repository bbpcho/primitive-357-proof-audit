#!/usr/bin/env python3
"""Validate seven saved official-calculator observations; execute no Magma."""
import argparse
import copy
import datetime as dt
from decimal import Decimal, localcontext
import hashlib
import json
from pathlib import Path
import re
import sys

SERVICE = "https://magma.maths.usyd.edu.au/calc/"
ARCHIVE = "27e3e6eeb50f83ea484e7cd0c94dbd88de0141ab9f47634ed5181e7db0ecba33"
SOURCE = Path(__file__).resolve().parents[1] / "verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1/evidence/v3/repository/results"
EXPECTED = {
    "section7_groups": ("2026-09-10_section7_mordell_weil_basis_lemma_7_3_v1/scripts/verify_section7_mordell_weil_basis_lemma_7_3.m", "1b348d417d63078157bcc20b8b96eeeb234e4cc89139d886bcef40aca24fc862", 2198),
    "rational_c1_height": ("2026-09-09_rational_factor_mw_basis_attack_v1/inputs/magma_v2_29_10_height_pairing_points_bound15_input.m", "96eaa0d189fa6529706de336c8a81184a866178cd1a6b6fdde54f1544880a468", 537),
    "rational_c3": ("2026-09-10_rational_factor_proposition_6_1_composition_v2/inputs/magma_v2_29_10_c3_rank_chabauty_input.m", "90ed1a57ca36d181f4f8e8ef91379c1cc3c99ce1d2d3800ee817fb7c21ce0c79", 409),
    "rational_c3_challenge": ("2026-09-10_rational_factor_proposition_6_1_composition_v2/inputs/magma_v2_29_10_c3_chabauty_challenge_input.m", "9dbca348ca214de1cce27beaf9f2d842d5e65c4a5fdf446a0818e05ea962351c", 364),
    "quadratic_fake_selmer": ("2026-09-09_quadratic_factor_2_5_reconstruction_v1/scripts/reconstruct_fake_selmer.m", "97b437293d97f71b00d81a6ebf95658e68143227763baba371fdbf58c7244a39", 621),
    "quadratic_class41": ("2026-09-09_quadratic_factor_2_5_reconstruction_v1/scripts/reconstruct_class41.m", "73a4f662f7731bac2f45fb225444f6a67089363a2d645e6411361ff6ac4687a8", 1967),
    "quadratic_class42": ("2026-09-09_quadratic_factor_2_5_reconstruction_v1/scripts/reconstruct_class42.m", "0e87fabb4b2e5f748683f3df613048c1714758f44fd61e5a7105eb5949fed49a", 1725),
}
NUM = r"-?\d+(?:\.\d+)?(?:[Ee][+-]?\d+)?"
ERROR = re.compile(r"\b(?:error|errors|assertion|assert|syntax|timeout|timed\s+out|aborted|terminated|interrupt(?:ed)?|exception|warning)\b|time\s+limit|memory\s+limit", re.I)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key: " + key)
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def normalize(text):
    # Magma inserts backslash-newline continuations inside long numbers.
    return " ".join(re.sub(r"\\\r?\n[ \t]*", "", text).split())


def compact(text):
    return re.sub(r"\s+", "", text)


def fields(text, labels):
    positions = []
    for label in labels:
        matches = list(re.finditer(r"(?<![A-Za-z0-9_])" + re.escape(label), text))
        require(len(matches) == 1, "missing/duplicate field: " + label)
        positions.append(matches[0].start())
    require(positions[0] == 0 and positions == sorted(positions), "unexpected prefix/field order")
    ends = positions[1:] + [len(text)]
    return {label: text[pos + len(label):end].strip() for label, pos, end in zip(labels, positions, ends)}


def exact_fields(data, expected):
    for key, value in expected.items():
        require(compact(data[key]) == compact(value), "wrong value: " + key)


def decimal_close(actual, expected, tolerance="1e-60"):
    require(re.fullmatch(NUM, actual) is not None, "invalid decimal")
    with localcontext() as context:
        context.prec = 100
        require(abs(Decimal(actual) - Decimal(expected)) <= Decimal(tolerance), "numerical comparison failed")


def point_set(value, expected):
    body = value.strip()
    require(body.startswith("{") and body.endswith("}"), "point set delimiters")
    body = body[1:-1].replace("@", "").strip()
    points = re.findall(r"\([^()]*\)", body)
    require(re.sub(r"\([^()]*\)", "", body).replace(",", "").strip() == "", "unparsed point set")
    require(len(points) == len(expected) and {compact(p) for p in points} == {compact(p) for p in expected}, "wrong actual point set")


def mathematical_output(job, raw):
    require(not ERROR.search(raw), job + ": diagnostic in output")
    text = normalize(raw)
    if job == "section7_groups":
        final = "SECTION7_LEMMA_7_3_MAGMA=PASS_RIGOROUS_FULL_GROUPS_AND_NAMED_GENERATORS"
        data = fields(text, ["UNTWISTED_GROUP", "UNTWISTED_NAMED_COORDINATES", "UNTWISTED_PROVED", "TWISTED_GROUP", "TWISTED_NAMED_COORDINATES", "TWISTED_PROVED", final])
        exact_fields(data, {"UNTWISTED_GROUP": "[10,0]", "TWISTED_GROUP": "[2,0,0]", "UNTWISTED_PROVED": "true true 1", "TWISTED_PROVED": "true true 2", final: ""})
        for key, count, dimension in [("UNTWISTED_NAMED_COORDINATES", 2, 2), ("TWISTED_NAMED_COORDINATES", 3, 3)]:
            vector = r"\[\s*-?\d+(?:\s*,\s*-?\d+){" + str(dimension - 1) + r"}\s*\]"
            require(re.fullmatch(r"(?:" + vector + r"\s*){" + str(count) + r"}", data[key]) is not None, "named coordinate output malformed")
        return "Both full groups proved; unchanged source asserts named generators generate."
    if job == "rational_c1_height":
        data = fields(text, ["MW_FINAL_SEARCH_BEGIN", "HEIGHT_PAIRING", "REGULATOR", "POINT_COUNT", "MW_FINAL_SEARCH_END"])
        exact_fields(data, {"MW_FINAL_SEARCH_BEGIN": "", "MW_FINAL_SEARCH_END": ""})
        rows = re.findall(r"\[([^\[\]]+)\]", data["HEIGHT_PAIRING"])
        require(len(rows) == 3 and re.sub(r"\[[^\[\]]+\]", "", data["HEIGHT_PAIRING"]).strip() == "", "height matrix dimensions")
        reference = [["0.6170338153091093765007061550307144846212267747069335429614000152820326256437488920", "0.2485239417400757638439020285492291401397659673578768070940680926365216873901838352", "-0.06164201068493820755579881145256186053249713109926582827442326149125379811934457333"], ["0.2485239417400757638439020285492291401397659673578768070940680926365216873901838352", "0.9346607177033773411071292139084171169251733631014718279743702375607132424169967132", "-0.1856021406461365101571676871332116491634790750311227748861977010936867568706625282"], ["-0.06164201068493820755579881145256186053249713109926582827442326149125379811934457333", "-0.1856021406461365101571676871332116491634790750311227748861977010936867568706625282", "1.452921451314992814205509502503906338644264158357075106779734970554442138145379432"]]
        for row, expected in zip(rows, reference):
            values = row.split()
            require(len(values) == 3, "height matrix row")
            for actual, target in zip(values, expected):
                decimal_close(actual, target)
        decimal_close(data["REGULATOR"], "0.7290659611819572606802519846059231153467221355230732041915298288776668724689619164")
        count = data["POINT_COUNT"]
        require(count.startswith("3 POINT "), "point count")
        entries = re.findall(r"POINT (\([^()]+\)) NAIVE (" + NUM + r") CANONICAL (" + NUM + r")", count[2:])
        require(len(entries) == 3 and re.sub(r"POINT (\([^()]+\)) NAIVE (" + NUM + r") CANONICAL (" + NUM + r")", "", count[2:]).strip() == "", "point records malformed")
        expected = {"(1,0,0)", "(x^2+2/5*x-11/5,161/25*x-938/25,2)", "(x^2+2/5*x-11/5,-161/25*x+938/25,2)"}
        require({compact(p) for p, _, _ in entries} == expected, "wrong enumerated C1 points")
        for point, naive, canonical in entries:
            identity = compact(point) == "(1,0,0)"
            decimal_close(naive, "0" if identity else "2.39789527279837054406194357797", "1e-25")
            decimal_close(canonical, "0" if identity else "1.946671245254225775594618034629497102200496670865476993192288462853967167550439178")
        return "Exact bounded point list agrees; floating height/regulator comparison only. Prior exact duplication bounds remain separate."
    if job in {"rational_c3", "rational_c3_challenge"}:
        challenge = job.endswith("challenge")
        order = "OrderNegativeD" if challenge else "OrderD"
        chabauty = "ChabautyTwiceNegative" if challenge else "Chabauty"
        labels = ["RankBounds", order, chabauty] if challenge else ["BadPrimes", "RankBounds", "SearchPoints", order, chabauty]
        data = fields(text, labels)
        require(data["RankBounds"] in {"0 1", "1 1"}, "C3 rank upper bound")
        exact_fields(data, {order: "0"})
        expected = ["(-2:540:1)", "(-2:-540:1)"]
        if not challenge:
            exact_fields(data, {"BadPrimes": "[2,3,5,7]"})
            point_set(data["SearchPoints"], expected)
        match = re.fullmatch(r"(\{[^{}]*\})\s*\{\s*11,\s*47,\s*79\s*\}\s*\[\s*3,\s*5\s*\]", data[chabauty])
        require(match is not None, "C3 Chabauty output format")
        point_set(match.group(1), expected)
        return "Rank one, infinite-order divisor, and exhaustive Chabauty point set agree."
    if job == "quadratic_fake_selmer":
        require(text == "TWO_COVER_DESCENT_CLASSES 3 FAKE_SELMER_STATUS=PASS_EXACT_THREE_CLASSES", "fake Selmer completion")
        return "Unchanged source asserts exactly the three specified fake-cover classes."
    if job == "quadratic_class41":
        final = "CLASS41_STATUS=PASS_GLOBAL_CHABAUTY_AND_INDEX_DISCHARGE"
        labels = ["E1_RANK_BOUNDS", "E1_TORSION_INVARIANTS", "E1_GENERATORS_INDEPENDENT", "E1_EXACT_RANK_FROM_UPPER_BOUND_AND_INDEPENDENCE", "E1_GLOBAL_CHABAUTY_V", "E1_GLOBAL_CHABAUTY_R", "E1_GLOBAL_R_FACTORIZATION", "E1_RATIONAL_X", "E1_SATURATION_THROUGH_97_UNCHANGED", final]
        data = fields(text, labels)
        require(data["E1_RANK_BOUNDS"] in {f"{i} 3" for i in range(4)}, "E1 rank bound")
        exact_fields(data, {"E1_TORSION_INVARIANTS": "[]", "E1_GENERATORS_INDEPENDENT": "true", "E1_EXACT_RANK_FROM_UPPER_BOUND_AND_INDEPENDENCE": "3", "E1_GLOBAL_CHABAUTY_R": "6592880678883323322765152793600", "E1_SATURATION_THROUGH_97_UNCHANGED": "true", final: ""})
        elements = compact(data["E1_GLOBAL_CHABAUTY_V"])
        require(elements.startswith("{") and elements.endswith("}"), "E1 V delimiters")
        require(len(elements[1:-1].split(",")) == 3 and set(elements[1:-1].split(",")) == {"0", "-2*G.2+2*G.3", "2*G.2-2*G.3"}, "E1 actual subgroup points")
        factorization = compact(data["E1_GLOBAL_R_FACTORIZATION"])
        pairs = [(int(p), int(e)) for p, e in re.findall(r"<(\d+),(\d+)>", factorization)]
        expected = [(2,10),(3,5),(5,2),(7,4)] + [(p,1) for p in [11,17,19,29,31,37,43,47,53,61,71,83,97]]
        require(factorization == "[" + ",".join(f"<{p},{e}>" for p, e in pairs) + "]" and sorted(pairs) == expected, "E1 index prime factorization")
        point_set(data["E1_RATIONAL_X"], ["(35/9:1)", "(0:1)"])
        return "Rank-three Chabauty points and every required index-prime saturation agree."
    if job == "quadratic_class42":
        final = "CLASS42_STATUS=PASS_FULL_BASIS_AND_LOCAL_CHABAUTY"
        expected = {"E3_RANK_BOUNDS": "2 2", "E3_TORSION_INVARIANTS": "[]", "E3_GENERATORS_INDEPENDENT": "true", "E3_FULL_SATURATION_UNCHANGED": "true", "E3_LOCAL_CHABAUTY_N": "1", "E3_LOCAL_CHABAUTY_V": "{0}", "E3_LOCAL_CHABAUTY_R": "4", "E3_LOCAL_CHABAUTY_UNRESOLVED": "{}", "E3_RATIONAL_X": "{(0:1)}", final: ""}
        exact_fields(fields(text, list(expected)), expected)
        return "Full rank-two basis, one rational-image point, and no unresolved cosets agree."
    raise ValueError("unknown job")


def load_bundle(root, source):
    names = {f"{job}.{suffix}" for job in EXPECTED for suffix in ["json", "txt"]}
    require({p.name for p in (root / "outputs").iterdir()} == names, "outputs must contain exactly seven JSON/text pairs")
    index = read_json(root / "INPUT_INDEX.json")
    return {"index": index, "inputs": {job: (root / "inputs" / (job + ".m")).read_bytes() for job in EXPECTED}, "sources": {job: (source / info[0]).read_bytes() for job, info in EXPECTED.items()}, "captures": {job: read_json(root / "outputs" / (job + ".json")) for job in EXPECTED}, "texts": {job: (root / "outputs" / (job + ".txt")).read_bytes() for job in EXPECTED}}


def validate(bundle):
    index = bundle["index"]
    require(index["source_release"] == "verified-2026-09-14.1" and index["source_archive_sha256"] == ARCHIVE and index["service"] == SERVICE and index["observed_magma_version"] == "V2.29-10" and index["observed_time_limit_seconds"] == 60, "index provenance")
    jobs = index["jobs"]
    require(len(jobs) == 7 and {j["id"] for j in jobs} == set(EXPECTED), "exactly seven indexed jobs required")
    for key in ["inputs", "sources", "captures", "texts"]:
        require(set(bundle[key]) == set(EXPECTED), "missing/extra job in " + key)
    results = []
    for job in jobs:
        name = job["id"]
        relative, sha, size = EXPECTED[name]
        require(job["source_relative_to_results"] == relative and job["input"] == f"inputs/{name}.m" and job["sha256"] == sha and job["bytes"] == size, name + ": input index mismatch")
        source, input_data = bundle["sources"][name], bundle["inputs"][name]
        require(source == input_data and len(input_data) == size and digest(input_data) == sha, name + ": changed source/input")
        capture = bundle["captures"][name]
        require(capture["id"] == name and capture["service"] == SERVICE and capture["magma_version"] == "V2.29-10" and capture["inputSha256"] == sha, name + ": capture provenance")
        output = capture["output"].encode("utf-8")
        require(output == bundle["texts"][name] and digest(output) == capture["outputSha256"], name + ": output/hash mismatch")
        observed = dt.datetime.fromisoformat(capture["observedAt"].replace("Z", "+00:00"))
        require(observed.utcoffset() == dt.timedelta(0) and observed.date() == dt.date(2026, 9, 15), name + ": observation date")
        stats = re.fullmatch(r"Seed: (\d+); Total time: (\d+(?:\.\d+)?) seconds; Total memory usage: (\d+(?:\.\d+)?)MB\.", capture["stats"])
        require(stats is not None and Decimal(0) < Decimal(stats[2]) <= Decimal(60) and Decimal(stats[3]) > 0, name + ": missing/invalid successful-run statistics")
        conclusion = mathematical_output(name, capture["output"])
        results.append({"id": name, "status": "PASS", "input_sha256": sha, "output_sha256": capture["outputSha256"], "observed_at": capture["observedAt"], "stats": capture["stats"], "conclusion": conclusion})
    return results


def controls(bundle):
    cases = []
    missing = copy.deepcopy(bundle)
    del missing["captures"]["section7_groups"]
    cases.append(("missing_job", missing))
    injected = copy.deepcopy(bundle)
    cap = injected["captures"]["section7_groups"]
    cap["output"] = "Runtime error: Assertion failed\n" + cap["output"]
    injected["texts"]["section7_groups"] = cap["output"].encode()
    cap["outputSha256"] = digest(injected["texts"]["section7_groups"])
    cases.append(("error_with_later_PASS_and_consistent_hash", injected))
    changed = copy.deepcopy(bundle)
    changed["inputs"]["section7_groups"] += b"\n"
    cases.append(("changed_input", changed))
    wrong_point = copy.deepcopy(bundle)
    cap = wrong_point["captures"]["rational_c3"]
    original = "Chabauty { (-2 : 540 : 1)"
    require(cap["output"].count(original) == 1, "printing-only control fixture not found")
    cap["output"] = cap["output"].replace(original, "Chabauty { (-2 : 541 : 1)")
    wrong_point["texts"]["rational_c3"] = cap["output"].encode()
    cap["outputSha256"] = digest(wrong_point["texts"]["rational_c3"])
    cases.append(("wrong_C3_point_with_consistent_hash", wrong_point))
    records = []
    for name, modified in cases:
        try:
            validate(modified)
        except (ValueError, KeyError, TypeError) as error:
            records.append({"control": name, "status": "PASS_REJECTED", "reason": str(error)})
        else:
            raise ValueError("negative control accepted: " + name)
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--source-results", type=Path, default=SOURCE)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    bundle = load_bundle(args.root, args.source_results)
    jobs = validate(bundle)
    result = {"status": "PASS_SEVEN_FRESH_MAGMA_CALCULATOR_CAPTURES", "job_count": 7, "service": SERVICE, "magma_version": "V2.29-10", "source_archive_sha256": ARCHIVE, "input_index_sha256": digest((args.root / "INPUT_INDEX.json").read_bytes()), "validator_sha256": digest(Path(__file__).read_bytes()), "scope": "Fresh executions by the official web calculator of seven unchanged reducible-sector inputs; local validation of captured outputs, not local Magma or an independent implementation.", "height_scope": "C1 floating values are comparisons only; the earlier independent exact duplication/interval proof remains the rigorous height bound.", "jobs": jobs}
    if args.self_test:
        result["negative_controls"] = controls(bundle)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"status": "FAIL_MAGMA_CAPTURE_VALIDATION", "reason": str(error)}))
        sys.exit(1)
