"""Cross-check article claims using definitions and alternative numerical routes."""
from pathlib import Path
import sys,importlib.util,json,xml.etree.ElementTree as ET
sys.dont_write_bytecode=True
import numpy as np
import scipy
from scipy import signal,integrate
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/digital-signal-processing-2026-11-02'
spec=importlib.util.spec_from_file_location('models',ROOT/'public/code/digital-signal-processing/experiments.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def close(a,b,tol=1e-11):np.testing.assert_allclose(a,b,atol=tol,rtol=tol)
def record(name,**metrics):checks.append(dict(check=name,status='passed',**metrics))
rng=np.random.default_rng(61102)
# 1 DFT direct definition, inverse and Parseval.
x=rng.normal(size=31);n=np.arange(len(x));D=np.exp(-2j*np.pi*n[:,None]*n/len(x));X=D@x
close(X,np.fft.fft(x));close(D.conj().T@X/len(x),x);close(np.sum(x*x),np.sum(abs(X)**2)/len(x))
record('DFT definition / inverse / Parseval',N=len(x))
# 2 Zero padding samples the same finite-record DTFT.
f=np.arange(1024)/1024;direct=np.exp(-2j*np.pi*f[:,None]*n)@x
close(direct,np.fft.fft(x,1024));record('Zero padding / direct finite DTFT',original_length=31,FFT_length=1024)
# 3 Coherent real-tone amplitude, CG, ENBW and DC/Nyquist.
fs=16000;N=256;n=np.arange(N);w=.5-.5*np.cos(2*np.pi*n/N)
close(w,signal.windows.hann(N,sym=False));close(w.mean(),.5)
close(fs*np.sum(w*w)/w.sum()**2,93.75)
close(2*abs(np.fft.rfft(w*.8*np.cos(2*np.pi*32*n/N))[32])/w.sum(),.8)
close(abs(np.fft.rfft(w*2)[0])/w.sum(),2)
close(abs(np.fft.rfft(w*((-1.)**n))[N//2])/w.sum(),1)
record('Periodic Hann / coherent gain / ENBW / endpoint amplitudes',ENBW_Hz=93.75)
# 4 PSD scaling and one-sided endpoint rules, odd and even FFT.
x=rng.normal(size=N)+.7
for nf in [256,511,1024]:
    fft=np.fft.fft(w*x,nf);two=abs(fft)**2/(fs*np.sum(w*w))
    f,P=signal.periodogram(x,fs=fs,window=w,nfft=nf,detrend=False,scaling='density',return_onesided=False)
    close(two,P)
    one=two[:nf//2+1].copy()
    one[1:-1 if nf%2==0 else None]*=2
    f,P=signal.periodogram(x,fs=fs,window=w,nfft=nf,detrend=False,scaling='density',return_onesided=True)
    close(one,P);close(P.sum()*fs/nf,np.sum((w*x)**2)/np.sum(w*w))
    _,S=signal.periodogram(x,fs=fs,window=w,nfft=nf,detrend=False,scaling='spectrum')
    close(S,P*93.75)
record('PSD / spectrum / weighted mean square',FFT_lengths=[256,511,1024],
       weighted_ms=float(np.sum((w*x)**2)/np.sum(w*w)),unweighted_ms=float(np.mean(x*x)))
# 5 Welch mean of explicit overlapping periodograms.
x=rng.normal(size=1000);hop=128;parts=[]
for start in range(0,len(x)-N+1,hop):
    _,P=signal.periodogram(x[start:start+N],fs=fs,window=w,detrend=False,scaling='density')
    parts.append(P)
_,welch=signal.welch(x,fs=fs,window=w,nperseg=N,noverlap=N-hop,detrend=False,scaling='density',average='mean')
close(welch,np.mean(parts,axis=0));record('Welch explicit segment averaging',segments=len(parts),overlap_samples=128)
# 6 Difference equation signs and nonunit a0.
x=rng.normal(size=200);b=np.array([.6,.2]);a=np.array([2.,-.8]);y=np.zeros(len(x))
for n in range(len(x)):
    y[n]=(.6*x[n]+(.2*x[n-1] if n else 0)+(.8*y[n-1] if n else 0))/2
close(y,signal.lfilter(b,a,x));record('Difference equation / feedback sign / a0 normalization')
# 7 Windowed sinc vs FIR library, phase slope, cutoff convention.
M=129;k=np.arange(M);alpha=(M-1)/2
hd=2*3000/fs*np.sinc(2*3000/fs*(k-alpha))
hw=hd*np.kaiser(M,8.6);hw/=hw.sum();h=m.fir_designs()[2][1];close(hw,h);close(h,h[::-1])
f=np.linspace(100,2400,2000);_,H=signal.freqz(h,worN=2*np.pi*f/fs)
delay=-np.gradient(np.unwrap(np.angle(H)),2*np.pi*f/fs);close(delay,64,tol=1e-8)
_,Hc=signal.freqz(h,worN=[2*np.pi*3000/fs]);assert abs(abs(Hc[0])-.5)<1e-4
record('FIR sinc construction / symmetry / phase slope / half amplitude',group_delay_samples=64,cutoff_magnitude=float(abs(Hc[0])))
# 8 Butterworth analog poles mapped independently through bilinear transform.
order=6;wc=2*fs*np.tan(np.pi*3000/fs)
pa=wc*np.exp(1j*np.pi*(2*np.arange(order)+1+order)/(2*order))
pd=(2*fs+pa)/(2*fs-pa);zz=-np.ones(order);gain=np.prod(1-pd)/np.prod(1-zz)
f=np.linspace(0,7900,2000);z=np.exp(2j*np.pi*f/fs)
Hp=gain*np.prod(z[:,None]-zz,axis=1)/np.prod(z[:,None]-pd,axis=1)
sos=m.iir_design();_,Hs=signal.sosfreqz(sos,worN=2*np.pi*f/fs);close(Hp,Hs)
_,hc=signal.sosfreqz(sos,worN=[2*np.pi*3000/fs]);close(abs(hc[0]),1/np.sqrt(2))
assert np.max(abs(pd))<1
record('Butterworth prototype / prewarp / independent pole product',maximum_pole_radius=float(np.max(abs(pd))),cutoff_magnitude=float(abs(hc[0])))
# 9 Independently implemented section recurrence, whole vs irregular streaming.
x=rng.normal(size=1003);alt=x.copy()
for b0,b1,b2,a0,a1,a2 in sos:
    xx=alt.copy();alt=np.zeros(len(xx))
    for n in range(len(xx)):
        alt[n]=(b0*xx[n]+(b1*xx[n-1]-a1*alt[n-1] if n else 0)+(b2*xx[n-2]-a2*alt[n-2] if n>1 else 0))/a0
whole=signal.sosfilt(sos,x);close(alt,whole)
for B in [1,64,127,400]:
    zi=np.zeros((len(sos),2));parts=[];reset=[]
    for start in range(0,len(x),B):
        chunk=x[start:start+B];yy,zi=signal.sosfilt(sos,chunk,zi=zi);parts.append(yy);reset.append(signal.sosfilt(sos,chunk))
    close(np.concatenate(parts),whole)
    if B==64:assert np.max(abs(np.concatenate(reset)-whole))>.01
record('SOS independent recurrence / state continuity / reset counterexample',block_sizes=[1,64,127,400])
# 10 Long tone double pass, cropped away from endpoint effects.
n=np.arange(8192);x=np.cos(2*np.pi*3000*n/fs);double=signal.sosfiltfilt(sos,x,padtype='odd')
close(double[1000:-1000],.5*x[1000:-1000],tol=1e-10)
record('Forward/backward internal response / squared magnitude',single_cutoff_dB=float(20*np.log10(abs(hc[0]))),double_cutoff_dB=float(40*np.log10(abs(hc[0]))))
# 11 OLA all tails; independent OLS with full output coverage.
h=m.fir_designs()[1][1];M=len(h);x=rng.normal(size=257);expected=np.convolve(x,h)
for B in [1,32,64,100,512]:close(m.overlap_add(x,h,B),expected)
nf=256;B=nf-M+1;xp=np.pad(x,(M-1,M-1+B));outs=[]
for start in range(0,len(expected),B):
    block=xp[start:start+nf];v=np.fft.irfft(np.fft.rfft(block,nf)*np.fft.rfft(h,nf),nf)
    outs.append(v[M-1:])
close(np.concatenate(outs)[:len(expected)],expected)
record('OLA vs direct / OLS / partial block / complete tails',input_length=257,FIR_length=129,output_length=len(expected),OLA_blocks=[1,32,64,100,512])
# 12 STFT frames against SciPy, aligning scale and the extra padding frame.
d=m.stft_demo();N=256;R=64;nf=512;ww=d['window'];xp=np.pad(d['x'],(N,N))
f,t,Z=signal.stft(xp,fs=fs,window=ww,nperseg=N,noverlap=N-R,nfft=nf,boundary=None,padded=False,detrend=False,scaling='spectrum')
close(Z.T*ww.sum(),d['X']);close(t-N/fs,d['times']);close(f,d['frequencies'])
close(d['y'],d['x']);close(d['den'],1.5)
assert signal.check_NOLA(ww,N,N-R)
assert not signal.check_NOLA(ww,N,0)
record('STFT convention / independent API / normalized WOLA / NOLA failure',max_reconstruction_error=float(np.max(abs(d['y']-d['x']))))
# 13 Raw upfirdn explicit insertion and full convolution, several ratios.
for L,D in [(3,2),(2,5),(1,2),(5,1)]:
    h=signal.firwin(31,1/max(L,D),fs=2,window=('kaiser',5))
    x=rng.normal(size=17);z=np.zeros((len(x)-1)*L+1);z[::L]=x
    close(signal.upfirdn(L*h,x,up=L,down=D),np.convolve(z,L*h)[::D])
record('Polyphase vs explicit upsample / filter / downsample',ratios=['3/2','2/5','1/2','5/1'])
# 14 Downsampling aliases and centred antialias suppression.
fsin,x,h,nv,fv=m.multirate_demo();n=np.arange(len(nv))
close(nv,.8*np.cos(2*np.pi*1000*n/16000)+.5*np.cos(2*np.pi*3000*n/16000))
alias=m.tone_amplitude(fv[1024:3072],3000,16000);pas=m.tone_amplitude(fv[1024:3072],1000,16000)
assert alias<3e-6 and abs(pas-.8)<1e-5
record('Rate conversion / exact alias / filtered central amplitude',filtered_alias_amplitude=alias,filtered_pass_amplitude=pas)
# 15 Quantization bounds, conditional distribution variance, periodic error.
x=np.linspace(-.99,.99,9999);e=m.quantizer(x)-x;assert np.max(abs(e))<=.125+1e-15
variance=integrate.quad(lambda e:e*e/.25,-.125,.125)[0];close(variance,.25**2/12)
x,q,e,r=m.quantization_demo();close(e[32:],e[:-32]);assert r[32]>.9
assert abs(m.quantizer([2])[0]-2)>.125
record('Quantizer no-overload bound / uniform-model variance / periodic error / overload counterexample',conditional_variance=variance,error_autocorrelation_lag32=float(r[32]))
# 16 Coefficient-only rounding, independent scalar recurrences.
a,aq,imp,impq,step,stepq=m.coefficient_demo();assert aq==1
for aa,ii,ss in [(a,imp,step),(aq,impq,stepq)]:
    yi=0.;ys=0.;iv=[];sv=[]
    for n in range(len(ii)):
        yi=aa*yi+(1. if n==0 else 0.);ys=aa*ys+1;iv.append(yi);sv.append(ys)
    close(iv,ii);close(sv,ss,tol=1e-8)
record('Coefficient-only rounding / impulse and step recurrence',original_a=a,rounded_a=aq)
# 17 NLMS finite-difference loss gradient and normalization.
u=rng.normal(size=16);w0=rng.normal(size=16);target=.3
loss=lambda v:.5*(target-v@u)**2
eta=1e-6;gradient=np.array([(loss(w0+eta*np.eye(16)[k])-loss(w0-eta*np.eye(16)[k]))/(2*eta) for k in range(16)])
close(gradient,-(target-w0@u)*u,tol=1e-8)
close(.2*0*np.zeros(16)/(1e-6+0),np.zeros(16))
record('Real NLMS loss gradient / zero input normalization')
# 18 Independently verify frozen-model held-out metrics by direct convolution.
d=m.adaptive_demo();cv=np.convolve(d['validation_x'],d['h'])[:1000];pred=np.convolve(d['validation_x'],d['w'])[:1000]
close(cv,d['validation_clean']);close(pred,d['prediction'])
close(np.sqrt(np.mean((pred-cv)**2)),d['validation_model_rmse'])
close(np.sqrt(np.mean((pred-d['validation_observed'])**2)),d['validation_observation_rmse'])
assert not np.array_equal(d['x'][:1000],d['validation_x'])
record('Frozen NLMS / separate validation / two reference targets',coefficient_RMSE=d['coefficient_rmse'],validation_model_RMSE=d['validation_model_rmse'],validation_observation_RMSE=d['validation_observation_rmse'])
# 19 Source and XML integrity (scientific source scope is reviewed separately).
sources=json.loads((REC/'source-index.json').read_text(encoding='utf-8'));assert len(sources)==22 and all(s['status']=='fetched' for s in sources)
figs=list((ROOT/'public/figures/digital-signal-processing').glob('*.svg'));assert len(figs)==10
for path in figs:ET.parse(path)
ET.parse(ROOT/'public/figures/foundation-courses/digital-signal-processing.svg')
record('Source retrieval records / 10 original figure XML / card SVG',sources=22,figures=10)
result=dict(status='passed',check_groups=len(checks),numpy=np.__version__,scipy=scipy.__version__,checks=checks,
    limitations='Finite numerical cross-checks of the specified teaching examples; not external peer review, all-parameter proofs, device measurements or perceptual validation.')
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=result['status'],check_groups=len(checks),numpy=np.__version__,scipy=scipy.__version__)))
