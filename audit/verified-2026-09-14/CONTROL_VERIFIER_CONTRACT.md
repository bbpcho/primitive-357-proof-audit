# Control-verifier adoption and final replay binding

The manuscript's mathematical rank gate is complete. The draft `audit/status.json` intentionally has `release_state: pending_fresh_replay`, `proof_complete: false` and `public_proof_release_authorized: false` until the new release's own final records are available. These publication flags do not reopen the completed independent rank audit.

Copy all four programs together: `scripts/verify_repository.py`, `scripts/verify_assets.py`, `scripts/verification_common.py`, and `scripts/test_verifiers.py`. The shared module is required. The workflow runs normal, `-O` and `-OO` verification and the synthetic controls. No validation depends on an assert statement. The status schemas are v2; legacy open-rank status is intentionally not treated as the current release decision.

## Final promotion record

After the real fresh replay succeeds and the archive is sealed, copy the actual result, component logs, tested manifest, proof-input index and final manifest into `audit/verified-2026-09-14/`. Preserve the `logs/` directory relative to the copied `REPLAY_RESULT.json` as recorded by the orchestrator.

Create `REPLAY_BINDING.json` with the following structure; replace every digest and size with the computed value, not a placeholder:

```json
{
  "schema": "primitive357_replay_binding_v1",
  "release_tag": "verified-2026-09-14.1",
  "asset_id": "PRIMITIVE_357_VERIFIED_RELEASE_2026_09_14_V1",
  "asset_sha256": "<sealed archive SHA-256>",
  "asset_bytes": 0,
  "replay_result": {"path": "audit/verified-2026-09-14/REPLAY_RESULT.json", "sha256": "<SHA-256>"},
  "tested_manifest": {"path": "audit/verified-2026-09-14/TESTED_RELEASE_MANIFEST.json", "sha256": "<SHA-256>"},
  "proof_inputs": {"path": "audit/verified-2026-09-14/PROOF_INPUTS_SHA256.json", "sha256": "<SHA-256>"},
  "final_manifest": {"path": "audit/verified-2026-09-14/FINAL_RELEASE_MANIFEST.json", "sha256": "<SHA-256>"}
}
```

The proof-input index has schema `primitive357_proof_inputs_v1`, the release tag, and a sorted `files` array containing every tested manifest row, with exactly `path`, `sha256` and `bytes`. All those identities must remain unchanged in the final manifest. The final manifest may additionally contain final verification records. Thus an index that selectively omits a tested input does not pass.

The replay result must use schema `primitive357_integrated_replay_v1`, status `PASS_FRESH_INTEGRATED_REPLAY`, exactly the three component IDs `prior`, `rank_local`, `sectors`, integer exit codes zero and hash-matching component logs with their unique terminal success markers. It must bind the tested manifest's hash and file count, include the complete required prior-group list and affirm the actual B-plus-literal-c rank join.

Add the new sealed asset to `evidence/assets.json` and its exact checksum-list line. Then change `audit/status.json` to:

- `release_state: verified`;
- `proof_complete: true` and `public_proof_release_authorized: true`;
- `fresh_replay: {"state": "pass", "binding": "audit/verified-2026-09-14/REPLAY_BINDING.json"}`;
- states `pass` for the `fresh_integrated_replay` and `public_proof_release` gates;
- clear the human-readable `blocking_gate` once all required checks have actually passed.

Keep the imported-premises gate marked `imported`; it is not a claim to have rerun Magma. The rank workplan remains complete. Regenerate `evidence/TRACKED_SNAPSHOT_SHA256.txt` after all control files are final.

## File coverage and tests

The snapshot manifest must cover every ordinary file except itself, the root `.git/` and `build/` directories, and `.pyc`/`.pyo` files directly inside a directory named `__pycache__`. These are the only defined exclusions. A nested `evidence/build/` or `.git/` directory is not silently omitted. A non-bytecode cache payload must be tracked. Symlink files and directories, including symlink parent components of an indexed path, are rejected; non-regular filesystem entries are rejected. The asset index and checksum file must have the same nonempty, duplicate-free asset list, with strictly positive integer sizes and safe relative paths.

`checker_controls/CONTROL_VERIFIER_TESTS.json` records synthetic valid and invalid fixtures. These are tests of checker behavior, not fabricated arithmetic evidence. The real pending control snapshot is separately checked against the actual imported asset index. Actual asset-byte verification and final verified-state acceptance still require the real sealed archive and replay records.

These verifiers validate recorded identities and consistency. They do not authenticate a historical mathematical assertion merely because its text says PASS. The arithmetic programs and the manuscript's independently checked implications supply that distinct evidence.

## Checking only selected downloaded assets

`verify_assets.py` checks every indexed asset by default. To verify the new archive without downloading historical archives, use:

```bash
python3 -B scripts/verify_assets.py --assets-dir /path/to/downloads \
  --asset-id PRIMITIVE_357_VERIFIED_RELEASE_2026_09_14_V1
```

Repeat `--asset-id` for several indexed assets. Unknown or duplicate selections fail. The complete index and checksum-list structure are always validated; only the selected asset bytes are read. This option does not change the meaning of the default all-assets check. The selection controls and the regression for a verified hosting repository bring the test total to 55 cases and 165 executions across normal, -O and -OO modes.

## Archived replay records

Promotion additionally recomputes the complete artifact selection from the actual finished replay, using the synchronized local selector. Every retained result, job log, runtime record and mathematical binary must occur in the final archive with the same size and SHA-256. The final archive may add exactly the selected files and the declared assembly records to the tested inputs. The full Fano log and PDF-extractor runtime identity are mandatory. The candidate ZIP, tested manifest, proof-input index, top-level driver log, host record and archived selector are bound separately. This check rejects omitted/substituted evidence even when a forged final manifest is internally consistent. The 25 promotion cases pass in all three Python modes (75 executions).
