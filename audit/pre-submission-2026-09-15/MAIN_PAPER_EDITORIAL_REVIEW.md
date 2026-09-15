# Main-paper editorial consistency review

Reviewed 15 September 2026. Scope: the complete main-paper diff between `work/publication_2026_09_15/repository/paper/manuscript.tex` and `work/pre_submission_revision_2026_09_15/repository/paper/manuscript.tex`. Appendix D, its mathematical arguments, and its supplementary computations are outside this review. No manuscript was edited and no mathematical computation was rerun.

Baseline SHA-256: `3619e519ae58533573cc5b5ebd6e86df0f063a916376200949c6c8ab8cb6c507`.

Reviewed final revised SHA-256: `e49f621482dfe41fcd2bd0a5d251b88115e2083bee7064b9a0f457f3bf8cc852`.

## Outcome

The seven recorded edits preserve the existing mathematical formulas, theorem assertions, computational counts, and trust qualifications. The AI disclosure and ownership clarification are consistent. The narrow provenance ambiguity identified in the first review has been resolved in the final text: supplementary checks and Magma records are expressly limited to those assembled for the fixed release. No outstanding issue was found within this bounded main-paper review.

## Findings

1. **AI disclosure, revised lines 1296–1305: satisfactory.** ChatGPT and Codex are described as assisting argument development and checking, programs, verification materials, and writing. Claude is described only as used for error checking, consistent with the author's supplied description. The paragraph retains author responsibility and explicitly disclaims independent human peer review and proof-assistant formalization. It does not imply that AI review itself proves the theorem, or that the different tools supplied independent mathematical implementations. The preceding distinction between Magma execution and independent implementation remains intact at lines 1288–1294. This is a consistency review of the stated roles, not an independent reconstruction of all AI usage.

2. **Section 6.2, revised lines 1021–1037: satisfactory.** “Our earlier computation” and “the degree-48 filter in our earlier computation” correctly assign the earlier filtering omission to this project. The nearby PVT citation and upstream `Data.txt` description do not now suggest that PVT itself omitted the trace. The 17/18 coverage statement, trace at 131, and replacement by `T^{49}-T` are unchanged. The wording does not assert authorship of the upstream data.

3. **Section 8.5 archive identifiers, revised lines 1313–1326: consistent with the freshly checked records.** `checks/ARCHIVE_IDENTITIES.json` records the following identities, which agree exactly with the manuscript:

   | Component | Bytes | Release tag | SHA-256 |
   |---|---:|---|---|
   | `PRIMITIVE_357_FIRST_SUBMISSION_COMPANION_V1.zip` | 601649354 | `first-submission-2026-09-15.1` | `fa0eaae5e193010a0714b1e72fd141f146e3e155148d530706258e3bb42e9a90` |
   | `PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip` | 588945520 | `verified-2026-09-14.1` | `27e3e6eeb50f83ea484e7cd0c94dbd88de0141ab9f47634ed5181e7db0ecba33` |

   The recorded archive verification is a local byte/hash check, not a fresh arithmetic replay; this review does not upgrade its scope. `checks/MAIN_PAPER_DIFF_CHECK.json` records exact reconstruction by the seven edits, with the two source hashes above. I separately checked those source hashes, read the entire main-paper diff, and reread the final provenance paragraph after its correction. No mutable branch name is substituted for either fixed release identity.

4. **Section 8.5 chronology, revised lines 1312 and 1328–1348: concern resolved.** The initially reviewed text said that the fixed companion was used for “the checks reported here” and included “the exact supplementary checks”, potentially assigning later checks to the old frozen archive. The final text instead says “The fixed first-submission companion is” and limits its argument-audit materials, supplementary checks and seven Magma records to those “assembled for that release”. It also expressly preserves earlier manuscript copies as provenance while identifying subsequent exposition in the present document. This no longer suggests that the old archive was silently updated with new checks. The paragraph identifies the contents of the frozen records; it is not itself a verification or inventory of any later revision supplement.

   The final line 1333 also changes the ambiguous “It contains” to “The source and data component contains”, making the location of the geometric, 5-adic and rank-closure inputs explicit.

The statement that integrity checking alone is not arithmetic replay survives at lines 1348–1349, as do the explicit imported premises and exact-height qualification. No additional substantive editorial issue was found within the requested main-paper scope.

## Final layout-only binding addendum

The final built main source has SHA-256 `9568974a78699bedfea5aecce92e547fd0122b9306f790ffb6681f11f99838c1`. The two release tags were moved to centered displays, with “under release tag” changed to the introductory sentence “Its release tag is”. I checked this change by reversing those two exact layout blocks in memory: the result recovers the previously reviewed source hash `e49f621482dfe41fcd2bd0a5d251b88115e2083bee7064b9a0f457f3bf8cc852`. There are no other main-source changes. The archive identities, AI disclosure, ownership wording, provenance clarification, mathematical assertions, and trust qualifications retain the findings above.

The corresponding 39-page PDF has SHA-256 `d29b38ee9e41cebe695f358166eb04dadccc4322ac79189583a9c79bbe704e75`, size 533980 bytes. The completed visual review is recorded in `checks/PDF_VISUAL_REVIEW.md`; both tags and both full digests are clear on page 18. This addendum supersedes the earlier source hash only for final artifact binding, not for the scope of the editorial review.
