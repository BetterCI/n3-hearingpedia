"""Original specified teaching models; numpy/scipy required, no measured data."""
import json
import numpy as np
from scipy.signal import lfilter
def pulse(t,width=.0008):
    return np.exp(-(np.asarray(t)/width)**2)
def echo():
    fs=8000.;n=np.arange(160);x=np.exp(-.5*((n-24)/6)**2)
    h=np.zeros(97);h[[0,40,96]]=[1.,.55,-.25]
    return fs,x,h,np.convolve(x,h)
def lowpass(w,tau=.005):
    return 1/(1+1j*np.asarray(w)*tau)
def initial(t,tau=.005,y0=.5):
    t=np.asarray(t);zero_state=1-np.exp(-t/tau);zero_input=y0*np.exp(-t/tau)
    return zero_state,zero_input,zero_state+zero_input
def square_series(t,last):
    t=np.asarray(t);k=np.arange(1,last+1,2)
    return np.sum(4/(np.pi*k[:,None])*np.sin(2*np.pi*k[:,None]*t),axis=0)
def record_sequence():
    return np.exp(2j*np.pi*(3.4/32)*np.arange(32))
def dtft(x,cycles):
    return np.exp(-2j*np.pi*np.outer(np.asarray(cycles),np.arange(len(x))))@np.asarray(x)
def quantize(x,bits=3):
    levels=2**bits;delta=2./levels
    code=np.clip(np.floor((np.asarray(x)+1)/delta),0,levels-1)
    return -1+(code+.5)*delta
def feedback(k,N=60):
    x=np.zeros(N);x[0]=1
    return lfilter([1.],[1.,k],x)
def summary():
    fs,x,h,y=echo();zs,zi,total=initial(.005)
    H=lowpass(2*np.pi*100)
    return dict(echo=dict(fs_Hz=fs,length=len(y),tap_sum=float(h.sum()),delays_ms=[0.,40/fs*1000,96/fs*1000],sum_residual=float(y.sum()-x.sum()*h.sum())),
        initial=dict(tau_s=.005,at_tau_zero_state=float(zs),at_tau_zero_input=float(zi),at_tau_total=float(total)),
        frequency=dict(tau_s=.005,cutoff_Hz=1/(2*np.pi*.005),gain_100Hz=float(abs(H)),phase_100Hz_rad=float(np.angle(H)),cutoff_gain_db=float(20*np.log10(abs(lowpass(200*2*np.pi,1/(400*np.pi)))))),
        roc=dict(a=.8,causal_absolute_sum=1/(1-.8),causal_unit_circle_inside_ROC=True,anticausal_unit_circle_inside_ROC=False),
        sampling=dict(fs_Hz=8000.,aliased_cosines_Hz=[6000.,2000.],max_alias_sample_error=float(np.max(abs(np.cos(2*np.pi*6000*np.arange(64)/8000)-np.cos(2*np.pi*2000*np.arange(64)/8000))))),
        quantization=dict(bits=3,levels=8,delta=.25,uniform_error_model_variance=.25**2/12),
        dft=dict(record_length=32,padded_length=128,cycles_per_sample=3.4/32),
        feedback=dict(stable_pole=-.5,unstable_pole=-1.05,last_abs_stable=float(abs(feedback(.5)[-1])),last_abs_unstable=float(abs(feedback(1.05)[-1]))))
if __name__=='__main__':print(json.dumps(summary(),indent=2))
