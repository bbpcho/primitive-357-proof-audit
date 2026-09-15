# First-submission editorial review

Reviewed 15 September 2026 against `EDITORIAL_CHANGES.diff`, `EDITORIAL_CHANGES.json`, `checks/prepare_paper.py`, and the resulting `paper/manuscript.tex`. No mathematical computation was rerun and no manuscript or preparation script was edited in this review.

Final synchronized manuscript SHA-256: `3619e519ae58533573cc5b5ebd6e86df0f063a916376200949c6c8ab8cb6c507`. The replacement replay, hash checks, mathematical-span comparison and unchanged-environment/appendix checks described below were repeated successfully against this final text.

The changes are suitable for a first submission. The author and affiliation are the supplied Peter Chocian and Independent researcher; no email was invented. The title and normal manuscript date remove the internal audit-draft framing. The citations to Dahmen–Siksek, Putz and Pacetti–Villagra Torcomian remain citations to other authors' work. The GitHub tag is explicitly a version identifier for the source and data component, not an earlier paper or arXiv submission by the author.

I independently replayed the declared text replacements in memory and confirmed both recorded manuscript hashes. All 944 inline/display mathematical spans are unchanged in order, after ignoring whitespace. The complete equation, align, theorem, proposition and proof environments are unchanged. The included rank appendix is byte-identical. The actual diff contains no mathematical formula or theorem alteration. These are text-integrity checks, not mathematical reruns or a new theorem verification.

The necessary trust qualifications are retained:

- Cited general theorems and the rational/twisted rank and torsion results remain explicit inputs.
- The finite-field 173 argument supplies the separate two-saturation step.
- The seven Magma executions retain the software version and their exact input/output evidence; they are expressly not independent implementations of Magma's algorithms.
- Numerical height comparisons do not replace exact height bounds.
- The source/data component and supplementary verification materials are distinguished within the single companion collection.
- Integrity checks and checksums are explicitly distinguished from arithmetic replay and mathematical conclusions.
- The actual local-image, fake-kernel, literal-c and H0/H1 interfaces remain named.

The companion filename and component references describe the intended assembled collection coherently. Confirming its final contents, checksums and replay instructions belongs to the separate packaging verification; this editorial review does not claim the forthcoming ZIP has already been sealed.

The minor wording issues identified in the initial review are resolved in the final text: it now uses “an existing argument,” “standard results in descent,” “results in” before the citation, and “Seven archived Magma inputs.” The repository hyperlink has a shorter display label while retaining its original target. These final adjustments introduce no change in mathematical or verification scope.

No further editorial correction is required before packaging. The mathematical audit and its stated import boundaries remain separate from this presentation review.
