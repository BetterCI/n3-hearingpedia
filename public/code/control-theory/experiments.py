"""Original normalized control examples, not measurements or device prescriptions.
Time tau=t/T0, T0=1 s. States, inputs and outputs are normalized.
Publication runtime: Python 3.11 / NumPy 1.26.4 / SciPy 1.17.1.
"""
import json
import numpy as np
import scipy
from scipy import signal
from scipy.linalg import expm,solve_continuous_are,solve_continuous_lyapunov

def plant():
    return np.array([[0.,1.],[-2.,-.6]]),np.array([[0.],[1.]]),np.array([[1.,0.]])

def proportional(t,k=4.,disturbance=.3,switch=3.):
    t=np.asarray(t)
    closed=k/(1+k)*(1-np.exp(-(1+k)*t))
    closed+=disturbance/(1+k)*(1-np.exp(-(1+k)*np.maximum(t-switch,0)))
    opened=1-np.exp(-t)+disturbance*(1-np.exp(-np.maximum(t-switch,0)))
    return opened,closed

def root_response(k,t):
    _,y=signal.step(signal.TransferFunction([k],[1,3,2,k]),T=t)
    return y

def loop(w,delay=0.):
    s=1j*np.asarray(w)
    return 4*np.exp(-delay*s)/((s+1)*(s+2))

def margins():
    wc=np.sqrt((-5+np.sqrt(73))/2)
    pm=np.pi-np.arctan(wc)-np.arctan(wc/2)
    return dict(crossover=wc,phase_margin_radians=pm,
        phase_margin_degrees=np.rad2deg(pm),delay_margin=pm/wc)

def windup(anti=False,dt=.0025,end=14.):
    """RK4 with reference constant within each step; switch aligns to grid."""
    assert abs(5/dt-round(5/dt))<1e-9
    n=round(end/dt);t=np.arange(n+1)*dt
    states=np.zeros((n+1,2))
    def fun(v,r):
        y,z=v;uc=2*(r-y)+z;u=np.clip(uc,-1,1)
        return np.array([-y+u,(r-y)+(2*(u-uc) if anti else 0.)])
    for k in range(n):
        v=states[k];r=2. if k<round(5/dt) else .5
        a=fun(v,r);b=fun(v+.5*dt*a,r);c=fun(v+.5*dt*b,r);d=fun(v+dt*c,r)
        states[k+1]=v+dt*(a+2*b+2*c+d)/6
    r=np.where(t<5,2.,.5);uc=2*(r-states[:,0])+states[:,1]
    return dict(t=t,y=states[:,0],integral=states[:,1],reference=r,command=uc,actual=np.clip(uc,-1,1))

def state_feedback(t):
    a,b,c=plant();k=signal.place_poles(a,b,[-2.,-3.],method='YT').gain_matrix
    x0=np.array([1.,0.])
    opened=np.array([expm(a*ti)@x0 for ti in t])
    closed=np.array([expm((a-b@k)*ti)@x0 for ti in t])
    return dict(k=k,opened=opened,closed=closed,control=-(closed@k.T).ravel())

def observer(t,poles=(-4.,-5.)):
    a,b,c=plant();l=signal.place_poles(a.T,c.T,poles,method='YT').gain_matrix.T
    e0=np.array([1.,0.])
    error=np.array([expm((a-l@c)*ti)@e0 for ti in t])
    return dict(l=l,error=error,norm=np.linalg.norm(error,axis=1))

def observer_noise(w,poles=(-4.,-5.)):
    a,b,c=plant();l=signal.place_poles(a.T,c.T,poles,method='YT').gain_matrix.T
    return np.array([abs(np.linalg.solve(1j*wi*np.eye(2)-a+l@c,l)[1,0]) for wi in w])

def lqr(r=1.,t=None):
    a,b,c=plant();q=np.eye(2);rr=np.array([[float(r)]])
    p=solve_continuous_are(a,b,q,rr,balanced=True)
    k=np.linalg.solve(rr,b.T@p);ac=a-b@k
    residual=a.T@p+p@a-p@b@np.linalg.solve(rr,b.T@p)+q
    # Independent cost integration via the closed-loop Lyapunov identity.
    pcost=solve_continuous_lyapunov(ac.T,-(q+k.T@rr@k))
    result=dict(r=r,p=p,k=k,poles=np.linalg.eigvals(ac),riccati_residual=np.max(np.abs(residual)),
        cost_from_x0=p[0,0],independent_cost=pcost[0,0])
    if t is not None:
        x=np.array([expm(ac*ti)@np.array([1.,0.]) for ti in t])
        result.update(x=x,control=-(x@k.T).ravel())
    return result

def sampled(h,k=4.):
    ad,bd,_,_,_=signal.cont2discrete((np.array([[-1.]]),np.array([[1.]]),np.array([[1.]]),np.array([[0.]])),h,method='zoh')
    return dict(h=h,ad=float(ad[0,0]),bd=float(bd[0,0]),pole=float((ad-k*bd)[0,0]),
                continuous_feedback_sampled=float(np.exp(-(1+k)*h)))

def summary():
    a,b,c=plant();cont=np.hstack((b,a@b));obs=np.vstack((c,c@a))
    t=np.linspace(0,8,401);k=state_feedback(t)['k'];l=observer(t)['l']
    return dict(runtime=dict(numpy=np.__version__,scipy=scipy.__version__),
        normalized_time='tau=t/T0; T0=1 second',
        proportional=dict(open_steady=1.3,closed_steady=.86,closed_error=.14),
        root_locus={str(k):np.roots([1,3,2,k]) for k in [2,5,6,8]},
        margins=margins(),state=dict(a=a,b=b,c=c,controllability_rank=np.linalg.matrix_rank(cont),
            observability_rank=np.linalg.matrix_rank(obs),k=k,l=l,
            feedback_poles=np.linalg.eigvals(a-b@k),observer_poles=np.linalg.eigvals(a-l@c)),
        lqr=[lqr(r) for r in [.1,1,10]],
        sampling=dict(limit=np.log(5/3),cases=[sampled(h) for h in [.1,.4,.6]]),
        windup_at_8={str(anti):{key:float(d[key][round(8/.0025)]) for key in ['y','integral','command','actual']} for anti in [False,True] for d in [windup(anti)]})

def serial(x):
    if isinstance(x,np.ndarray):
        if np.iscomplexobj(x):return [dict(real=float(z.real),imag=float(z.imag)) for z in x.ravel()]
        return x.tolist()
    if isinstance(x,np.generic):return x.item()
    raise TypeError(type(x).__name__)
if __name__=='__main__':print(json.dumps(summary(),ensure_ascii=False,indent=2,default=serial))
