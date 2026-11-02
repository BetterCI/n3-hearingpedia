"""Small original deep-learning teaching models. No recordings, pretrained weights or participant data.
Run with Python 3.11+, NumPy and SciPy. Batch rows are examples; all random seeds fixed.
"""
import itertools
import numpy as np
from scipy.special import expit,logsumexp

def xor_representation(X):
    s=np.asarray(X).sum(-1)
    return np.maximum(s,0)-2*np.maximum(s-1,0)+np.maximum(s-2,0)

X_SMALL=np.array([[.2,-.4],[1.,.3],[-.5,.8]])
Y_SMALL=np.array([0.,1.,1.])
THETA_SMALL=np.array([.3,-.2,.5,.4,.1,-.1,.7,-.6,.05])

def binary_loss_grad(theta,X=X_SMALL,y=Y_SMALL):
    """2 -> tanh(2) -> binary logit; mean BCE, no regularizer. Nine parameters."""
    W=theta[:4].reshape(2,2);b=theta[4:6];v=theta[6:8];c=theta[8]
    h=np.tanh(X@W+b);z=h@v+c
    loss=np.mean(np.logaddexp(0,z)-y*z)
    delta=(expit(z)-y)/len(y);hidden=delta[:,None]*v[None,:]*(1-h*h)
    gradient=np.r_[(X.T@hidden).ravel(),hidden.sum(0),h.T@delta,delta.sum()]
    return float(loss),gradient

def masked_ce(logits,labels,valid):
    """Unweighted hard labels; mean over valid positions, not padded length."""
    assert logits.shape[:-1]==labels.shape==valid.shape and valid.any()
    z=logits[valid];y=labels[valid]
    return float(np.mean(logsumexp(z,axis=-1)-z[np.arange(len(y)),y]))

def normalize(X,axis,eps=1e-5):
    X=np.asarray(X,dtype=float)
    return (X-X.mean(axis=axis,keepdims=True))/np.sqrt(X.var(axis=axis,keepdims=True)+eps)

def causal_xcorr(x,k,dilation=1):
    """Deep-learning cross-correlation, oldest-to-newest kernel, left zero padding."""
    x=np.asarray(x,dtype=float);k=np.asarray(k,dtype=float);left=(len(k)-1)*dilation
    padded=np.pad(x,(left,0))
    return np.array([sum(k[j]*padded[t+j*dilation] for j in range(len(k))) for t in range(len(x))])

def receptive_field(kernels=(3,3,3),strides=(1,1,1),dilations=(1,2,4)):
    size=jump=1;history=[]
    for k,s,d in zip(kernels,strides,dilations):
        size+=(k-1)*d*jump;jump*=s;history.append((size,jump))
    return history

ATTENTION_X=np.array([[1.,0.],[0.,1.],[1.,1.],[-1.,1.]])
def attention(Q,K,V,allow=None):
    """Single head. True = allowed key; masks are combined before row softmax."""
    Q,K,V=map(lambda x:np.asarray(x,dtype=float),(Q,K,V))
    scores=Q@K.T/np.sqrt(Q.shape[-1])
    if allow is not None:
        assert allow.shape==scores.shape and np.all(allow.any(axis=-1)),'Every query needs an allowed key'
        scores=np.where(allow,scores,-np.inf)
    weights=np.exp(scores-logsumexp(scores,axis=-1,keepdims=True))
    return weights@V,weights

def collapse_ctc(path,blank=0):
    merged=[x for i,x in enumerate(path) if i==0 or x!=path[i-1]]
    return tuple(x for x in merged if x!=blank)

def ctc_enumerate(probs):
    totals={}
    for path in itertools.product(range(probs.shape[1]),repeat=len(probs)):
        label=collapse_ctc(path);mass=np.prod([probs[t,p] for t,p in enumerate(path)])
        totals[label]=totals.get(label,0.)+mass
    return totals

def ctc_forward(probs,target=(1,),blank=0):
    ext=[blank]
    for a in target:ext.extend([a,blank])
    old=np.zeros(len(ext));old[0]=probs[0,blank]
    if len(ext)>1:old[1]=probs[0,ext[1]]
    for t in range(1,len(probs)):
        new=np.zeros_like(old)
        for s,a in enumerate(ext):
            total=old[s]+(old[s-1] if s>0 else 0)
            if s>1 and a!=blank and a!=ext[s-2]:total+=old[s-2]
            new[s]=probs[t,a]*total
        old=new
    return float(old[-1]+(old[-2] if len(old)>1 else 0))

def target_function(x):return .7*np.sin(3*np.pi*x)

def regression_training(steps=12000,width=32,seed=20261102):
    """Full-batch Adam on a specified 1-hidden-layer tanh regression problem.
    This is an optimization/generalization example, not a claim that all networks are deep.
    The known toy population enables quadrature risk; checkpoint selection uses validation only.
    """
    rng=np.random.default_rng(seed);x=np.linspace(-1,1,18);y=target_function(x)+rng.normal(0,.25,len(x))
    xv=rng.uniform(-1,1,96);yv=target_function(xv)+rng.normal(0,.25,len(xv))
    nodes,weights=np.polynomial.legendre.leggauss(256)
    theta=np.r_[rng.normal(0,.5,width),np.zeros(width),rng.normal(0,.1,width),0.]
    first=np.zeros_like(theta);second=np.zeros_like(theta);records=[];snapshots=[]
    def forward_grad(theta,x,y=None):
        W=theta[:width];b=theta[width:2*width];v=theta[2*width:3*width];c=theta[-1]
        h=np.tanh(x[:,None]*W+b);pred=h@v+c
        if y is None:return pred
        delta=2*(pred-y)/len(y);dh=delta[:,None]*v*(1-h*h)
        grad=np.r_[(x[:,None]*dh).sum(0),dh.sum(0),h.T@delta,delta.sum()]
        return np.mean((pred-y)**2),grad
    for step in range(steps+1):
        loss,gradient=forward_grad(theta,x,y)
        if step%100==0 or step==steps:
            validation=np.mean((forward_grad(theta,xv)-yv)**2)
            population=.5*np.sum(weights*(forward_grad(theta,nodes)-target_function(nodes))**2)+.25**2
            records.append([step,loss,validation,population]);snapshots.append(theta.copy())
        if step==steps:break
        t=step+1;first=.9*first+.1*gradient;second=.999*second+.001*gradient**2
        theta-=.01*(first/(1-.9**t))/(np.sqrt(second/(1-.999**t))+1e-8)
    records=np.asarray(records);best=int(np.argmin(records[:,2]))
    return dict(records=records,best_index=best,best_theta=snapshots[best],final_theta=theta,x=x,y=y,xval=xv,yval=yv,width=width,seed=seed)

def diffusion_forward(length=512,steps=100,beta=.02,seed=20261102):
    t=np.arange(length)/length;x0=np.sin(2*np.pi*5*t)+.3*np.sin(2*np.pi*13*t)
    x0=(x0-x0.mean())/x0.std();x=x0.copy();rng=np.random.default_rng(seed);states={0:x.copy()}
    for step in range(1,steps+1):
        x=np.sqrt(1-beta)*x+np.sqrt(beta)*rng.normal(size=length)
        if step in [10,40,100]:states[step]=x.copy()
    return t,states

def calibration(T):
    logit=np.log(9)/np.asarray(T);prob=expit(logit)
    risk=np.logaddexp(0,logit)-.6*logit
    return prob,risk

if __name__=='__main__':
    loss,gradient=binary_loss_grad(THETA_SMALL)
    print('Small-network loss and gradient:',loss,gradient)
    P=np.tile([.4,.6],(3,1));print('CTC labels:',ctc_enumerate(P))
    print('CTC forward probability for a:',ctc_forward(P))
    T=np.log(9)/np.log(1.5);print('Temperature optimum, before/after:',T,calibration(1),calibration(T))
    train=regression_training();r=train['records'];print('Selected validation checkpoint:',r[train['best_index']]);print('Final checkpoint:',r[-1])
