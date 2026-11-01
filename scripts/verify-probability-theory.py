"""Independent numerical and actual-media checks for the probability course."""
from pathlib import Path
from math import comb, exp, sqrt, pi, factorial
import json
import wave
import numpy as np
from scipy.integrate import quad
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
REC=ROOT/'docs/research/probability-theory-2026-11-01'
record=json.loads((REC/'calculations.json').read_text(encoding='utf-8'))
checks=[]
def near(name, observed, expected, atol=1e-11):
    np.testing.assert_allclose(observed, expected, atol=atol, rtol=0)
    checks.append(name)

# Direct finite enumeration rather than the generator's SciPy PMF/SF.
ks=np.arange(41)
pmf=np.array([comb(40,int(k))*.75**int(k)*.25**int(40-k) for k in ks])
near('binomial normalization and moments',[pmf.sum(),ks@pmf,((ks-30)**2)@pmf],[1,30,7.5])
tail=sum(comb(40,k) for k in range(30,41))/2**40
near('exact one-sided binomial tail',record['binomial']['one_sided_p_at_chance'],tail)
near('Poisson example and count normalization',sum(exp(-2)*2**k/factorial(k) for k in range(35)),1)
normal=lambda x: exp(-x*x/(2*.02**2))/(sqrt(2*pi)*.02)
near('normal integral',quad(normal,-.01,.01)[0],record['normal']['prob_within_0_01_Pa'])
near('normal density units example',normal(0),record['normal']['density_at_zero'])
near('Bayes expected-count directions',[160/200,80/800,160/240],[.8,.1,record['bayes']['prior_0_2']])
near('rare-signal Bayes update',16/(16+98),record['bayes']['prior_0_02'])

# Enumerate the two-trial distribution after mixing two listener types.
joint=np.zeros((2,2))
for p in (.6,.9):
    for x in (0,1):
        for y in (0,1):
            joint[x,y]+=.5*(p if x else 1-p)*(p if y else 1-p)
ex=joint[1,:].sum()
ey=joint[:,1].sum()
near('mixed listeners marginal expectation and covariance',[ex,ey,joint[1,1]-ex*ey],[.75,.75,.0225])
near('total variance decomposition',.165+.0225,.75*.25)
xx=np.array([-1,0,1])
near('uncorrelated dependent counterexample',np.mean(xx*xx**2)-np.mean(xx)*np.mean(xx**2),0)

# Matrix covariance calculation independently checks the scalar average formula.
M=16
for rho,key in [(0,'independent_sd'),(.5,'shared_sd')]:
    cov=.2**2*((1-rho)*np.eye(M)+rho*np.ones((M,M)))
    weights=np.ones(M)/M
    near('averaging covariance matrix '+str(rho),sqrt(weights@cov@weights),record['averaging'][key])
near('independent power SNR gain',10*np.log10(.2**2/.05**2),record['averaging']['independent_power_snr_gain_dB'])
near('shared power SNR gain',10*np.log10(.2**2/record['averaging']['shared_sd']**2),record['averaging']['shared_power_snr_gain_dB'])

# Quadrature rather than norm.sf for detector probabilities.
pdf=lambda z: exp(-z*z/2)/sqrt(2*pi)
near('detector F by quadrature',quad(pdf,1,np.inf)[0],record['detection']['F'])
near('detector H by quadrature',quad(pdf,-.5,np.inf)[0],record['detection']['H'])
near('independent difference 2IFC',quad(pdf,-1.5/sqrt(2),np.inf)[0],record['detection']['two_interval_correct'])
t=record['psychometric']['threshold_at_0_75_dB']
near('inverse psychometric threshold',.5+.48/(1+exp(-t/3)),.75)
lo,hi=record['estimation']['wilson_95']
z=stats.norm.ppf(.975)
# Wilson endpoints invert the binomial score statistic, independently of its closed form.
near('Wilson score inversion',[(.75-v)/sqrt(v*(1-v)/40) for v in (lo,hi)],[z,-z])
# Direct normalization and integration of the posterior polynomial.
kernel=lambda p:p**30*(1-p)**10
norm=quad(kernel,0,1,epsabs=1e-30)[0]
post=lambda p:kernel(p)/norm
near('posterior normalization',quad(post,0,1)[0],1)
near('posterior mean by quadrature',quad(lambda p:p*post(p),0,1)[0],31/42)
blo,bhi=record['estimation']['credible_95']
near('posterior equal tail integrals',[quad(post,0,blo)[0],quad(post,bhi,1)[0]],[.025,.025])

# Reconstruct original random arrays, then inspect the actual PCM files and headers.
fs=16000
time=np.arange(12800)/fs
tone=.15*np.sin(2*np.pi*1000*time)
rng=np.random.default_rng(20261103)
ind=rng.normal(0,.2,(16,len(time)))
common=rng.normal(0,.2,len(time))
private=rng.normal(0,.2,(16,len(time)))
shared=sqrt(.5)*common+sqrt(.5)*private
ramp=np.ones(len(time));ramp[:160]=np.linspace(0,1,160);ramp[-160:]=np.linspace(1,0,160)
models={'one-trial':tone+ind[0],'average-16':tone+ind.mean(axis=0),
        'shared-average-16':tone+shared.mean(axis=0)}
for name,model in models.items():
    with wave.open(str(ROOT/f'public/audio/probability-theory/{name}.wav'),'rb') as f:
        assert (f.getnchannels(),f.getsampwidth(),f.getframerate(),f.getnframes())==(1,2,16000,12800)
        pcm=np.frombuffer(f.readframes(f.getnframes()),dtype='<i2')
    assert np.max(np.abs(pcm.astype(int)))<32767
    expected=np.rint(32767*.65*ramp*model).astype('<i2')
    np.testing.assert_array_equal(pcm,expected)
    checks.append('actual WAV, common gain, ramp, reconstruction and no clipping: '+name)
    near('actual noise RMS '+name,sqrt(np.mean((model-tone)**2)),record['audio']['records'][name]['noise_rms_before_ramp_and_gain'])
assert len(list((ROOT/'public/figures/probability-theory').glob('*.svg')))==8
checks.append('eight generated SVG teaching figures')
out={'status':'passed','checks':checks,'count':len(checks),
     'scope':'independent analytic enumeration, quadrature, covariance matrix, score inversion and actual PCM media'}
(REC/'numerical-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
