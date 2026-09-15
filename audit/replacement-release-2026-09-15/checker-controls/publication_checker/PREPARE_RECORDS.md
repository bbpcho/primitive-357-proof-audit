# Staging actual publication records

`../prepare_publication_records.py` makes no network requests and modifies neither the input repository overlay nor GitHub. Run it only after final artifact construction, public publication, full unauthenticated downloads and the two old-asset withdrawals have actually completed. It does not manufacture an observation. Its tests use explicitly synthetic files in temporary directories.

```sh
PYTHON -B prepare_publication_records.py \
  --repo-overlay /absolute/path/to/current-control-overlay \
  --download-root /absolute/path/to/public_downloads \
  --companion-archive /absolute/path/to/PRIMITIVE_357_REPLAY_COMPANION_2026-09-15_V2.zip \
  --final-identity /absolute/path/to/FINAL_ARCHIVE_IDENTITY.json \
  --paper-build /absolute/path/to/FINAL_PAPER_BUILD.json \
  --observation /absolute/path/to/FULL_PUBLIC_DOWNLOAD_OBSERVATION.json \
  --withdrawal-record /absolute/path/to/OLD_ASSET_WITHDRAWAL_OBSERVATION.json \
  --output /absolute/path/to/new-publication-records
```

Use physical absolute paths without symlink components. The output's parent must exist; the output itself must be new and outside the input overlay. The overlay contains the final canonical `paper/{manuscript.tex,rank-proof.tex,manuscript.pdf}`, `release/PRIMITIVE_357_ARXIV_SOURCE_2026-09-15_V2.zip`, the current companion binding and every record it authenticates. The default binding is `audit/replacement-release-2026-09-15/BINDING.json`; `--binding-path` may give another safe overlay-relative path. If `audit/status.json` is present, its historical fields are preserved and any affirmative arXiv submission/readiness claim is rejected.

The helper checks all five observed downloads and the saved raw repository/release/tag API responses, including their actual file hashes, sizes, IDs, exact URLs and publication timestamps. It selects exactly the paper PDF, source ZIP and companion for the publication contract. It compares the canonical paper with the final build record and authenticates every source-ZIP member through the publication checker. It invokes the actual companion checker with the local large archive and then the exact current-publication checker on a temporary merged overlay. It creates the requested output atomically only after all checks pass.

Outputs are the three records under `audit/replacement-release-2026-09-15/`, `PROSPECTIVE_CURRENT_PUBLICATION.json` with the exact four-key status object, `PROSPECTIVE_STATUS.json` preserving any supplied historical status, and `PUBLICATION_RECORD_PREPARATION.json`. Apply the validated records and status only in the parent's final publication step. The helper's status keeps `arxiv_submission_made` and readiness false and the requested Dahmen reply as a hold. The paper build and visual review retain their separate scope; this helper does not render a PDF or certify layout.

## Withdrawal observation contract

The actual input uses schema `primitive357_old_asset_withdrawal_observation_v1`, status `PASS_WITHDRAWN_PUBLIC_ENDPOINTS`, the repository URL, replacement tag, timezone-qualified `checked_utc` **at or after the completed public-download check**, `unauthenticated_request: true`, and exactly these two historical asset rows:

- GitHub ID `561595084`: `2026-09-13_p5_literal_c_obstruction_dependency_closure_v1.zip`, 149934212 bytes, SHA-256 `03f3bfe077372275e570dd2541c033ba9a3c0701c80fecadfe1b575f3991d6eb`.
- GitHub ID `561674379`: `2026-09-13_corrected66_predyadic_and_p2_place2_dependency_closure_v1.zip`, 137069860 bytes, SHA-256 `ec90f7ce74fcdebfb3c398a7ac7da8426d590ff9abc0ef115e4824c0e2918248`.

Each row contains `asset_id`, `name`, `bytes`, `sha256`, the exact `api_url` (`https://api.github.com/repos/bbpcho/primitive-357-proof-audit/releases/assets/<id>`), the original `download_url` under tag `audit-2026-09-13.1`, and integer `api_http_status: 404` and `download_http_status: 404`. Both values must be actual unauthenticated GET observations of those endpoints. Preserve raw HTTP outputs and timestamps with the actual event record; a planned deletion, authenticated-only result or missing endpoint response does not satisfy this contract.

`WITHDRAWAL_OBSERVATION_SYNTHETIC_EXAMPLE.json` illustrates the shape only. Its `_example_only: true` field makes it deliberately unacceptable to the helper. It is not evidence of deletion or public access. Create the real record from the actual responses; do not use or relabel the example as observed data.

The normalized withdrawal record's digest and size, the complete download observation's digest and size, and the two final build/identity record digests are bound into `PAPER_REVISION.json`. The raw download/API evidence must remain preserved by the publication audit. This is an offline consistency/authentication check, not a fresh independent network observation.
