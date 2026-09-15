# Independent bounded publication review: actionable items

`download_published_release.py` checks success statuses in `FINAL_ARCHIVE_IDENTITY.json` and `FINAL_PAPER_BUILD.json`, but does not join the complete `paper["companion"]` identity to the current final identity. The paper builder records that identity and embeds its digest. If the companion is resealed after the paper build, each individual download can match its respective record while the published PDF still identifies an older companion. Require `paper["companion"] == final` before creating the download directory. This is a missing preventive check, not an observation that the actual current PDF is stale. No code was edited by this review.

Integration detail for the forthcoming record writer: the actual downloader emits `primitive357_full_public_download_observation_v1` with five download roles, whereas the offline publication checker intentionally accepts `primitive357_current_public_access_v1` with exactly three roles (`paper_pdf`, `source_zip`, `companion`). Construct that compact record from the actual observations and retain the raw five-download record separately; passing it unchanged will fail the current checker. This is not a defect in either schema.

Inspected source identities (SHA-256):

- `publication_checker/verify_current_publication.py`: `590e35b0d1296cfcab6568ce0292aede0abf9d346c8079989071b7ebe911dcab`
- `publication_checker/CONTRACT.md`: `4dd127e56081885a1bc8ce35dc8279f0daf17b5cac6d56c125cedcba2b18fd51`
- `download_published_release.py`: `da4089d0c895fd2b1babc023595d5bcb2bfc61d003f09835964c58aba18d39b8`
- `prepare_final_paper.py`: `a40af5291ac953801651cc270742e53a15afad17154787d40de8479e806cf375`

Resolution: the parent added the exact `paper["companion"] == final` check before output creation or network access. The final reviewed downloader SHA-256 is `da4089d0c895fd2b1babc023595d5bcb2bfc61d003f09835964c58aba18d39b8`. The parent confirmed the five-role original observation will be retained separately from the three-role compact record. No remaining actionable issue from this bounded review; no full replay or public download success is implied.
