Q<x>:=PolynomialRing(Rationals());
f:=x^6-6*x^5+69*x^4-38*x^3+6*x^2-240*x+1057;
J:=Jacobian(HyperellipticCurve(f));
D1:=J![x^2-x-8/3,-70*x/3+35/3];
D2:=J![x^2-x-26,-245];
D3:=J![x^2-7*x/2+3/2,55*x/4+95/4];
print "MW_FINAL_SEARCH_BEGIN";
H:=HeightPairingMatrix([D1,D2,D3] : Precision:=80);
print "HEIGHT_PAIRING",H;
print "REGULATOR",Determinant(H);
Pts:=Points(J : Bound:=15);
print "POINT_COUNT",#Pts;
for P in Pts do
  print "POINT",P,"NAIVE",NaiveHeight(P),"CANONICAL",Height(P : Precision:=80);
end for;
print "MW_FINAL_SEARCH_END";
