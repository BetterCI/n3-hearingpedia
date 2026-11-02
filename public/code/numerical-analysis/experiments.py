"""Specified numerical analysis teaching experiments, not hearing/device measurements."""
from decimal import Decimal,localcontext
from math import comb
import json
import numpy as np
from scipy import linalg,optimize,interpolate,integrate,sparse,special
from scipy.sparse import linalg as sla
def cancellation():
    x=np.logspace(-18,-1,137);naive=np.log(1+x);stable=np.log1p(x);en=[];es=[]
    with localcontext() as ctx:
        ctx.prec=80
        for xx,a,b in zip(x,naive,stable):
            true=(Decimal(1)+Decimal.from_float(float(xx))).ln()
            en.append(float(abs(Decimal.from_float(float(a))-true)/abs(true)))
            es.append(float(abs(Decimal.from_float(float(b))-true)/abs(true)))
    return x,naive,stable,np.array(en),np.array(es)
def condition_demo():
    delta=np.logspace(-1,-12,12);bn=np.sqrt(1+delta*delta)
    return dict(delta=delta,forward=np.full_like(delta,1/np.sqrt(2)),relative_residual=delta/bn,
        scaled_residual=delta/(1+bn),condition=1/delta,forward_upper_bound=1/bn)
def pivot_demo():
    A=np.array([[1e-20,1.],[1.,1.]]);b=np.array([1.,2.])
    multiplier=A[1,0]/A[0,0]
    x2=(b[1]-multiplier*b[0])/(A[1,1]-multiplier*A[0,1])
    unpivoted=np.array([(b[0]-A[0,1]*x2)/A[0,0],x2])
    return A,b,unpivoted,np.linalg.solve(A,b)
def least_squares():
    fs=16000.;n=np.arange(256);t=n/fs
    A=np.column_stack([np.sin(2*np.pi*1000*t),np.sin(2*np.pi*1000.0001*t)])
    true=np.array([.8,-.3]);b=A@true;U,s,Vh=np.linalg.svd(A,full_matrices=False)
    perturb=1e-4*U[:,-1];bp=b+perturb
    Q,R=np.linalg.qr(A,mode='reduced')
    clean=np.linalg.solve(R,Q.T@b);perturbed=np.linalg.solve(R,Q.T@bp)
    lam=1e-4
    augmented=np.vstack([A,np.sqrt(lam)*np.eye(2)])
    ridge=np.linalg.lstsq(augmented,np.r_[bp,np.zeros(2)],rcond=None)[0]
    return dict(fs=fs,t=t,A=A,true=true,b=b,perturb=perturb,s=s,condition=float(s[0]/s[-1]),
        clean=clean,perturbed=perturbed,ridge=ridge,lam=lam,
        perturb_norm=float(np.linalg.norm(perturb)),coefficient_change=float(np.linalg.norm(perturbed-clean)),
        output_change=float(np.linalg.norm(A@perturbed-b)),ridge_output_error=float(np.linalg.norm(A@ridge-b)))
def roots():
    f=lambda x:np.cos(x)-x
    root=optimize.brentq(f,0,1,xtol=1e-14,rtol=4*np.finfo(float).eps)
    left,right=0.,1.;bis=[];newton=[1.];fixed=[1.]
    for i in range(30):
        mid=(left+right)/2;bis.append(mid)
        if f(left)*f(mid)<=0:right=mid
        else:left=mid
        newton.append(newton[-1]-f(newton[-1])/(-np.sin(newton[-1])-1))
        fixed.append(np.cos(fixed[-1]))
    cycle=[0.]
    for i in range(10):
        x=cycle[-1];cycle.append(x-(x**3-2*x+2)/(3*x*x-2))
    return dict(root=float(root),bisection=np.array(bis),newton=np.array(newton),fixed=np.array(fixed),cycle=np.array(cycle))
def runge(degree,chebyshev=False):
    j=np.arange(degree+1)
    if chebyshev:
        x=np.cos(np.pi*j/degree);weights=(-1.)**j;weights[[0,-1]]*=.5
    else:
        x=np.linspace(-1,1,degree+1);weights=np.array([(-1.)**k*comb(degree,k) for k in j]);weights/=max(abs(weights))
    y=1/(1+25*x*x)
    interp=interpolate.BarycentricInterpolator(x,y,wi=weights)
    return x,y,interp
def runge_errors():
    x=np.linspace(-1,1,10001);true=1/(1+25*x*x);rows=[]
    for degree in [4,8,12,16,20,24,28,32,36,40]:
        row=dict(degree=degree)
        for name,cheb in [('equally_spaced',False),('Chebyshev_Lobatto',True)]:
            _,_,p=runge(degree,cheb);row[name]=float(np.max(abs(p(x)-true)))
        rows.append(row)
    return rows
def splines():
    x=np.array([0.,1.,2.,3.]);y=np.array([0.,.01,.02,1.]);z=np.linspace(0,3,3001)
    natural=interpolate.CubicSpline(x,y,bc_type='natural',extrapolate=False)
    pchip=interpolate.PchipInterpolator(x,y,extrapolate=False)
    return x,y,z,natural,pchip
def narrow_integral():
    center=.37;sigma=.001
    f=lambda x:np.exp(-((np.asarray(x)-center)/sigma)**2)
    exact=sigma*np.sqrt(np.pi)/2*(special.erf((1-center)/sigma)+special.erf(center/sigma))
    rows=[]
    for N in [16,32,64,128,256,512,1024,2048]:
        x=np.linspace(0,1,N+1);rows.append(dict(intervals=N,value=float(integrate.trapezoid(f(x),x=x))))
    blind,err=integrate.quad(f,0,1,epsabs=1e-10,epsrel=1e-10)
    informed,ierr=integrate.quad(f,0,1,points=[center-5*sigma,center,center+5*sigma],epsabs=1e-10,epsrel=1e-10)
    return dict(center=center,sigma=sigma,exact=float(exact),function=f,rows=rows,
        blind=float(blind),blind_error_estimate=float(err),informed=float(informed),informed_error_estimate=float(ierr))
def stiff_euler(h,implicit=False,T=1.):
    n=int(round(T/h));t=np.arange(n+1)*h;y=np.zeros(n+1)
    for k in range(n):
        if implicit:
            y[k+1]=(y[k]+h*(1000*np.cos(t[k+1])-np.sin(t[k+1])))/(1+1000*h)
        else:y[k+1]=y[k]+h*(-1000*(y[k]-np.cos(t[k]))-np.sin(t[k]))
    return t,y
def stiff_solvers():
    times=np.linspace(0,1,2001);exact=np.cos(times)-np.exp(-1000*times);rows=[]
    for method in ['RK45','Radau']:
        sol=integrate.solve_ivp(lambda t,y:-1000*(y-np.cos(t))-np.sin(t),(0,1),[0.],method=method,
            t_eval=times,rtol=1e-6,atol=1e-8)
        assert sol.success
        rows.append(dict(method=method,nfev=sol.nfev,max_absolute_error=float(np.max(abs(sol.y[0]-exact)))))
    return rows
def bvp(N):
    h=1./N;x=np.arange(1,N)*h
    A=sparse.diags([-np.ones(N-2),2*np.ones(N-1),-np.ones(N-2)],[-1,0,1],format='csc')/(h*h)
    b=np.pi**2*np.sin(np.pi*x);y=sla.spsolve(A,b)
    return x,y,float(np.max(abs(y-np.sin(np.pi*x)))),float(np.linalg.norm(A@y-b)/np.linalg.norm(b))
def cg_demo(N=80):
    D=sparse.diags(np.geomspace(1,1000,N),format='csr')
    T=sparse.diags([-np.ones(N-1),2*np.ones(N),-np.ones(N-1)],[-1,0,1],format='csr')
    A=(D@T@D).tocsr();truth=np.ones(N);b=A@truth
    M=sla.LinearOperator((N,N),matvec=lambda v:v/A.diagonal(),dtype=float)
    rows=[]
    for name,P in [('CG',None),('Jacobi_PCG',M)]:
        residual=[]
        def callback(xk):residual.append(float(np.linalg.norm(b-A@xk)/np.linalg.norm(b)))
        x,info=sla.cg(A,b,x0=np.zeros(N),M=P,rtol=1e-10,atol=0,maxiter=1000,callback=callback)
        rows.append(dict(name=name,iterations=len(residual),info=int(info),residual=np.array(residual),
            final_relative_residual=float(np.linalg.norm(b-A@x)/np.linalg.norm(b)),
            relative_forward_error=float(np.linalg.norm(x-truth)/np.linalg.norm(truth))))
    return A,b,rows
def summary():
    A,b,x0,xp=pivot_demo();ls=least_squares();r=roots();x,y,z,cs,pc=splines();ni=narrow_integral();_,_,cg=cg_demo()
    return dict(runtime_precision=dict(float64_eps=float(np.finfo(float).eps),unit_roundoff=float(np.finfo(float).eps/2)),
        pivot=dict(condition=float(np.linalg.cond(A)),unpivoted=x0.tolist(),pivoted=xp.tolist()),
        least_squares={k:ls[k] for k in ['condition','perturb_norm','coefficient_change','output_change','ridge_output_error','lam']},
        root=r['root'],Newton_cycle=r['cycle'].tolist(),Runge=runge_errors(),
        spline=dict(natural_min=float(cs(z).min()),pchip_min=float(pc(z).min()),pchip_monotone=bool(np.all(np.diff(pc(z))>=-1e-14))),
        narrow_integral={k:v for k,v in ni.items() if k!='function'},stiff_solvers=stiff_solvers(),
        BVP=[dict(intervals=N,max_absolute_error=bvp(N)[2],relative_residual=bvp(N)[3]) for N in [16,32,64,128]],
        CG=[{k:v for k,v in row.items() if k!='residual'} for row in cg])
if __name__=='__main__':print(json.dumps(summary(),ensure_ascii=True,indent=2))
