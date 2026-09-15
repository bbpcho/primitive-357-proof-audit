# Response to the cumulative 15 September report

This record assesses the author-supplied `REFEREE_REPORT_ARXIV_CANDIDATE_15SEP.md`
against repository commit `b8d278de668861a30b72bdc947d7fdf84ab3d974` and the
current reviewer-corrected manuscript. The supplied file has SHA-256
`a3fdb49701d8786dd9f4b93dff1a16d04c77302b46b45f55de3cfad5fe82c69b`.
The report is identified here without redistributing its text. Its title
does not establish external human peer review.

## Which draft was reviewed

Sections 1–6 of the report concern the earlier 36-page paper. Section 7
concerns the first corrected source. Section 8 explicitly reviews the
current source ZIP, SHA-256
`2e4dfac874cecb55f16b1f18a039d430f7777ea472f9477129a0577b7ec976bf`,
and accepts the source corrections. Earlier findings must therefore be
read with those later dispositions.

The current 40-page PDF is already rebuilt and published, with SHA-256
`298c057b09e765e9bbe71ae4cd7460e323180691b7e4187201fa6bfffba121a5`.
The two source ZIP members still match the canonical LaTeX files byte for
byte. [ARTIFACT_CHECK.json](ARTIFACT_CHECK.json) records this fresh identity
check; the [preceding revision record](../reviewer-corrections-2026-09-15/README.md)
contains the clean build and visual checks. This response does not rebuild
or change the paper or source ZIP.

## Disposition

| Finding | Current disposition |
| --- | --- |
| F1: AI disclosure | Section 8.4 contains the author-approved detailed contribution statement. The repository README now carries the matching statement. Unestablished details suggested by the report, such as an unattended four-day run and independent re-derivation of every number, have not been added. |
| F2: archive identities | Both frozen archive hashes, sizes and release tags are printed. These archives have since been withdrawn; Section 8.5 must be updated for a verified replacement before submission. The current source ZIP's digest is recorded outside the ZIP and in this response, avoiding a self-referential checksum. |
| F3: licences | The author's MIT and CC BY 4.0 grants and full notices were already published. They exclude third-party material. PVT and other third-party distribution questions remain part of the replacement-companion work; adopting the author's licences does not settle them. |
| F4: rank exposition | Appendix D has been rewritten as mathematics, including the fake-descent definitions, local completeness argument, containing space and local conditions. The global two-torsion argument is explicit. Section 8 of the supplied report accepts these changes. |
| F5: citations | The paper now explicitly follows PVT v1's citation of Breuil–Diamond. The published Dembélé–Voight reference, corrected authors' version, MSC codes and keywords are present. The Raynaud locator was checked against the primary article; see the reference review below. |
| F6: attribution of the old filter | The text says “our earlier computation” and “filter in our earlier computation”. No further source change is needed. |
| F7: smaller points | “Calm” is removed. The calculator's observed 60-second limit and both full-group proof flags are documented in the Magma audit. The historical V3 PDF is now under `audit/historical-manuscripts/`, with unchanged bytes. The saved-capture validation command now requires an explicit extraction path. |
| Section 7: prime above 1051 | The current appendix gives the chosen prime, the factor pattern `1^8 2^10` and local two-torsion dimension 4. The earlier suggestion of complete splitting and dimension 6 was not adopted; the report's Section 8 accepts the correction. |
| Section 8: rebuilt PDF and repository notices | Already completed before this report was supplied, except the full README disclosure, now added. |

## A correction to the report's mathematical reasoning

Sections 2 and 5 suggest that the branch profiles `7^2 1`, `5^3` and `3^5`
identify the printed parameter with the Fano resolvent parameter because a
projective-line automorphism fixing 0, 1 and infinity is the identity.
That conclusion does not follow from the branch profiles alone. One first
has to establish that the covers are related by such an automorphism, or
prove an applicable uniqueness theorem. Fixing the three branch values
only removes a normalization ambiguity after that relation is established.
No assertion that this particular passport has multiple realizations is
needed to identify the missing inference.

The current paper uses stronger evidence: the exact canonical substitution
and both inverse-coordinate identities over the number field, including
nonzero denominators. It does not use the report's shortcut. The supplied
finite-prime computations are useful consistency checks, not substitutes
for that exact identification. See
[FANO_IDENTIFICATION_REVIEW.md](FANO_IDENTIFICATION_REVIEW.md) for the
manuscript and verifier references and the scope of this check.

## Remaining submission work and verification boundary

The two large public archives containing the Dahmen–Siksek PDF were already
withdrawn; their [withdrawal record](../dahmen-removal-2026-09-15/README.md)
records the download and history checks. The PVT snapshot embedded in those
large assets is no longer distributed through those downloads. This is
not a clearance of all third-party material: the separate p=5 and rank
packages remain public, and the replacement plan includes full-paper
copies and upstream software. A local derivative with the Dahmen–Siksek
PDF removed is not a complete verified replacement.

Before submission, the complete replacement companion needs resolved
third-party distribution arrangements, an explicit dependency contract,
and successful replay from a clean extraction. Section 8.5 must then name
that actual available release. The author reports that the email to
Dahmen has been sent; the requested reply remains pending. No arXiv
submission is recorded.

The report itself marks major computations as imported or not inspected.
This follow-up checks its disposition against the current files, inspects
the exact-identification argument, and validates existing records. It does
not claim a fresh complete arithmetic replay, a new Magma execution,
proof-assistant formalization, or independent human specialist review.

Additional evidence: [REFERENCE_AND_RECORD_REVIEW.md](REFERENCE_AND_RECORD_REVIEW.md).
