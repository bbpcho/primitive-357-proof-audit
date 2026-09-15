# Concrete redistribution repair plan

15 September 2026. **A corrected distribution is feasible without rerunning hours of Magma.** The smallest PVT repair is an externally hydrated input package: distribute acquisition metadata and hashes, acquire the pinned inputs into a user-side cache, and run the same authenticated arithmetic on a private materialized tree. Do not embed the old source-data ZIP in the new companion. Full-paper copies discovered below must be addressed at their actual nested locations, not only at the visible references directory.

This is a technical dependency/packaging plan, not a copyright opinion, blanket clearance or licence selection. No public asset, original archive or source program was changed; no external message was sent. Peter approved MIT for his original code and CC BY 4.0 for his original paper/documentation on 15 September 2026; those grants explicitly exclude third-party material. The factual licence findings from `work/pre_submission_revision_2026_09_15/THIRD_PARTY_REVIEW.md` are carried forward without expanding them into a legal guarantee.

## Baseline and exact removal scope

All paths below marked `R/` are relative to:

`/Users/pcho/Documents/Codex/2026-09-13/ple/work/verified_release_2026_09_14/final_extraction/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1`

The corresponding immutable-source files were also inspected in `work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1`. The current source-data ZIP has SHA `27e3e6eeb50f83ea484e7cd0c94dbd88de0141ab9f47634ed5181e7db0ecba33` and is 588,945,520 bytes. The current 601,649,354-byte companion has SHA `fa0eaae5e193010a0714b1e72fd141f146e3e155148d530706258e3bb42e9a90`. A new companion containing either unchanged ZIP would retain the complained-of distribution.

| Material and exact location | Treatment and input identity |
|---|---|
| `R/evidence/v3/third_party/GFE-5p3/` | Remove the 15 upstream files listed below from the **new distribution**. Retain attribution and a new external-input lock; the two locally added origin/hash records may remain as historical metadata. Prior review found no upstream licence grant in the pinned snapshot. Public access/citation is not recorded permission. |
| `R/evidence/v3/repository/references/Pacetti_Villagra_Torcomian_2512.17845v1.pdf` | External acquisition from `https://arxiv.org/pdf/2512.17845v1`; require 719,399 bytes and SHA `d5983c0949129942c3510d9c3a8de1fbf8998e4b0e5b5d822ddf94a795048004`. Prior review identified the arXiv non-exclusive distribution licence, not a downstream Creative Commons grant. |
| `R/evidence/v3/repository/beal_357_spark_handover_2026-08-20/project/p7_level23_data_mod7.m` | Remove this derived PVT table too; regenerate it privately from the acquired `Outputs/Data.txt`. Require 12,869 bytes and SHA `2833cdd1e290727028496b1339997ac3b401ab1d42dd51a9a970502a69837403`. Calling it independently generated would be inaccurate: it is a reduction of the upstream dataset. |
| `R/evidence/{v3,p5,rank}/repository/results/2026-08-21_descent_galois/inputs/Bruin_Poonen_Stoll_1205.4456v2.pdf` | Three exact copies of the full BPS paper: each 766,724 bytes, SHA `e53e4912cab98eb0e514afa2fbf17b21f446ac032b6b1855e11784bbc478fb47`. Externalize one acquired input, materialized to three logical destinations. Candidate source `https://arxiv.org/pdf/1205.4456v2`; verify exact bytes before acceptance. This pass has not established a redistribution grant for this paper, so externalization avoids relying on one. |
| `R/evidence/v3/repository/results/2026-09-09_putz_hunter_local_algebra_covering_v6/inputs/local_algebra_covering_evidence_v6.tar.gz` member `primary/dahmen-siksek/GFE357.pdf` | A full 235,180-byte Dahmen–Siksek paper is inside this archive, SHA `8b69da80fe79959ed1e05d35b613f7f728f599571b8f84f0a0d29c78e4c205c6`. The archive itself has SHA `803cba99f24401b350fb36b602de5e91e21ac4e3f74804f385fcf10e0dc09eaa`. Use the recorded author URL `https://few.vu.nl/~sdn249/GFE357.pdf`, pinning the bytes; no new licence conclusion is made. The new public TAR must omit this member and its verifier must separately authenticate the acquired PDF. |

The Putz thesis is a distinct case: the prior review found an official **CC BY-ND 4.0** indication, requiring appropriate attribution/source/licence documentation for an unchanged included work. The smallest repair may retain those unchanged copies with that documentation, rather than call them unlicensed. There are **two different wrapped versions**:

- `R/evidence/v3/repository/references/Thesis_CasperPutz.pdf`: 1,946,808 bytes, SHA `5652812adac99a7d5c8b429a83072cbf5b1ccae35552645a837093dd8ade2c7c`.
- `R/evidence/v3/repository/results/2026-09-09_putz_hunter_local_tschirnhaus_support_v5/inputs/local_tschirnhaus_support_evidence_v5.tar.gz`, member `./primary/thesis/Thesis_CasperPutz.pdf`: same size, SHA `9d8a1aa38c3195b15a48e13751d0c5603876ba9a0ec28e35c265a7282f9df627`.

If the policy is to bundle **no full external papers**, externalize both Putz versions too using `https://research.vu.nl/files/367784086/Thesis_CasperPutz.pdf` as a source locator and the separate hashes as acceptance criteria. The prior review did not demonstrate a current download reproducing either dated portal wrapper; do not weaken hashes or promise automatic acquisition of those exact versions. Existing local copies permit an explicitly labelled local-cache test, not proof of public re-acquisition.

I inspected the ZIP/TAR members within R: the two nested full-paper locations above are concrete findings. The remaining named PDFs are project reports/manuscripts. This is not a full licensing review of Putz software or every third-party source fragment in those archives.

## The minimal input architecture

Add these **proposed new files**, not present implementations:

1. `inputs/EXTERNAL_INPUTS_LOCK.json`: exact public URL, full upstream commit, byte count, SHA, logical destinations and consumer IDs for every acquired input. No “latest” URL or mutable default branch.
2. `scripts/acquire_external_inputs.py`: explicit setup step to a cache **outside** the distributed release; supports user-supplied files, validates them before use, refuses path traversal, symlinks, duplicate identities and hash mismatches. Do not run downloaded upstream programs. Acquisition is separate from offline replay.
3. `scripts/materialize_replay_inputs.py`: makes a fresh private working tree, copies the distributed subset, inserts authenticated external bytes at their legacy destinations, and regenerates the reduced table. Record every input hash and destination in `EXTERNAL_INPUTS_USED.json`. Recheck after replay.
4. `inputs/DISTRIBUTION_OMISSIONS.json`: identifies each omitted original payload, the original hash, its replacement source, and any deliberately repacked container. Keep the old manifests as historical identities where possible; the new distribution receives its own exact-set manifest and release identity.

For **PVT plus the flat BPS omissions alone**, private hydration can restore the old logical files byte for byte. The original V3, p5, rank and prior inventory verifiers can therefore remain unchanged; execute them from the hydrated tree. This avoids broad changes to mathematical source or “missing-file exemptions.” The Hecke foundations runner must likewise run from that tree, since it requires its script to be contained in its `--release-root` and validates the exact 14-file closure.

The nested Dahmen–Siksek removal needs one additional explicit contract change. The v6 verifier currently authenticates the whole compressed TAR and every member. Its PDF is never consumed by the local algebra arithmetic: `read_evidence()` checks it, while the arithmetic reads the GFE/local-algebra source members. Create a new TAR retaining every other member byte-identically, update the whole-TAR identity, and move only the PDF row to a separately authenticated external input. Do **not** silently skip the original checksum or pretend the repacked archive is unchanged. A narrow experiment found that zlib 1.2.12 and the available `/usr/bin/gzip` do not recreate the original compressed bytes at any tested level, so exact gzip reproduction is not an established shortcut.

## Exact source edits and authentication propagation

The following are concrete consumers, not inferred collection rules:

| File | Required change |
|---|---|
| `R/scripts/verify_release.py` | Add external-cache/materialized-input arguments and bind the input lock and actual hashes into the final result. Check public distribution integrity separately from hydrated logical integrity. Start the same three components from the hydrated tree; preserve cancellation, 65 prior jobs, 13 sector records and rank joins. |
| `R/scripts/replay_sectors.py` | Materialize before cloning/running V3; its integrity job must use the complete authenticated private V3 tree instead of the incomplete distributed directory. Keep all 13 jobs. Keep the full PVT hash, theorem text checks and explicit Poppler adapter. |
| `R/evidence/v3/scripts/verify_dependency_closed_release_v3.py:157–170` and `verify_hilbert_hecke_filter_coverage.py:133–167,223–234` | No mathematical change is needed under private hydration: retain the pinned complete snapshot check, 6,253-polynomial comparison and source-loop checks. If explicit direct cache paths are chosen instead, replace only their `UPSTREAM` resolver with the common authenticated lock resolver. |
| `R/evidence/v3/scripts/portable_python.py:20–24` | With full hydration its legacy reference mappings remain valid. With direct cache paths, map the two PDF literals through the authenticated resolver, not a guessed download location. |
| `R/evidence/v3/repository/beal_357_spark_handover_2026-08-20/project/verify_p7_data_mod7.py` | Existing code already constructs canonical `lines`; add a small separate writer or explicit output mode to save those generated bytes only in private replay output. Retain the independent parse comparison and exact expected hash. |
| `R/audit/work/hecke_foundations/run_hecke_foundations.py` and `evidence_dependencies.json` | Hydration preserves the existing 14 inputs unchanged. Under direct cache routing, update only the derived-table resolver and its explicit source record; preserve the 1,264 ordinary/128 boundary checks. |
| `R/audit/work/integration_prior/replay_prior_evidence.py:43–57` and `REQUIRED_PRIOR_EVIDENCE.json` | Preparation requires complete v3/p5 repository inventories, including BPS. Hydrate these before preparation; do not remove those required rows to make a test pass. |
| `R/evidence/v3/repository/results/2026-09-09_putz_hunter_local_algebra_covering_v6/scripts/verify_putz_hunter_local_algebra_covering_v6.py:36–105` | For the nested DS removal, authenticate the new TAR/member set and the external PDF separately; keep every classification function and arithmetic input unchanged. |
| Optional Putz removal: `.../2026-09-09_putz_hunter_local_tschirnhaus_support_v5/scripts/verify_putz_hunter_local_tschirnhaus_support_v5.py:32–54` | Apply the same split between retained members and exact externally supplied thesis bytes. Its arithmetic is separate from the PDF identity. The external interface `.../2026-09-10_pvt_putz_interface_audit_v2/scripts/verify_pvt_putz_interface_v2.py:151–174` must keep both complete PDF and page checks. |

For the DS container change, regenerate its package manifest `results/2026-09-09_putz_hunter_local_algebra_covering_v6/manifests/PUTZ_HUNTER_LOCAL_ALGEBRA_COVERING_V6_SHA256SUMS.txt`. Its direct consumers include `results/2026-09-08_signed_ds_branch_local_pattern_audit_v1/scripts/verify_signed_ds_branch_local_pattern_audit_v1.py`, its ledger/certificate, `results/2026-09-08_putz_degree7_f42_projector_bridge_audit_v1/inputs/putz_degree7_f42_projector_ledger_v1.json`, and `results/2026-09-10_irreducible_degree7_sector_closure_v1/inputs/irreducible_degree7_sector_dependency_ledger_v1.json`. Update their authenticated dependency identities and propagate through the existing V3 base/dependency/sector indexes and root manifest. Preserve archived old records as old evidence; do not relabel their PASS as a newly executed revised package. This is a finite provenance update, but not just one filename deletion.

**Prevent accidental redistribution during record collection.** `work/verified_release_2026_09_14/integration_rank/select_final_artifacts.py:98–115` currently retains a hydrated file absent from the candidate as a “new artifact inside known copy.” Thus it would re-bundle the removed snapshot/PDF/table. Add a separate exact exclusion class for authenticated external acquisitions and their canonical reduced table, keyed by path + size + SHA and recorded in the selection. Do not exclude arbitrary new files or mathematical binaries. Synchronize the trusted selector with `work/pre_submission_revision_2026_09_15/repository/scripts/select_final_artifacts.py`, `promote_release.py`, and their controls. Extend `append_verification_records.py` and promotion to bind the external-input manifest while preserving all retained generated mathematics and logs. The outer source-data and companion archives must be rebuilt from the sanitized selection, not include the unchanged earlier ZIP.

## Feasible verification in this turn

A **new sanitized distribution with honest transport/provenance verification** is feasible now. A new claim of a full fresh integrated arithmetic run is a separate, longer task; do not conflate the two.

- Already performed here: the inspected `verify_p7_data_mod7.py` was run read-only on the frozen upstream Data.txt. It freshly parsed all 6,253 polynomials at 37 primes and rebuilt exactly 12,869 bytes with SHA `2833cdd1e290727028496b1339997ac3b401ab1d42dd51a9a970502a69837403`. No full upstream Magma/GP generation was run.
- In a fresh extraction, test missing input, changed input, wrong commit, duplicate/path-traversal input, forbidden bundled payload, and altered externally hydrated bytes. The acquisition test should use a fresh public fetch where available; a local-file fallback must be labelled.
- With network disabled, authenticate the complete hydrated logical trees, run the PVT data/filter and PDF-interface checks, run the independent Hecke foundations, and run the unchanged v6 local-algebra calculation after its container-contract change. Confirm the branch manifest/graph joins. The full sector suite is available if time allows; it needs Python/Sage/FLINT/C++/Poppler, not a fresh Magma session.
- Existing runtimes verified present: `work/v3_audit/runtime/sage-env/bin/python` (Sage 10.9), `work/v3_audit/runtime/pari-2.15.4/gp` (PARI 2.15.4), bundled Python at `/Users/pcho/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`, Poppler at `/opt/homebrew/bin/pdftotext`, and the Xcode Clang executable. Existing `final_replay2/RUNTIME_VERSIONS.json` records SymPy 1.14, mpmath 1.3 and python-flint 0.9. Use fresh runtime preflight, not those records alone.
- The already completed Magma component has unchanged source/data/log identities and can be carried as **previously executed evidence**. No new Magma result is required merely because its surrounding archive or paper distribution changes. If any mathematical input to those jobs changes, this carry-forward argument no longer applies.
- Keep the older full-run records explicitly identified as belonging to the old logical input manifest; issue a new `PASS_SANITIZED_DISTRIBUTION_TRANSPORT`/targeted replay record. Only advertise a new complete fresh run if one actually finishes.

All cache and materialization paths must be excluded from publication. Extend the existing network-denying isolation profile to allow only the new distribution, the declared cache/materialized output and installed runtimes; keep the previous proof trees denied. Before sealing, scan the outer ZIP and all nested archives for the exact forbidden file hashes and known full-paper members. Assert that no original companion/source-data ZIP is embedded. This check must also cover the added verification records.

## Pinned PVT acquisition list

Repository: `https://github.com/lucasvillagra/GFE-5p3`; commit `e88f914c577ab6cf9a45e5cdd82c1993477fb423`.
For each row the source is `https://raw.githubusercontent.com/lucasvillagra/GFE-5p3/e88f914c577ab6cf9a45e5cdd82c1993477fb423/<path>`. The byte hashes below were freshly checked locally, not freshly fetched in this pass.

| Path | Bytes | SHA-256 |
|---|---:|---|
| `Codes/CharPoly.m` | 1774 | `0a0e7a1aa51a8993eddd82bb7dbe858006bffc58577add1afc11841602662283` |
| `Codes/CurveConstruction.m` | 585 | `4cbb2dba3100375a9234ee640f8e520ab98192275358544a4075c29258cfccec` |
| `Codes/GPcode.gp` | 5497 | `a6617041cd22bda5edf65beccfa59022fc5fb7ce2e05aa465f5e67406b438232` |
| `Codes/IgusaIn.m` | 2345 | `642e2f5e362e922c59c0b8129abaad0294f39189c982c53de030514ada3eaba9` |
| `Codes/IrredTest.m` | 1088 | `1fd61e5307b008936cdc0a6094912d24353533bad4bb84b5962d2850e821a5e9` |
| `Codes/MagmaCode.m` | 9206 | `618bfed88d6809edb483ac78356305d226a52d79f24061626f55b8997d48ffe0` |
| `Outputs/BoundIrreducibility.txt` | 310 | `192a54f878e11a8ff38617f69553cd559ff8db0d28f1247f69d30afb99c4e700` |
| `Outputs/CharPoly.txt` | 718 | `33fa4cecdafe160187af8a4133c34533236b9aa3c57ffc67e295183a6ed6b02e` |
| `Outputs/CurveConstruction.txt` | 323 | `4b7a562233c2b2e3611101dc84495f0cc7cebe3ef8f5cca2b53dc3dfb22607d3` |
| `Outputs/Data.txt` | 102250 | `cc73ca915d3b25fe4def2b323b93bdc0fcdc46bbd560f16193af4dbdfae08ba5` |
| `Outputs/DataTimes.txt` | 2595 | `f646e077d5e7c9a5e71f07e2ae95ec8579e1b0cfbb32c9a0b02e8bd95c4cf4d0` |
| `Outputs/IgusaIn.txt` | 2124 | `cb5c68e9b48613d86e1d18bd8af44d822a3651afa5e4609a524994a314a36e63` |
| `Outputs/Table.txt` | 358 | `812a9e1e8f289532728d055c76c898b549ff0f2bf8bb3981f45dfc893c4f1cda` |
| `Outputs/TheoremA.txt` | 9609 | `6b05ad7356248dd32e1d4661120893bada83685b5c7f7697fe2b44482b187489` |
| `README.md` | 1283 | `9648cfced9f792e3f1cacb0618d74515c04b575c9af0d0676ec5ec714697f240` |
