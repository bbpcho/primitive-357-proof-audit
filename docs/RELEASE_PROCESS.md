# Release process

The mathematical rank gate is closed. Promotion of this integrated candidate to the verified release separately requires a fresh replay of its exact input set and verification of the sealed asset.

## Candidate and sealing procedure

1. Finish the manuscript and guide, build the paper, and inspect the changed PDF pages.
2. Assemble declared immutable evidence and adopted checks in a new release directory. Generate its complete input manifest.
3. Extract a newly created candidate archive into a clean directory. Run `scripts/verify_release.py --replay` with the documented Python, Sage and PARI/GP runtimes and a fresh output directory outside the extracted input.
4. Require all three components: prior foundations, rank/local reconstruction and sector checks. Preserve complete logs, the integrated result and the tested input manifest.
5. Add compact verification records to the final archive. Every tested input must retain its exact path, size and hash. The proof-input index must cover every tested manifest row; the final manifest may add the final records.
6. Seal the new archive under its new basename, record its size and SHA-256 in the asset index, and verify the actual archive bytes.
7. Copy the integrated result, logs, tested manifest, proof-input index, final manifest and their binding record into the control repository. Set the release status to verified only when their required identities and successful component records agree.
8. Regenerate the control-repository snapshot manifest and run both repository verification and asset verification, including Python optimization mode. Review the resulting commit and attach the sealed archive to the authorized GitHub release.

The control verifier checks the structure and identity of recorded evidence. The arithmetic verifier reconstructs its declared calculations. Neither replaces the mathematical implications and imported premises stated in the manuscript and guide.

## Names and immutable history

This release uses tag `verified-2026-09-14.1` and asset `PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip`. Earlier tags and archives remain unchanged. A later repair receives a new name and manifest; an existing sealed archive must not be recompressed under the same name.

The author field in the supplied manuscript remains for the author to complete before arXiv submission. The release does not invent author, affiliation or license metadata. Published results and the identified historical Magma computations retain their explicit provenance.
