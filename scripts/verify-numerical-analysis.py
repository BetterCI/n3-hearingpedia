"""Definition-based and independent-route checks for specified teaching examples."""
from pathlib import Path
from decimal import Decimal,localcontext
from fractions import Fraction as F
import sys,importlib.util,json,math,hashlib,xml.etree.ElementTree as ET
sys.dont_write_bytecode=True
import numpy as np
import scipy
from scipy import linalg,integrate,interpolate,sparse
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/numerical-analysis-2026-11-02'
spec=importlib.util.spec_from_file_location('models',ROOT/'public/code/numerical-analysis/experiments.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def close(a,b,tol=1e-10):np.testing.assert_allclose(a,b,atol=tol,rtol=tol)
def record(name,**metrics):checks.append(dict(check=name,status='passed',**metrics))
rng=np.random.default_rng(20261102)
# 1 Exact binary spacing and rounding convention.
eps=np.finfo(float).eps;close(np.nextafter(1.,np.inf)-1,2.**-52,tol=0)
assert eps==2.**-52 and eps/2==2.**-53
assert np.float64(1)+np.float64(1e-16)==1
record('float64 spacing / unit roundoff / rounded 1+x',epsilon=eps,unit_roundoff=eps/2)
# 2 Dedicated logarithm, compared to the exact same binary input at 80 digits.
x,a,b,ea,eb=m.cancellation();assert np.max(ea[x<1e-16])==1 and np.max(eb)<3e-16
with localcontext() as ctx:
    ctx.prec=80;x0=Decimal.from_float(float(np.float64(1e-16)));truth=(1+x0).ln()
    err=abs(Decimal.from_float(float(np.log1p(float(x0))))-truth);assert err<Decimal('1e-30')
record('Cancellation / Decimal reference / log1p',maximum_log1p_relative_error=float(np.max(eb)))
# 3 Scalar relative conditioning by exact perturbation of x**2.
x=2.;delta=1e-7
relative_input=delta/x;relative_output=((x+delta)**2-x*x)/(x*x)
close(relative_output/relative_input,2,tol=1e-6)
record('Local scalar condition-number approximation',condition=2)
# 4 Linear residual vs actual forward error, checking the bound independently.
for delta in [1e-1,1e-4,1e-8,1e-12]:
    A=np.diag([1.,delta]);truth=np.ones(2);b=A@truth;approx=np.array([1.,0.]);r=b-A@approx
    forward=np.linalg.norm(approx-truth)/np.linalg.norm(truth);rr=np.linalg.norm(r)/np.linalg.norm(b)
    condition=np.linalg.norm(A,2)*np.linalg.norm(linalg.solve(A,np.eye(2)),2)
    assert forward<=condition*rr+1e-15
    close(forward,1/np.sqrt(2));close(rr,delta/np.sqrt(1+delta*delta))
record('Residual / normalized scale / condition-bound / nonzero forward-error counterexample')
# 5 Pivoting in a well-conditioned example, with exact rational truth.
A,b,x0,xp=m.pivot_demo();tiny=F(1,10**20)
exact=np.array([float(1/(1-tiny)),float((1-2*tiny)/(1-tiny))])
close(xp,exact);assert np.linalg.norm(A@x0-b)>.5 and np.linalg.cond(A)<3
P,L,U=linalg.lu(A);close(A,P@L@U);assert not np.allclose(P,np.eye(2))
record('Unpivoted cancellation / partial pivot / exact rational system',condition=float(np.linalg.cond(A)),unpivoted_solution=x0.tolist())
# 6 SPD and Cholesky, plus an indefinite counterexample.
T=np.diag(np.full(6,2.))+np.diag(np.full(5,-1.),1)+np.diag(np.full(5,-1.),-1)
L=np.linalg.cholesky(T);close(L@L.T,T);assert np.all(np.linalg.eigvalsh(T)>0)
try:np.linalg.cholesky(np.diag([1.,-1.]));raise AssertionError('Indefinite matrix accepted')
except np.linalg.LinAlgError:pass
record('Positive definiteness / Cholesky identity / symmetry alone insufficient')
# 7 Thin QR and squared conditioning of normal equations.
d=m.least_squares();A=d['A'];Q,R=np.linalg.qr(A,mode='reduced')
close(Q.T@Q,np.eye(2));close(Q@R,A)
assert Q.shape==(256,2) and not np.allclose(Q@Q.T,np.eye(256))
ratio=np.linalg.cond(A.T@A)/np.linalg.cond(A)**2;assert abs(ratio-1)<.01
record('Thin QR dimensions / orthogonality / normal-equation conditioning',condition=d['condition'],Gram_condition_ratio=float(ratio))
# 8 Weak direction: SVD predicts coefficient and output perturbation independently.
U,s,Vh=np.linalg.svd(A,full_matrices=False)
delta_x=Vh[-1]*(1e-4/s[-1])
close(d['perturbed']-d['clean'],delta_x,tol=1e-7)
close(A@(d['perturbed']-d['clean']),d['perturb'],tol=1e-10)
record('Least-squares weak singular direction',output_perturbation=d['perturb_norm'],coefficient_change=d['coefficient_change'])
# 9 Ridge via independent singular-value filter and its nonzero bias.
bp=d['b']+d['perturb'];lam=d['lam']
svd_ridge=Vh.T@((s/(s*s+lam))*(U.T@bp));close(svd_ridge,d['ridge'],tol=1e-9)
clean_ridge=Vh.T@((s/(s*s+lam))*(U.T@d['b']))
assert np.linalg.norm(clean_ridge-d['true'])>.1
record('Augmented ridge vs independent SVD / bias even without observation perturbation')
# 10 Bisection bracket invariants and midpoint bound.
root=m.roots()['root'];f=lambda x:np.cos(x)-x;left,right=0.,1.
for k in range(30):
    mid=(left+right)/2
    assert abs(mid-root)<=(right-left)/2+1e-14
    if f(left)*f(mid)<=0:right=mid
    else:left=mid
    assert left-1e-14<=root<=right+1e-14
    close(right-left,2.**-(k+1))
record('Bisection interval invariant / width bound',reference_root=root)
# 11 Local Newton rate and an interval contraction for cos.
dd=m.roots();err=abs(dd['newton']-root)
assert err[2]/err[1]**2<1 and err[3]/err[2]**2<1
assert np.sin(1)<.85 and .54<np.cos(1)<1
assert np.max(abs(dd['fixed'][20:]-root))<np.max(abs(dd['fixed'][:10]-root))
record('Newton pre-roundoff quadratic behavior / cos contraction on [0,1]')
# 12 Exact two-cycle, independent rational arithmetic.
x=F(0);seq=[x]
for i in range(10):x=x-(x**3-2*x+2)/(3*x*x-2);seq.append(x)
assert seq==[F(i%2) for i in range(11)] and all(x**3-2*x+2!=0 for x in seq)
record('Exact Newton two-cycle with nonzero residual')
# 13 Runge interpolant node identities and high-precision rational-node evaluation.
for cheb in [False,True]:
    x,y,p=m.runge(20,cheb);close(p(x),y,tol=1e-12)
with localcontext() as ctx:
    ctx.prec=80;n=20;xx=Decimal('0.975');nodes=[Decimal(-1)+Decimal(2*j)/n for j in range(n+1)]
    ys=[1/(1+25*t*t) for t in nodes];value=Decimal(0)
    for j in range(n+1):
        lj=Decimal(1)
        for k in range(n+1):
            if j!=k:lj*=(xx-nodes[k])/(nodes[j]-nodes[k])
        value+=ys[j]*lj
    true=1/(1+25*xx*xx);assert abs(value-true)>30
    _,_,p=m.runge(20);close(p(float(xx)),float(value),tol=1e-7)
record('Interpolation at nodes / independent 80-digit Lagrange oscillation',Runge_error_at_point975=float(abs(value-true)))
# 14 Shape and continuity via explicit piecewise polynomial derivatives.
x,y,z,cs,pc=m.splines();close(cs(x),y);close(pc(x),y);close(cs([0,3],2),[0,0])
assert cs(z).min()<-.06
for i,h in enumerate(np.diff(x)):
    c=pc.c[:,i];candidates=[0.,h]
    if c[0]!=0:
        vertex=-c[1]/(3*c[0])
        if 0<vertex<h:candidates.append(vertex)
    assert min(3*c[0]*v*v+2*c[1]*v+c[2] for v in candidates)>=-1e-12
for obj in [cs,pc]:
    for i in [1,2]:
        h=x[i]-x[i-1];left=obj.c[:,i-1];right=obj.c[:,i]
        close(((left[0]*h+left[1])*h+left[2])*h+left[3],right[3])
        close(3*left[0]*h*h+2*left[1]*h+left[2],right[2])
record('Natural endpoint curvature / exact polynomial monotonicity test / C1 knot continuity')
# 15 Finite differences and noise amplification.
a=.4;der=np.cos(a);errors=[]
for h in [.02,.01]:errors.append(abs((np.sin(a+h)-np.sin(a-h))/(2*h)-der))
assert 3.99<errors[0]/errors[1]<4.01
noise=rng.normal(0,1e-4,(150000,2));observed=np.var((noise[:,0]-noise[:,1])/(2*.001),ddof=1)
assert abs(observed/(1e-8/(2e-6))-1)<.02
record('Central difference order / independent-noise variance')
# 16 Quadrature and Richardson using exact polynomial sums.
for N in [8,16,32]:
    x=np.linspace(0,1,N+1);xx=np.linspace(0,1,2*N+1)
    q=integrate.trapezoid(x*x,x=x);fine=integrate.trapezoid(xx*xx,x=xx)
    close(q,float(F(1,3)+F(1,6*N*N)))
    close(fine+(fine-q)/3,1/3)
record('Exact trapezoid polynomial error / Richardson leading-term cancellation')
# 17 Local change of variable gives an independent narrow-peak integral.
d=m.narrow_integral();sigma=d['sigma']
local=sigma*integrate.quad(lambda u:np.exp(-u*u),-10,10,epsabs=1e-13,epsrel=1e-13)[0]
close(local,d['exact']);close(d['informed'],d['exact'])
record('Narrow peak erf expression / localized scaled quadrature',integral=d['exact'])
# 18 Misleading coarse-grid agreement and an uncertified adaptive error estimate.
assert all(row['value']<1e-10 for row in d['rows'][:3])
assert d['blind']<1e-20 and d['blind_error_estimate']<1e-20
assert abs(d['rows'][-1]['value']-d['exact'])<1e-12
record('Unresolved peak counterexample / coarse-grid plateau / adaptive estimate limitation',blind=d['blind'],blind_estimate=d['blind_error_estimate'])
# 19 Exact stiff ODE residual, with units supplied by a=1000/s and omega=1/s.
t=np.linspace(0,1,1001);y=np.cos(t)-np.exp(-1000*t);yp=-np.sin(t)+1000*np.exp(-1000*t)
close(yp,-1000*(y-np.cos(t))-np.sin(t));close(y[0],0)
record('Stiff forced ODE exact solution / initial state / two timescales')
# 20 Euler and backward Euler independently as triangular systems.
for h,implicit in [(.001,False),(.01,True),(.01,False)]:
    t,y=m.stiff_euler(h,implicit,T=.02);n=len(t)-1
    if implicit:
        mat=np.diag(np.full(n,1+1000*h))+np.diag(np.full(n-1,-1.),-1)
        rhs=h*(1000*np.cos(t[1:])-np.sin(t[1:]))
    else:
        mat=np.eye(n)+np.diag(np.full(n-1,-(1-1000*h)),-1)
        rhs=h*(1000*np.cos(t[:-1])-np.sin(t[:-1]))
    close(linalg.solve_triangular(mat,rhs,lower=True),y[1:],tol=1e-9)
assert abs(1-1000*.001)<1 and abs(1-1000*.01)>1 and abs(1/(1+1000*.01))<1
record('Explicit/implicit recurrences vs independent triangular solves / decay factors')
# 21 Euler and RK4 global order on a different exact problem.
e=[];r=[]
for N in [40,80]:
    h=1/N;e.append(abs((1-h)**N-np.exp(-1)))
    R=sum((-h)**k/math.factorial(k) for k in range(5));r.append(abs(R**N-np.exp(-1)))
assert 1.99<e[0]/e[1]<2.02 and 15.8<r[0]/r[1]<16.3
record('Euler and RK4 fixed-time global orders / amplification polynomial')
# 22 Adaptive solver output checked against exact trajectory, not against rtol alone.
rows=m.stiff_solvers();assert all(row['max_absolute_error']<1e-3 for row in rows)
record('RK45/Radau sampled global errors vs analytic trajectory',solvers=rows)
# 23 BVP discrete sine eigenmode, independent formula for the whole computed vector.
for N in [16,32,64,128]:
    x,y,err,res=m.bvp(N);h=1/N;lam=4*np.sin(np.pi*h/2)**2/(h*h)
    close(y,(np.pi**2/lam)*np.sin(np.pi*x),tol=1e-11)
    close(err,np.pi**2/lam-1,tol=1e-11)
assert m.bvp(16)[3]<1e-12 and m.bvp(16)[2]>.003
record('Discrete sine eigenvalue / analytic discrete solution / residual vs continuum error')
# 24 Nonzero boundary values must enter the RHS.
N=32;h=1/N;x=np.arange(1,N)*h
A=sparse.diags([-np.ones(N-2),2*np.ones(N-1),-np.ones(N-2)],[-1,0,1],format='csc')/(h*h)
b=np.pi**2*np.sin(np.pi*x);b[0]+=1/(h*h);b[-1]+=3/(h*h)
y=m.sla.spsolve(A,b);close(y,1+2*x+m.bvp(N)[1])
errors=np.array([m.bvp(n)[2] for n in [16,32,64,128]]);orders=np.log2(errors[:-1]/errors[1:]);assert np.all(abs(orders-2)<.01)
record('Nonzero Dirichlet terms / aligned grid errors / observed second order',orders=orders.tolist())
# 25 CG assumptions, stopping rules, and symmetric preconditioned conditioning.
A,b,rows=m.cg_demo();dense=A.toarray();np.linalg.cholesky(dense)
diag=np.diag(dense);S=dense/np.sqrt(diag[:,None]*diag[None,:])
assert np.all(np.linalg.eigvalsh(S)>0) and np.linalg.cond(S)<np.linalg.cond(dense)
for row in rows:
    assert row['info']==0 and row['final_relative_residual']<=1e-10
    assert row['relative_forward_error']<1e-5
assert rows[1]['iterations']<rows[0]['iterations']
record('SPD CG / inverse Jacobi action / symmetric conditioning / actual stopping',iterations=[r['iterations'] for r in rows])
# 26 Spectral radius below one allows transient norm growth for a nonnormal iteration.
G=np.array([[.5,10.],[0,.5]]);v=np.array([0.,1.]);values=[np.linalg.norm(v)]
for n in range(100):v=G@v;values.append(np.linalg.norm(v))
assert max(abs(np.linalg.eigvals(G)))<1 and values[1]>values[0] and values[-1]<1e-20
record('Stationary iteration spectral radius / transient growth counterexample')
# 27 Check source hashes and original figure XML.
sources=json.loads((REC/'source-index.json').read_text(encoding='utf-8'))
assert len(sources)==25 and all(r['status']=='fetched' for r in sources)
for row in sources:
    data=(ROOT/'artifacts/numerical-analysis/sources'/(row['id']+'.html')).read_bytes()
    assert hashlib.sha256(data).hexdigest()==row['sha256']
figs=list((ROOT/'public/figures/numerical-analysis').glob('*.svg'));assert len(figs)==10
for p in figs:ET.parse(p)
ET.parse(ROOT/'public/figures/foundation-courses/numerical-analysis.svg')
record('25 retrieved source hashes / 10 teaching SVGs / native course sketch')
result=dict(status='passed',check_groups=len(checks),numpy=np.__version__,scipy=scipy.__version__,checks=checks,
    limitations='Specified finite checks complement mathematical arguments; not external professional review, certified interval bounds, or device/listener measurements.')
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status='passed',check_groups=len(checks),numpy=np.__version__,scipy=scipy.__version__)))
