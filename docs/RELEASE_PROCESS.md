# Release process

The current release is [`replay-companion-2026-09-15.2`](https://github.com/bbpcho/primitive-357-proof-audit/releases/tag/replay-companion-2026-09-15.2), with `PRIMITIVE_357_REPLAY_COMPANION_2026-09-15_V2.zip` and the separate `PRIMITIVE_357_ARXIV_SOURCE_2026-09-15_V2.zip`. The [replacement audit](../audit/replacement-release-2026-09-15/README.md) records the actual identities and completed checks. The procedure below describes the required binding for this release and future replacements.

## Candidate, replay and publication

1. Prepare the manuscript revisions and check their layout. Leave the final companion identity unsettled until step 6. The author is Peter Chocian, Independent researcher; retain the approved contribution and licence statements.
2. Assemble the exact public evidence subset, object map, transformation records and pinned external-input lock. Scan every public payload and nested archive for excluded material. Acquire and authenticate the required upstream files privately, then regenerate the declared derived inputs to their exact expected hashes.
3. Extract the candidate into a clean directory and authenticate its public manifest. Materialize its logical and private external inputs in fresh directories. Run `scripts/replay_companion.py` inside a process-wide offline isolation boundary with only those proof input roots and the explicitly declared software dependencies. Follow the [programs guide](../release/PROGRAMS_AND_CERTIFICATES.md) for the complete command and runtime arguments.
4. Require all 13 sector/interface records, all 65 prior jobs and all 16 rank-local checks. Verify the five fresh rank-local input joins, complete stage logs, before/after input identities and independent completed-result checks. Retain failed environment attempts separately; a partial run or saved PASS is not a replacement for this full run.
5. Add the completed verification records and current release metadata. Preserve every tested mathematical input's identity and map. Verify the binding from the final public distribution to the tested logical manifest, external lock and complete result. Record any metadata-only additions explicitly.
6. Seal the final ZIP under its new basename. Record its exact size and SHA-256, re-extract and authenticate it, and repeat the public-content scan over the final bytes. Insert that identity into the current manuscript, then build the final PDF and small source ZIP. Check a clean source extraction and inspect the final PDF. Bind these current paper/source identities outside the sealed companion, keeping them separate from historical manuscripts carried as evidence; do not put the final paper back into the archive whose digest it prints.
7. Publish the authorized GitHub release and verify the actual public downloads against the sealed identities. Withdraw superseded downloads containing excluded full papers only after the replacement is available; retain their original filenames, hashes, release notes and withdrawal verification.
8. Update the current release, paper, availability and submission-readiness records in the control repository. Preserve the old computational baseline and audit bindings as historical records. Refresh the exact repository snapshot manifest and run repository verification, including optimization mode, and targeted verification of the new indexed assets.

The acquisition step is online preparation; arithmetic replay is offline. The wrapper does not establish operating-system isolation itself. Public distribution, cache, logical inputs, private external inputs and output must have separate roots. No upstream acquisitions or private cache are uploaded.

## Immutable history and proof boundary

A changed archive gets a new name, checksum and release identity. Older mathematical results, failed attempts and withdrawn-asset records are retained in their original scope. The inner logical manifest's `verified-2026-09-14.1` label is the inherited verifier's compatibility contract; the new public manifest and completed-run binding identify this replacement.

The repository verifier checks identities and recorded status; it does not execute the complete arithmetic suite. The seven earlier official Magma executions and four negative controls remain identified evidence, not computations rerun by this suite. Published mathematical results and software algorithms remain explicit premises. Neither successful replay nor the argument audit is proof-assistant certification or external human peer review.

GitHub publication does not submit the paper to arXiv. The requested Dahmen reply remains the submission hold.
