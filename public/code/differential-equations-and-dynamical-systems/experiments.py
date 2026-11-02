"""Original differential-equation/dynamical-system teaching models.
All variables normalized: tau=t/T0, T0=1 second, xi=x/L0 for the PDE.
Not hearing, neural, room or device measurements.
Publication: Python 3.11, NumPy 1.26.4, SciPy 1.17.1.
"""
import json
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.linalg import expm

def logistic_flow(t,x0=.15,rate=1.2):
    t=np.asarray(t)
    if x0==0:return np.zeros_like(t)
    return 1/(1+(1/x0-1)*np.exp(-rate*t))

def linear_examples():
    return {
        "node":np.diag([-1.,-2.]),
        "focus":np.array([[-.2,-1.],[1.,-.2]]),
        "saddle":np.diag([1.,-1.]),
        "center":np.array([[0.,-1.],[1.,0.]])}

def oscillator(t,damping=.1):
    """q''+4*zeta*q'+4*q=.4*cos(2*t), q(0)=q'(0)=0."""
    t=np.asarray(t)
    sol=solve_ivp(lambda tau,x:[x[1],.4*np.cos(2*tau)-4*damping*x[1]-4*x[0]],
        (0,float(t[-1])),[0.,0.],t_eval=t,method="DOP853",
        rtol=1e-11,atol=1e-13,max_step=.04)
    assert sol.success
    return sol.y.T

def pendulum(t,damping=.4):
    t=np.asarray(t)
    sol=solve_ivp(lambda tau,x:[x[1],-damping*x[1]-np.sin(x[0])],
        (0,float(t[-1])),[1.4,0.],t_eval=t,method="DOP853",
        rtol=1e-11,atol=1e-13,max_step=.03)
    assert sol.success
    x=sol.y.T;energy=.5*x[:,1]**2+1-np.cos(x[:,0])
    return dict(state=x,energy=energy)

def hopf_radius(t,r0=.2,mu=1.):
    t=np.asarray(t)
    if r0==0:return np.zeros_like(t)
    if mu==0:return r0/np.sqrt(1+2*r0*r0*t)
    return np.sqrt(mu/(1+(mu/(r0*r0)-1)*np.exp(-2*mu*t)))

def hopf(t,r0=.2,mu=1.,omega=2.):
    t=np.asarray(t);r=hopf_radius(t,r0,mu)
    return np.column_stack((r*np.cos(omega*t),r*np.sin(omega*t)))

def map_orbit(rate=4.,x0=.123456789,steps=70):
    out=[float(x0)]
    for _ in range(steps):out.append(rate*out[-1]*(1-out[-1]))
    return np.array(out)

def map_bifurcation():
    rates=np.linspace(2.8,4.,650);x=np.full_like(rates,.123456789)
    for _ in range(1500):x=rates*x*(1-x)
    out=[]
    for _ in range(140):x=rates*x*(1-x);out.append(x.copy())
    return rates,np.array(out)

def lorenz_rhs(t,x):
    xx,yy,zz=x
    return np.array([10*(yy-xx),xx*(28-zz)-yy,xx*yy-(8/3)*zz])

def lorenz(t,perturbation=0.,method="DOP853",rtol=1e-11,atol=1e-13):
    t=np.asarray(t)
    sol=solve_ivp(lorenz_rhs,(0,float(t[-1])),[1.+perturbation,1.,1.],
        t_eval=t,method=method,rtol=rtol,atol=atol,max_step=.025)
    assert sol.success
    return sol.y.T

def pde(x,t,kind="heat"):
    x=np.asarray(x);t=np.asarray(t)
    basis=np.array([np.sin(np.pi*x),.25*np.sin(3*np.pi*x)])
    if kind=="heat":weights=np.exp(-.08*np.outer(t,[np.pi**2,9*np.pi**2]))
    elif kind=="wave":weights=np.cos(np.outer(t,[np.pi,3*np.pi]))
    else:raise ValueError(kind)
    return weights@basis

def summary():
    period=np.pi
    cycle=np.array([(3.2+1-np.sqrt((3.2-3)*(3.2+1)))/(2*3.2),
                    (3.2+1+np.sqrt((3.2-3)*(3.2+1)))/(2*3.2)])
    near=lorenz(np.linspace(0,2,201));p=pendulum(np.linspace(0,15,601))
    orbit=map_orbit(4.,steps=51000)
    lyap=np.mean(np.log(np.abs(4-8*orbit[1000:-1])))
    return dict(runtime=dict(numpy=np.__version__,scipy=scipy.__version__),
        normalization='tau=t/T0; T0=1 second; all states normalized',
        logistic=dict(rate=1.2,carrying_level=1.,initials=[0.,.15,.6,1.4]),
        nonunique=dict(rhs='2*sqrt(abs(x))',initial=0,waiting_times=[0,1,2]),
        blowup=dict(rhs='x^2',initial=1,maximal_interval='(-infinity,1)'),
        oscillator=dict(natural_frequency=2.,forcing=.4,damping=.1,
            resonant_displacement_peak_frequency=2*np.sqrt(1-2*.1**2)),
        nonnormal=dict(a=[[-1,10],[0,-1]],initial=[0,1],x1_peak=10/np.e),
        pendulum=dict(initial=[1.4,0.],initial_energy=1-np.cos(1.4),
            final_energy_at_15=p['energy'][-1],damping=.4,barrier_energy=2.),
        hopf=dict(mu=1,omega=2,radius=1.,period=period,radial_return_multiplier=np.exp(-2*period)),
        logistic_map=dict(rate=3.2,two_cycle=cycle,multiplier=-3.2**2+2*3.2+4,
            r4_finite_average_log_derivative=float(lyap),r4_theoretical_typical_exponent=float(np.log(2)),
            exception=[.25,.75,.75]),
        lorenz=dict(parameters=[10,28,8/3],initial=[1,1,1],state_at_2=near[-1],
            divergence=-(10+1+8/3),scope='Finite trajectory divergence is illustrative, not a proof of chaos.'),
        pde=dict(heat_diffusivity=.08,wave_speed=1.,initial_modes=[1,.25],modes=[1,3],
            boundary='zero Dirichlet at xi=0,1',wave_initial_velocity=0.,
            wave_energy=25*np.pi**2/64,wave_displacement_at_half=0.))

def serial(x):
    if isinstance(x,np.ndarray):return x.tolist()
    if isinstance(x,np.generic):return x.item()
    raise TypeError(type(x).__name__)
if __name__=="__main__":print(json.dumps(summary(),ensure_ascii=False,indent=2,default=serial))
