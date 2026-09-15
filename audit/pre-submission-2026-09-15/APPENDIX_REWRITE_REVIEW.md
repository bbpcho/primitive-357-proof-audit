# Appendix D mathematical rewrite review

The revised `repository/paper/rank-proof.tex` replaces the 184-line publication appendix with a 437-line mathematical argument. The conclusion and every original cross-reference label are preserved. The new text defines the descent spaces, states a rank–nullity stopping lemma, identifies the actual dyadic divisors, explains coherent global lifts and their local obstruction, and gives the subgroup-index and logarithmic deductions in full.

This is an expository revision of the previously audited argument. It does not purport to be a new independent implementation of the arithmetic, a proof-assistant formalization, or an external human referee report. The computational premises remain exact arithmetic results supplied with the ancillary data; their role is now separated from the deductions that use them.

## Scope and reference versions

- Baseline: `work/publication_2026_09_15/repository/paper/rank-proof.tex`.
- Revised text: `work/pre_submission_revision_2026_09_15/repository/paper/rank-proof.tex`.
- Supporting audit: `work/mathematical_argument_audit_2026_09_15/`.
- No sealed release, control repository, main manuscript, or computational evidence was edited by this rewrite task.
- The parent owns compilation, PDF inspection, and publication decisions. This task performed no build or network/GitHub operation.

## Proof-obligation mapping

Line numbers refer to the current revised file; the original numbers refer to the publication baseline.

| Original obligation | Original lines | Revised treatment |
|---|---:|---|
| Identify K, J, H0, H1; distinguish the two saturation claims | 4–14 | 4–16: definitions and the exact downstream conclusions are stated first. The fifth-division class remains E; the finite descent module is now E_Δ, avoiding a collision. |
| Identify the actual bitangent and tetrad modules and establish the BPS hypotheses | 20–27 | 18–76: degree-28 étale algebra, fake squareclass quotient and map, even-subset and tetrad modules, q, correction quotient and contact identity. The rational point supplies the divisor hypothesis. Only containment in a transitive affine group is asserted. |
| A global 66-dimensional containing space exists and contains all relevant representatives | 18–20 | 95–118: explicit support S, including the complex place; class number one of K; Cl(L)[2]=0; 28 independent unit classes and 38 principal support primes. The valuation exact sequence establishes the actual space V0=L(S,2), rather than only a formal array of 66 columns. |
| Restriction maps and complete allowed images | 29–46 | 78–93 and 120–150: one local completeness lemma and a table of domain/image dimensions; all 66 actual restriction columns; the original dimension chain and redundant-condition qualification. |
| Identify the final diagonal quotient and complementary class | 48–57 | 152–169: D is the intersection with the global diagonal image, so Q embeds in the fake squareclass quotient. Exact coordinate membership and successive ranks 7,11,12 establish Q=B⊕⟨c⟩. No equality between Q and the Selmer group is asserted. |
| Seven-adic full fake-kernel membership | 61–68 | 173–179: z7=P4−P1 and f(z7)=3λ² in every one of the seven source factors. Renaming the old z3 to z7 changes no cycle. |
| Seven-adic target identification, correction character and exact nonzero sign | 70–99 | 179–203 and 222–234: actual degree-42 target completion and incidence fields; normalized residues 1,1,6; exact μ2 identity and descended character. The proved conservative error bound 254 is separated from computed sign separations 255 and 511. |
| Seven-adic actual nonzero image and stopping equality | 101–113 | 205–220: the degree-zero cycle Norm(P)−2P1 over the unramified quadratic extension is written explicitly, with Z_original=−7Z_local and stable line classes. Image≥1 and kernel≥1 fill dimension2. |
| First dyadic complete image | 139–141 | 238–241: the Hensel lift of [2:46:1] and the known differences exhibit rank4, attaining the local Kummer dimension. |
| Second dyadic points and formerly opaque masks | 117–125 | 243–282: defines C0, P2′ and P5′ by explicit local charts and Hensel congruences, then z2=P2′+P2+C0−3P1 and z5=P5′+P2−2P1. The respective diagonal factors are −10 and 2. |
| Second dyadic correction quotient, signs and stopping | 126–141 | 284–311: target degrees 3,3,6,6,24; independent sextic characters; both cycles give the same nonzero vector (0,1). Only one kernel dimension is claimed. Root residual/derivative inequalities, propagated errors, and the threshold ord_A(2)=2 explain exact sign determination. |
| Global coherent lifts and local exclusion of c | 145–158, 170–172 | 313–381: distinguishes compatibility under BPS A.13(b) from merely squaring target roots. The 98 vectors, 77 relations, all315 extension, two global lifts, same source representative, actual 5-adic Kummer comparison, and correction characters yield the stated two obstructions. |
| Vanishing comparison kernel and rank/Sha conclusion | 156–169 | 365–369 and 383–407: one nonzero localization detects the one-dimensional global correction quotient; subtraction of a global point class rules out c+B; the true Selmer bound and Kummer exact sequence give dimension4, rank4, Sha[2]=0. |
| Odd and 5-prime subgroup indices, sieve coefficient coverage, global annihilator | 174–184 | 409–427: H0 odd index, H0⊂H1, H1 5-saturated, multiplication by400 on the finite quotient, and integer-torsion-free logarithmic target supply the deductions explicitly. |
| Arithmetic data locate the computational premises | Distributed throughout | 429–437: mechanical file locations and replay details are grouped in an evidence note pointing to the ancillary component guide. |

## Sources for the expanded definitions and bounds

The additions use existing exact project-specific evidence, not guessed interpretations of old log labels.

- `reviews/rank_global_foundations.md` supplies the complete support set, the correct `(29,s−15)` convention, the unconditional class-group/unit argument, all38 principal support generators, and the actual 66-dimensional squareclass basis. It also supplies the first-dyadic actual-point/image argument.
- `reviews/rank_geometry_supplement.md` supplies the actual bitangent/tetrad and target binding, all315 conic masks and exact incidence norm identities.
- `reviews/rank_p7_supplement.md` supplies the actual seven-component square tests, Eisenstein/Hensel/Krasner comparison, conservative margin254, and the norm cycle over the unramified quadratic extension.
- `reviews/rank_descent.md`, its claim ledger, and `checks/rank/` supply the BPS implications, the fresh coherent-root relation audit, the same-source 5-adic obstruction and actual dyadic point/target precision audit. The early open-coverage paragraphs in that evolving report are superseded by the later supplements and the aggregate audit; they are not treated as proof claims by this rewrite.
- In particular, `checks/rank/dyadic_curve_charts.gp` and its output identify the two normalized chart polynomials. `checks/rank/dyadic_actual_full_relations.gp` and its two outputs identify the cycles formerly written as `[old mask,C0 coefficient,diagonal]=[1,1,−10]` and `[1,0,2]`: old mask1 is D2, and the moving point difference must also be included. The final points and divisors in the rewritten text use exactly those meanings.
- The stored independent BPS applicability audit read the primary BPS paper, including Corollary12.5, Proposition7.3, the relevant global containing theorem, Remark11.6, and AppendixA. The rewrite retains those mathematical imports and does not claim to reprove the general descent framework.

## Deliberate wording safeguards

The rewrite continues to distinguish a containing fake space from an actual Selmer group, factor profiles from a nonzero evaluated character, a square target norm from a coherent true lift, and the difference `(1,1)` of the 5-adic obstructions from either individual obstruction. It does not assume the Galois group is the full affine group. It does not infer exact equality from numerical closeness or from repeated output, nor demand uniqueness of a finite square-root search when a norm witness suffices.

At the second dyadic place the correction quotient has dimension2, while the actual fake kernel has dimension1. Both displayed cycles detect the same kernel direction. At5 the actual fake kernel is zero, so there is no further quotient of the dimension2 correction space when testing local Kummer membership.

The representative c and the high-degree coefficient arrays remain specified by the exact ancillary data. No unsubstantiated short formula for c, contact conics, or field generators was invented for the prose. The appendix explains what those data must establish and how the resulting identities imply the conclusion.

## Checks and remaining work

All three original labels are present: `app:rank-proof`, `eq:rank-dimensions`, and `eq:rank-containing-quotient`. Two new internal labels name the correction formula and local-completeness lemma. A read-only structural check found balanced LaTeX environments. An initially invalid two-pair `split` display was changed to `aligned`; the parent then built the paper and requested one natural prose adjustment to eliminate an overfull line.

The separate pure-sector agent independently read the baseline, the relevant audit evidence and the full rewrite. It found no substantive mathematical error in the rewrite, confirmed the explicit dyadic cycles and local dimensions, and suggested the E_Δ/D definitions and explicit archimedean place in S; these suggestions are incorporated. This is a second AI review, not external specialist review.

No unresolved mathematical-definition issue was identified in the rewrite. Compilation, rendered-page review and final submission clearance remain with the parent. The existing gate requiring Dahmen's response is unaffected by this editorial work.
