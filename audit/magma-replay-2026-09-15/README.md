# Fresh Magma calculator replay — 15 September 2026

This directory records executions of seven unchanged proof inputs through the University of Sydney's [official Magma calculator](https://magma.maths.usyd.edu.au/calc/), observed as Magma V2.29-10 with a 60-second limit. It does not represent a local Magma installation or an independent implementation of Magma's algorithms.

All seven observations completed on 15 September 2026 and passed the local validator, including all four rejection controls. The same validation passed with Python optimization enabled (`-OO`). Calculator CPU times total 97.976 seconds; individual jobs ranged from 0.590 to 37.130 seconds. Each of the required mathematical conclusions below agrees with the retained evidence. The machine-readable result is `VALIDATION_REPORT.json`; it records the exact input/output hashes and per-job observations.

`INPUT_INDEX.json` pins the exact input copies to the sealed `verified-2026-09-14.1` archive (SHA-256 `27e3e6eeb50f83ea484e7cd0c94dbd88de0141ab9f47634ed5181e7db0ecba33`). Its original `NOT_RUN` labels describe the pre-execution inventory and are retained unchanged. Actual observations are in `outputs/<job>.json` and the matching `.txt`; each contains the live result, input/output string hashes, observation time, and calculator statistics. These hashes bind the captured files; they are not cryptographic attestations issued by the service.

Recheck the saved observations:

```sh
/opt/anaconda3/bin/python3 verify_capture.py --self-test
```

Its successful result is `PASS_SEVEN_FRESH_MAGMA_CALCULATOR_CAPTURES`. The validator performs no network requests, executes no mathematical software, and writes no files. It checks the copies against both fixed hashes and the unchanged extracted source release. Use `--source-results /path/to/release/evidence/v3/repository/results` to relocate that source comparison.

| Job | Calculator seconds | Required conclusion |
|---|---:|---|
| `section7_groups` | 26.149 | Rational group `Z/10 + Z`, negative-35 twist `Z/2 + Z + Z`, both proof flags true, and named generators spanning the groups as asserted by the unchanged input. |
| `rational_c1_height` | 0.590 | The bounded Jacobian search returns exactly the identity and the specified two opposite divisors; the height matrix and regulator agree numerically. |
| `rational_c3` | 3.759 | Rank one, infinite-order divisor, and Chabauty's exhaustive point set `(-2, ±540)`. |
| `rational_c3_challenge` | 3.779 | The same exhaustive set using a doubled, negated divisor and the alternate base point. |
| `quadratic_fake_selmer` | 6.179 | The exact three specified fake 2-cover classes. |
| `quadratic_class41` | 37.130 | Rank-three curve, trivial torsion, rational-image coordinates `0, 35/9`, and saturation at every prime dividing the returned Chabauty index. |
| `quadratic_class42` | 20.390 | Full rank-two basis, trivial torsion, sole rational-image coordinate `0`, and no unresolved cosets. |

The validator requires exactly seven indexed jobs and seven JSON/text pairs, checks every source/input/output identity, rejects diagnostics even when a later PASS line exists, and checks the actual point sets and mathematical outputs. It handles Magma's line wrapping before parsing long decimal strings. The three printing-only inputs are checked explicitly rather than treated as successful merely because they finished. Its in-memory negative controls remove a job, inject a runtime error before a retained PASS while recomputing the output hash, change an input, and change a C3 Chabauty point to `(-2, 541)` while retaining consistent output hashes. Each must be rejected. No Python `assert` statements are used for validation, so optimization cannot disable these checks.

The [Mordell–Weil handbook](https://magma.maths.usyd.edu.au/magma/handbook/text/1618) identifies the two flags and rank upper bound. Section 7 uses both flags, normal saturation, and inverse-map generator checks. Its existing finite-field p=173 Kummer argument is still the separate corrected step over the quadratic field; the superseded historical index argument is not reinstated.

The [elliptic saturation routines](https://magma.maths.usyd.edu.au/magma/handbook/text/1570) and [elliptic Chabauty contract](https://magma.maths.usyd.edu.au/magma/handbook/text/1568) explain the index conditions checked by the two quadratic branches. [Genus-two Chabauty](https://magma.maths.usyd.edu.au/magma/handbook/text/1620) incorporates saturation, so the doubled-divisor challenge is legitimate. C1 floating height/regulator agreement is only a numerical comparison: the earlier independent exact duplication and interval bounds remain the rigorous height evidence.

These jobs reproduce the retained computations in the published reducible-sector arguments. The previously replayed new genus-three rank-four, p=5 obstruction, and conservative Hecke arguments remain separate evidence. Completion of these seven jobs does not rerun every historical exploratory Magma file, replace the cited mathematical theorems, or constitute a proof-assistant formalization. The sealed source release is unchanged.
