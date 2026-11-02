"""Independent mathematical and numerical checks of specified teaching models, not a benchmark."""
from pathlib import Path
import importlib.util,sys,json,itertools,hashlib,xml.etree.ElementTree as ET
from fractions import Fraction as F
sys.dont_write_bytecode=True
import numpy as np
from scipy.integrate import quad
from scipy.optimize import linprog,minimize_scalar
from scipy.signal import correlate
from scipy.special import expit,logsumexp
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/deep-learning-2026-11-02'
spec=importlib.util.spec_from_file_location('m',ROOT/'public/code/deep-learning/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def record(name,**detail):checks.append(dict(check=name,result='passed',**detail))
def close(a,b,rtol=1e-8,atol=1e-10):assert np.allclose(a,b,rtol=rtol,atol=atol),(a,b)
rng=np.random.default_rng(9911)
# 1: All-affine composition is independently collapsed, including bias broadcasting.
X=rng.normal(size=(5,3));W1=rng.normal(size=(3,4));W2=rng.normal(size=(4,2));b1=rng.normal(size=4);b2=rng.normal(size=2)
close((X@W1+b1)@W2+b2,X@(W1@W2)+b1@W2+b2)
record('Affine composition and batch-row shape convention',batch=5,input=3,hidden=4,output=2)
# 2: Infeasible positive-margin affine XOR versus the exact nonlinear representation.
corners=np.array([[0.,0.],[0.,1.],[1.,0.],[1.,1.]]);labels=np.array([0,1,1,0]);sign=2*labels-1
fit=linprog(np.zeros(3),A_ub=-sign[:,None]*np.c_[corners,np.ones(4)],b_ub=-np.ones(4),bounds=[(None,None)]*3,method='highs')
assert fit.status==2;close(m.xor_representation(corners),labels)
record('XOR affine infeasibility and explicit nonlinear construction',nonlinear_probabilities=expit(8*labels-4).tolist())
# 3: Complex-step differentiation is independent of the analytic backward equations.
theta=m.THETA_SMALL;loss,g=m.binary_loss_grad(theta)
def complex_loss(t):
    h=np.tanh(m.X_SMALL@t[:4].reshape(2,2)+t[4:6]);z=h@t[6:8]+t[8]
    return np.mean(np.log(1+np.exp(z))-m.Y_SMALL*z)
cg=np.array([np.imag(complex_loss(theta.astype(complex)+1e-25j*e))/1e-25 for e in np.eye(9)])
fd=np.array([(complex_loss(theta+1e-5*e)-complex_loss(theta-1e-5*e))/2e-5 for e in np.eye(9)])
close(cg,g,atol=1e-13);close(fd,g,atol=1e-9)
record('Nine-parameter backprop versus complex-step and central differences',loss=loss,complex_step_max_error=float(np.max(abs(cg-g))),finite_difference_max_error=float(np.max(abs(fd-g))))
# 4: A mean of uniformly selected 2-example gradients equals the full 3-example gradient.
sub=[]
for pair in itertools.combinations(range(3),2):
    idx=list(pair);sub.append(m.binary_loss_grad(theta,m.X_SMALL[idx],m.Y_SMALL[idx])[1])
close(np.mean(sub,axis=0),g);close(sum(m.binary_loss_grad(theta,m.X_SMALL[[i]],m.Y_SMALL[[i]])[1] for i in range(3))/3,g)
record('Batch averaging and uniform minibatch-gradient expectation',batch_size=3,uniform_minibatch_size=2)
# 5: Stable CE, arbitrary padding, valid-position denominator, and logit-shift invariance.
z=np.array([[[2.,0.],[100.,-100.],[-100.,100.]],[[0.,2.],[2.,0.],[0.,2.]]]);y=np.array([[0,0,0],[1,0,1]])
valid=np.arange(3)[None,:]<np.array([1,3])[:,None];expected=np.log1p(np.exp(-2))
close(m.masked_ce(z,y,valid),expected)
changed=z.copy();changed[~valid]=rng.normal(size=(2,2))*1e3;close(m.masked_ce(changed,y,valid),expected)
close(m.masked_ce(z+1000,y,valid),expected,atol=1e-12);assert valid.sum()==4
close(expected*valid.sum()/valid.size,expected*2/3)
record('Masked CE stability and mean denominator',valid_positions=4,padded_positions=6,loss=expected)
# 6: Equal coefficients agree for identity SGD, not a general adaptive diagonal scale.
th=np.array([2.,1.]);gradient=np.array([.5,-.25]);eta=.1;lam=.2;D=np.array([1.,.1])
coupled=th-eta*D*(gradient+lam*th);decoupled=(1-eta*lam)*th-eta*D*gradient
close(coupled,[1.91,1.0005]);close(decoupled,[1.91,.9825]);assert not np.allclose(coupled,decoupled)
close(th-eta*(gradient+lam*th),(1-eta*lam)*th-eta*gradient)
record('L2 versus decoupled weight decay under a fixed diagonal preconditioner',coupled=coupled.tolist(),decoupled=decoupled.tolist())
# 7: Gaussian quadrature distinguishes ReLU second moment, mean and centered variance.
mean=quad(lambda z:z*np.exp(-z*z/2)/np.sqrt(2*np.pi),0,np.inf,epsabs=1e-12)[0]
second=quad(lambda z:z*z*np.exp(-z*z/2)/np.sqrt(2*np.pi),0,np.inf,epsabs=1e-12)[0]
close(mean,1/np.sqrt(2*np.pi));close(second,.5);assert not np.isclose(second-mean**2,.5)
close(32*(2/32)*second,1)
record('ReLU moments and He forward scaling assumptions',mean=mean,second_moment=second,centered_variance=second-mean**2)
# 8: Finite differences of a residual block and its exact cancellation counterexample.
A=np.diag([-.5,.01]);h=np.array([.4,-.2]);eps=1e-5
J=np.column_stack([((h+eps*e+A@(h+eps*e))-(h-eps*e+A@(h-eps*e)))/(2*eps) for e in np.eye(2)])
close(J,np.eye(2)+A);close(np.eye(2)-np.eye(2),np.zeros((2,2)))
close(.5**100,7.888609052210118e-31,atol=1e-40)
record('Residual Jacobian, cancellation and fixed scalar products',gain_half_100=.5**100,gain_1p01_100=1.01**100)
# 9: Verify axes and companion-sample dependence through exact batch statistics.
batch=np.array([[1.,4.],[3.,8.],[5.,6.]]);altered=batch.copy();altered[-1]=[50,60]
close(m.normalize(batch,0)[0],np.array([-2.,-2.])/np.sqrt(8/3+1e-5))
close(m.normalize(batch,1)[0],[-1.5,1.5]/np.sqrt(2.25+1e-5))
assert not np.allclose(m.normalize(batch,0)[0],m.normalize(altered,0)[0]);close(m.normalize(batch,1)[0],m.normalize(altered,1)[0])
record('BatchNorm-like versus LayerNorm-like statistic axes',batch_other_sample_changes_first=True,per_sample_other_sample_changes_first=False,eps=1e-5)
# 10: Exhaustive dropout masks: exact first/second moments and a nonlinear counterexample.
activation=np.array([1.,2.,3.]);mask=np.array(list(itertools.product([0,1],repeat=3)));outputs=mask*activation/.5
close(outputs.mean(0),activation);close(outputs.var(0),activation**2)
nonlinear=(expit(0)+expit(2))/2;assert abs(nonlinear-expit(1))>.04
record('Inverted-dropout moments and nonlinear non-equivalence',sigmoid_random_mean=float(nonlinear),sigmoid_of_mean=float(expit(1)))
# 11: Independent SciPy correlation, including asymmetric kernel and dilation.
x=rng.normal(size=17);kernel=np.array([1.,-2.,.5])
for d in [1,2,3]:
    expanded=np.zeros((len(kernel)-1)*d+1);expanded[::d]=kernel
    expected=correlate(np.pad(x,(len(expanded)-1,0)),expanded,mode='valid')
    close(m.causal_xcorr(x,kernel,d),expected)
record('Causal cross-correlation versus independent signal implementation',kernel=kernel.tolist(),dilations=[1,2,3])
# 12: A future perturbation cannot affect a causal prefix; centered filtering can.
imp=np.zeros(41);imp[20]=1
assert np.all(m.causal_xcorr(imp,[.25,.5,.25])[:20]==0)
assert np.convolve(imp,[.25,.5,.25],'same')[19]>.2
record('Future-dependence counterexample for centered filters',first_causal_response=20,first_centered_response=19)
# 13: Receptive field by enumerating reachable input offsets rather than the size recurrence.
offsets={0};sizes=[];jump=1
for k,s,d in zip([3,3,3],[1,1,1],[1,2,4]):
    offsets={a+j*d*jump for a in offsets for j in range(k)};jump*=s;sizes.append(max(offsets)-min(offsets)+1)
assert offsets==set(range(15));assert sizes==[3,7,15]==[x[0] for x in m.receptive_field()]
record('Receptive field by exact reachable offsets',sizes=sizes)
# 14: Rational arithmetic on all eight CTC paths.
rational={}
for path in itertools.product([0,1],repeat=3):
    mass=np.prod([F(2,5) if v==0 else F(3,5) for v in path]);label=m.collapse_ctc(path);rational[label]=rational.get(label,F(0))+mass
assert rational=={():F(8,125),(1,):F(99,125),(1,1):F(18,125)}
assert m.collapse_ctc([1,0,1])==(1,1) and m.collapse_ctc([1,1,1])==(1,)
greedy_counter=m.ctc_enumerate(np.tile([.6,.4],(2,1)));close(greedy_counter[()],.36);close(greedy_counter[(1,)],.64)
assert m.collapse_ctc(np.argmax(np.tile([.6,.4],(2,1)),axis=1))==()
record('CTC exact fractions, collapse order and greedy counterexample',empty=float(rational[()]),a=float(rational[(1,)]),aa=float(rational[(1,1)]),two_frame_greedy_empty_probability=.36,two_frame_a_probability=.64)
# 15: General DP agrees with brute force for nonhomogeneous three-symbol distributions.
cases=0
for T in [1,2,3,4]:
    probs=rng.uniform(.1,1,(T,3));probs/=probs.sum(1,keepdims=True)
    all_labels=m.ctc_enumerate(probs);close(sum(all_labels.values()),1)
    for label,mass in all_labels.items():close(m.ctc_forward(probs,label),mass);cases+=1
close(m.ctc_forward(np.tile([.4,.6],(3,1))),.792)
record('CTC forward dynamic programming versus exhaustive path sums',label_cases=cases)
# 16: Cross-attention dimensions, row normalization and row-constant score invariance.
Q=rng.normal(size=(3,2));K=rng.normal(size=(5,2));V=rng.normal(size=(5,4));out,weights=m.attention(Q,K,V)
assert out.shape==(3,4) and weights.shape==(3,5);close(weights.sum(1),1);assert np.all(weights>=0)
shifted=m.attention(Q,K+[5,-2],V);close(out,shifted[0]);close(weights,shifted[1])
record('Cross-attention dimensions and softmax shift invariance',query_positions=3,key_positions=5,key_width=2,value_width=4)
# 17: Prefix invariance under nonfuture masks and an explicit all-masked guard.
X=m.ATTENTION_X;Y=X.copy();Y[-1]=[6,-5];allow=np.tril(np.ones((4,4),bool))
prefix=m.attention(X,X,X,allow)[0][:3];changed=m.attention(Y,Y,Y,allow)[0][:3];close(prefix,changed)
full_change=float(np.max(abs(m.attention(X,X,X)[0][:3]-m.attention(Y,Y,Y)[0][:3])));assert full_change>5
bad=allow.copy();bad[0]=False
try:m.attention(X,X,X,bad)
except AssertionError:pass
else:raise AssertionError('All-masked query was not rejected')
record('Attention causal prefix and empty-mask guard',causal_prefix_max_change=float(np.max(abs(prefix-changed))),full_prefix_max_change=full_change)
# 18: Pure unpositioned full self-attention is permutation equivariant in this example.
perm=[2,0,3,1];close(m.attention(X[perm],X[perm],X[perm])[0],m.attention(X,X,X)[0][perm])
record('Unpositioned self-attention permutation equivariance',position_information_absent=True,mask_absent=True)
# 19: Independently reconstruct initial data and finite-difference the regression network.
seed=20261102;rr=np.random.default_rng(seed);width=32;trainx=np.linspace(-1,1,18);trainy=.7*np.sin(3*np.pi*trainx)+rr.normal(0,.25,18)
valx=rr.uniform(-1,1,96);valy=.7*np.sin(3*np.pi*valx)+rr.normal(0,.25,96)
init=np.r_[rr.normal(0,.5,width),np.zeros(width),rr.normal(0,.1,width),0.]
def predict(theta,x):return np.tanh(x[:,None]*theta[:width]+theta[width:2*width])@theta[2*width:3*width]+theta[-1]
def trainloss(theta):return np.mean((predict(theta,trainx)-trainy)**2)
eps=1e-5;rg=np.array([(trainloss(init+eps*e)-trainloss(init-eps*e))/(2*eps) for e in np.eye(len(init))])
expected=init-.01*rg/(np.abs(rg)+1e-8);one=m.regression_training(steps=1)['final_theta'];close(one,expected,atol=2e-8)
record('First Adam step versus finite-difference regression gradient',parameters=len(init),max_parameter_error=float(np.max(abs(one-expected))))
# 20: Known population risk by adaptive quadrature, independent of Gauss-Legendre summation.
training=m.regression_training();records=training['records'];best=training['best_index'];assert best==int(np.argmin(records[:,2]))
errors=[]
for i,theta in [(best,training['best_theta']),(-1,training['final_theta'])]:
    close(trainloss(theta),records[i,1]);close(np.mean((predict(theta,valx)-valy)**2),records[i,2])
    population=.5*quad(lambda x:(float(predict(theta,np.array([x]))[0])-.7*np.sin(3*np.pi*x))**2,-1,1,epsabs=1e-11,limit=200)[0]+.0625
    errors.append(abs(population-records[i,3]));close(population,records[i,3],atol=1e-8)
assert records[-1,1]<records[best,1] and records[-1,3]>records[best,3]
record('Validation selection and independent population-risk quadrature',selected_step=int(records[best,0]),selected=records[best].tolist(),final=records[-1].tolist(),max_population_error=max(errors))
# 21: A direct weighted-noise formula independently checks the forward Markov chain.
t,states=m.diffusion_forward();noise=np.random.default_rng(seed).normal(size=(100,512));initial=states[0]
close(initial.mean(),0);close(np.mean(initial**2),1)
for step in [10,40,100]:
    coefficients=np.sqrt(.02)*np.sqrt(.98)**np.arange(step-1,-1,-1)
    direct=np.sqrt(.98)**step*initial+coefficients@noise[:step]
    close(direct,states[step],atol=1e-13);close(coefficients@coefficients,1-.98**step)
record('Forward diffusion direct Gaussian combination versus recurrence',alpha_bar={str(i):.98**i for i in [10,40,100]},only_forward_chain=True)
# 22: Scalar optimization and Bernoulli entropy independently identify the optimum temperature.
opt=minimize_scalar(lambda T:float(m.calibration(T)[1]),bounds=(.1,20),method='bounded',options={'xatol':1e-10})
analytic=np.log(9)/np.log(1.5);close(opt.x,analytic,atol=2e-7)
entropy=-.6*np.log(.6)-.4*np.log(.4);close(m.calibration(analytic)[1],entropy)
assert all(float(m.calibration(T)[0])>.5 for T in [.5,1,analytic,10])
record('Temperature optimum and exact population cross entropy',optimal_temperature=analytic,risk_before=float(m.calibration(1)[1]),risk_after=float(entropy),unchanged_expected_accuracy=.6)
# 23: Source identity and accessible text; no source figures reused.
rows=json.loads((REC/'source-index.json').read_text(encoding='utf-8'));assert len(rows)==27 and len({r['id'] for r in rows})==27
for row in rows:
    assert row['status']=='fetched'
    p=ROOT/'artifacts/deep-learning/sources'/(row['id']+('.pdf' if row['kind']=='original_paper' else '.html'))
    assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],row['id']
record('Primary source file identities',sources=27,author_textbook_chapters=13,original_papers=11,official_documentation=3)
# 24: SVG structural completeness, including the taller 2x2 diffusion figure.
figures=list((ROOT/'public/figures/deep-learning').glob('*.svg'));assert len(figures)==10
for p in figures:
    expected='0 0 1008 576' if p.stem=='diffusion-forward' else '0 0 1008 396'
    assert ET.parse(p).getroot().attrib['viewBox']==expected,p.name
assert ET.parse(ROOT/'public/figures/foundation-courses/deep-learning.svg').getroot().attrib['viewBox']=='0 0 320 180'
record('Scientific SVG and course sketch structure',scientific_figures=10,course_sketches=1)
result=dict(status='passed',check_groups=len(checks),checks=checks,scope='Specified teaching mathematics, implementation and file identities; not participant validation, benchmark reproduction or external professional review')
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status='passed',check_groups=len(checks),complex_step_gradient_error=float(np.max(abs(cg-g))),known_population_quadrature_error=max(errors))))
