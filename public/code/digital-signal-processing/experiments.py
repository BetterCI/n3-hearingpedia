"""Original DSP teaching calculations. NumPy/SciPy; no measured signals."""
import json
import numpy as np
from scipy import signal
FS=16000.
def spectral_demo():
    N=256;n=np.arange(N);x=.8*np.cos(2*np.pi*2050*n/FS)
    windows={'矩形窗':np.ones(N),'周期Hann窗':signal.windows.hann(N,sym=False)}
    return n,x,windows
def fir_designs():
    return [('65点Hann',signal.firwin(65,3000,fs=FS,window='hann')),
            ('129点Hann',signal.firwin(129,3000,fs=FS,window='hann')),
            ('129点Kaiser β=8.6',signal.firwin(129,3000,fs=FS,window=('kaiser',8.6)))]
def iir_design():
    return signal.butter(6,3000,fs=FS,output='sos')
def overlap_add(x,h,B=64):
    """Full linear convolution, power-of-two FFT, all overlap and tail retained."""
    x=np.asarray(x);h=np.asarray(h);M=len(h);Nfft=1<<int(np.ceil(np.log2(B+M-1)))
    y=np.zeros(len(x)+M-1);H=np.fft.rfft(h,Nfft)
    for start in range(0,len(x),B):
        block=x[start:start+B];v=np.fft.irfft(np.fft.rfft(block,Nfft)*H,Nfft)
        length=len(block)+M-1;y[start:start+length]+=v[:length]
    return y
def stft_demo():
    """Explicit rFFT, zero extension, analysis/synthesis Hann, normalized WOLA."""
    N=256;hop=64;nfft=512;L=4096;n=np.arange(L);t=n/FS
    x=np.where(n<L//2,np.cos(2*np.pi*1000*t),np.cos(2*np.pi*3000*t))
    w=signal.windows.hann(N,sym=False);xp=np.pad(x,(N,N))
    starts=np.arange(0,len(xp)-N+1,hop)
    frames=xp[starts[:,None]+np.arange(N)]*w
    X=np.fft.rfft(frames,nfft,axis=1)
    timeframes=np.fft.irfft(X,nfft,axis=1)[:,:N]
    y=np.zeros(len(xp));den=np.zeros(len(xp))
    for start,frame in zip(starts,timeframes):
        y[start:start+N]+=frame*w;den[start:start+N]+=w*w
    valid=den>1e-12;y[valid]/=den[valid]
    return dict(x=x,y=y[N:N+L],den=den[N:N+L],X=X,
        times=(starts+N/2-N)/FS,frequencies=np.fft.rfftfreq(nfft,1/FS),window=w,hop=hop,nfft=nfft)
def multirate_demo():
    fs=32000.;n=np.arange(8192);x=.8*np.cos(2*np.pi*1000*n/fs)+.5*np.cos(2*np.pi*13000*n/fs)
    h=signal.firwin(129,7000,fs=fs,window=('kaiser',8.6))
    naive=x[::2];filtered=signal.resample_poly(x,1,2,window=h,padtype='constant')
    return fs,x,h,naive,filtered
def tone_amplitude(x,f,fs):
    n=np.arange(len(x));return float(2*abs(np.sum(x*np.exp(-2j*np.pi*f*n/fs)))/len(x))
def quantizer(x,delta=.25):
    code=np.clip(np.floor((np.asarray(x)+1)/delta),0,int(2/delta)-1)
    return -1+(code+.5)*delta
def quantization_demo():
    n=np.arange(512);x=.1*np.cos(2*np.pi*n/32+.2);q=quantizer(x);e=q-x
    r=np.correlate(e,e,'full')[len(e)-1:]/len(e)
    return x,q,e,r/r[0]
def coefficient_demo(N=10000):
    a=.9997;aq=np.round(a*1024)/1024;n=np.arange(N)
    return a,float(aq),a**n,aq**n,(1-a**(n+1))/(1-a),n+1.
def adaptive_demo():
    rng=np.random.default_rng(20261102);M=16;h=np.zeros(M);h[[0,3,8]]=[.8,.35,-.2]
    x=rng.normal(0,.2,4000);clean=signal.lfilter(h,[1.],x);d=clean+rng.normal(0,.02,len(x));w=np.zeros(M)
    xp=np.pad(x,(M-1,0));mu=.2;eps=1e-6;train_error=[]
    for n in range(len(x)):
        u=xp[n:n+M][::-1];pred=w@u;e=d[n]-pred
        w+=mu*e*u/(eps+u@u);train_error.append(e)
    xv=rng.normal(0,.2,1000);cv=signal.lfilter(h,[1.],xv);dv=cv+rng.normal(0,.02,len(xv));pred=signal.lfilter(w,[1.],xv)
    return dict(h=h,w=w,x=x,d=d,train_error=np.asarray(train_error),validation_x=xv,validation_clean=cv,validation_observed=dv,prediction=pred,
        mu=mu,epsilon=eps,coefficient_rmse=float(np.sqrt(np.mean((w-h)**2))),
        validation_model_rmse=float(np.sqrt(np.mean((pred-cv)**2))),validation_observation_rmse=float(np.sqrt(np.mean((pred-dv)**2))))
def summary():
    _,_,windows=spectral_demo();fir=[]
    for name,h in fir_designs():
        f,H=signal.freqz(h,worN=65536,fs=FS)
        fir.append(dict(name=name,length=len(h),delay_samples=(len(h)-1)/2,delay_ms=(len(h)-1)/2/FS*1000,
            passband_max_absolute_magnitude_error=float(np.max(abs(abs(H[f<=2500])-1))),
            stopband_attenuation_dB=float(-20*np.log10(np.max(abs(H[f>=3500])))),
            cutoff_magnitude=float(abs(H[np.argmin(abs(f-3000))]))))
    sd=stft_demo();fs,x,h,nv,fv=multirate_demo();a,aq,_,_,_,_=coefficient_demo();ad=adaptive_demo()
    return dict(fs_Hz=FS,windows={name:dict(coherent_gain=float(w.mean()),ENBW_Hz=float(FS*np.sum(w*w)/np.sum(w)**2)) for name,w in windows.items()},
        FIR=fir,IIR=dict(order=6,cutoff_Hz=3000,cutoff_single_magnitude=float(1/np.sqrt(2)),cutoff_forward_backward_magnitude=.5),
        WOLA=dict(window_length=256,hop=64,nfft=512,original_length=len(sd['x']),max_reconstruction_error=float(np.max(abs(sd['x']-sd['y']))),minimum_denominator=float(sd['den'].min())),
        multirate=dict(input_fs_Hz=fs,output_fs_Hz=fs/2,input_tones_Hz=[1000,13000],alias_Hz=3000,
            naive_alias_amplitude=tone_amplitude(nv[1024:3072],3000,fs/2),filtered_alias_amplitude=tone_amplitude(fv[1024:3072],3000,fs/2),
            filtered_pass_amplitude=tone_amplitude(fv[1024:3072],1000,fs/2)),
        coefficient=dict(original_a=a,rounded_a=aq,fractional_bits=10,coefficient_only_rounding=True),
        adaptive={key:ad[key] for key in ['mu','epsilon','coefficient_rmse','validation_model_rmse','validation_observation_rmse']})
if __name__=='__main__':print(json.dumps(summary(),ensure_ascii=True,indent=2))
