# A concrete repair of the Section 7 basis argument

The requested finite-field witness exists already at p=173 and theta=22. It proves the remaining 2-saturation, conditional only on the previously established rank, torsion, rational/twisted generators, and exact divisor relation. It replaces the invalid index inference after quotienting by torsion.

`independent_basis_kummer.py` uses only Python's standard library. It verifies the five distinct branch roots, the point defining D3, the monic odd model, all denominators, each quadratic character, the norm parity relation, and the matrix rank. Its first eligible fully split prime produces rank four. The exact data are saved in `independent_basis_kummer.json` and `.log`.

For p=173, theta=22, the odd-model roots are (15,90,119,122,164). The values before applying quadratic characters, with divisors as columns, are:

|root|D0|D1|D2|D3|
|---:|---:|---:|---:|---:|
|15|140|137|27|110|
|90|53|139|86|48|
|119|145|117|110|38|
|122|11|134|119|30|
|164|28|5|59|50|

Their Legendre bits form the matrix

```
0 0 1 1
1 0 1 1
1 0 1 0
1 1 0 1
1 1 1 1
```

The first four rows have determinant 1 modulo 2. Equivalently, all 15 nonempty sums of the columns are nonzero.

The original divisor convention is confirmed by `repository/results/2026-09-10_section7_mordell_weil_basis_lemma_7_3_v1/scripts/verify_section7_mordell_weil_basis_lemma_7_3.m:17–20`: D0=P4−infinity_minus. The sieve source `.../2026-09-10_section7_mw_sieve_lemma_7_4_v1/scripts/verify_section7_mw_sieve_lemma_7_4.py:148–159` agrees for all four divisors. D2's two moving points have odd-model u-polynomial u²−3au+a²; subtracting the two original infinities contributes the square r_i². Choices between the two infinities cannot affect the Kummer image because both have u=0.

For the standard map and branch-value convention, see Michael Stoll, *Descent and Covering Collections*, §7.1, pp.13–14, and §7.2, p.15, where the odd monic curve map is identified with the Jacobian Kummer map restricted along P↦[P−infinity]. This construction works over the present good odd residue field; for the proof here it is enough that the resulting homomorphism kills doubles. [Primary source](https://www.mathe2.uni-bayreuth.de/stoll/papers/Ohrid2014-Stoll.pdf)

The group-theoretic conclusion is short. Write A=J(K), H=<D0,D1,D2,D3>, H0=<D0,D1,D2,D3'>. The trace/anti-trace identity gives 2A⊆H0, and the verified relation D3'=9D0+3D1−D2−2D3 gives H0⊆H. The rank-three and torsion-C10 conclusions give dim A/2A=4. The witness gives four independent images from H, hence A=H+2A=H. No unsupported upper bound on a gluing index is used.

A manuscript-ready replacement is `section7_basis_kummer_repair.tex`. This audit does not independently rerun the two original Magma Mordell–Weil computations; their rigorous rank/torsion/generation output remains a separate input. It does independently and exactly settle the previously missing 2-saturation step.
