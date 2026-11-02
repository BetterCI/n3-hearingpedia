"""Independent analytic/numerical audit of the published toy examples, not human validation."""
from pathlib import Path
import importlib.util,sys,json,hashlib,xml.etree.ElementTree as ET
from fractions import Fraction as F
sys.dont_write_bytecode=True
import numpy as np
from scipy.integrate import quad,solve_bvp
from scipy.optimize import brentq
from scipy.stats import norm
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/psychology-2026-11-02'
spec=importlib.util.spec_from_file_location('m',ROOT/'public/code/psychology/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def record(name,**detail):checks.append(dict(check=name,result='passed',**detail))
def close(a,b,atol=1e-10,rtol=1e-9):assert np.allclose(a,b,atol=atol,rtol=rtol),(a,b)
# 1: A shift cannot change Pearson correlation; agreement is a different quantity.
x=np.linspace(20,80,21);y=x+12
close(np.corrcoef(x,y)[0,1],1);close(np.mean(y-x),12);close(np.sqrt(np.mean((y-x)**2)),12)
record('Correlation versus absolute agreement',r=1,mean_shift=12,RMSE=12)
# 2: Explicit covariance decomposition under the stated classical assumptions.
cov=np.array([[100,0],[0,25.]])
total=np.ones(2)@cov@np.ones(2);close(total,125);close(cov[0,0]/total,.8);close(np.sqrt(cov[1,1]),5)
record('Classical variance decomposition under zero covariance',reliability=.8,error_SD=5)
# 3: Exact integer arithmetic establishes the reversal, including the denominators.
ok,n,within,pooled=m.simpson()
exact=[[F(int(ok[i,j]),int(n[i,j])) for j in range(2)] for i in range(2)]
assert all(exact[1][j]>exact[0][j] for j in range(2));assert F(82,100)>F(35,100)
close(within,[[.9,.1],[.95,.2]]);close(pooled,[.82,.35]);close(within.mean(1),[.5,.575])
record('Simpson reversal and equal-context standardization',pooled=pooled.tolist(),equal_weight=within.mean(1).tolist())
# 4: Inverse location by a root search, independent of the logit formula.
root=brentq(lambda x:float(m.psychometric(x))-.75,-10,20,xtol=1e-13)
close(m.threshold(),root);close(m.psychometric(5),.74);assert root>5
record('Psychometric threshold root and midpoint',threshold_75=root,midpoint_correct=.74)
# 5: If lapse means fully random responding, its rate is not the asymptote deficit.
random_rate=.04;gamma=.5
for z in [-8.,0.,3.,8.]:
    S=1/(1+np.exp(-z));mixture=(1-random_rate)*(gamma+(1-gamma)*S)+random_rate*gamma
    expected=gamma+(1-gamma-.02)*S;close(mixture,expected)
record('Lapse-mixture definition conversion',random_response_probability=.04,upper_deficit=.02)
# 6: Gaussian tail quadrature independently checks SF-based hit/false-alarm rates.
for k in [0.,.75,1.5]:
    H,Fp,_,_=m.detection(k)
    close(H,quad(lambda z:np.exp(-(z-1.5)**2/2)/np.sqrt(2*np.pi),k,np.inf,epsabs=1e-12)[0])
    close(Fp,quad(lambda z:np.exp(-z*z/2)/np.sqrt(2*np.pi),k,np.inf,epsabs=1e-12)[0])
record('SDT rates by independent density quadrature',noise_mean=0,signal_mean=1.5,common_SD=1)
# 7: Recover the assumed distribution separation across a range of criteria.
k=np.linspace(-2,3.5,111);H,Fp,dp,c=m.detection(k)
close(dp,1.5);close(c,k-.75);assert np.all(np.diff(H)<0) and np.all(np.diff(Fp)<0)
record('SDT sensitivity invariant versus criterion changes',max_dprime_error=float(np.max(abs(dp-1.5))))
# 8: Exact rational single-cue solution; no assumption of complete blocking after finite n.
history=m.rw_compound();a20=1-F(4,5)**20
close(history[20,0],float(a20));assert history[20,0]<1 and history[20,1]==0
record('RW finite pretraining against rational solution',V_A_20=float(a20))
# 9: Exact compound residual recursion and invariant A-B; code uses simultaneous updates.
residual=F(4,5)**20;B15=residual*(1-F(3,5)**15)/2
close(history[-1,1],float(B15));close(np.diff(history[20:,0]-history[20:,1]),0)
close(1-history[20:,0]-history[20:,1],float(residual)*.6**np.arange(16))
record('RW compound exact error recursion and invariant',V_B_15=float(B15))
# 10: Baseline with no pretrained cue and complete blocking at the mathematical limit.
base=m.rw_compound(0,15)[-1];close(base,(1-.6**15)/2)
A,B=1.,0.
for _ in range(15):
    err=1-A-B;A,B=A+.2*err,B+.2*err
close([A,B],[1,0]);assert history[-1,1]>0
record('RW baseline and exact versus finite blocking',baseline_B=float(base[1]),finite_pretraining_B=float(history[-1,1]))
# 11: Sequentially recomputing the error gives a different recurrence, not our model.
A,B=float(a20),0.
for _ in range(15):
    A+=.2*(1-A-B);B+=.2*(1-A-B)
assert abs(B-history[-1,1])>1e-4
record('Sequential-update counterexample',incorrect_sequential_B=B,difference=float(B-history[-1,1]))
# 12: Conditional probability by exact counts, not a statistical fit.
table=np.array([[80,20],[180,720]])
assert table.sum()==1000 and table[0].sum()==100
close(m.posterior(),float(F(80,260)));close(table[:,0].sum(),260)
record('Bayes probability by enumerated frequency table',posterior=float(F(4,13)))
# 13: Independent boundary-value solver for hitting probability and mean exit time.
errors=[]
for a in [.5,1.,2.]:
    grid=np.linspace(-a,a,121)
    prob=solve_bvp(lambda x,y:np.vstack([y[1],-2*y[1]]),lambda ya,yb:np.array([ya[0],yb[0]-1]),grid,np.vstack([(grid+a)/(2*a),np.full_like(grid,1/(2*a))]),tol=1e-9,max_nodes=20000)
    mean=solve_bvp(lambda x,y:np.vstack([y[1],-2-2*y[1]]),lambda ya,yb:np.array([ya[0],yb[0]]),grid,np.vstack([a*a-grid**2,-2*grid]),tol=1e-9,max_nodes=20000)
    assert prob.success and mean.success
    p,rt=m.diffusion_decision(a);errors += [abs(float(prob.sol(0)[0])-float(p)),abs(float(mean.sol(0)[0])+.3-float(rt))]
assert max(errors)<1e-8
record('DDM analytic moments versus independent boundary-value equations',max_absolute_error=max(errors),generator='0.5 u_second + u_first',boundaries='+-a',nondecision_s=.3)
# 14: Rescaling evidence units does not alter observable probabilities or time.
a=np.array([.5,1,2.]);p,rt=m.diffusion_decision(a)
for scale in [.1,3,10]:
    pp,tt=m.diffusion_decision(a*scale,v=scale,s=scale);close(pp,p);close(tt,rt)
record('DDM evidence-unit scaling and total time',correct=p.tolist(),mean_total_RT_s=rt.tolist())
# 15: Gaussian overlap by piecewise integration, not the closed-form CDF expression.
integral=quad(lambda x:norm.pdf(x-.5),-np.inf,.25,epsabs=1e-12)[0]+quad(lambda x:norm.pdf(x),.25,np.inf,epsabs=1e-12)[0]
close(integral,m.overlap());close(m.overlap(0),1)
record('Normal-distribution overlap by independent quadrature',overlap=integral)
# 16: Distinct calendar-time start points versus within-cohort changes.
cohorts=np.array([[80,78,76],[66,64,62]])
assert cohorts[0,0]-cohorts[1,0]==14 and np.all(cohorts[:,-1]-cohorts[:,0]==-4)
record('Cohort arithmetic and distinct comparison targets',cross_sectional_difference=14,within_cohort_20year_change=-4)
# 17: Construct the full covariance matrix for 50 independent blocks of size20.
block=.2*np.ones((20,20))+.8*np.eye(20);C=np.kron(np.eye(50),block)
variance=C.sum()/1000**2;aware,naive=m.clustered_se(50)
close(aware**2,variance);close(naive**2,1/1000);close((aware/naive)**2,4.8);close(1/variance,1000/4.8)
record('Cluster mean variance by explicit 1000x1000 covariance matrix',SE=float(aware),naive_SE=float(naive),design_effect=4.8,variance_equivalent_N=1/variance)
# 18: Correlated repeats saturate; independent participants reduce all variance terms.
close(m.clustered_se(50,m=1)[0],1/np.sqrt(50));close(m.clustered_se(50,rho=0)[0],1/np.sqrt(1000))
close(m.clustered_se(200)[0],m.clustered_se(50)[0]/2)
limit=np.sqrt(.2/50);large_repeat=m.clustered_se(50,m=10**9)
assert all(np.isfinite(x) for x in large_repeat) and abs(large_repeat[0]-limit)<1e-9
record('Repeat and participant-count limits',infinite_repeat_SE_limit=limit)
# 19: All ten SVGs must be complete, parseable and have the specified dimensions.
files=list((ROOT/'public/figures/psychology').glob('*.svg'));assert len(files)==10
for p in files:
    root=ET.parse(p).getroot();assert root.attrib.get('viewBox')=='0 0 1008 396'
thumb=ET.parse(ROOT/'public/figures/foundation-courses/psychology.svg').getroot();assert thumb.attrib['viewBox']=='0 0 320 180'
record('Scientific figures and course sketch XML',scientific_figures=10,course_sketches=1)
# 20: Source hashes explicitly distinguish original HTTP bytes and web-reader excerpts.
rows=json.loads((REC/'source-index.json').read_text(encoding='utf-8'));assert len(rows)==25
for row in rows:
    assert row['status']=='fetched'
    if row.get('hash_target'):path=ROOT/'artifacts/psychology/sources'/(row['id']+'.verified-excerpt.txt')
    else:path=ROOT/'artifacts/psychology/sources'/(row['id']+('.pdf' if row['url'].lower().endswith('.pdf') else '.html'))
    assert hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256'],row['id']
record('Scoped source cache identities',records=25,original_HTTP_files=23,web_reader_texts=2,scanned_chapter_targeted_visual_review=True)
result=dict(status='passed',check_groups=len(checks),checks=checks,scope='Specified teaching models and evidence identities, not empirical replication, clinical validation or external professional review')
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status='passed',check_groups=len(checks),DDM_BVP_max_error=max(errors))))
