"""Independent arithmetic/distribution checks for teaching examples, not peer review."""
from pathlib import Path
from itertools import product
from collections import Counter
import math
import json
import xml.etree.ElementTree as ET
import numpy as np
from scipy import stats, integrate, optimize

ROOT=Path(__file__).resolve().parents[1]
REC=ROOT/'docs/research/mathematical-statistics-2026-11-02'
r=json.loads((REC/'calculations.json').read_text(encoding='utf-8'));checks=[]
def near(name,a,b,tol=1e-10):
    np.testing.assert_allclose(a,b,rtol=0,atol=tol);checks.append(name)
def require(name,value):
    assert value,name;checks.append(name)

d=r['differences_dB'];n=len(d);total=sum(d);ss=sum(x*x for x in d)-total*total/n
near('paired count',n,12);near('paired sum',total,24);near('sum of squares',sum(x*x for x in d),78)
near('centered sum of squares',ss,30);near('sample mean',r['mean_dB'],total/n)
near('unbiased variance',r['variance_unbiased'],30/11);near('MLE variance',r['variance_mle'],30/12)
near('sample SD',r['sample_sd_dB'],math.sqrt(30/11));near('estimated SE',r['se_dB'],math.sqrt(30/132))
near('paired t',r['t_statistic'],math.sqrt(17.6));near('standardized dz',r['mean_dB']/r['sample_sd_dB'],math.sqrt(22/15))
near('paired raw conditions',np.array(r['condition_A_dB_SNR'])-r['condition_B_dB_SNR'],d)

def t_pdf(x,df):
    return math.exp(math.lgamma((df+1)/2)-math.lgamma(df/2))/math.sqrt(df*math.pi)*(1+x*x/df)**(-(df+1)/2)
critical=optimize.brentq(lambda c: integrate.quad(lambda x:t_pdf(x,11),0,c,epsabs=1e-12)[0]-.475,1,4)
near('t critical from integrated explicit density',r['t_critical'],critical)
tail=2*integrate.quad(lambda x:t_pdf(x,11),r['t_statistic'],np.inf,epsabs=1e-13)[0]
near('two-sided p from explicit t density integration',r['t_p_two_sided'],tail)
near('t CI endpoints from integrated quantile',r['t_ci_95_dB'],[2-critical*math.sqrt(30/132),2+critical*math.sqrt(30/132)])
near('normal density integrates to one',integrate.quad(lambda x:math.exp(-x*x/2)/math.sqrt(2*math.pi),-np.inf,np.inf)[0],1)
near('known-model SE n12',3/math.sqrt(12),math.sqrt(.75));near('known-model SE n48',3/math.sqrt(48),math.sqrt(.1875))

maximum=optimize.minimize_scalar(lambda p:-(60*math.log(p)+20*math.log1p(-p)),bounds=(.01,.99),method='bounded',options={'xatol':1e-12})
near('numerical likelihood maximizer',maximum.x,.75,2e-8)
near('relative likelihood at p05',r['relative_likelihood_p05'],.5**80/(.75**60*.25**20))
for p in [.2,.75]:
    score=[-1/(1-p),1/p];prob=[1-p,p]
    near(f'Bernoulli score zero mean p{p}',sum(a*b for a,b in zip(score,prob)),0)
    near(f'Bernoulli Fisher information p{p}',sum(a*a*b for a,b in zip(score,prob)),1/(p*(1-p)))
    weights=[math.comb(80,k)*p**k*(1-p)**(80-k) for k in range(81)]
    near(f'binomial normalization p{p}',sum(weights),1)
    near(f'sample proportion unbiased p{p}',sum(k/80*w for k,w in enumerate(weights)),p)
    near(f'sample proportion variance reaches CR bound p{p}',sum((k/80-p)**2*w for k,w in enumerate(weights)),p*(1-p)/80)
    conditional=[p**3*(1-p)**3/(math.comb(6,3)*p**3*(1-p)**3) for seq in product([0,1],repeat=6) if sum(seq)==3]
    near(f'conditional sequence probability independent of p{p}',conditional,np.full(20,1/20))

z=stats.norm.ppf(.975);phat=.75;nn=80
roots=np.sort(np.roots([nn+z*z,-2*nn*phat-z*z,nn*phat*phat]))
near('Wilson endpoints from quadratic inversion',r['wilson_60_80'],roots)
for p in roots:near('Wilson score boundary',nn*(phat-p)**2/(p*(1-p)),z*z)
near('posterior shape',r['posterior_beta'],[61,21]);near('posterior mean',r['posterior_mean'],61/82)
def beta_cdf_integer(p):
    return sum(math.comb(81,k)*p**k*(1-p)**(81-k) for k in range(61,82))
posterior_roots=[optimize.brentq(lambda p:beta_cdf_integer(p)-q,.1,.99,xtol=1e-14) for q in [.025,.975]]
near('Beta quantiles from finite binomial sum',r['posterior_equal_tail_95'],posterior_roots)
near('posterior interval probability via finite sum',beta_cdf_integer(posterior_roots[1])-beta_cdf_integer(posterior_roots[0]),.95)

rng=np.random.default_rng(r['seed_bootstrap']);index=rng.integers(0,n,size=(20000,n))
manual_boot=np.array([sum(d[int(i)] for i in row)/n for row in index])
near('bootstrap quantiles computed by scalar summation',r['bootstrap_ci_95_dB'],np.quantile(manual_boot,[.025,.975],method='linear'))
near('bootstrap MC SD',r['bootstrap_sd_dB'],manual_boot.std(ddof=1))
near('conditional bootstrap theoretical variance',np.var(d)/n,2.5/12)
require('bootstrap MC mean close to empirical mean',abs(manual_boot.mean()-2)<.02)
require('bootstrap MC SD close to conditional theoretical SD',abs(manual_boot.std(ddof=1)-math.sqrt(2.5/12))<.01)

counts=Counter({0:1})
for value in d:
    updated=Counter()
    for total,count in counts.items():updated[total+value]+=count;updated[total-value]+=count
    counts=updated
near('sign configuration DP weights',sum(counts.values()),4096)
tail_count=sum(count for total,count in counts.items() if abs(total)>=24)
near('sign tail DP count',r['sign_tail_count'],tail_count);near('sign tail count 16',tail_count,16)
near('sign exact probability',r['sign_p_two_sided'],tail_count/4096)
require('sign distribution symmetric',all(counts[t]==counts[-t] for t in counts))
near('sign zero expectation',sum(t*c for t,c in counts.items()),0)

coverage_rng=np.random.default_rng(r['coverage_seed']);samples=coverage_rng.normal(2,3,size=(40,12))
means=[sum(row)/12 for row in samples];halves=[critical*math.sqrt(sum((x-m)**2 for x in row)/11/12) for row,m in zip(samples,means)]
near('coverage means scalar calculation',r['coverage_means'],means)
near('coverage halfwidth scalar calculation',r['coverage_halfwidths'],halves)
near('coverage contains count',r['coverage_count'],sum(m-h<=2<=m+h for m,h in zip(means,halves)))
near('coverage count 39',r['coverage_count'],39)

def independent_power(count,delta):
    df=count-1;c=stats.t.ppf(.975,df);nc=delta*math.sqrt(count)/3
    def integrand(v):
        if v<=0:return 0
        chi=math.exp((df/2-1)*math.log(v)-v/2-(df/2)*math.log(2)-math.lgamma(df/2))
        cutoff=c*math.sqrt(v/df)
        return chi*(stats.norm.sf(cutoff-nc)+stats.norm.cdf(-cutoff-nc))
    return integrate.quad(integrand,0,np.inf,epsabs=1e-11)[0]
for count in [12,24,32,33,34,48]:near(f'power via normal/chi-square mixture n{count}',r['power_by_n'][str(count)],independent_power(count,1.5),2e-9)
near('null rejection probability',independent_power(12,0),.05,2e-9)
require('34 first integer reaches 80 percent',r['power_by_n']['33']<.8<r['power_by_n']['34'])
near('normal approximate sample size',r['sample_size_normal_approx'],(stats.norm.ppf(.975)+stats.norm.ppf(.8))**2*4)
near('20 independent null FWER',1-.95**20,.6415140775914581)

K,m,rho=r['cluster_K'],r['cluster_m'],r['cluster_rho']
block=(1-rho)*np.eye(m)+rho*np.ones((m,m));covariance=np.kron(np.eye(K),block)
near('cluster mean variance from full covariance',covariance.sum()/(K*m)**2,rho/K+(1-rho)/(K*m))
near('design effect',r['design_effect'],1+(m-1)*rho)
near('mean equivalent count',r['mean_equivalent_n'],K*m/r['design_effect'])
require('cluster covariance positive definite',np.linalg.eigvalsh(covariance).min()>0)

x=np.array(r['regression_x']);y=np.array(r['regression_y']);xc=x-45
slope=sum((x-x.mean())*(y-y.mean()))/sum((x-x.mean())**2);intercept=y.mean()-slope*xc.mean()
near('OLS coefficients via scalar centered sums',r['regression_coefficients'],[intercept,slope])
resid=y-intercept-slope*xc;rss=sum(resid**2);rs=math.sqrt(rss/(len(x)-2))
near('residual SD via scalar sum',r['regression_residual_sd'],rs)
near('residual mean orthogonal to intercept',sum(resid),0);near('residuals orthogonal to x',sum(resid*xc),0)
X=np.column_stack([np.ones(len(x)),xc]);x0=np.array([1,0])
h=x0@np.linalg.inv(X.T@X)@x0
near('leverage at mean x',h,1/len(x));require('prediction variance exceeds mean variance',rs*math.sqrt(1+h)>rs*math.sqrt(h))
f=((sum((y-y.mean())**2)-rss)/1)/(rss/(len(x)-2));slope_t=slope/(rs/math.sqrt(sum((x-x.mean())**2)))
near('nested model F equals slope t squared',f,slope_t**2)

for path in sorted((ROOT/'public/figures/mathematical-statistics').glob('*.svg')):
    require('SVG valid '+path.name,ET.parse(path).getroot().tag.endswith('svg'))
require('eight scientific figures',len(list((ROOT/'public/figures/mathematical-statistics').glob('*.svg')))==8)
thumb=ROOT/'public/figures/foundation-courses/mathematical-statistics.svg'
require('course sketch valid',ET.parse(thumb).getroot().tag.endswith('svg'))
result={'date':'2026-11-02','scope':'Independent numerical, distribution, unit and SVG checks; not a professional scientific review',
 'checks':len(checks),'passed':len(checks),'details':checks}
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(checks)} independent numerical/distribution/media checks passed')
