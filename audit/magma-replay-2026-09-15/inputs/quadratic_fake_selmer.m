Q := Rationals();
Qx<x> := PolynomialRing(Q);
f := x^4 - 4*x^3 + 6*x^2 + 9;
C := HyperellipticCurve(-35*x*(x-4)*f);
Hk, AtoHk := TwoCoverDescent(C);
A := Domain(AtoHk); T := A.1;
d40 := A!(-3 + 27/35*T + 6*T^2 - 192/35*T^3
              + 209/105*T^4 - 26/105*T^5);
d41 := A!(-35 + 9*T - 24*T^2 + 22*T^3 - 8*T^4 + T^5);
d42 := A!(-35 + 267/35*T - 20*T^2 + 1934/105*T^3
               - 706/105*T^4 + 89/105*T^5);
assert #Hk eq 3;
assert #{AtoHk(d40),AtoHk(d41),AtoHk(d42)} eq 3;
assert {AtoHk(d40),AtoHk(d41),AtoHk(d42)} eq Hk;
print "TWO_COVER_DESCENT_CLASSES", #Hk;
print "FAKE_SELMER_STATUS=PASS_EXACT_THREE_CLASSES";
