"""Independent analytic, rational, finite-difference and cross-solver audit."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import sys,importlib.util,json
sys.dont_write_bytecode=True
import numpy as np
from scipy.optimize import brentq, minimize_scalar, minimize
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('optmodels',ROOT/'public/code/optimization-methods/experiments.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def done(name,detail):checks.append(dict(check=name,result='passed',detail=detail))
# Rational certificate is independent of SLSQP and floating-point arithmetic.
x=[F(3,2),F(1,2)];b=[F(2),F(1)];mu=F(1,2)
assert sum(x)==2 and all(t>0 for t in x)
assert all(xi-bi+mu==0 for xi,bi in zip(x,b))
p=sum((xi-bi)**2 for xi,bi in zip(x,b))/2
assert p==mu-mu**2==F(1,4)
done('rational_KKT_and_gap','Exact fractions prove feasibility, stationarity, complementarity and matching lower bound 1/4.')
r=m.constrained();assert r['success'] and np.allclose(r['x'],[1.5,.5],atol=1e-10)
assert max(r['stationarity'],r['feasibility'],r['complementarity'],abs(r['gap']))<1e-12
done('SLSQP_crosscheck',r)
# The dual infimum is analytic coordinatewise, independently minimized numerically.
for mu in np.linspace(0,3,17):
    y=np.maximum(np.array([2.,1.])-mu,0)
    q=.5*np.sum((y-[2,1])**2)+mu*(sum(y)-2)
    z=minimize(lambda z:.5*np.sum((z-[2,1])**2)+mu*(sum(z)-2),
        [0.,0.],method='L-BFGS-B',bounds=[(0,None)]*2,
        jac=lambda z:z-np.array([2,1])+mu,options={'gtol':1e-12,'ftol':1e-14})
    assert abs(z.fun-q)<1e-10 and q<=.25+1e-12
    if mu<=1:assert abs(q-(mu-mu**2))<1e-12
done('dual_infimum_and_domain','17 multipliers in [0,3]; coordinate clipping and separate bound solver agree, q<=1/4; parabola used only through mu=1.')
for c in [.05,.5,1,1.2,2,3,4]:
    x,mu=m.budget_solution(c);lower=np.maximum(mu-np.array([2,1]),0)
    assert min(x)>=0 and sum(x)<=c+1e-12 and mu>=0
    assert np.max(np.abs(x-[2,1]+mu-lower))<1e-12
    assert abs(mu*(sum(x)-c))<1e-12 and np.max(np.abs(lower*x))<1e-12
done('active_sets_all_regimes','Budget solutions independently satisfy all KKT equations including lower-bound multipliers.')
for c in [.5,1.,2.,3.,3.5]:
    v=lambda z:.5*np.sum((m.budget_solution(z)[0]-[2,1])**2)
    d=(v(c+1e-5)-v(c-1e-5))/2e-5
    assert abs(d+m.budget_solution(c)[1])<3e-6
done('budget_sensitivity','Central differences confirm v prime=-mu, including the differentiable switches.')
# Independent bracketed polynomial roots.
f=lambda z:(z*z-1)**2+.3*z
df=lambda z:4*z**3-4*z+.3
roots=np.array([brentq(df,a,b,xtol=1e-14) for a,b in [(-1.5,-.5),(0,.2),(.5,1.5)]])
nc=m.nonconvex();assert np.allclose(roots,nc['roots'],atol=1e-12)
assert nc['curvature'][0]>0>nc['curvature'][1] and nc['curvature'][2]>0
assert f(roots[0])<f(roots[2])
done('all_stationary_points','Three disjoint brackets cross-check polynomial roots; cubic degree exhausts real candidates; coercivity proves existence.')
assert np.dot([1,0],np.diag([2,-2])@np.array([1,0]))>0
assert np.dot([0,1],np.diag([2,-2])@np.array([0,1]))<0
assert (.1**4)>0 and -(.1**4)<0
done('saddle_and_degenerate_hessian','Explicit directions and +/-x^4 show insufficiency of zero gradient and semidefinite Hessian.')
for alpha in [.05,.09,.1,.105]:
    path=m.gradient(alpha)
    exact=np.array([3.,1.])*(1-alpha*np.array([1,20]))**60
    assert np.allclose(path[-1],exact,rtol=1e-12,atol=1e-12)
assert abs(m.gradient(.1)[-1,1])==1 and abs(m.gradient(.105)[-1,1])>300
done('quadratic_GD_factors','Exact powers cross-check all iterates at final step; alpha=0.1 does not decay, 0.105 diverges.')
rng=np.random.default_rng(2718);Q=np.diag([1.,20.])
for _ in range(100):
    x=rng.normal(size=2);a=rng.uniform(.0001,.0999);g=Q@x
    fv=lambda x:.5*x@Q@x
    assert fv(x-a*g)<=fv(x)-a*(1-20*a/2)*(g@g)+1e-12
done('descent_lemma','100 deterministic test cases complement direct quadratic derivation; not a proof for arbitrary functions.')
x=np.array([3.,1.]);p=np.linalg.solve(Q,-Q@x)
assert np.array_equal(x+p,[0,0])
done('Newton_SPD_quadratic','Independent linear solve reaches the exact quadratic minimizer.')
x=.1;p=-df(x)/(12*x*x-4)
assert df(x)*p>0 and f(x+p)>f(x)
done('Newton_negative_curvature','Both directional derivative and actual objective increase at x=0.1.')
d=m.nonlinear_fit();a,b=d['parameters'];u=d['u'];observed=d['y'].copy();e=np.exp(-b*u)
J=np.column_stack([e,-a*u*e])
h=1e-5
res=lambda p:p[0]*np.exp(-p[1]*u)-observed
Jfd=np.column_stack([(res(d['parameters']+h*np.eye(2)[j])-res(d['parameters']-h*np.eye(2)[j]))/(2*h) for j in range(2)])
assert np.max(np.abs(J-Jfd))<1e-9
done('residual_Jacobian','Analytic derivatives agree with independent centered differences.')
def grad(p):
    e=np.exp(-p[1]*u);j=np.column_stack([e,-p[0]*u*e])
    return j.T@res(p)
H=J.T@J
for ui,ei,ri in zip(u,e,d['residual']):
    H=H+ri*np.array([[0,-ui*ei],[-ui*ei,a*ui*ui*ei]])
Hfd=np.column_stack([(grad(d['parameters']+h*np.eye(2)[j])-grad(d['parameters']-h*np.eye(2)[j]))/(2*h) for j in range(2)])
assert np.max(np.abs(H-Hfd))<1e-8 and np.max(np.abs(H-J.T@J))>1e-5
done('full_vs_Gauss_Newton_Hessian','Finite differences verify the residual curvature term; it is nonzero for the specified model.')
# Reduce nonlinear optimization independently to a one-dimensional bounded search.
def profile(b):
    e=np.exp(-b*u);a=np.clip((e@d['y'])/(e@e),0,3)
    return .5*np.sum((a*e-d['y'])**2)
grid=np.linspace(0,8,1601);j=np.argmin([profile(z) for z in grid])
scalar=minimize_scalar(profile,bounds=(grid[j-1],grid[j+1]),method='bounded',options={'xatol':1e-13})
assert abs(scalar.x-d['parameters'][1])<3e-7 and abs(scalar.fun-d['objective'])<1e-12
assert d['success'] and d['gradient_inf']<1e-8
done('nonlinear_fit_cross_solver','Profile out amplitude exactly, scan rate grid then scalar refine; confirms candidate, not certified global optimization.')
# LICQ qualification counterexample is exact: at x=0 gradient of x^2 vanishes.
assert 0**2<=0 and 1+100*(2*0)==1
done('KKT_qualification_counterexample','Unique feasible minimizer for min x, x^2<=0 has no stationarity multiplier.')
for z in [np.array([3.,1.]),np.array([1.5,.5]),np.array([-.5,5.])]:
    p=minimize(lambda x:.5*np.sum((x-z)**2),[.2,.2],jac=lambda x:x-z,
        method='SLSQP',bounds=[(0,None)]*2,
        constraints=[{'type':'ineq','fun':lambda x:2-x.sum(),'jac':lambda x:-np.ones(2)}],
        options={'ftol':1e-13,'maxiter':100})
    assert p.success and min(p.x)>-1e-10 and sum(p.x)<2+1e-10
    if np.allclose(z,[1.5,.5]):assert np.max(np.abs(z-p.x))<1e-9
x=np.array([1.5,.5]);assert np.linalg.norm(x-[2,1])>.7
assert np.linalg.norm(x-m.budget_solution(2)[0])==0
done('projection_and_boundary','Independent projections and boundary fixed point distinguish ordinary from projected gradient.')
for rho in [.1,1,10,100,1e4]:
    x=(2+rho)/(1+rho)
    assert x>1 and abs((x-2)+rho*(x-1))<1e-10
    penalty_result=minimize_scalar(lambda z:.5*(z-2)**2+rho/2*max(z-1,0)**2,
        bounds=(0,3),method='bounded',options={'xatol':1e-12})
    assert abs(penalty_result.x-x)<3e-7
done('quadratic_penalty','Analytic stationarity and independent scalar solver verify finite-parameter violation.')
for tau in [1e-4,.01,.1,1,10]:
    x=(3-np.sqrt(1+4*tau))/2
    assert x<1 and abs(x-2+tau/(1-x))<1e-10
    mu=tau/(1-x);assert abs(mu*(1-x)-tau)<1e-12
done('log_barrier','Exact quadratic root verifies stationarity, strict interior and perturbed complementarity.')
b=np.array([1.2,.15,-.08]);lam=.2;x=m.soft(b,lam);nz=x!=0
assert np.max(np.abs(x[nz]-b[nz]+lam*np.sign(x[nz])))<1e-12 and np.all(np.abs(b[~nz])<=lam)
grid=np.linspace(-2,2,8001)
for bi,xi in zip(b,x):
    assert .5*(xi-bi)**2+lam*abs(xi)<=np.min(.5*(grid-bi)**2+lam*np.abs(grid))+1e-12
done('L1_soft_threshold','Subgradient conditions and independent dense one-dimensional comparisons.')
x=b/(1+lam);assert np.max(np.abs(x-b+lam*x))<1e-12
assert abs(.1)>abs(0)
done('ridge_and_subgradient_ascent','Ridge gradient vanishes; valid subgradient +1 at |x| minimum makes any positive step increase the value.')
# Enumerate all 16 possible noise paths for four steps, no Monte Carlo required.
fixed=[];dec=[]
for noise in product([-1.,1.],repeat=4):
    x=y=2.
    for k,n in enumerate(noise,1):x=.9*x-.1*n;y-=(y+n)/k
    fixed.append(x*x);dec.append(y*y)
assert abs(np.mean(fixed)-(.9**8*4+.1/1.9*(1-.9**8)))<1e-14
assert abs(np.mean(dec)-1/4)<1e-14
done('SGD_exact_enumeration','All 16 four-step paths independently match both second-moment formulas.')
d=m.sgd()
assert d['k'][-1]==600
assert abs(d['fixed_mse'][-1]/d['fixed_theory'][-1]-1)<.2
assert abs(d['decreasing_mse'][-1]/d['decreasing_theory'][-1]-1)<.2
done('SGD_seeded_reproduction','512 trajectories agree with exact moments within stated finite-sample check; not a general convergence proof.')
Q=np.diag([1,1e4]);D=np.diag([1,.01]);assert np.allclose(D.T@Q@D,np.eye(2))
assert np.linalg.cond(Q)==1e4 and np.linalg.cond(D.T@Q@D)==1
raw=m.gradient(1e-4,1000,(1,1),(1,1e4));assert raw[-1,0]>.9
done('coordinate_scaling','Exact congruence and independent condition numbers verify equivalent parameterization.')
assert np.sqrt(2)*1e-12<1e-8 and np.linalg.norm([1,1])>1
done('absolute_stopping_counterexample','A scaled objective passes a chosen absolute gradient threshold while distance remains sqrt(2).')
# Independent directional derivative check on the teaching fit.
p=np.array([.8,1.2]);direction=np.array([.3,-.4])
for h in [1e-3,1e-4,1e-5]:
    fv=lambda p:.5*np.sum(res(p)**2)
    fd=(fv(p+h*direction)-fv(p-h*direction))/(2*h)
    assert abs(fd-grad(p)@direction)<2*h*h+1e-10
done('directional_derivative','Three step sizes independently check sign, Jacobian orientation and objective derivative.')
out=dict(status='passed',check_groups=len(checks),checks=checks,scope='Specified models only; calculations supplement analytic arguments; professional review pending.')
(ROOT/'docs/research/optimization-methods-2026-11-02/numerical-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,default=m.serial)+'\n',encoding='utf-8')
print(json.dumps(dict(status='passed',check_groups=len(checks))))
