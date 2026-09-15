# Licence scope and MSC2020 review

Reviewed 15 September 2026. Read-only review of the notices in `work/pre_submission_revision_2026_09_15/repository`; no manuscript, licence or release files were changed.

**Outcome:** the new notices consistently assign MIT to the author's original program code and CC BY 4.0 to his original manuscript and documentation. I found no grant purporting to relicense the Pacetti–Villagra Torcomian materials or other third-party components. The source and printed manuscript notices clearly identify the paper's licence. This is a consistency and scope review, not a determination that every component is author-owned or that the frozen companion may be redistributed.

## Scope findings

1. `LICENSE.md` expressly limits the grant to original contributions and to rights Peter Chocian holds. Its table identifies both manuscript source files and their compiled PDF. It preserves component-specific licences and excludes third-party papers, theses, software, copied or adapted upstream code, and other material outside the author's rights. This implements the distinction in the [CC BY 4.0 legal code](https://creativecommons.org/licenses/by/4.0/legalcode.en), especially its definition of Licensed Rights and its guidance to identify excluded material.

2. `LICENSES/MIT.txt` contains the standard MIT permission, notice-retention and warranty clauses; its wording agrees with the [SPDX MIT text](https://spdx.org/licenses/MIT.html). `LICENSES/CC-BY-4.0.txt` contains the full eight-section CC BY 4.0 legal text and its accompanying explanatory material. The root scope table determines which original contributions receive each licence; the presence of these standard texts does not apply either licence to every bundled file. The commercial-use and modification summary in `LICENSE.md` is consistent with the linked licences.

3. `NOTICE.md` explicitly keeps the PVT paper and the `GFE-5p3` snapshot at commit `e88f914c577ab6cf9a45e5cdd82c1993477fb423` outside these grants. It preserves the unresolved redistribution issue and explains that historical checksums are not permission. It does not incorrectly treat the author's choice as resolving that issue. See the separate, bounded inventories in `work/pre_submission_revision_2026_09_15/THIRD_PARTY_REVIEW.md` and this directory's `REDISTRIBUTION_REPAIR_PLAN.md` for the practical replacement work.

4. `paper/manuscript.tex:1–3` and `paper/rank-proof.tex:1–3` identify Peter Chocian, CC BY 4.0 and its canonical URL, and point to the third-party exclusion. The printed licence paragraph at `paper/manuscript.tex:1324–1332` states the same division and explicitly says these grants do not authorize redistribution of third-party material in the frozen archives. That last sentence limits **these grants**; it does not purport to cancel permissions independently supplied by a third-party rights holder.

5. The source notice is intelligible even outside the repository: both TeX files carry the licence URL, and the compiled paper includes the full licence name and exclusion. The final source-upload archive should retain these reviewed files and notices. This review did not inspect a newly rebuilt upload ZIP or make an arXiv licence selection; those final packaging/interface checks remain separate. The intended selection is CC BY 4.0 for the original manuscript, consistently with its notice.

No further wording change is required by this review. The absence of accidental relicensing does not resolve the previously identified redistribution permissions for the frozen third-party copies, and the new notices correctly retain that boundary.

## MSC2020 verification

The joint Mathematical Reviews/zbMATH [official MSC2020 list](https://msc2020.org/MSC_2020.pdf) confirms all four codes. The descriptions below are brief subject summaries, not replacements for the official classification labels.

| Code | Subject | Official PDF page | Proposed role |
| --- | --- | --- | --- |
| 11D41 | Fermat and higher-degree Diophantine equations | 19 | Primary |
| 11G30 | Arithmetic of curves over global fields | 21 | Secondary |
| 11Y50 | Computational solution of Diophantine equations | 27 | Secondary |
| 14G05 | Rational points | 36 | Secondary |

This choice fits the equation, the use of curves and Jacobians, and the computational proof. The single-primary/three-secondary line at `paper/manuscript.tex:89` is consistent with the classification's guidance.

## Reviewed file identities

Paths below are relative to the reviewed repository. SHA-256 binds the findings to these bytes; subsequent manuscript builds are not covered by this identity table unless their source is unchanged.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `LICENSE.md` | 2012 | `e45902e9acc6c44f7987ab8a98b97613daf89728afc51f510f0c4268afc74ae7` |
| `LICENSES/MIT.txt` | 1070 | `7725db43ebd8b09f0683d9e1ea8f5a99c13d080c255c53413ee5d0b35dedeff1` |
| `LICENSES/CC-BY-4.0.txt` | 18657 | `9ba9550ad48438d0836ddab3da480b3b69ffa0aac7b7878b5a0039e7ab429411` |
| `NOTICE.md` | 1579 | `dbcff2b661a7501d07c70677758b3a64e4ac2c08b7cbf57fe12cab6fb6e3f6c7` |
| `paper/manuscript.tex` | 87621 | `70f66fe3605ecbde730e21fbee0308daaf0533fcd566d464274944066c3ef9cf` |
| `paper/rank-proof.tex` | 21502 | `5d2df25bebb4f6bb9b737e6504adde76db4a21e8244c4611879dcd625efdebf8` |
