"""Independent algebraic, quadrature, recurrence and finite precision cross-checks."""
from pathlib import Path
from fractions import Fraction as F
import sys,importlib.util,json,math,xml.etree.ElementTree as ET
sys.dont_write_bytecode=True
import numpy as np
import scipy
from scipy import integrate,special
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/calculus-2026-11-02'
spec=importlib.util.spec_from_file_location('models',ROOT/'public/code/calculus/experiments.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def close(a,b,tol=1e-10):np.testing.assert_allclose(a,b,atol=tol,rtol=tol)
def record(name,**metrics):checks.append(dict(check=name,status='passed',**metrics))
rng=np.random.default_rng(20261102)
# 1 Exact algebra and the epsilon-dependent bound, not a substitute for quantifiers.
for eps in [F(1,10000),F(3,10),F(10)]:
    delta=min(F(1),eps/3)
    for sign in [-1,1]:
        x=1+sign*delta*F(999,1000)
        assert abs(x*x-1)==abs(x-1)*abs(x+1)
        assert abs(x*x-1)<eps
record('Exact rational epsilon-delta inequality examples',proof='General inequality and quantifier order stated in article')
# 2 Changed point and cusp.
for h in [1e-2,1e-4,1e-6]:
    assert abs((1+h)**2-1.6)>.5
    close(abs(h)/h,1);close(abs(-h)/(-h),-1)
record('Changed point limit / continuity / absolute-value cusp')
# 3 Gaussian complex-step derivative independent of analytic expression.
a=.002;h=1e-24;cs=np.imag(m.pulse(a+1j*h))/h;analytic=float(m.pulse_derivative(a))
close(cs,analytic);close(analytic,-np.exp(-.5)/.002)
aa,hs,slopes,true=m.secants();assert abs(slopes[-1]-true)<abs(slopes[0]-true)
record('Gaussian derivative / complex step / secant convergence',derivative_Pa_per_s=analytic)
# 4 Product and chain rules in a time-varying tone.
t=.017;h=1e-22
A=lambda t:1+.2*np.cos(2*np.pi*5*t)
phase=lambda t:2*np.pi*(200*t+500*t*t)
wave=lambda t:A(t)*np.cos(phase(t))
Ap=-.2*2*np.pi*5*np.sin(2*np.pi*5*t);phip=2*np.pi*(200+1000*t)
close(np.imag(wave(t+1j*h))/h,Ap*np.cos(phase(t))-A(t)*phip*np.sin(phase(t)))
record('Envelope product / phase chain rule / physical seconds')
# 5 Mean-value bound for all sampled secants, derivative maximum derived analytically.
K=np.exp(-.5)/.002
left=rng.uniform(-.01,.01,10000);right=left+rng.uniform(1e-5,.004,10000)
assert np.max(abs((m.pulse(right)-m.pulse(left))/(right-left)))<=K*(1+1e-12)
record('Gaussian derivative maximum and Lipschitz-bound examples',bound_Pa_per_s=float(K))
# 6 Taylor coefficients vs integral remainder, independently integrated.
for n in [1,2,4]:
    for u in [.1,.2,.5,1.]:
        rem=(-1)**(n+1)/math.factorial(n)*integrate.quad(lambda t:np.exp(-t)*(u-t)**n,0,u)[0]
        close(np.exp(-u)-m.taylor(u,n),rem)
        assert abs(rem)<=u**(n+1)/math.factorial(n+1)+1e-15
record('Taylor polynomial / integral remainder / Lagrange upper bounds')
# 7 Flat-function structure: Laurent polynomial derivative recurrence.
# Each derivative equals P(1/u)*exp(-1/u**2), hence vanishes at zero.
P={0:1}
for order in range(1,9):
    nxt={}
    for power,coefficient in P.items():
        if power:nxt[power+1]=nxt.get(power+1,0)-power*coefficient
        nxt[power+3]=nxt.get(power+3,0)+2*coefficient
    P={p:c for p,c in nxt.items() if c}
    assert all(isinstance(p,int) and p>=0 for p in P)
assert max(P)==24
record('Flat smooth function derivative structure',orders_algebraically_generated=8,
       proof_scope='All-order induction and exponential domination explained in scientific audit; no finite check claimed as proof')
# 8 Exact midpoint sums plus upper/lower bounds for nonuniform partitions.
for N in [4,16,64]:
    exact=sum(((F(2*k+1,2*N))**2 for k in range(N)),F(0))/N
    assert exact==F(1,3)-F(1,12*N*N);close(float(exact),m.riemann(N))
breaks=np.r_[0,np.sort(rng.uniform(size=100)),1];dx=np.diff(breaks)
assert np.sum(breaks[:-1]**2*dx)<=1/3<=np.sum(breaks[1:]**2*dx)
record('Exact midpoint formula / nonuniform Riemann lower and upper sums')
# 9 FTC and three different cycle integrals using independent quadrature.
d=m.cycle();T=d['T']
for t in [.001,.003,.005,.01]:
    value=integrate.quad(lambda s:np.sin(2*np.pi*s/T),0,t,epsabs=1e-13)[0]
    close(value,T/(2*np.pi)*(1-np.cos(2*np.pi*t/T)))
close(integrate.quad(lambda t:np.sin(2*np.pi*t/T),0,T)[0],0)
close(integrate.quad(lambda t:abs(np.sin(2*np.pi*t/T)),0,T,points=[T/2])[0],2*T/np.pi)
close(integrate.quad(lambda t:np.sin(2*np.pi*t/T)**2,0,T)[0],T/2)
close(d['RMS'],1/np.sqrt(2))
record('FTC cumulative function / signed area / absolute area / square and RMS')
# 10 Change of variable and integration by parts, no dropped boundary or units.
tau=.002;b=.01
close(integrate.quad(lambda t:np.exp(-t/tau),0,b)[0],tau*integrate.quad(lambda u:np.exp(-u),0,b/tau)[0])
close(integrate.quad(lambda x:x*np.exp(x),0,1)[0],1)
record('Substitution with time Jacobian / integration-by-parts boundary term')
# 11 Improper integral truncations and principal-value distinction.
for R in [2,10,100]:
    close(integrate.quad(lambda x:1/x,1,R)[0],np.log(R))
    close(integrate.quad(lambda x:1/x**2,1,R)[0],1-1/R)
for e in [.1,.01,.001]:
    l=integrate.quad(lambda x:1/x,-1,-e)[0];r=integrate.quad(lambda x:1/x,e,1)[0]
    close(l+r,0);close(r,-np.log(e))
record('Improper truncation identities / separate divergent sides vs symmetric principal value')
# 12 Series exact geometric sums, harmonic grouping and square-tail bounds.
for ratio in [F(1,2),F(-1,3)]:
    assert sum((ratio**k for k in range(20)),F(0))==(1-ratio**20)/(1-ratio)
for j in range(1,12):
    assert sum((F(1,n) for n in range(2**(j-1)+1,2**j+1)),F(0))>=F(1,2)
for N in [10,100,1000]:
    tail=float(special.polygamma(1,N+1));assert 1/(N+1)<=tail<=1/N
record('Geometric series / harmonic divergence grouping / convergent square-series tails')
# 13 Partial derivatives do not imply continuity.
for h in [1e-1,1e-3,1e-6]:
    close(m.partial_counterexample(h,0)/h,0);close(m.partial_counterexample(0,h)/h,0)
    close(m.partial_counterexample(h,h),.5)
record('Axis partial derivatives / diagonal discontinuity counterexample')
# 14 Gradient, Hessian and directional derivative checked by polynomial expansion.
a,b=2.,.25;g=m.objective_gradient(a,b);close(g,[2,6]);H=np.diag([2.,8.])
for delta in [np.array([.1,-.2]),np.array([-.03,.04])]:
    close(m.objective(a+delta[0],b+delta[1])-m.objective(a,b),g@delta+.5*delta@H@delta)
assert np.all(np.linalg.eigvalsh(H)>0)
v=np.array([.6,.8]);h=1e-5
close((m.objective(a+h*v[0],b+h*v[1])-m.objective(a-h*v[0],b-h*v[1]))/(2*h),g@v,tol=1e-8)
record('Quadratic gradient / Hessian / directional derivative / unique global minimum')
# 15 Coordinate scaling changes normalized steepest directions.
scale=100.
scaled_gradient=np.array([g[0],g[1]/scale]);assert not np.allclose(scaled_gradient/np.linalg.norm(scaled_gradient),g/np.linalg.norm(g))
record('Coordinate scaling / Euclidean steepest-direction convention')
# 16 Linear covariance propagation via explicit correlated samples.
cov=np.array([[1e-4,3e-5],[3e-5,4e-5]])
draw=rng.multivariate_normal([0,0],cov,100000);linear=draw@g
theory=float(g@cov@g);observed=float(np.var(linear,ddof=1));assert abs(observed/theory-1)<.02
record('Exact linear covariance rule / correlated Monte Carlo',predicted_variance=theory,observed_variance=observed)
# 17 Fubini check for a continuous rectangular integrand.
q=lambda y,x:x+2*y
value=integrate.dblquad(q,0,1,0,1)[0];reverse=integrate.dblquad(lambda x,y:x+2*y,0,1,0,1)[0]
close(value,1.5);close(value,reverse)
record('Continuous rectangle double integral / both integration orders')
# 18 Polar determinant, disk Cartesian quadrature and radial expression.
for r,theta in [(0.3,.2),(2.1,1.7)]:
    J=np.array([[np.cos(theta),-r*np.sin(theta)],[np.sin(theta),r*np.cos(theta)]])
    close(np.linalg.det(J),r)
R=3.
cart=integrate.dblquad(lambda y,x:np.exp(-(x*x+y*y)/2),-R,R,
    lambda x:-np.sqrt(max(0,R*R-x*x)),lambda x:np.sqrt(max(0,R*R-x*x)),epsabs=1e-9,epsrel=1e-9)[0]
radial=integrate.quad(lambda r:2*np.pi*r*np.exp(-r*r/2),0,R)[0]
close(cart,m.disk(),tol=1e-8);close(radial,m.disk())
close(integrate.quad(lambda r:2*np.pi*r*np.exp(-r*r/2),0,np.inf)[0],2*np.pi)
record('Polar Jacobian / Cartesian disk quadrature / radial integral / normalization',disk_integral=cart)
# 19 Initial state and analytic ODE residual, then independent adaptive RK45.
t,yn,ya,err=m.ode_solution();assert err<1e-8
tau=.005
close(tau*(.6/tau)*np.exp(-t/tau)+m.decay_step(t,.4),1)
close(m.decay_step(0,.4),.4);close(m.decay_step(tau,0),1-np.exp(-1));close(m.decay_step(tau,.4),1-.6/np.e)
record('Linear initial value / residual / RK45 vs analytic',maximum_absolute_error=err)
# 20 Two exact nonlinear initial solutions (right-hand time domain).
t=np.linspace(0,1,101);close(t/2,np.sqrt(t*t/4));close(np.zeros_like(t),np.sqrt(np.zeros_like(t)))
record('Continuous nonlinear RHS / two exact solutions with identical initial value')
# 21 Euler recurrence and step-size boundary.
for h in [.001,.008,.012]:
    t,y=m.euler(h);n=np.arange(len(y));close(y,1-(1-h/.005)**n)
assert abs(1-.001/.005)<1 and abs(1-.008/.005)<1 and abs(1-.012/.005)>1
assert abs(1-.01/.005)==1
record('Euler exact recurrence / stable and unstable steps / neutral boundary')
# 22 Exact quadrature error expressions and numerical differentiation/noise.
for row in m.quadrature():
    N=row['intervals'];trap=F(1,5)+F(1,3*N*N)-F(1,30*N**4);simpson=F(1,5)+F(2,15*N**4)
    close(row['trapezoid'],float(trap));close(row['Simpson'],float(simpson))
ferr=[];cerr=[]
for h in [.01,.005]:
    ferr.append(abs((np.exp(1+h)-np.e)/h-np.e));cerr.append(abs((np.exp(1+h)-np.exp(1-h))/(2*h)-np.e))
assert 1.98<ferr[0]/ferr[1]<2.02 and 3.98<cerr[0]/cerr[1]<4.02
sigma,h,obs,theory=m.noise_difference();assert np.max(abs(obs/theory-1))<.01
record('Exact trapezoid/Simpson errors / finite difference orders / independent noise amplification',maximum_relative_SD_deviation=float(np.max(abs(obs/theory-1))))
# 23 Source and figure integrity.
sources=json.loads((REC/'source-index.json').read_text(encoding='utf-8'))
assert len(sources)==22 and all(r['status']=='fetched' for r in sources),[(r['id'],r['status']) for r in sources]
figs=list((ROOT/'public/figures/calculus').glob('*.svg'));assert len(figs)==10
for path in figs:ET.parse(path)
ET.parse(ROOT/'public/figures/foundation-courses/calculus.svg')
record('22 retrieved source records / 10 figure XML files / native course sketch')
result=dict(status='passed',check_groups=len(checks),numpy=np.__version__,scipy=scipy.__version__,checks=checks,
    limitations='Finite specified checks complement the stated mathematical arguments; not proofs by plotting, external professional review, or hearing/device validation.')
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status='passed',check_groups=len(checks),numpy=np.__version__,scipy=scipy.__version__)))
