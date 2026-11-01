"""Original synthetic demonstrations. NumPy/SciPy; no recordings or clinical data.
Run: python experiments.py
Loss conventions are defined in the article; no scikit-learn dependency required.
"""
import numpy as np
from scipy.optimize import minimize
from scipy.special import expit

def ridge_example():
    x=np.array([-2.,-1.,0.,1.,2.]);y=np.array([-3.8,-2.2,.2,1.8,4.])
    n=len(x);lam=1.
    # x and y are centered; the intercept is zero and unpenalized.
    slope=(x@y)/(x@x+n*lam)
    return {'ols_slope':float((x@y)/(x@x)),'ridge_slope':float(slope),'lambda':lam}

def logistic_example():
    rng=np.random.default_rng(20261102)
    x=rng.normal(size=(600,2));design=np.column_stack([np.ones(len(x)),x])
    y=rng.binomial(1,expit(-.3+1.1*x[:,0]-.8*x[:,1]))
    train=np.arange(400);test=np.arange(400,600);lam=.05
    def objective(beta):
        z=design[train]@beta
        return np.mean(np.logaddexp(0,z)-y[train]*z)+lam/2*(beta[1:]@beta[1:])
    def gradient(beta):
        return design[train].T@(expit(design[train]@beta)-y[train])/len(train)+lam*np.r_[0.,beta[1:]]
    fit=minimize(objective,np.zeros(3),jac=gradient,method='BFGS',options={'gtol':1e-9})
    assert fit.success or np.linalg.norm(gradient(fit.x))<1e-7
    z=design[test]@fit.x
    return {'coefficients':fit.x.tolist(),'test_log_loss':float(np.mean(np.logaddexp(0,z)-y[test]*z)),
            'test_accuracy':float(np.mean((z>=0)==y[test])),'gradient_norm':float(np.linalg.norm(gradient(fit.x)))}

def pca_example():
    data=np.array([(a,b) for a in [-3.,-1.,1.,3.] for b in [-.2,.2]])
    centered=data-data.mean(axis=0)
    _,s,vt=np.linalg.svd(centered,full_matrices=False)
    projection=centered@vt[:1].T@vt[:1]
    return {'data':data.tolist(),'first_variance_fraction':float(s[0]**2/np.sum(s*s)),
            'reconstruction_mse_per_entry':float(np.mean((centered-projection)**2)),
            'labels':(data[:,1]>0).astype(int).tolist()}

def identity_split_example():
    rng=np.random.default_rng(20261103)
    labels=np.r_[rng.permutation(np.tile([0,1],10)),rng.permutation(np.tile([0,1],10))]
    groups=np.repeat(np.arange(40),6);take=np.tile(np.arange(6),40)
    x=np.eye(40)[groups];y=labels[groups]
    def score(train,test):
        d2=np.sum((x[test,None,:]-x[train][None,:,:])**2,axis=2)
        # Exact ties are broken by the first training row.
        pred=y[train][np.argmin(d2,axis=1)]
        return float(np.mean(pred==y[test]))
    return {'within_identity_accuracy':score(np.flatnonzero(take<4),np.flatnonzero(take>=4)),
      'unseen_identity_accuracy':score(np.flatnonzero(groups<20),np.flatnonzero(groups>=20)),
      'identities':40,'repeats':6}

def metrics_example():
    tp,fn,fp,tn=40,10,95,855
    y=np.r_[np.ones(80),np.zeros(20)]
    return {'accuracy':(tp+tn)/(tp+fn+fp+tn),'precision':tp/(tp+fp),'recall':tp/(tp+fn),
       'specificity':tn/(tn+fp),'balanced_accuracy':.5*(tp/(tp+fn)+tn/(tn+fp)),
       'f1':2*tp/(2*tp+fp+fn),'brier_08':float(np.mean((.8-y)**2)),
       'brier_095':float(np.mean((.95-y)**2)),
       'logloss_08':float(-np.mean(y*np.log(.8)+(1-y)*np.log(.2))),
       'logloss_095':float(-np.mean(y*np.log(.95)+(1-y)*np.log(.05)))}

if __name__=='__main__':
    import json
    print(json.dumps({name:fn() for name,fn in [('ridge',ridge_example),('logistic',logistic_example),
      ('pca',pca_example),('identity_split',identity_split_example),('metrics',metrics_example)]},indent=2))
