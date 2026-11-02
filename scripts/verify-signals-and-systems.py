"""Independent numerical checks of specified mathematical teaching examples."""
from pathlib import Path
import sys,json,importlib.util,xml.etree.ElementTree as ET
sys.dont_write_bytecode=True
import numpy as np
from scipy.integrate import quad,solve_ivp
from scipy.linalg import expm
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('m',ROOT/'public/code/signals-and-systems/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def close(a,b,rtol=1e-9,atol=1e-11):
    assert np.allclose(a,b,rtol=rtol,atol=atol),(a,b)
def add(name,**values):checks.append(dict(name=name,status='passed',**values))
# 1 Coordinates and continuous energy scaling, with independent quadrature.
width=.0008
E=quad(lambda t:m.pulse(t,width)**2,-.01,.01,epsabs=1e-13)[0]
E2=quad(lambda t:m.pulse(2*t,width)**2,-.01,.01,epsabs=1e-13)[0]
close(E,width*np.sqrt(np.pi/2),atol=1e-13);close(E2,E/2,atol=1e-13)
close(80/8000,.01);close(80/16000,.005)
add('Signal coordinates, sampling index and continuous energy scaling',energy=E,compressed_energy=E2)
# 2 Superposition and independent time-invariance counterexamples.
t=np.linspace(-.003,.005,501);x=.6*m.pulse(t);z=.6*m.pulse(t-.0004);cl=lambda a:np.clip(a,-.7,.7)
close(2*(x+z),2*x+2*z)
assert np.max(abs(cl(x+z)-cl(x)-cl(z)))>.4
assert np.max(abs((x+z+1)-(x+1)-(z+1)))>.99
delay=.001
assert np.max(abs(t*m.pulse(t-delay)-(t-delay)*m.pulse(t-delay)))>1e-4
add('Linearity versus time invariance, with explicit counterexamples')
# 3 Discrete convolution by Toeplitz columns, FFT, sum and Young bound.
fs,x,h,y=m.echo();A=np.zeros((len(y),len(x)))
for k in range(len(x)):A[k:k+len(h),k]=h
close(y,A@x);close(y,np.fft.ifft(np.fft.fft(x,len(y))*np.fft.fft(h,len(y))).real)
close(y.sum(),x.sum()*h.sum());assert len(y)==256
assert max(abs(y))<=max(abs(x))*sum(abs(h))+1e-12
step=np.cumsum(h);close(np.diff(np.r_[0.,step]),h)
add('Full linear convolution, Toeplitz, FFT, sum and step difference',length=len(y),sum_residual=float(y.sum()-x.sum()*h.sum()))
# 4 Zero state and zero input checked through ODE and impulse quadrature.
tau=.005;tt=np.linspace(0,.03,501)
sol=solve_ivp(lambda _,y:[(1-y[0])/tau],(0,tt[-1]),[.5],t_eval=tt,rtol=1e-11,atol=1e-13)
zs,zi,total=m.initial(tt);err=float(max(abs(sol.y[0]-total)))
assert sol.success and err<1e-10
for q in [.001,.005,.02]:
    step_integral=quad(lambda s:np.exp(-(q-s)/tau)/tau,0,q)[0]
    close(step_integral,m.initial(q)[0])
close(quad(lambda q:np.exp(-q/tau)/tau,0,1)[0],1)
add('Continuous convolution and initial-state ODE',max_error=err)
# 5 Fourier transform of h checked by separate real/imaginary quadrature; transient ODE.
errors=[]
for f in [0.,31.8309886184,100.,200.]:
    w=2*np.pi*f
    numeric=quad(lambda q:np.exp(-q/tau)/tau*np.cos(w*q),0,1,epsabs=1e-11)[0]-1j*quad(lambda q:np.exp(-q/tau)/tau*np.sin(w*q),0,1,epsabs=1e-11)[0]
    errors.append(abs(numeric-m.lowpass(w)))
assert max(errors)<1e-10
w=2*np.pi*100;tt=np.linspace(0,.08,1601);H=m.lowpass(w)
sol=solve_ivp(lambda t,y:[(np.cos(w*t)-y[0])/tau],(0,.08),[0.],t_eval=tt,rtol=1e-12,atol=1e-14)
exact=np.real(H*np.exp(1j*w*tt))-np.real(H)*np.exp(-tt/tau)
assert max(abs(sol.y[0]-exact))<1e-10
dw=.001
for w in [10.,200.,2000.]:
    numeric=-(np.angle(m.lowpass(w+dw))-np.angle(m.lowpass(w-dw)))/(2*dw)
    close(numeric,tau/(1+(w*tau)**2),rtol=1e-7)
close(abs(m.lowpass(1/tau)),1/np.sqrt(2))
add('Frequency response integral, sinusoidal startup and group-delay derivative',max_transform_error=float(max(errors)))
# 6 Square Fourier coefficients via quadrature and Parseval via orthogonal integrals.
for k in [1,3,5,7]:
    coef=2*(quad(lambda t:np.sin(2*np.pi*k*t),0,.5)[0]-quad(lambda t:np.sin(2*np.pi*k*t),.5,1)[0])
    close(coef,4/(np.pi*k))
grid=np.linspace(0,1,20001);s=m.square_series(grid,21)
energy=np.trapezoid(s*s,grid) if hasattr(np,'trapezoid') else np.trapz(s*s,grid)
k=np.arange(1,22,2);close(energy,.5*np.sum((4/(np.pi*k))**2))
assert 1<max(s)<1.3;close(m.square_series(np.array([0.]),21),0)
add('Fourier-series coefficients, partial Parseval energy and jump midpoint',partial_mean_square=float(energy),peak=float(max(s)))
# 7 Continuous Gaussian transform, inversion, modulation and Parseval (dimensionless).
FT=lambda w:np.sqrt(np.pi)*np.exp(-w*w/4)
for w in [0.,1.,3.]:
    val=quad(lambda t:np.exp(-t*t)*np.cos(w*t),-10,10)[0]
    close(val,FT(w))
for t in [0.,.3,1.]:
    val=quad(lambda w:FT(w)*np.cos(w*t)/(2*np.pi),-20,20)[0]
    close(val,np.exp(-t*t))
et=quad(lambda t:np.exp(-2*t*t),-10,10)[0];ef=quad(lambda w:FT(w)**2/(2*np.pi),-20,20)[0];close(et,ef)
wc=2.;w=3.
numeric=quad(lambda t:np.exp(-t*t)*np.cos(wc*t)*np.cos(w*t),-10,10)[0]
close(numeric,(FT(w-wc)+FT(w+wc))/2)
add('Continuous Fourier convention, inversion, Parseval and modulation',parseval_residual=abs(et-ef))
# 8 Direct DFT matrix and finite-sequence DTFT, periodicity, Parseval, zero padding.
x=m.record_sequence()
for N in [32,128]:
    ff=np.arange(N)/N;direct=m.dtft(x,ff);fast=np.fft.fft(x,N)
    close(direct,fast,atol=5e-12)
    close(np.sum(abs(fast)**2)/N,np.sum(abs(x)**2))
close(m.dtft(x,np.array([.1,.2])),m.dtft(x,np.array([1.1,1.2])),atol=1e-12)
close(np.fft.fft(x,128)[::4],np.fft.fft(x,32))
add('DFT matrix, DTFT periodicity, Parseval and unchanged padded-grid values')
# 9 Circular wrapping and sufficient zero padding.
x=np.array([1.,2.,3.]);h=np.array([1.,-.5,.25]);linear=np.convolve(x,h)
circular=np.fft.ifft(np.fft.fft(x,3)*np.fft.fft(h,3)).real
close(circular,[linear[i::3].sum() for i in range(3)])
close(np.fft.ifft(np.fft.fft(x,5)*np.fft.fft(h,5)).real,linear)
add('Linear versus circular convolution and tail wrapping',linear=linear.tolist(),circular=circular.tolist())
# 10 Z series on the two ROCs, and continuous bilateral Laplace integrations.
a=.8
for z in [1.1+.2j,-1.2+.1j]:
    n=np.arange(500);close(np.sum((a/z)**n),1/(1-a/z),atol=1e-11)
for z in [.3+.1j,-.4+.1j]:
    q=np.arange(1,500);close(-np.sum((z/a)**q),1/(1-a/z),atol=1e-11)
assert (a/.5)**50>1 and (1.1/a)**50>1 # terms do not vanish on wrong sides.
s=1.3
close(quad(lambda t:np.exp(-t)*np.exp(-s*t),0,30)[0],1/(s+1))
s=-2.
close(quad(lambda t:-np.exp(-t)*np.exp(-s*t),-40,0)[0],1/(s+1))
add('Same rational expression, two distinct Z/Laplace convergence regions')
# 11 Aliasing and Nyquist endpoint counterexample.
n=np.arange(64);t=n/8000
alias=max(abs(np.cos(2*np.pi*6000*t)-np.cos(2*np.pi*2000*t)))
assert alias<1e-11 and max(abs(np.sin(np.pi*n)))<1e-12
# Nontrivial bandlimited sinc(t/2), cardinal interpolation converges with truncation.
t0=.37;err=[]
for N in [200,400,800]:
    n=np.arange(-N,N+1)
    err.append(abs(np.sum(np.sinc(n/2)*np.sinc(t0-n))-np.sinc(t0/2)))
assert err[-1]<err[0] and err[-1]<1e-6,err
add('Aliased cosine equality, critical-rate sine loss, truncated sinc reconstruction',alias_error=float(alias),sinc_truncation_errors=err)
# 12 Quantizer bound, code count and uniform-error model integral.
xx=np.linspace(-1,1,20001);q=m.quantize(xx)
assert len(np.unique(q))==8 and np.max(abs(q-xx))<=.125+1e-15
variance=quad(lambda e:e*e/.25,-.125,.125)[0];close(variance,.25**2/12)
add('Eight-level quantizer, no-overload error bound and conditional uniform variance',max_error=float(np.max(abs(q-xx))),uniform_variance=variance)
# 13 Independent closed-loop recursion and boundary BIBO example.
for k in [.5,1.,1.05]:
    out=np.zeros(60)
    for i in range(60):out[i]=(1. if i==0 else 0.)-(k*out[i-1] if i else 0.)
    close(out,m.feedback(k))
    close(out,(-k)**np.arange(60))
n=np.arange(100);x=(-1.)**n;y=np.zeros(100)
for i in range(100):y[i]=x[i]-(y[i-1] if i else 0.)
close(y,(-1.)**n*(n+1))
add('Feedback pole, independent recursion and unit-circle BIBO failure')
# 14 Hidden unstable internal mode with stable zero-state external transfer.
A=np.diag([-1.,1.]);B=np.array([1.,0.]);C=np.array([1.,1.])
for w in [0.,.5,2.]:
    close(C@np.linalg.solve(1j*w*np.eye(2)-A,B),1/(1+1j*w))
q=expm(A*3)@np.array([0.,1.]);close(C@q,np.exp(3))
add('Stable transfer can hide unstable unforced internal initial mode')
# 15 Exact ZOH state transition versus augmented matrix exponential; Euler stability.
tau=.005
for Ts in [.001,.006,.012]:
    E=expm(np.array([[-1/tau,1/tau],[0.,0.]])*Ts)
    close(E[0],[np.exp(-Ts/tau),1-np.exp(-Ts/tau)])
assert abs(1-.004/tau)<1 and abs(1-.012/tau)>1
add('Exact zero-order-hold transition, Euler versus physical stability')
# 16 Spectral quotient identity on a finite two-member ensemble, plus correlated-noise bias.
X=np.arange(1,17)+1j*np.arange(16);H=m.lowpass(np.arange(16))
W=np.exp(1j*np.arange(16));Xs=np.stack([X,X]);V=np.stack([W,-W])
Y=H*Xs+V;Sxx=np.mean(Xs*Xs.conj(),axis=0);Syx=np.mean(Y*Xs.conj(),axis=0)
close(Syx/Sxx,H)
Y=H*Xs+.2*Xs;close(np.mean(Y*Xs.conj(),axis=0)/Sxx,H+.2)
add('Finite-ensemble spectral ratio and correlated-output-noise bias; not a WSS proof')
# 17 Assets and source record consistency.
idx=json.loads((ROOT/'docs/research/signals-and-systems-2026-11-02/source-index.json').read_text(encoding='utf-8'))
assert len(idx)==18 and all(r['status']=='fetched' and r.get('sha256') for r in idx)
figs=list((ROOT/'public/figures/signals-and-systems').glob('*.svg'));assert len(figs)==10
for p in figs:assert ET.parse(p).getroot().tag.endswith('svg')
add('All official source records and ten scientific SVGs',sources=len(idx),figures=len(figs))
out=dict(scope='Specified mathematical examples and implementations; no external expert review, general theorem proof, physiological or device validation.',passed=True,total_check_groups=len(checks),checks=checks)
(ROOT/'docs/research/signals-and-systems-2026-11-02/numerical-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=True,indent=2))
