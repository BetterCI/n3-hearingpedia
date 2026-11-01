"""Independent mathematical checks against the specified models, not a biological review."""
from pathlib import Path
import importlib.util,json,math
import numpy as np
from scipy import integrate,optimize,special
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/machine-learning-2026-11-02'
C=json.loads((REC/'calculations.json').read_text(encoding='utf-8'));checks=[]
def check(name,condition,detail=None):
    if not bool(condition):raise AssertionError((name,detail))
    checks.append({'name':name,'passed':True,'detail':detail})
def close(name,a,b,atol=1e-9,rtol=1e-8):
    check(name,np.allclose(a,b,atol=atol,rtol=rtol),{'max_absolute_error':float(np.max(np.abs(np.asarray(a)-np.asarray(b))))})
# Ridge: independent augmented least squares and an unconstrained optimizer.
x=np.arange(-2.,3.);y=np.array([-3.8,-2.2,.2,1.8,4.]);n=5
close('centered feature and target',[sum(x),sum(y)],[0,0])
A=np.column_stack([np.ones(n),x]);aug=np.vstack([A,[0,np.sqrt(n)]]);target=np.r_[y,0]
beta=np.linalg.lstsq(aug,target,rcond=None)[0]
close('ridge augmented least squares',beta,[0,C['ridge']['ridge_slope']])
objective=lambda b:sum((A@b-y)**2)/(2*n)+b[1]**2/2
fit=optimize.minimize(objective,[.3,.5],method='BFGS',tol=1e-10)
close('ridge independent objective minimization',fit.x,beta,atol=1e-7)
close('ridge normal equation residual',A.T@(A@beta-y)/n+np.array([0,beta[1]]),[0,0])
close('OLS independent least squares',np.linalg.lstsq(A,y,rcond=None)[0],[0,C['ridge']['ols_slope']])
scaled=A.copy();scaled[:,1]*=1000
scaled_beta=np.linalg.lstsq(np.vstack([scaled,[0,np.sqrt(n)]]),target,rcond=None)[0]
check('same penalty after rescaling changes predictions',np.max(np.abs(A@beta-scaled@scaled_beta))>1)
values=19.6/(10+5*np.logspace(-5,4,50));check('ridge path shrinks monotonically',np.all(np.diff(values)<0))
# Population risk: independent Vandermonde least squares and adaptive scalar integration.
p=C['polynomial'];px=np.array(p['x']);py=np.array(p['y'])
for i,d in enumerate(p['degrees']):
    design=np.vander(px,d+1,increasing=True);coef=np.linalg.lstsq(design,py,rcond=None)[0]
    predict=lambda t:sum(float(a)*t**j for j,a in enumerate(coef))
    risk=integrate.quad(lambda t:(predict(t)-(1+.7*t-.9*t*t))**2,-1,1,epsabs=1e-9)[0]/2+.25**2
    close(f'degree {d} independent training MSE',np.mean((design@coef-py)**2),p['training_mse'][i],atol=1e-8)
    close(f'degree {d} independent population integral',risk,p['population_mse'][i],atol=1e-7)
check('nested polynomial training errors nonincreasing',np.all(np.diff(p['training_mse'])<1e-10))
check('quadratic beats degree12 in specified population',p['population_mse'][1]<p['population_mse'][11])
# Finite distribution bias/variance identity.
pred=np.array([.5,1.,1.4,2.1]);fstar=1.2;noise=np.array([-.3,.3])
direct=np.mean([(a-(fstar+e))**2 for a in pred for e in noise])
close('bias variance identity by enumeration',direct,(pred.mean()-fstar)**2+pred.var()+.09)
# Logistic independent Newton iteration, finite differences, test likelihood.
rng=np.random.default_rng(20261102);features=rng.normal(size=(600,2));X=np.column_stack([np.ones(600),features])
labels=rng.binomial(1,special.expit(-.3+1.1*features[:,0]-.8*features[:,1]))
Xt=X[:400];yt=labels[:400];lam=.05;pen=np.diag([0.,lam,lam])
def loss(b):
    z=Xt@b
    return np.mean(np.logaddexp(0,z)-yt*z)+b@pen@b/2
def grad(b):return Xt.T@(special.expit(Xt@b)-yt)/400+pen@b
b=np.zeros(3)
for _ in range(25):
    probs=special.expit(Xt@b);hess=Xt.T@((probs*(1-probs))[:,None]*Xt)/400+pen
    b-=np.linalg.solve(hess,grad(b))
close('Newton and BFGS logistic solutions',b,C['logistic']['coefficients'],atol=1e-7)
close('logistic gradient finite difference',optimize._numdiff.approx_derivative(lambda t:np.array([loss(t)]),[.2,-.1,.4]).ravel(),grad(np.array([.2,-.1,.4])),atol=1e-8)
check('regularized logistic Hessian positive definite',np.linalg.eigvalsh(hess).min()>0)
close('logistic first-order residual',grad(b),np.zeros(3),atol=1e-8)
test_p=special.expit(X[400:]@b)
direct_ll=-sum(math.log(float(q)) if yy else math.log1p(-float(q)) for q,yy in zip(test_p,labels[400:]))/200
close('test logloss direct Bernoulli likelihood',direct_ll,C['logistic']['test_log_loss'])
close('test threshold accuracy',sum(int(q>=.5)==yy for q,yy in zip(test_p,labels[400:]))/200,C['logistic']['test_accuracy'])
# Softmax: invariance, normalization, and score gradient.
scores=np.array([1.2,-.4,.8]);probs=special.softmax(scores);target_class=2
close('softmax normalization',sum(probs),1)
close('softmax additive invariance',special.softmax(scores+400),probs)
onehot=np.eye(3)[target_class]
close('softmax cross entropy score derivative',optimize._numdiff.approx_derivative(lambda z:np.array([special.logsumexp(z)-z[target_class]]),scores).ravel(),probs-onehot,atol=1e-8)
# One hidden layer tanh NN; finite differences for all parameters.
xi=np.array([.6,-.9]);w=np.array([[.4,-.7],[.2,.3]]);bias=np.array([.1,-.2]);v=np.array([.5,-.6]);c=.15;label=1
theta=np.r_[w.ravel(),bias,v,c]
def nn_loss(t):
    ww=t[:4].reshape(2,2);bb=t[4:6];vv=t[6:8];cc=t[8]
    z=vv@np.tanh(ww@xi+bb)+cc
    return np.logaddexp(0,z)-label*z
hidden=np.tanh(w@xi+bias);delta=special.expit(v@hidden+c)-label;da=delta*v*(1-hidden**2)
analytic=np.r_[np.outer(da,xi).ravel(),da,delta*hidden,delta]
numeric=optimize._numdiff.approx_derivative(lambda t:np.array([nn_loss(t)]),theta).ravel()
for j in range(9):close(f'NN chain rule parameter {j}',analytic[j],numeric[j],atol=1e-8)
# PCA: covariance eigenvalues rather than same SVD implementation.
data=np.array(C['pca']['data']);cov=np.cov(data,rowvar=False);ev,evec=np.linalg.eigh(cov);direction=evec[:,-1]
close('PCA eigenvalue variance ratio',ev[-1]/ev.sum(),C['pca']['first_variance_fraction'])
close('PCA retained axis up to sign',np.abs(direction),[1,0])
res=data-np.outer(data@direction,direction)
close('PCA per-entry reconstruction error',np.mean(res**2),.02)
close('PCA per-sample squared norm',np.mean(np.sum(res**2,axis=1)),.04)
for value in [-3,-1,1,3]:
    remaining=data[data[:,0]==value,1]
    check(f'projected x1={value} balanced labels',len(remaining)==2 and np.sum(remaining>0)==1)
check('low variance axis gives perfect labels',np.all((data[:,1]>0).astype(int)==C['pca']['labels']))
# Identity split: independent dictionary lookup and unseen-group majority.
rng=np.random.default_rng(20261103);tags=np.r_[rng.permutation(np.tile([0,1],10)),rng.permutation(np.tile([0,1],10))]
check('identity labels balanced in training half',sum(tags[:20])==10)
check('identity labels balanced in test half',sum(tags[20:])==10)
dictionary={i:int(t) for i,t in enumerate(tags)}
close('dictionary within identity accuracy',np.mean([dictionary[i]==tags[i] for i in range(40) for _ in range(2)]),C['identity_split']['within_identity_accuracy'])
close('unseen exact tie first-label accuracy',np.mean(tags[20:]==tags[0]),C['identity_split']['unseen_identity_accuracy'])
# Metrics via rational arithmetic and manual probability scores.
from fractions import Fraction
expected={'accuracy':Fraction(895,1000),'precision':Fraction(40,135),'recall':Fraction(40,50),'specificity':Fraction(855,950),
 'balanced_accuracy':Fraction(85,100),'f1':Fraction(80,185),'brier_08':Fraction(16,100),'brier_095':Fraction(1825,10000)}
for k,val in expected.items():close('metric '+k,C['metrics'][k],float(val))
for name,prob in [('08',.8),('095',.95)]:
    close('manual logloss '+name,C['metrics']['logloss_'+name],-.8*math.log(prob)-.2*math.log1p(-prob))
close('always negative accuracy',950/1000,.95)
# Cost threshold by direct decisions on a dense probability grid.
for fp,fn in [(1,1),(1,4),(8,2)]:
    ps=np.linspace(.0001,.9999,1001);threshold=fp/(fp+fn)
    close(f'Bayes decision cost threshold {fp},{fn}',np.where(ps>threshold,fp*(1-ps),fn*ps),np.minimum(fp*(1-ps),fn*ps))
# Attention: independent scalar dot products and row normalizer.
Q=np.array([[1.,0],[0,1]]);K=np.array([[1.,1],[-1,0],[.5,.2]]);V=np.array([[1.,2.,0],[0,1,2],[2,0,1]])
mask=np.array([[0,0,-np.inf],[0,0,0]])
attention=special.softmax(Q@K.T/np.sqrt(2)+mask,axis=1)
for i in range(2):
    weights=[math.exp(float(np.dot(Q[i],K[j])/math.sqrt(2)+mask[i,j])) for j in range(3)]
    manual=np.array(weights)/sum(weights)
    close(f'attention scalar normalization row{i}',attention[i],manual)
    close(f'attention row sum {i}',attention[i].sum(),1)
close('masked attention zero',attention[0,2],0)
check('attention output dimensions', (attention@V).shape==(2,3))
# SVG structural integrity and caption markup.
for path in sorted((ROOT/'public/figures/machine-learning').glob('*.svg')):
    root=ET.parse(path).getroot();check('SVG parse '+path.name,root.tag.endswith('svg'))
check('nine article figures',len(list((ROOT/'public/figures/machine-learning').glob('*.svg')))==9)
ET.parse(ROOT/'public/figures/foundation-courses/machine-learning.svg');check('course sketch XML',True)
result={'scope':'Independent checks of specified mathematics, synthetic examples and media structure; not biological validation or professional review.','total':len(checks),'passed':len(checks),'checks':checks}
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'total':len(checks),'passed':len(checks)},ensure_ascii=True))
