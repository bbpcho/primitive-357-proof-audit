# Argument audit ledger

This ledger targets the corrected 15 September review draft. A checked row records the stated review and evidence, not proof-assistant certification. Imported results remain explicit dependencies. Grouped claims cover the argument at lemma/interface level; they are not a formal sentence-by-sentence proof.

Claims: 118. Open project-specific claim nodes after the supplementary reviews: 0. Named import dependencies: 70. The graph is acyclic.

The frozen source errors remain visible as source_status and source_claim in the JSON. The draft corrections are separately labelled; original review ledgers retain their historical open statuses and are superseded only by the explicit supplements.

| Claim | Current audit status | Dependencies |
|---|---|---|
| GLOBAL-01 | CHECKED_ARGUMENT |  |
| GLOBAL-02 | CHECKED_ARGUMENT | GLOBAL-01 |
| GLOBAL-03 | CHECKED_ARGUMENT | GLOBAL-02 |
| GLOBAL-04 | IMPORTED_RESULT_APPLICABILITY_CHECKED | GLOBAL-01, DS:Proposition3.5 |
| GLOBAL-05 | CHECKED_ARGUMENT | GLOBAL-03, GLOBAL-04 |
| GLOBAL-06 | IMPORTED_RESULT_APPLICABILITY_CHECKED | GLOBAL-01, GLOBAL-02, GLOBAL-03, GLOBAL-04, DS:Corollary3.4, DS:Propositions3.6-3.7, DS:UnramifiedSupport |
| RAT-01 | CHECKED_ARGUMENT | GLOBAL-02 |
| RAT-02 | IMPORTED_RESULT_APPLICABILITY_CHECKED | RAT-01, DS:Lemmas6.2-6.3 |
| RAT-03 | IMPORTED_RESULT_APPLICABILITY_CHECKED | RAT-02, DS:Lemma6.4 |
| RAT-04 | CHECKED_ARGUMENT | RAT-03 |
| RAT-05 | CHECKED_COMPUTATION |  |
| RAT-06 | CHECKED_ARGUMENT | RAT-03, RAT-05, GLOBAL-02 |
| RAT-07 | CHECKED_ARGUMENT | RAT-03 |
| RAT-08 | IMPORTED_RESULT_APPLICABILITY_CHECKED | DS:Lemma6.6 |
| RAT-09 | IMPORTED_RESULT_APPLICABILITY_CHECKED | RAT-08, DS:Lemma6.7 |
| RAT-10 | IMPORTED_RESULT_APPLICABILITY_CHECKED | RAT-09, DS:Lemma6.8 |
| RAT-11 | CHECKED_ARGUMENT | RAT-03, GLOBAL-02 |
| RAT-END | CHECKED_ARGUMENT | RAT-04, RAT-06, RAT-07, RAT-08, RAT-09, RAT-10, RAT-11 |
| QUAD-01 | CHECKED_ARGUMENT | GLOBAL-03, GLOBAL-04, DS:Corollary3.4, DS:UnramifiedSupport |
| QUAD-02 | IMPORTED_RESULT_APPLICABILITY_CHECKED | QUAD-01, GLOBAL-02, DS:Proposition5.1 |
| QUAD-03 | CHECKED_COMPUTATION | QUAD-02 |
| QUAD-04 | CHECKED_ARGUMENT | QUAD-03 |
| QUAD-05 | CHECKED_COMPUTATION | QUAD-03, Magma:EllipticChabauty, Magma:Saturation |
| QUAD-06 | CHECKED_ARGUMENT | QUAD-04, QUAD-05 |
| QUAD-END | CHECKED_ARGUMENT | QUAD-02, QUAD-06, GLOBAL-02 |
| CUBIC-01 | IMPORTED_RESULT_APPLICABILITY_CHECKED | GLOBAL-05, DS:Proposition4.3 |
| CUBIC-02 | CHECKED_ARGUMENT | CUBIC-01, GLOBAL-02, DS:Lemma7.2 |
| CUBIC-03 | CHECKED_ARGUMENT |  |
| CUBIC-04 | IMPORTED_RESULT_APPLICABILITY_CHECKED | CUBIC-03, DS:Lemma7.3 |
| CUBIC-05 | CHECKED_ARGUMENT | CUBIC-03, CUBIC-04 |
| CUBIC-06 | IMPORTED_RESULT_APPLICABILITY_CHECKED | CUBIC-05, DS:Lemma7.4 |
| CUBIC-07 | IMPORTED_RESULT_APPLICABILITY_CHECKED | Flynn:Corollary2.2, Flynn:Theorem3.5 |
| CUBIC-08 | CHECKED_ARGUMENT | CUBIC-05, CUBIC-07 |
| CUBIC-09 | CHECKED_ARGUMENT | CUBIC-07 |
| CUBIC-10 | IMPORTED_RESULT_APPLICABILITY_CHECKED | CUBIC-02, CUBIC-06, CUBIC-08, CUBIC-09, DS:Lemma7.6 |
| CUBIC-11 | CHECKED_ARGUMENT | CUBIC-10, DS:Lemma7.7 |
| CUBIC-END | CHECKED_ARGUMENT | CUBIC-02, CUBIC-10, CUBIC-11, DS:Proposition7.1 |
| FIELD-END | IMPORTED_RESULT_APPLICABILITY_CHECKED | Putz Theorem 3.50, GLOBAL-06 |
| RANK-01 | CHECKED_COMPUTATION |  |
| RANK-03 | CHECKED_COMPUTATION | RANK-01, BPS:12.1, BPS:12.2, BPS:5.7 |
| RANK-04 | CHECKED_COMPUTATION | RANK-01, RANK-03, BPS:12.2, BPS:12.3 |
| RANK-07 | IMPORTED_RESULT_APPLICABILITY_CHECKED | RANK-01, RANK-03, RANK-04, BPS:6.3, BPS:6.10, BPS:12.5 |
| RANK-08 | CHECKED_ARGUMENT | RANK-07, BPS:7.2, BPS:7.3, BPS:9.2, BPS:10.9a, STANDARD:Minkowski, STANDARD:ClassFieldTheory, Yu:OrdinaryAmbiguousClassFormula, Doud:Theorem2.4, DAndreaDickenstein:MacaulayResultant, STANDARD:AnalyticClassNumberFormula, STANDARD:DirichletUnits |
| RANK-09 | CHECKED_ARGUMENT | RANK-03, RANK-08, STANDARD:LocalSquareclasses |
| RANK-02 | IMPORTED_RESULT_APPLICABILITY_CHECKED | RANK-01, BPS:10.2, BPS:Hyp10.1, BPS:Hyp11.1 |
| RANK-05 | CHECKED_COMPUTATION | RANK-03, RANK-04, BPS:5.1, BPS:5.4, BPS:5.5 |
| RANK-06 | CHECKED_ARGUMENT | RANK-05, RANK-03 |
| RANK-10 | CHECKED_COMPUTATION | RANK-06, RANK-07, BPS:11.6 |
| RANK-14 | CHECKED_COMPUTATION | RANK-03, RANK-09 |
| RANK-15 | CHECKED_ARGUMENT | RANK-03 |
| RANK-16 | IMPORTED_RESULT_APPLICABILITY_CHECKED | RANK-07, RANK-14, RANK-15, BPS:A24a |
| RANK-17 | CHECKED_COMPUTATION | RANK-06, RANK-07, RANK-15 |
| RANK-18 | CHECKED_ARGUMENT | RANK-03, RANK-09 |
| RANK-19 | CHECKED_ARGUMENT | RANK-02, RANK-10, RANK-14, RANK-15, RANK-16, RANK-17, RANK-18, BPS:A24b |
| RANK-20 | CHECKED_COMPUTATION | RANK-01, RANK-03, RANK-07 |
| RANK-21 | CHECKED_COMPUTATION | RANK-03, RANK-20 |
| RANK-22 | CHECKED_COMPUTATION | RANK-06, RANK-07, RANK-21 |
| RANK-FIRST-DYADIC | CHECKED_ARGUMENT | RANK-01, RANK-03, RANK-06, RANK-09, BPS:11.6, STANDARD:StrongHensel, RANK-02 |
| RANK-23 | CHECKED_ARGUMENT | RANK-02, RANK-20, RANK-21, RANK-22, BPS:11.6, BPS:A24b, RANK-FIRST-DYADIC |
| RANK-24 | CHECKED_COMPUTATION | RANK-06, RANK-07 |
| RANK-33 | CHECKED_COMPUTATION | RANK-01, RANK-03, RANK-07 |
| RANK-25 | CHECKED_COMPUTATION | RANK-03, RANK-05, RANK-07, RANK-24, RANK-33, BPS:A13, BPS:A14 |
| RANK-26 | CHECKED_ARGUMENT | RANK-10, RANK-33 |
| RANK-34 | CHECKED_COMPUTATION | RANK-03, RANK-04, RANK-05, RANK-07, RANK-33 |
| RANK-27 | CHECKED_COMPUTATION | RANK-03, RANK-25, RANK-26, RANK-33, RANK-34, BPS:A26 |
| RANK-11 | CHECKED_ARGUMENT | RANK-09, RANK-10 |
| RANK-12 | CHECKED_COMPUTATION | RANK-09, RANK-11, RANK-19, RANK-23 |
| RANK-13 | CHECKED_COMPUTATION | RANK-08, RANK-12 |
| RANK-28 | CHECKED_ARGUMENT | RANK-02, RANK-24, RANK-25, RANK-26, RANK-27, BPS:10.14, BPS:A26 |
| RANK-29 | CHECKED_ARGUMENT | RANK-07, RANK-13, RANK-24, RANK-28, STANDARD:KummerExactSequence, STANDARD:MordellWeil |
| RANK-30 | CHECKED_ARGUMENT | RANK-13, RANK-24, RANK-29, STANDARD:MordellWeil |
| PURE-02 | CHECKED_ARGUMENT |  |
| PURE-03 | CHECKED_COMPUTATION | PURE-02 |
| PURE-04 | CHECKED_ARGUMENT | PURE-03 |
| PURE-06 | CHECKED_ARGUMENT | PURE-02, PURE-04 |
| PURE-07 | CHECKED_ARGUMENT | PURE-04, PURE-06 |
| RANK-31 | CHECKED_ARGUMENT | RANK-30, PURE-06, PURE-07 |
| RANK-32 | CHECKED_ARGUMENT | RANK-30, RANK-31, STANDARD:FiniteAbelianGroups |
| RANK-END | CHECKED_ARGUMENT | RANK-08, RANK-09, RANK-19, RANK-23, RANK-25, RANK-27, RANK-29, RANK-30, RANK-31, RANK-32 |
| PURE-01 | CHECKED_ARGUMENT |  |
| PURE-05 | CHECKED_ARGUMENT | PURE-01, PURE-02, PURE-04 |
| PURE-11 | CHECKED_COMPUTATION | PURE-04 |
| PURE-12 | CHECKED_ARGUMENT | PURE-04, PURE-11 |
| PURE-08 | CHECKED_ARGUMENT | RANK-END, PURE-06, PURE-07, PURE-12 |
| PURE-09 | CHECKED_ARGUMENT | PURE-08 |
| PURE-10 | CHECKED_COMPUTATION | PURE-04, PURE-09 |
| PURE-13 | CHECKED_ARGUMENT | RANK-END, PURE-12 |
| PURE-14 | IMPORTED_RESULT_APPLICABILITY_CHECKED | PURE-04, PURE-08, PURE-11, PURE-13, Siksek:Theorem2 |
| PURE-15 | CHECKED_ARGUMENT | PURE-10, PURE-13, PURE-14 |
| PURE-16 | CHECKED_ARGUMENT | PURE-11, PURE-13 |
| PURE-17 | CHECKED_ARGUMENT | PURE-04, PURE-16 |
| PURE-18 | CHECKED_ARGUMENT | PURE-05, PURE-06, PURE-08, PURE-10, PURE-15, PURE-17 |
| PURE-END | CHECKED_ARGUMENT | FIELD-END, RANK-END, PURE-05, PURE-18 |
| EXC-01 | CHECKED_ARGUMENT |  |
| EXC-02 | IMPORTED_RESULT_APPLICABILITY_CHECKED | EXC-01, PVT Theorems 2.1 and 2.4(1), Remark 2.2 |
| EXC-03 | IMPORTED_RESULT_APPLICABILITY_CHECKED | EXC-01, EXC-02, PVT Theorem 7.8 |
| EXC-04 | CHECKED_COMPUTATION |  |
| EXC-05 | IMPORTED_RESULT_APPLICABILITY_CHECKED | EXC-04, Eichler maximal-order mass formula, Voight Theorem 26.5.4 |
| EXC-06 | CHECKED_ARGUMENT | EXC-03, EXC-04, EXC-05, Dembélé–Voight Theorem 3.9 and §4 |
| EXC-08 | CHECKED_ARGUMENT | EXC-01, EXC-02, PVT §2.2 and §7.1 RM realization |
| EXC-09 | CHECKED_ARGUMENT | EXC-02 |
| EXC-07 | CHECKED_COMPUTATION | EXC-01, EXC-02, PVT §7.4, EXC-08, EXC-09 |
| EXC-10 | CHECKED_ARGUMENT |  |
| EXC-11 | CORRECTED_IN_REVIEW_DRAFT | EXC-01, EXC-10 |
| EXC-12 | CHECKED_COMPUTATION | EXC-06, EXC-07, EXC-09, EXC-10, EXC-11 |
| EXC-13 | CHECKED_ARGUMENT | EXC-02, PVT Corollaries3.6,3.11, Proposition3.14 and local tables |
| EXC-14 | IMPORTED_RESULT_APPLICABILITY_CHECKED | EXC-02, Raynaud Corollary3.4.4 |
| EXC-15 | CHECKED_ARGUMENT | EXC-13, EXC-14, Global class field reciprocity |
| EXC-16 | CHECKED_ARGUMENT | EXC-15, Global ray class exact sequence |
| EXC-17 | CHECKED_COMPUTATION |  |
| EXC-18 | CHECKED_ARGUMENT | EXC-01 |
| EXC-19 | CHECKED_COMPUTATION | EXC-01, EXC-17, EXC-18, PVT equation32 and Proposition7.1 |
| EXC-20 | CHECKED_ARGUMENT | EXC-12, EXC-16 |
| EXC-21 | CHECKED_COMPUTATION | EXC-19, EXC-20 |
| EXC-END | CHECKED_ARGUMENT | EXC-01, EXC-02, EXC-03, EXC-06, EXC-07, EXC-10, EXC-11, EXC-12, EXC-13, EXC-14, EXC-15, EXC-16, EXC-17, EXC-18, EXC-19, EXC-20, EXC-21 |
| GLOBAL-END | CHECKED_ARGUMENT | GLOBAL-01, GLOBAL-02, GLOBAL-05, RAT-END, QUAD-END, CUBIC-END, FIELD-END, PURE-END, EXC-END |
| SCOPE-01 | CORRECTED_IN_REVIEW_DRAFT |  |
| PURE-19 | CORRECTED_IN_REVIEW_DRAFT | PURE-04 |

## Claim details

### GLOBAL-01: Primitivity is equivalent to pairwise coprimality, and variable exchange preserves signed solutions.

A prime dividing any two variables divides the third by the equation. Thus gcd=1 forbids all pairwise common primes. The change (X,Y,Z)=(y,x,z) is a bijection and preserves nonzero signs.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### GLOBAL-02: The parameter eta=X^5/Z^7 is a reduced fifth-power/seventh-power quotient outside0,1,infinity.

Z≠0 makes eta finite, X≠0 makes eta≠0, and eta=1 would force Y=0. Numerator and denominator have no cancellation, so their prime valuations are multiples5 and7 respectively.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### GLOBAL-03: The septic has one real root and discriminant squareclass -7.

The derivative105T^4(T-1)^2 is nonnegative and positive away from two isolated points, hence Phi is strictly increasing; its limits are ±infinity. The independently computed discriminant is -3^6*5^6*7^7*eta^4*(eta-1)^2, nonzero with squareclass -7.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### GLOBAL-04: The local7 degree patterns are among[1,6],[2,5],[3,4],[7].

The actual primary proposition treats all four local valuation cases, including Z divisible by7. Its algebra is the same Phi(T)-eta; no positivity hypothesis occurs.

Limits / remaining scope: The general structural-stability proof and all internal enumeration of the cited working paper are retained as literature dependencies.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### GLOBAL-05: The four displayed global sectors are exhaustive.

Every global irreducible factor splits into disjoint local irreducible factors. Each listed local pattern has at most two parts, so its only coarsenings are itself and[7]. This proves exhaustiveness, not existence of each sector.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### GLOBAL-06: Every solution-induced field has the ramification support and local algebras used in the seven-field theorem.

The solution lies in the local set defined by equation(4) at every prime, with exactly the same parameter and variable convention. The four local cases are exhaustive by primitivity. The actual stated local results therefore apply; degree and signature follow from the global polynomial. Ramification away from3,5,7 is also seen from the separable ordinary or scaled branch reductions in Proposition3.3.

Limits / remaining scope: The local classification and its structural-stability enumeration are cited mathematical inputs, not a newly rerun enumeration.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### RAT-01: A rational root gives the displayed integral-coefficient equation and quartic-cube equation.

Multiply by Z^7 and use the exact identity Phi(T)-1=(T-1)^3(15T^4+10T^3+6T^2+3T+1). The sign is -Y^3 because X^5-Z^7=-Y^3.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### RAT-02: The local restrictions and denominator bound onw hold.

The cited lemmas use the same r,w and impose no extra global sign assumption. The rational-root denominator divides15; the5-adic restriction removes5, leaving denominator at most3. Coprimality gives the stated local alternative.

Limits / remaining scope: Internal Newton-polygon enumeration remains a cited input.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### RAT-03: The norm decomposition and three cubic classes, including alpha=1 integrality, are valid.

Independent polynomial reduction verifies A^2-AB+9B^2 and all three cubic expansions. Lemma6.4 supplies the ideal-theoretic exhaustive alternatives and integrality/copimality for alpha=1.

Limits / remaining scope: The class-number and ideal-principalization argument is imported; it is not inferred from the three printed choices alone.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### RAT-04: The second cubic case has no Q2-point, including infinity.

The normalized homogeneous sextic is5 modulo8 for every primitive pair; all64 residue pairs were exhausted. A square in Q2 with unit value cannot have this residue. The v=0 case is included.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### RAT-05: The third cubic curve has only the two stated rational points.

Two fresh Magma Chabauty runs, one using a doubled negated divisor, return exactly(-2,±540); rank upper bound1 and infinite-order divisor give rank1. The leading coefficient76 is not a rational square, excluding rational infinity.

Limits / remaining scope: Trusts Magma descent and genus-two Chabauty implementation/contracts; not a proof-assistant certificate.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### RAT-06: The C3 points cannot arise from a primitive nonzero solution.

At u/v=-2, F3/G3=3. Thus Z(Z+4w)=0; Z≠0 forces r=w/Z=-1/4. Phi(r)=-491/2^14 has reduced numerator prime valuation1. No v=0 point exists.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### RAT-07: The remaining descent gives the displayed C1 sextic.

The exact identity (A-B)^2+12B^2=((Z+w)^2+3w^2)^2 gives y=((Z+w)^2+3w^2)/v^3 and x=u/v. Polynomial expansion matches every coefficient of C1.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### RAT-08: The three C1 divisors are a full Mordell-Weil basis.

Lemma6.6 identifies the same curve and divisors. The adopted exact-height reconstruction uses regulator intervals, small-prime saturation, local subgroup index72, and the exhaustive bounded search; fresh Magma corroborates the bounded points and numerical values.

Limits / remaining scope: This pass inspected the exact-height implication but did not independently rederive all class/unit, saturation, local-height and uniform h-hhat<12 premises. Those remain imported/prior-audit inputs; the floating replay alone is insufficient.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### RAT-09: Every C1 rational point lies in one of six classes modulo1080.

The cited lemma is precisely a congruence covering, not a complete rational-point determination. Its modulus2^3*3^3*5=1080 and six representatives match the manuscript.

Limits / remaining scope: The complete sieve is adopted from literature and prior replay; this row does not certify every line of its implementation.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### RAT-10: The six C1 classes imply ord3(x)≤-3 or ord5(y)≥1.

The cited local lemma has exactly this disjunction; infinity representatives use the3-adic formal group and finite representatives use the5-adic formal group.

Limits / remaining scope: The local formal-coordinate computations are prior-replayed/imported here.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### RAT-11: The v=0 descent case cannot yield a solution.

u=±1. The second equation gives w=0 or Z=-w. The former forces X=0 in the cleared equation; the latter makes -3w^2=±1, impossible for integerw.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### RAT-END: The rational-factor sector is empty.

For v≠0, ord5(y)≥1 would force the numerator divisible by5, contradicting the exact primitive mod5 check. The other arm forces27|v; then27|w(Z+w). Since3∤Z the two factors cannot both be divisible by3;27|w contradicts the r-valuation bound. Thus27|Z+w, and the first descent equation mod3 forces3|u, contrary to gcd(u,v)=1.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### QUAD-01: A quadratic factor must be Q(sqrt(-35)).

It cannot be real, since that would give two real roots. At2 a global quadratic factor must be the degree2 component of[1,2,4];[1,3,3] has no coarsening2. Thus2 is inert and unramified. The only supported negative odd fundamental discriminants with D≡5mod8 are-3,-35. The local degree2 component at7 is ramified, excluding-3.

Limits / remaining scope: Unramified support and the local2/7 classification remain explicit DS inputs.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### QUAD-02: A quadratic root and its conjugate produce a rational point ofD.

uv≠0 prevents poles in alpha. The symmetric quotient relation gives beta and gamma fixed by conjugation; the primary derivation explicitly gives the two D equations. The u+v=0 case is retained as alpha=0.

Limits / remaining scope: Full symbolic quotient construction is imported, with endpoint algebra independently checked here.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### QUAD-03: D maps to the stated genus-two curve and is covered by three fake descent classes.

Set x=alpha and y=beta*gamma. Then -35y^2=x(x-4)*quartic(x). The fresh exact Magma descent asserts equality with the three specified classes, not just their cardinality.

Limits / remaining scope: Completeness of TwoCoverDescent is a trusted Magma theorem/implementation input.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### QUAD-04: The first fake class has no nonendpoint lift toD, and x=4 is excluded.

For x=-3ta^2 and x-4=tb^2 with all nonzero, dividing the D square by(t*a*b)^2 would make3/35 a square, but its7-adic valuation is-1. Endpointx=4 requires beta^2=105. Endpointx=0 is retained separately.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### QUAD-05: The two elliptic-cover branches exhaust to x=0 or35/9.

Fresh rank3 and rank2 runs pass all independence/torsion checks. In rank3 the unchanged basis is saturated at every prime dividing the returned R; rank2 full saturation is unchanged and unresolved cosets are empty. The rational images are the asserted sets.

Limits / remaining scope: The explicit cover construction is in the cited reconstruction package; formal correctness of the Magma algorithms is not established here.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### QUAD-06: The six displayed D-points are exhaustive.

For alpha0, beta=±3,gamma=0. For alpha35/9, beta=±782/81,gamma=±1/9 independently. Direct substitution checks all six. There is no rational point above alpha=infinity on the projective completion, since gamma/alpha would square to-1/35.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### QUAD-END: No displayed D-point gives an admissible primitive power quotient.

For alpha0 the nonzero roots are ±delta/5 and eta=2401/25. For alpha35/9, exact factorization for v/u=(17+delta)/18 gives two nonzero roots; conjugation covers the other ratio. Their eta values are0 or the printed large fraction. Exact coprime factorization shows a numerator valuation1. The branch and power obstructions exclude every case.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### CUBIC-01: The two allowed cubic-quartic products share the stated quartic fieldM.

The primary proposition gives exactly the same two cubic fields and quartic polynomial under the same primitive-solution setup.

Limits / remaining scope: The completeness of the external cubic/quartic field databases used by DS is retained as a cited dependency.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### CUBIC-02: A solution in this sector gives P∈C2(k) with rational rho(P) and nonrational U(P).

The quotient is defined on the conjugate nonzero pair. Independently: Norm(kappa)=21 implies thatk is the only quadratic subfield. RationalU would give u/v∈k and u=b*sqrt(kappa). RationalPhi(u) forces b^2=-7/(5*kappa), whose norm7/75 cannot be a square. The draft inserts this omitted interface explicitly.

Limits / remaining scope: The quotient-map construction and rho function remain as cited/exact reconstructed inputs.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### CUBIC-03: The rational and twisted groups give rank3 and2A⊂H0.

Both full-group Magma computations freshly pass with named generators spanning. For everyP,2P=(P+sigmaP)+(P-sigmaP); fixed and anti-fixed terms lie in the named rational/twist subgroups. This uses actual groups, including torsion, not just eigenspaces modulo torsion.

Limits / remaining scope: The twist identification is the standard quadratic-twist descent and exact displayed model.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### CUBIC-04: A has torsion Z/10 and H0⊂H by the displayed divisor relation.

The torsion bound is distinct from rank. Injecting prime-to-residue-characteristic torsion at both good primes gives the bound10; the displayed divisor has order10. The exact relation gives H0⊂H.

Limits / remaining scope: This pass inspected the relation checker and prior independent Kummer report; it did not rerun the large divisor addition or both reduction orders.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### CUBIC-05: The finite173 Kummer characters prove thatH=A.

Exact model transformation, five simple roots, and matrix determinant were independently checked now. The prior independent entry-by-entry Kummer check supplies the matrix. Rank3 and one-dimensional2-torsion give dimA/2A=4, so H+2A=A. Since2A⊂H, A=H.

Limits / remaining scope: Individual Kummer entries are carried forward from the sealed independent audit; the false historical index inference is not used.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### CUBIC-06: Every C2(k)-point belongs to a listed class modulo2240A.

The primary lemma supplies a congruence covering of every k-point. This is not a proof that the twelve reference points are all k-points.

Limits / remaining scope: The full finite sieve is prior-replayed and imported here.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### CUBIC-07: The chosen origin neighbourhood has integral formal parameters, including at the bad prime7.

The actual primary text requires integral coefficients and a complete DVR; it does not require the polynomial discriminant to be a unit. Thus bad reduction does not invalidate this formal-neighbourhood application. Integral power-series addition and inversion preserve m^2.

Limits / remaining scope: Flynn’s universal identities and formal-group theorem are imported.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### CUBIC-08: The printed valuations imply2240A⊂G[2].

The basis transform has determinant±1 and fixes origin parameters. The printed first two parameter valuations are at least2; all nonorigin coordinates are in m^2. The torsion part is killed by2240, and closure under addition handles every integral combination.

Limits / remaining scope: The valuations themselves are prior certified exact coordinate calculations.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### CUBIC-09: The local pullback check exhausts whole residue classes, including infinity.

Fresh exact comparison proves all16 adapted coordinate identities. The independently implemented uniform tree covers all residue pairs and49 lifts per pending node; strict valuation inequalities use valid error bounds, including all18 negative-beta cases. No pending nodes remain outside the stated disks. Integral square-root series and exact leading unit coefficients treat every infinity disk. A second source review verifies all-orders error bounds and the direct limit binding of the infinity vector.

Limits / remaining scope: Imports Flynn’s universal formal-neighbourhood theorem, with its hypotheses checked at CUBIC-07; no proof-assistant formalization.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### CUBIC-10: The7-adic and23-adic conditions leave only P4,P9,P12 solution-bearing disks.

The primary local root slopes forceU≡4 and sufficientV-valuation. Mod23 the Jacobian exponent2240 identifies the reduction; rho at P10,P11 is outside F23, so those disks cannot contain a rational parameter.

Limits / remaining scope: Finite arithmetic is supported by prior replay of the inspected terminal-engine code.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### CUBIC-11: P9,P12 disks contain no additional solution-bearing point.

Two necessary equations in s1,s2 have a unit linear determinant. Higher terms have valuation at least2r for r=min valuations≥1, forcing both variables divisible by23^(2r), contradicting finite r. Conjugation covers P12.

Limits / remaining scope: Coleman coefficient accuracy and all-order integrality are imported/prior-verified; this row is the implication, not a new numerical integration.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### CUBIC-END: The final P4 disk cannot contain a solution-bearing point; sector[3,4] is empty.

The trace integral is2t1 times a unit: its higher terms have valuations at least2n-v23(2n+1)>0 for n≥1. Thus t1=0. The even inverse series makes U∈Q23∩k=Q, since23 is inert, contradiction. The reconstructed leading residue is4; the primary source’s12 is a harmless typo, since both are nonzero.

Limits / remaining scope: Uses the certified Coleman unit and integral inverse series; does not assert that every k-point has been enumerated.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### FIELD-END: Conditional on the solution-induced septic field satisfying the stated local-algebra hypotheses, Putz's theorem leaves exactly the six pure fields and the displayed exceptional field.

The displayed list matches the actual theorem, with no extra local or signature restriction omitted in the stated application.

Limits / remaining scope: The exhaustive Hunter enumeration is imported, not freshly rerun. The parent structural audit owns the local-algebra and ramification premise; this terminal alias does not certify that premise by itself.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-01: The printed curve is a smooth plane quartic over K=Q(sqrt(-7)) with a K-rational degree-one point P1.

Fresh Fraction arithmetic substituted P1 and returned zero in both basis coefficients. A fresh SymPy Groebner computation returned [1] for the quartic and all partial derivatives in each of three projective charts, at both embeddings s=237021,496156 modulo733177. These good reductions imply geometric smoothness in characteristic zero. The 15 printed coefficient rows were inspected against the manifest.

Limits / remaining scope: No claim here that every other displayed point or parameter value was recomputed.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-03: The exact source line/contact algebra gives all28 actual bitangents with the printed base embedding; the degree42/56 targets and incidence quartics represent their stated syzygetic four-subsets, and the exported tau(c) values are the actual four-incidence norms of the same literal source.

Fresh exact computations prove P is monic integral irreducible of degree56, s²=−7 and the exact source/base bindings. The universal line restriction of the actual printed quartic is a nonzero scalar times its contact quadratic squared; its28 conjugates are distinct. Smoothness and the standard28 count identify all bitangents. The actual315 conic masks are freshly determined at good reduction and identify characteristic-zero syzygies by specialization and the315 count. Both exact target polynomials are squarefree and their monic quartic J divides H28. All target nodes are distinct and every reduced J is exactly the product over the assigned four actual roots, giving the unique Hensel fibre identification. All336 contact flags have A and the conic proportionality numerator nonzero, so no product-algebra component is lost. Exact CP22=N6 and 24-term determinants of multiplication by its incidence pullback verify both tau(c) norm arrays. The additional exact export/trace join prevents substituting a different degree56 target or incidence record. No stored PASS was used to accept these identities.

Limits / remaining scope: No remaining project-specific exact geometry/export obligation in this node. Standard arithmetic implementations and the stated smoothness/BPS premises are trusted. Global coherent-root signs and other rank nodes are separate; this node does not claim a rank bound.

Detailed evidence: reviews/rank_geometry_supplement.json; see the JSON for exact locations, inputs and output records.

### RANK-04: The supplied reduced incidence structure has all315 syzygetic tetrads.

Freshly executed the inspected conic-rank checker on both reductions:28 distinct line/contact squares each; among20,475 four-subsets per embedding exactly315 have conic rank5 and20,160 rank6. All315 match supplied masks. Given the exact binding, specialization preserves characteristic-zero syzygies; the known315 count and injective reduction identify the full structure.

Limits / remaining scope: Characteristic-zero binding still inherits RANK-03.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-07: The actual descent is the BPS fake2-descent with J[2]=ker(Edual→Rdual).

Cor12.5 explicitly identifies the incidence modules and kernel; Proposition6.10 identifies line evaluation with the cohomological map. The contact-divisor interpretation and canonical polarization give the multiplication-by2 descent. The theorem does not require generic/full Sp6 or AGL image.

Limits / remaining scope: Exact-data identification remains RANK-03; this node checks the theorem specialization, not all its arithmetic premises.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-08: The ordered66-dimensional space contains every relevant global fake Selmer representative.

An independently reconstructed primitive integral quartic discriminant gives a sufficient bad-prime support set, with the correct s=15 place over29; exact inventories and38 principal generators are bound to it. K has class number1 by Minkowski. The reviewed unconditional class-number chain uses the degree21 analytic discriminant bound, ordinary quadratic ambiguous class formulas, the S4 zeta relation and independently recomputed free regulator factor2^27. Exact two-layer unit enlargement and full-rank residue characters prove v2(J)=27 and Cl(L)[2]=0. The S-unit sequence therefore supplies all28+38=66 squareclasses; BPS7.3 and10.9(a) give the required containing direction.

Limits / remaining scope: BPS, class field theory, the explicit analytic discriminant inequality and exact arithmetic libraries are imports. This pass independently reran support/determinant arithmetic and reviewed the class/unit sources and sealed fresh outputs; it did not rerun the large interval partition or every high-degree field computation.

Detailed evidence: reviews/rank_global_supplement.json; see the JSON for exact locations, inputs and output records.

### RANK-09: Each of66 local columns is the restriction of the same global generator in the actual local algebra.

All66 actual global generators are restricted, with the printed line-field and base-place identities checked. Odd coordinates are actual valuation parity and residue Euler characters. In each actual dyadic completion d=e*f+2 selected global classes have nonsingular actual Hilbert pairing, hence form a squareclass basis. Each of66 proposed coordinate combinations is tested by an exact local-square test in that completion. These462 multiplybacks certify the map independently of the approximate factor models used to discover coordinates.

Limits / remaining scope: The predyadic and actual-completion arithmetic is the sealed fresh replay whose complete source was reviewed here. Local-image completeness is a separate premise; exact number-field/local-square algorithms are trusted software inputs.

Detailed evidence: reviews/rank_global_supplement.json; see the JSON for exact locations, inputs and output records.

### RANK-02: BPS hypotheses on divisor-class representability and local degree-one divisors apply.

P1 gives a global point and a point over every completion. BPS Lemma10.2(i) gives J(k)^circ=J(k) globally and locally; Hyp11.1 is satisfied since the completion field has characteristic zero, including residue characteristic2. The printed curve has genus3 as a smooth plane quartic.

Limits / remaining scope: None for these hypotheses; descent-object identifications are separate dependencies.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-05: The exact tower defines seven intrinsic blocks; the actual theta torsor has an intrinsic Galois-stable eight-set whose separating invariant fixes an even theta characteristic, implying Galois containment in AGL3(F2).

T1(T4)=0, T3(T4)=T5 and T5²=−7 hold exactly in the actual source field; fourteen distinct simple T1 reductions across the two K embeddings prove the degree14 intermediate field and exact seven blocks of four over K. The verified full theta incidence makes the even/orthogonality condition intrinsic and Galois-stable; exhaustive enumeration gives8 candidates and56 triples per candidate. Their invariants are integral, degree at most16 over Q. The exact coefficient inequality puts every conjugate source root inside radius9, giving difference norm bound40889^16. At each embedding,28 distinct simple source roots lift correctly modulo733177^24, with the proper T5 value; freshly recomputed triangle sums separate all8 candidates and candidate0 equals−48+12w to this precision. Since733177^24 exceeds the nonzero integral norm bound, equality is exact. Its distinct invariant makes this theta Galois-fixed. The explicitly reconstructed graph and exact full stabilizer calculation give containment in AGL3(F2), not equality. These are project-specific numerical and theorem-interface checks, not reliance on a group-name field or saved flag.

Limits / remaining scope: No remaining project-specific tower/root-bound/theta identification obligation in this node. It depends on the actual geometry and standard primary results listed. The complete rank upper bound still requires its other separately audited nodes.

Detailed evidence: reviews/rank_geometry_supplement.json; see the JSON for exact locations, inputs and output records.

### RANK-06: Only containment in AGL and transitivity on28 bitangents are needed; full AGL equality is unnecessary.

An irreducible degree56 field containing quadratic K has degree28 over K, giving transitivity. The adopted finite arguments explicitly check every compatible subgroup. No later inference inspected requires full Galois-group equality.

Limits / remaining scope: The irreducibility and exact embedded K are part of RANK-03/05 input audit.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-10: The odd-place local Kummer dimensions used for stopping are valid for every compatible subgroup.

Fresh GAP enumeration produced95 AGL subgroup classes. All matches give J[2] dimensions4 at1051,2 at3,3 at5,2 at7. Independently counted fixed even-eight-coordinate classes modulo complement from exported generators, with identical results. For odd residue characteristic multiplication by2 has unit derivative, giving local quotient size equal to local2-torsion size, even at bad reduction.

Limits / remaining scope: Actual field profiles remain under RANK-09.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-14: z3=P4−P1 has f(z3)=3 lambda² in the entire local bitangent algebra at7.

The source derives Diffs[3] from the explicit P4 and P1 and the exact universal line, verifies all five points on the bound quartic, compares the full actual prime decomposition, and tests Diffs[3]/3 at every one of the seven primes with exact nfislocalpower. Clearing the integral-basis denominator by its square preserves the squareclass. Fresh sealed output and independently computed valuation/Euler columns agree. This is full semilocal fake-kernel membership, not a target-only test.

Limits / remaining scope: No unresolved local square/source-point obligation. Exact global line/field dictionary remains the explicit RANK-03/09 dependency; nonzero kernel is supplied by the separate correction calculation.

Detailed evidence: reviews/rank_p7_supplement.json; see the JSON for exact locations, inputs and output records.

### RANK-15: The selected7-adic target and incidence fields have the claimed exact identities and controlled errors.

Actual modulus coefficients are Eisenstein of degree8 with derivative valuation7. Original-target residual800 gives exact root radius793; conjugate separation1 and Krasner prove the same field. Rational input errors are bounded below by769. Coprime quadratic-block lifting gives coefficient error256; blow-up by the uniformizer square loses2, giving254 in the first unramified quadratic model. A fresh read-only diagnostic gives line numerator/denominator valuations and Gauss bounds (10,8)/(10,8) and (8,8)/(8,8), proving relative model-transfer margins254 and256. Conic values have valuations2,0 and relative error at least767. Thus the actual field/line squareclasses and the residue6 correction are stable; exact mu2 membership still comes from the cited contact identity, not numerical proximity.

Limits / remaining scope: No unresolved target/Krasner/factor/denominator-loss obligation. Exact contact and Galois-incidence interpretation remains explicit under RANK-03/16/17; the factor-degree profile alone is not used to infer a nonzero quotient character.

Detailed evidence: reviews/rank_p7_supplement.json; see the JSON for exact locations, inputs and output records.

### RANK-16: The correction formula is r(z)/(tau(lambda)*a²), and exact mu2 membership precedes sign reading.

Weight4 gives theta(a)=a². The contact relation implies the quotient squares to1; units with residues1 and−1 are distinct in odd residue characteristic. Quadratic factor norms are invariant under root-sign change. This is the precise BPS fake-kernel formula; a high-precision near-one check by itself would be insufficient.

Limits / remaining scope: Actual residue/norm values remain RANK-15.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-17: Every physically compatible7-adic target evaluation descends to Rdual(Kv)/q(Edual(Kv)).

Fresh GAP recomputation found three D8 classes, one compatible inertia each, eight carriers each. All24 annihilate the image of invariant Edual; exactly12 characters are nonzero and12 zero. Independent integer pairing from recorded generators agrees. The arithmetic value−1 must select a nonzero character; the finite profile does not prove that value.

Limits / remaining scope: Field-profile binding remains RANK-15.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-18: A genuine closed-point cycle supplies the nonzero fake image at7.

The absolute source model verifies K7(i)/K7 unramified quadratic. Applying Zoriginal=-7Zlocal to both quartic and line gives F, derivative and content valuations24,8,8; the content-normalized X derivative is a unit and Hensel changes X by at least16. For each L-component, each conjugate line valuation is at most v(A^2+B^2)-min(v(A),v(B)); the change bound v(line_X)+(e_L/2)*16 exceeds it by64,64,64,30,64,30,64, including the split incidence case. Hence the actual degree-zero Norm(P)-2P1 cycle has the exact nonzero raw squareclass vector. It raises diagonal rank2 to3 and lies in the stored allowed line.

Limits / remaining scope: No unresolved source smoothness/content-normalization/model-transport or all-component stability obligation. This proves the lower bound; full local image dimension1 also uses the separately checked domain dimension2 and nonzero fake kernel.

Detailed evidence: reviews/rank_p7_supplement.json; see the JSON for exact locations, inputs and output records.

### RANK-19: The full7-adic fake image has dimension1.

A nonzero image and a nonzero kernel in a group of order4 force each to have order2. The injection of the local Kummer kernel into the correction quotient justifies detection by the nonzero character value. Both witnesses need not come from the same generating search.

Limits / remaining scope: The implication is checked; its arithmetic witness dependencies remain open where specified.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-20: At the second dyadic place actual cycles give image rank3 and the two printed full fake-kernel relations.

Read every relevant raw point/refinement/relation calculation. Fresh checks prove the curve coefficients differ from the already identified integral model by one exact nonzero scalar. The normalized C chart has a unit d derivative at d=0; the triple chart has a unit g derivative at(0,0) and a unit e derivative at(1,0), supplying genuine unique Hensel roots for the chosen parameter disks. All three actual primes are freshly matched to idealprimedec, verified to contract to w=0, and have relative degrees4+12+12=28. Every local-square input is converted to the full integral-basis column times an exactly verified denominator square. Exhausting16 old masks and8 base squareclasses yields kernel masks0,5,11,14 and thus old image rank2. C0 has no old relation and strictly positive stability slacks58,56,28, hence supplies rank3. The P2 and P5 fresh full-component relations are respectively[1,1,-10] and[1,0,2], with slacks54,48,24 and60,56,28. Positive slacks mean each true line ratio differs from the tested truncation by a unit in1+pi^(2e+1), which is square by strong Hensel. The original scout comma bug is immaterial: the adopted C0 independent extension is established before that tracker, and full cycle relations are separately tested. No conclusion uses its unsupported second-extension state.

Limits / remaining scope: The global geometric/line identification is RANK-03; no unverified second-dyadic raw point, squareclass or component-coverage step remains in this node.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-21: The dyadic sextic/quadratic fields and square-root calculations certify correction profile(0,1).

The entire local model and strengthened source was read. New exact2-maximal models for all five factors of the target specialization have one prime each, degrees summing42. Direct evaluation of the original target polynomial in their integral bases gives residual/derivative/root-error bounds(160,12,148),(160,8,152),(320,12,308),(320,2,318),(640,6,634). Each error exceeds both its own defining-polynomial derivative bound and every cross-factor evaluation bound, so strong Hensel and Krasner identify five distinct genuine factors of the original target with profile[3,3,6,6,24]. For the two sextic carriers the checked six-element bases are locally maximal, their uniformizers have valuation1, and residue cubics are irreducible. The main arithmetic was rerun in exact truncated sextic models with a coefficient ball containing the actual target root (2^150 and2^155 on every power coefficient). The two lifted incidence factors are monic integral with resultant a unit; their product residual has target valuation64, so Hensel gives exact factors within that bound. Their lower coefficients were explicitly widened by2^28 on all six power coefficients, conservatively accounting for the basis denominators, before the final norm computation. The relative quadratics are Eisenstein or unramified with irreducible F8 reduction as asserted. True point-coordinate errors63/67 give relative line/conic errors at least118. Normalized unit-root residual/derivative pairs are(40,4) in ramified factors and(20,2) in the unramified factor, giving exact root errors36/18. Quadratic norms therefore have relative target error at least18, exceeding vA(2)=2. With the exact contact identity from RANK-03, the true obstruction is in mu2; fresh widened-input margins(19,2),(2,18) prove profile(0,1). Square-root uniqueness is neither established nor needed because changing a quadratic root sign leaves its norm unchanged.

Limits / remaining scope: Standard exact local-field/Hensel/Krasner and PARI arithmetic specifications are trusted; no remaining project-specific second-dyadic field, factor, point or sign precision step. The geometric contact identity remains the explicit RANK-03 dependency. First-dyadic image arithmetic is separate RANK-09/23 input.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-22: Both physical sextic evaluations form an independent character pair on each compatible dyadic correction quotient.

New integer linear algebra rebuilt315 tetrads, R of dimension21, and the physical42-target as affine matchings with two directions each twice. For all28 exported compatible groups it gave dimJ[2]=1, correction dimension2, and two descended sextic characters of rank2. Inspected envelope enumeration: Sylow conjugacy covers wild2-subgroups; a tame cyclic odd complement and a normalizing Frobenius cover finite local decomposition groups.

Limits / remaining scope: The28-group data were independently checked, but the full dyadic enumeration was inspected rather than regenerated in this pass; field profiles remain RANK-21.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-FIRST-DYADIC: The first dyadic allowed matrix is the full fake local image, of dimension4.

At w=1, [2:46:1] lifts to a true point with X error of valuation9. Strict line estimates preserve squareclasses in every actual completion. Three diagonal classes, four exact global differences and the true local point are verified against RANK09 bases. Their total rank7 minus diagonal3 proves fake-image dimension at least4. The independent finite local group bound gives at most4, hence equality. The upper bound is now explicit: fresh exhaustive enumeration of all95 AGL3(F2) subgroup classes gives five classes with the actual first-place orbit degrees[4,6,6,12], and every one fixes a one-dimensional subspace of J[2]. Thus the genus3 Q2 local quotient has dimension3+1=4 by BPS11.6.

Limits / remaining scope: The actual points/columns were replayed in the sealed audit and source-reviewed here; the complete local-torsion subgroup enumeration was rerun in this pass. Strong Hensel and the local Kummer dimension theorem remain imported.

Detailed evidence: reviews/rank_global_supplement.json; see the JSON for exact locations, inputs and output records.

### RANK-23: The second-dyadic image is exactly3-dimensional and the first dyadic cut also uses a complete image.

The dyadic local Kummer group has order2^(3+1)=16. At place2 the actual image subgroup has order8 and the detected kernel at least2, so both are full. At place1 four independent actual images already attain16 and suffice. No point-search exhaustion beyond these size equalities is needed.

Limits / remaining scope: First-dyadic actual rank4 witness is now an explicit parent supplement dependency RANK-FIRST-DYADIC; second-dyadic arithmetic is RANK20/21. No extra local stopping hypothesis remains.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-24: The global comparison correction is1-dimensional and the common root ratio is its nonzero class.

Fresh95-subgroup GAP enumeration found all four transitive cases of orders56,168,168,1344. In each, Edual invariants=0, Rdual invariants=1 and the AGL common ratio remains nonzero. Independent integer recomputation also gave J[2](K)=0 for each representative. Hence full AGL equality is unnecessary.

Limits / remaining scope: Identification of the actual coherent root ratio inherits RANK-25.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-33: At5 the actual chosen cycle P2+P4−2P1 has f(z)/(c(s−1)/2) square in all11 bitangent completions; four actual point images span a3-dimensional fake image.

K has exactly one unramified quadratic completion at5. Fresh idealprimedec of the degree56 field yields11 primes with relative degrees totaling28. At odd residue characteristic each local squareclass is completely specified by valuation parity and its unit residue Euler character. The two diagonal generators5 and(s−1)/2 span the base squareclasses, with the latter nonsquare mod5. Exact f(z)/(c(s−1)/2) has zero coordinates in all22 rows and is separately tested with nfislocalpower at all11 primes after an exact denominator-square normalization. Five points satisfy the quartic and have nonzero gradients; line evaluations are nonzero. Exact reconstruction of c from N6 equals CP22. Thus this is the actual cycle used by the p5 obstruction, not only an unspecified preimage or selected-target square.

Limits / remaining scope: The line/curve interpretation is explicitly upstream RANK-03; no all66-generator or other-place claim is made.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-25: The literal c has exactly two coherent global lifts modulo the comparison kernel.

Freshly evaluated the exact42- and56-target root blobs: each root squares to its recorded exact norm, with full coefficient equality to the norm/provenance arrays. The identification of those arrays with the actual four-incidence tau(c) is explicitly RANK-03, and c=N6=CP22 is RANK-33. At the odd split prime733177, all source coordinates and denominators are reduced directly and nonzero; every one of196 root reductions is evaluated from its exact algebra element and checked against the corresponding incidence product. Under the target/mask identification in RANK-03/05, each relation quotient is exactly in mu2 before reduction, so its residue detects its exact sign. The relation-sign rule is multiplicative on the binary kernel because the squared root identities cancel overlaps. The freshly reconstructed98 columns have rank21 and77-dimensional relation kernel; all77 basis quotients are+1. They therefore define a well-defined lift on all ofR, not merely a square tau(c). The entire315 extension and423360 transports per embedding were rerun; exact algebra elements defined overK supply the Galois transport on the98 input carriers, and kernel independence supplies the extension. The common whole-orbit sign solutions are exactly00 and11; both exact root42 signs used at5 thus belong to coherent global lifts. Their ratio is−1 on all98 spanning carriers, hence a nonzero invariant functional onR. RANK-24 gives zero Edual invariants and a1-dimensional correction quotient for every possible actual transitive group, so this ratio represents its unique nonzero class and exhausts the two lifts. No Sha1-vanishing or generic-full-Galois assumption is inserted.

Limits / remaining scope: No remaining project-specific coherent-root/finite-relation step. Global source/target/bitangent identifications RANK-03 and actual theta/Galois embedding RANK-05 remain explicitly upstream and are being audited separately; this conditional status does not discharge them or the class/unit/support bounds.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-26: The local fake kernel at5 is zero, so the full finite correction quotient is W5.

An image of dimension3 from a3-dimensional domain forces injectivity. Therefore the quotient by the local fake-kernel correction removes nothing. This is necessary: nonzero restriction into the unreduced correction quotient alone would not otherwise prove zero global Selmer comparison kernel.

Limits / remaining scope: No further project-specific local5 image check remains after RANK-33. The geometry/Galois premises remain explicit upstream dependencies.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-34: Every compatible p5 local group gives a2-dimensional correction quotient with the physical rq1/rq2/rq3 characters satisfying chi1=chi3 and rank(chi1,chi2)=2.

There is no wild inertia because5 does not divide1344. Tame inertia is cyclic, and the verified source ef profile with maximal ramification2 forces its faithful action to have order2. Frobenius commutes with it because the base residue size25 is1 mod2. Enumerating all such inertia/Frobenius pairs is therefore exhaustive. Every compatible group has lifted Rdual invariant dimension16, denominator dimension14 (after subtracting the7-dimensional ambient kernel:9 and7), correction quotient2, and J2 invariants3. Among all physical carrier assignments respecting one ramified and one unramified quadratic component, each case has exactly the required assignment, chi1=chi3 and independent chi1,chi2. Using only target factor degrees still gives84 cases. The extra split+split carrier fails character descent and is rejected in all84 cases.

Limits / remaining scope: The actual global theta/target embeddings remain explicit upstream hypotheses. No further finite group enumeration remains for this local statement.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-27: The two coherent lift obstructions at5 are(1,0) and(0,1), differing by(1,1).

The exact chosen local source is now RANK-33. The norm-first computation uses genuine degree2 local components: the ramified model is Eisenstein (v(C)=1,v(D)>=1), while the unramified model has unit nonsquare discriminant. For G²=C+DG, Norm(A+BG)=A²+ABD-B²C. At a ramified quadratic component the residue of the norm of a unit square root is the square-root-square residue; at an unramified quadratic it is rbar^(25+1). The uniformizer norm contributes the recorded scale. These residue choices determine the correct square root of Norm(S), independent of sign of the local lambda root. Fixed-inverse iteration is valid because the normalized derivative2*n0 is a unit and final residuals are checked; all six residuals imply relative root errors at least21. Norm valuation1 is allowed and explicitly accounted for. Exact contact and global-root identities (RANK-03/25) force the target obstruction into mu2; the three computed signs are separated from the opposite sign at valuations22,21,22, while propagated target precision is at least35. Each exact absolute incidence norm divides the squarefree source polynomial under RANK-03. Enumerating every degree8 subset product (19 possibilities) finds the selected product uniquely modulo5, with agreement39–41digits and every competitor distance0. Thus the carrier association no longer relies on a potentially misleading factorization of an inexact intermediate. RANK-34 supplies the actual quotient coordinates: signs(-,+,-) give(1,0); reversing the coherent root gives(0,1). Standard PARI exact number-field/factorpadic/finite-precision arithmetic specifications are trusted, not re-proved internally.

Limits / remaining scope: Local project-specific algorithm, carrier identification, character coordinates, chosen source and precision implications are checked. The exact global contact/target binding RANK-03 and coherent global lift association RANK-25 remain open; this local status does not close them.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-11: The sampled images at the four split primes,1051,3 and5 are complete.

A map from a finite2-vector space cannot have image dimension exceeding its domain. The verified independent images reach6 at split primes,4 at1051,2 at3 and3 at5; therefore equality forces the whole image and zero fake kernel. No unproved exhaustiveness of a point search is needed once this dimension equality holds.

Limits / remaining scope: Actual cycle/squareclass ranks still depend on arithmetic review RANK-09; no claim that stored ranks alone prove existence.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-12: The supplied matrices cut66 dimensions to46,28,24,23,22,20,19,18,15,12.

New integer-only elimination constructs annihilators of every allowed column space and composes them with each66-column raw map. The resulting stage dimensions were recomputed and match exactly. Dropping other prime/norm conditions cannot discard true classes, and this route already supplies the stated final containing space.

Limits / remaining scope: Arithmetic interpretation inherits the referenced map/image nodes.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-13: Modulo the seven-dimensional diagonal, the final containing quotient is exactly B direct-sum<c>.

New integer calculation gave ranks7,11,12 for diagonal; diagonal+four point columns; and those columns+literal c. Every column lies in the reconstructed12-space, so equality follows. This proves actual row-space equality rather than merely equal dimensions.

Limits / remaining scope: Exact field-to-coordinate identities and diagonal completeness inherit RANK-08/09.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-28: The5-adic obstruction excludes both lifts and proves the true-to-fake Selmer comparison kernel is zero.

The functional(u,v)↦u+v vanishes on the global correction image but equals1 on either obstruction. Both lifts fail local Kummer membership. Nonzero restriction of the sole global correction generator implies ker(kappa)=0. One place suffices; no computation of Wv at every other place is needed for these two negative conclusions.

Limits / remaining scope: Witness dependencies remain open; the exact-sequence implication itself is checked.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-29: All true Selmer classes map into B, and dimSel2(J/K)=rankJ(K)=4 with Sha[2]=0.

A true Selmer class over c+b minus the global Kummer class of a point mapping to b would be a locally Kummer lift of c, contradiction. Injectivity gives dimension≤4. The known four-dimensional fake point image implies dimJ(K)/2J(K)≥4; with J(K)[2]=0 this gives rank≥4. Kummer exactness then forces equality and Sha[2]=0. No assumption that every element of the containing space is a fake Selmer class is used.

Limits / remaining scope: This is a checked implication with open upstream input-verification nodes, not a closed certification of the final rank theorem.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-30: H0 has finite odd index in J(K).

The four point classes form a basis of J(K)/2J(K). They are independent in the torsion-free quotient, so H0 has finite index. For F=J(K)/H0, surjectivity modulo2 gives F/2F=0; finiteF therefore has odd order. This also shows why no claim of5-saturation of H0 follows.

Limits / remaining scope: No further abstract index step remains; arithmetic hypotheses remain upstream.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-02: The generic degree15 Fano cover and degree120 unordered compatible-pair cover have the claimed monodromy, indices and passports.

h_t has derivative7V^4(V−15)^2, critical values0,1 and an order7 pole. Every possible generating5/3-cycle pair in the program generates A7; the discriminant adds the nontrivial quadratic constant extension. The unordered-pair stabilizers are actual normalizers, not groups identified by size alone. Riemann–Hurwitz gives genera3 and20.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-03: The printed R+ is the genuine irreducible Fano orbit polynomial with coordinate q=M/225.

The degree bound floor(3k/7) follows from root growth. Integer alternating coefficients factor through the Vandermonde, making the U/W reconstruction integral before scaling. The Cauchy and seven-node interpolation bound applies to every coefficient. A separating fibre shows no invariant-sheet collapse, and A7 transitivity then gives irreducibility.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-04: The explicit quartic is smooth and isomorphic to the smooth projective Fano model, preserving t.

Recovering both q and t makes the induced function-field map an isomorphism. Nonconstant t ensures the image is the whole smooth quartic. Proper smooth projective models extend this isomorphism across zeros of coordinate denominators. Smooth reduction at23 excludes a geometric generic singularity; a smooth plane quartic is geometrically irreducible and has genus3.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-06: The global divisor construction supplies E and the exact relation5E=D3+D4+3D5.

A=(t)_0/5 is a K7-rational effective degree3 divisor. With B=[A−3P1],5B=7D3+7D4+D5. Therefore E=3B−4D3−4D4 has the claimed relation. This is an existence construction, not an unsupported division by5. Since pole orders7+7+1 exhaust degree15, there are no omitted poles.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-07: H0 and H1 are2-saturated; H1 is5-saturated, without using a global rank upper bound.

Four independent characters kill2J, respectively5J, and force all subgroup coefficients of an element in ell J to be divisible byell. Thus H intersect ell J=ell H; absence of ell-torsion gives ell-saturation. At the character places, exact full orders and independently distinguished subgroup sizes prove the character domain is the whole two/five-primary part. Proper local subgroups at other sieve primes are not used to invent global characters.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-31: H1 contains H0 and is5-saturated with index coprime400.

The relation gives D3=5E−D4−3D5, hence H0⊂H1. Thus J/H1 has odd order. If the four mod5 images are independent and the local maps factor through J/5J, rank4 gives5-saturation; J/H1 then also has order prime to5, so it is coprime400. An order25 target alone is insufficient unless its reduction/quotient is correctly a map on J/5J; that arithmetic interface belongs to the downstream branch.

Limits / remaining scope: Link to the downstream audited E/divisor relation and exact5-saturation map predicates; do not infer it from determinant4 alone.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-32: H1 covers J(K)/400J(K), while logarithmic annihilators of H0 are global.

Multiplication by400 is an automorphism of the finite quotientJ/H1, hence J=H1+400J. For anyP, some nonzero integern has nP∈H0; nL(P)=L(nP)=0 implies L(P)=0 in characteristic zero. These implications require no saturation at other primes and no division by a p-adic unit.

Limits / remaining scope: Construction and certified precision of the logarithmic functionals themselves belong to downstream review.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### RANK-END: The assembled descent gives the rank-four conclusion and the stated downstream H0/H1 consequences.

The parent merged the exact geometry, global support/class/unit, actual restriction,7-adic and both dyadic reviews with the coherent-root and p5 character computations. Every project-specific open dependency in the rank branch has a reviewed replacement. The terminal BPS and Mordell–Weil implications and downstream saturation relation are assembled from these explicit premises.

Limits / remaining scope: The closure is a reviewed computational argument with imported mathematics and software. It is not proof-assistant verification or an external human specialist review.

Detailed evidence: reviews/rank_descent_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-01: Each of the six pure septic fields has normal closure F42 and quadratic subfield Q(sqrt(-7)).

Eisenstein at5 gives degree7. Its compositum with Q(zeta7) has degree42, since degrees7 and6 are coprime, and is the splitting field. The quadratic subfield of Q(zeta7) is Q(sqrt(-7)); the cyclic order7 normal subgroup yields no additional quadratic quotient.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-05: Every pure-field specialization with rational t outside0,1,infinity gives a K7-point on C+ with that same t.

The specialized F42 has a unique Sylow7 subgroup and, on seven roots, equals its normalizer. It fixes a conjugate compatible-pair sheet, hence a rational point of the finite etale quotient fibre. After base change to K7 the chosen parity orientation defines the forgetful map. Normalization and the smooth-projective isomorphism cover all coordinate-chart failures; no affine denominator restriction is imposed on the hypothetical point.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-11: Both23-adic curve charts and the printed differential evaluations meet the good-reduction hypotheses.

23 is odd and unramified in K7 and splits as4/19. Both plane reductions are geometrically smooth. Every reference point is in X=1 with Q_z a unit, so y−y(Pi) parametrizes its entire disk and(1,y,z)dy/Q_z is the compatible integral regular differential basis. In particular the points labelled t=infinity do not require an omitted affine chart.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-12: All four actual divisor-class logarithms at both23-adic places are reconstructed with the stated precision.

Here d0=6≥g+1=4. The validated lattices and unit minors give the local-ring versions of the field operations without hidden division by23. The divisor matrices represent D0+Pi−P1, so the class sign is correct. A unit scalar moves each class into the formal neighborhood; decoded divisors give the sum of local integrals divided by that scalar. Integral differential tails k−v23(k) bound truncation, and precision10 gives9 digits after dividing the logs by23. Old D4 caches serve only as comparisons.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-08: H1 has finite index prime to400 and provides a common coefficient vector for the sieve.

The four logarithm columns show H0 has rank4; the rank upper bound makes its index finite. Its2-saturation makes the index odd. H0 is contained in H1, and H1 is5-saturated, so [J:H1] is prime to2 and5. H0 itself need not be5-saturated and is never used as the corrected mod400 basis. Surjectivity H1→J/400J follows.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-09: The finite tables give necessary simultaneous constraints on every global curve point, even where only projected point images rather than a full local group order were reconstructed.

Write n[P−P1] as an integer combination of H1. Its coefficient vector multiplied by n inverse mod400 works at every selected place. On the actually checked primary point images and generator images multiplication by n is invertible. This proves the needed common-vector condition without assuming an uncomputed whole-Jacobian order at every large prime. It also justifies discarding point images proved outside the known local subgroup.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-10: The exhaustive coupled sieve leaves592 mod16,1252 mod25,144 mod400 classes and exactly the five stated ordered residue pairs at23.

All16^4 and25^4 vectors and all compatible pairs are considered. The corrected coefficient map is(a,e,c,d)→(a,13e,c+13e,d+39e) mod16. At each point, rational t requires equal projective reductions when both are defined by the printed forms. A simultaneous zero is retained as unknown, so the false branch-only base-locus sentence is not used by the filter. The resulting five pairs are verified on coordinates, not inferred merely from matching counts.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-13: Two exact global annihilator rows exist and kill all of J(K7), not just H0.

The unit block remains invertible over Z23, so its exact lift defines an exact annihilator whose computed reduction is certified. If nP lies in H0, then n L log(P)=0; characteristic zero gives L log(P)=0. Torsion is killed automatically. Neither knowledge of the full index nor23-saturation is required.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-14: Siksek Theorem2 applies to the four regular product disks.

Here d=2,g=3,r=4,h=2. The checked matrices are precisely the two-place differential evaluation matrices followed by the integral annihilator. All required hypotheses, including the product of both residue disks, are met.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-15: The four regular product disks contain no extra common Coleman zero.

A unit2×2 linear term and integral higher terms give uniqueness on each entire product residue disk centered atP2,P3,P4,P5. The reference point is an exact zero because its divisor class is global. This is an exhaustion argument on disks, not a finite sample of local points.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-16: The whole P1 product disk contains exactly two common Coleman zeros, one being P1.

With local parameters23u,23v, divide the first annihilator integral by23 and the combination(second−6first) by23². These are integral restricted power series, and the divisions do not discard zeros. Their reductions are2u+4v and21u+6v+14u²+21v². They have exactly(0,0),(14,16), with determinants20,3. Multivariate Hensel uniqueness/existence in each residue pair and complete residue enumeration cover the entire Z23² domain.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-17: The second P1 Coleman zero has unequal split-place t-values, rigorously excluding rational t.

Coefficients modulo23^9 and two normalizing divisions yield equations modulo23^7; omitted integrated terms k≥12 have valuation at least12 before those divisions. The root therefore determines coordinates modulo23^8. Unit denominators preserve that precision for t. Values59233664629 and24239267738 differ with exact valuation5 and first digit9, also independently checked in this audit. Equality of rational t in the two embeddings is impossible.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-18: The rational-parameter locus is exactly P1,…,P5.

The sieve forces any rational-parameter point into a reference product disk. Four disks are unique by the regular criterion. The P1 disk has its reference zero plus one extra zero excluded by unequal t. Conversely the five exact K7-points have rational values0,1,infinity,infinity,infinity. The argument claims neither that the extra zero is global nor that all C+(K7) points have rational t.

Limits / remaining scope: None within this claim; upstream dependencies retain their separate scope.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-END: None of the six pure fields in the seven-field enumeration can arise from a nonzero primitive solution.

The pure-field specialization forces a K7-point on C+ preserving eta. The rational-parameter theorem restricts its value to0,1,infinity, contradicting nonzero primitive input. The separate ancillary base-locus correction PURE-19 is required in the text but is not a premise of this elimination.

Limits / remaining scope: The FIELD-END and RANK-END claims remain owned by the other reviewers; this report does not replace their audits. Apply PURE-19 wording correction.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-01: The manuscript's solution maps to the PVT plus-Frey specialization at t0=eta/(eta-1).

Since p=7 is odd, X^5+(-Z)^7+Y^3=0; eta-1=-Y^3/Z^7, giving the stated parameter. Nonzero coordinates exclude t0=0,1,infinity.

Limits / remaining scope: No unresolved project-specific obligation identified for this claim; cited general results remain imports.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-02: The weight-two plus realization is modular, has cyclotomic determinant, is residually unramified outside 3,5,7 and finite flat above 7.

These theorem statements apply to this rational specialization and p=7. The small prime is not excluded. The curve/count realization uses the weight-two Tate normalization.

Limits / remaining scope: Optional clarity edit: name the weight-two realization explicitly. This is not an unresolved determinant or modularity gap.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-03: If the residual representation is irreducible, it comes from a trivial-nebentypus parallel-weight-two newform at one of the four displayed levels.

All hypotheses of the theorem actually cited in the paper are satisfied; it does not impose a large-p or p!=7 condition.

Limits / remaining scope: No open Breuil–Diamond applicability gate in the present argument. A separate direct application of BD would require irreducibility on G_{F(zeta7)}; that alternative was not asserted or independently proved here.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-04: The quaternion order, its complete projective unit group and all 20 neighbour sets used by the Brandt generator are the required exact objects.

The finite norm equations bound every twice-coordinate by 2, proving enumeration completeness. Lattice discriminant implies relative reduced discriminant1. N(q)+1 distinct residue images exhaust neighbours; at2 exact right-unit inequivalence handles the five neighbours.

Limits / remaining scope: The code's PASS is supported by the checked completeness argument; no ideal-class completeness is inferred until EXC-05.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-05: The displayed maximal quaternion order has ideal class number one, so the orbit-function model has no missing ideal classes.

The principal class contributes 1/60 and the total mass is 1/60. Every class has positive mass, so none is omitted.

Limits / remaining scope: No fresh Hunter or general ideal-class algorithm is being claimed; the standard mass theorem plus exact arithmetic proves completeness.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-06: Every level-lowered eigenform has a nonzero reduction in the computed cuspidal Brandt lattice, after coefficient-field extension if necessary.

Transfer in characteristic zero, scale a nonzero eigenvector to be primitive in the local lattice, and reduce. The mass equation and all Hecke equations persist; kernels commute with scalar extension. Old/new subtraction and integral JL are unnecessary.

Limits / remaining scope: No unresolved project-specific obligation identified for this claim; cited general results remain imports.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-08: At inert auxiliary primes13 and17, every relevant residual trace is scalar in F7, so T^7-T is a valid filter.

For semilinear rational Frobenius A sigma, trace(A sigma(A)) is sigma-fixed by cyclicity of trace. Good boundary realizations obey the same identity; multiplicative level-lowering traces ±(p^2+1) are scalar.

Limits / remaining scope: Rational origin alone would not imply this assertion; the checked RM Galois compatibility is essential. No missing inert-prime case remains.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-09: Replacing the unsound131 condition by T^49-T preserves every required Frey eigenvector.

The historical A131 omits1=-132 mod7. T^49-T vanishes on every F49-valued trace, hence annihilates the required eigenvector.

Limits / remaining scope: Replace literal 'no-filter' wording by 'no additional restriction on F49-valued Frey eigenvalues'; it is not an identity condition on arbitrary nilpotent directions or larger residue fields.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-07: The local filter list covers ordinary, degenerate and level-lowering trace alternatives at every required auxiliary prime.

All p-2 ordinary values are exhausted at18 required primes, and all five/three boundary characters at the16 split primes. Relative extension squares Frobenius, giving a^2-2p; ordinary data already over F must not be pulled back again. Both signs N(q)+1 are included.

Limits / remaining scope: Precision improvement: manuscript986–989 should distinguish parsing/reducing6253 upstream polynomials at37 primes from independent point-count reconstruction of1264 ordinary cases at18 required primes.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-10: The exceptional field forces Z odd, making the two prime-2 parity alternatives exhaustive.

If2|Z, the integral U-polynomial reduces to the separable U7+1 with degrees1,3,3, incompatible with the exceptional field's1,2,4. Thus exactly one ofX,Y is even.

Limits / remaining scope: Added in corrected draft. The original snapshot omitted this explanation; its proof is now supplied without changing the required arithmetic.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-11: The review draft correctly assigns Y-even to trace−1 and X-even to trace0 in X^5+Y^3=Z^7.

The source cube variable is the manuscriptY. Swap the sentence and row labels; keep1,2,2,5 with trace−1 and2,10,3,11 with trace0. Both branches were already retained, so the36-occurrence union and terminal exclusion are unchanged.

Limits / remaining scope: The frozen original and published sealed release still contain the original wording. The corrected draft is a distinct artifact.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-12: The four filtered cuspidal modules and all T2-compatible eigenvalue supports are completely accounted for.

Commutativity, full factor-kernel dimensions and total dimensions prove coverage. Independently, T(T+2)(T2+5T+2)(T2+3T+4) annihilates T29 on both scalar-T2 eigenspaces at every level. No old/new quotient is used.

Limits / remaining scope: An eigensystem-signature merger would be a harmless superset. This claim concerns necessary eigenvalue support, not a complete characteristic-zero newform classification.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-13: A reducible constituent has conductor exponent at most1 at3 and5 and is unramified at other finite primes away from7.

Inertial characters are inverses away from7, so their conductor exponents agree. Twice the constituent exponent equals the semisimplified conductor, which is at most the original≤3. The earlier nonsplit equality error is correctly repaired.

Limits / remaining scope: No unresolved project-specific obligation identified for this claim; cited general results remain imports.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-14: Finite flatness permits exactly the four level-two constituent inertia characters1,omega2,omega2^7,omega2^8.

The coefficients7 are inert/unramified in F. Wild inertia maps trivially to Fbar7*, and full local Frobenius forces tame level≤2. Raynaud then gives the four indicated digits.

Limits / remaining scope: No unresolved project-specific obligation identified for this claim; cited general results remain imports.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-15: Global reciprocity excludes both mixed inertia characters, leaving a constituent unramified at7.

At every place except7 the unit's value is trivial by conductor/sign conditions. At7 the mixed cases give−1, contradiction. The remaining equal-digit cases allow one constituent unramified there.

Limits / remaining scope: No unresolved project-specific obligation identified for this claim; cited general results remain imports.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-16: The relevant narrow ray group is C4×C2 and its29-prime class gives exactly trace support±2.

Unit relation quotient has invariant factors4,2. Alpha² is epsilon² mod the modulus and alpha cannot be a positive unit modulo3; thus class order2. Since29=1mod7, reducible traces are±2.

Limits / remaining scope: No missing ray character or archimedean sign branch identified.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-17: For ordinary29-adic parameters the exceptional factor pattern allows exactly eta10,14,24,28.

Comparing the actual squarefree reductions at all27 ordinary parameters gives precisely the four displayed values.

Limits / remaining scope: No unresolved project-specific obligation identified for this claim; cited general results remain imports.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-18: No branch residue0,1,infinity at29 has the exceptional factor pattern.

X- andY-divisible branches give1,1,1,2,2; Z-divisible branch gives split7 or irreducible7. Each scaled reduction is separable. None is1,3,3.

Limits / remaining scope: No unresolved project-specific obligation identified for this claim; cited general results remain imports.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-19: The four count-derived polynomials correctly annihilate both conjugate RM Frobenius traces mod7.

The genus-two coefficient identities give sumA and productB−58 for the RM traces. The table records these norm polynomials, not degree-two Frobenius characteristic polynomials. Both conjugates are covered.

Limits / remaining scope: No unresolved project-specific obligation identified for this claim; cited general results remain imports.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-20: The six terminal factors cover all irreducible and reducible trace alternatives, including the conjugate29-prime convention.

The ambient T+2 factor is T−5, and T2+3T+4=(T−2)^2. Reducible±2 usesT−2,T−5. Changing to the conjugate prime permutes trace conjugates and preserves the endpoint.

Limits / remaining scope: No unresolved project-specific obligation identified for this claim; cited general results remain imports.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-21: All24 resultants are nonzero and therefore exclude every common trace in Fbar7.

Nonzero resultants imply coprimality overF7 and no common root over its algebraic closure. Repeated factors create no exception.

Limits / remaining scope: No unresolved project-specific obligation identified for this claim; cited general results remain imports.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### EXC-END: A solution-induced exceptional field is incompatible with both residual irreducibility alternatives.

Every2-dimensional residual representation is reducible or irreducible. In either case its29-trace must satisfy a curve polynomial and a terminal factor, contradicting EXC-21.

Limits / remaining scope: No unresolved exceptional-specific mathematical gap found after the supplied correction. This deduction does not re-prove imported theorems, Putz's enumeration, the structural field premise, or other sectors; dependencies remain explicit.

Detailed evidence: reviews/exceptional_claims.json; see the JSON for exact locations, inputs and output records.

### GLOBAL-END: The four sector exclusions imply the main nonexistence theorem.

A hypothetical solution has exactly one of the four sectors. Reducible branches contradict the first three terminal claims. The irreducible branch is one of seven fields; pure and exceptional terminal exclusions cover that list. This is a valid conditional composition, not a claim that all dependencies have been certified in this pass.

Limits / remaining scope: None specific to this row.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### SCOPE-01: The review draft records the dated seven-input Magma replay separately from the immutable release and preserves the exact-height limitation.

The14September audit statement was historically accurate. A current review draft must distinguish it from the new seven-run replay. Both trust-boundary paragraphs are updated without rewriting the old release.

Limits / remaining scope: The frozen original and published sealed release still contain the original wording. The corrected draft is a distinct artifact.

Detailed evidence: reviews/global_reducible_claims.json; see the JSON for exact locations, inputs and output records.

### PURE-19: The rational parameter extends uniquely across common quintic zeros after cancellation; the finite sieve retains ambiguous reductions. The false branch-only base-locus assertion is removed.

The special base scheme has length5 and no X=0 point. Generic common-base degree is20−15=5; therefore the finite scheme is flat overZ23. Its simple rational point lifts etale to a genuine generic base point. The local leading coefficients G=5u+…,H=9u+… give t=2 mod23, outside0,1,infinity. This is a false ancillary mathematical/scope statement, not a failure of the normalized t-map or the conservative sieve.

Limits / remaining scope: The frozen original and published sealed release still contain the original wording. The corrected draft is a distinct artifact.

Detailed evidence: reviews/pure_parameter_claims.json; see the JSON for exact locations, inputs and output records.

## Imported mathematics and software

- BPS:10.14: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:10.2: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:10.9a: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:11.6: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:12.1: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:12.2: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:12.3: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:12.5: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:5.1: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:5.4: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:5.5: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:5.7: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:6.10: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:6.3: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:7.2: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:7.3: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:9.2: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:A13: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:A14: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:A24a: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:A24b: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:A26: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:Hyp10.1: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- BPS:Hyp11.1: Primary statement and applicability reviewed; general theorem is imported. Source: https://math.mit.edu/~poonen/papers/genus3.pdf
- DAndreaDickenstein:MacaulayResultant: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: https://arxiv.org/pdf/math/0007036
- DS:Corollary3.4: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Lemma6.4: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Lemma6.6: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Lemma6.7: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Lemma6.8: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Lemma7.2: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Lemma7.3: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Lemma7.4: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Lemma7.6: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Lemma7.7: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Lemmas6.2-6.3: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Proposition3.5: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Proposition4.3: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Proposition5.1: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Proposition7.1: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:Propositions3.6-3.7: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- DS:UnramifiedSupport: Working-paper result and applicability adopted as described in its claim row; internal classification/sieve/rank computations are not all independently re-proved in this pass. Source: https://few.vu.nl/~sdn249/GFE357.pdf
- Dembélé–Voight Theorem 3.9 and §4: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: https://jvoight.github.io/articles/hmf-crm-bcn-053024.pdf
- Doud:Theorem2.4: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: https://mathdept.byu.edu/~doud/Papers/Local.pdf
- Eichler maximal-order mass formula, Voight Theorem 26.5.4: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: https://jvoight.github.io/quat-book.pdf
- Flynn:Corollary2.2: Universal identities and integral formal-neighbourhood theorem imported; the bad-reduction applicability and specific coordinate/precision claims were checked. Source: https://people.maths.ox.ac.uk/~flynn/arts/art2.pdf
- Flynn:Theorem3.5: Universal identities and integral formal-neighbourhood theorem imported; the bad-reduction applicability and specific coordinate/precision claims were checked. Source: https://people.maths.ox.ac.uk/~flynn/arts/art2.pdf
- Global class field reciprocity: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: See applicable sector review and cited mathematical framework.
- Global ray class exact sequence: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: See applicable sector review and cited mathematical framework.
- Magma:EllipticChabauty: Exact unchanged-input rerun with returned hypotheses/results checked; Magma internals are not independently implemented or formally certified. Source: Fresh Magma replay addendum, official calculator V2.29-10.
- Magma:Saturation: Exact unchanged-input rerun with returned hypotheses/results checked; Magma internals are not independently implemented or formally certified. Source: Fresh Magma replay addendum, official calculator V2.29-10.
- PVT Corollaries3.6,3.11, Proposition3.14 and local tables: Primary result and its p=7/field/normalization hypotheses reviewed in exceptional.md; general proof is imported. Source: https://arxiv.org/abs/2512.17845
- PVT Theorem 7.8: Primary result and its p=7/field/normalization hypotheses reviewed in exceptional.md; general proof is imported. Source: https://arxiv.org/abs/2512.17845
- PVT Theorems 2.1 and 2.4(1), Remark 2.2: Primary result and its p=7/field/normalization hypotheses reviewed in exceptional.md; general proof is imported. Source: https://arxiv.org/abs/2512.17845
- PVT equation32 and Proposition7.1: Primary result and its p=7/field/normalization hypotheses reviewed in exceptional.md; general proof is imported. Source: https://arxiv.org/abs/2512.17845
- PVT §2.2 and §7.1 RM realization: Primary result and its p=7/field/normalization hypotheses reviewed in exceptional.md; general proof is imported. Source: https://arxiv.org/abs/2512.17845
- PVT §7.4: Primary result and its p=7/field/normalization hypotheses reviewed in exceptional.md; general proof is imported. Source: https://arxiv.org/abs/2512.17845
- Putz Theorem 3.50: Complete seven-field classification imported after matching its hypotheses; the entire classification is not recreated here. Source: See exact thesis artifact in FIELD-END evidence.
- Raynaud Corollary3.4.4: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: https://www.numdam.org/article/BSMF_1974__102__241_0.pdf
- STANDARD:AnalyticClassNumberFormula: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: See applicable sector review and cited mathematical framework.
- STANDARD:ClassFieldTheory: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: See applicable sector review and cited mathematical framework.
- STANDARD:DirichletUnits: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: See applicable sector review and cited mathematical framework.
- STANDARD:FiniteAbelianGroups: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: See applicable sector review and cited mathematical framework.
- STANDARD:KummerExactSequence: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: See applicable sector review and cited mathematical framework.
- STANDARD:LocalSquareclasses: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: See applicable sector review and cited mathematical framework.
- STANDARD:Minkowski: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: See applicable sector review and cited mathematical framework.
- STANDARD:MordellWeil: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: See applicable sector review and cited mathematical framework.
- STANDARD:StrongHensel: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: See applicable sector review and cited mathematical framework.
- Siksek:Theorem2: Theorem2, p776: the general number-field Chabauty criterion is imported; its actual rank, reduction, integrality and unit-determinant application is checked in PURE-14. Source: https://msp.org/ant/2013/7-4/ant-v7-n4-p01-p.pdf
- Yu:OrdinaryAmbiguousClassFormula: Imported mathematical theorem with the application explained in its review; not formalized or re-proved in full. Source: https://arxiv.org/pdf/1412.1458
