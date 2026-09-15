# Independent second review of the Section 7 local pullback

The new evidence establishes exclusions on whole local residue discs, not just on the displayed centers. I find no remaining universal-coverage gap in CUBIC-09, subject to the explicitly imported Flynn coordinate/formal-neighbourhood theorem. The finite-base infinity truncation has a particularly simple all-orders justification below. This review does not independently re-audit the Mordell–Weil basis or the separate calculation placing 2240A in G[2].

The inspected files are `checks/check_flynn_coordinates.py`, `checks/flynn_coordinate_results.json`, and `checks/section7_uniform_recheck.py` with its JSON, relative to `work/mathematical_argument_audit_2026_09_15`. The archive source imported by those checkers is `evidence/v3/repository/results/2026-09-10_section7_formal_group_lemma_7_5_v2_model_intrinsic/scripts/verify_section7_formal_group_lemma_7_5_v2.py` in the sealed verified release. I read the actual Definition 1.1 and the integral expansions preceding Theorem 2.1 and Corollary 2.2 in `work/review/flynn1990_layout.txt`, from the primary Flynn paper.

## Coordinate binding

The specialization at checker lines 21–57 agrees with all 16 entries of Flynn's Definition 1.1. The divisor Q−P is correctly represented by `(x,y)+(a,−b)`. The coordinate change fixes the first 12 coordinates and replaces the last four by `(a13,a14,a15,a12−2a13)`; it is integral unimodular and fixes the origin and the two formal parameters. Reduction modulo `y²−f(x), b²−f(a)` proves polynomial identities, not tests at finitely many points. The divided-difference identity and both ordinary-coordinate expressions also agree identically.

For a finite base, the polynomial vector is `(x−a)^4` times the Flynn vector. At the conjugate locus, where this clearing may vanish, the alternative slope `(f(x)−f(a))/((x−a)(y−b))` extends the appropriate chart whenever y−b is nonzero. The residue pruning does not assume the cleared vector stays nonzero everywhere: a strict, stable nonzero coordinate is needed before that chart can reject a ball. At a true common zero of the cleared vector, such a rejection cannot occur. The alternative chart handles the conjugate cases; the base-point disc itself is deliberately retained.

One binding was implicit in the new checker: `infinity_base_vector` is read from the archive, rather than itself compared there with Definition 1.1. I closed that binding by a short fresh symbolic check. Let the fixed point tend to the actual infinity of sign τ, so

`b=τ(a³−4a²+3a)+O(a⁻²)`.

In the 16 cleared generic coordinates, the coefficient of a⁶ is exactly `infinity_base_vector(x,y,−τ)`, entry by entry, modulo `y²=f(x)`. There are no higher coefficients. Substitution of the omitted b-tail affects orders at most a⁵: inspecting coefficients of an auxiliary error e shows `degree_a(coefficient(e^j))−2j≤5` for every j≥1. Thus the equality is the true projective limit. Both signs were checked. This explains why the source's `fixed_sign` is the negative of the actual fixed infinity's y/x³ sign; its identity-branch test `moving_sign == −fixed_sign` is correct.

## Integral affine discs

Write O for the valuation ring of Q₇(θ), θ²=−35, with v(θ)=1. The valuation formula used by the exact rational-quadratic replay is

`v(a+bθ)=min(2v7(a), 2v7(b)+1)`.

The two possible terms have different parity, so there is no hidden cancellation. All ten fixed finite points are O-integral. For each base, the initial 49 representatives exhaust O/(θ²), and the 98 pairs retained by the curve congruence include every integral local point. Each unresolved pair is replaced by all 49 possible next-digit pairs satisfying the next curve congruence. An actual point in an unresolved ball must therefore occur in one of its children; no Hensel nonsingularity assumption is needed for this exhaustion. The output's empty final pending list, reached by depth 2 or 5, proves there is no infinite branch outside the permitted base-point congruence class.

For integral polynomial coordinates, changing x,y within θⁿ changes every coordinate within θⁿ. The replacement `strict_reject` in `section7_uniform_recheck.py` tests only a coordinate valuation strictly below both its error bound and v(a0)+2. If a0 is itself invisible, it uses a lower bound for v(a0). Those are valid rejection inequalities on the entire ball. This repairs the general weakness of the older predicate, which did not always explicitly restrict to visible precision. No rejection used in the new run has an invisible strict inequality.

For the alternative chart, let d=v(y−b)<n. If the slope β is integral, its error is at least n−d: numerator and denominator are integral polynomial functions, and the numerator has valuation at least d. Polynomial coordinates in integral x,a,β inherit that bound. In the 18 exceptional cases where β has negative valuation (six each for P3,P7,P8), the separate `Ball` arithmetic propagates errors through every division and multiplication. Its multiplication bound is the minimum of the two linear error terms and their product; its division bound uses a denominator of fixed valuation below its precision. The `ball_reject` assertion then exhibits a fixed nonorigin coordinate strictly below the lower bound for a0 plus two. These calculations validate those entire balls even though the simpler integral-β precision rule would not apply.

The congruent initial disc is retained once, rather than being proved empty: CUBIC-09 needs the implication `[Q−P] in G[2] => Q congruent P mod θ²`. Flynn's integral power-series expansions make all nonorigin coordinates have valuation at least two on G[2], so the tested violations are necessary-condition contradictions.

## Finite base and moving point near infinity

Every nonintegral x has w=1/x in θO. The equation gives

`y=±w⁻³ S(w)`, where `S(w)²=(1−4w)(1−4w+6w²+9w⁴)` and `S(0)=1`.

Since 2 is a unit, the recursive coefficient equations give **S in O[[w]]**, with convergence throughout θO. There are exactly the two signs, including the two points at infinity when w=0. This is an all-orders integrality statement, not a conclusion drawn from the first 20 coefficients.

Every monomial xⁱyʲ in the cleared coordinate vector, with a,b fixed, has i+3j≤12. Therefore after multiplication by w¹² every coordinate is a polynomial over O in w and S, with no negative powers of w. Replacing S by its degree-19 truncation changes each such coordinate by an element of **w²⁰ O[[w]]**. This is stronger and clearer than the loose remainder wording in `flynn_coordinate_results.json`.

In all 20 sign/base cases the exact leading common exponent after w¹² clearing is six. The observed coefficients through degree six are exact, because the omitted remainder starts at degree 20. Dividing by w⁶ consequently gives an integral vector whose omitted tail begins at degree 14. At least one nonorigin constant coefficient is a unit in every case (indeed index15 is always listed). For every w in θO, that coordinate remains a unit, while all coordinates remain integral. Thus the projective point cannot reduce to the Jacobian origin, let alone belong to G[2]. This proves exclusion of the **entire** infinity disc for every finite base. It also covers w=0 by the projective limit.

The exact formula integrality, rather than the checker merely finding integral coefficients in one finite truncation, is what controls the unseen tail. The fixed points' denominators are 7-adic units, and θ itself is integral, so no base-specific denominator destroys this reasoning.

## Infinity bases

For an integral moving point and an infinity base, the bound is immediate: the bound infinity vector has a15=1 and every coordinate is integral. It cannot be in the origin neighbourhood. This case need not be approximated by a Laurent expansion.

For moving points in the two infinity discs, the four checked series suffice, with the following unit-denominator proof. On the identity branch, w⁶a0 has constant 16, a 7-adic unit, and `s1=(fixed_sign/2)w+O(w²)` with integral higher coefficients. Hence v(s1)=v(w); belonging to G[2] forces v(w)≥2, exactly the required congruence to the fixed infinity. On the opposite branch, w²a0 has constant36, also a unit, and `s3=−1/6+O(w)` with integral higher coefficients. It stays outside the origin neighbourhood throughout that disc. These follow from

`S(w)=1−4w+3w²+0w³+0w⁴−18w⁵+...`.

The degree-9 truncation in the checker determines the needed leading terms; integrality of the full S and the unit denominator constants prevent higher terms from cancelling them. Both infinity-base signs and all moving-point cases are covered.

## Disposition

CUBIC-09 can be recorded as checked computation plus checked argument, with the coordinate/Flynn theorem dependency explicit. The needed universal quantifier follows from exact polynomial identities, complete residue lifting, strict visible error inequalities, and integral unit-leading series—not from a finite list of sampled points or an unexplained PASS marker. No original evidence, manuscript, or other review file was modified in this second review.
