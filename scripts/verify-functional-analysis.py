"""Checks of specified examples and independent formulations, not proofs of general FA theorems."""
from pathlib import Path
import importlib.util,sys,json
sys.dont_write_bytecode=True
import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve_banded
from scipy.optimize import minimize_scalar
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/functional-analysis-2026-11-02'
spec=importlib.util.spec_from_file_location('models',ROOT/'public/code/functional-analysis/experiments.py')
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
checks=[]
def check(name,ok,detail=None):checks.append(dict(name=name,passed=bool(ok),detail=detail))
def close(name,a,b,atol=1e-10,rtol=1e-7):
    err=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    check(name,np.allclose(a,b,atol=atol,rtol=rtol),dict(max_abs_error=err))
def cq(fun,a=0,b=1):
    return quad(lambda t:np.real(fun(t)),a,b,epsabs=1e-12)[0]+1j*quad(lambda t:np.imag(fun(t)),a,b,epsabs=1e-12)[0]
# Norm geometry and comparison, explicit vectors attaining constants.
for N in [1,2,8,50,200]:
    vec=np.ones(N)
    close(f'finite norm comparison attains sqrt N, N={N}',np.linalg.norm(vec)/np.max(abs(vec)),np.sqrt(N))
for p in [1,2,np.inf]:
    z=np.array([1.2,-.3])
    close(f'norm homogeneity p={p}',np.linalg.norm(-2.4*z,ord=p),2.4*np.linalg.norm(z,ord=p))
close('L2 parallelogram identity',np.linalg.norm([2.,1.])**2+np.linalg.norm([0.,1.])**2,2*np.linalg.norm([1.,1.])**2+2*np.linalg.norm([1.,0.])**2)
check('L1 norm fails parallelogram for coordinate unit vectors',np.linalg.norm([1.,1.],1)**2+np.linalg.norm([1.,-1.],1)**2!=4)
# Continuous ramp completion and point-evaluation counterexample by quadrature.
for n in [2,4,8,32,128]:
    error=quad(lambda t:(model.ramp(t,n)-(t>.5))**2,0,1,points=[.5,.5+1/n],epsabs=1e-13)[0]
    close(f'ramp L2 error squared n={n}',error,1/(3*n))
    norm2=quad(lambda t:model.spike(t,n)**2,0,1,points=[.5-1/n,.5,.5+1/n],epsabs=1e-13)[0]
    close(f'triangular spike L2 norm squared n={n}',norm2,2/(3*n))
    close(f'triangular spike retains point value n={n}',model.spike(.5,n),1)
    area=quad(lambda t:model.spike(t,n),0,1,points=[.5-1/n,.5,.5+1/n],epsabs=1e-13)[0]
    close(f'triangular spike L1 area n={n}',area,1/n)
    derivative2=quad(lambda t:n*n,.5-1/n,.5)[0]+quad(lambda t:n*n,.5,.5+1/n)[0]
    close(f'spike weak derivative squared norm n={n}',derivative2,2*n)
for n,m in [(4,8),(8,32),(32,128)]:
    d=quad(lambda t:(model.ramp(t,n)-model.ramp(t,m))**2,0,1,points=[.5,.5+1/n,.5+1/m],epsabs=1e-13)[0]**.5
    check(f'ramp pairwise Cauchy error bound n={n},m={m}',d<=np.sqrt(1/(3*n))+np.sqrt(1/(3*m)))
# Hilbert projection: independent continuous quadrature and basis.
e=[lambda t:np.sqrt(2)*np.sin(2*np.pi*t),lambda t:np.sqrt(2)*np.cos(4*np.pi*t)]
for i in range(2):
    for j in range(2):close(f'projection Gram i={i},j={j}',quad(lambda t:e[i](t)*e[j](t),0,1)[0],float(i==j))
coef=np.array([quad(lambda t:ee(t)*model.signal(t),0,1)[0] for ee in e])
close('projection coefficients',coef,[1/np.sqrt(2),.4/np.sqrt(2)])
close('signal squared norm',quad(lambda t:model.signal(t)**2,0,1)[0],.6)
close('projection squared norm',quad(lambda t:model.projection(t)**2,0,1)[0],.58)
close('residual squared norm',quad(lambda t:(model.signal(t)-model.projection(t))**2,0,1)[0],.02)
for i in range(2):close(f'orthogonal residual i={i}',quad(lambda t:e[i](t)*(model.signal(t)-model.projection(t)),0,1)[0],0)
for a,b in [(0.,0.),(.1,-.2),(-1.,.3)]:
    err=quad(lambda t:(model.signal(t)-model.projection(t)-a*e[0](t)-b*e[1](t))**2,0,1)[0]
    close(f'projection optimality error decomposition a={a},b={b}',err,.02+a*a+b*b)
# Infinite tail by an independent integral representation.
for N in [1,5,20,100,1000]:
    integral=quad(lambda x:x**N*(-np.log(x))/(1-x) if 0<x<1 else (1. if x==1 else 0.),0,1,epsabs=1e-12)[0]
    algebra=np.pi**2/6-np.sum(1/np.arange(1,N+1,dtype=float)**2)
    close(f'1/n coefficients squared tail N={N}',algebra,integral,atol=2e-12)
# Differentiation norms and integration by parts with a nontrivial complex field.
for n in [1,3,12,30]:
    f=lambda t:np.sqrt(2)*np.sin(n*np.pi*t);df=lambda t:np.sqrt(2)*n*np.pi*np.cos(n*np.pi*t)
    l2=quad(lambda t:f(t)**2,0,1,epsabs=1e-11)[0]
    der=quad(lambda t:df(t)**2,0,1,epsabs=1e-9)[0]
    close(f'unit sine L2 n={n}',l2,1)
    close(f'derivative L2 n={n}',np.sqrt(der),n*np.pi)
    close(f'vanishing input nonvanishing derivative n={n}',np.sqrt(der)/n,np.pi)
    check(f'derivative bounded in graph norm n={n}',np.sqrt(der/(l2+der))<=1)
f=lambda x:(1+2j)*x*(1-x);df=lambda x:(1+2j)*(1-2*x)
g=lambda x:(1-.3j)*(1+x*x);dg=lambda x:(1-.3j)*2*x
close('complex integration by parts with zero input trace',cq(lambda x:np.conj(df(x))*g(x)),-cq(lambda x:np.conj(f(x))*dg(x)))
# Complex weighted adjoint and correct variable of linearity.
A,M,W,adj=model.weighted_adjoint();rng=np.random.default_rng(102)
for k in range(6):
    x=rng.normal(size=2)+1j*rng.normal(size=2);y=rng.normal(size=2)+1j*rng.normal(size=2)
    close(f'weighted adjoint identity sample={k}',np.vdot(A@x,W@y),np.vdot(x,M@(adj@y)))
x=np.array([1+.2j,-.4j]);y=np.array([.3j,2-1j])
check('bare conjugate transpose fails for weighted inner products',not np.isclose(np.vdot(A@x,W@y),np.vdot(x,M@(A.conj().T@y))))
v=np.array([1+2j,-.4j]);gg=np.array([.3j,2-1j]);z=.4+1.2j
close('Riesz functional linear in input',np.vdot(gg,z*v),z*np.vdot(gg,v))
close('Riesz correspondence conjugate linear in representing vector',np.vdot(z*gg,v),np.conj(z)*np.vdot(gg,v))
close('Riesz norm attained at aligned unit vector',abs(np.vdot(gg,gg/np.linalg.norm(gg))),np.linalg.norm(gg))
# Finite-window averaging functional norm and preservation of area.
for eps in [.5,.2,.05,.01]:
    aa=.5-eps/2;bb=.5+eps/2
    close(f'window area eps={eps}',quad(lambda t:1/eps,aa,bb)[0],1)
    norm=quad(lambda t:1/eps**2,aa,bb)[0]**.5
    close(f'window Riesz norm eps={eps}',norm,1/np.sqrt(eps))
    close(f'window functional norm attained eps={eps}',quad(lambda t:(1/eps)**2/norm,aa,bb)[0],norm)
# Nonunique norm-preserving Hahn-Banach extensions in R2 with sup norm.
for a in [0,.2,.5,.8,1.]:
    gvec=np.array([a,1-a]);corners=np.array([[1,1],[1,-1],[-1,1],[-1,-1]])
    close(f'HB extension norm a={a}',np.max(abs(corners@gvec)),1)
    for t in [-.4,1.3]:close(f'HB extension agrees on line a={a},t={t}',np.dot(gvec,[t,t]),t)
# Standard basis: fixed test vector and distances; not a theorem proof from finite truncation.
for n in [1,3,10,30]:
    ee=np.zeros(100);ee[n-1]=1;test=1/np.arange(1,101,dtype=float)
    close(f'weak-example vector norm n={n}',np.linalg.norm(ee),1)
    close(f'weak-example fixed readout n={n}',np.dot(test,ee),1/n)
    other=np.zeros(100);other[n]=1
    close(f'orthonormal basis pair distance n={n}',np.linalg.norm(ee-other),np.sqrt(2))
# Projection truncations converge strongly on this test vector but not in norm.
for N in [1,5,20,50]:
    P=np.diag(np.r_[np.ones(N),np.zeros(100-N)])
    close(f'I-P operator norm finite witness N={N}',np.linalg.norm(np.eye(100)-P,2),1)
# Multiplication operator approximate eigenvectors; continuous integrals.
for lam in [.2,.5,.8]:
    for eps in [.1,.03,.01]:
        close(f'M=t approximate eigenvector norm lam={lam},eps={eps}',quad(lambda t:1/(2*eps),lam-eps,lam+eps)[0],1)
        residual=quad(lambda t:(t-lam)**2/(2*eps),lam-eps,lam+eps,epsabs=1e-13)[0]**.5
        close(f'M=t approximate eigenvector residual lam={lam},eps={eps}',residual,eps/np.sqrt(3))
# Green eigenrelations by independent kernel quadrature.
for n in range(1,7):
    for x in [.1,.37,.8]:
        integrated=quad(lambda xi:model.green(x,xi)*np.sqrt(2)*np.sin(n*np.pi*xi),0,1,points=[x],epsabs=1e-12)[0]
        close(f'Green eigenrelation n={n},x={x}',integrated,np.sqrt(2)*np.sin(n*np.pi*x)/(n*np.pi)**2)
for xi in [.2,.5,.8]:
    eps=1e-6
    jump=(model.green(xi+eps,xi)-model.green(xi,xi))/eps-(model.green(xi,xi)-model.green(xi-eps,xi))/eps
    close(f'Green derivative jump xi={xi}',jump,-1,atol=1e-9)
for N in [5,20,60]:
    exactnorm=1/((N+1)*np.pi)**2
    diag=1/(np.arange(1,301)*np.pi)**2;tail=diag.copy();tail[:N]=0
    close(f'Green finite-rank norm-tail witness N={N}',np.max(abs(tail)),exactnorm)
# FEM/Galerkin: separate band solve, exact derivative integral and functional.
for n in [1,2,5]:
    norm2=quad(lambda t:2*np.sin(n*np.pi*t)**2,0,1)[0]
    der2=quad(lambda t:2*(n*np.pi)**2*np.cos(n*np.pi*t)**2,0,1)[0]
    check(f'unit interval Poincare bound mode={n}',norm2<=der2/np.pi**2+1e-10)
    check(f'H1 coercivity constant mode={n}',der2>=(np.pi**2/(1+np.pi**2))*(norm2+der2)-1e-9)
for N in [4,8,16,32,64]:
    d=model.galerkin(N);h=1/N
    ab=np.zeros((3,N-1));ab[1]=2/h;ab[0,1:]=-1/h;ab[2,:-1]=-1/h
    other=solve_banded((1,1),ab,np.full(N-1,h))
    close(f'Galerkin independent tridiagonal solve N={N}',d['u'][1:-1],other)
    close(f'Galerkin nodal values N={N}',d['u'],d['x']*(1-d['x'])/2)
    energy=0.;functional=0.;weak=0.
    for j in range(N):
        aa=j*h;bb=(j+1)*h;slope=d['slopes'][j];uj=d['u'][j]
        energy+=quad(lambda x:(slope-(.5-x))**2,aa,bb,epsabs=1e-14)[0]
        functional+=quad(lambda x:.5*slope*slope-(uj+slope*(x-aa)),aa,bb,epsabs=1e-14)[0]
    close(f'Galerkin derivative error integral N={N}',energy,d['energy_error2'],atol=1e-13)
    close(f'Galerkin independent functional integral N={N}',functional,d['J'])
    close(f'Galerkin energy identity N={N}',functional+1/24,.5*energy,atol=1e-12)
    close(f'Galerkin algebraic weak equation N={N}',d['K']@d['u'][1:-1],d['load'])
# Tikhonov: augmented least squares, stationarity, exact bias/noise split and gain bound.
for alpha in [1e-2,1e-3,1e-4,1e-6]:
    d=model.regularization(alpha);s=d['sigma'];A=np.diag(s);y=d['y'];x=d['estimate']
    aug=np.vstack([A,np.sqrt(alpha)*np.eye(len(s))]);rhs=np.r_[y,np.zeros(len(s))]
    independent=np.linalg.lstsq(aug,rhs,rcond=None)[0]
    close(f'Tikhonov augmented least-squares alpha={alpha}',x,independent,atol=1e-11)
    close(f'Tikhonov gradient alpha={alpha}',A.T@(A@x-y)+alpha*x,0,atol=1e-12)
    bias=-alpha*d['truth']/(s*s+alpha);noise=s*d['eta']/(s*s+alpha)
    close(f'Tikhonov error bias plus propagated noise alpha={alpha}',x-d['truth'],bias+noise)
    check(f'Tikhonov noise bound alpha={alpha}',np.linalg.norm(noise)<=np.linalg.norm(d['eta'])/(2*np.sqrt(alpha))*(1+1e-12))
    gain=s/(s*s+alpha)
    check(f'Tikhonov discrete gain bound alpha={alpha}',max(gain)<=1/(2*np.sqrt(alpha))*(1+1e-12))
    objective=np.linalg.norm(A@x-y)**2+alpha*np.linalg.norm(x)**2
    truthobj=np.linalg.norm(d['eta'])**2+alpha*np.linalg.norm(d['truth'])**2
    check(f'Tikhonov objective beats true-vector trial alpha={alpha}',objective<=truthobj+1e-13)
    close(f'Tikhonov maximum gain at sqrt alpha={alpha}',np.sqrt(alpha)/(alpha+alpha),1/(2*np.sqrt(alpha)))
d=model.regularization()
close('prescribed deterministic noise norm',np.linalg.norm(d['eta']),.001)
check('specified regularization improves coefficient error',d['regularized_error']<d['raw_error'])
# Banach contraction example and both a priori/a posteriori error bounds.
q=.4;fixed=1/(1-q);x=-2.;first=abs((q*x+1)-x)
for n in range(1,17):
    prev=x;x=q*x+1;err=abs(x-fixed)
    check(f'contraction a priori bound n={n}',err<=q**n/(1-q)*first+1e-14)
    check(f'contraction a posteriori bound n={n}',err<=q/(1-q)*abs(x-prev)+1e-14)
# Sources and original SVG structure.
sources=json.loads((REC/'source-index.json').read_text(encoding='utf-8'))
check('22 primary author or official course sources retrieved',len(sources)==22 and all(s['status']=='fetched' for s in sources))
for path in sorted((ROOT/'public/figures/functional-analysis').glob('*.svg')):
    try:ET.parse(path);ok=True
    except ET.ParseError:ok=False
    check('SVG XML '+path.name,ok)
check('10 teaching figures present',len(list((ROOT/'public/figures/functional-analysis').glob('*.svg')))==10)
ET.parse(ROOT/'public/figures/foundation-courses/functional-analysis.svg');check('course thumbnail valid SVG',True)
result=dict(scope='Independent quadrature, matrices, kernels, variational energy and optimization for specified examples. Not proofs of abstract theorems, physical/clinical validation or external professional review.',total=len(checks),passed=sum(c['passed'] for c in checks),checks=checks)
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for c in checks:
    if not c['passed']:print('FAIL',c)
print(json.dumps(dict(total=result['total'],passed=result['passed'])))
if result['passed']!=result['total']:raise SystemExit(1)
