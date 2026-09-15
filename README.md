# The Primitive Generalized Fermat Equation x³+y⁵=z⁷

**A computer-assisted proof — Peter Chocian, Independent researcher**

Pre-submission review revision · 15 September 2026

This repository accompanies the paper proving that `x^3 + y^5 = z^7` has no solution in nonzero coprime integers. It is prepared for the author's first arXiv submission on this equation. Citations to Dahmen–Siksek, Putz and other authors refer to their work; dates in the computational archives identify evidence versions, not earlier papers by Peter Chocian.

Read the [revised paper (PDF)](paper/manuscript.pdf), its [LaTeX source](paper/manuscript.tex), and the [rank appendix](paper/rank-proof.tex). The [current arXiv source ZIP](release/PRIMITIVE_357_ARXIV_SOURCE_REVIEWER_CORRECTED_2026-09-15.zip) contains only the two LaTeX files; use `manuscript.tex` and pdfLaTeX. This revision clarifies the place above 1051 and the transitivity argument for rational two-torsion, completes the bibliography and subject classification, and records the author's fuller Claude attribution and approved licences. The [latest revision record](audit/reviewer-corrections-2026-09-15/README.md) binds the files and checks. The [preceding records](audit/pre-submission-2026-09-15/README.md) document the Appendix D rewrite, printed evidence hashes and other publication fixes; the [earlier disclosure revision](audit/ai-disclosure-2026-09-15/README.md) retains its historical identity.

Submission remains on hold for Dahmen’s reply and resolution of third-party redistribution, including the PVT snapshot and full-paper copies inside nested archives. This revision has not been submitted to arXiv. The published V1 paper and companion retain their original identities; the current paper is a subsequent revision. Their preservation does not certify redistribution rights.

## Frozen downloads

The earlier first-submission release is [`first-submission-2026-09-15.1`](https://github.com/bbpcho/primitive-357-proof-audit/releases/tag/first-submission-2026-09-15.1).

| Asset | Purpose | Size |
|---|---|---:|
| [PRIMITIVE_357_ARXIV_SOURCE_PETER_CHOCIAN_V1.zip](https://github.com/bbpcho/primitive-357-proof-audit/releases/download/first-submission-2026-09-15.1/PRIMITIVE_357_ARXIV_SOURCE_PETER_CHOCIAN_V1.zip) | The two LaTeX files for the arXiv source upload; main file `manuscript.tex`, processor pdfLaTeX. | 35,879 bytes |
| [PRIMITIVE_357_FIRST_SUBMISSION_COMPANION_V1.zip](https://github.com/bbpcho/primitive-357-proof-audit/releases/download/first-submission-2026-09-15.1/PRIMITIVE_357_FIRST_SUBMISSION_COMPANION_V1.zip) | Paper, full source/data release, argument audit, supplementary checks and Magma execution records. | 601,649,354 bytes |

The large companion stays on GitHub; it is separate from the small arXiv source upload. Publishing these files on GitHub does not submit the paper to arXiv.

The release also provides the [paper as a separate PDF download](https://github.com/bbpcho/primitive-357-proof-audit/releases/download/first-submission-2026-09-15.1/PRIMITIVE_357_PETER_CHOCIAN.pdf). Check the [release SHA-256 sums](audit/first-submission-2026-09-15/SHA256SUMS.txt) when downloading assets.

## What was checked

The argument audit records **118 grouped claims and 70 named imported dependencies**, with no unresolved project-specific nodes at the level reviewed. It covers the rank and local-image arguments, the exceptional-field comparison, the reducible sectors and their mathematical interfaces. The canonical paper incorporates the reviewed corrections.

The companion includes seven Magma input jobs executed through the official calculator, version V2.29-10, and four negative controls. These include the rational and twisted full-group computations used in the cubic–quartic sector. The finite-field 173 argument supplies the separate two-saturation step; numerical height comparisons do not replace exact height bounds.

**This is not proof-assistant certification or external human peer review.** The argument imports the cited mathematical theorems and computer-algebra algorithms. A recorded execution is not an independent implementation of that software. The [proof status](docs/PROOF_STATUS.md) and [evidence guide](docs/EVIDENCE.md) give the precise review and replay boundaries.

The repository includes the [argument-audit report](audit/logical-audit-2026-09-15/AUDIT_REPORT.md), [claim ledger](audit/logical-audit-2026-09-15/PROOF_LEDGER.md), [Magma replay records](audit/magma-replay-2026-09-15/README.md), and [first-submission record](audit/first-submission-2026-09-15/README.md). The argument-audit extracts and Magma records support convenient review; the complete evidence collection and large replay inputs are in the companion.

## Evidence and verification

Begin with `README.md` inside the companion. Its component manifest records filenames, sizes and SHA-256 values. The companion includes the unchanged [`verified-2026-09-14.1`](https://github.com/bbpcho/primitive-357-proof-audit/releases/tag/verified-2026-09-14.1) source/data release and the separate argument-audit and Magma materials. Manuscripts inside those fixed components are evidence history. The current revision is in this checkout's `paper/` directory; the frozen companion's top-level `paper/` directory contains the preceding V1 manuscript.

After extracting the companion, `python3 checks/verify_companion.py` checks file identities. Follow each component's guide for its mathematical replays and runtime requirements. The new collection does not claim a newly executed combined replay or a single command that replays every supplementary check. Integrity checks, arithmetic replay and mathematical implication have distinct scopes.

In this repository, `make verify` checks the repository records and `make paper` builds the manuscript. The [programs guide](release/PROGRAMS_AND_CERTIFICATES.md) describes the earlier integrated computational component. The [rank reconstruction](docs/RANK_GAP.md) and [H0/H1 correction](docs/H0_H1_CORRIGENDUM.md) retain their identified historical scope.

Exact source/data archives retain their original filenames and checksums. Original code is licensed under MIT; the original paper and documentation are licensed under CC BY 4.0. These grants explicitly exclude third-party material. See [LICENSE.md](LICENSE.md) and [NOTICE.md](NOTICE.md).
