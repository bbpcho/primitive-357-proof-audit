# V3 release audit and handoff

Date: 13 September 2026

## Result

The revised paper and its dependency-closed companion release have been
built and verified.  The complete replay succeeded from a fresh extraction
inside an empty-root filesystem namespace.  The original working repository
was not visible there.

This V3 release directly addresses the independent V2 review.  It is not a
renaming of V2: the evidence closure, the foundational replay, the Section 7
argument, the manuscript, and the submission verifier all changed.

## Independent-review findings addressed

1. All 100 paths in `v2_missing_evidence.txt` are present at their original
   repository-relative locations and are individually indexed by SHA-256,
   byte size, role, and reverse reference.
2. Eight additional files discovered by actually running the restored
   generators are included.  These are the three local-condition binaries,
   three direct restriction inputs, the resumed norm table, and the geometry
   data packet required by the five-place workers.
3. The release now freshly executes both answer-separated five-place workers,
   compares their exact textual and semantic outputs, and replays the Selmer
   character projector and rank-four deduction.
4. Both split-prime global logarithm matrices at 23 are freshly reconstructed.
   Their mathematical JSON invariants agree exactly with the sealed records.
   Sage compressed-object byte identities are recorded but are not treated as
   canonical serialization.
5. The first complete rehearsal exposed a missing `identity_matrix` import in
   the historical `s=19` generator.  The historical source is preserved.  A
   separately indexed replay copy adds exactly that import and no mathematical
   change.
6. The Section 7 two-saturation step is replaced by the independent
   finite-field Kummer witness at `(173, theta-22)`.  The first four rows of
   the printed five-by-four character matrix have determinant one over F2.
7. The manuscript incorporates the review's attribution, conductor,
   level-lowering, Fano/function-field, terminology, bibliography, and Hecke
   coverage corrections.  Its companion-archive section now names the V3
   verifier and the full foundational replay.

## Complete clean-extraction replay

The sealed log is
`dependency_closed_release_v3/2026-09-13_primitive_357_dependency_closed_release_v3/logs/CLEAN_EXTRACTION_COMPLETE_REPLAY_V3.log`.

- Clean namespace status: `ORIGINAL_WORKSPACE=ABSENT` and
  `ORIGINAL_WORKSPACE_PATH_VISIBLE=0`.
- Exit status: 0.
- Wall time: 2489.040337 seconds.
- Repository closure: 765 exact files.
- Historical base: 369 rows across 52 manifests.
- Upstream snapshot: 17 exact files.
- Ordinary sector entry points: all ten passed.
- Foundational replay: passed.

The longest ordinary replay was the cubic--quartic Section 7 sector
(1618.918757 seconds).  The conservative Hecke ambient reconstruction took
185.767125 seconds.  The fresh five-place producer and independent worker took
75.981479 and 105.050512 seconds.  The two fresh global-log branches took
170.887924 and 190.143639 seconds.  The combined rank/Siksek certificate and
both exceptional local calculations also returned their exact PASS markers.

## Paper build

The paper is 32 A4 pages.  Three `pdflatex` passes complete with no unresolved
references, LaTeX warnings, overfull boxes, or underfull boxes.  The Appendix A
long coefficients are set in breakable display tables and do not overlap the
page margins.

Paper source SHA-256:

`565700bf54a5519dd97775bde64f892aada151e67f8d6cd0239fb82cc7896889`

Compiled release PDF SHA-256:

`5d5ec337f436f2d303b46e9956a454cb4a3a6bae7d7379d9f9d66db42e2e27ea`

## Programs and software boundary

The repository contains 222 mathematical program sources:

- 138 Python files;
- 39 PARI/GP files;
- 25 SageMath files;
- 20 Magma files.

The clean replay used Python 3.12, PARI/GP 2.15.4, SageMath 10.9, SymPy
1.14.0, and mpmath 1.3.0.  Magma was not installed on the build host.  For the
Magma-dependent specialist layers, the release contains the exact programs,
inputs, manifests, and authenticated completed logs; the V3 clean replay does
not falsely claim to have rerun proprietary Magma.

## Frozen artifacts

- Complete reproducibility archive:
  `anc/PRIMITIVE_357_REPRODUCIBILITY_V3.tar.gz`
  
  SHA-256: `99ef2fa0466277092ed39570748870648c08c596a68ecb50f55cfc5d59107f26`
- arXiv upload ZIP with complete ancillary release:
  `PRIMITIVE_357_ARXIV_UPLOAD_WITH_PROGRAMS_V3.zip`
  
  SHA-256: `6556c9135681d9d21327ca232dcaabf1184db79dbfba4b944f1b521df49695c7`
- Equivalent arXiv upload tarball:
  `PRIMITIVE_357_ARXIV_UPLOAD_WITH_PROGRAMS_V3.tar.gz`
  
  SHA-256: `a5fae5dac1ece532a3c08507a96fdc78ed78e93e17b7ae7200ca23e1ae12a466`
- Reader bundle:
  `PRIMITIVE_357_PAPER_AND_RELEASE_GUIDE_V3.zip`
  
  SHA-256: `3b89c5a42b9fa0eaae4e6a33c892ab72730bc88ac04d748c08010278f34bd0e3`

The submission verifier independently checks the upload exact set, both
archive formats, a fresh three-pass paper build, the complete companion
manifest, the Section 7 Kummer repair, and the 222-source inventory.  Its
default run passes.

## Deliberate final submission gates

Two matters are intentionally not guessed by the build system.

1. The manuscript author field is blank.  The submitting author must supply
   the desired name and affiliation before public submission.
2. The upload archive is about 260 MB because it carries the complete binary
   evidence closure.  arXiv treats unusually large submissions as exceptions;
   the submitter should either obtain an oversize exception or place the full
   companion archive in a durable data repository and submit a smaller arXiv
   source bundle that points to the deposited object by URL and SHA-256.
   Copyright and redistribution permission for the bundled third-party PDFs
   should be checked before choosing the oversize-upload route.

Those are publication choices, not mathematical replay failures.  No further
mathematical or packaging defect was found in the final V3 checks.
