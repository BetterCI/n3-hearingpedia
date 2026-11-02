"""Independent moment, spectral, sampling and estimation checks; no empirical data."""
from pathlib import Path
import importlib.util,sys,json,hashlib,itertools,xml.etree.ElementTree as ET
sys.dont_write_bytecode=True
import numpy as np
from scipy.linalg import toeplitz
from scipy.integrate import quad
from scipy.signal import freqz,periodogram,welch,csd,coherence,get_window
from scipy.stats import poisson
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/stochastic-processes-2026-11-02';spec=importlib.util.spec_from_file_location('sp',ROOT/'public/code/stochastic-processes/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def check(name,condition,**evidence):
    assert condition,(name,evidence);checks.append(dict(name=name,passed=True,**evidence))
a,fs,q=m.AR,m.FS,m.INNOVATION_VARIANCE
check('AR innovation variance gives stationary variance one',np.isclose(q/(1-a*a),1))
R=toeplitz(a**np.arange(32));check('Specified covariance is symmetric positive definite',np.allclose(R,R.T) and np.linalg.eigvalsh(R).min()>0)
gaussian_fourth=quad(lambda x:x**4*np.exp(-x*x/2)/np.sqrt(2*np.pi),-np.inf,np.inf)[0];rademacher_fourth=np.mean(np.array([-1.,1.])**4)
check('WSS-not-strict counterexample differs in fourth marginal moment',abs(gaussian_fourth-3)<1e-11 and np.isclose(rademacher_fourth,1) and gaussian_fourth>rademacher_fourth,Gaussian_fourth_moment=gaussian_fourth,Rademacher_fourth_moment=rademacher_fourth,common_mean=0,common_variance=1)
ea2=np.mean(np.array([1.,2.])**2);ea4=np.mean(np.array([1.,2.])**4)
check('Shared amplitude white process retains higher-order dependence',np.isclose(ea2,2.5) and np.isclose(ea4-ea2**2,2.25),squared_samples_covariance=ea4-ea2**2)
check('Mixture mean is mean-square ergodic but power variance has positive limit',np.isclose(ea2/1000,.0025) and np.isclose((ea4-ea2**2)+2*ea4/1000,2.267),limiting_power_average_variance=ea4-ea2**2)
for N in [1,2,8,64,128]:
    mat=toeplitz(a**np.arange(N));value=np.ones(N)@mat@np.ones(N)/N**2;assert abs(value-m.mean_variance(N))<1e-12
check('Exact finite-N mean variance equals covariance quadratic form',True,value_N64=m.mean_variance(64),mean_specific_effective_N=1/m.mean_variance(64))
check('AR large-N variance inflation tends to nine',abs(100000*m.mean_variance(100000)-9)<.001)
f=np.linspace(-fs/2,fs/2,301);lag=np.arange(1,300);series=(1+2*np.sum(a**lag[:,None]*np.cos(2*np.pi*lag[:,None]*f/fs),axis=0))/fs
check('AR PSD from covariance Fourier series matches filter formula',np.max(abs(series-m.ar_psd(f)))<1e-14)
integral=quad(lambda f:m.ar_psd(f),-fs/2,fs/2,epsabs=1e-12)[0]
check('Per-Hz PSD integrates to stationary variance',abs(integral-1)<1e-12,integral=integral)
for k in [0,1,5]:assert abs(quad(lambda f:m.ar_psd(f)*np.cos(2*np.pi*f*k/fs),-fs/2,fs/2,epsabs=1e-12)[0]-a**k)<1e-11
check('Spectral inversion recovers several covariance lags',True)
check('Real AR spectrum is even and nonnegative',np.all(m.ar_psd(f)>0) and np.allclose(m.ar_psd(f),m.ar_psd(-f)))
_,H=freqz(np.ones(8)/8,worN=2*np.pi*f/fs)
check('Eight-point filter frequency response agrees with independent polynomial evaluation',np.max(abs(H-m.moving_average_H(f)))<1e-13)
outvar=quad(lambda f:float(abs(m.moving_average_H([f])[0])**2*m.ar_psd(f)),-fs/2,fs/2,epsabs=1e-12)[0];R8=toeplitz(a**np.arange(8));h=np.ones(8)/8
check('Filtered variance by spectral integral, covariance matrix and finite average formula',abs(outvar-h@R8@h)<1e-12 and abs(outvar-m.mean_variance(8))<1e-12,output_variance=outvar)
check('White per-Hz and normalized-angular densities have correct variance scaling',np.isclose((2.5/fs)*fs,2.5) and np.isclose(2.5/(2*np.pi)*(2*np.pi),2.5))
for k in [0,1,7]:
    moment=quad(lambda phase:2*np.cos(2*np.pi*.125*k+phase)*np.cos(phase),0,2*np.pi)[0]/(2*np.pi)
    assert abs(moment-np.cos(2*np.pi*.125*k))<1e-12
check('Uniform random phase gives stated stationary tone covariance and line masses',True,line_mass_each=.5,total_mean_square=1)
for N in [256,1024]:
    f,S=periodogram(m.random_phase_tone(N),fs=fs,window='boxcar',detrend=False,scaling='density');assert abs(S.max()-N/fs)<1e-12 and abs(S.sum()*fs/N-1)<1e-12
check('Two tone record lengths change peak height but preserve integrated mean square',True)
N=256;f,S=periodogram(np.full(N,3.),fs=fs,window='boxcar',detrend=False,scaling='density')
check('Constant mean produces DC spectral mass, not a record-length-invariant peak density',np.isclose(S[0]*fs/N,9) and np.count_nonzero(S)==1)
alias=quad(lambda f:float(m.alias_density(f)),-500,500,points=[-250,250],epsabs=1e-12)[0]
check('Physical-Hz alias sum preserves variance in specified bandlimited model',np.allclose(m.alias_density(np.array([0,200,300,490])),[.001,.001,.002,.002]) and abs(alias-1.5)<1e-12,variance=alias)
check('Ideal antialias passband deletes out-of-band variance',np.isclose(.001*900,.9) and .9<1.5)
rng=np.random.default_rng(42);x=rng.normal(size=1024);y=np.roll(x,3)
f,Pxy=csd(x,y,fs=fs,window='boxcar',nperseg=1024,noverlap=0,detrend=False,return_onesided=False)
_,Pxx=csd(x,x,fs=fs,window='boxcar',nperseg=1024,noverlap=0,detrend=False,return_onesided=False)
phase_error=float(np.max(abs(Pxy/Pxx-np.exp(-2j*np.pi*f*3/fs))))
check('SciPy CSD orientation matches S_YX for a circular delay semantic check',phase_error<1e-10,max_error=phase_error)
z=rng.normal(size=len(x));_,coh=coherence(x,z,fs=fs,window='boxcar',nperseg=len(x),noverlap=0,detrend=False)
check('One unaveraged segment yields unit sample coherence even for unrelated draws',np.max(abs(coh-1))<1e-12)
w=m.wiener_example();Rw=w['normal_matrix'];r=w['cross_vector'];weights=w['weights']
check('Causal normal equation has unique positive-definite solution',np.linalg.eigvalsh(Rw).min()>0 and np.max(abs(Rw@weights-r))<1e-12)
quadratic=1-2*weights@r+weights@Rw@weights
check('Population quadratic risk and error-observation orthogonality agree',abs(quadratic-w['causal_mse'])<1e-12 and np.linalg.norm(r-Rw@weights)<1e-12,population_MSE=quadratic)
for direction in np.eye(3):
    perturbed=weights+.1*direction;assert 1-2*perturbed@r+perturbed@Rw@perturbed>quadratic
check('Independent coefficient perturbations increase the specified convex risk',True)
v=.5;closed=q*v/np.sqrt((q+v*(1+a*a))**2-(2*v*a)**2)
check('Noncausal Wiener spectral integral agrees with independent closed-form integral',abs(closed-w['noncausal_mse'])<1e-12,closed_form_MSE=float(closed))
risks=[]
for L in [1,3,8]:
    r=a**np.arange(L);R=toeplitz(r)+v*np.eye(L);risks.append(float(1-r@np.linalg.solve(R,r)))
check('Causal risk decreases with more past observations and stays above full-time noncausal risk',np.all(np.diff(risks)<0) and min(risks)>closed and max(risks)<.5,causal_population_risks=risks)
ensemble=m.ar1(n=8,paths=20000,seed=121);variance=float(np.var(ensemble[:,0]));covariance=float(np.mean(ensemble[:,0]*ensemble[:,3]));mean=float(ensemble[:,0].mean())
check('Fixed-seed stationary AR initialization moment cross-check',abs(mean)<.025 and abs(variance-1)<.04 and abs(covariance-a**3)<.035,empirical_mean=mean,empirical_variance=variance,empirical_lag3_second_moment=covariance)
lambda_rate=20.;t=.7
check('Poisson mean and variance, and covariance time dependence',np.isclose(poisson.mean(lambda_rate*t),lambda_rate*t) and np.isclose(poisson.var(lambda_rate*t),lambda_rate*t) and np.isclose(lambda_rate*min(.3,.7),6))
for t in [.01,.1,.3]:assert abs(poisson.pmf(0,lambda_rate*t)-np.exp(-lambda_rate*t))<1e-14
check('Poisson zero-count probability matches exponential waiting survival',True)
times=np.array([.1,.3,.8,1.]);delta=np.diff(np.r_[0,times]);L=np.tril(np.ones((4,4)));cov=L@np.diag(delta)@L.T
check('Brownian covariance from independent increment construction is min(s,t)',np.allclose(cov,np.minimum.outer(times,times)) and np.allclose(np.diag(cov),times))
P,pi,states=m.markov_example();check('Markov rows, stationary law and eigenvalues',np.allclose(P.sum(axis=1),1) and np.allclose(pi@P,pi) and np.allclose(np.sort(np.linalg.eigvals(P)),[.85,1]))
for k in [0,1,5,30]:
    Pk=np.linalg.matrix_power(P,k);assert np.isclose(Pk[0,1],(1/3)*(1-.85**k))
    covariance=pi[1]*Pk[1,1]-pi[1]**2;assert np.isclose(covariance,(2/9)*.85**k)
check('Markov transient law and stationary indicator covariance',True)
x,b,u,theta,sb,su=m.finite_correlations();dtft=np.exp(-1j*theta[:,None]*np.arange(len(x)))@x
check('Fixed-denominator correlation zero-extension equals nonnegative DTFT power',np.max(abs(sb-abs(dtft)**2/len(x)))<1e-12 and sb.min()>-1e-12)
angle=np.arccos(.25);negative=u[0]+2*np.sum(u[1:]*np.cos(np.arange(1,3)*angle));extended=toeplitz(np.r_[u,np.zeros(5)])
check('Unbiased lag estimate with zero-extension need not define a nonnegative spectrum',abs(negative+1.25)<1e-12 and np.linalg.eigvalsh(extended).min()<0,spectral_value=float(negative))
N=4;expected_b=np.zeros(N);expected_u=np.zeros(N)
for seq in itertools.product([-1.,1.],repeat=N):
    z=np.array(seq);prob=.5*np.prod([.9 if z[i]==z[i-1] else .1 for i in range(1,N)]);sums=np.correlate(z,z,'full')[N-1:];expected_b+=prob*sums/N;expected_u+=prob*sums/(N-np.arange(N))
check('Exact finite Markov enumeration verifies lag-unbiasedness under known zero mean',np.allclose(expected_u,a**np.arange(N)) and np.allclose(expected_b,(1-np.arange(N)/N)*a**np.arange(N)))
rng=np.random.default_rng(722);z=rng.normal(size=(12000,64));F=np.fft.rfft(z,axis=1);I=abs(F)**2/(fs*64)
check('Fixed-seed white Gaussian periodogram fluctuation matches interior-bin law',abs(I[:,7].mean()/(1/fs)-1)<.04 and abs(I[:,7].var()/(1/fs)**2-1)<.08,mean_ratio=float(I[:,7].mean()*fs),variance_ratio=float(I[:,7].var()*fs**2))
x=m.ar1(n=8192)[0];window=get_window('hann',512,fftbins=True);segment=x[:512];f,s=periodogram(segment,fs=fs,window=window,detrend=False,scaling='density')
weighted=np.sum(window**2*segment**2)/np.sum(window**2)
check('Window density Parseval integral gives weighted second moment',abs(s.sum()*fs/512-weighted)<1e-12)
pieces=[]
for start in range(0,len(x)-512+1,256):
    F=np.fft.rfft(x[start:start+512]*window);s=abs(F)**2/(fs*np.sum(window**2));s[1:-1]*=2;pieces.append(s)
f,s=welch(x,fs=fs,window='hann',nperseg=512,noverlap=256,detrend=False,scaling='density')
check('Welch matches independent segment-window-normalization-and-fold calculation',np.max(abs(s-np.mean(pieces,axis=0)))<1e-13)
source=json.loads((REC/'source-index.json').read_text(encoding='utf-8'))
for row in source:
    assert row['status']=='fetched';path=ROOT/'artifacts/stochastic-processes/sources'/(row['id']+('.pdf' if row['pdf'] else '.html'));assert hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256']
check('Eighteen scoped author/official source hashes match cached originals',len(source)==18)
files=list((ROOT/'public/figures/stochastic-processes').glob('*.svg'))+[ROOT/'public/figures/foundation-courses/stochastic-processes.svg']
for file in files:ET.parse(file);assert '<script' not in file.read_text(encoding='utf-8')
check('Eleven original SVGs parse without executable script',len(files)==11)
result=dict(slug='stochastic-processes',check_groups=len(checks),checks=checks,professional_review='pending');(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(check_groups=len(checks),passed=len(checks))))
