# Third-party provenance and redistribution review

15 September 2026. This is a factual inventory and a proposed reproducibility-preserving response. It does not choose Peter Chocian's licence, determine infringement, or provide a legal guarantee. No third party was contacted; no published asset or repository was changed.

## Findings

The companion contains an exact copy of the public [lucasvillagra/GFE-5p3 repository](https://github.com/lucasvillagra/GFE-5p3), pinned to commit [`e88f914c577ab6cf9a45e5cdd82c1993477fb423`](https://github.com/lucasvillagra/GFE-5p3/tree/e88f914c577ab6cf9a45e5cdd82c1993477fb423). The copied material consists of **15 upstream files, 140,065 bytes**, plus two locally added provenance files. It also contains a separate **719,399-byte copy of the PVT paper**, arXiv:2512.17845v1.

No upstream licence file or grant was found in the copied snapshot or its code/README. The current public repository page and the pinned root, Codes and Outputs listings were checked on this date; they display the same three root entries and no licence declaration. This records what was found, not a claim that no separate permission could exist. The unauthenticated GitHub licence API could not be opened by the web tool; the conclusion relies on the visible upstream listings, README and supplied complete snapshot.

The local `UPSTREAM_ORIGIN.json` itself records that no licence file was present. Its explanation that the files are a cited computational snapshot acknowledges provenance; it does **not** document permission from the upstream authors. `Codes/MagmaCode.m`, lines 3–4, credits Ariel Pacetti and Lucas Villagra Torcomian. `Outputs/DataTimes.txt`, lines 7–10, includes PARI/GP's copyright/GPL banner; that is a notice about PARI/GP, not an identified licence for the authors' repository.

GitHub's official guidance distinguishes public access and GitHub viewing/forking rights from a general software licence. It says the absence of a licence leaves default copyright rules in place. Attribution and a public repository therefore should not be treated as a documented general redistribution permission. [GitHub: Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).

The PVT paper's current [arXiv record](https://arxiv.org/abs/2512.17845v1) links to the [arXiv non-exclusive distribution licence](https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html). That text grants distribution rights to **arXiv.org**; it is not a displayed Creative Commons grant to downstream republishers. The PDF and repository snapshot should therefore be treated as **two distinct permission questions**. Citing their mathematical results is also distinct from redistributing their files.

Peter's repository has no project-wide licence file in the inspected checkout. Its [NOTICE.md](/Users/pcho/Documents/Codex/2026-09-13/ple/work/publication_2026_09_15/repository/NOTICE.md:8) explicitly says no project-wide licence has been selected. Peter can decide the terms for material he is entitled to license; this cannot supply a missing licence for another author's material. No licence has been selected by this review.

## Exact local scope

Let `R` denote:

`work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1`

The snapshot is `R/evidence/v3/third_party/GFE-5p3/`. Its [origin record](/Users/pcho/Documents/Codex/2026-09-13/ple/work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1/evidence/v3/third_party/GFE-5p3/UPSTREAM_ORIGIN.json) identifies the repository, full commit and fetch date. Its [SHA-256 manifest](/Users/pcho/Documents/Codex/2026-09-13/ple/work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1/evidence/v3/third_party/GFE-5p3/UPSTREAM_SHA256SUMS.txt) pins every copied file. I recomputed their sizes and hashes from the supplied files.

| Upstream file | Bytes |
|---|---:|
| `Codes/CharPoly.m` | 1,774 |
| `Codes/CurveConstruction.m` | 585 |
| `Codes/GPcode.gp` | 5,497 |
| `Codes/IgusaIn.m` | 2,345 |
| `Codes/IrredTest.m` | 1,088 |
| `Codes/MagmaCode.m` | 9,206 |
| `Outputs/BoundIrreducibility.txt` | 310 |
| `Outputs/CharPoly.txt` | 718 |
| `Outputs/CurveConstruction.txt` | 323 |
| `Outputs/Data.txt` | 102,250 |
| `Outputs/DataTimes.txt` | 2,595 |
| `Outputs/IgusaIn.txt` | 2,124 |
| `Outputs/Table.txt` | 358 |
| `Outputs/TheoremA.txt` | 9,609 |
| `README.md` | 1,283 |

The two additional files are the locally supplied `UPSTREAM_ORIGIN.json` (399 bytes) and `UPSTREAM_SHA256SUMS.txt` (1,379 bytes). These are not upstream licence files.

The PDF is `R/evidence/v3/repository/references/Pacetti_Villagra_Torcomian_2512.17845v1.pdf`, SHA-256 `d5983c0949129942c3510d9c3a8de1fbf8998e4b0e5b5d822ddf94a795048004`. The snapshot and PDF are carried inside `PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip`, which is embedded unchanged in `PRIMITIVE_357_FIRST_SUBMISSION_COMPANION_V1.zip`. Merely removing a top-level third-party folder from a new companion would not remove copies inside the embedded component.

The current control Git checkout contains the release tools and provenance indexes but no byte-identical copy of these 15 upstream files or the PDF. The release assets are the principal full-copy distribution identified here. There is also a derived trace-data file in the evidence repository, discussed below; changing its filename does not make it independently generated.

The same references directory additionally contains `Thesis_CasperPutz.pdf`; the narrow addendum below covers that named PDF. This report does not exhaustively clear other third-party items and embedded historical packets. A future distribution inventory should cover those separately instead of treating this review as a blanket rights clearance.

## What the replay actually uses

Paths in this table are relative to `R`.

| Consumer | Actual reliance | Consequence of simply removing the copy |
|---|---|---|
| `evidence/v3/scripts/verify_dependency_closed_release_v3.py:157–170` | Checks the pinned commit and exact complete file set of the 17-file snapshot directory. | The integrity/interface stage fails, even for snapshot files not otherwise used arithmetically. |
| `evidence/v3/scripts/verify_hilbert_hecke_filter_coverage.py:133–151` | Rechecks every snapshot hash and exact file set. | The filter replay fails. |
| Same script, lines 154–167 | Passes upstream `Outputs/Data.txt` to `verify_p7_data_mod7.py`, comparing 6,253 polynomials at 37 primes with `p7_level23_data_mod7.m`. | The provenance and reduction comparison cannot run. |
| Same script, lines 223–234 | Reads `Codes/GPcode.gp` and checks the ordinary/degenerate generator-loop expressions. | The existing source-loop check cannot run. This step reads the GP source; it does not execute all upstream GP/Magma generators. |
| Same script, lines 170–219 and 236–279 | Uses the reduced trace data and archived consumer arrays to reconstruct the 18 filters, transport relative-degree-two traces, adjoin level-lowering values, and expose the old 131 defect. | Keeping only saved PASS records would lose the actual calculation. |
| `audit/work/hecke_foundations/scripts/independent_ordinary_counts.c` and `independent_ordinary.py` | Freshly count all 1,264 ordinary parameters at the 18 required primes and test containment in the consumer filters. | These checks do not need the copied `GPcode.gp` or full `Data.txt`; they are an independent route for these ordinary inputs. |
| `audit/work/hecke_foundations/scripts/independent_boundary_jacobi.py` | Reconstructs all 128 boundary character values at 16 split primes by exact finite-field Jacobi sums, then compares them with groups parsed from `p7_level23_data_mod7.m`. | The arithmetic is independent, but the current comparator still consumes that derived table. It would need a new generated-output contract to remove the table. |
| `evidence/v3/repository/results/2026-09-10_pvt_putz_interface_audit_v2/scripts/verify_pvt_putz_interface_v2.py:167–174` | Checks the full PVT PDF hash and the page-32 extraction/hash/content markers for Theorem 7.8. | A citation alone cannot satisfy the current executable contract. An externally acquired exact PDF could. |
| `scripts/replay_sectors.py:51–61,104–116` | Retains the exact PDF check while adapting the specifically audited Poppler extraction; runs the snapshot/filter/interface and independent-foundation jobs. | Any dependency relocation must be integrated here and into the manifests, not concealed by skipping jobs. |

The reduced table is `evidence/v3/repository/beal_357_spark_handover_2026-08-20/project/p7_level23_data_mod7.m` (12,869 bytes; SHA-256 `2833cdd1e290727028496b1339997ac3b401ab1d42dd51a9a970502a69837403`). The current checks independently reconstruct the **required** ordinary and boundary values; they do not independently regenerate all 6,253 upstream polynomials. The scope distinction must survive any revision.

The other upstream scripts and output transcripts remain part of the exact snapshot-authentication contract. Their inclusion is not evidence that the final pipeline freshly executes each one. The seven separate Magma jobs in the companion concern the reducible-sector inputs; they are not fresh executions of all six PVT code files. `Outputs/DataTimes.txt` also supplies historical software/provenance information to the release builder.

## Concrete options for the next version

**A. Seek permission for the exact copies.** Ask the authors whether the 15-file snapshot and, separately, the paper PDF may remain in public research companion archives; request their preferred citation and any notice/conditions. Preserve the original attribution and record any written permission without implying endorsement. The unsent draft below gives the exact scope. This is the smallest change to the present replay design if permission is granted.

**B. Distribute acquisition instructions and hashes instead of those copies.** A new package can retain the repository URL, full commit and 15 per-file hashes, with a setup step that acquires the pinned public files into a verifier-owned external directory. Individual source URLs have the form `https://raw.githubusercontent.com/lucasvillagra/GFE-5p3/e88f914c577ab6cf9a45e5cdd82c1993477fb423/<path>`. Acquire the PVT PDF separately from its versioned arXiv source and require the recorded full-file hash. No credential is needed for these public sources.

The replay must gain explicit external-input paths, authenticate the same bytes before use, and reject missing or changed acquisitions. The current all-files-exact-set checks, root mappings, dependency indexes and release hashes need a reviewed replacement. Once acquisition is complete, the arithmetic can run without network access. This removes bundled full copies from the **new** package while retaining the computational contract; it does not prove the legal permissibility of every possible use. The new archive must not embed the unchanged old ZIP containing the files it is intended to omit.

**C. Reduce the dependency by generating the needed data independently.** The existing ordinary point counter and boundary Jacobi-sum checker make this technically plausible. A revised generator could emit every needed trace polynomial/value directly, construct the 18 conservative filters, preserve the inert-prime argument and degree-two transport, retain the corrected 131 filter, and reproduce the ambient/terminal exclusions. The new outputs should have their own schema, input ledger and exact coverage checks. Merely retaining the current derived table or relabelling it as regenerated is insufficient.

This alternative is **not implemented or newly replayed by this inventory**. It would replace the full upstream-data comparison with a narrower, independently generated sufficient dataset, so the manuscript's 6,253/37-prime provenance sentence and the relevant verifier claims must be revised honestly. The PVT mathematical theorems still require citation and applicability review, even if their PDF is acquired externally rather than bundled. Run the changed Hecke and PVT interface checks and the complete revised release contract, with missing-input and altered-data controls, before claiming the new package is replayable.

Peter's own code/data/paper licensing decision is separate from A–C. A project licence should clearly identify its scope and third-party exclusions; this report selects none. No existing published asset was deleted, replaced or re-licensed. Any action concerning already published copies remains a separate decision.

## UNSENT courtesy-email draft

**Subject:** Permission and citation for the GFE-5p3 snapshot in a research companion

Dear Ariel Pacetti and Lucas Villagra Torcomian,

I am preparing my first arXiv submission on the primitive equation \(x^3+y^5=z^7\), titled “The Primitive Generalized Fermat Equation x³ + y⁵ = z⁷: A computer-assisted proof.” It cites your paper *On the generalized Fermat equation of signature (5,p,3)* and uses its modularity, conductor and level-lowering results.

The current computational companion includes an unchanged copy of your GFE-5p3 repository at commit `e88f914c577ab6cf9a45e5cdd82c1993477fb423`: the six files in `Codes/`, the eight files in `Outputs/`, and `README.md` (15 files, 140,065 bytes). Their individual SHA-256 values are recorded. It also includes a separate copy of arXiv:2512.17845v1 for an exact theorem-source check.

I did not find a repository licence. Would you permit us to retain and redistribute that exact code/output snapshot in the public GitHub research companion, with attribution and any notices you specify? Separately, may the paper PDF be included, or would you prefer a versioned link and local acquisition step instead? The repository is https://github.com/bbpcho/primitive-357-proof-audit.

Please also let me know your preferred citation for the paper and computational repository. I can provide the file manifest and explain precisely which computations use the snapshot. If you prefer that we distribute acquisition instructions rather than copies, I will prepare that change while preserving the verification requirements.

Thank you for making your work available.

Peter Chocian  
Independent researcher

*Draft only. No email address was inferred and this message has not been sent.*

## Narrow addendum: Putz thesis PDF

This addendum concerns only `R/evidence/v3/repository/references/Thesis_CasperPutz.pdf`, not Putz's software or other archived material. I checked its front matter, recomputed its full-file hash, read the consuming verifier, and consulted the official publication record on 15 September 2026. No mathematical calculation was rerun.

**Bibliographic identity.** Piet Hein Casper Putz, *Enumeration of local and global étale algebras applied to generalized Fermat equations*, PhD thesis, Vrije Universiteit Amsterdam, 2024; award/publication date 14 November 2024; DOI `10.5463/thesis.832`. The [official VU record](https://research.vu.nl/en/publications/enumeration-of-local-and-global-%C3%A9tale-algebras-applied-to-general/) identifies the final published thesis and links to [the named PDF](https://research.vu.nl/files/367784086/Thesis_CasperPutz.pdf). The portal lists 222 pages; the bundled file has 223 PDF pages including its portal cover sheet.

**Displayed terms require both sources to be read.** The bundled cover carries generic VU portal terms permitting a research/private-study copy, restricting further distribution and permitting circulation of the publication URL. However, the current official publication record explicitly associates the thesis DOI with **CC BY-ND 4.0**, linking to [the Creative Commons legal code](https://creativecommons.org/licenses/by-nd/4.0/legalcode). The cover alone is therefore insufficient to conclude that the thesis lacks a redistribution licence. CC BY-ND 4.0 permits sharing licensed unadapted material subject to its attribution and other conditions; it does not permit sharing adapted material under that licence. Sections 2–3 require, among other things, appropriate retained attribution/notices, a source link and a licence indication/link, and do not grant endorsement.

The appropriate inventory status is **“a public licence is displayed; document its applicability and attribution for the exact bundled artifact.”** It is not the PVT repository's “no licence found” status. The generic cover and the specific record should be preserved as distinct evidence. If the exact wrapped file's coverage remains uncertain, clarification from the author or repository is preferable to ignoring either notice. This is not a legal guarantee that all conditions have already been met.

**Exact replay identity.** The local file is **1,946,808 bytes**, SHA-256 `5652812adac99a7d5c8b429a83072cbf5b1ccae35552645a837093dd8ade2c7c`; this agrees with `results/2026-09-10_pvt_putz_interface_audit_v2/inputs/pvt_putz_interface_ledger_v2.json`. The consuming script `verify_pvt_putz_interface_v2.py`, lines 151–165, requires this whole-file hash, extracts PDF page 125 (printed page 118), checks the text-extraction hash `928528c5c7aa3c742a83d1a1f50d2ab4de236325003fc9ccc7aae103f65a74dd`, and checks Theorem 3.50's hypothesis and seven-field conclusion markers. `evidence/v3/scripts/portable_python.py` maps the original download path to this bundled reference. The outer manifests and the Putz–PVT sector job also depend on its identity.

**External acquisition is technically possible, with an exact-byte qualification.** A revised verifier could accept an explicit user-supplied `--putz-pdf` path, authenticate the same source and page checks, and leave the PDF outside the distributed package. The DOI and file-ID URL identify the work and hosted document, but are not a demonstrated immutable byte version: the bundled portal cover contains the download date 8 September 2026. A fresh portal download may have a different wrapper. The web tool received HTTP 403 when fetching the current full PDF, so a byte-identical new acquisition was **not** demonstrated here.

Consequently the current strict hash must not silently be relaxed. Either obtain the exact accepted version, or explicitly review a newly acquired version, document the bibliographic/body correspondence and page mapping, and issue a new input manifest and tested verifier contract. The theorem remains an imported result; source authentication is not a new execution of the thesis's entire Hunter enumeration. With the displayed CC BY-ND licence properly documented, retaining an unchanged appropriately attributed thesis may also be an available route, distinct from choosing external acquisition.

No thesis file, published asset or verifier was modified. The courtesy draft above remains unsent and now uses the current full paper title.
