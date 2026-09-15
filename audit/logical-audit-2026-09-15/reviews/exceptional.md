# Exceptional septic argument: logical audit, 15 September 2026

The exceptional-field elimination is supported by the checked finite computations and the stated mathematical imports. I found a reversed pair of parity labels in the manuscript, together with an omitted explanation that the exceptional case forces Z odd. Both have concrete repairs below. They do not change the union of packets tested or the terminal contradiction. I found no additional unresolved mathematical gap in this bounded exceptional-sector audit. This conclusion does not independently certify the other sectors or the structural local-algebra premise used in the seven-field classification.

The audited source is `work/mathematical_argument_audit_2026_09_15/sources/manuscript.tex`, principally lines 936–1163 and 736–747. All line references below are to that unchanged snapshot. Let R denote the absolute release directory `/Users/pcho/Documents/Codex/2026-09-13/ple/work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1`, and P its `evidence/v3/repository/beal_357_spark_handover_2026-08-20/project` subdirectory. Sources and sealed release files were not edited. The accompanying claim ledger separates checked deductions, numerical evidence, imports, and the required correction. A terminal checked deduction is conditional on all of its listed dependencies; it does not mark their transitive closure checked.

## Required correction: the prime-2 labels and the missing Z-odd explanation

Lines 1009–1010 and 1017–1018 use the opposite X/Y convention to their certificate. `P/p7_odd_branch_local2_certificate.py:4–15,88–99` uses s=X³/Z⁷ and thus X³+Y⁵=Z⁷. The manuscript uses X⁵+Y³=Z⁷. Consequently the correct manuscript traces are **−1 when Y is even, and 0 when X is even**. Exchange the two table labels, keeping the entries fixed:

| branch in manuscript notation | 22 | 23 | 32 | 33 |
|---|---:|---:|---:|---:|
| Y even | 1 | 2 | 2 | 5 |
| X even | 2 | 10 | 3 | 11 |

The fresh ambient log retains both scalar possibilities and all 36 occurrences. This error therefore does not invalidate the terminal exclusion. The numerical certificate and its historically named output markers are correct in their own convention; the mistake is their transfer into the paper.

The two-branch test also requires Z odd. This follows locally. A fresh exact PARI calculation with `nfinit(T^7-483*T^2+3955*T-3945)` and `idealprimedec(nf,2)` gives `(e,f)=[(1,1),(1,2),(1,4)]`. If 2 divides Z, primitivity forces X,Y odd, and U=ZT gives the integral defining polynomial

`15U^7 − 35ZU^6 + 21Z²U^5 − X^5`.

Its mod-2 reduction is the separable polynomial

`U^7+1 = (U+1)(U³+U+1)(U³+U²+1)`.

Hensel's lemma would give local degrees [1,3,3], contradicting the exceptional field's [1,2,4]. Thus Z is odd and exactly one of X,Y is even.

Here is precise replacement text for lines 1009–1011, before the relabelled table:

```tex
The exceptional field is unramified at $2$ with local factor degrees
$[1,2,4]$.  If $2\mid Z$, the scaled equation for $U=ZT$ reduces to
$U^7+1=(U+1)(U^3+U+1)(U^3+U^2+1)$, so its local degrees would be
$[1,3,3]$, a contradiction.  Hence $Z$ is odd and exactly one of $X,Y$
is even.  The prime-$2$ calculation gives the necessary residual trace
$-1$ when $Y$ is even and $0$ when $X$ is even.  Retaining every packet
for which that scalar is a root of the residual $T_2$ polynomial gives
```

I also checked the trace identification directly, beyond reading the certificate labels. Put s=Y³/Z⁷ and e=1−s=X⁵/Z⁷. PVT Proposition 7.1 identifies the plus curve at t₀=(s−1)/s with

`y²+y(x³+s e²)=2s e²x³+3s²e³x+s²e⁴`.

If Y is even, choose k³=s e² and substitute x=kx′, y=s e²y′. Reduction is `y²+y(x³+1)=1`, with counts 3 and 7 over F₂ and F₄; over F₄ its Frobenius polynomial is `(T²+T+4)²`, giving RM trace −1. If X is even, choose k⁵=s²e³ and substitute x=kx′, y=k³y′. With d=(e/s)^(1/5), reduction is `y²+yx³=x`, with counts 3 and 5, and Frobenius polynomial over F₄ `(T²+4)²`, giving trace 0. Odd-power roots of 2-adic units exist uniquely, and the valuations are divisible by the needed odd powers. Both reduced curves are smooth, including their two points at infinity. This establishes the convention independently.

No other same-convention transfer error was found: `(a,b,c)=(X,−Z,Y)`, t₀=η/(η−1), the five-root X branch and three-root Y branch at 29, and the ordered parameter/count table all match the manuscript's X⁵+Y³ convention.

## Published theorem interfaces

**Seven-field frontier (FIELD-END).** I read Putz's actual Theorem 3.50, printed page 118 (PDF page 125), in `R/evidence/v3/repository/references/Thesis_CasperPutz.pdf`. Its degree, signature, ramification and specified local-algebra hypotheses are precisely those listed at manuscript 736–739, and its seven fields are exactly those at 743–745. The signature can also be checked directly: Φ′(T)=105T⁴(T−1)² makes Φ strictly increasing on the real line, so an ordinary specialization has one real root. Putz's exhaustive enumeration is an **imported theorem**, not a newly rerun Hunter enumeration. Verification that every solution-induced field has the cited Dahmen–Siksek local algebras belongs to the parent's structural audit and remains an explicit dependency of FIELD-END.

**Frey specialization and p=7.** I read the exact archived PVT v1 PDF, `R/evidence/v3/repository/references/Pacetti_Villagra_Torcomian_2512.17845v1.pdf`, especially Theorems 2.1, 2.4 and 7.8, Remark 2.2, Proposition 7.1 and §7.4. The mapping a=X,b=−Z,c=Y satisfies the cited a⁵+bᵖ+c³ equation for p=7. The specialization is ordinary over Q because X,Y,Z are nonzero. The modularity assertion used at 958 is Theorem 2.4(1), and the irreducible four-level conclusion is exactly Theorem 7.8. That theorem has no exclusion of p=7; the large-exponent headline theorem is not the input. Theorem 2.1 supplies residual ramification and finiteness at p. The conductor bounds used in the reducible case come from Corollary 3.6/Table 3.2 and Corollary 3.11, Proposition 3.14 and Table 3.5 (exchanging q/r as in the source); those local bounds do not require the residual irreducibility assumption of Theorem 7.8.

The determinant and trace formulas refer to the weight-two realization: Remark 2.2 distinguishes the Tate-twisted realization from unnormalized hypergeometric traces. The curve and all terminal trace formulas in this manuscript use the weight-two normalization consistently. Naming it explicitly would remove possible ambiguity.

I also checked [Breuil–Diamond, Theorem 3.2.2](https://www.imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/extensions.pdf). A direct application of that theorem requires irreducibility after restriction to F(ζ₇), not merely irreducibility over F. The present paper imports the specialized PVT Theorem 7.8 instead, so it does not purport to establish a separate direct Breuil–Diamond application. Do not replace the precise PVT import by a bare appeal to Breuil–Diamond without addressing that extra hypothesis.

## Why the finite Hecke computation covers a newform

The original source and the V2 independent arithmetic were compared: both coverage verifiers, the C consumer, the two quaternion generators, and the local-2 source are unchanged. The release's actual fresh log `R/verification/sectors/logs/hilbert-hecke-ambient-coverage.log` contains all four full operator runs. Its mathematical relevance is supported by the following source and independent arithmetic checks, rather than its final PASS label.

The independent foundation source is `R/audit/work/hecke_foundations/scripts/independent_quaternion_generators.py:16–115`. The order's parity lattice has index 16 over O_F⁴, is multiplicatively closed, and has absolute trace discriminant 625=disc(F)⁴, so its relative reduced discriminant is 1 and it is maximal. The norm-one unit enumeration is exhaustive: writing twice-coordinates v, the two norm equations imply Σvᵢ²=4, hence each vᵢ lies in [−2,2]. The list has 120 units, or 60 modulo ±1. Since ε has norm −1, all totally positive units of F are squares, so these give the full projective order-unit group. Minkowski's bound gives h_F=h_F⁺=1. Eichler's maximal-order mass formula gives mass 1/60 using ζ_F(−1)=1/30; the principal class already contributes 1/60, so there is no missing ideal class. The formula applies to this definite algebra with finite discriminant 1. [Voight, Theorem 26.5.4](https://jvoight.github.io/quat-book.pdf)

The 20 neighbour sets have the required norm, order membership, and exactly N(q)+1 distinct local projective images (at 2, exact unit inequivalence instead). These prove completeness, not only correctness of individual supplied neighbours. The transposition anti-involution preserving the order checks the left/right convention. Quotienting the entire finite projective sets gives 46,226,406,2026 orbits at levels 22,23,32,33. Their sizes before quotienting are 2700,13500,24300,121500. The mass functional uses orbit sizes, proportional to inverse stabilizer orders; stabilizers divide 60, and 7 divides neither their orders nor these four total sizes. Thus the constant line splits off and the mass kernel gives the correct saturated cuspidal lattice.

[Dembélé–Voight, Theorem 3.9 and §4](https://jvoight.github.io/articles/hmf-crm-bcn-053024.pdf) provide the Hecke-equivariant characteristic-zero correspondence and the orbit-function model; finite quaternion discriminant 1 means its image is the full Hilbert cusp space. All four levels are allowed. A transferred algebraic eigenvector can be scaled to be primitive in the local function lattice at a coefficient prime above 7. Its reduction is nonzero, its mass remains zero, and all Hecke equations survive reduction. The reduced vector may live over an extension of F₇, which is harmless: the computed kernels commute with scalar extension. No integral Jacquet–Langlands theorem, mod-7 old/new injectivity, or semisimplicity of a degeneracy map is required.

**Filter coverage.** PVT §7.4 gives ordinary parameters, boundary character possibilities at 0 and infinity, and the level-lowering signs at 1. The degree-two transport applies to the boundary traces computed over the larger cyclotomic field: a ↦ a²−2ℓ; the ordinary data are already over F and must not receive that transport. The independently written integer point counter checks all 1264 ordinary parameters at the 18 required primes; the Jacobi-sum computation checks all 128 boundary character possibilities at the 16 split primes. The input parser separately reduces all 6253 polynomials across the full 37-prime upstream file. These are different verification scopes; lines 986–989 should ideally distinguish them explicitly.

At the two inert primes 13,17 the adopted filter is T⁷−T. Its scalar-trace assertion uses the Frey curve's rational origin **and** the Galois compatibility of its RM correspondences, not rational origin alone. If rational Frobenius is Aσ on the two-dimensional coefficient space, the F-prime Frobenius is Aσ(A); its trace is fixed by σ because tr(σ(A)A)=tr(Aσ(A)). Thus the residual trace is in F₇. The ordinary point counts check this scalar case directly; the same semilinear argument covers the good boundary realizations, and the multiplicative level-lowering traces ±(ℓ²+1) are scalar already. The RM realization used here is the plus-Jacobian construction in PVT §2.2/§7.1.

The old ℓ=131 filter indeed misses 1=−132 mod7. Replacing it by T⁴⁹−T preserves every possible F₄₉-valued Frey eigenvector. It is not literally a vacuous condition on an arbitrary ambient module: it may remove other residue fields or nilpotent directions. Consequently “conservative no-filter condition” at 997 should preferably read “a condition imposing no further restriction on F₄₉-valued Frey eigenvalues.” The proof only needs the latter, which is checked.

**Actual coverage and terminal Hecke support.** `P/p7_level33_mod7_intersection.c:430–474` computes ordinary filter kernels and the mass kernel. Lines 204–257 split invariant components and check every factor-kernel dimension against characteristic multiplicity before accepting a split. Coprimeness, commutativity and the total dimension checks prevent an omitted component. Names/signatures may merge eigensystems, but such a merger is a harmless superset here. No old/new subtraction is made.

The independent `work/v2_audit/independent_hecke_review.py`, its fresh four sparse matrices and `independent_hecke_22_23_32_33.json` check the implication without relying on packet labels or this consumer's decomposition algorithm:

| level | filtered cusp dimension | T₂=−1 eigenspace | T₂=0 eigenspace |
|---|---:|---:|---:|
| 22 | 8 | 3 | 4 |
| 23 | 38 | 6 | 28 |
| 32 | 28 | 8 | 9 |
| 33 | 98 | 20 | 54 |

On each of the eight spaces, `T(T+2)(T²+5T+2)(T²+3T+4)` annihilates T₂₉, and each of the four curve polynomials has zero kernel. The fresh release run agrees on dimensions and the 36 selected occurrences. Its annihilator family T,T²,T+2,T²+5T+2,T²+3T+4 is covered by the six manuscript factors, including the sixth factor T−5. The manuscript has correctly repaired its former “first four only” wording at 1135.

The neighbour at 29 has norm 5+ε, hence uses the conjugate of the manuscript's prime, whose generator is 6−ε. This does not change the comparison: each trace-norm polynomial contains both conjugates and the ray-character support is the same at both primes. This is a second convention transfer checked explicitly.

## Reducible representations and the ray character

The semisimplification argument at 1040–1049 is sound. Away from 7, the two constituents have inverse inertial characters and equal conductor exponent; semisimplification can only decrease the conductor. The bounds ≤3 therefore give a(ψ)≤1 at 3 and 5. All other finite primes away from 7 are unramified by the Frey input.

At the unique prime over 7, the local field is absolutely unramified with residue F₄₉. [Raynaud, Corollary 3.4.4](https://www.numdam.org/article/BSMF_1974__102__241_0.pdf) bounds the finite-flat constituent's fundamental-character digits by 0 and 1. A rank-one character of the full local Galois group has tame inertia level dividing two: wild inertia has no nontrivial image in a characteristic-7 multiplicative group, and Frobenius conjugation makes the tame image's order divide 48. Thus the four possibilities are 1,ω₂,ω₂⁷,ω₂⁸, with ω₂⁸=χ̄₇. The two mixed possibilities are not excluded by finite flatness alone; the manuscript now supplies the necessary global step.

Indeed u=ε⁸=13+21ε is totally positive, 1 modulo 3√5 and −1 modulo 7. Reciprocity and the already proved conductor bounds force ψ(rec₇(u))=1. The mixed possibilities give −1, so only the equal-digit possibilities remain. Interchanging the two constituents then gives one unramified at 7. This repair correctly avoids the earlier invalid inert-prime shortcut.

For completeness, the narrow ray group can be calculated from `(O_F/3)× × (O_F/√5)× × {±1}²`, of order 128. In cyclic coordinates (8,4,2,2), ε and −1 have vectors (1,3,0,1) and (4,2,1,1); their image has order 16. The quotient has eight elements, with counts 1,3,4 of orders 1,2,4, hence C₄×C₂. This uses the checked strict class number one. At q=(29,√5−11), α=6−ε is totally positive of norm 29, and α²−ε²=12(3−ε) is divisible by 3√5. The ray class thus has order at most two; modulo 3, α=ε⁵ while totally positive units are even powers of ε, of order eight modulo 3, proving the class nontrivial. Therefore every possible ψ gives trace ±2 since χ̄₇(q)=29=1 mod7. Both roots occur in the displayed six-factor family. This uses all characters; no conductor or sign branch is discarded.

## The 29-adic endpoint

I reran the independent elementary arithmetic `work/review/exceptional_audit.py` against the four-parameter calculation. The exceptional polynomial is squarefree mod29 with degrees [1,3,3]; exhaustive η=2,…,28 gives exactly 10,14,24,28. The map t₀=η/(η−1) gives 14,10,25,15, with no sign reversal.

The nonordinary branch exclusions at 1097–1106 are justified. The five-root X cluster has separable scaled reduction of degrees [1,2,2], with complementary quadratic [1,1]. The three-root Y cluster has [1,2], with complementary quartic [1,1,2]. Here the cluster valuations are respectively multiples of five and three, so the scalings are over Q₂₉. If 29 divides Z, the U=ZT reduction is 15U⁷−X⁵; because μ₇ is in F₂₉, this is either split or irreducible of degree seven. Each reduction is separable, so Hensel lifting preserves these local factor degrees. None gives [1,3,3]. Primitivity excludes simultaneous divisibility branches.

Fresh counts, including the points at infinity, were:

| η | t₀ | N₁ | N₂ | trace-norm polynomial mod7 |
|---|---:|---:|---:|---|
|10|14|29|955|T²+6T+6|
|14|10|22|916|T²+6T+4|
|24|25|37|931|T²+4|
|28|15|25|883|T²+2T+3|

The relation to the RM traces is correct: if the degree-four Frobenius polynomial has coefficients `(1,−A,B,−29A,29²)`, the two traces have sum A and product B−58. These are trace-norm polynomials, not degree-two Frobenius characteristic polynomials. The manuscript now explicitly distinguishes them. The four curves are smooth ordinary specializations at 29, and the RM factorization is the cited plus-Jacobian realization.

The freshly recomputed resultant rows are `[6,1,5,1,1,5]`, `[4,2,3,1,6,3]`, `[4,2,6,1,1,1]`, `[3,2,6,2,4,3]`. Every entry is nonzero. Bézout over F₇ therefore excludes a common root even over its algebraic closure; repeated factors cause no exception. The irreducible and reducible cases exhaust all two-dimensional residual representations. Conditional on the explicitly cited Frey, level-lowering and modular-form interfaces and the structural solution-to-field premise, the exceptional field is excluded (EXC-END). The terminal deduction is not a claim that those imported theorems, Putz's Hunter enumeration, or the other sectors have been re-proved by running the release.

## Evidence scope and disposition

This turn reread the primary theorem statements, inspected the consumer and foundation logic, checked unchanged core bytes against the earlier independent audit, read the actual new ambient output, freshly repeated the 29-arithmetic, and freshly checked the exceptional local factorization at 2. It did not rerun the expensive four-level operator generation, which is supported by the earlier independent matrices and the later fresh release replay. The explicit sources and outputs above make that distinction reproducible. The system `python3` currently refuses execution pending an Xcode license; no license was accepted. Lightweight arithmetic used the existing bundled Python and PARI runtime.

Required editorial disposition: swap the X/Y labels and add the Z-odd proof. Optional precision improvements: name the weight-two realization, distinguish the 37-prime input reduction from the 18-prime independent count reconstruction, and qualify “no-filter” as a statement about F₄₉-valued eigenvalues. No sealed artifact was changed during this audit.

The parent's corrected copy at `work/mathematical_argument_audit_2026_09_15/draft/manuscript.tex` was subsequently read and independently validated. Its added W=ZT argument, Y-even/−1 and X-even/0 sentence, and exchanged table labels are correct. This is recorded as **corrected in draft**, while the original snapshot's ledger status remains `CORRECTION_REQUIRED`. In particular, no open project-specific Breuil–Diamond condition is being carried silently: the primitive specialization and irreducibility are exactly the hypotheses of the specialized PVT Theorem 7.8 actually used, and their applicability is checked. General theorem reliance remains an explicitly imported premise, rather than an unresolved verification label.
