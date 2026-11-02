"""Reproducible dimensionless models, not empirical acoustic or neural recordings.
Python 3.11; NumPy 1.26.4, SciPy 1.17.1. No random model fitted to measurements.
"""
import numpy as np
from scipy.integrate import solve_ivp

def solve(fun,span,y0,t_eval=None,rtol=1e-10,atol=1e-12,max_step=.05):
    s=solve_ivp(fun,span,y0,method='DOP853',rtol=rtol,atol=atol,max_step=max_step,t_eval=t_eval)
    if not s.success:raise RuntimeError(s.message)
    return s

def cubic_roots(h):
    roots=np.roots([1.,0.,-1.,-h]);real=np.sort(roots.real[abs(roots.imag)<1e-9])
    return real,1-3*real**2

def hopf_fun(t,z,mu=.2,omega=2*np.pi,c=0.):
    x,y=z;r2=x*x+y*y;growth=mu-r2;speed=omega-c*r2
    return np.array([growth*x-speed*y,speed*x+growth*y])

def hopf_jac(z,mu=.2,omega=2*np.pi):
    x,y=z
    return np.array([[mu-3*x*x-y*y,-omega-2*x*y],[omega-2*x*y,mu-x*x-3*y*y]])

def hopf_floquet(mu=.2,omega=2*np.pi):
    period=2*np.pi/omega;r=np.sqrt(mu)
    def aug(t,z):return np.r_[hopf_fun(t,z[:2],mu,omega),(hopf_jac(z[:2],mu,omega)@z[2:].reshape(2,2)).ravel()]
    s=solve(aug,(0,period),np.r_[r,0.,np.eye(2).ravel()],max_step=.02)
    matrix=s.y[2:,-1].reshape(2,2);return matrix,np.linalg.eigvals(matrix)

def hopf_radial(t,r0,mu=.2):
    t=np.asarray(t)
    if mu==0:return r0/np.sqrt(1+2*r0*r0*t)
    return np.sqrt(mu/(1+(mu/r0**2-1)*np.exp(-2*mu*t)))

def subcritical_radii(mu):
    if mu<-.25:return []
    u=np.array([(1-np.sqrt(1+4*mu))/2,(1+np.sqrt(1+4*mu))/2])
    return np.sqrt(u[u>0]).tolist()

def vdp_example():
    out={}
    for mu in [.2,5.]:
        fun=lambda t,z:[z[1],mu*(1-z[0]**2)*z[1]-z[0]]
        s=solve(fun,(0,200),[.5,0],t_eval=np.linspace(160,200,4001),max_step=.02)
        out[mu]=s
    return out

def duffing_candidates(omega,zeta=.05,alpha=1.,force=.2):
    # u=A²; first-harmonic balance, not an exact response or stability classifier.
    b=.75*alpha;d=1-omega**2
    roots=np.roots([b*b,2*b*d,d*d+(2*zeta*omega)**2,-force**2])
    return sorted(np.sqrt(r.real) for r in roots if abs(r.imag)<1e-8 and r.real>0)

def adler_example():
    t=np.linspace(0,50,2501);out={}
    for delta in [.4,1.3]:out[delta]=solve(lambda t,p:[delta-np.sin(p[0])],(0,50),[2.],t_eval=t)
    return t,out

def logistic_series(r=4.,initial=.1234567,burn=1000,n=8192):
    x=float(initial)
    for _ in range(burn):x=r*x*(1-x)
    out=[]
    for _ in range(n):out.append(x);x=r*x*(1-x)
    return np.array(out)

def logistic_bifurcation():
    r=np.linspace(2.8,4,1000);x=np.full_like(r,.1234567)
    for _ in range(1600):x=r*x*(1-x)
    samples=[];logs=np.zeros_like(r)
    for _ in range(400):
        samples.append(x.copy());logs+=np.log(np.maximum(abs(r*(1-2*x)),1e-300));x=r*x*(1-x)
    return r,np.array(samples),logs/400

def lorenz(t,z,sigma=10.,rho=28.,beta=8/3):
    x,y,w=z;return np.array([sigma*(y-x),x*(rho-w)-y,x*y-beta*w])

def lorenz_jac(z):
    x,y,w=z;return np.array([[-10.,10.,0.],[28-w,-1.,-x],[y,x,-8/3]])

def lorenz_qr(duration=240.,burn=30.,interval=.5,rtol=1e-9,max_step=.04):
    state=solve(lorenz,(0,burn),[1.,1.,1.],rtol=rtol,atol=rtol/100,max_step=max_step).y[:,-1]
    q=np.eye(3);total=np.zeros(3);history=[];times=[]
    def aug(t,z):return np.r_[lorenz(t,z[:3]),(lorenz_jac(z[:3])@z[3:].reshape(3,3)).ravel()]
    count=int(round(duration/interval));assert np.isclose(count*interval,duration)
    for k in range(count):
        s=solve(aug,(0,interval),np.r_[state,q.ravel()],rtol=rtol,atol=rtol/100,max_step=max_step)
        state=s.y[:3,-1];q,r=np.linalg.qr(s.y[3:,-1].reshape(3,3));total+=np.log(abs(np.diag(r)))
        times.append((k+1)*interval);history.append(total/times[-1])
    return dict(exponents=(total/duration).tolist(),times=times,history=np.asarray(history).tolist(),duration=duration,burn=burn,interval=interval,rtol=rtol,max_step=max_step)

def summary():
    matrix,eigen=hopf_floquet();r=3.2;a=logistic_series(r,n=20);four=logistic_series(4.,n=20000)
    radii=subcritical_radii(-.15);roots,derivative=cubic_roots(0.)
    return dict(cubic_fold_h=2/(3*np.sqrt(3)),cubic_roots_h0=roots.tolist(),cubic_derivatives_h0=derivative.tolist(),ghost_passage_epsilon_001=float(2*np.arctan(10)/.1),hopf=dict(mu=.2,period=1.,radius=float(np.sqrt(.2)),floquet_matrix=matrix.tolist(),multipliers=eigen.real.tolist(),expected_radial_multiplier=float(np.exp(-.4))),subcritical_mu_minus_015_radii=radii,adler=dict(delta=.4,K=1.,stable_phase=float(np.arcsin(.4)),relaxation_eigenvalue=float(-np.sqrt(1-.4**2)),running_delta=1.3,mean_slip_rate=float(np.sqrt(1.3**2-1))),logistic=dict(r32_two_cycle=sorted(a[-2:].tolist()),r32_multiplier=float(-r*r+2*r+4),r4_finite_exponent=float(np.mean(np.log(abs(4*(1-2*four))))),r4_typical_exact_exponent=float(np.log(2))))

if __name__=='__main__':
    import json
    print(json.dumps(summary(),ensure_ascii=False,indent=2))
