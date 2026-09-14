# Final promotion utility

`scripts/promote_release.py` is intended for the parent release assembly after the real clean replay has succeeded and the new archive has been sealed. It does not run arithmetic, manufacture a PASS result, seal or alter an archive, commit, upload, or publish. By default it validates a temporary proposal and leaves the selected control repository unchanged. Only `--apply` writes the validated records.

The actual input directory must contain:

- `REPLAY_RESULT.json` and its three hash-bound `logs/` files;
- `prior/PRIOR_REPLAY_RESULT.json`, with a fresh, complete required-job set;
- `sectors/SECTOR_REPLAY_RESULT.json`, including the independent Hecke foundations and full Fano reconstruction;
- `rank_local/rank_local_results.json`, with the actual B-plus-literal-c conclusion.

The utility also requires the actual candidate archive, top-level driver log and host record. It independently recomputes the complete retained-artifact selection using its synchronized local selector, then checks that every selected result, log, runtime record and mathematical binary in the final archive equals the actual fresh output. Omitting or substituting the Fano log or runtime record fails this join. The tested manifest, proof-input index, driver, host, candidate identity and archived selector are bound separately.

The utility reads the required prior-job contract from the sealed archive. It checks every ZIP member against the supplied final manifest, checks the embedded manifest itself, and requires every tested input to retain its path, size and SHA-256. The control repository's manuscript source, rank appendix and PDF must match the tested archive. The supplied separate PDF must be byte-identical to that manuscript PDF.

## Review first

```bash
python3 -B scripts/promote_release.py \
  --control-root /path/to/control-repository \
  --candidate-archive /path/to/tested-candidate.zip \
  --driver-log /path/to/actual-integrated-driver.log \
  --host-record /path/to/actual-HOST_ENVIRONMENT.json \
  --final-replay /path/to/actual-final-replay-output \
  --tested-manifest /path/to/tested-RELEASE_MANIFEST.json \
  --final-archive /path/to/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip \
  --final-manifest /path/to/final-RELEASE_MANIFEST.json \
  --paper-pdf /path/to/PRIMITIVE_357_VERIFIED_MANUSCRIPT_2026-09-14.pdf \
  --workspace-root /path/containing/the/two/new/assets \
  --review-output /path/outside/control/promotion-review.json
```

The two actual asset files must lie below the chosen workspace root; the asset index records their relative source paths. The PDF asset keeps the supplied PDF's basename. The primary ZIP basename is fixed to the new release identity. The readable JSON review lists exact file changes, asset hashes and successful validations.

After reviewing that actual result, repeat the command with `--apply`. Omit `--review-output` or choose a new output filename, because an existing review record is not overwritten. Applying regenerates the control snapshot manifest, so newly copied control utilities can be included in that snapshot. All seven control/checker/selector programs must match the copies beside the promotion utility; the utility rejects stale checkers.

## Changes made only on apply

The utility copies the actual integrated result, three component logs, tested and final manifests into `audit/verified-2026-09-14/`. It derives the complete `PROOF_INPUTS_SHA256.json` and actual `REPLAY_BINDING.json` from those inputs. It appends two assets: the primary ZIP and the separate manuscript PDF. All seven historical asset records are preserved exactly.

It updates the checksum list and the two release gates, changes the status to verified, clears the blocking description, and regenerates the exact tracked snapshot. Existing different records under the same sealed audit identity are rejected. The completed rank workplan and explicitly imported published/Magma premise state remain unchanged. Repository verification runs in normal, `-O` and `-OO` modes on the proposal; both new assets are checked using their actual workspace files. A concurrent change to the control file set aborts application.

After applying, the parent should independently run:

```bash
python3 -B -O scripts/verify_repository.py
python3 -B scripts/verify_assets.py --workspace-root /path/containing/assets \
  --asset-id PRIMITIVE_357_VERIFIED_RELEASE_2026_09_14_V1 \
  --asset-id PRIMITIVE_357_VERIFIED_MANUSCRIPT_2026_09_14
```

The parent remains responsible for reviewing the Git diff and performing the authorized commit/release operations. No real promotion has been performed while developing this utility.

## Tests

`python3 -B scripts/test_promotion.py --output-dir /path/to/new-test-results` uses explicitly synthetic temporary fixtures. It tests dry review, application to a synthetic control repository, bad/stale/partial replay rejection, missing Hecke/Fano coverage, changed PDF/source, extra ZIP members, omitted or substituted archived records, falsified selection, unknown native outputs/symlinks, changed candidate identity and stale checkers. All cases run normally and under both Python optimization modes. No synthetic record is copied into the actual control repository or release inputs. The recorded results are under `audit/verified-2026-09-14/promotion_controls/` and are labelled as checker tests, not mathematical evidence.
