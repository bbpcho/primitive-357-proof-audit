# PDF visual review — 15 September 2026

**Result: no visual correction required.** Reviewed the complete 36-page corrected draft `draft/manuscript.pdf`, SHA256 `707e25f07262fb0bb8d6aa6cebf04c0bf65df209b1372f75fc1d6889657afd04`. All36 pages were rendered with Poppler and visually inspected in nine contact sheets. The changed passages on pages9,13–18 and32 were additionally inspected at150dpi; the long-table continuation pages29–30 were also opened individually. No PDF or TeX source was edited.

The PDF has25 portrait pages and11 landscape pages (20 and22–31). Printed page numbers run correctly from1 through36. The table of contents, headings, theorem/equation numbers, references, table continuation headings, and changes between portrait and landscape pages are visually intact.

## Changed-page checks

- **Page9:** the solution-bearing quotient formula, nonrational-U argument, norm/anti-norm identity, subgroup relation, odd-monic model and Kummer matrix are fully visible and spaced correctly. Superscripts, square roots and primes are legible.
- **Page13:** both normalized P1 equations, the two residue roots, determinants, seven/eight-digit precision explanation, and both large parameter values render correctly. The proof-end marker does not overlap the last line or the following paragraph.
- **Pages14–16:** the exceptional parity explanation and swapped X/Y-even table labels are visible; the weight-two and finite-filter scope paragraphs fit; the finite-flat formulas and final polynomial/table/resultant displays remain aligned and untruncated.
- **Pages17–18:** the new Magma-execution boundary and separate-addendum wording fit within the page text area. The archive identifier and verifier command are intact, and the three-column certificate table has no collisions or cut-off cells.
- **Page32:** the replacement common-zero/local-cancellation paragraph is complete. The reference values and local orders are visible, and the subsequent integral-coordinate and split-prime appendices retain correct spacing and table alignment.

## Overall layout and legibility

No clipped text, overlapping formula, missing glyph, black replacement square, broken fraction bar or truncated table row was found. A supplementary check of every PDF text character found zero characters outside the36 page boxes; this supported, and did not replace, the visual inspection. The compilation log has no overfull/underfull-box or undefined-reference warning. Its disabled-shell-escape notice does not indicate a rendering failure.

The exact coefficient ledger on pages22–31 uses approximately6.97pt numerator/denominator digits. This is compact and benefits from PDF zoom, but the digits are sharp and the rows and fractions do not overlap. It is an existing presentation choice, not a defect introduced by these corrections. Large blank areas around the landscape tables likewise arise from the explicit table-page layout; no content is lost.

Rendered pages, contact sheets, enlarged changed pages and the supplementary text-bound measurements are retained under `pdf_review/`. This is a visual QA result, not a new mathematical or coefficient-by-coefficient correctness claim; those conclusions belong to the separate argument and exact-data reviews.
