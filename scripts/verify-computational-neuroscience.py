"""Independent numerical/model/unit checks; not a review of biological truth."""
from pathlib import Path
import math
import cmath
import json
import xml.etree.ElementTree as ET
import numpy as np
from scipy import integrate, optimize, stats

ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/computational-neuroscience-2026-11-02'
r=json.loads((REC/'calculations.json').read_text(encoding='utf-8'));checks=[]
def near(name,a,b,tol=1e-10):
    np.testing.assert_allclose(a,b,atol=tol,rtol=0);checks.append(name)
def require(name,value):
    assert value,name;checks.append(name)

R,C=100e6,200e-12;EL,Vr,Vth=-.065,-.065,-.050;current=.2e-9;tau=R*C;steady=EL+R*current
near('SI RC time constant ms',r['tau_ms'],tau*1000)
near('SI resistance times current mV',R*current*1000,20)
near('steady membrane mV',r['steady_mV'],steady*1000)
near('threshold current nA',r['rheobase_nA'],(Vth-EL)/R*1e9)
cross=integrate.quad(lambda v:C/(current-(v-EL)/R),Vr,Vth,epsabs=1e-13)[0]
near('first crossing from separated ODE integral ms',r['first_spike_ms'],cross*1000)
def event(t,y):return y[0]-Vth
event.terminal=True;event.direction=1
def rhs(t,y):return [(-(y[0]-EL)/R+current)/C]
sol=integrate.solve_ivp(rhs,[0,.1],[Vr],events=event,rtol=1e-11,atol=1e-13,max_step=.0002)
near('independent numerical ODE event ms',sol.t_events[0][0]*1000,r['first_spike_ms'],2e-7)
near('period includes reset hold',r['period_ms'],(cross+.002)*1000)
near('steady rate reciprocal seconds',r['steady_rate_Hz'],1/(cross+.002))
near('five analytic event times',r['spike_times_ms'],[(cross+i*(cross+.002))*1000 for i in range(5)])
require('first event not delayed by initial refractory',r['first_spike_ms']<r['period_ms'])
near('one time constant fraction',1-math.exp(-1),.6321205588285577)
require('at rheobase subthreshold for any finite tested time',all(EL+(Vth-EL)*(1-math.exp(-t/tau))<Vth for t in [.001,.02,.2]))
near('stable Euler factor',abs(1-.001/tau),.95)
require('too large Euler step unstable',abs(1-.05/tau)>1)
for h in [.001,.0005]:
    v=Vr
    for _ in range(round(.02/h)):v+=h*rhs(0,[v])[0]
    exact=steady+(Vr-steady)*math.exp(-.02/tau)
    require(f'Euler error bounded h={h}',abs(v-exact)<.0002)

for item in r['shunt']:
    gi=item['gI_nS']*1e-9;gl,ge=10e-9,5e-9;ee,ei=0.,EL
    a=gl+ge+gi;b=gl*EL+ge*ee+gi*ei
    equilibrium=optimize.brentq(lambda v:b-a*v,-.1,.02)
    near(f'shunt KCL equilibrium gI{item["gI_nS"]}',item['steady_mV'],equilibrium*1000)
    near(f'shunt effective tau gI{item["gI_nS"]}',item['tau_ms'],C/a*1000)
    near(f'shunt current conservation gI{item["gI_nS"]}',gl*(equilibrium-EL)+ge*(equilibrium-ee)+gi*(equilibrium-ei),0,1e-20)
near('inhibition at reversal has zero current',10e-9*(EL-EL),0)
near('initial excitatory inward current pA',5e-9*(0-EL)*1e12,325)
near('one nS times one mV is one pA',1e-9*1e-3,1e-12,1e-25)
near('HH density conductance times voltage',1e-3*1e-3,1e-6,1e-18)
near('HH density capacitance times voltage derivative',1e-6*(1e-3/1e-3),1e-6,1e-18)
alpha,beta,x=.1,.2,.7
near('gate kinetic and relaxation forms agree',alpha*(1-x)-beta*x,((alpha/(alpha+beta))-x)/(1/(alpha+beta)))
require('gate fixed point in unit interval',0<alpha/(alpha+beta)<1)

expected=sum((end-start)*rate for start,end,rate in r['poisson_segments'])
near('piecewise intensity integral',r['poisson_expected_count'],expected)
weights=[math.exp(-expected)*expected**k/math.factorial(k) for k in range(60)]
near('Poisson mass normalization',sum(weights),1)
near('Poisson expected count finite sum',sum(k*p for k,p in enumerate(weights)),expected)
near('Poisson variance finite sum',sum((k-expected)**2*p for k,p in enumerate(weights)),expected)
mean_isi=integrate.quad(lambda t:t*40*math.exp(-40*t),0,np.inf)[0]
second_isi=integrate.quad(lambda t:t*t*40*math.exp(-40*t),0,np.inf)[0]
near('Poisson ISI mean integral',mean_isi,1/40)
near('Poisson ISI CV',math.sqrt(second_isi-mean_isi**2)/mean_isi,1)
near('at least one event probability is not mean count',1-math.exp(-.4),.3296799539643607)
require('finite bin may contain multiple events',1-math.exp(-.4)*(1+.4)>.06)
prng=np.random.default_rng(r['poisson_seed']);counts=[];bin_counts=[0]*25
for _ in range(r['poisson_trials']):
    row=[]
    for start,end,rate in r['poisson_segments']:
        count=prng.poisson((end-start)*rate);row.extend(prng.uniform(start,end,count))
    counts.append(len(row))
    require_range=all(0<=t<.25 for t in row)
    assert require_range
    for t in row:bin_counts[int(t/.01)]+=1
near('simulation counts independently regenerated',r['poisson_counts'],counts)
near('PSTH scalar event binning',r['psth_Hz'],np.array(bin_counts)/(200*.01))
near('PSTH integrated total per trial',sum(r['psth_Hz'])*.01,sum(counts)/200)
sample_mean=sum(counts)/len(counts);sample_var=sum((c-sample_mean)**2 for c in counts)/(len(counts)-1)
near('count mean scalar',r['poisson_count_mean'],sample_mean)
near('count variance scalar',r['poisson_count_variance'],sample_var)
near('empirical Fano scalar',r['poisson_fano'],sample_var/sample_mean)
require('finite sample Fano not forced to one',r['poisson_fano']!=1)

kernel=np.array(r['strf_kernel']);near('STRF kernel unit norm',sum(v*v for row in kernel for v in row),1)
require('STRF includes signed feature weights',kernel.min()<0<kernel.max())
grng=np.random.default_rng(r['glm_seed']);feature=grng.uniform(-1,1,4000);X=np.column_stack([np.ones(4000),feature]);dt=r['glm_dt_s']
y=grng.poisson(dt*np.exp(X@np.array([math.log(30),.8])));A=X[:2000];b=y[:2000]
w=np.array([math.log(b.mean()/dt),0.])
for _ in range(12):
    mu=dt*np.exp(A@w);score=A.T@(b-mu);information=A.T@(mu[:,None]*A)
    step=np.linalg.solve(information,score);w+=step
    if np.linalg.norm(step)<1e-13:break
near('GLM MLE via independent Newton score iterations',r['glm_fitted_coefficients'],w,2e-9)
near('GLM training score zero',A.T@(b-dt*np.exp(A@w)),[0,0],2e-9)
require('GLM information positive definite',np.linalg.eigvalsh(information).min()>0)
test=X[2000:];observed=y[2000:];mu=dt*np.exp(test@w);baseline=b.mean()
gain=sum(float(stats.poisson.logpmf(count,pred)-stats.poisson.logpmf(count,baseline)) for count,pred in zip(observed,mu))
near('GLM test likelihood gain via complete Poisson logpmf',r['glm_test_gain_nats'],gain,2e-9)
near('GLM test spikes',r['glm_test_spikes'],sum(observed))
near('GLM bits conversion',r['glm_test_gain_bits_per_spike'],gain/math.log(2)/sum(observed))
near('GLM baseline uses training data',r['glm_train_baseline_Hz'],sum(b)/(2000*dt))
def objective(v):return sum(dt*math.exp(a@v)-count*(a@v) for a,count in zip(A,b))
v=np.array([3.2,.6]);h=1e-5;finite=np.array([(objective(v+np.eye(2)[j]*h)-objective(v-np.eye(2)[j]*h))/(2*h) for j in range(2)])
near('GLM gradient finite difference',finite,A.T@(dt*np.exp(A@v)-b),2e-5)

pmf=lambda k,m:math.exp(-m)*m**k/math.factorial(k)
correct=sum(pmf(a,2)*pmf(b,.5)*(1 if a>b else .5 if a==b else 0) for a in range(31) for b in range(31))
near('two-neuron decoder accuracy via direct joint enumeration',r['population_optimal_accuracy'],correct)
near('decoder count means',np.array(r['population_rates_plus_Hz'])*r['population_window_s'],[2,.5])
lr_errors=[abs(math.log(pmf(a,2)*pmf(b,.5)/(pmf(a,.5)*pmf(b,2)))-(a-b)*math.log(4)) for a in range(5) for b in range(5)]
require('decoder log likelihood ratio algebra for all count pairs',max(lr_errors)<1e-12)
near('decoder equal evidence at tie',math.log(pmf(2,2)*pmf(2,.5)/(pmf(2,.5)*pmf(2,2))),0)

for index,item in enumerate(r['network']):
    W=np.array(item['W']);A=(W-np.eye(2))/r['network_tau_ms'];trace=float(np.trace(A));det=float(np.linalg.det(A))
    eig=np.array(item['eig_real_per_ms'])+1j*np.array(item['eig_imag_per_ms'])
    near(f'network {index} Jacobian',item['A_per_ms'],A)
    near(f'network {index} trace characteristic identity',sum(eig),trace)
    near(f'network {index} determinant characteristic identity',np.prod(eig),det)
    require(f'network {index} E/I source column convention',np.all(W[:,0]>0) and np.all(W[:,1]<0))
    disc=cmath.sqrt(trace*trace/4-det);time=100
    expA=cmath.exp(trace*time/2)*(cmath.cosh(disc*time)*np.eye(2)+cmath.sinh(disc*time)/disc*(A-trace/2*np.eye(2)))
    analytic=np.real_if_close(expA@np.array([1.,0.]));z=np.array([1.,0.]);h=.05
    for _ in range(round(time/h)):
        k1=A@z;k2=A@(z+h*k1/2);k3=A@(z+h*k2/2);k4=A@(z+h*k3);z+=h*(k1+2*k2+2*k3+k4)/6
    near(f'network {index} perturbation RK4 vs explicit 2x2 exponential',z,analytic,2e-9)
    near(f'network {index} norm vs generator matrix exponential',item['perturbation_norm_100ms'],np.linalg.norm(analytic),2e-10)
require('stable matrix eigenvalues negative real',max(r['network'][0]['eig_real_per_ms'])<0)
require('unstable matrix has positive real eigenvalue',max(r['network'][1]['eig_real_per_ms'])>0)
near('STDP positive 10 ms',r['stdp_plus_10ms'],.01/math.sqrt(math.e))
near('STDP negative 10 ms',r['stdp_minus_10ms'],-.012/math.sqrt(math.e))
near('unbounded illustrative weight at 300',.5+300*.01,3.5)
near('bounded illustrative weight at 300',min(1,max(0,.5+300*.01)),1)

vrng=np.random.default_rng(r['phase_seed'])
for item in r['phase_statistics']:
    sigma=item['jitter_sd_s'];errors=vrng.normal(0,sigma,2000);angles=2*np.pi*500*errors
    scalar=math.hypot(sum(math.cos(t) for t in angles),sum(math.sin(t) for t in angles))/len(angles)
    near(f'VS scalar circular mean sigma{sigma}',item['sample_vs'],scalar)
    c=2*math.pi*500*sigma
    real=integrate.quad(lambda z:math.cos(c*z)*math.exp(-z*z/2)/math.sqrt(2*math.pi),-10,10,epsabs=1e-13)[0]
    near(f'Gaussian jitter characteristic integral sigma{sigma}',item['population_vs_500Hz'],real)
    require(f'VS within unit interval sigma{sigma}',0<=scalar<=1)
    rotated=abs(np.exp(1j*(angles+1.23)).mean())
    near(f'VS invariant to common phase offset sigma{sigma}',scalar,rotated)
near('single event VS exactly one',abs(cmath.exp(.7j)),1)
near('four cardinal phases average to zero',abs(sum(cmath.exp(1j*p) for p in [0,math.pi/2,math.pi,3*math.pi/2])/4),0)
near('delay converts to 36 degrees',r['delay_degrees'],360*r['delay_s']*r['delay_reference_Hz'])
near('500 Hz period ms',1000/r['delay_reference_Hz'],2)
near('integer-period delay gives same phase',abs(cmath.exp(2j*math.pi*500*.0002)-cmath.exp(2j*math.pi*500*(.0002+.002))),0)

paths=sorted((ROOT/'public/figures/computational-neuroscience').glob('*.svg'))
near('nine scientific SVGs',len(paths),9)
for path in paths:require('valid SVG '+path.name,ET.parse(path).getroot().tag.endswith('svg'))
require('valid course sketch',ET.parse(ROOT/'public/figures/foundation-courses/computational-neuroscience.svg').getroot().tag.endswith('svg'))
report={'date':'2026-11-02','scope':'Independent unit, analytical/numerical model, probability, likelihood, stability, circular-statistic and SVG checks; not professional biological review','checks':len(checks),'passed':len(checks),'details':checks}
(REC/'numerical-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(checks)} independent numerical/model/unit/media checks passed')
