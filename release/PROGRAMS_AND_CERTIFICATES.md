# Programs and certificates — verified-2026-09-14.1

The integrated release combines immutable exact inputs with the adopted independent verification route. Run the release-level verifier from the extracted archive root:

```bash
python3 -B scripts/verify_release.py
python3 -B scripts/verify_release.py --replay \
  --python /path/to/python-with-sympy-and-flint \
  --sage-python /path/to/sage-python --gp /path/to/gp \
  --output-dir /path/to/new-verification-output
```

The first command checks the declared identity and interface records. The second runs the adopted arithmetic reconstruction, using explicitly supplied runtimes and a separate output directory. Read its per-stage results; a recorded historical PASS is not a fresh replay result.

The `--python` runtime needs SymPy 1.14, mpmath 1.3 and python-flint 0.9. The Sage and PARI/GP runtimes are supplied separately. Use `--python-path` only when those Python packages are installed in a separate declared directory. `--flint-prefix` is optional and defaults to the Sage environment. The integrated local-rank runner is `audit/work/rank_local/run_rank_local.py`.

## Input and output layout

The preserved input repositories are `evidence/v3/repository`, `evidence/p5/repository`, and `evidence/rank/repository`. Independent sources and explanations are under `audit/work/`. Exact dependency indexes accompany the portable runners. Paths in older sealed transcripts describe their original environment; the adopted runners bind their actual reads to the new extraction.

The prior-evidence runner is `audit/work/integration_prior/replay_prior_evidence.py`, with `REQUIRED_PRIOR_EVIDENCE.json`. Its README states its runtime arguments, stage scope and retained premises. The release-level command is the supported complete entry point; individual historical programs may have narrower assumptions.

## Mathematical correspondence

| Assertion | Required adopted evidence |
|---|---|
| Actual genus-three model and descent dictionary | Exact quartic/contact identities, all 315 tetrads, theta/tower reconstruction, Galois containment, and global class/unit/support checks. |
| Four independent divisor classes | Actual finite-Jacobian/Kummer maps or the independently reconstructed full-rank logarithm matrix, with the stated torsion input. |
| Complete pre-dyadic containing space | All 66 restriction columns at the selected places, actual full local images, independent intersection and exact equality with the downstream 18-dimensional array. |
| Complete p=7 fake image | Full seven-component square test for P4−P1 divided by 3; fresh target norm/conic correction −1; all-compatible-carrier descent; genuine nonzero closed-point image with Z_original=−7Z_local. |
| Complete second-dyadic fake image | Actual rank-three fake image, genuine kernel cycles, certified local integral models and roots, nonzero correction, and all 28 compatible finite characters. |
| Literal complementary class excluded at 5 | Exact same-c binding, exact target norm roots, coherent μ2 relations, complete local image, both lift obstructions, and zero comparison kernel. |
| Rank four | Exact Q=B⊕⟨c⟩ identity and the true-Selmer comparison argument, combined with the lower bound. |
| Coefficient coverage modulo 400 | Odd index for H0 and 5-saturation for H1=⟨D2,E,D4,D5⟩. |
| Global logarithmic annihilator | Both reconstructed split-23 matrices and their verified annihilator, extended from H0 using its finite index. |
| Terminal rational-parameter locus | Actual finite reduction maps, coupled sieve, unit tangent tests, exceptional disk calculation and incompatible parameter values. |
| Exceptional septic elimination | Conservative Hecke-filter and ambient coverage, local source hypotheses, ray-character argument, and the terminal 24 nonzero resultants. |
| Cubic–quartic sector | Published/Magma rational/twist rank and torsion inputs, p=173 Kummer repair, actual sieve, and corrected formal-coordinate/precision checks. |

The sector replay includes a full reconstruction of the degree-15 Fano resolvent by the unchanged [original Fano certificate](../evidence/v3/repository/beal_357_spark_handover_2026-08-20/project/p7_fano_resolvent_certificate.py). It recomputes all 80 CRT primes, obtains a 1330-bit modulus exceeding the rigorous 1230-bit coefficient bound, and checks five further primes. Its fresh log is `sectors/logs/independent_fano_resolvent_foundation.log` in the selected output directory. The absolute and relative degree-42 verifier defaults separately audit their saved CRT certificates at three fresh primes each; those defaults do not rerun their entire CRT production. The full Fano reconstruction and the exact canonical identities supply the adopted resolvent foundation.

## Rank and local witness records

The named rank audit reports are retained under `audit/work/rank_closure_audit/`:

- `predyadic/`: actual restriction maps, local point/source witnesses and the independent intersection;
- `dyadic_geometry/`: all 28 physical local groups and independent sextic quotient characters;
- `dyadic_arithmetic/`: full-component relations, local integral bases, stronger Hensel/precision checks and correction profile;
- `p7_replacement/`: exact-data witness reconstruction, precision 100/120 runs, cycle-1 calibration and `P7_REPLACEMENT_INDEX.json`;
- `p7_finite/`: all-compatible-carrier quotient descent and `P7_FINITE_CHARACTER_INDEX.json`.

The p=7 replacement reads the exact contact coefficient export whose hash and original binding are recorded in its index. That input must be included or regenerated by its declared exact export; an undeclared workspace cache is not permitted. The historical ROOT5/mask-8 label is unnecessary for the replacement proof: every matching physical character descends, and the actual value −1 proves nonzero.

The p=5 geometry/coherence and obstruction records are retained under `audit/work/p5_archive_audit/`; prior foundation, saturation and logarithm records are under `audit/work/v3_audit/` and the explicitly indexed inherited packages. The top-level dependency index determines the precise required subset and source hashes.

## Earlier repairs retained

The Section 7 p=173 Kummer witness replaces the unsupported inference that the original rational-plus-twist index was at most two. Its rational/twist rank and torsion inputs remain cited. The adapted Flynn infinity label and propagated local error bounds remain corrected. The Hecke route covers the conservative filtered ambient spaces and does not depend on old/new subtraction or a complete-newspace assertion. All four logarithm columns are reconstructed; saved D4 first-log data are not the sole source.

The square-root searches certify existence of witnesses, not uniqueness among 4096 candidates. Their quadratic norms are unchanged when the root signs are reversed. The resolved-branch scout assignment and the replay wrappers use the tested corrections rather than the superseded code paths.

## What is not claimed by the new replay

The independent release audit does not claim a new Magma execution of the cited Section 7 rational/twist group computations. Published mathematical theorems remain bibliographic inputs. The final result combines those stated premises with the adopted exact arithmetic and independently checked implications. Asset checks alone are not a proof of any local image or Selmer bound.
