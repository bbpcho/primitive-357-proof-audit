Q := Rationals(); Qx<x> := PolynomialRing(Q);
K<th> := NumberField(x^4 - 4*x^3 + 6*x^2 + 9);
KX<X> := PolynomialRing(K);
fK := X^4 - 4*X^3 + 6*X^2 + 9; g := fK div (X-th);
E1c := HyperellipticCurve(-35*X*g); O1 := E1c![0,0,1];
E1a,phi1 := EllipticCurve(E1c,O1);
a2 := (-2*th^3+5*th^2-12*th+57)/6; a3 := -3*th+3;
a4 := (31*th^3+110*th^2-1299*th+3114)/6;
a6 := (2509*th^3-10861*th^2+16341*th+5445)/6;
E1 := EllipticCurve([K|0,a2,a3,a4,a6]); iso1 := Isomorphism(E1a,E1);
P1 := E1![(-th^3+7*th^2-12)/3,
          (13*th^3-63*th^2+83*th+29)/2,1];
P2 := E1![(-5*th^3+26*th^2-69*th+12)/6,
          (-8*th^3+39*th^2-90*th+41)/2,1];
P3 := E1![(82*th^3+345*th^2-3078*th+5013)/81,
          (-16906*th^3+208815*th^2-683064*th+846999)/1458,1];
lo,hi := RankBounds(E1); Tor,tor_map := TorsionSubgroup(E1);
assert hi eq 3; assert Invariants(Tor) eq [];
assert &and[Order(P) eq 0:P in [P1,P2,P3]];
ind := IsLinearlyIndependent([P1,P2,P3]); assert ind;
G := FreeAbelianGroup(3);
Gmap := map<G->E1|a:->&+[Integers()!Eltseq(a)[i]*[P1,P2,P3][i]:i in [1..3]]>;
Pone := ProjectiveSpace(Q,1);
E1c_to_Pone := map<E1c->Pone|[E1c.1,E1c.3]>;
E1_to_Pone := Expand(Inverse(iso1)*Inverse(phi1)*E1c_to_Pone);
V,R := Chabauty(Gmap,E1_to_Pone:
  InertiaDegreeBound:=4,SmoothBound:=100,PrimeBound:=30,InitialPrimes:=30);
Xs := {E1_to_Pone(Gmap(v)):v in V};
assert Xs eq {Pone![0,1],Pone![35,9]};
assert R eq 6592880678883323322765152793600;
assert Max(PrimeDivisors(R)) eq 97;
Sat := Saturation([P1,P2,P3],97:TorsionFree:=true);
assert Sat eq [P1,P2,P3];
print "E1_RANK_BOUNDS",lo,hi;
print "E1_TORSION_INVARIANTS",Invariants(Tor);
print "E1_GENERATORS_INDEPENDENT",ind;
print "E1_EXACT_RANK_FROM_UPPER_BOUND_AND_INDEPENDENCE",3;
print "E1_GLOBAL_CHABAUTY_V",V;
print "E1_GLOBAL_CHABAUTY_R",R;
print "E1_GLOBAL_R_FACTORIZATION",Factorization(R);
print "E1_RATIONAL_X",Xs;
print "E1_SATURATION_THROUGH_97_UNCHANGED",Sat eq [P1,P2,P3];
print "CLASS41_STATUS=PASS_GLOBAL_CHABAUTY_AND_INDEX_DISCHARGE";
