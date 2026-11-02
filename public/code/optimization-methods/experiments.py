"""Original optimization teaching experiments; no listener/device measurements.

Python 3.11, NumPy 1.26.4 and SciPy 1.17.1 were used for publication.
Run: python experiments.py
"""
import json
import numpy as np
import scipy
from scipy.optimize import minimize, least_squares

def budget_solution(c):
    """Euclidean projection of (2,1) onto x>=0, sum(x)<=c; c>=0."""
    c=float(c)
    if c<0:raise ValueError("c must be nonnegative")
    if c<=1:x=np.array([c,0.]);mu=2-c
    elif c<3:x=np.array([(c+1)/2,(c-1)/2]);mu=(3-c)/2
    else:x=np.array([2.,1.]);mu=0.
    return x,mu

def constrained():
    b=np.array([2.,1.])
    sol=minimize(lambda x:.5*np.dot(x-b,x-b),[.3,.3],
        jac=lambda x:x-b,method="SLSQP",bounds=[(0,None)]*2,
        constraints=[{"type":"ineq","fun":lambda x:2-x.sum(),
                      "jac":lambda x:-np.ones(2)}],
        options={"ftol":1e-12,"maxiter":200})
    x=sol.x;mu=.5
    return dict(x=x,objective=sol.fun,success=bool(sol.success),
        stationarity=np.max(np.abs(x-b+mu)),
        feasibility=max(0.,x.sum()-2,-x.min()),
        complementarity=abs(mu*(x.sum()-2)),
        dual=mu-mu*mu,gap=sol.fun-(mu-mu*mu))

def nonconvex():
    roots=np.sort(np.roots([4.,0.,-4.,.3]))
    return dict(roots=roots,values=(roots*roots-1)**2+.3*roots,
                curvature=12*roots**2-4)

def gradient(alpha=.05,steps=60,start=(3.,1.),diag=(1.,20.)):
    x=np.asarray(start,dtype=float);q=np.asarray(diag,dtype=float)
    out=[x.copy()]
    for _ in range(steps):x=x-alpha*q*x;out.append(x.copy())
    return np.asarray(out)

def nonlinear_fit():
    u=np.linspace(0,1,41)
    y=np.exp(-2*u)+.025*np.cos(9*u)
    def residual(p):return p[0]*np.exp(-p[1]*u)-y
    def jac(p):
        e=np.exp(-p[1]*u)
        return np.column_stack((e,-p[0]*u*e))
    sol=least_squares(residual,[.6,.6],jac=jac,bounds=([0.,0.],[3.,8.]),
        method="trf",loss="linear",x_scale=[1.,1.],
        ftol=1e-13,xtol=1e-13,gtol=1e-13,max_nfev=500)
    r=residual(sol.x);j=jac(sol.x)
    return dict(u=u,y=y,parameters=sol.x,prediction=y+r,residual=r,
        objective=.5*np.dot(r,r),gradient_inf=np.max(np.abs(j.T@r)),
        success=bool(sol.success),singular_values=np.linalg.svd(j,compute_uv=False))

def soft(z,threshold):
    return np.sign(z)*np.maximum(np.abs(z)-threshold,0.)

def sgd(repetitions=512,steps=600,seed=20261102):
    rng=np.random.default_rng(seed)
    noise=rng.choice([-1.,1.],size=(repetitions,steps))
    fixed=np.full(repetitions,2.);decreasing=fixed.copy()
    fixed_mse=[4.];decreasing_mse=[4.];path_fixed=[2.];path_decreasing=[2.]
    for k in range(1,steps+1):
        fixed-=.1*(fixed+noise[:,k-1])
        decreasing-=(decreasing+noise[:,k-1])/k
        fixed_mse.append(np.mean(fixed**2));decreasing_mse.append(np.mean(decreasing**2))
        path_fixed.append(fixed[0]);path_decreasing.append(decreasing[0])
    k=np.arange(steps+1)
    return dict(k=k,fixed_mse=np.array(fixed_mse),decreasing_mse=np.array(decreasing_mse),
        fixed_theory=.9**(2*k)*4+(.1/1.9)*(1-.9**(2*k)),
        decreasing_theory=np.r_[4.,1/np.arange(1,steps+1)],
        fixed_path=np.array(path_fixed),decreasing_path=np.array(path_decreasing))

def summary():
    fit=nonlinear_fit();nc=nonconvex();con=constrained()
    return dict(runtime=dict(numpy=np.__version__,scipy=scipy.__version__),
        constrained=con,nonconvex=nc,
        gradient_final={str(a):gradient(a)[-1] for a in [.05,.09,.105]},
        newton_negative_curvature=dict(start=.1,gradient=4*.1**3-4*.1+.3,
            hessian=12*.1**2-4,step=-(4*.1**3-4*.1+.3)/(12*.1**2-4)),
        nonlinear_fit={k:fit[k] for k in ['parameters','objective','gradient_inf','success','singular_values']},
        regularization=dict(b=[1.2,.15,-.08],lam=.2,
            lasso=soft(np.array([1.2,.15,-.08]),.2),ridge=np.array([1.2,.15,-.08])/1.2),
        scalar_penalty={str(r):(2+r)/(1+r) for r in [1,10,100]},
        scalar_barrier={str(t):(3-np.sqrt(1+4*t))/2 for t in [1,.1,.01]},
        sgd=dict(seed=20261102,repetitions=512,steps=600,fixed_stationary_mse=.1/1.9,
            decreasing_exact_mse_at_600=1/600))

def serial(value):
    if isinstance(value,np.ndarray):return value.tolist()
    if isinstance(value,np.generic):return value.item()
    raise TypeError(type(value).__name__)

if __name__=="__main__":
    print(json.dumps(summary(),ensure_ascii=False,indent=2,default=serial))
