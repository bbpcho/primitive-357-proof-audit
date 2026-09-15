# The Primitive Generalized Fermat Equation x³+y⁵=z⁷

**A computer-assisted proof — Peter Chocian, Independent researcher**

Pre-submission review revision · 15 September 2026

This repository accompanies the paper proving that `x^3 + y^5 = z^7` has no solution in nonzero coprime integers. It is prepared for the author's first arXiv submission on this equation. Citations to Dahmen–Siksek, Putz and other authors refer to their work; dates in the computational archives identify evidence versions, not earlier papers by Peter Chocian.

Read the [revised paper (PDF)](paper/manuscript.pdf), its [LaTeX source](paper/manuscript.tex), and the [rank appendix](paper/rank-proof.tex). The [current arXiv source ZIP](release/PRIMITIVE_357_ARXIV_SOURCE_REVIEWER_CORRECTED_2026-09-15.zip) contains only the two LaTeX files; use `manuscript.tex` and pdfLaTeX. This revision clarifies the place above 1051 and the transitivity argument for rational two-torsion, completes the bibliography and subject classification, and records the author's fuller Claude attribution and approved licences. The [latest revision record](audit/reviewer-corrections-2026-09-15/README.md) binds the files and checks. The [preceding records](audit/pre-submission-2026-09-15/README.md) document the Appendix D rewrite, printed evidence hashes and other publication fixes; the [earlier disclosure revision](audit/ai-disclosure-2026-09-15/README.md) retains its historical identity.

Submission remains on hold for Dahmen’s reply and resolution of third-party redistribution, including the PVT snapshot and full-paper copies inside nested archives. This revision has not been submitted to arXiv. The earlier paper and computational records retain their identities; the two large archive downloads have been withdrawn as described below.

The [round-9 review](audit/round9-review-2026-09-15/README.md) reproduces the new exact counts and divisors, documents repairs to the supplied scripts, and distinguishes numerical monodromy evidence from exact identification. The [preceding referee-report response](audit/referee-report-2026-09-15/README.md) distinguishes the earlier findings from their dispositions. The [authorless V3 working manuscript](audit/historical-manuscripts/README.md) is retained under `audit/` for provenance.

## Current availability

On 15 September 2026, the two large public assets `PRIMITIVE_357_FIRST_SUBMISSION_COMPANION_V1.zip` and `PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip` were withdrawn because a nested archive contained the Dahmen–Siksek working paper without redistribution permission. Their release pages and original checksums remain as historical records. The [withdrawal record](audit/dahmen-removal-2026-09-15/README.md) identifies the affected assets and verification scope.

The current paper and small source ZIP linked above remain available. Earlier project PDFs, source ZIPs and the separate p=5 and rank packages also remain available; those public files do not contain the identified Dahmen–Siksek PDF. The public control repository and its reachable Git history do not contain it, so no Git-history rewrite was needed.

A complete replacement computational companion is not yet published. The paper's Section 8.5 records the withdrawn archives' historical identities; its links now lead to withdrawal notices. These identities must not be read as a claim that the complete replay inputs are currently downloadable. A replacement requires a new archive identity and verification of its dependencies, as well as resolution of other third-party material. Citations to the mathematical literature remain in the paper.

## What was checked

The argument audit records **118 grouped claims and 70 named imported dependencies**, with no unresolved project-specific nodes at the level reviewed. It covers the rank and local-image arguments, the exceptional-field comparison, the reducible sectors and their mathematical interfaces. The canonical paper incorporates the reviewed corrections.

The historical companion included seven Magma input jobs executed through the official calculator, version V2.29-10, and four negative controls. These include the rational and twisted full-group computations used in the cubic–quartic sector. The finite-field 173 argument supplies the separate two-saturation step; numerical height comparisons do not replace exact height bounds.

**This is not proof-assistant certification or external human peer review.** The argument imports the cited mathematical theorems and computer-algebra algorithms. A recorded execution is not an independent implementation of that software. The [proof status](docs/PROOF_STATUS.md) and [evidence guide](docs/EVIDENCE.md) give the precise review and replay boundaries.

The repository includes the [argument-audit report](audit/logical-audit-2026-09-15/AUDIT_REPORT.md), [claim ledger](audit/logical-audit-2026-09-15/PROOF_LEDGER.md), [Magma replay records](audit/magma-replay-2026-09-15/README.md), and [first-submission record](audit/first-submission-2026-09-15/README.md). The argument-audit extracts and Magma records support convenient review; the complete evidence collection and large replay inputs were in the withdrawn companion.

## Substantial AI-assisted research and writing

OpenAI Codex was used extensively in developing and checking mathematical arguments, computational investigation, program and certificate development, verification design, debugging, release preparation, and drafting and revising the manuscript. OpenAI ChatGPT also supported the research and writing. Anthropic Claude acted as an independent auditor, reproducing the finite data from published inputs and reviewing every draft; its findings led to the database-free identification of Q(√−35) and to the model-intrinsic formal-group argument at the prime above 7. Peter Chocian originated the project's discovery approach and research direction, supplied key inputs, reviewed the evidence, and accepts responsibility for all claims. AI-generated suggestions and reviews are not mathematical certificates: the proof rests on the arguments given in the paper, the cited results and the specified computations. These AI-assisted reviews do not constitute independent human peer review or proof-assistant formalization.

## Evidence and verification

The historical companion combined the unchanged 14 September source/data release with the separate argument-audit and Magma materials. Its component manifest records filenames, sizes and SHA-256 values. The original manuscripts and replay logs remain identified as historical evidence; the current paper is in this checkout's `paper/` directory.

For an existing local copy, the historical command `python3 checks/verify_companion.py` checks identities against that original component manifest. It does not restore a public download, certify redistribution permission, or verify a newly repacked release. Mathematical replays retain each component's recorded scope and runtime requirements.

In this repository, `make verify` checks the repository records and `make paper` builds the manuscript. The [programs guide](release/PROGRAMS_AND_CERTIFICATES.md) describes the earlier integrated computational component. The [rank reconstruction](docs/RANK_GAP.md) and [H0/H1 correction](docs/H0_H1_CORRIGENDUM.md) retain their identified historical scope.

Exact source/data archives retain their original filenames and checksums. Original code is licensed under MIT; the original paper and documentation are licensed under CC BY 4.0. These grants explicitly exclude third-party material. See [LICENSE.md](LICENSE.md) and [NOTICE.md](NOTICE.md).
