# Rank descent: logical audit, 15 September 2026

This is an ongoing audit of the rank appendix and its BPS interfaces, using the frozen source snapshot and the released evidence. It identifies **no new mathematical contradiction** in this branch. It also does **not** certify every underlying arithmetic argument: the precise unreviewed foundations and coefficient-level precision chains remain `OPEN_VERIFICATION` in the attached claim ledger. A `CHECKED_ARGUMENT` entry validates the stated implication under its recorded hypotheses; it does not silently discharge open dependencies.

## Primary-source checks

I read the archived Bruin–Poonen–Stoll arXiv v2 and the published 2016 PDF hosted by an author: [Generalized explicit descent and its application to curves of genus3](https://math.mit.edu/~poonen/papers/genus3.pdf). The checked passages are Section6.3/Proposition6.10, Corollary12.5, Hypotheses10.1 and11.1, Lemma10.2, Remark11.6, Theorem10.14, and LemmasA13, A24 andA26. The relevant statements and numbering agree between the checked versions.

The rational point supplies the divisor hypotheses, including at dyadic completions: the field characteristic is zero. The incidence theorem applies to smooth plane quartics without requiring full generic Galois image. The local stopping rule multiplies a genuinely observed image size by a genuinely detected kernel size. The comparison exact sequence permits the rank argument from a containing fake space; one need not assert that every survivor is a Selmer class or assume vanishing of Sha^1 of the correction module. These are important applicability checks distinct from executing a program.

## Newly performed computations

The current audit freshly substituted the displayed P1 using exact rational pairs in Q(sqrt(-7)); the quartic value is exactly zero. A separate SymPy computation checked all three projective smoothness charts at each embedding above733177, returning the unit ideal every time. The inspected conic checker was rerun with relocated input paths and output writes removed: each embedding has28 distinct contact squares and exactly315 of the20,475 four-subsets support conics; all315 incidence masks match.

New integer-only linear algebra, independent of the released matrix routines, reconstructed the local constraints. Remaining dimensions are:

| Added place | Dimension |
|---|---:|
|19163|46|
|23431|28|
|29059|24|
|38189|23|
|1051|22|
|3|20|
|5|19|
|7|18|
|first dyadic place|15|
|second dyadic place|12|

The diagonal, diagonal plus known points, and diagonal plus known points plus the literal c have ranks7,11,12. Every such vector satisfies every reconstructed constraint. This proves exact equality to the final containing space from these supplied arithmetic matrices, not only an equality of dimensions.

I also freshly enumerated all95 AGL(3,2) subgroup conjugacy classes with GAP using the inspected finite sources. All four edge-transitive classes have a one-dimensional global correction quotient; independent integer calculations on their generators also give zero global2-torsion. The odd-place envelope gives local2-torsion dimensions4,2,3,2 at1051,3,5,7. The p7 envelope has three D8 classes and24 compatible carriers: every evaluation descends, but only12 are nonzero. This reproduces the manuscript's essential distinction between descent of a character and its nonvanishing.

The current integer checker independently reconstructed all315 relation masks and the42-target matchings. For all28 exported second-dyadic groups matching target splitting[3,3,6,6,24], it found local2-torsion dimension1, correction quotient dimension2, and two descended sextic characters of rank2. The full dyadic group-envelope algorithm was read for completeness but not regenerated in this bounded pass; its Sylow/wild/tame/Frobenius logic is explained in the ledger. No exact local-field coefficient or sign value was accepted merely because an accompanying JSON said PASS.

The first attempts to use the macOS system Python, a bundled Python without the explicit math package path, and Sage without a task cache failed before the requested arithmetic. Successful checks used the existing runtime with its explicit math package path and a new Sage cache under this audit directory. No sealed proof source or release file was edited.

## Mathematical implications checked

For the 7-adic stopping step, the actual closed-point image must be nonzero and the actual full fake-kernel cycle must have nonzero correction. Given those witnesses and local Kummer order4, the image and kernel necessarily each have order2. The full seven-component square test is essential; a square only on the selected target would not suffice. Likewise, at the second dyadic place, three independent images plus a nonzero kernel fill a local Kummer group of order16. Character computations alone do not establish the actual nonzero arithmetic correction.

The contact-divisor normalization is consistent. A four-incidence tetrad gives theta(a)=a^2. If f(z)=a lambda^2, the expression r(z)/(a^2 tau(lambda)) is the fake-kernel correction; if f(z)=c a lambda^2 and u^2=tau(c), the expression u a^2 tau(lambda)/r(z) is the corresponding lift obstruction. Exact contact identities force these expressions into mu2 before precision can read their sign. At2, actual error bounds must exceed the valuation of2 to distinguish the signs. Root-search uniqueness is unnecessary because each quadratic norm is unchanged under sign reversal.

The global-lift issue was checked against LemmaA13(b), not only its convenient square-power necessary condition. The supplied all315 validator uses77 relation conditions on98 carrier columns spanning the relation module, thereby addressing q-prime compatibility. Its exact root and reduction bindings remain separately auditable inputs. Once there are exactly two coherent lifts and their actual W5 obstructions are(1,0) and(0,1), the functional(u,v)↦u+v excludes both while killing their difference(1,1). Because the local fake kernel at5 is zero and the global correction group has dimension1, its nonzero restriction proves the global comparison kernel is zero. No knowledge of the correction spaces at other places is needed for this negative argument.

If a true Selmer class maps to c+b, subtracting a global point Kummer class mapping to b gives a locally Kummer lift of c, a contradiction. The true Selmer image therefore lies in B. The injective comparison and four independent point images yield rank4 and Sha[2]=0 through the Kummer exact sequence. This implication does not confuse the containing space with the actual fake Selmer group.

After rank4, the four independent point images modulo2 imply H0 has finite odd index. The relation5E=D3+D4+3D5 gives H0 contained in H1; an independently justified5-saturation of H1 then makes its index coprime400. Thus H1 covers J/400J. For logarithms, finite index of H0 alone suffices: a nonzero integer multiple of any point lies in H0, and the logarithm's target has characteristic zero. No p-adic unit condition on that integer is needed.

## Remaining audit coverage

The main open foundation is the global66-generator containment: complete support, class-group2-primary control, unit saturation and corrected principal/diagonal data. Correct principal multiplybacks alone do not prove generation; an unramified bitangent algebra alone does not prove all required Jacobian/Tamagawa support conditions. The historical reports describe substantive arguments, but this pass has not independently checked their full primary-theorem and numerical chains.

Other open nodes identify the exact bitangent/target exports, rational-theta tower inputs, the coefficientwise map/point bindings, actual p7 Hensel/Krasner/denominator error estimates, and the precise bindings consumed by the coherent global roots. The coherent-root construction itself and the p5 local source, physical-character and norm/sign computation has since been checked in the follow-up below, conditional on those explicit global bindings. These are **uncompleted audit coverage**, not claims that the release lacks those computations or that its mathematical conclusions are false. The E/divisor and5-saturation arithmetic is assigned to the downstream branch and is an explicit external branch dependency here.

The JSON ledger is the authoritative dependency list for this branch. Its terminal `RANK-END` remains open while any load-bearing dependency remains open. This work is an AI-assisted internal review, not independent external specialist certification.

## Focused p5 follow-up: actual local arithmetic

The new follow-up closes RANK-27 as a local computation with explicit upstream hypotheses, and adds RANK-33/34 to separate its actual source/image and physical characters. The global contact/target export remains an open dependency; the coherent-root construction was checked in the subsequent follow-up below. The terminal rank claim has not become transitively verified.

A new focused calculation constructed the exact cycle z=P2+P4−2P1 and scalar a=(s−1)/2. It reconstructed c from the N6 coefficients and checked exact equality with CP22. The quotient f(z)/(ca) has zero in every one of the22 valuation/residue squareclass coordinates, and is independently a square at all11 actual primes by direct local-power tests after multiplication by an exactly verified denominator square. This establishes precisely the source used by the local obstruction. The same fresh construction verifies the five smooth curve points and nonzero line values; the diagonal has rank2 and the diagonal plus four point images has rank5. Thus the actual fake image has dimension3 and the local fake kernel is zero once the already checked Kummer dimension is used.

I read the full norm-first worker. Its quadratic models are validated as Eisenstein in the ramified case and by nonsquare unit discriminant in the unramified case. The quadratic norm formula and residue used to choose the square root of Norm(lambda²) are correct in both cases. A sign choice for lambda does not alter its quadratic norm. The iteration uses a fixed initial inverse; quadratic convergence is not assumed, and the final residual bounds are what justify it. All six new norm residuals give relative error at least21. Exact contact and coherent-root identities force the obstruction into mu2, and the computed signs have separation22,21,22 while propagated target precision is at least35. This proves the local sign determination given those identities, without inferring exact equality from numerical closeness alone.

One subtle interface required an additional check. PARI's official [factorpadic specification](https://pari.math.u-bordeaux.fr/dochtml/html/Polynomials_and_power_series.html) guarantees approximations to true factors for exact inputs; an inexact input is first truncated. The original carrier finder factors such an intermediate incidence norm. To avoid assuming this intermediate factorization establishes exact incidence, the new check enumerates every degree8 divisor product of the true degree56 source factors. There are19 possibilities. At each of the six degree2 targets, the actual incidence norm must be one of them by the exact global divisibility premise. The selected product is uniquely determined already modulo5: it agrees to39–41digits, and every other candidate has coefficient difference of valuation0. This establishes the carrier association independently of the inexact factorization's semantics.

The finite character checker was read completely and freshly rerun after weakening its target filter to use only the independently computed factor degrees. All126 source-compatible tame inertia/Frobenius pairs are considered, and84 remain compatible with target orbit lengths1^6,2^8,4^5. Every case has a2-dimensional correction quotient and the physical characters satisfy chi1=chi3 with chi1,chi2 independent. A tempting split+split carrier is rejected because it does not descend. The fresh local signs are(-,+,-), giving obstruction(1,0); the opposite coherent root gives(0,1). The 5-adic local argument is therefore checked conditional on the explicitly open exact global geometry and coherent-root identification. This relies on the ordinary specifications of PARI/Sage arithmetic; it does not claim a formal verification of those libraries.

The added draft cubic–quartic paragraph at manuscript lines590–608 was also independently checked. Norm(kappa)=21 is not a square in k, so the quartic field is non-Galois and has only the quadratic subfield k. Rational U forces u/v into k; uv in k then forces u² in k and u=b sqrt(kappa). The odd part of Phi(u) is3u^5(5u²+7), so b²=−7/(5kappa), whose norm would require the impossible rational square7/75. No correction to that paragraph was needed.

## Global coherent-root follow-up

RANK-25 is now checked conditional on the separately audited exact geometric/target bindings. The exact root evaluator and independent validator were read in full and rerun: both root blobs square exactly to their supplied norm elements, and every one of196 reductions was freshly evaluated from these exact algebra elements using the live literal N6 source. These checks do not replace the upstream proof that the supplied norm elements are actual four-incidence norms; that is RANK-03.

The full finite coherence validator was also rerun on the newly generated reductions. The98 carrier columns span the21-dimensional relation module, giving77 independent relations. Each relation quotient is exactly in mu2 by the square identities and even incidence; since every denominator is a unit at the odd checking prime, reduction distinguishes its exact sign. Multiplicativity on the binary relation kernel follows by cancellation of overlapping columns using the exact root-square identities, so77 basis checks establish all relations. This supplies the compatibility required by BPS A13(b), beyond merely asserting that tau(c) is square. The315 extension and423360 transport checks per embedding all pass. The two coherent whole-orbit sign choices are00 and11, and their ratio is nonzero on the spanning carrier set. The already checked correction quotient then proves these are exactly the two global lifts. Exact global geometry/target labeling and theta/Galois identification remain upstream obligations, rather than being inferred from the finite computations.

## Second-dyadic follow-up

RANK-20/21 are now checked as actual local computations conditional on the exact geometry. The raw source and all its point, component-square and precision formulas were read. Fresh runs confirm the exact curve scaling and the two smooth Hensel charts; all three actual primes are matched to a fresh prime decomposition and to the w=0 base place. Their degrees total28. Every tested algebraic element is converted to an integral-basis column after multiplication by an exactly verified denominator square. The old four points have fake rank2, C0 gives an independent third image, and the two full-component relations are[1,1,−10] and[1,0,2]. The Hensel and line-stability bounds identify these with true local divisors. The historical branch-tracker typo is not used by this argument.

A new direct check handles another subtle precision interface: factoring a polynomial after approximating its quadratic-base coefficients. Instead of assuming the resulting factorization describes the exact target, the check evaluates the original target polynomial in exact local models for every factor. Strong Hensel and Krasner bounds, together with cross-factor separation, prove that the actual factor degrees are3,3,6,6,24. The absolute e,f pairs are(1,3),(1,3),(2,3),(2,3),(4,6). In particular both sextic carriers are actual fields with e=2,f=3.

The final sign computation was then rerun with explicit conservative uncertainty. Direct original-polynomial root bounds308 and318 give target-root coefficient balls2^150 and2^155 in the exact sextic models. The quadratic incidence factors have unit resultant and product residual of target valuation64; all their lower coefficients were widened by2^28 before the downstream calculation. This allows the true target and incidence factors, rather than silently treating finite approximations as exact. The validated local bases and Eisenstein/unramified quadratic models make the valuation formulas legitimate. The point-coordinate errors give line and conic relative errors at least118. The unit square-root residuals yield exact root errors36 or18; norms retain target relative error at least18. Since the exact contact identity puts the true correction in mu2 and vA(2)=2, the final margins(19,2) and(2,18) prove the nonzero correction profile(0,1). The first-dyadic rank4 witness is a separate parent-audited input to RANK-23.

## Claim inventory

|Claim|Source line|Status|
|---|---:|---|
|RANK-01|sources/rank-proof.tex:5|CHECKED_COMPUTATION|
|RANK-02|sources/rank-proof.tex:4|IMPORTED_RESULT_APPLICABILITY_CHECKED|
|RANK-03|sources/rank-proof.tex:20|OPEN_VERIFICATION|
|RANK-04|sources/rank-proof.tex:23|CHECKED_COMPUTATION|
|RANK-05|sources/rank-proof.tex:24|OPEN_VERIFICATION|
|RANK-06|sources/rank-proof.tex:25|CHECKED_ARGUMENT|
|RANK-07|sources/rank-proof.tex:21|IMPORTED_RESULT_APPLICABILITY_CHECKED|
|RANK-08|sources/rank-proof.tex:18|OPEN_VERIFICATION|
|RANK-09|sources/rank-proof.tex:29|OPEN_VERIFICATION|
|RANK-10|sources/rank-proof.tex:31|CHECKED_COMPUTATION|
|RANK-11|sources/rank-proof.tex:31|CHECKED_ARGUMENT|
|RANK-12|sources/rank-proof.tex:37|CHECKED_COMPUTATION|
|RANK-13|sources/rank-proof.tex:48|CHECKED_COMPUTATION|
|RANK-14|sources/rank-proof.tex:63|OPEN_VERIFICATION|
|RANK-15|sources/rank-proof.tex:70|OPEN_VERIFICATION|
|RANK-16|sources/rank-proof.tex:83|IMPORTED_RESULT_APPLICABILITY_CHECKED|
|RANK-17|sources/rank-proof.tex:95|CHECKED_COMPUTATION|
|RANK-18|sources/rank-proof.tex:101|OPEN_VERIFICATION|
|RANK-19|sources/rank-proof.tex:109|CHECKED_ARGUMENT|
|RANK-20|sources/rank-proof.tex:117|CHECKED_COMPUTATION|
|RANK-21|sources/rank-proof.tex:126|CHECKED_COMPUTATION|
|RANK-22|sources/rank-proof.tex:133|CHECKED_COMPUTATION|
|RANK-23|sources/rank-proof.tex:137|CHECKED_ARGUMENT|
|RANK-24|sources/rank-proof.tex:145|CHECKED_COMPUTATION|
|RANK-25|sources/rank-proof.tex:145|CHECKED_COMPUTATION|
|RANK-26|sources/rank-proof.tex:156|CHECKED_ARGUMENT|
|RANK-27|sources/rank-proof.tex:148|CHECKED_COMPUTATION|
|RANK-28|sources/rank-proof.tex:153|CHECKED_ARGUMENT|
|RANK-29|sources/rank-proof.tex:160|CHECKED_ARGUMENT|
|RANK-30|sources/rank-proof.tex:174|CHECKED_ARGUMENT|
|RANK-31|sources/rank-proof.tex:174|CHECKED_ARGUMENT|
|RANK-32|sources/rank-proof.tex:180|CHECKED_ARGUMENT|
|RANK-33|sources/rank-proof.tex:156|CHECKED_COMPUTATION|
|RANK-34|sources/rank-proof.tex:148|CHECKED_COMPUTATION|
|RANK-END|sources/rank-proof.tex:167|OPEN_VERIFICATION|

Counts: CHECKED_ARGUMENT=10, CHECKED_COMPUTATION=14, IMPORTED_RESULT_APPLICABILITY_CHECKED=3, OPEN_VERIFICATION=8.

Source SHA256:

- `manuscript.tex`: `5dc92b60a88cdc0ec4addbe549efc5756e164db49b290fc0ac225bbc5dc972ff`
- `rank-proof.tex`: `fd54ed8996f5ecbfd3fff53bbdf27eaacb1210846eb4fe5db2b0c942d56f81cd`
