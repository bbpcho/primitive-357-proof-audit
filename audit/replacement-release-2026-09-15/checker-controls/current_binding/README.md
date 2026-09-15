# Additive current-distribution binding

This directory contains a proposed additive control-repository check. It does not edit the control repository or change any historical 14 September status, gate, asset, or replay binding. No current companion is marked verified by creating these helper files.

Copy `verify_current_distribution.py` and `current_replay_coverage.py` together into the control repository's `scripts/` directory. `test_current_distribution.py` uses only the standard library and those two modules. After the existing historical checks, the parent may call:

```python
from verify_current_distribution import verify_current_distribution
current = verify_current_distribution(ROOT, read_json(regular_file(ROOT, "audit/status.json")))
```

The existing tracked snapshot manifest must then cover the added files and records. Existing historical `verify_status`/`verify_replay` behavior remains unchanged. The new function returns `CURRENT_DISTRIBUTION_NOT_VERIFIED` for the existing withdrawn state or an explicit pending state; it never turns either into a success claim.

## Final status/binding fields

After successful completion and publication, `status.current_distribution` should be:

```json
{
  "state": "verified_externalized_replay",
  "public_complete_replay_inputs_available": true,
  "replacement_complete_companion_published": true,
  "original_mathematical_replay_status_unchanged": true,
  "binding": {"path": "audit/replacement-release-2026-09-15/CURRENT_DISTRIBUTION_BINDING.json", "bytes": 0, "sha256": "REPLACE_WITH_ACTUAL_DIGEST"}
}
```

The displayed zero/placeholder are intentionally invalid. Fill them from the actual completed binding file. The binding object has these fields:

- `schema`: `primitive357_current_distribution_binding_v1`.
- `release_tag`: the public replacement tag, identical to both public manifests.
- `logical_release_tag`: `verified-2026-09-14.1`, the preserved internal compatibility identity.
- `asset`: `{name, bytes, sha256, url}`. The URL must equal the repository's GitHub release-download URL for this exact tag/name. The default check does not make a network request or assert remote availability from a status label.
- `archive_root`: the final ZIP's single enclosing directory name.
- `verification_prefix`: `records/completed-replay` (without a trailing slash).
- `local_artifact_root`: the control-repository directory containing copied completion logs with their original **outer-output-relative** names, e.g. `audit/replacement-release-2026-09-15/output-records`. The roughly 0.5MB of job/component logs can be copied here without copying software caches or full producer data.
- `records`: the exact eighteen roles in the table below. Each descriptor is `{path, bytes, sha256, archive_path}`. `path` names the committed control-repository copy; `archive_path` names the corresponding final companion member. All paths are relative, canonical and nonsymlinked.

| Role | Final archive member |
|---|---|
| `tested_public_manifest` | `records/completed-replay/TESTED_PUBLIC_MANIFEST.json` |
| `final_public_manifest` | `COMPANION_MANIFEST.json` |
| `logical_manifest` | `records/completed-replay/TESTED_LOGICAL_MANIFEST.json` |
| `replay_file_map` | `inputs/REPLAY_FILE_MAP.json` |
| `external_lock` | `inputs/EXTERNAL_INPUTS_LOCK.json` |
| `replay_contract` | `inputs/BASELINE_REPLAY_CONTRACT.json` |
| `externalized_result` | `records/completed-replay/EXTERNALIZED_REPLAY_RESULT.json` |
| `integrated_result` | `records/completed-replay/suite/REPLAY_RESULT.json` |
| `independent_envelope` | `records/completed-replay/INDEPENDENT_ENVELOPE.json` |
| `prior_result` | `records/completed-replay/suite/prior/PRIOR_REPLAY_RESULT.json` |
| `sector_result` | `records/completed-replay/suite/sectors/SECTOR_REPLAY_RESULT.json` |
| `rank_result` | `records/completed-replay/suite/rank_local/rank_local_results.json` |
| `retained_artifacts` | `records/completed-replay/RETAINED_ARTIFACTS.json` |
| `suite_selection` | `records/completed-replay/SUITE_ARTIFACT_SELECTION.json` |
| `isolated_driver` | `records/completed-replay/isolation/CLEAN2_ISOLATED_DRIVER.json` |
| `driver_log` | `records/completed-replay/isolation/OUTER_DRIVER.log` |
| `isolation_profile` | the indexed `records/completed-replay/isolation/clean2_offline.sb` |
| `isolation_probes` | the indexed `records/completed-replay/isolation/CLEAN2_PROBE_RESULTS.json` |

The names in the last two rows may follow the actual finalizer's copied filenames; the bound profile filename must match the driver's `-f` argument. The driver is the existing, unmodified `primitive357-isolated-driver-v1` record, with `PASS_ISOLATED_DRIVER`, `exit_code: 0`, `output_did_not_exist: true`, start/finish times, original command/environment, and its existing input/profile/outer-log hashes. No derived record should replace or relabel the actual driver.

`RETAINED_ARTIFACTS.json` is the finalizer's `primitive357_retained_replay_artifacts_v1` index with sorted `{path, archive_path, bytes, sha256}` rows and `source_suite_selection_sha256`. Completion-log bytes resolve at `local_artifact_root/path`; a row may optionally specify an explicit `local_path` instead. Other generated payloads do not need local duplicate copies merely to check their record joins. Every retained row must be present with the same identity in the final public manifest.

For an original copied source omitted by the differential selector, the checker uses only the exact `suite_selection.excluded` row with `reason: identical_sealed_input_copy`, its `candidate_path`, and equal size/SHA in the bound logical manifest/map. Public objects and locked external sources remain distinct. It does not infer a source path from a matching hash, redistribute an external source, or require copying the old repository. This rule also supports an exactly identical producer output if the selector explicitly records that exclusion.

## What is checked

- Every tested public row is preserved exactly in the final manifest. Only records under the append prefix may be added. The final manifest points to the bound outer replay result and tested manifest identity. Logical input mapping, object/external identities and the internal logical manifest remain unchanged.
- The full outer result binds the tested public/logical/lock identities, integrated result and independent envelope. The independent checker counts are exactly 13 sectors, 65 prior jobs, 16 rank checks and five producer joins.
- Actual copied job/component logs are hashed and inspected, and full result records have exact required IDs, successful integer exit codes, no resumed/partial prior mode, consistent H0/H1 definitions and exact rank conclusions. The exact unchanged prior/sector marker declarations are pinned in `current_replay_coverage.py`. Thirteen Python/Sage jobs intentionally have no stdout marker and rely on successful fail-closed execution; their declared empty marker lists are preserved rather than inventing new markers.
- Every selected output appears in the retained index; each executed prior source and all five producer identities join to a selected artifact or a specifically named unchanged input copy. Rank evidence digests match the logical inputs.
- The actual isolated driver has a new-output declaration, correct profile/input/log hashes, assertions enabled, a complete replay command and a time interval containing the outer run. Its actual captured output must parse to the **same full outer result JSON**. The bound isolation probes must include successful allowed reads, immutable-input write denial, old-input denials, native-code denial, network TCP/UDP denials and runtime checks.

These are integrity and provenance checks of the observed run, not a new execution or an independent mathematical proof. They cannot independently establish that arbitrary fabricated records describe real events. The root task's observed isolated execution and fresh negative controls supply that execution provenance. Historical Magma computations remain historical.

## Optional actual archive validation

`verify_current_distribution(root, status, archive=path)` additionally hashes the actual final ZIP, requires its exact regular-member set, rejects duplicate/nonregular/symlink entries and rehashes every member against the final manifest. The CLI equivalent is:

```text
python -B scripts/verify_current_distribution.py --root /path/to/control-repository --archive /path/to/final-companion.zip
```

Without `--archive`, the result is `PASS_CURRENT_DISTRIBUTION_RECORD_BINDING`, and `archive_payloads_checked` is false. With the actual archive it is `PASS_CURRENT_DISTRIBUTION_ARCHIVE_AND_RECORD_BINDING`. The default repository check must not claim it rehashed an absent 305MB asset.

The compact tests cover valid record/ZIP bindings, unchanged source-copy references, missing Fano/Hecke/prior/rank/producer rows, changed producer/input/result joins, resumed runs, failed/boolean exit codes, altered marker requirements, absent output freshness, isolation failure, changed/symlink logs, nonrecord additions, wrong URLs, and extra/duplicate/substituted/symlink ZIP members. They run with ordinary Python and `python -O`; all validation uses explicit conditions rather than removable assertions.

The intended completed release binds CLEAN2 as the active isolated run. Failed CLEAN1 records remain below `records/completed-replay/earlier-incomplete-run/`; retaining them neither satisfies nor weakens the current successful-driver checks. `PREPARER_REVIEW.md` and `CLEAN2_SCHEMA_REVIEW.json` distinguish the actual passing preflight from the still-pending complete replay. The parent preparer also rejects overlapping final/output roots before creating its overlay.
