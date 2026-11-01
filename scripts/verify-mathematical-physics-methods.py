"""Independent mathematical and numerical checks; does not certify real hardware."""
from pathlib import Path
import importlib.util,sys,json
sys.dont_write_bytecode=True
import numpy as np
from math import factorial
from scipy.integrate import quad,solve_ivp
from scipy.special import jv,jvp,jn_zeros,jnp_zeros,eval_legendre
from scipy.optimize import brentq,minimize_scalar
from scipy.linalg import eigh
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
REC=ROOT/'docs/research/mathematical-physics-methods-2026-11-02'
spec=importlib.util.spec_from_file_location('models',ROOT/'public/code/mathematical-physics-methods/experiments.py')
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
checks=[]
def check(name,ok,detail=None):
    checks.append(dict(name=name,passed=bool(ok),detail=detail))
def close(name,a,b,atol=1e-10,rtol=1e-7):
    err=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    check(name,np.allclose(a,b,atol=atol,rtol=rtol),dict(max_abs_error=err))
# Endpoint conditions and exact eigenfunction identities.
for n in range(1,6):
    k=n*np.pi
    close(f'Dirichlet endpoints n={n}',[np.sin(0),np.sin(k)],[0,0])
    close(f'Neumann derivative endpoints n={n}',[0,-k*np.sin(k)],[0,0])
    close(f'mixed right derivative n={n}',np.cos((n-.5)*np.pi),0)
    for m in range(1,n+1):
        val=quad(lambda x:2*np.sin(n*np.pi*x)*np.sin(m*np.pi*x),0,1,epsabs=1e-12)[0]
        close(f'sine Gram n={n},m={m}',val,float(n==m))
close('Neumann zero-mode derivative',0,0)
# Weighted self-adjoint example: p=w=exp(x), X=exp(-x/2) sin(n*pi*x).
for n in range(1,4):
    for m in range(1,n+1):
        val=quad(lambda x:np.exp(x)*(np.exp(-x/2)*np.sin(n*np.pi*x))*(np.exp(-x/2)*np.sin(m*np.pi*x)),0,1,epsabs=1e-12)[0]
        close(f'weighted Sturm-Liouville Gram n={n},m={m}',val,.5 if n==m else 0)
# Pluck coefficients, errors, Parseval derivative energy.
a=.3;A=.001
for n in range(1,21):
    numeric=2*quad(lambda x:model.pluck_shape(x)*np.sin(n*np.pi*x),0,1,points=[a],epsabs=1e-14)[0]
    close(f'pluck coefficient by independent quadrature n={n}',model.pluck_coeff(n),numeric,atol=1e-12)
ns=np.arange(1,1001);bs=model.pluck_coeff(ns)
energy_derivative=.5*A*A*(1/a+1/(1-a))
close('pluck strain energy via derivative Parseval',np.sum((ns*np.pi*bs)**2)/4,energy_derivative,atol=0,rtol=.001)
errors=[]
grid=np.linspace(0,1,10001);shape=model.pluck_shape(grid)
for N in [3,10,50,100]:
    n=np.arange(1,N+1)
    rec=np.sum(model.pluck_coeff(n)[:,None]*np.sin(n[:,None]*np.pi*grid),axis=0)
    err=np.trapz((rec-shape)**2,grid);errors.append(err)
check('pluck L2 truncation error decreases',np.all(np.diff(errors)<0),errors)
close('pluck fundamental frequency',100/(2*1),50)
# Heat/wave independent ODE solutions in modal coordinates and energy.
tt=np.linspace(0,1,71);omega=np.array([np.pi,3*np.pi])
sol=solve_ivp(lambda t,y:np.r_[y[2:],-omega**2*y[:2]],[0,1],[1,.4,0,0],t_eval=tt,rtol=1e-11,atol=1e-12)
analytic=np.array([np.cos(np.pi*tt),.4*np.cos(3*np.pi*tt)])
close('wave modal ODE versus cosine solution',sol.y[:2],analytic,atol=1e-9)
energy=(np.sum(sol.y[2:]**2+omega[:,None]**2*sol.y[:2]**2,axis=0))/4
close('wave modal kinetic plus potential energy conserved',energy,energy[0],atol=1e-8)
heat=solve_ivp(lambda t,y:-.1*omega**2*y,[0,1],[1,.4],t_eval=tt,rtol=1e-11,atol=1e-12)
close('heat modal ODE versus exponential',heat.y,np.array([np.exp(-.1*np.pi**2*tt),.4*np.exp(-.9*np.pi**2*tt)]),atol=1e-10)
check('heat L2 energy monotone',np.all(np.diff(np.sum(heat.y**2,axis=0))<0))
close('heat attenuation at t=.2',np.exp(-.1*omega**2*.2),[.8208687174155399,.16922454248244995])
for x in [.2,.6]:
    for t in [.123,.34]:
        dx=1e-4;dt=1e-4
        h,w=model.heat_wave(x,t)
        hp,wp=model.heat_wave(x+dx,t);hm,wm=model.heat_wave(x-dx,t)
        ht,wt=model.heat_wave(x,t+dt);hb,wb=model.heat_wave(x,t-dt)
        close(f'heat PDE finite residual x={x},t={t}',(ht-hb)/(2*dt),.1*(hp-2*h+hm)/dx**2,atol=2e-6)
        close(f'wave PDE finite residual x={x},t={t}',(wt-2*w+wb)/dt**2,(wp-2*w+wm)/dx**2,atol=3e-6)
# d'Alembert, initial displacement/velocity for two independently evaluated expressions.
f=lambda x:np.exp(-x*x)
g=lambda x:x*np.exp(-x*x)
for x in [-.4,0,.8]:
    c=2.;eps=1e-5
    def dA(t):return .5*(f(x-c*t)+f(x+c*t))+quad(g,x-c*t,x+c*t,epsabs=1e-13)[0]/(2*c)
    close(f'dAlembert displacement x={x}',dA(0),f(x))
    close(f'dAlembert velocity x={x}',(dA(eps)-dA(-eps))/(2*eps),g(x),atol=1e-9)
# Resonance maxima against independent optimizer and singular projection logic.
for z in [.03,.2,.6]:
    opt=minimize_scalar(lambda r:-1/np.sqrt((1-r*r)**2+4*z*z*r*r),bounds=(0,2),method='bounded',options={'xatol':1e-12})
    close(f'damped response peak zeta={z}',opt.x,np.sqrt(1-2*z*z),atol=2e-7)
r=np.linspace(0,2,1001)
check('high damping .8 has no positive-frequency magnitude peak',np.argmax(abs(1/(1-r*r+1.6j*r)))==0)
# Radiating Green kernel: radial Helmholtz residual and outgoing phase derivative.
k=3.;rad=.7;dr=1e-5
G=lambda r:np.exp(-1j*k*r)/(4*np.pi*r)
first=(G(rad+dr)-G(rad-dr))/(2*dr);second=(G(rad+dr)-2*G(rad)+G(rad-dr))/dr**2
close('outgoing radial kernel Helmholtz equation',second+2/rad*first+k*k*G(rad),0,atol=2e-6)
for R in [2.,10.,50.]:
    # exact r*(dG/dr + ikG) = -G; approaches zero for exp(+iwt) convention.
    close(f'radiation derivative identity r={R}',R*((-1j*k-1/R)*G(R)+1j*k*G(R)),-G(R))
# Bessel roots by independent bracketed solver, ODE, weighted inner products.
for m in range(4):
    for z in [0.,.2,1.4,4.]:
        series=sum((-1)**k*(z/2)**(2*k+m)/(factorial(k)*factorial(k+m)) for k in range(45))
        close(f'Bessel defining power series m={m},z={z}',series,jv(m,z),atol=2e-14)
for m in range(3):
    roots=jn_zeros(m,2)
    for n,root in enumerate(roots,1):
        other=brentq(lambda z:jv(m,z),root-.2,root+.2,xtol=1e-13)
        close(f'Bessel root independent solver m={m},n={n}',other,root)
        close(f'membrane edge m={m},n={n}',jv(m,root),0)
        z=root*.61
        close(f'Bessel differential equation m={m},n={n}',z*z*jvp(m,z,2)+z*jvp(m,z)+(z*z-m*m)*jv(m,z),0,atol=1e-11)
    for i in range(2):
        for j in range(i+1):
            val=quad(lambda r:r*jv(m,roots[i]*r)*jv(m,roots[j]*r),0,1,epsabs=1e-13)[0]
            exact=.5*jv(m+1,roots[i])**2 if i==j else 0
            close(f'Bessel weighted Gram m={m},i={i},j={j}',val,exact,atol=1e-12)
close('J0 first two quoted membrane frequencies',20*jn_zeros(0,2)/(2*np.pi*.1),[76.54797495620123,175.70954350108698])
close('rigid tube J0 derivative zero-mode',jvp(0,0),0)
close('first positive rigid axisymmetric derivative zero',jnp_zeros(0,1)[0],3.8317059702075125)
for ell in range(5):
    poly=np.polynomial.Legendre.basis(ell);z=np.linspace(-.9,.9,71)
    close(f'Legendre differential equation ell={ell}',(1-z*z)*poly.deriv(2)(z)-2*z*poly.deriv()(z)+ell*(ell+1)*poly(z),0,atol=1e-12)
    for m in range(ell+1):
        val=quad(lambda z:eval_legendre(ell,z)*eval_legendre(m,z),-1,1,epsabs=1e-12)[0]
        close(f'Legendre orthogonality ell={ell},s={m}',val,2/(2*ell+1) if ell==m else 0)
    # m=0 normalized spherical harmonic norm including azimuth.
    norm=2*np.pi*(2*ell+1)/(4*np.pi)*quad(lambda th:eval_legendre(ell,np.cos(th))**2*np.sin(th),0,np.pi)[0]
    close(f'spherical m0 angular norm ell={ell}',norm,1)
# Heat kernel Gaussian moments, convolution, Fourier factor and semigroup.
for t in [.05,.2,.5]:
    mass=quad(lambda x:model.gaussian(x,t),-np.inf,np.inf,epsabs=1e-11)[0]
    var=quad(lambda x:x*x*model.gaussian(x,t),-np.inf,np.inf,epsabs=1e-11)[0]
    close(f'Gaussian conserved mass t={t}',mass,1)
    close(f'Gaussian variance t={t}',var,.01+.2*t)
    for x in [0,.25]:
        kernel=lambda s:np.exp(-s*s/(.4*t))/np.sqrt(.4*np.pi*t)
        conv=quad(lambda xi:kernel(x-xi)*model.gaussian(xi,0),-np.inf,np.inf,epsabs=1e-11)[0]
        close(f'heat convolution Gaussian x={x},t={t}',conv,model.gaussian(x,t))
for k in [0,1,5]:
    t=.2
    ft=quad(lambda x:np.exp(-x*x/(.4*t))/np.sqrt(.4*np.pi*t)*np.cos(k*x),-np.inf,np.inf,epsabs=1e-11)[0]
    close(f'heat kernel Fourier multiplier k={k}',ft,np.exp(-.1*k*k*t))
# Green boundaries, reciprocity, jump, volume and weak identity.
for L in [1.,2.5]:
    for xi in [.2*L,.5*L,.8*L]:
        close(f'Green boundaries L={L},xi={xi}',[model.green(0,xi,L),model.green(L,xi,L)],[0,0])
        e=1e-6*L
        slopeR=(model.green(xi+e,xi,L)-model.green(xi,xi,L))/e
        slopeL=(model.green(xi,xi,L)-model.green(xi-e,xi,L))/e
        close(f'Green jump L={L},xi={xi}',slopeR-slopeL,-1,atol=1e-9)
        for x in [.1*L,.65*L]:
            close(f'Green reciprocity L={L},x={x},xi={xi}',model.green(x,xi,L),model.green(xi,x,L))
for x in np.linspace(0,1,9):
    constant=quad(lambda xi:model.green(x,xi),0,1,points=[x],epsabs=1e-12)[0]
    sine=quad(lambda xi:model.green(x,xi)*np.sin(np.pi*xi),0,1,points=[x],epsabs=1e-12)[0]
    close(f'Green constant forcing x={x}',constant,x*(1-x)/2)
    close(f'Green sine forcing x={x}',sine,np.sin(np.pi*x)/np.pi**2)
for xi in [.2,.4,.8]:
    weak=quad(lambda x:(1-xi)*(1-2*x),0,xi)[0]+quad(lambda x:-xi*(1-2*x),xi,1)[0]
    close(f'Green weak identity test x(1-x) xi={xi}',weak,xi*(1-xi))
# Neumann solvability on u=x^2: f=-2, outward derivatives 0,2.
close('Neumann source-boundary compatibility sign',-2,-(0+2))
# Laplace initial terms: q=a cos wt + b sin wt, direct numerical Laplace integral.
a,b,w,s=.7,-.2,3.,2.
trans=quad(lambda t:np.exp(-s*t)*(a*np.cos(w*t)+b*np.sin(w*t)),0,np.inf,epsabs=1e-11)[0]
close('Laplace modal initial displacement and velocity',trans,(s*a+b*w)/(s*s+w*w))
# Variational quotient and matrix spectra, independent exact discrete formula.
num=quad(lambda x:(1-2*x)**2,0,1)[0];den=quad(lambda x:x*x*(1-x)**2,0,1)[0]
close('Rayleigh polynomial trial quotient',num/den,10.)
check('Rayleigh trial is first eigenvalue upper bound',num/den>np.pi**2)
for M in [10,20,40,80]:
    h=1/M;K=(2*np.eye(M-1)-np.eye(M-1,k=1)-np.eye(M-1,k=-1))/h**2
    vals=np.linalg.eigvalsh(K)
    exact=4/h**2*np.sin(np.arange(1,M)*np.pi/(2*M))**2
    close(f'discrete matrix spectrum M={M}',vals,exact,atol=1e-9)
    solution=np.linalg.solve(K,np.ones(M-1));x=np.arange(1,M)*h
    close(f'discrete Poisson versus analytic parabola M={M}',solution,x*(1-x)/2)
errors=[abs(model.fd_first(M)-np.pi**2) for M in [20,40,80]]
check('first eigenvalue errors converge at order two',np.all((np.array(errors[:-1])/errors[1:]>3.9)&(np.array(errors[:-1])/errors[1:]<4.1)))
# Amplification analysis independent from time recurrence.
theta=np.linspace(0,np.pi,1001)
for r in [.1,.49,.5,.6]:
    amplification=1-4*r*np.sin(theta/2)**2
    check(f'heat amplification r={r}',np.max(abs(amplification))<=1+1e-12 if r<=.5 else np.max(abs(amplification))>1+1e-3)
for nu in [.3,.7,1.,1.1]:
    z=1-2*nu*nu*np.sin(theta/2)**2
    roots=np.array([np.roots([1,-2*zz,1]) for zz in z])
    radius=np.max(abs(roots))
    check(f'wave recurrence amplification nu={nu}',radius<=1+2e-7 if nu<=1 else radius>1.1,dict(spectral_radius=float(radius)))
for nu in [.3,.7,1.]:
    kh=np.linspace(.01,np.pi,100)
    omegaDt=2*np.arcsin(nu*np.sin(kh/2))
    close(f'discrete wave dispersion recurrence nu={nu}',np.cos(omegaDt),1-2*nu*nu*np.sin(kh/2)**2)
    if nu==1:close('nu=1 special constant-grid phase speed',omegaDt,kh)
# Source retrieval and XML media assets.
sources=json.loads((REC/'source-index.json').read_text(encoding='utf-8'))
check('20 primary/official sources retrieved',len(sources)==20 and all(x['status']=='fetched' for x in sources))
for path in sorted((ROOT/'public/figures/mathematical-physics-methods').glob('*.svg')):
    try:ET.parse(path);ok=True
    except ET.ParseError:ok=False
    check('SVG XML '+path.name,ok)
check('10 teaching figures present',len(list((ROOT/'public/figures/mathematical-physics-methods').glob('*.svg')))==10)
ET.parse(ROOT/'public/figures/foundation-courses/mathematical-physics-methods.svg')
check('course thumbnail SVG valid',True)
result=dict(scope='Independent equations/quadrature/ODEs/roots/energy/spectra and media checks for specified ideal models, not professional review or device measurement.',total=len(checks),passed=sum(c['passed'] for c in checks),checks=checks)
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for c in checks:
    if not c['passed']:print('FAIL',c)
print(json.dumps(dict(total=result['total'],passed=result['passed'])))
if result['passed']!=result['total']:raise SystemExit(1)
