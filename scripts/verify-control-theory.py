"""Independent analytic, algebraic, frequency and numerical cross-checks."""
from pathlib import Path
from fractions import Fraction as F
import sys,importlib.util,json
sys.dont_write_bytecode=True
import numpy as np
from scipy import signal
from scipy.linalg import expm,solve_continuous_lyapunov
from scipy.integrate import solve_ivp,quad
from scipy.optimize import root,brentq
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('ctmodels',ROOT/'public/code/control-theory/experiments.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def done(name,detail):checks.append(dict(check=name,result='passed',detail=detail))
# 1 Independent ODE solution with the input discontinuity explicitly split.
t=np.linspace(0,8,801)
for closed in [False,True]:
    first=solve_ivp(lambda tt,y:-(5 if closed else 1)*y+(4 if closed else 1),(0,3),[0.],rtol=1e-11,atol=1e-13,dense_output=True)
    second=solve_ivp(lambda tt,y:-(5 if closed else 1)*y+(4 if closed else 1)+.3,(3,8),first.y[:,-1],rtol=1e-11,atol=1e-13,dense_output=True)
    y=np.r_[first.sol(t[t<=3])[0],second.sol(t[t>3])[0]]
    analytic=m.proportional(t)[int(closed)]
    assert np.max(np.abs(y-analytic))<1e-9
assert (F(4)+F(3,10))/5==F(43,50)
done('proportional_response_and_equilibrium','Piecewise high-accuracy ODE and exact rational steady output 43/50 independently verify the analytic graph.')
# 2 State transfer equivalence.
A,B,C=m.plant()
for s in [.2+1j,1.3+2j,3j]:
    g=(C@np.linalg.solve(s*np.eye(2)-A,B))[0,0]
    assert abs(g-1/(s*s+.6*s+2))<1e-13
done('state_transfer_equivalence','Three complex points verify C(sI-A)^-1B versus independently derived scalar denominator.')
# 3 Hidden unstable mode and minimal input/output map.
Ah=np.diag([-1.,1.]);Bh=np.array([[1.],[0.]]);Ch=np.array([[1.,0.]])
assert np.max(np.linalg.eigvals(Ah))==1
assert np.linalg.matrix_rank(np.hstack((Bh,Ah@Bh)))==1
assert np.linalg.matrix_rank(np.vstack((Ch,Ch@Ah)))==1
assert np.allclose(expm(Ah*8)@np.array([1.,.02]),[np.exp(-8),.02*np.exp(8)])
for s in [1+2j,2+3j]:assert abs((Ch@np.linalg.solve(s*np.eye(2)-Ah,Bh))[0,0]-1/(s+1))<1e-13
done('hidden_internal_instability','An uncontrollable/unobservable +1 mode grows while the reduced transfer remains 1/(s+1).')
# 4 Standard second-order response independently from the pole residue form.
t=np.linspace(0,8,801)
for z in [.2,.7,1.2]:
    _,numerical=signal.step(([4.],[1.,4*z,4.]),T=t)
    if z<1:
        wd=2*np.sqrt(1-z*z)
        analytic=1-np.exp(-2*z*t)*(np.cos(wd*t)+z/np.sqrt(1-z*z)*np.sin(wd*t))
    else:
        p1=-2*z+2*np.sqrt(z*z-1);p2=-2*z-2*np.sqrt(z*z-1)
        analytic=1+(p2*np.exp(p1*t)-p1*np.exp(p2*t))/(p1-p2)
    assert np.max(np.abs(numerical-analytic))<1e-12
done('second_order_response','Underdamped trigonometric and overdamped exponential formulas independently match all three plotted responses.')
for z in [.2,.7]:
    tp=np.pi/(2*np.sqrt(1-z*z));mp=np.exp(-np.pi*z/np.sqrt(1-z*z))
    _,yp=signal.step(([4.],[1.,4*z,4.]),T=np.array([0.,tp]))
    assert abs(yp[-1]-1-mp)<1e-12
done('peak_time_and_overshoot','Analytic peak time and overshoot agree with independent state propagation at exactly the predicted time.')
# 6 A complete cubic Routh criterion and numerical root count.
for k in np.r_[np.linspace(.01,5.99,61),np.linspace(6.01,12,61)]:
    r=np.roots([1,3,2,k])
    assert (np.max(r.real)<0)==(0<k<6)
    assert np.count_nonzero(r.real>0)==(0 if k<6 else 2)
assert np.array_equal(np.polymul([1,3],[1,0,2]),[1,3,2,6])
done('Routh_interval_and_boundary','All first-column signs give 0<K<6; 122 sample root counts and exact factorization at K=6 cross-check.')
# 7 Root response independently through scalar third-order ODE.
tt=np.linspace(0,25,501)
for k in [2,5,8]:
    a=np.array([[0,1,0],[0,0,1],[-k,-2,-3]],dtype=float)
    sol=solve_ivp(lambda t,x:a@x+[0,0,k],(0,25),[0,0,0],t_eval=tt,rtol=1e-10,atol=1e-12)
    assert np.max(np.abs(sol.y[0]-m.root_response(k,tt)))<2e-8
done('root_locus_step_responses','Independent third-order ODE with explicit forcing verifies all three plotted step responses.')
# 8 Feedback algebra at a complex test point, independent linear system solve.
for w in [.1,1.,7.]:
    p=1/((1j*w+1)*(1j*w+2));cc=4.;l=p*cc;s=1/(1+l);T=l/(1+l)
    assert abs(s+T-1)<1e-14 and abs(s)+abs(T)>=1-1e-14
    for r,d,n in [(1,0,0),(0,1,0),(0,0,1)]:
        # y-p*u=p*d; cc*y+u=cc*(r-n)
        yy=np.linalg.solve(np.array([[1,-p],[cc,1]],complex),[p*d,cc*(r-n)])[0]
        assert abs(yy-(T*r+p*s*d-T*n))<1e-14
done('S_T_and_disturbance_locations','Independent two-equation interconnection checks reference, input disturbance and measurement-noise signs.')
w=np.logspace(-3,3,2000)
assert np.max(np.abs(abs(m.loop(w,1.5))-abs(m.loop(w,0))))<1e-14
done('pure_delay_magnitude','Exact exponential preserves loop magnitude over the specified frequency range.')
mar=m.margins();wc=brentq(lambda w:abs(m.loop(w))-1,.1,4,xtol=1e-14)
assert abs(wc-mar['crossover'])<1e-13
assert abs(1+m.loop(wc,mar['delay_margin']))<1e-14
assert abs(mar['phase_margin_degrees']-93.26760361817844)<1e-10
done('gain_crossover_and_exact_delay_crossing','Independent bracketed solve finds unity crossing; exact delayed characteristic vanishes at the predicted first boundary.')
def dde_root(theta,guess):
    def residual(v):
        s=v[0]+1j*v[1];f=(s+1)*(s+2)+4*np.exp(-theta*s)
        return [f.real,f.imag]
    rr=root(residual,guess,tol=1e-11)
    assert rr.success and np.linalg.norm(residual(rr.x))<1e-10
    return rr.x
left=dde_root(1.,[-.1,1.5]);right=dde_root(1.5,[.1,1.2])
assert left[0]<0<right[0]
done('delay_characteristic_pair',dict(root_at_theta_1=left,root_at_theta_1_5=right,scope='Checks this crossing pair, not all delay roots by finite search.'))
# 12 The full frequency contour plus its asymptotic closure gives a winding cross-check.
ww=np.r_[-np.logspace(5,-5,20000),0,np.logspace(-5,5,20000)]
for theta,expected in [(0,0),(1.,0),(1.5,2)]:
    z=1+m.loop(ww,theta);z=np.r_[z,z[0]]
    N=-np.sum(np.angle(z[1:]/z[:-1]))/(2*np.pi)
    assert abs(N-expected)<1e-10
done('Nyquist_orientation_and_winding','Both frequency halves, clockwise-positive convention and asymptotic closure give N=0,0,2; numerical corroboration of analytic boundary only.')
# 13 Analytic H-infinity bound, not a grid maximum used as a certificate.
# T0(s)=4/(s^2+3s+6), |den(jw)|^2=(w^2-1.5)^2+33.75.
peak=4/np.sqrt(33.75)
assert abs(abs(m.loop(np.sqrt(1.5))/(1+m.loop(np.sqrt(1.5))))-peak)<1e-14
assert .2*peak<1
done('small_gain_example_bound','An independently completed square yields a continuous-frequency bound for W=0.2 and the undelayed stable loop.')
# 14 Linear PI is stable when unsaturated, but cannot achieve unreachable reference 2.
assert np.max(np.roots([1,3,1]).real)<0
without=m.windup(False);i=round(8/.0025)
assert abs(without['y'][i]-(1-np.exp(-8)))<1e-10
assert abs(without['integral'][i]-(8.5-4-np.exp(-8)))<1e-10
assert without['actual'][i]==1 and without['command'][i]>3.5
done('windup_analytic_segment','Exact saturated trajectory independently verifies delayed recovery through tau=8.')
# 15 Independent adaptive integration across the known reference switch.
for anti in [False,True]:
    def dyn(ref):
        def fun(t,v):
            y,z=v;e=ref-y;uc=2*e+z;u=np.clip(uc,-1,1)
            return [-y+u,e+(2*(u-uc) if anti else 0)]
        return fun
    first=solve_ivp(dyn(2),(0,5),[0,0],rtol=1e-10,atol=1e-12,dense_output=True,max_step=.02)
    second=solve_ivp(dyn(.5),(5,14),first.y[:,-1],rtol=1e-10,atol=1e-12,dense_output=True,max_step=.02)
    d=m.windup(anti);idx=d['t']<=5
    ref=np.vstack((first.sol(d['t'][idx]).T,second.sol(d['t'][~idx]).T))
    assert np.max(np.abs(np.c_[d['y'],d['integral']]-ref))<2e-5
    fine=m.windup(anti,dt=.00125)
    assert np.max(np.abs(d['y']-fine['y'][::2]))<2e-5
done('windup_independent_integration','Piecewise adaptive ODE and RK4 step halving check saturation transitions and reference boundary.')
# 16 Exact ranks and invariance under an invertible coordinate change.
assert F(-3,5)==F('-.6')
assert np.linalg.det(np.hstack((B,A@B)))==-1
assert np.array_equal(np.vstack((C,C@A)),np.eye(2))
V=np.array([[2.,1.],[0.,.5]]);Av=np.linalg.solve(V,A@V);Bv=np.linalg.solve(V,B);Cv=C@V
assert np.linalg.matrix_rank(np.hstack((Bv,Av@Bv)))==2
assert np.linalg.matrix_rank(np.vstack((Cv,Cv@Av)))==2
done('controllability_observability_and_coordinates','Exact determinants and invertible state transformation independently verify structure.')
k=np.array([[4.,4.4]]);lo=np.array([[8.4],[12.96]])
assert np.allclose(np.poly(A-B@k),[1,5,6])
assert np.allclose(np.poly(A-lo@C),[1,9,20])
assert np.allclose(m.state_feedback([0])['k'],k) and np.allclose(m.observer([0])['l'],lo)
done('pole_placement_closed_form','Hand-derived characteristic coefficients independently confirm both API gains.')
# 18 Direct integration cross-checks matrix-exponential state propagation.
tt=np.linspace(0,8,301);d=m.state_feedback(tt)
sol=solve_ivp(lambda t,x:(A-B@k)@x,(0,8),[1,0],t_eval=tt,rtol=1e-11,atol=1e-13)
assert np.max(np.abs(sol.y.T-d['closed']))<1e-10
done('state_transition_crosscheck','Independent adaptive integration matches exact linear matrix-exponential propagation.')
for poles in [(-4.,-5.),(-12.,-15.)]:
    L=m.observer([0],poles)['l'];l1,l2=L.ravel()
    ww=np.logspace(-2,3,60)
    formula=abs((l2*1j*ww-2*l1)/((1j*ww)**2+(l1+.6)*1j*ww+.6*l1+2+l2))
    assert np.max(np.abs(formula-m.observer_noise(ww,poles)))<1e-12
done('observer_noise_transfer','Independent scalar rational expression verifies velocity-estimate noise channel for both pole pairs.')
slow=m.observer_noise([10],(-4,-5))[0];fast=m.observer_noise([10],(-12,-15))[0]
assert fast>slow and np.max(m.observer(np.linspace(0,.3,100),(-12,-15))['norm'])>1
done('observer_noise_and_peaking','Faster example amplifies 10-rad/normalized-time noise more and has initial error peaking; no universal ranking claimed.')
Fcl=np.block([[A-B@k,B@k],[np.zeros((2,2)),A-lo@C]])
assert np.allclose(np.sort(np.linalg.eigvals(Fcl)),[-5,-4,-3,-2])
done('separation_principle_algebra','Explicit triangular closed-loop matrix has the union of feedback and observer poles.')
# 22 CARE is independently solved in closed form for the specified second-order model.
for r in [.1,1,10]:
    p12=r*(-2+np.sqrt(4+1/r))
    p22=r*(-.6+np.sqrt(.36+(2*p12+1)/r))
    p11=.6*p12+2*p22+p12*p22/r
    analytic=np.array([[p11,p12],[p12,p22]])
    d=m.lqr(r)
    assert np.max(np.abs(d['p']-analytic))<1e-12
    assert d['riccati_residual']<1e-12 and np.min(np.linalg.eigvalsh(d['p']))>0
    assert np.max(np.real(d['poles']))<0 and abs(d['independent_cost']-d['cost_from_x0'])<1e-12
done('LQR_closed_form_and_stability','Independent analytic Riccati solution, PSD, residual and Hurwitz checks, plus separate Lyapunov cost identity.')
for r in [.1,1,10]:
    d=m.lqr(r);K=d['k'];P=d['p'];ac=A-B@K
    def cost(t):
        x=expm(ac*t)@np.array([1.,0.]);u=float((-K@x)[0])
        return x@x+r*u*u
    value,error=quad(cost,0,40,epsabs=1e-11,epsrel=1e-11)
    xf=expm(ac*40)@np.array([1.,0.]);tail=xf@P@xf
    assert abs(value+tail-P[0,0])<1e-10
done('LQR_direct_cost_integral','Independent scalar adaptive quadrature plus exact tail verifies total infinite-horizon cost for each weight.')
# 24 Linear and nonlinear Lyapunov examples with exact identities.
ac=A-B@k;P=solve_continuous_lyapunov(ac.T,-np.eye(2))
assert np.min(np.linalg.eigvalsh(P))>0 and np.max(np.abs(ac.T@P+P@ac+np.eye(2)))<1e-12
x0=.7;t=np.linspace(0,10,101);x=x0/np.sqrt(1+2*x0*x0*t)
assert np.all(x>0) and x[-1]<x[0] and np.all(-x**4<0)
done('Lyapunov_identities','SPD linear Lyapunov certificate and exact solution x0/sqrt(1+2*x0^2*t) for x prime=-x^3.')
for h in [.1,.4,.6]:
    d=m.sampled(h)
    assert abs(d['ad']-np.exp(-h))<1e-14 and abs(d['bd']-(1-np.exp(-h)))<1e-14
    held=solve_ivp(lambda t,x:-x-4,(0,h),[1.],rtol=1e-12,atol=1e-14).y[0,-1]
    assert abs(held-d['pole'])<1e-12
    assert (abs(d['pole'])<1)==(h<np.log(5/3))
assert abs(5*np.exp(-np.log(5/3))-4+1)<1e-14
done('ZOH_and_sampling_boundary','Exact integral, API and independent held-input ODE agree; strict stability boundary h=ln(5/3).')
assert abs(np.exp(-5*.6))<1<abs(m.sampled(.6)['pole'])
done('interconnection_order_counterexample','Sampling the continuous closed loop is distinct from digital feedback around a ZOH plant.')
out=dict(status='passed',check_groups=len(checks),checks=checks,scope='Specified normalized teaching models; finite numerical checks complement analytic arguments; professional review pending.')
(ROOT/'docs/research/control-theory-2026-11-02/numerical-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,default=m.serial)+'\n',encoding='utf-8')
print(json.dumps(dict(status='passed',check_groups=len(checks))))
