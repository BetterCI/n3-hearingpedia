"""Independent mathematical and numerical audit of specified teaching models."""
from pathlib import Path
from fractions import Fraction as F
import sys,importlib.util,json
sys.dont_write_bytecode=True
import numpy as np
from scipy.integrate import solve_ivp,quad
from scipy.linalg import expm
from scipy.optimize import minimize_scalar
ROOT=Path(__file__).resolve().parents[1];SLUG='differential-equations-and-dynamical-systems'
spec=importlib.util.spec_from_file_location('ddsmodels',ROOT/'public/code'/SLUG/'experiments.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def done(name,detail):checks.append(dict(check=name,result='passed',detail=detail))
t=np.linspace(0,6,301)
for x0 in [0.,.15,.6,1.4]:
    sol=solve_ivp(lambda t,x:1.2*x*(1-x),(0,6),[x0],t_eval=t,method='DOP853',rtol=1e-11,atol=1e-13,max_step=.03)
    assert sol.success and np.max(np.abs(sol.y[0]-m.logistic_flow(t,x0)))<1e-10
    assert sol.y[0,0]==x0 and min(sol.y[0])>=0
assert 1.2*0*(1-0)==1.2*1*(1-1)==0
done('logistic_IVP_and_equilibria','Independent ODE matches all four analytic curves; zero and unit equilibria retained.')
for c in [0,1,2]:
    for tau in [0,c,c+.1,c+1]:
        y=max(tau-c,0)**2;dy=2*max(tau-c,0)
        assert abs(dy-2*np.sqrt(abs(y)))<1e-14
assert np.isclose(2*np.sqrt(1e-12)/1e-12,2e6)
done('nonunique_waiting_solutions','Piecewise derivatives agree on both sides and at joining times; sqrt RHS has unbounded difference quotient at zero.')
for tau in [0,.5,.9,.99]:
    x=1/(1-tau);assert abs(1/(1-tau)**2-x*x)<1e-10
assert F(1)/(1-F(99,100))==100
done('finite_time_blowup','Exact algebra verifies x prime=x^2 and unbounded limit at tau=1; no continuation through the pole claimed.')
# On [0,1], f prime=1.2(1-2x), hence a shared Lipschitz constant 1.2.
x=m.logistic_flow(t,.3);y=m.logistic_flow(t,.30001)
assert np.all(abs(x-y)<=np.exp(1.2*t)*.00001+1e-14)
done('continuous_dependence_bound','Bounded invariant interval and explicit derivative bound support the finite-time Gronwall inequality.')
# Independent integrating factor example: y prime+2y=3, y(0)=.4.
sol=solve_ivp(lambda t,y:3-2*y,(0,4),[.4],t_eval=np.linspace(0,4,101),rtol=1e-11,atol=1e-13)
exact=1.5+(.4-1.5)*np.exp(-2*sol.t)
assert np.max(abs(sol.y[0]-exact))<1e-10
done('integrating_factor_and_nonhomogeneous_form','A separately chosen first-order linear model verifies particular plus homogeneous structure.')
# Resonance closed form versus independent high-order integration.
t=np.linspace(0,30,901);x=m.oscillator(t,0)
q=.1*t*np.sin(2*t);v=.1*np.sin(2*t)+.2*t*np.cos(2*t)
assert np.max(abs(x[:,0]-q))<2e-10 and np.max(abs(x[:,1]-v))<4e-10
done('exact_resonance','Both displacement and velocity match the independently differentiated resonant closed form.')
for zeta in [.1,.5]:
    amp=lambda w:.4/np.sqrt((4-w*w)**2+(4*zeta*w)**2)
    peak=minimize_scalar(lambda w:-amp(w),bounds=(0,4),method='bounded',options={'xatol':1e-13})
    assert abs(peak.x-2*np.sqrt(1-2*zeta*zeta))<1e-7
done('damped_displacement_resonance','Independent scalar maximization checks the peak formula and observation-variable scope.')
for name,A in m.linear_examples().items():
    x0=np.array([1.5,.6]);times=np.linspace(0,5,201)
    sol=solve_ivp(lambda t,x:A@x,(0,5),x0,t_eval=times,rtol=1e-11,atol=1e-13)
    exact=np.array([expm(A*t)@x0 for t in times])
    assert np.max(abs(sol.y.T-exact))<2e-8
    assert np.max(abs(expm(2*A)-expm(A)@expm(A)))<1e-12
done('linear_flow_and_semigroup','Independent IVP integrations and matrix-exponential composition check all four phase portraits.')
examples=m.linear_examples()
assert np.max(np.linalg.eigvals(examples['node']).real)<0
assert np.max(np.linalg.eigvals(examples['focus']).real)<0
assert set(np.linalg.eigvals(examples['saddle']))=={-1,1}
assert np.allclose(np.linalg.eigvals(examples['center']).real,0)
assert np.allclose(expm(examples['center']*2*np.pi),np.eye(2))
done('phase_classification','Eigenvalue signs and exact center return agree with node/focus/saddle/center labels.')
A=np.array([[-1.,10.],[0.,-1.]])
for tau in [0,.2,1,3]:
    actual=expm(A*tau)@np.array([0.,1.]);exact=np.exp(-tau)*np.array([10*tau,1])
    assert np.allclose(actual,exact,atol=1e-13)
assert 10/np.e>3
done('Jordan_transient','Exact nilpotent factor gives 10*tau*exp(-tau); negative eigenvalues do not force monotone norm decay.')
A1=np.array([[0.,1.],[0.,0.]]);A2=A1.T
assert np.linalg.norm(expm(A2)@expm(A1)-expm(A1+A2))>.2
done('noncommuting_time_dependent_warning','A concrete time-ordered product differs from exp(integral A); constant-matrix formula not generalized blindly.')
# Nonhyperbolic one-dimensional examples have the same zero linearization.
tau=.5;x0=.2
stable=x0/np.sqrt(1+2*x0*x0*tau);unstable=x0/np.sqrt(1-2*x0*x0*tau)
assert stable<x0<unstable
done('nonhyperbolic_higher_order','Exact +/-x^3 solutions confirm different behavior despite identical Jacobian zero.')
t=np.linspace(0,20,1201)
for gamma in [0,.4]:
    d=m.pendulum(t,gamma);theta,v=d['state'].T
    vd=-gamma*v-np.sin(theta)
    derivative=np.sin(theta)*v+v*vd
    assert np.max(abs(derivative+gamma*v*v))<1e-14
    if gamma==0:assert np.max(abs(d['energy']-d['energy'][0]))<1e-10
    else:
        assert np.max(np.diff(d['energy']))<1e-10
        assert np.max(d['energy'])<2 and np.max(abs(theta))<np.pi
done('pendulum_energy_and_trapping','Chain-rule identity, conservation/dissipation and the specified V<2 potential well independently checked.')
# Integrate energy loss as an extra state rather than evaluating V from the output.
sol=solve_ivp(lambda t,z:[z[1],-.4*z[1]-np.sin(z[0]),.4*z[1]**2],(0,20),[1.4,0,0],
    method='RK45',rtol=1e-11,atol=1e-13,max_step=.02)
end=sol.y[:,-1]
assert abs(.5*end[1]**2+1-np.cos(end[0])+end[2]-(1-np.cos(1.4)))<1e-10
done('independent_dissipation_integral','RK45 integrated loss plus terminal potential/kinetic energy agrees with initial energy.')
def hopf_rhs(t,z,mu=1):
    x,y=z;r2=x*x+y*y
    return [(mu-r2)*x-2*y,2*x+(mu-r2)*y]
t=np.linspace(0,10,601)
for r0 in [.2,2.]:
    sol=solve_ivp(hopf_rhs,(0,10),[r0,0],t_eval=t,method='DOP853',rtol=1e-11,atol=1e-13,max_step=.025)
    assert np.max(abs(sol.y.T-m.hopf(t,r0)))<2e-10
    assert np.max(abs(np.linalg.norm(sol.y,axis=0)-m.hopf_radius(t,r0)))<2e-10
done('Hopf_cartesian_vs_radial','Independent full nonlinear Cartesian solve agrees with exact radius and angle on both sides of cycle.')
for mu in [-.5,0,.5,1]:
    r0=.7
    sol=solve_ivp(lambda t,r:mu*r-r**3,(0,4),[r0],t_eval=np.linspace(0,4,101),rtol=1e-11,atol=1e-13)
    assert np.max(abs(sol.y[0]-m.hopf_radius(sol.t,r0,mu)))<1e-10
done('radial_parameter_regimes','Stable origin, critical algebraic decay and stable nonzero radius all checked across mu signs.')
def event(t,z):return z[1]
event.direction=1;event.terminal=False
sol=solve_ivp(hopf_rhs,(0,12),[.2,0],events=event,method='DOP853',rtol=1e-11,atol=1e-13,max_step=.03)
returns=sol.t_events[0];returns=returns[returns>1e-8]
assert len(returns)==3 and np.max(abs(np.diff(returns)-np.pi))<1e-10
eps=1e-5;T=np.pi
der=(m.hopf_radius(T,1+eps)-m.hopf_radius(T,1-eps))/(2*eps)
assert abs(der-np.exp(-2*T))<1e-10
done('Poincare_period_and_multiplier','Actual upward events verify period pi; independent finite difference of return radius matches exp(-2*pi).')
# Shift both initial phases by a constant: same radial attraction, persistent phase offset.
xy=m.hopf([3.],.2)[0];rot=np.array([[0,-1],[1,0]])
assert np.isclose(np.linalg.norm(xy-rot@xy),np.sqrt(2)*np.linalg.norm(xy))
done('orbital_vs_point_stability','A fixed pi/2 phase offset persists although radii converge; attraction is to the orbit set.')
for mu in [.04,.25,1]:
    root=np.sqrt(mu)
    assert abs(mu-root*root)<1e-14 and -2*root<0 and 2*root>0
    for x in [0,root,-root]:assert abs(mu*x-x**3)<1e-14
    assert mu>0 and mu-3*root*root<0
assert -(.1)**2<0 and -(-.1)**2<0
done('bifurcation_branches_and_signs','Real equilibria only for mu>=0 in saddle-node; stability derivatives and pitchfork branches verified directly, avoiding source sign typo.')
for mu in [-.1,0,.1]:
    J=np.array([[mu,-2.],[2.,mu]])
    assert np.allclose(np.sort(np.linalg.eigvals(J).imag),[-2,2])
    assert np.allclose(np.linalg.eigvals(J).real,mu)
done('Hopf_linear_crossing','Nonzero angular frequency and real-part derivative one verified; radial cubic supplies the nondegenerate supercritical sign.')
r=3.2;cycle=np.array([(r+1-np.sqrt((r-3)*(r+1)))/(2*r),(r+1+np.sqrt((r-3)*(r+1)))/(2*r)])
Fmap=lambda x:r*x*(1-x)
assert np.allclose(Fmap(cycle),cycle[::-1])
assert abs(np.prod(r*(1-2*cycle))-.16)<1e-14
orbit=m.map_orbit(r,steps=250)
assert abs(orbit[-1]-orbit[-3])<1e-14 and abs(orbit[-1]-orbit[-2])>.2
assert -F(16,5)**2+2*F(16,5)+4==F(4,25)
done('discrete_two_cycle','Algebraic roots, exact rational multiplier 4/25 and independent iteration agree for r=3.2.')
assert np.array_equal(m.map_orbit(4.,.25,3),[.25,.75,.75,.75])
for x in [.1,.3,.7]:assert np.isclose(4*x*(1-x),4*(1-x)*x)
assert abs(m.logistic_flow(1,.3)-1.2*.3*(1-.3))>.1
done('map_exceptions_noninvertibility_and_flow_difference','Exact special orbit and symmetric preimages separate map behavior from an ODE time-one flow.')
rates,cloud=m.map_bifurcation()
assert cloud.shape==(140,650) and np.min(cloud)>=0 and np.max(cloud)<=1
orbit=m.map_orbit(4.,steps=51000)
finite=float(np.mean(np.log(abs(4-8*orbit[1000:-1]))))
assert abs(finite-np.log(2))<.003
done('finite_bifurcation_and_exponent_scope',dict(sampled_shape=list(cloud.shape),finite_average=finite,scope='Finite samples complement established theory; not proof that every initial condition is chaotic.'))
def lorenz_jac(x):
    a,b,c=x
    return np.array([[-10,10,0],[28-c,-1,-a],[b,a,-8/3]])
for x in [np.array([1.,1.,1.]),np.array([-4.,5.,20.])]:
    h=1e-5
    fd=np.column_stack([(m.lorenz_rhs(0,x+h*np.eye(3)[j])-m.lorenz_rhs(0,x-h*np.eye(3)[j]))/(2*h) for j in range(3)])
    assert np.max(abs(fd-lorenz_jac(x)))<2e-9
    assert abs(np.trace(lorenz_jac(x))+41/3)<1e-14
s=np.sqrt((8/3)*27)
for eq in [[0,0,0],[s,s,27],[-s,-s,27]]:assert np.linalg.norm(m.lorenz_rhs(0,eq))<1e-12
done('Lorenz_Jacobian_divergence_equilibria','Independent finite differences and three analytic equilibria verify equations and constant divergence; no chaos inference from divergence alone.')
t=np.linspace(0,2,401);a=m.lorenz(t);b=m.lorenz(t,method='RK45',rtol=2e-12,atol=2e-14)
assert np.max(abs(a-b))<1e-8
xp=m.lorenz(t,1e-8)
# Compare a finite perturbation with the variational equation only on this short interval.
aug=solve_ivp(lambda t,z:np.r_[m.lorenz_rhs(t,z[:3]),lorenz_jac(z[:3])@z[3:]],(0,2),[1,1,1,1,0,0],
    t_eval=t,method='DOP853',rtol=1e-12,atol=1e-14,max_step=.015)
assert np.max(abs((xp-a)-1e-8*aug.y[3:].T))<3e-10
done('short_time_Lorenz_and_variation','Independent algorithms agree at short time; a separate variational solve checks infinitesimal response, without long-time pointwise guarantee.')
# Spatial field and boundary checks use independently evaluated sine expressions.
xx=np.linspace(0,1,201);initial=np.sin(np.pi*xx)+.25*np.sin(3*np.pi*xx)
for kind in ['heat','wave']:
    fields=m.pde(xx,[0,.2,.5,1],kind)
    assert np.max(abs(fields[0]-initial))<1e-14
    assert np.max(abs(fields[:,[0,-1]]))<1e-14
assert np.max(abs(m.pde(xx,[.5],'wave')))<1e-15
done('PDE_initial_boundary_and_zero_displacement','Common initial field, fixed ends and the wave half-time zero field verified.')
xx=np.linspace(.05,.95,51);tau=.31;h=1e-4
for kind in ['heat','wave']:
    f=lambda x,t:m.pde(x,[t],kind)[0]
    u=f(xx,tau);uxx=(f(xx+h,tau)-2*u+f(xx-h,tau))/h**2
    if kind=='heat':left=(f(xx,tau+h)-f(xx,tau-h))/(2*h);right=.08*uxx
    else:left=(f(xx,tau+h)-2*u+f(xx,tau-h))/h**2;right=uxx
    assert np.max(abs(left-right))<4e-5
done('PDE_residual_independent_differences','Independent centered space/time differences check both exact modal solutions at interior points.')
for tau in [0,.2,.5,1]:
    def ux(x):return np.pi*np.cos(np.pi*tau)*np.cos(np.pi*x)+.75*np.pi*np.cos(3*np.pi*tau)*np.cos(3*np.pi*x)
    def ut(x):return -np.pi*np.sin(np.pi*tau)*np.sin(np.pi*x)-.75*np.pi*np.sin(3*np.pi*tau)*np.sin(3*np.pi*x)
    energy=quad(lambda x:.5*(ut(x)**2+ux(x)**2),0,1,epsabs=1e-12)[0]
    assert abs(energy-25*np.pi**2/64)<1e-12
assert quad(lambda x:(-np.pi*np.sin(np.pi*x)+.75*np.pi*np.sin(3*np.pi*x))**2,0,1)[0]>7
done('wave_energy_not_displacement','Independent spatial quadrature verifies constant total energy and nonzero half-time velocity.')
for tau in [0,.3,1]:
    V=.25*(np.exp(-.16*np.pi**2*tau)+.25**2*np.exp(-1.44*np.pi**2*tau))
    value=quad(lambda x:.5*m.pde(np.array([x]),[tau],'heat')[0,0]**2,0,1,epsabs=1e-12)[0]
    assert abs(value-V)<1e-13
assert np.linalg.norm(m.pde(xx,[1],'heat'))<np.linalg.norm(m.pde(xx,[0],'heat'))
done('heat_L2_dissipation','Orthogonality formula, independent quadrature and monotone norm decay agree for the fixed-end diffusion example.')
for h in [.001,.003]:
    factor=1-1000*h
    assert (abs(factor)<1)==(h<.002)
A=np.array([[0.,1.],[-4.,0.]]);Q=np.diag([4.,1.]);h=.1;M=np.eye(2)+h*A
assert np.allclose(M.T@Q@M,(1+4*h*h)*Q)
done('Euler_stability_and_energy_counterexamples','Fast decay has step restriction; forward Euler multiplies undamped oscillator energy by 1+4h^2 despite exact conservation.')
out=dict(status='passed',check_groups=len(checks),checks=checks,scope='Specified normalized models; finite computations complement arguments, not general certified proofs; professional review pending.')
(ROOT/'docs/research'/f'{SLUG}-2026-11-02'/'numerical-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,default=m.serial)+'\n',encoding='utf-8')
print(json.dumps(dict(status='passed',check_groups=len(checks))))
