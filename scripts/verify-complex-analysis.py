"""Independent analytic counterexamples, numerical quadrature, recurrence and PCM checks."""
from pathlib import Path
import json
import wave
import xml.etree.ElementTree as ET
import numpy as np
from scipy import signal,integrate,optimize

ROOT=Path(__file__).resolve().parents[1]
REC=ROOT/'docs/research/complex-analysis-2026-11-02'
d=json.loads((REC/'calculations.json').read_text(encoding='utf-8'))
checks=[]
def near(name,actual,expected,atol=1e-10):
    np.testing.assert_allclose(actual,expected,atol=atol,rtol=0)
    checks.append(name)

# Time-domain product over an exact complete cycle, independent of complex-product formula.
angle=2*np.pi*np.arange(16384)/16384
p=.02*np.cos(angle)
velocity=1e-4*np.cos(angle-np.pi/3)
near('pressure-velocity periodic mean versus complex intensity',np.mean(p*velocity),d['specific_impedance']['mean_intensity_W_per_m2'],1e-17)
near('impedance components',[d['specific_impedance']['real_Pa_s_per_m'],d['specific_impedance']['imag_Pa_s_per_m']],[100,100*np.sqrt(3)])
near('peak versus RMS',np.sqrt(np.mean(p*p)),.02/np.sqrt(2))
near('phasor Cartesian coordinates',[.02*np.cos(np.pi/3),.02*np.sin(np.pi/3)],[d['phasor']['real_Pa'],d['phasor']['imag_Pa']])
for phase,target in zip([0,2*np.pi/3,np.pi],[.4,.2,0]):
    # Fourier sine/cosine coefficients rather than modulus of a phasor sum.
    values=.2*np.cos(angle)+.2*np.cos(angle+phase)
    c=2*np.mean(values*np.cos(angle));s=2*np.mean(values*np.sin(angle))
    near('coherent tone amplitude '+str(phase),np.hypot(c,s),target)

# All-path identities and a single-point CR counterexample.
h=np.array([.01,.01j,.01*(1+1j),-.003+.007j])
z0=1+1j
near('square difference quotient identity',((z0+h)**2-z0**2)/h,2*z0+h)
near('conjugate directional derivatives',np.conj(h[:2])/h[:2],[1,-1])
near('modulus squared all-path derivative at origin',abs(h)**2/h,np.conj(h))
# f(z)=conj(z)^2/z, f(0)=0: CR holds from the axes, diagonal limit differs.
counter=lambda z:np.conj(z)**2/z
near('single-point CR does not suffice without real differentiability',counter(h[:3])/h[:3],[1,1,-1])
z1=np.exp(3j*np.pi/4)
near('principal logarithm branch discrepancy',2*np.log(z1)-np.log(z1*z1),2j*np.pi)
fgrid=np.arange(0,2001)
wrapped=np.exp(-2j*np.pi*fgrid*.003)
near('delay unwrapped phase',np.unwrap(np.angle(wrapped)),-2*np.pi*fgrid*.003,1e-11)
near('sampled delay ambiguity',np.exp(-2j*np.pi*fgrid*(.003+1)),wrapped,1e-10)

z=np.exp(1j*angle)
near('unit-circle integral of z',2*np.pi*np.mean(z*1j*z),0)
near('unit-circle integral of reciprocal',2*np.pi*np.mean((1/z)*1j*z),2j*np.pi)
near('Cauchy formula sample',2*np.pi*np.mean(z*z/(z-.5)*1j*z),.5j*np.pi)
for pole,expected,record in zip([.5,1.5],[2j*np.pi,0],d['contours']):
    integral=2*np.pi*np.mean(1/(z-pole)*1j*z)
    near('circle pole inside or outside '+str(pole),integral,expected)
    near('generated contour record '+str(pole),record,[integral.real,integral.imag])
near('clockwise contour sign',2*np.pi*np.mean(1/np.conj(z)*(-1j*np.conj(z))),-2j*np.pi)

a=.8
near('finite geometric sum and exact tail',[sum(a**n for n in range(8)),5-sum(a**n for n in range(8))],
     [d['series']['at_z_1_partial_sum'],d['series']['at_z_1_absolute_tail']])
near('internal expansion at z=0.4',-sum((.4/a)**k for k in range(1,60)),.4/(.4-a))
for radius in [1.2,.4]:
    circle=radius*z
    H=circle/(circle-a)
    ns=range(-3,7)
    got=[np.mean(H*circle**n) for n in ns]
    expected=[a**n if n>=0 else 0 for n in ns] if radius>a else [-a**n if n<0 else 0 for n in ns]
    near('inverse-Z including negative indices R='+str(radius),got,expected)
assert abs(sum((a/.6)**n for n in range(16))-.6/(.6-a))>abs(sum((a/.6)**n for n in range(8))-.6/(.6-a))
checks.append('outside ROC increasing outer-series terms diverge')

fs=16000;theta0=np.pi/8
for row in d['resonators']:
    r=row['r'];den=[1,-2*r*np.cos(theta0),r*r]
    poles=np.roots(den)
    near('conjugate pole modulus r='+str(r),np.abs(poles),[r,r])
    n=np.arange(16384);impulse=np.zeros(len(n));impulse[0]=1
    manual=np.zeros(len(n))
    for k in range(len(n)):
        manual[k]=impulse[k]
        if k>=1:manual[k]-=den[1]*manual[k-1]
        if k>=2:manual[k]-=den[2]*manual[k-2]
    analytic=r**n*np.sin((n+1)*theta0)/np.sin(theta0)
    near('manual impulse versus analytic r='+str(r),manual,analytic,2e-11)
    near('lfilter versus manual recurrence r='+str(r),signal.lfilter([1],den,impulse),manual,2e-11)
    frequencies=np.array([600.,1000.,1400.])
    _,H=signal.freqz([1],den,worN=frequencies,fs=fs)
    # Independent Fourier sum of 16384 known samples; the remaining tail is bounded.
    direct=np.exp(-2j*np.pi*np.outer(frequencies,n)/fs)@analytic
    tail_bound=r**len(n)/((1-r)*abs(np.sin(theta0)))
    near('freqz versus impulse Fourier sum r='+str(r),H,direct,tail_bound+1e-9)
    def magnitude(f):
        q=np.exp(-2j*np.pi*f/fs)
        return abs(1/(1+den[1]*q+den[2]*q*q))
    peak=optimize.minimize_scalar(lambda f:-magnitude(f),bounds=(600,1400),method='bounded',options={'xatol':1e-8}).x
    near('peak by independent scalar optimization r='+str(r),peak,row['peak_Hz'],.001)
    near('decay time constant r='+str(r),r**(row['time_constant_ms']*fs/1000),np.exp(-1))

wc=2*np.pi*1000
s=wc*(-.5+.3j)
real=integrate.quad(lambda u:np.real(np.exp(-(1+s/wc)*u)),0,np.inf)[0]
imag=integrate.quad(lambda u:np.imag(np.exp(-(1+s/wc)*u)),0,np.inf)[0]
near('continuous Laplace integral',real+1j*imag,wc/(s+wc))
near('analog cutoff magnitude and phase',[abs(1/(1+1j)),np.angle(1/(1+1j))],[d['analog_lowpass']['gain_at_fc'],d['analog_lowpass']['phase_at_fc_rad']])
area=integrate.quad(lambda u:1/(1+u*u),0,np.inf)[0]
near('real-axis lowpass area versus residue',area,np.pi/2)
near('Hz versus angular-frequency area',1000*area,d['analog_lowpass']['one_sided_square_response_area_Hz'])
near('area below three-dB frequency',integrate.quad(lambda u:1/(1+u*u),0,1)[0],np.pi/4)

time=np.arange(11200)/fs
ramp=np.ones(len(time));ramp[:160]=np.linspace(0,1,160);ramp[-160:]=np.linspace(1,0,160)
for phase,name in zip([0,2*np.pi/3,np.pi],['phase-0','phase-120','phase-180']):
    model=.6*ramp*(.2*np.cos(2*np.pi*1000*time)+.2*np.cos(2*np.pi*1000*time+phase))
    with wave.open(str(ROOT/f'public/audio/complex-analysis/{name}.wav'),'rb') as f:
        assert (f.getnchannels(),f.getsampwidth(),f.getframerate(),f.getnframes())==(1,2,16000,11200)
        pcm=np.frombuffer(f.readframes(f.getnframes()),dtype='<i2')
    np.testing.assert_array_equal(pcm,np.rint(32767*model).astype('<i2'))
    assert np.max(np.abs(pcm.astype(int)))<32767
    if name=='phase-180':assert np.count_nonzero(pcm)==0
    checks.append('actual PCM duration, common gain/ramp, no clipping '+name)
figures=list((ROOT/'public/figures/complex-analysis').glob('*.svg'))
assert len(figures)==8
for figure in figures:ET.parse(figure)
checks.append('eight well-formed generated SVGs')
result={'status':'passed','checks':checks,'count':len(checks),
 'scope':'independent identities and counterexamples, circle quadrature, exact coefficients, manual recurrence, impulse Fourier sum, optimized peak, real integrals and actual PCM'}
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
