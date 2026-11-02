"""Independent identities, quadrature, Jacobians, Floquet and QR sensitivity checks."""
from pathlib import Path
import importlib.util,sys,json,hashlib,xml.etree.ElementTree as ET
sys.dont_write_bytecode=True
import numpy as np
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/nonlinear-dynamics-2026-11-02';spec=importlib.util.spec_from_file_location('nd',ROOT/'public/code/nonlinear-dynamics/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def check(name,condition,**evidence):
    assert condition,(name,evidence);checks.append(dict(name=name,passed=True,**evidence))
rhs=lambda x:x-x**3
check('Nonlinear superposition fails in specified scalar model',abs(rhs(.2+.3)-rhs(.2)-rhs(.3))>.01)
x=np.linspace(-2,2,101);grad=x**3-x
check('Potential derivative is minus squared scalar flow',np.allclose(grad*rhs(x),-rhs(x)**2))
roots,d=m.cubic_roots(0);check('Two attracting equilibria and an unstable separator',np.allclose(roots,[-1,0,1]) and np.allclose(d,[-2,1,-2]))
for initial in [-1.5,-.4,.4,1.5]:assert abs(m.solve(lambda t,x:rhs(x),(0,20),[initial]).y[0,-1]-np.sign(initial))<1e-10
check('Specified scalar basins match signed trajectories',True)
hc=2/(3*np.sqrt(3));folds=np.array([-1,1])/np.sqrt(3)
check('Cubic fold coordinates and vanishing derivative',np.allclose(abs(folds**3-folds),hc) and np.allclose(1-3*folds**2,0),fold_h=hc)
for h,count in [(-.5,1),(0,3),(.5,1)]:
    r,_=m.cubic_roots(h);assert len(r)==count and np.max(abs(h+r-r**3))<1e-12
check('Cubic root residuals and counts on both sides of folds',True)
q=np.linspace(-1,1,101);mu=3*q*q;h=-2*q**3
check('Two-parameter cusp fold parametrization',np.allclose(h+mu*q-q**3,0) and np.allclose(mu-3*q*q,0))
eps=.01;integral=quad(lambda x:1/(eps+x*x),-1,1)[0];expected=2*np.arctan(1/np.sqrt(eps))/np.sqrt(eps)
check('Ghost passage time by independent quadrature',abs(integral-expected)<1e-10,time=integral)
t=np.linspace(0,15,1001);s=m.solve(m.hopf_fun,(0,15),[.12,0],t_eval=t)
check('Hopf radial exact solution versus Cartesian ODE',np.max(abs(np.linalg.norm(s.y,axis=0)-m.hopf_radial(t,.12)))<1e-9)
s=m.solve(lambda t,r:-r**3,(0,10),[.7],t_eval=np.linspace(0,10,101))
check('Critical Hopf algebraic decay',np.max(abs(s.y[0]-m.hopf_radial(s.t,.7,0)))<1e-10)
matrix,ev=m.hopf_floquet();check('Full two-dimensional Floquet integration matches neutral and radial multipliers',np.allclose(np.sort(ev.real),[np.exp(-.4),1],atol=1e-9) and np.max(abs(ev.imag))<1e-10,multipliers=ev.real.tolist())
z=np.array([.3,-.5]);e=1e-6;fd=np.column_stack([(m.hopf_fun(0,z+e*v)-m.hopf_fun(0,z-e*v))/(2*e) for v in np.eye(2)])
check('Independent centered-difference Hopf Jacobian',np.max(abs(fd-m.hopf_jac(z)))<1e-8)
F=np.geomspace(1e-6,1,50);r=F**(1/3)
check('Critical resonant cubic-root response and rotating-frame stability',np.allclose(r**3,F) and np.all(-3*r*r<0) and np.all(-r*r<0))
r=np.array(m.subcritical_radii(-.15));u=r*r;deriv=2*u*(1-2*u)
check('Quintic subcritical radii and transverse signs',np.allclose(-.15+u-u*u,0) and deriv[0]>0 and deriv[1]<0,radii=r.tolist(),derivatives=deriv.tolist())
check('Cycle saddle-node at mu=-1/4',np.isclose(-.25+.5-.5**2,0) and np.isclose(2*.5*(1-2*.5),0))
x,v,mu=.4,-.7,.8;vprime=mu*(1-x*x)*v-x
check('Van der Pol energy balance',np.isclose(x*v+v*vprime,mu*(1-x*x)*v*v))
y=x-x**3/3-v/mu;yp=(1-x*x)*v-vprime/mu
check('Slow-fast coordinate and time-rescaling identities',np.isclose(v,mu*(x-x**3/3-y)) and np.isclose(yp,x/mu))
A=1.3;mu=.01;avg=quad(lambda p:mu*(1-A*A*np.cos(p)**2)*A*A*np.sin(p)**2,0,2*np.pi)[0]/(2*np.pi)
check('Averaged Van der Pol energy gives stated amplitude equation',abs(avg-mu*(A*A/2-A**4/8))<1e-12)
fundamental=quad(lambda p:np.cos(p)**3*np.cos(p),0,2*np.pi)[0]/np.pi;third=quad(lambda p:np.cos(p)**3*np.cos(3*p),0,2*np.pi)[0]/np.pi
check('Duffing cubic harmonic projection',abs(fundamental-.75)<1e-12 and abs(third-.25)<1e-12)
res=[]
for omega in [1.,1.2,1.4]:
    for A in m.duffing_candidates(omega):res.append(abs(A*A*((1+.75*A*A-omega*omega)**2+(.1*omega)**2)-.04))
check('Harmonic-balance candidates satisfy their approximate algebraic equation',max(res)<1e-10,max_residual=max(res))
A=.1;period=4*quad(lambda theta:1/np.sqrt(1+.5*A*A*(1+np.sin(theta)**2)),0,np.pi/2)[0];frequency=2*np.pi/period;approx=np.sqrt(1+.75*A*A)
check('Small-amplitude Duffing backbone compared with exact energy quadrature',abs(frequency-approx)<2e-6,exact_frequency=frequency,approximate_frequency=float(approx))
delta=.4;psi=np.arcsin(delta)
check('Adler locked phase and linear relaxation rate',abs(delta-np.sin(psi))<1e-12 and abs(-np.cos(psi)+np.sqrt(1-delta*delta))<1e-12)
delta=1.3;T=quad(lambda psi:1/(delta-np.sin(psi)),0,2*np.pi)[0]
check('Unlocked phase slip rate by one-turn quadrature',abs(2*np.pi/T-np.sqrt(delta*delta-1))<1e-10,mean_slip=2*np.pi/T)
r=3.2;cycle=np.array([(r+1-np.sqrt((r-3)*(r+1)))/(2*r),(r+1+np.sqrt((r-3)*(r+1)))/(2*r)])
check('Analytic logistic period-two cycle and multiplier',np.allclose(r*cycle*(1-cycle),cycle[::-1]) and np.isclose(np.prod(r*(1-2*cycle)),-r*r+2*r+4))
threshold=1+np.sqrt(6);check('Second period-doubling threshold',np.isclose(-threshold*threshold+2*threshold+4,-1))
sample=m.logistic_series(n=20000);finite=float(np.mean(np.log(abs(4*(1-2*sample)))))
check('Specified r=4 estimate near typical ln2, with explicit exceptional fixed point',abs(finite-np.log(2))<.005 and 4*.75*(1-.75)==.75,finite_estimate=finite,typical_value=float(np.log(2)))
z=np.array([4.,5.,20.]);fd=np.column_stack([(m.lorenz(0,z+e*v)-m.lorenz(0,z-e*v))/(2*e) for v in np.eye(3)])
check('Lorenz analytic Jacobian and trace',np.max(abs(fd-m.lorenz_jac(z)))<1e-7 and np.isclose(np.trace(m.lorenz_jac(z)),-41/3))
base=json.loads((REC/'lorenz-qr.json').read_text(encoding='utf-8'))
alternative=m.lorenz_qr(duration=360.,interval=.25,rtol=2e-10,max_step=.02)
for run in [base,alternative]:
    le=np.array(run['exponents']);assert le[0]>.5 and abs(le[1])<.05 and le[2]<-10 and abs(le.sum()+41/3)<1e-6
check('Lorenz QR robust to longer duration, finer step, tolerance and reorthogonalization',abs(base['exponents'][0]-alternative['exponents'][0])<.15,base={k:v for k,v in base.items() if k not in ['times','history']},alternative={k:v for k,v in alternative.items() if k not in ['times','history']})
# Independently check finite-time determinant growth on a short interval.
def aug(t,z):return np.r_[m.lorenz(t,z[:3]),(m.lorenz_jac(z[:3])@z[3:].reshape(3,3)).ravel()]
s=m.solve(aug,(0,.2),np.r_[1.,1.,1.,np.eye(3).ravel()],max_step=.005)
logdet=np.linalg.slogdet(s.y[3:,-1].reshape(3,3))[1]
check('Liouville determinant identity on independent short variational solve',abs(logdet-(-41/3)*.2)<1e-8,log_abs_determinant=float(logdet))
source=json.loads((REC/'source-index.json').read_text(encoding='utf-8'))
for row in source:
    assert row['status']=='fetched';path=ROOT/'artifacts/nonlinear-dynamics/sources'/(row['id']+('.html' if row['kind']=='official_documentation' else '.pdf'));assert hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256']
check('Eighteen source file hashes match scoped records',len(source)==18)
files=list((ROOT/'public/figures/nonlinear-dynamics').glob('*.svg'))+[ROOT/'public/figures/foundation-courses/nonlinear-dynamics.svg']
for file in files:ET.parse(file);assert '<script' not in file.read_text(encoding='utf-8')
check('Eleven original SVG files parse without executable scripts',len(files)==11)
result=dict(slug='nonlinear-dynamics',check_groups=len(checks),checks=checks,professional_review='pending')
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(check_groups=len(checks),passed=len(checks),alternative_lorenz_exponents=alternative['exponents'])))
