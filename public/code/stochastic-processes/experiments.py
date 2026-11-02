"""Original stochastic-process teaching models. No recordings or participant data.
Python 3.11, NumPy 1.26.4, SciPy 1.17.1. Spectral densities use Hz and physical sampling rate.
"""
import numpy as np
from scipy.signal import lfilter,periodogram,welch
from scipy.linalg import toeplitz
from scipy.integrate import quad
FS=1000.
AR=.8
INNOVATION_VARIANCE=1-AR**2

def ar1(n=8192,paths=1,a=AR,q=INNOVATION_VARIANCE,seed=20261102):
    assert abs(a)<1 and q>0
    rng=np.random.default_rng(seed);x=np.empty((paths,n));x[:,0]=rng.normal(size=paths)*np.sqrt(q/(1-a*a))
    for i in range(1,n):x[:,i]=a*x[:,i-1]+rng.normal(size=paths)*np.sqrt(q)
    return x

def ar_psd(f,fs=FS,a=AR,q=INNOVATION_VARIANCE):
    return (q/fs)/(1+a*a-2*a*np.cos(2*np.pi*np.asarray(f)/fs))

def mean_variance(n,a=AR,variance=1.):
    lag=np.arange(1,n)
    return float(variance*(n+2*np.sum((n-lag)*a**lag))/n**2)

def mixture_white(n=4096,paths=8,seed=20261103):
    rng=np.random.default_rng(seed);amplitudes=np.array([1.,2.]*(paths//2+1))[:paths]
    return amplitudes,amplitudes[:,None]*rng.normal(size=(paths,n))

def moving_average_H(f,length=8,fs=FS):
    f=np.atleast_1d(f);return np.mean(np.exp(-2j*np.pi*f[:,None]*np.arange(length)[None,:]/fs),axis=1)

def alias_density(f,fs=FS,bandlimit=750.,level=.001):
    f=np.asarray(f);return sum(level*(abs(f+k*fs)<=bandlimit) for k in range(-3,4))

def wiener_example(n=8192):
    noise_variance=.5;length=3;lags=np.arange(length);R=toeplitz(AR**lags)+noise_variance*np.eye(length);r=AR**lags;weights=np.linalg.solve(R,r)
    causal_mse=float(1-r@weights)
    noncausal_mse=quad(lambda f:ar_psd(f)*(noise_variance/FS)/(ar_psd(f)+noise_variance/FS),-FS/2,FS/2,epsabs=1e-12)[0]
    clean=ar1(n=n)[0];noise=np.random.default_rng(20261104).normal(size=n)*np.sqrt(noise_variance);observed=clean+noise;estimate=lfilter(weights,[1.],observed)
    return dict(clean=clean,observed=observed,estimate=estimate,weights=weights,normal_matrix=R,cross_vector=r,causal_mse=causal_mse,noncausal_mse=float(noncausal_mse),noisy_mse=noise_variance,history_incomplete_samples=length-1)

def random_phase_tone(n=1024,frequency=125.,fs=FS,phase=.7):
    return np.sqrt(2)*np.cos(2*np.pi*frequency*np.arange(n)/fs+phase)

def finite_correlations():
    x=np.array([1.,-1.,1.]);n=len(x);sums=np.correlate(x,x,'full')[n-1:]
    biased=sums/n;unbiased=sums/(n-np.arange(n));theta=np.linspace(-np.pi,np.pi,2001)
    def spectrum(c):return c[0]+2*np.sum(c[1:,None]*np.cos(np.arange(1,n)[:,None]*theta),axis=0)
    return x,biased,unbiased,theta,spectrum(biased),spectrum(unbiased)

def count_and_brownian():
    rng=np.random.default_rng(20261105);events=[]
    for _ in range(4):
        t=0.;row=[]
        while True:
            t+=rng.exponential(1/20)
            if t>1:break
            row.append(t)
        events.append(np.array(row))
    dt=.001;t=np.arange(1001)*dt;paths=np.c_[np.zeros(4),np.cumsum(rng.normal(size=(4,1000))*np.sqrt(dt),axis=1)]
    return events,t,paths

def markov_example(n=250):
    P=np.array([[.95,.05],[.1,.9]]);pi=np.array([2/3,1/3]);rng=np.random.default_rng(20261106);states=np.empty(n,dtype=int);states[0]=rng.choice(2,p=pi)
    for i in range(1,n):states[i]=rng.choice(2,p=P[states[i-1]])
    return P,pi,states

def summary():
    w=wiener_example();_,b,u,theta,sb,su=finite_correlations();P,pi,_=markov_example();N=64;f=np.linspace(-FS/2,FS/2,20001)
    output_variance=mean_variance(8);tone={}
    for n in [256,1024]:
        freq,s=periodogram(random_phase_tone(n),fs=FS,window='boxcar',detrend=False,scaling='density');df=FS/n;tone[str(n)]=dict(bin_width_Hz=df,peak_Pa2_per_Hz=float(s.max()),integrated_mean_square=float(s.sum()*df))
    return dict(fs_Hz=FS,AR_coefficient=AR,innovation_variance=INNOVATION_VARIANCE,stationary_variance=1.,mean_N64_variance=mean_variance(N),mean_N64_iid_variance=1/N,mean_N64_effective_independent_count=1/mean_variance(N),mean_asymptotic_variance_inflation=(1+AR)/(1-AR),moving_average8_output_variance=output_variance,mixture_white=dict(ensemble_variance=2.5,shared_amplitudes=[1,2],conditional_time_powers=[1,4],distinct_squared_samples_covariance=2.25),random_phase_tone=tone,aliasing=dict(original_variance=1.5,sampled_variance=float(quad(lambda f:float(alias_density(f)),-FS/2,FS/2,points=[-250,250])[0]),antialias_variance=.9),wiener=dict(weights=w['weights'].tolist(),causal3_population_MSE=w['causal_mse'],noncausal_population_MSE=w['noncausal_mse'],noisy_MSE=.5),correlation_estimators=dict(biased=b.tolist(),unbiased=u.tolist(),unbiased_zero_extended_spectrum_at_cos_quarter=-1.25),markov=dict(transition=P.tolist(),stationary=pi.tolist(),second_eigenvalue=.85),poisson=dict(rate_per_second=20,mean_count_at_1s=20,variance_count_at_1s=20),brownian=dict(mean=0,variance_at_t='t',covariance='min(s,t)'))

if __name__=='__main__':
    import json
    print(json.dumps(summary(),ensure_ascii=False,indent=2))
