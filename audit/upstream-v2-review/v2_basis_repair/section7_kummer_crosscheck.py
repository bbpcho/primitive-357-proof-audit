"""Independent fixed-prime cross-check of the proposed Section 7 basis repair.

Uses direct derivative evaluation at the branch point and a table of squares,
not the search program's product/Legendre-power implementation.
"""
import json
from pathlib import Path
from fractions import Fraction

p=173;theta=22;a=-36
assert all(p%d for d in range(2,14)) and theta*theta%p==(-35)%p
g=[1679616,373248,28512,864,9,1]  # ascending; exact transformed sextic
f=[0,-36,9,-24,22,-8,1]
assert [Fraction(a)**(4-i)*f[6-i] for i in range(6)]==g
def ev(poly,t):
    z=0
    for c in reversed(poly):z=(z*t+c)%p
    return z
roots=[r for r in range(p) if ev(g,r)==0]
assert roots==[15,90,119,122,164]
gp=[i*g[i] for i in range(1,len(g))]
assert all(ev(gp,r) for r in roots)
def div(x,y):return x*pow(y%p,-1,p)%p
r0=div(a,4);u1=-a%p;u3=div(30*a,theta+85)
squares={x*x%p for x in range(1,p)}
columns=[[],[],[],[]]
for r in roots:
    numerator0=ev(gp,r) if r==r0 else (r0-r)%p
    vals=[div(numerator0,-r),div(u1-r,-r),ev([a*a,-3*a,1],r),div(u3-r,-r)]
    assert all(vals)
    for col,val in zip(columns,vals):col.append(val)
bits=[[int(v not in squares) for v in col] for col in columns]
rows=list(map(list,zip(*bits)))
# Every nonzero linear combination is nonzero: exhaustive 15-vector proof.
images=[]
for mask in range(1,16):
    image=[sum(row[j] for j in range(4) if mask>>j&1)%2 for row in rows]
    assert any(image)
    images.append(image)
assert len({tuple(v) for v in images})==15
assert all(sum(col)%2==0 for col in bits)
data=json.loads((Path(__file__).with_name('independent_basis_kummer.json')).read_text())
w=data['selected'][0]
assert w['values_columns_D0_D1_D2_D3']==columns
assert w['bit_columns_D0_D1_D2_D3']==bits and w['rows']==rows
print('ODD_MODEL_COEFFICIENTS_ASCENDING',g)
print('P173_SMOOTH_SPLIT_BRANCH_ROOTS',roots)
print('BRANCH_D0_U',r0,'D1_U',u1,'D3_U',u3)
print('KUMMER_VALUE_COLUMNS',columns)
print('KUMMER_BIT_ROWS',rows)
print('ALL_15_NONZERO_COMBINATIONS_DISTINCT_NONZERO=PASS')
print('INDEPENDENT_CROSSCHECK=PASS_RANK4_WITNESS')
