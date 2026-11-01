"""Independent cross-checks for the specified teaching models, not physiological validation."""
from pathlib import Path
import sys,json,importlib.util,xml.etree.ElementTree as ET
sys.dont_write_bytecode=True
import numpy as np
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq
from scipy.linalg import solve_banded,expm
from scipy.stats import binom
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('m',ROOT/'public/code/biophysics/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def record(name,**data):checks.append(dict(name=name,status='passed',**data))
def close(x,y,rtol=1e-9,atol=1e-12):assert np.allclose(x,y,rtol=rtol,atol=atol),(x,y)
# Exact SI definitions, particle/molar scale and thermal weights.
close(m.R,8.31446261815324);close(m.F,96485.33212331001);close(m.kB*m.T/1e-21,4.2800119)
d=np.linspace(-5,5,101);p=m.open_prob(d*m.kB*m.T)
close(p/(1-p),np.exp(-d));assert np.all((p>0)&(p<1))
record('SI constants and Boltzmann odds',kBT_J=m.kB*m.T,RT_J_per_mol=m.R*m.T)
# Quadrature is independent of kernel construction; finite differences check the PDE.
for t in [.1,1.,5.]:
    D=100.;bound=15*np.sqrt(2*D*t)
    mass=quad(lambda x:m.diffusion(x,t),-bound,bound,epsabs=1e-11)[0]
    var=quad(lambda x:x*x*m.diffusion(x,t),-bound,bound,epsabs=1e-9)[0]
    close(mass,1);close(var,2*D*t)
    x=4.;dt=1e-5*t;dx=1e-2
    pt=(m.diffusion(x,t+dt)-m.diffusion(x,t-dt))/(2*dt)
    pxx=(m.diffusion(x+dx,t)-2*m.diffusion(x,t)+m.diffusion(x-dx,t))/dx**2
    close(pt,D*pxx,rtol=2e-5)
Dsi=m.kB*m.T/(6*np.pi*.001*5e-9);close(Dsi*1e12,45.4123366928,rtol=1e-9)
close(np.array([10,100])**2/(2*100),[.5,50])
record('Diffusion normalization, variance, PDE and Stokes–Einstein',D_um2_per_s=Dsi*1e12)
# Integrate mass-action reaction ODE, rather than evaluating the same analytical function.
err=0.
for scale in [.2,1,5]:
    kon,koff=scale*1e6,scale;c=2e-6;t=np.linspace(0,3,901)
    sol=solve_ivp(lambda _,y:[kon*c*(1-y[0])-koff*y[0]],(0,3),[0.],t_eval=t,rtol=1e-11,atol=1e-13)
    assert sol.success
    err=max(err,float(np.max(abs(sol.y[0]-m.binding(t,scale)))))
    close(koff/kon,1e-6,atol=1e-18)
assert err<1e-9
record('Binding ODE versus closed form; shared Kd does not set rate',max_absolute_error=err)
# Ideal one-valent Donnan: negative fixed charge A, electroneutrality and product law.
co,A=150.,100.;cp=(A+np.sqrt(A*A+4*co*co))/2;cm=cp-A
close(cp*cm,co**2);close(cp-cm,A)
close(m.nernst(1,cp,co),m.nernst(-1,cm,co))
close(m.R*m.T*(1e-3*1000),2577.483411627504)
record('Osmotic concentration conversion and Donnan equilibrium',inside_cation_mM=cp,inside_anion_mM=cm)
res=[]
for z in [-2,-1,1,2]:
    for ci,ce in [(140,5),(12,145),(10,120)]:
        V=m.nernst(z,ci,ce)
        res.append(abs(m.R*m.T*np.log(ci/ce)+z*m.F*V))
assert max(res)<1e-8
close([m.nernst(1,140,5),m.nernst(1,12,145),m.nernst(-1,10,120)],[-.08901562196158918,.0665660039154573,-.066381133052286])
record('Nernst electrochemical-potential equality, both signs and valences',max_residual_J_per_mol=max(res))
# Independent constant-field current, with outward conventional-current convention.
def current(V,z,ci,ce,P):
    u=z*m.F*V/(m.R*m.T)
    if abs(u)<1e-8:return P*z*m.F*(ci-ce)
    return P*z*m.F*u*(ci-ce*np.exp(-u))/(-np.expm1(-u))
errs=[]
for ko in [1.,5.,20.,100.]:
    for pk,pna,pcl in [(1,.04,.45),(.3,.2,.1),(1,0,0)]:
        f=lambda V:sum(current(V,z,ci,ce,P) for z,ci,ce,P in [(1,140,ko,pk),(1,12,145,pna),(-1,10,120,pcl)])
        root=brentq(f,-.25,.25,xtol=1e-14)
        errs.append(abs(root-m.ghk(ko,pk,pna,pcl)))
        assert abs(f(m.ghk(ko,pk,pna,pcl)))<1e-6
assert max(errs)<1e-12
record('GHK voltage versus independently rooted constant-field ion currents',max_voltage_error_V=max(errs),cases=len(errs))
# Unit conversion and charge counting by molar and particle routes.
A_si=1000*(1e-6)**2;C=(1e-6/(1e-2)**2)*A_si;Q=C*.070
close(C,10e-12,atol=1e-25);close(Q/m.e,Q/m.F*m.NA,rtol=1e-12)
s=m.summary();close(Q/m.e/s['membrane']['total_K_ions'],s['membrane']['fraction'])
record('Membrane area, capacitance, molar/particle charge consistency',C_F=C,charge_fraction=s['membrane']['fraction'])
# Independent membrane ODE and current balance.
t=np.linspace(0,.05,501);g=1e-9;EL=-.070;I=20e-12
sol=solve_ivp(lambda _,v:[(-g*(v[0]-EL)+I)/C],(0,.05),[EL],t_eval=t,rtol=1e-11,atol=1e-13)
v,cap,leak=m.passive(t);error=float(np.max(abs(sol.y[0]-v)))
assert sol.success and error<1e-10;close(cap+leak,I,atol=1e-22)
close(m.passive(.01)[0],-.05735758882342885)
record('Passive membrane independent ODE and branch charge balance',max_voltage_error_V=error)
# Markov master equation and exact binomial PMF moments.
Qm=np.array([[-100.,50.],[100.,-50.]])
for t0 in [0,.001,.01,.04]:
    q=expm(Qm*t0)@np.array([.8,.2]);close(q.sum(),1);close(q[1],m.gate(t0))
for N in [100,10000]:
    n=np.arange(N+1);pm=binom.pmf(n,N,.2);close(pm.sum(),1)
    mean=np.sum(n*pm);var=np.sum((n-mean)**2*pm)
    close(mean,N*.2);close(var,N*.2*.8)
    mi,si=m.channel_moments(N)
    close(mi,-mean*1e-12,atol=1e-23);close(si,np.sqrt(var)*1e-12,atol=1e-23)
record('Two-state master equation and exact binomial moments')
# Geometry parameters and an independent finite-difference boundary value solve.
a=1e-6;RM=1.;rho=1.;CM=.01
cm=2*np.pi*a*CM;ri=rho/(np.pi*a*a);rm=RM/(2*np.pi*a)
lam=np.sqrt(rm/ri);tau=rm*cm
close(lam,np.sqrt(a*RM/(2*rho)));close(tau,RM*CM)
n=6001;x=np.linspace(0,12*lam,n);h=x[1]-x[0];mask=x<=2*lam
errors=[]
for f in [0,10,100]:
    k2=ri/rm+2j*np.pi*f*ri*cm
    band=np.zeros((3,n-2),complex);band[0,1:]=1;band[1,:]=-2-k2*h*h;band[2,:-1]=1
    rhs=np.zeros(n-2,complex);rhs[0]=-1
    v=np.r_[1.,solve_banded((1,1),band,rhs),0.]
    err=float(np.max(abs(v[mask]-m.cable(x[mask],f))));errors.append(err)
assert max(errors)<1e-5
record('Cable geometry and independent complex finite-difference BVP',lambda_m=lam,tau_s=tau,max_voltage_ratio_error=max(errors),far_boundary_lambda=12)
# Mechanical distribution integrals in nm avoid numerical underflow in SI quadrature.
d=m.mechanics();sd=d['rms']*1e9;density=lambda x:np.exp(-x*x/(2*sd*sd))/(np.sqrt(2*np.pi)*sd)
close(quad(density,-15*sd,15*sd)[0],1)
var=quad(lambda x:x*x*density(x),-15*sd,15*sd)[0]*1e-18
close(var,m.kB*m.T/d['k'],atol=1e-27)
# Integrate dimensionless overdamped mean displacement and Lorentzian power spectrum.
tt=np.linspace(0,6*d['tau'],501)
sol=solve_ivp(lambda t,y:[(1-y[0])/d['tau']],(0,tt[-1]),[0.],t_eval=tt,rtol=1e-11,atol=1e-13)
assert np.max(abs(sol.y[0]-(1-np.exp(-tt/d['tau']))))<1e-9
# Integral of normalized two-sided angular-frequency PSD is 1.
close(quad(lambda u:1/(np.pi*(1+u*u)),-np.inf,np.inf)[0],1)
record('Overdamped response, Gaussian equipartition and OU spectrum normalization',rms_nm=sd,tau_s=d['tau'])
# MET and voltage reference invariance. KCL root is independent of weighted-average expression.
for x0 in [-80e-9,10e-9,100e-9]:
    p,v=m.transduction(x0);gm=10e-9*p
    root=brentq(lambda V:20e-9*(V+.080)+gm*(V-.080),-.1,.1)
    close(root,v)
close(m.transduction(10e-9)[0],.5);close(m.transduction(10e-9)[1],-.048)
for shift in [-.1,0.,.05]:
    vi,ve,vp=-.060+shift,.080+shift,shift
    close(vi-ve,-.140);close(vi-vp,-.060)
    Em_relative_to_peri=(ve-vp)+0.
    assert 10e-9*((vi-vp)-Em_relative_to_peri)<0
    assert 20e-9*((vi-vp)-(-.080))>0
record('MET logistic half-point, KCL and reference-invariant driving signs',width_nm=m.kB*m.T/.3e-12*1e9)
# 10 pA inward for 1 ms, no buffers/pumps: amount then volume-normalized concentration.
Ica=-10e-12;duration=.001;mol=-Ica*duration/(2*m.F);vol_L=1e-12
close(mol*m.NA,-Ica*duration/(2*m.e),atol=1e-8)
assert mol>0
record('Calcium divalent charge-to-amount conversion',amount_mol=mol,unbuffered_delta_M=mol/vol_L)
idx=json.loads((ROOT/'docs/research/biophysics-2026-11-02/source-index.json').read_text(encoding='utf-8'))
assert len(idx)==24 and all(r['status']=='fetched' and r.get('sha256') for r in idx)
figs=sorted((ROOT/'public/figures/biophysics').glob('*.svg'));assert len(figs)==10
for fig in figs:assert ET.parse(fig).getroot().tag.endswith('svg')
record('Source audit records and all scientific SVGs',sources=len(idx),abstract_sources=sum(r['access']=='abstract' for r in idx),figures=len(figs))
out=dict(scope='Independent numerical/structural checks of specified ideal teaching models; no expert review or biological validation.',checks=checks,total_checks=len(checks),passed=True)
(ROOT/'docs/research/biophysics-2026-11-02/numerical-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=True,indent=2))
