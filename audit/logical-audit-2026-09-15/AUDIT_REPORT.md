# Mathematical argument audit — 15 September 2026

**Two manuscript errors have been corrected in a separate review draft. A third error in an older explanatory note is documented. After the supplementary checks, this audit found no remaining project-specific gap in the assembled argument, subject to the explicit literature and software dependencies below.**

This is a computational and mathematical review, not proof-assistant certification or external human peer review. The assertion “no remaining gap identified” describes the outcome of the work performed. It is not a guarantee that the paper contains no further error.

## Corrections

1. **The exceptional-sector parity labels were reversed.** In the paper's convention X^5+Y^3=Z^7, Y even gives residual trace−1 and X even gives trace0. The sentence and table labels are fixed. Both branches were already included in the finite calculation, so the terminal numerical exclusion is unchanged. The draft also proves why Z is odd in this sector.

2. **The common quintic base points were not correctly accounted for.** An exact calculation at23 gives the common base point[1:15:5] with cancelled parameter2, outside the three branch values. A finite-flat argument lifts it to characteristic zero. The draft replaces the erroneous scope statement with the unique extension of the rational function after local cancellation. The finite sieve already treats common-zero reductions conservatively, so its terminal exclusion survives.

3. **An archival support note names the wrong conjugate prime over29.** HNF[29,22;0,1] is the printed s=15 place, not s=14. A fresh resultant and actual-prime calculation confirm that the numerical support data already use the correct place. No support generator or restriction matrix has been changed.

The full old/new text and reasons are in MANUSCRIPT_CHANGES.json, with a unified diff in MANUSCRIPT_CHANGES.diff. The draft also makes several proof interfaces explicit: the nonrational coordinate needed by the cubic-quartic exclusion, the full-group norm identity, and the P1 equations, whole-disk Hensel argument and precision bounds. There are13 recorded edits including dating and computational-scope statements.

## Audit coverage

The assembled PROOF_LEDGER.json has118 grouped claim nodes and70 named imported dependencies. It joins the global case split, three reducible branches, seven-field classification, pure-field geometry/rank/parameter argument and exceptional modular argument. Its dependency graph is acyclic. After applying the explicitly identified supplemental reviews and draft corrections, no project-specific node remains marked open.

These are grouped mathematical obligations, not a formal encoding of every sentence. A “checked argument” records a reviewed deduction from its premises; a “checked computation” records the precise arithmetic and evidence named in that row. The ledger preserves superseded open rows and original error statuses. It also propagates literature dependencies into the terminal claim, so a checked final deduction cannot silently erase an imported premise.

Fresh work in this pass includes:

- Exact polynomial, discriminant, norm, endpoint and local-obstruction calculations for the global and reducible cases.
- All16 adapted genus-two coordinate identities, exhaustive whole-residue-ball bounds and the infinity argument in Section7.
- Exact contact and incidence identities, all196 target fibres, all40,950 conic tests and the intrinsic theta/tower binding.
- Coherent global square-root signs, actual p5 sources and physical characters, and the dyadic corrections with explicit field/factor uncertainty.
- An independent Macaulay resultant, the complete support-prime binding and the exact free regulator determinant.

The review also examined the source and mathematical implications of substantial earlier computations: odd class numbers, unit indices, actual-completion restrictions, local source images, finite sieves and Hecke exclusions. Those are labelled as previously replayed evidence where they were not rerun here. Separate agent reviews checked the especially delicate global rank foundation, formal-local bounds and geometry. These agents are part of this AI audit, not external human referees.

The separate fresh-Magma addendum records seven unchanged jobs completed through the official free calculator, versionV2.29-10, with four negative controls. It includes the retained full-group, genus-two and elliptic-cover computations. The floating height comparison does not replace the exact height-bound argument.

## Remaining trust and submission status

The argument still imports substantial mathematics, including the Dahmen–Siksek local/reducible results, Putz's complete field classification, the BPS descent framework, Flynn's formal-neighbourhood theorem, and the specified modularity and level-lowering results. This audit checked their stated applicability; it did not re-prove every internal argument or recreate every external enumeration.

It also trusts the stated exact-arithmetic and mathematical algorithms in PARI/GP, SageMath, Magma and Arb. Many conclusions were checked through independent identities or implementations, but that does not amount to a formal proof of those software systems.

The strongest next independent validation would be a human specialist review of the rank/descent and modular branches using this ledger and the exact evidence. Formalizing the complete proof in a proof assistant would be a separate substantial project. Neither has been completed, and the paper should not claim they have.

The original release remains frozen. The corrected document is clearly dated as a review draft, its author field is still blank, and no arXiv submission was made. This addendum does not turn the corrected draft into a newly published verified release; the final submission package must incorporate the corrections and carry its own identity.

## Deliverables and verification

- AUDIT_REPORT.md: this assessment.
- PROOF_LEDGER.json and PROOF_LEDGER.md: claims, dependencies, evidence, limitations and superseded rows.
- draft/manuscript.tex, draft/rank-proof.tex and draft/manuscript.pdf: the corrected review draft.
- MANUSCRIPT_CHANGES.json and MANUSCRIPT_CHANGES.diff: exact manuscript edits.
- ARCHIVAL_ERRATA.md: source and historical-note corrections.
- reviews/: detailed sector and supplemental reviews.
- checks/ and selected runtime/rank_geometry evidence: new checks and outputs.
- EVIDENCE_INDEX.json: hashes of the explicitly cited files, including external dependencies.

The draft compiled to36 pages with no overfull/underfull boxes or unresolved references. All pages were rendered and visually inspected, with enlarged checks of the amended passages. No clipping, overlap or missing glyphs were found. See reviews/pdf_visual_review.md.

This is an **audit addendum and review draft**, not a self-contained transitive replay archive. Its checks and evidence index deliberately refer to the sealed release and its original directory structure. The accompanying README states those dependencies and exact archive identities.
