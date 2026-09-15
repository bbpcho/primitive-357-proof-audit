# Evidence and verification boundary

The first-submission release distinguishes exact input data, recorded output, replayable computations, and checked mathematical implications. Hash equality identifies bytes; it does not prove the statement written in those bytes. A successful historical replay is used only for its documented scope. This is not proof-assistant certification or external human peer review.

## The first-submission collection

The release [`first-submission-2026-09-15.1`](https://github.com/bbpcho/primitive-357-proof-audit/releases/tag/first-submission-2026-09-15.1) supplies the canonical 36-page paper and two separate assets: the 35,879-byte arXiv source ZIP and the 601,649,354-byte companion ZIP. The [README download table](../README.md#downloads) identifies their exact names and links. The large companion is a GitHub asset, not the arXiv source upload.

The companion includes three immutable components:

| Component | Scope |
|---|---|
| `computational_materials/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip` | Full source/data snapshot, adopted reconstruction programs and recorded integrated replays. |
| `verification/PRIMITIVE_357_LOGICAL_AUDIT_AND_REVIEW_DRAFT_2026-09-15_V1.zip` | The 118-node argument ledger, 70 named imports, sector reviews, corrections and supplementary exact checks. Begin with its `AUDIT_REPORT.md`. |
| `verification/PRIMITIVE_357_FRESH_MAGMA_REPLAY_2026-09-15_V1.zip` | Seven official Magma V2.29-10 executions, exact inputs/outputs, mathematical checks and four negative controls. |

The ledger has no unresolved project-specific nodes at the reviewed lemma/interface level. It preserves superseded rows and draft corrections, and leaves cited mathematics and software algorithms explicit. The first-submission editorial record binds the canonical paper to that reviewed draft without changing formulas, theorem environments or the rank appendix.

For convenient reading, this repository contains indexed extracts of the [argument audit](../audit/logical-audit-2026-09-15/AUDIT_REPORT.md), the [Magma replay records](../audit/magma-replay-2026-09-15/README.md), and the [first-submission record](../audit/first-submission-2026-09-15/README.md). The argument-audit extracts do not replace the complete audit folders and large replay inputs in the companion.

The companion does not claim a newly executed combined replay of all three components. Its integrity command is `python3 checks/verify_companion.py`. Mathematical replays follow each component's guide and runtime requirements; supplementary audit scripts may require their recorded paths to be relocated after extraction.

## Immutable inputs and adopted checks

The unchanged 14 September source/data component preserves the V3, p=5 and rank-closure repositories under separate roots:

- `evidence/v3/repository/`
- `evidence/p5/repository/`
- `evidence/rank/repository/`

Within that component, the audit sources and reports are carried under `audit/work/`, with their dependency indexes. Runtime installations and untracked caches are not evidence inputs. Its supported replays use declared paths in the extracted component and a separate output directory. Its entry point is `scripts/verify_release.py`, with the documented `--replay` options for Python, SageMath, PARI/GP and output location.

The independent rank route supplies more than the original archive's top-level PASS: actual local restrictions for all 66 coordinates, full local image bounds, the replacement 7-adic nonzero kernel witness, the second-dyadic character and Hensel proof, and exact identification of the same complementary class c. The previous p=5 audit supplies its actual geometry, coherent roots, local obstruction and comparison-kernel calculation. The earlier class/unit, finite-Jacobian, saturation, and full logarithm checks supply the remaining premises.

The absent historical p=7 cycle-3 worker is replaced by `reconstruct_p7_witness_unramified.py`, its exact contact input binding, finite quotient check and companion full-component square/source proofs. The replacement does not claim to reproduce an unavailable program byte for byte.

## Imported results and software

The sector routing and prior reducible-sector eliminations use Dahmen–Siksek; the seven-field bound uses Putz; the modularity/level-lowering argument uses the cited Pacetti–Villagra Torcomian and Hilbert modular results. The generalized descent and correction interpretation use Bruin–Poonen–Stoll, including Corollary 12.5 and Appendix A. The local conclusions also use the stated Hensel, local abelian-variety, Kummer and Chabauty results with checked hypotheses. These citations concern other authors' work, not earlier arXiv papers by Peter Chocian.

The cubic–quartic sector retains its identified rational and twisted Mordell–Weil and torsion inputs. Both full-group computations occur among the seven Magma jobs in the companion. The p=173 finite-field Kummer proof supplies the separate saturation step. A fresh Magma execution is evidence from that software, not an independent implementation of its algorithms. The numerical height comparison does not replace exact height bounds. The 14 September component's statement that it did not newly execute those Magma jobs remains accurate for that component; the new records are separately identified.

The Python, PARI/GP and SageMath arithmetic replays use their documented versions. Their checks are designed to reject missing inputs, failed operations, unresolved precision, and arithmetic diagnostics even when a subprocess returns zero. Each verification record identifies which checks were actually executed. Independently checked arithmetic does not amount to an independent implementation of every computer-algebra primitive.

## Scope of the group statements

Rank four proves that the original point subgroup H0 has finite index. Its 2-saturation gives odd index. The 5-saturated group is H1, which contains the branch-division class E. It is H1 that has index coprime to 400 and covers the finite sieve coefficients. The logarithmic annihilator already extends from H0 by finite index. See [the correction notice](H0_H1_CORRIGENDUM.md).

A literature theorem or authenticated transcript is not silently promoted to a fresh independent computation. A formerly missing interface is no longer listed as open once its replacement proof and hypotheses have been checked; the ledger retains the earlier status and identifies the supplement.

## Asset identity

The first-submission assets have new basenames and a new release tag. Their exact byte sizes, SHA-256 values and verification results are recorded in the machine-readable indexes. `COMPONENT_MANIFEST.json` inside the companion identifies all its named components and top-level files. Earlier archives retain their identities, including records of failed attempts and superseded arguments. Older manuscripts inside those archives are historical evidence; the canonical paper is `paper/manuscript.pdf` at the top level of the companion and in this repository.
