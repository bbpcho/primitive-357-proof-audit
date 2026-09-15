/* Exact Magma reconstruction of the rational and twisted Mordell--Weil
   computations used in Dahmen--Siksek, Lemma 7.3.

   This script requires Magma's rigorous MordellWeilGroupGenus2 intrinsic.
   The two returned maps have inverses; the subgroup assertions therefore
   check the named generators, rather than only the abstract ranks.
*/

Q := Rationals();
R<X> := PolynomialRing(Q);
f := X*(X-4)*(X^4-4*X^3+6*X^2+9);

/* The untwisted Jacobian. */
C := HyperellipticCurve(f);
J := Jacobian(C);
infinity_plus := C![1,1,0];
infinity_minus := C![1,-1,0];
P4 := C![4,0,1];
P5 := C![-1,10,1];
D0 := J![P4,infinity_minus];
D1 := J![P5,infinity_plus];

SetSeed(1);
A, toJ, finite_index, proved, rank_bound :=
    MordellWeilGroupGenus2(J : MaxIndex:=2000, MaxBound:=10000,
                               BoundC:=10000);
assert finite_index and proved and rank_bound eq 1;
assert AbelianInvariants(A) eq [ 10, 0 ];
a0 := D0 @@ toJ;
a1 := D1 @@ toJ;
assert sub< A | a0, a1 > eq A;
assert Order(a0) eq 10 and Order(a1) eq 0;
print "UNTWISTED_GROUP", AbelianInvariants(A);
print "UNTWISTED_NAMED_COORDINATES", Eltseq(a0), Eltseq(a1);
print "UNTWISTED_PROVED", finite_index, proved, rank_bound;

/* The -35 twist.  Multiplying a twist Mumford y-polynomial by 1/theta
   gives the corresponding polynomial on C. */
Ct := HyperellipticCurve(-35*f);
Jt := Jacobian(Ct);
E0 := Jt![X^2-4*X, 0];
E2 := Jt![X^2-3*X+1, 35*X-35];
E3prime := Jt![X^2-963/281*X+336/281,
                (1191750*X+1265880)/78961];

SetSeed(1);
At, toJt, finite_index_t, proved_t, rank_bound_t :=
    MordellWeilGroupGenus2(Jt : MaxIndex:=2000, MaxBound:=10000,
                                BoundC:=10000);
assert finite_index_t and proved_t and rank_bound_t eq 2;
assert AbelianInvariants(At) eq [ 2, 0, 0 ];
e0 := E0 @@ toJt;
e2 := E2 @@ toJt;
e3 := E3prime @@ toJt;
assert sub< At | e0, e2, e3 > eq At;
assert Order(e0) eq 2 and Order(e2) eq 0 and Order(e3) eq 0;
print "TWISTED_GROUP", AbelianInvariants(At);
print "TWISTED_NAMED_COORDINATES", Eltseq(e0), Eltseq(e2), Eltseq(e3);
print "TWISTED_PROVED", finite_index_t, proved_t, rank_bound_t;
print "SECTION7_LEMMA_7_3_MAGMA=PASS_RIGOROUS_FULL_GROUPS_AND_NAMED_GENERATORS";
