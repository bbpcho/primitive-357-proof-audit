# Pure septic and rational-parameter logical audit

The terminal pure-field argument is coherent **conditional on the separately audited rank and field-enumeration conclusions** (`RANK-END`, `FIELD-END`). I found one false ancillary statement that should be corrected before submission: the common base points of the two printed quintics are not all above the three branch values. This does not invalidate the normalized rational map or the conservative finite sieve. No further terminal logical gap was found in the scope reviewed below.

This is a mathematical argument audit of the immutable manuscript snapshot, chiefly lines755–934,1321–1551 and1581–1617. I inspected the actual arithmetic sources, their identities and the final retained outputs. Earlier independently completed computations are used as such; I did not rerun broad arithmetic suites or infer mathematical truth from a status field. New bounded checks in this audit were the complete printed-coefficient binding, a separating Fano fibre, the exact finite base scheme and local ratio at its rational point, and the stated parameter-difference arithmetic. A direct characteristic-zero Groebner attempt was stopped at50 seconds and supplies no conclusion; the characteristic-zero base-point conclusion below instead has a finite-flat proof.

`pure_parameter_claims.json` supplies the claim graph. `PURE-END` is the branch conclusion. The genus-two/Flynn appendix belongs to the separate Section7 branch and is not used here.

## Required correction: common base points

At manuscript lines1540–1542, replace the claim that the certificate checks base points in the three branch fibres with:

> The function-field identities identify $t=-G_t/H_t$ with the parameter on $C_+$. This rational function extends uniquely to a morphism from the smooth projective quartic to $\mathbf P^1$, including at common zeros of $G_t$ and $H_t$. None of the five displayed reference points is a common zero of these forms; direct substitution gives the parameter values below.

The existing next line listing $0,1,\infty,\infty,\infty$ can then remain. The named canonical verifier actually checks those five substitutions and both rational inverse identities; it does not establish the stated confinement of all common base points.

There is also a concrete contradiction to that confinement. Over $\mathbf F_{23}$ at $s=4$, in the chart $X=1$, the reduced ideal $(Q,G_t,H_t)$ has the following lexicographic Groebner basis with variable order $Z,Y$:

```
Z − 11Y^4 − 2Y^2 − 11Y + 11
Y^5 − 11Y^4 + 4Y^3 − 3Y − 8
```

The second polynomial factors as

```
(Y+8)(Y²+5Y+1)(Y²−Y−1).
```

It is squarefree and the base scheme has length5. The corresponding homogeneous calculation has no common base point on $X=0$: the affine-at-infinity gcd is1, and $Q(0,0,1)=1$. Its rational point is $[1:15:5]$. At this point,

```
Q_Y=9, Q_Z=1, dZ/dY=14,
G_t=5u+O(u²), H_t=9u+O(u²), u=Y−15,
−G_t/H_t=2+O(u)  (mod23).
```

This is not merely a possible extra base point arising in reduction. On the generic smooth quartic the two sections have degree20, while the already proved map has degree15. Their common-base divisor consequently has degree5. Over the valuation ring at $(23,s−4)$, the common-zero scheme is proper and has finite generic and special fibres, hence is finite. Its generic rank and special-fibre length are both5, so the corresponding finite module has no23-torsion and is flat. The simple rational special point is therefore etale and lifts over $\mathbf Z_{23}$ to a generic common base point. Its two simple local zeros cancel, and its parameter reduces to2. A generic point with parameter0,1 or infinity cannot have that reduction. Thus the characteristic-zero branch-only claim is false, using the already established degree15 result rather than an unfinished generic elimination.

No terminal step uses the false claim:

- The field-to-curve bridge uses normalization and the isomorphism of smooth projective curves, so it extends across coordinate denominators.
- The actual zero divisor $(t)_0$ used to construct $E$ is the divisor of the cancelled rational function, not the uncorrected zero scheme of $G_t$.
- `verify_mixed_rational_t_mw_sieve_durable_v1.py:56–61` returns an unknown value at a simultaneous numerator/denominator zero. The pairing conditions at lines115–118 and148–151 retain that case. This can add candidates, never improperly remove a rational-parameter point.
- At the extra P1 Coleman zero, the evaluator explicitly checks the denominator is a23-adic unit before using its inverse.

The five reference points themselves have no common-base ambiguity. The false sentence concerns other geometric points.

## Fano necessity, completeness and the canonical model

A pure polynomial $T^7-3^a5$ is Eisenstein at5. Its splitting field is the compositum of the degree7 pure field and $\mathbf Q(\zeta_7)$, so its Galois group is $C_7\rtimes C_6$ and its unique quadratic subfield is $\mathbf Q(\sqrt{-7})$.

The scaled septic has derivative $7V^4(V-15)^2$. Its degree7 map has branch permutations of types5,3,7 over0,1,infinity. The inspected cover program checks all ten possible3-cycle partners of a fixed5-cycle whose product is a7-cycle; each generates $A_7$. The discriminant supplies the additional arithmetic sign. It also identifies the compatible-pair stabilizers with actual normalizers of a regular $C_7$, not merely groups of orders21 and42. The unordered-pair convention is essential and is now correct. The30 Fano planes, parity orbits15+15,120 pairs and degree8 forgetful map all follow from these actions. Riemann–Hurwitz gives genera3 and20.

For a pure-field specialization, the unique Sylow7 subgroup is normal and regular on the seven roots. Its normalizer is the specialized order42 group and fixes a compatible unordered pair. Over the unramified parameter locus, the quotient fibre is a finite etale Galois set; the fixed sheet is therefore a rational point. After adjoining the specified quadratic field, forgetting the negative-orbit plane gives a point of the selected $C_+$. This works for every conjugate embedding of the pure normal closure; no field-specific sheet was silently selected. Normalization handles a possible collision in an affine resolvent coordinate.

The separate fresh Fano main computation reconstructs unscaled integer coefficients with80 primes and a1330-bit CRT modulus beyond the1230-bit coefficient bound. The degree bound comes from root growth; the alternating difference is integrally divisible by the Vandermonde. The interpolation bound accounts for all coefficients, not just sampled values. As an additional bounded separating-fibre check I used

```
p=101879, t=68522,
roots of 15T^7−35T^6+21T^5−t:
170,15537,77158,78821,84363,92575,92854.
```

The15 Fano invariants in each parity orbit are distinct. Hence the invariant has not collapsed the15-sheet quotient. Transitivity supplies irreducibility. The corresponding fresh main output is retained at `verification/sectors/logs/independent_fano_resolvent_foundation.log`.

The canonical verifier performs actual exact remainder calculations modulo monic $R_+$: the quartic equation and both inverse identities, with each inverse denominator nonzero. Recovering both $q$ and $t$ proves a function-field isomorphism. Since the quartic is smooth, the isomorphism extends to the smooth projective curves. Smooth reduction at both23-adic places independently proves generic geometric smoothness. No proof depends on the ancillary stored “fresh-prime rank PASS” metadata of the old canonical routine or on its imported full-discriminant label.

I freshly compared the snapshot with the exact packet: all15 quartic coefficient pairs and all84 rational components of the two quintics agree, including the quintic monomial order. The five point coordinates and values are independently checked by exact substitution, and their characteristic-zero local orders are5,3,7,7,1. In particular P5 is unramified above infinity, as the corrected text now says.

## H0, H1, saturation and coefficient coverage

Let $D_i=[P_i-P_1]$. The construction in lines855–866 is valid: $A=(t)_0/5$ is a rational degree3 divisor and the pole divisor is $7P_3+7P_4+P_5$. Thus $5[A-3P_1]=7D_3+7D_4+D_5$, and $E=3[A-3P_1]-4D_3-4D_4$ satisfies $5E=D_3+D_4+3D_5$.

For two-saturation, the four actual global binary character rows on $(D_2,D_3,D_4,D_5)$ are

```
0 1 0 0
0 1 1 0
0 1 0 1
1 1 1 0
```

and on $(D_2,E,D_4,D_5)$ become

```
0 1 0 0
0 0 1 0
0 0 0 1
1 0 1 0.
```

The maps used for these characters come from the entire two-primary groups at the two places over23 and at $(43,s-37)$: their orders are independently reconstructed as8,8,16 after odd projection. Every state and generator edge has an actual divisor-class interpretation. Thus these are characters on all $J(K_7)$, not only on an enumerated proper subgroup. The corresponding mod5 character rows are

```
1 22 22 16
1 19  1 12
1  3  2  7
1 24 20 20,
```

whose determinant is4 mod5. The full five-primary groups used here have order25, from independently reconstructed whole orders10200 and73200. Reduction at53 gives order150039, excluding2- and5-torsion.

For either prime $\ell$, independent rows force $H\cap\ell J=\ell H$. Absence of $\ell$-torsion then gives saturation. This argument does **not** use the global rank upper bound. That upper bound is needed later: the four independent logarithm columns make the known subgroup rank4; `RANK-END` makes its index finite. $H_0$ has odd index; $H_0\subset H_1$; and $H_1$ is5-saturated. Consequently $[J:H_1]$ is coprime400. There is no unsupported claim that $H_0$ is5-saturated.

The coefficient-coverage claim also has a useful precise formulation for local maps whose full large-prime group orders were not independently reconstructed. Write $n=[J:H_1]$ and $n[P-P_1]=\sum a_i h_i$. At every selected place the actual projected curve-point class and projected generators have verified exponent dividing16 or25. Multiplication by $n$ is invertible on them. Therefore the same vector $n^{-1}(a_i)$ modulo400 supplies every local fingerprint. This proves necessity without presuming the uncomputed full order at every larger prime. All outside-subgroup point images were independently checked as two-primary, which is necessary for their exclusion; a “null” image was not treated as missing data.

## Finite sieve and all residue disks

The independent finite-map reconstruction covers16 embeddings,1272 curve-point images,222 pairwise distinguished subgroup states,888 actual generator transitions and321 outside-point checks. All projected point images are killed by16. The direct construction of $E$ passes at all16 embeddings. The six C25 reconstructions at23,43,109 cover336 point images and the corrected generator relation. The exact whole orders required for the global character domains at23 and43 are separately reconstructed.

The durable sieve enumerates all $16^4$ and $25^4$ coefficient vectors, then all compatible pairs. The old-to-corrected transformation is $(a,e,c,d)\mapsto(a,13e,c+13e,d+39e)$ modulo16. Its counts592,1252,144 and encoded survivor lists agree with the earlier independent enumeration. The five surviving modulo25 vectors and the **ordered**23-adic point pairs agree with the paper. At simultaneous form zeros, unknown parameters are retained; at a defined numerator/denominator pair, equality in projective residue coordinates is necessary for rationality of the global parameter. Point enumeration is projective and includes all chart boundaries.

Thus every hypothetical global rational-parameter point lies in one of the five product disks, not just one of five classes of an unspecified local subgroup. This is the interface needed by the subsequent analytic argument.

## Actual logarithms and the global annihilator

The adopted validators check exact function-field identity with the canonical quartic, pole cancellation and full integral Riemann–Roch lattices for $L(nD_0)$, $n=2,\ldots,7$. Each branch has150 basis functions and1088 checked multiplication identities modulo $23^{10}$. Unit derivative and distinct ordinate checks make the complementary-fibre cancellation integral; full reduction ranks and Riemann–Roch/Nakayama supply the complete lattice. The zero-class row module is the expected $V_2$ inside $V_3$.

The source group law matches the small-model algorithms in [Khuri-Makdisi, §5](https://arxiv.org/pdf/math/0105182). Here $\deg D_0=6\ge g+1=4$. Every row module, image and kernel is justified by unit pivots and full row checks over the local ring. This rules out hidden precision loss from nonunit elimination. The source's effective divisor $D_0+P_i-P_1$ represents the intended class with the correct sign. The decoded effective divisor near $2B$ represents a sum of local differences, so its tiny integrals divided by the checked unit scalar compute the required logarithm.

The two adopted replacements calculate **D4 as well as D2,D3,D5**. They use the earlier D4 caches only as comparisons. Their actual24 normalized entries agree with the final consumer at all9 digits. A unit4×4 block proves that the exact6×4 matrix has rank4. The exact kernel can be written $L=(-CB^{-1}\mid I_2)$, so the finite-precision annihilator rows genuinely lift to exact global annihilator rows.

After `RANK-END` makes $H_0$ finite index, these rows kill the whole Mordell–Weil group: a nonzero integer multiple of any class lies in $H_0$, and the target has characteristic zero. This step needs neither the exact index nor23-saturation. Torsion is killed automatically.

The relevant output identities are recorded in `verification/prior/work/v3_audit/sage_replay/{s4,s19}_candidate/audit_result.json`, the two `tensor_validation_*.json` files, and `global_log_binding_checks.json`. The source and arithmetic, not their status strings in isolation, support the inference.

## Regular disks and the complete P1 analysis

I checked the actual assumptions of [Siksek, Theorem2](https://msp.org/ant/2013/7-4/ant-v7-n4-p01-p.pdf). They require an odd unramified prime, good reduction at all its places, a full-rank subgroup and full column rank in the reduced tangent matrix. Here $d=2,g=3,r=4$, both places are good and the matrix is2×2. The four determinants12,16,4,19 are units. The differential basis is $(1,y,z)dy/Q_z$ on $X=1$; all ten reference reductions have a unit $Q_z$, including points above $t=\infty$. Consequently these are full product residue disks with valid uniformizers. Each of the four regular disks contains only its reference common zero.

At P1, write the two local parameters as23u and23v, so the **entire** product disk is parametrized by $\mathbf Z_{23}^2$. If $F_1,F_2$ are the two annihilator integrals, the normalized equations are $F_1/23$ and $(F_2-6F_1)/23^2$. The second numerator is integrally divisible by $23^2$: its two linear coefficients vanish modulo23 before scaling, and every higher local term supplies the extra factor. These divisions preserve the common-zero set; no branch is discarded.

The reductions are exactly

```
2u+4v=0,
21u+6v+14u²+21v²=0.
```

There are exactly two solutions among all529 residue pairs: $(0,0)$ and $(14,16)$, with Jacobian determinants20 and3. Multivariate Hensel gives one exact zero in each corresponding class and no zero elsewhere. The first is the exact reference point. The second is not assumed to be global.

The independent digit reconstruction ends at $u=2889982329,v=1104375606$ modulo $23^7$. Integral differential coefficients give an omitted integrated term of exponent $k$ valuation at least $k-v_{23}(k)$ on23u. For all omitted $k\ge12$, this is at least12; the two normalization divisions leave more than the required7 digits. The coefficient arithmetic modulo $23^9$ likewise leaves7 certified equation digits. Hensel therefore supplies the actual root coordinates modulo $23^8$.

At both endpoints the canonical denominator is a unit, so evaluating $t$ retains those8 digits. The values are59233664629 and24239267738 modulo78310985281. Their difference has exact23-adic valuation5 and leading digit9. Higher uncomputed digits cannot restore equality. A rational parameter has identical values in the two embeddings, so this unique extra Coleman zero is excluded. The five reference points are exactly the rational-parameter locus, conditional on the separately reviewed rank input.

For readability, the paper would benefit from printing the two normalized equations and the two-division precision argument rather than only the phrase “a normalized second-order system.” This is an exposition improvement: the actual supplied/adopted arithmetic already supports the argument, unlike the false base-locus sentence above.

## Audit limits and handoff

`RANK-END` owns the BPS descent, containing spaces, local stopping, p5 obstruction and global rank conclusion. `FIELD-END` owns the exhaustive seven-field enumeration and its hypotheses. I have not silently replaced either by an output marker or by the lower logarithm rank. The pure branch uses both as explicit graph dependencies. The published Chabauty result and the algebraic divisor-operation theorem were read in their primary statements and their hypotheses checked here.

No counterexample to the rational-parameter theorem was found. The concrete base-locus counterstatement requires a textual correction but introduces no missing terminal case. The current work changed only these two audit reports after the logical-audit assignment; no release, staging, GitHub or original attachment was modified by this audit.

## Input identities

The following SHA-256 values bind the principal exact data and sources examined. The printed-coefficient and new base-point calculations used the first two entries directly.

- `/Users/pcho/Documents/Codex/2026-09-13/ple/work/mathematical_argument_audit_2026_09_15/sources/manuscript.tex`
  `5dc92b60a88cdc0ec4addbe549efc5756e164db49b290fc0ac225bbc5dc972ff`

- `/Users/pcho/Documents/Codex/2026-09-13/ple/work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1/evidence/v3/repository/beal_357_spark_handover_2026-08-20/project/p7_f42_canonical_exact.json.gz`
  `1252327a057029dd0ff0f6347f848be88794842afa742503a6c179f683087739`

- `/Users/pcho/Documents/Codex/2026-09-13/ple/work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1/evidence/v3/repository/beal_357_spark_handover_2026-08-20/project/p7_f42_cover_certificate.py`
  `dd93bdb302ab4adc0d9b731c73dda488402016a5ddf78e816bdb8d73aa38bda9`

- `/Users/pcho/Documents/Codex/2026-09-13/ple/work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1/evidence/v3/repository/beal_357_spark_handover_2026-08-20/project/p7_fano_resolvent_certificate.py`
  `de3b8e28368510cdc18abc5dae9c3310b793b616ea8a15278f25c25ace6acaf7`

- `/Users/pcho/Documents/Codex/2026-09-13/ple/work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1/evidence/v3/repository/beal_357_spark_handover_2026-08-20/project/p7_f42_canonical_verify.py`
  `c71f094867f544fa0e8c79ad6919cd0803328f9bd7e3c10c7c0efb8df3f1b028`

- `/Users/pcho/Documents/Codex/2026-09-13/ple/work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1/evidence/v3/repository/results/2026-09-08_mixed_rational_t_signature_357_closure_v1/scripts/verify_mixed_rational_t_mw_sieve_durable_v1.py`
  `dca7a3638c06789de4cedf996e320f5fcc254e41c195ec47d7f10b2309f0f81e`

- `/Users/pcho/Documents/Codex/2026-09-13/ple/work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1/evidence/v3/repository/results/2026-08-31_p23_s19_alternative_km_base_chart_screen_v1/scripts/lift_p23_P1_exceptional_root_and_coefficients_v1.sage`
  `e9606acb97db17e86e33ddfa6273aa885d06c8fcee4d8856361da731a3affabf`

- `/Users/pcho/Documents/Codex/2026-09-13/ple/work/verified_release_2026_09_14/staging/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1/evidence/v3/repository/results/2026-08-31_p23_s19_alternative_km_base_chart_screen_v1/certificates/p23_ros_log_rank_and_siksek_v1.json`
  `183ae745a23d2b0353bf8280488a67e22ce39ee1cf9203b46e72fc85455456e8`

