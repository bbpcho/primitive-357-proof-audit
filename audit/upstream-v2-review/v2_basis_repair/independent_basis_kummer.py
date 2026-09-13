"""Search exact local Kummer witnesses for Section 7 two-saturation.

Odd monic model u=a/x, v=a²*y/x³, a=-36, v²=g(u).
Original infinities both map to u=0; their v signs do not affect Kummer.
All arithmetic is in prime finite fields, with explicit branch handling.
"""
from pathlib import Path
import json
B=Path(__file__).resolve().parent
A=-36
def primes(n):
 sieve=[True]*(n+1);sieve[0]=sieve[1]=False
 for p in range(2,n+1):
  if sieve[p]:
   yield p
   for j in range(p*p,n+1,p):sieve[j]=False
def rank(rows,n=4):
 piv={}
 for row in rows:
  x=sum((v&1)<<i for i,v in enumerate(row))
  while x:
   b=x.bit_length()-1
   if b in piv:x^=piv[b]
   else:piv[b]=x;break
 return len(piv)
def f(x,p):return x*(x-4)*(x**4-4*x**3+6*x*x+9)%p
def g(u,p):
 z=u*pow(A,-1,p)%p
 return A**4*(1-4*z)*(1-4*z+6*z*z+9*z**4)%p
def witness(p,theta,roots):
 a=A%p;ri=a*pow(4,-1,p)%p
 up=30*a*pow((theta+85)%p,-1,p)%p
 x3=(theta+85)*pow(30,-1,p)%p;y3=(2303*theta-595)*pow(1350,-1,p)%p
 assert y3*y3%p==f(x3,p)
 assert g(0,p)==a**4%p
 columns=[[],[],[],[]];values=[[],[],[],[]]
 for r in roots:
  d0=1
  if r==ri:
   for s in roots:
    if s!=r:d0=d0*(r-s)%p
  else:d0=(ri-r)%p
  ds=[d0*pow(-r,-1,p)%p,(-a-r)*pow(-r,-1,p)%p,(r*r-3*a*r+a*a)%p,(up-r)*pow(-r,-1,p)%p]
  if any(x==0 for x in ds):return None
  for j,x in enumerate(ds):
   leg=pow(x,(p-1)//2,p);assert leg in (1,p-1)
   values[j].append(x);columns[j].append(0 if leg==1 else 1)
 # Each Kummer norm is a square: the sum in every column is zero.
 assert all(sum(c)%2==0 for c in columns),(p,theta,values,columns)
 rows=list(map(list,zip(*columns)))
 return {'p':p,'theta':theta,'odd_branch_roots':roots,'values_columns_D0_D1_D2_D3':values,'bit_columns_D0_D1_D2_D3':columns,'rows':rows,'rank':rank(rows)}
def main():
 attempts=[];acc=[];selected=[]
 for p in primes(10000):
  if p in (2,3,5,7,11):continue
  theta=next((x for x in range(p) if (x*x+35)%p==0),None)
  if theta is None:continue
  xs=[x for x in range(1,p) if f(x,p)==0]
  if len(xs)!=5:continue
  roots=sorted(A*pow(x,-1,p)%p for x in xs)
  assert len(set(roots))==5 and all(g(r,p)==0 for r in roots)
  # g is monic of degree five since a=-36.
  for t in (0,1,2,3):
   prod=1
   for r in roots:prod=prod*(t-r)%p
   assert prod==g(t,p)
  for th in sorted({theta,(-theta)%p}):
   w=witness(p,th,roots)
   if w is None:continue
   attempts.append(w)
   old=rank(acc);acc+=w['rows'];new=rank(acc)
   if new>old:selected.append(w)
   print('KUMMER',p,th,'local_rank',w['rank'],'combined_rank',new,flush=True)
   if new==4:
    out={'status':'RANK4_WITNESS','selected':selected,'attempts':attempts}
    (B/'independent_basis_kummer.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2));return
 out={'status':'BOUNDED_SEARCH_NO_RANK4','rank':rank(acc),'selected':selected,'attempts':attempts}
 (B/'independent_basis_kummer.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
