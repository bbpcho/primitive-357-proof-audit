# Global squareclass foundation and restriction maps

This supplement closes the audit-coverage obligations RANK-08 and RANK-09, conditional on the separately reviewed identification of the actual bitangent descent. It distinguishes newly computed exact identities from the previously replayed arithmetic whose source and mathematical interpretation were reviewed here. It is not a formal proof or an independent implementation of every number-field algorithm.

## A sufficient set of places

The earlier descent-support manifest was an unfinished historical record. Its field discriminant alone would not prove the required support statement. The later geometric support manifest is the relevant input.

I independently reconstructed the resultant of the three partial derivatives of the printed quartic. The calculation uses a primitive integral scalar multiple, a36-by36 Macaulay matrix, and its9-by9 extraneous minor. Their exact determinant quotient, divided by2^14, agrees with the geometric manifest's normalized discriminant up to sign. The only nonzero prime-ideal valuations are72 and180 at the two places over2,168 over3,93 over5,162 over7, and36 at one place over29. The coefficient ideal is the unit ideal. Thus the primitive projective model is smooth outside these six places; its Jacobian has good reduction there and Tamagawa number1. The factor2 in the normalization introduces no issue because both dyadic places are included.

The construction of the matrices is the degree7 instance of the classical Macaulay formula: multiply each partial by the degree4 monomials assigned to its first divisible cube, and remove the rows and columns indexed by monomials divisible by two cubes for the denominator. The definitions of the Sylvester and extraneous matrices, and the resultant identity, are in [D'Andrea–Dickenstein, §§2–3](https://arxiv.org/pdf/math/0007036). The determinant arithmetic is new; the general resultant theorem is an imported result.

There is a further **archival prose correction**. The bad place over29 is\[
                 (29,s-15),\qquad s^2=-7.
\]It is the prime with PARI HNF[29,22;0,1]. In the actual degree56 field the four supplied support primes have indices2,3,7,8 and satisfy v(s_L-15)>0, v(s_L-14)=0. A historical acceptance note calls this same HNF the s_L=14 place. That sentence is false. The exact discriminant and the numerical support packet select the correct s_L=15 place. No generator or restriction matrix needs changing. The new direct source-sign check in the geometry supplement confirms that the printed s corresponds to +T[5], not its conjugate.

A fresh prime inventory reconstructs all7,9,11,7 primes over2,3,5,7 and the four selected primes over29. All38 supplied generators generate exactly those prime ideals. It also identifies the second dyadic set[1,3,7] by v((1+s_L)/2)>0. The exact line field's discriminant is supported on2,3,5,7, so its permutation module and the BPS quotient are unramified outside the chosen set.

For K=Q(sqrt(-7)), Minkowski's bound is(2/pi)sqrt(7)<2; hence its class group is trivial. This removes the ideal-class obstruction in BPS Proposition7.3, equation(18), between unramified fake classes and representatives in L(S,2). Applying the containing direction of BPS Theorem10.9(a) requires no exhaustive Frobenius packet. The local test set may omit29 because an upper bound is sufficient. [BPS, Propositions7.2–7.3,9.2 and Theorem10.9(a)](https://math.mit.edu/~poonen/papers/genus3.pdf)

New evidence: checks/support/check_macaulay_support.py and macaulay_support_result.json; check_base_conventions.gp and base_conventions.log.

## Class number and units

The class-number argument uses fields E,L,F,N of absolute degrees14,56,42,84 and a degree21 field T. It never promotes the saved conditional BNF class numbers of L or F to unconditional evidence.

The elementary implications were checked as follows.

1. If the ordinary class number of T were even, its ordinary Hilbert class field would have a quadratic subextension H/T unramified also at real places. H has degree42, six real embeddings and absolute discriminant |disc(T)|^2. Every principal T-prime splits in H. The exact arithmetic re-enumerates all3216 primes of norm at most30000 and proves their principality by ideal equality and factor multiplication. The interval calculation applies the unconditional part of [Brueggeman–Doud, Theorem2.4](https://mathdept.byu.edu/~doud/Papers/Local.pdf) with y=43849/1000000, and gives a strict positive margin greater than0.04072 against this discriminant. Therefore h(T) is odd.

2. I read the interval source, including its first-cell bound, alternating-series enclosure of the test function, upper bounds on the two integrals, and both infinite tails. Its range0≤f≤1 is justified by the sinc integral. Omitting further nonnegative local terms weakens the lower bound in the required direction. The arithmetic uses outward-rounded Arb intervals, not a floating quadrature. The source's coefficients match equations(2.1)–(2.2) and Theorem2.4(1) in the primary paper. The actual positive interval and prime enumeration are the sealed fresh replays; the large interval partition was not repeated in this pass.

3. F=T(sqrt(-7)) has one finite and three infinite ramified places. The exact source verifies the field isomorphism, relative discriminant, candidate-unit integrality and norms, Sturm-certified real signs, and a rank3 Hilbert-symbol matrix. For units at unramified places the local norm obstruction is zero; reciprocity gives the upper bound3 and the exhibited units attain it. The Hasse norm theorem therefore gives unit norm index8. The ordinary ambiguous class-number formula yields |Cl(F)^Gal(F/T)|=h(T). A nonzero2-torsion group under an involution has a nonzero fixed vector, so h(F) is odd. The same argument for N/F uses four finite ramified places and another rank3 unit obstruction, giving odd h(N). These are cyclic quadratic extensions; no noncyclic norm theorem is being applied. The [ordinary ambiguous class-number formula](https://arxiv.org/pdf/1412.1458) includes the real ramification in its product, as required here.

4. The relative quartic is irreducible and has irreducible cubic resolvent and nonsquare discriminant, hence its relative normal closure is S4. The exact source identifies the absolute field L, the cubic resolvent F, and N as the unordered-pair field. The pair sums/products multiply back to the original quartic. The permutation-character relation gives zeta_E*zeta_N=zeta_L*zeta_F. The relevant subgroup normal closures are S4, so none of L,F,N contains a nontrivial Galois extension of E; their roots of unity are consequently those of E, namely±1.

5. The regulator factor was independently recomputed here on the full integer lattices. In seven blocks the map is (a_i,b_partition) to(sum a_i, a_i+a_j+b_partition). Its49-by49 determinant has absolute value2^28. Unimodular changes of basis isolate the two product-formula directions, on which the matrix is[[1,0],[3,2]]. The remaining47-by47 determinant is exactly2^27. Thus\[
 \frac{R_E R_N}{R_L R_F}=\frac{2^{27}}{J},\qquad
 h(L)=\frac{h(E)h(N)}{h(F)}\frac{2^{27}}{J}.
\]There is no omitted unit index or floating regulator approximation. New evidence: checks/support/check_regulator_factor.py and regulator_factor_result.json.

6. The independent L-unit source verifies maximal order, signature(0,28), actual unit status, roots of unity±1, and28 independent residue characters including torsion. Dirichlet's theorem gives precisely28 unit squareclasses, so these candidates generate them. The analogous F calculation establishes21 independent unit squareclasses. These prove odd index in the full unit groups, which is all the2-adic index calculation needs.

7. I checked the exact correspondence construction, both enlargement steps and the terminal residue-character source. The47 source units are mapped through the actual relative norm and unordered-pair product. The21 first and6 second relations have independent pivots in the47 free columns, with the two torsion columns explicitly excluded from the pivots. Every inserted square root multiplies back exactly. Integrality follows because its square is an algebraic unit; thus it too is a unit. Each layer enlarges the free lattice by the stated power of2. The final47 free columns plus the two torsion columns have49 independent actual residue characters, so the enlarged subgroup has odd index. Consequently v2(J)=21+6=27. The source domains also have odd index, so using their candidate units does not change this2-adic value.

8. The degree14 class number is1 by the sealed unconditional bnfinit/bnfcertify replay. With h(F),h(N) odd and v2(J)=27, the displayed identity gives Cl(L)[2]=0.

For this pass I inspected the source arithmetic and existing fresh outputs for these class and unit calculations, rather than launching another complete high-degree class computation. The principal new computations are the resultant, support inventory and free-lattice determinant. The evidence manifest names and hashes the exact sources and outputs used.

Finally, Cl(L)[2]=0 also gives Cl(O_L,S)[2]=0. All38 support primes are principal, so the exact S-unit squareclass sequence consists of the28 ordinary-unit classes and38 independent valuation classes. Their66-dimensional span contains every relevant fake Selmer representative. The base diagonal has dimension1+6=7. This proves the required direction for RANK-08.

## Actual restriction of all66 generators

I read the full predyadic restriction source and the actual-completion dyadic validator. Both construct the same ordered28+34+4 list, with exact ideal checks; no inherited62-column prefix is accepted as arithmetic evidence. The new support inventory binds these entries to the entire necessary set and to the correct base places.

At the four split primes every selected root is tested in the exact absolute polynomial and the chosen base embedding. Every local line and curve coefficient is bound to the global object. The rows are genuine quadratic residue characters. At1051 the exact squarefree factorization and base embedding select the whole degree28 algebra. At3,5,7, actual maximal-order prime ideals and uniformizers are checked; valuation parity and the residue Euler character give all local squareclass coordinates in odd residue characteristic. The archived fresh run compares all66 columns, not only a complementary class.

For the dyadic places, it is unnecessary to trust the precision of an intermediate factor model as the final justification. The validator independently certifies the result in each **actual completion**. A full-rank set of columns selects d=e*f+2 candidate basis classes; their actual Hilbert pairing matrix is nonsingular. They therefore form a basis of that completion's squareclass group. For every one of the66 entries the stated coordinate combination divided into the actual global element is tested as a square in that same completion. This proves the proposed coordinate map on every input column regardless of how its candidate coordinates were found. Clearing an integral-basis denominator by its square preserves the squareclass, and that identity is checked before the exact local-square test.

There are seven actual dyadic components, of squareclass dimensions6,8,14,8 and6,14,14. The sealed fresh output records all seven nonsingular Hilbert bases and all462 column multiplybacks. The new place check binds[1,3,7] to w=(1+s)/2=0 and its complement to w=1. Thus RANK-09 is checked. This validates restrictions; completeness of the allowed local images is a separate dependency and is not inferred from this argument.

## First dyadic allowed image

The first dyadic image is bound to genuine points, not just to a proposed subspace. I read both complete verifiers, verify_local_point_lifts.gp and verify_source_columns.gp, and their sealed fresh outputs. The quartic is bound projectively to the same printed equation; all five global points satisfy it exactly. The first place is the root w congruent to 1 modulo 2 of w²−w+2, with s=2w−1.

At the approximate point [2:46:1], the residual has valuation 10 and the X derivative valuation 1. The univariate polynomial has content valuation 1, so its normalized residual has valuation 9 and derivative valuation 0. Strong Hensel gives a true point with X-coordinate error of valuation at least 9. In the four actual bitangent completions the line-change estimates exceed the square-stability threshold 2e by 28,14,28,14 respectively. Thus the true point and the approximate point have the same line squareclasses in every component.

The eight columns are the three diagonal classes [2,−1,5], the four exact global point differences, and this true local point difference. Each column is checked against the same actual-completion basis certified under RANK-09: their quotient is a square in each actual completion. The source ranks are 3 for the diagonal, 6 after the global differences, and 7 after the local point, so the fake image has dimension at least 7−3=4. The independent local group bound gives dimension at most 4. As a final provenance check I reran the entire 95-class subgroup enumeration unchanged: exactly five classes have the actual first-place orbit degrees [4,6,6,12], and all have fixed J[2] dimension 1. The genus-three Q2 local quotient therefore has dimension 3+1=4 by BPS Remark11.6. Consequently this is the entire first dyadic image. It is a separate premise of the combined dyadic cut in RANK-23.

Evidence: sealed verification/prior/logs/verify_local_point_lifts.log and verify_source_columns.log; their complete sources under audit/work/p5_archive_audit/local_upper_bound. These outputs were freshly replayed in the sealed audit, not rerun as part of this supplementary source review.

## Limits

The BPS framework, class field theory, the analytic discriminant inequality, the resultant theorem, and the computer-algebra primitives remain explicit mathematical/software imports. They were not formalized or independently implemented wholesale. The ledger records a reviewed argument with checked computational evidence, not proof-assistant certification or review by an external human specialist.
