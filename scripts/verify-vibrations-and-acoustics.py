"""Independent mechanics/acoustics identities, quadrature, eigenvalue and asset audit."""
from pathlib import Path
import importlib.util,sys,json,hashlib,xml.etree.ElementTree as ET
sys.dont_write_bytecode=True
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from scipy.linalg import expm
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/vibrations-and-acoustics-2026-11-02';spec=importlib.util.spec_from_file_location('va',ROOT/'public/code/vibrations-and-acoustics/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def check(name,condition,**evidence):
    assert condition,(name,evidence);checks.append(dict(name=name,passed=True,**evidence))
mass,k,wn=m.MASS,m.STIFFNESS,m.OMEGA_N
zeta=.3;b=2*zeta*mass*wn;t,q,v,E=m.free_vibration(zeta,t=np.linspace(0,.6,301));wd=wn*np.sqrt(1-zeta*zeta)
exact=.001*np.exp(-zeta*wn*t)*(np.cos(wd*t)+zeta/np.sqrt(1-zeta*zeta)*np.sin(wd*t))
check('Underdamped exact initial-value response versus solver',np.max(abs(q-exact))<1e-11)
t,q,v,E=m.free_vibration(1.);exact=.001*(1+wn*t)*np.exp(-wn*t)
check('Critical-damping exact response',np.max(abs(q-exact))<1e-11)
for zeta in [.05,.3,1.,1.5]:
    t,q,v,E=m.free_vibration(zeta,t=np.linspace(0,.6,31));b=2*zeta*mass*wn;A=np.array([[0,1],[-k/mass,-b/mass]])
    exact=np.array([expm(A*s)@np.array([.001,0]) for s in t]);assert np.max(abs(exact[:,0]-q))<1e-11 and np.max(np.diff(E))<1e-12
check('Four damping regimes agree with independent matrix exponentials and nonincreasing energy',True)
zeta=.3;b=2*zeta*mass*wn;A=np.array([[0,1],[-k/mass,-b/mass]]);tf=.4;initial=np.array([.001,0]);end=expm(A*tf)@initial
dissipated=quad(lambda t:b*(expm(A*t)@initial)[1]**2,0,tf,epsabs=1e-13)[0];E0=.5*k*.001**2;Ef=.5*k*end[0]**2+.5*mass*end[1]**2
check('Integrated damping loss matches mechanical energy decrease',abs(E0-Ef-dissipated)<1e-12)
omega=np.linspace(1,200,300);H=m.mechanical_response(omega,.2);b=.4*mass*wn
check('Mechanical compliance satisfies dynamic stiffness equation',np.max(abs((k-mass*omega**2+1j*b*omega)*H-1))<1e-12)
opt=minimize_scalar(lambda r:-abs(m.mechanical_response(r*wn,.2)),bounds=(.2,1.4),method='bounded',options={'xatol':1e-12})
check('Constant-force displacement peak matches conditional formula',abs(opt.x-np.sqrt(1-2*.2**2))<1e-7,frequency_ratio=opt.x)
r=np.linspace(.001,3,5001);amp=abs(m.mechanical_response(r*wn,.8))
check('High-damping displacement response has no nonzero-frequency peak',np.all(np.diff(amp)<0))
opt=minimize_scalar(lambda r:-abs(1j*r*wn*m.mechanical_response(r*wn,.3)),bounds=(.2,2),method='bounded',options={'xatol':1e-12})
check('Velocity peak is at natural frequency for constant-force viscous model',abs(opt.x-1)<1e-7)
for zeta in [.05,.3,1.5]:
    wpm=wn*np.array([np.sqrt(1+zeta*zeta)-zeta,np.sqrt(1+zeta*zeta)+zeta]);b=2*zeta*mass*wn
    power=abs(1j*wpm*m.mechanical_response(wpm,zeta))**2
    assert np.allclose(power,.5/b**2) and np.isclose(wpm[1]-wpm[0],2*zeta*wn)
check('Exact velocity half-power roots and Q bandwidth identity',True)
omega=1.2*wn;zeta=.2;b=2*zeta*mass*wn;F=.003;Q=m.mechanical_response(omega,zeta)*F;V=1j*omega*Q;T=2*np.pi/omega
avg=quad(lambda t:F*np.cos(omega*t)*np.real(V*np.exp(1j*omega*t)),0,T)[0]/T
check('Average force-velocity input equals viscous loss',abs(avg-.5*b*abs(V)**2)<1e-12)
M,K,C,values,phi=m.modal_model()
check('Generalized eigenvalues and analytic two-mode frequencies',np.allclose(values,[4000,9000]) and np.allclose(K@phi,(M@phi)*values),frequencies_Hz=(np.sqrt(values)/(2*np.pi)).tolist())
check('Mass orthogonality and diagonal modal stiffness',np.allclose(phi.T@M@phi,np.eye(2)) and np.allclose(phi.T@K@phi,np.diag(values)))
check('Specified proportional damping diagonalizes with modes',np.allclose(phi.T@C@phi,np.diag(1+.0005*values)))
direct,modal=m.modal_response(np.linspace(5,22,701));error=float(np.max(abs(direct-modal)))
check('Direct dynamic-stiffness response equals modal synthesis',error<1e-12,max_difference_m_per_N=error)
area=.003;Za=8+3j;V=.02-.01j;Qv=area*V;P=Za*Qv;F=area*P
check('Ideal uniform-piston area-squared impedance and power mapping',np.allclose(F/V,area**2*Za) and np.isclose(.5*np.real(F*np.conj(V)),.5*np.real(P*np.conj(Qv))))
x=.123;h=1e-6;f=500.;omega=2*np.pi*f;kac=omega/m.C;R=.3+.2j;p,u=m.plane_fields(x,R)
dp=(m.plane_fields(x+h,R)[0]-m.plane_fields(x-h,R)[0])/(2*h);du=(m.plane_fields(x+h,R)[1]-m.plane_fields(x-h,R)[1])/(2*h)
check('Double-wave phasors satisfy Euler and continuity with fixed exp(iwt) signs',abs(1j*omega*m.RHO*u+dp)<1e-7 and abs(1j*omega*p+m.RHO*m.C**2*du)<1e-5)
T=1/f;mean=quad(lambda t:np.cos(omega*t)**2,0,T)[0]/T;compound=quad(lambda t:(np.cos(omega*t)+.3*np.cos(3*omega*t))**2,0,T)[0]/T
check('Sinusoidal peak-to-RMS ratio is not a universal composite-wave ratio',abs(mean-.5)<1e-12 and abs(compound-.545)<1e-12 and abs(1.3/np.sqrt(compound)-np.sqrt(2))>.1)
p,u=m.plane_fields(.14,.5+.2j);avg=quad(lambda t:np.real(p*np.exp(1j*omega*t))*np.real(u*np.exp(1j*omega*t)),0,T)[0]/T
check('Time-domain pressure-velocity average matches peak-phasor intensity',abs(avg-m.active_intensity(p,u))<1e-12)
x=np.linspace(0,m.C/f,1001);p,u=m.plane_fields(x,1);energy=abs(p)**2/(4*m.RHO*m.C**2)+m.RHO*abs(u)**2/4
check('Pure standing wave stores energy with zero net active intensity',np.max(abs(m.active_intensity(p,u)))<1e-14 and np.allclose(energy,2/(m.RHO*m.C**2)))
p,u=m.plane_fields(x,.6)
check('Partially reflected field has constant net flux but nonconstant pressure squared',np.allclose(m.active_intensity(p,u),.64/m.Z0) and np.ptp(abs(p)**2/(2*m.Z0))>.001)
ratios=np.geomspace(.001,1000,101);rp,tp,ref,trans=m.interface(1.,ratios)
check('Lossless normal-incidence energy conservation over impedance range',np.allclose(ref+trans,1) and np.all((trans>=0)&(trans<=1)))
check('Interface pressure and signed normal velocity continuity',np.allclose(1+rp,tp) and np.allclose(1-rp,tp/ratios))
rp,tp,ref,trans=m.interface(m.Z0,3*m.Z0)
check('Pressure transmission greater than one with passive power balance',np.allclose([rp,tp,ref,trans],[.5,1.5,.25,.75]))
lp=20*np.log10(1/20e-6);li=10*np.log10(1/m.Z0/1e-12)
check('SPL and intensity level differ for stated air impedance',abs(lp-93.97940008672037)<1e-10 and abs(li-93.85524633909604)<1e-10 and not np.isclose(lp,li),SPL_dB=lp,intensity_level_dB=li)
check('Two 70 dB cases and ideal point cancellation',abs(m.combined_spl(70,70)-73.01029995663981)<1e-10 and abs(m.combined_spl(70,70,1)-76.02059991327963)<1e-10 and np.isneginf(m.combined_spl(70,70,-1)))
phase=.7;mean=quad(lambda t:(np.cos(omega*t)+np.cos(omega*t+phase))**2,0,T)[0]/T
check('Coherent pressure sum includes expected cross term',abs(mean-(1+np.cos(phase)))<1e-10)
r=.2;h=1e-6;p,u=m.spherical_fields(r);dp=(m.spherical_fields(r+h)[0]-m.spherical_fields(r-h)[0])/(2*h)
check('Spherical radial velocity from independent pressure derivative',abs(u+dp/(1j*omega*m.RHO))<1e-9)
r=np.geomspace(.01,10,501);p,u=m.spherical_fields(r);I=m.active_intensity(p,u)
check('Pure outgoing spherical active intensity identity holds even at small kr',np.allclose(I,abs(p)**2/(2*m.Z0),rtol=1e-12))
complex_I=.5*p*np.conj(u);kac=omega/m.C
check('Spherical reactive-to-active ratio and local impedance sign convention',np.allclose(complex_I.imag/complex_I.real,1/(kac*r)) and np.all((p/u).imag>0))
power=4*np.pi*r*r*I
check('Spherical power conservation and distance-doubling level difference',np.allclose(power,power[0]) and abs(-20*np.log10(2)+6.020599913279624)<1e-12)
L=.5
for n in [1,2,3]:
    kop=n*np.pi/L;kcl=(2*n-1)*np.pi/(2*L)
    assert abs(np.sin(kop*L))<1e-12 and abs(np.cos(kcl*L))<1e-12
check('Ideal open-open and closed-open pressure boundary frequencies',np.isclose(m.C/(2*L),343) and np.isclose(m.C/(4*L),171.5))
area=.002;zchar=m.Z0/area;kL=np.array([.2,.7,1.2,2.]);Rrigid=np.exp(-2j*kL);Ropen=-Rrigid
zrigid=zchar*(1+Rrigid)/(1-Rrigid);zopen=zchar*(1+Ropen)/(1-Ropen)
check('Tube input impedances from independent forward-backward wave ratio',np.allclose(zrigid,-1j*zchar/np.tan(kL)) and np.allclose(zopen,1j*zchar*np.tan(kL)))
small=.001
check('Tube low-frequency compliance and inertance limits',abs((1/np.tan(small))/(1/small)-1)<1e-6 and abs(np.tan(small)/small-1)<1e-6)
h=m.resonator();S,V,le=h['area_m2'],h['volume_m3'],h['effective_length_m'];plug_mass=m.RHO*S*le;spring=m.RHO*m.C**2*S*S/V
check('Helmholtz port model agrees with independent physical plug mass and spring',abs(np.sqrt(spring/plug_mass)/(2*np.pi)-h['frequency_Hz'])<1e-10,frequency_Hz=h['frequency_Hz'])
fs,h,ff,HH=m.echo_model();spectrum=np.fft.rfft(h,n=48000);freq=np.fft.rfftfreq(48000,1/fs);idx=np.arange(2001)
check('Two-tap DTFT equals independently evaluated FFT bins',np.allclose(spectrum[idx],1+.6*np.exp(-2j*np.pi*freq[idx]*.004)))
check('Echo extrema and comb spacing',np.isclose(20*np.log10(abs(1+.6)),4.082399653118496) and np.isclose(20*np.log10(abs(1-.6)),-7.958800173440752) and np.isclose(1/.004,250))
source=json.loads((REC/'source-index.json').read_text(encoding='utf-8'))
for row in source:
    assert row['status']=='fetched';path=ROOT/'artifacts/vibrations-and-acoustics/sources'/(row['id']+('.pdf' if row['pdf'] else '.html'));assert hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256']
check('Eighteen author/official source cache hashes match records',len(source)==18)
files=list((ROOT/'public/figures/vibrations-and-acoustics').glob('*.svg'))+[ROOT/'public/figures/foundation-courses/vibrations-and-acoustics.svg']
for file in files:ET.parse(file);assert '<script' not in file.read_text(encoding='utf-8')
check('Eleven original SVG assets parse without executable script',len(files)==11)
result=dict(slug='vibrations-and-acoustics',check_groups=len(checks),checks=checks,professional_review='pending')
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(check_groups=len(checks),passed=len(checks))))
