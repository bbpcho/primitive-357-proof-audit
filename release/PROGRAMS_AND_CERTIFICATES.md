# Programs and certificates — replay-companion-2026-09-15.2

The [replacement companion](https://github.com/bbpcho/primitive-357-proof-audit/releases/tag/replay-companion-2026-09-15.2), `PRIMITIVE_357_REPLAY_COMPANION_2026-09-15_V2.zip`, contains the public project evidence, exact mapping, external-input lock and replay tools. The [replacement audit](../audit/replacement-release-2026-09-15/README.md) binds the final bytes to the fresh isolated replay of the declared suite: **13 sector/interface records, 65 prior jobs and 16 rank-local checks**, with the latter joined to five freshly generated inputs. The current paper and `PRIMITIVE_357_ARXIV_SOURCE_2026-09-15_V2.zip` are separate release assets.

## Acquisition and complete replay

Run these commands from the extracted companion root. This is a different entry point from the historical `checks/verify_companion.py` and the inner `scripts/verify_release.py`.

Use Python 3.12, SageMath 10.9, PARI/GP 2.15.4, SymPy 1.14, mpmath 1.3, python-flint 0.9, Poppler, a C compiler, FLINT and GMP. Supply absolute paths for every capitalized value. Keep the distribution, cache, logical inputs, private external inputs and replay output in disjoint directories. `LOGICAL`, `PRIVATE` and `OUTPUT` must not exist.

```sh
python3 -B scripts/verify_companion.py
python3 -B scripts/acquire_external_inputs.py --lock inputs/EXTERNAL_INPUTS_LOCK.json --cache CACHE --record RECORDS/acquisition.json
python3 -B scripts/regenerate_hunter_sources.py --lock inputs/EXTERNAL_INPUTS_LOCK.json --recipes inputs/HUNTER_SOURCE_RECIPES.json --cache CACHE --record RECORDS/hunter.json
python3 -B scripts/regenerate_pvt_mod7.py --data CACHE/cc73ca915d3b25fe4def2b323b93bdc0fcdc46bbd560f16193af4dbdfae08ba5 --output CACHE/2833cdd1e290727028496b1339997ac3b401ab1d42dd51a9a970502a69837403 --record RECORDS/pvt.json
python3 -B scripts/verify_companion.py --cache CACHE --logical-root LOGICAL --private-root PRIVATE --report RECORDS/materialization.json
```

The first command checks public-file integrity, without executing arithmetic. Acquisition checks exact pinned inputs; `--offline` permits an existing authenticated cache, and `--file ID=PATH` accepts an explicitly supplied file without weakening its hash requirement. The lock identifies 62 downloads and 12 derived objects. Hunter sources are reconstructed exactly from acquired upstream files and original project changes. The PVT table is parsed and reduced from the acquired data; this does not rerun the upstream dataset's production.

Then run the complete suite **inside an independently configured, process-wide offline isolation boundary**, permitting only the new proof input roots and declared software dependencies:

```sh
python3 -B scripts/replay_companion.py --logical-root LOGICAL --private-root PRIVATE --output-root OUTPUT --python PYTHON --sage-python SAGE_PYTHON --gp GP --pdftotext PDFTOTEXT --python-path PYTHON_SOFTWARE_DEPENDENCIES --flint-prefix FLINT_PREFIX
```

The replay wrapper does not establish that operating-system isolation itself. It exposes no partial-group or resume option. Both `--python-path` and `--flint-prefix` are explicit arguments here. The [complete replay guide](FINAL_COMPANION_REPLAY_GUIDE.md) gives the exact runtime configuration, corrected record paths and the explicit macOS SDK setting. A historical PASS does not substitute for the result of this command.

Read `OUTPUT/EXTERNALIZED_REPLAY_RESULT.json`, `OUTPUT/INDEPENDENT_ENVELOPE.json`, `OUTPUT/suite/REPLAY_RESULT.json` and `OUTPUT/INTEGRATED_REPLAY.log`. The wrapper authenticates inputs before and after execution and independently verifies the result joins. Missing inputs, failed operations and unresolved arithmetic diagnostics are failures, even if a subprocess exits zero.

## Main and supplemental coverage

The main irreducible-sector job reports `DEEP_REPLAY=0` and invokes V15 without `--full`. The 13/65/16/5 totals describe the declared main jobs and joins; they do not count every optional producer in their dependency graph. Five separate isolated default-entry-point runs additionally cover the adapted V2/V3/V4/V5/V6 readers. They preserve the same logical/private inputs and offline profile, with independent fresh scratch directories and recorded outcomes. They do not constitute V15 `--full`, targeted Hunter V7 `--full`, or a fresh execution of the historical Hunter native searches.

The companion places these records at `records/completed-replay/supplemental/adapted-readers/` and `records/completed-replay/supplemental/v5/`. See the [replacement audit](../audit/replacement-release-2026-09-15/README.md) for their identity bindings and the [replay guide](FINAL_COMPANION_REPLAY_GUIDE.md#repeat-the-five-supplemental-default-checks) for usable direct commands and the V5 native-compiler setup.

The direct V5 reconstruction passed all eight exact support-set comparisons, totaling **237,182 rows**, with zero missing or extra rows. The preserved **236,182** aggregate in its source, raw log and inherited metadata is a reporting error. `supplemental/v5/SUPPLEMENTAL_V5_FINAL_RESULT.json` and `TOTAL_COUNT_ERRATUM.md` separate that historical label from the independently counted total. The original per-table arithmetic checks and all enumeration/exclusion bounds remain unchanged. V6 separately performed its 1,182-row local-algebra classification and precision comparison.

## Layout and mathematical correspondence

The public `objects/` store deduplicates repeated evidence. Materialization restores the logical repositories at `evidence/v3/repository/`, `evidence/p5/repository/` and `evidence/rank/repository/`, with adopted audit programs under `audit/work/`. The separate `PRIVATE` root holds authenticated external members used by the adapted nested-archive readers. Exact maps and dependency indexes bind all these paths; installed runtimes and undeclared workspace caches are not proof inputs.

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


The full Fano resolvent reconstruction uses the unchanged certificate at logical path `evidence/v3/repository/beal_357_spark_handover_2026-08-20/project/p7_fano_resolvent_certificate.py`. It recomputes all 80 CRT primes, obtains a 1330-bit modulus exceeding the rigorous 1230-bit coefficient bound, and checks five further primes. Its log is `OUTPUT/suite/sectors/logs/independent_fano_resolvent_foundation.log`. The absolute and relative degree-42 defaults separately check their saved CRT certificates at three fresh primes each; those defaults do not rerun their entire CRT production.

## Rank and local witness records

Within the logical tree, `audit/work/rank_closure_audit/` contains the pre-dyadic restrictions, dyadic geometry and arithmetic, `p7_replacement/` and `p7_finite/` records. The p=7 replacement reads the exact contact coefficient export identified by `P7_REPLACEMENT_INDEX.json`; its finite quotient and all-compatible-carrier proof are bound by `P7_FINITE_CHARACTER_INDEX.json`. The actual correction value −1 proves nonzero without relying on the old ROOT5/mask-8 label or unavailable historical workers.

The p=5 geometry, coherent lifts, obstruction and comparison-kernel checks are under `audit/work/p5_archive_audit/`. Foundation, saturation and both full logarithm branches are under `audit/work/v3_audit/` and the indexed inherited packages. The rank-local runner is `audit/work/rank_local/run_rank_local.py`; the 65-job prior runner is `audit/work/integration_prior/replay_prior_evidence.py`.

The adopted repairs remain: p=173 supplies the rational/twist two-saturation step; Flynn's infinity label and local precision propagation are corrected; the Hecke argument covers the conservative ambient spaces; all four logarithm columns are reconstructed. Square-root searches establish existence, not uniqueness among 4096 candidates.

## Preserved boundaries

Required unlicensed upstream papers and programs are acquired privately. The unchanged licensed Putz thesis and MPFR header retain their notices. Seven historical native executables were previously only hashed, never executed by this suite; their omitted identities and the removed provenance checks are explicit. Source, numerical-output and arithmetic checks remain.

The replacement suite does not execute Magma. Seven earlier official Magma V2.29-10 jobs and four negative controls remain authenticated records under `records/prior-audits/magma-replay-2026-09-15/` in the public companion. Published theorems, identified software algorithms and those recorded computations remain premises. Successful replay is neither proof-assistant certification nor external human peer review.

The inner `RELEASE_MANIFEST.json` retains `verified-2026-09-14.1` only for the inherited verifier's internal contract; its inventory is rebuilt and bound to this replacement. The public identity is `replay-companion-2026-09-15.2`, authenticated by `COMPANION_MANIFEST.json`. Earlier filenames, failed attempts and superseded arguments remain historical records, not the current download or paper.
