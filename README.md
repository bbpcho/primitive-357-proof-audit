# The Primitive Generalized Fermat Equation x³+y⁵=z⁷

**A computer-assisted proof — Peter Chocian, Independent researcher**

Replacement release · 15 September 2026

This repository accompanies the paper proving that `x^3 + y^5 = z^7` has no solution in nonzero coprime integers. It is prepared for the author's first arXiv submission on this equation. Citations to Dahmen–Siksek, Putz and other authors refer to their work; dates in computational archives identify evidence versions, not earlier papers by Peter Chocian.

Read the [current paper](paper/manuscript.pdf), [LaTeX source](paper/manuscript.tex), [rank appendix](paper/rank-proof.tex), and [small arXiv source ZIP](release/PRIMITIVE_357_ARXIV_SOURCE_2026-09-15_V2.zip). The source ZIP contains the two LaTeX files; use `manuscript.tex` and pdfLaTeX.

## Current availability

The [replacement computational companion](https://github.com/bbpcho/primitive-357-proof-audit/releases/tag/replay-companion-2026-09-15.2) is published as `PRIMITIVE_357_REPLAY_COMPANION_2026-09-15_V2.zip`. The [replacement audit](audit/replacement-release-2026-09-15/README.md) binds its exact bytes, the current paper and source ZIP, separately acquired inputs, and the fresh isolated replay of the declared suite. That run covers **13 sector/interface records, 65 prior jobs and 16 rank-local checks**, with the latter joined to five freshly generated inputs.

The main irreducible-sector job uses `DEEP_REPLAY=0` and V15 without `--full`. Five separate isolated default checks cover the adapted V2/V3/V4/V5/V6 readers; these are additional records, not a claim that the full Hunter searches or optional V15/V7 modes were rerun. Their paths and commands are in the [replay guide](release/FINAL_COMPANION_REPLAY_GUIDE.md); the companion stores them under `records/completed-replay/supplemental/`. V5's eight exact support-set comparisons total **237,182 rows**. Its preserved aggregate label **236,182** is a reporting error, corrected in the supplemental record; all eight set comparisons passed. The [replacement audit](audit/replacement-release-2026-09-15/README.md) records this scope and erratum.

The companion supplies the project evidence, an exact input map, acquisition tools and reconstruction programs. Required third-party papers and unlicensed upstream source snapshots are acquired separately from pinned sources and authenticated before private materialization. The unchanged licensed Putz thesis and MPFR header retain their original notices. Seven historical native executables used only for byte authentication are omitted with their identities recorded; the mathematical checks remain. See the [programs guide](release/PROGRAMS_AND_CERTIFICATES.md) and [redistribution notice](NOTICE.md).

The earlier large companion and source-data downloads were withdrawn because they contained the Dahmen–Siksek working paper without permission. The older p=5 and rank downloads containing the BPS paper have also been withdrawn. Their filenames, checksums and release records remain historical identities; the replacement does not reuse them. See the [earlier withdrawal record](audit/dahmen-removal-2026-09-15/README.md) and [replacement audit](audit/replacement-release-2026-09-15/README.md).

**The paper has not been submitted to arXiv. The remaining submission hold is Dahmen's requested reply.**

## What was checked

The argument audit records **118 grouped claims and 70 named imported dependencies**, with no unresolved project-specific nodes at the reviewed lemma/interface level. The [audit report](audit/logical-audit-2026-09-15/AUDIT_REPORT.md), [claim ledger](audit/logical-audit-2026-09-15/PROOF_LEDGER.md), [proof status](docs/PROOF_STATUS.md) and [evidence guide](docs/EVIDENCE.md) identify its scope. The [round-9 review](audit/round9-review-2026-09-15/README.md) distinguishes exact divisor and counting checks from numerical monodromy evidence.

Seven [official Magma V2.29-10 executions and four negative controls](audit/magma-replay-2026-09-15/README.md) remain identified, previously executed evidence. They include the rational and twisted full-group computations used in the cubic–quartic sector. The replacement's integrated replay does not execute Magma. The finite-field argument at 173 supplies the separate two-saturation step; numerical height comparisons do not replace exact height bounds.

**This is not proof-assistant certification or external human peer review.** The proof imports the cited mathematical theorems and computer-algebra algorithms. A recorded execution is not an independent implementation of that software.

## Substantial AI-assisted research and writing

OpenAI Codex was used extensively in developing and checking mathematical arguments, computational investigation, program and certificate development, verification design, debugging, release preparation, and drafting and revising the manuscript. OpenAI ChatGPT also supported the research and writing. Anthropic Claude acted as an independent auditor, reproducing the finite data from published inputs and reviewing every draft; its findings led to the database-free identification of Q(√−35) and to the model-intrinsic formal-group argument at the prime above 7. Peter Chocian originated the project's discovery approach and research direction, supplied key inputs, reviewed the evidence, and accepts responsibility for all claims. AI-generated suggestions and reviews are not mathematical certificates: the proof rests on the arguments given in the paper, the cited results and the specified computations. These AI-assisted reviews do not constitute independent human peer review or proof-assistant formalization.

## Using this repository

`make verify` checks this control repository's records; it does not run the complete arithmetic suite. `make paper` builds the manuscript. Complete acquisition and replay instructions are in the [programs guide](release/PROGRAMS_AND_CERTIFICATES.md) and [complete replay guide](release/FINAL_COMPANION_REPLAY_GUIDE.md).

The [first-submission record](audit/first-submission-2026-09-15/README.md), [reviewer corrections](audit/reviewer-corrections-2026-09-15/README.md), [rank reconstruction](docs/RANK_GAP.md), [H0/H1 correction](docs/H0_H1_CORRIGENDUM.md) and [historical manuscripts](audit/historical-manuscripts/README.md) preserve their earlier scope. The current canonical paper is in `paper/`; older manuscripts inside the evidence are provenance.

Original code is MIT licensed; the original paper and documentation are CC BY 4.0. These grants exclude third-party material. See [LICENSE.md](LICENSE.md) and [NOTICE.md](NOTICE.md).
