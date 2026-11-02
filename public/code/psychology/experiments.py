"""Original toy examples. No participant data, diagnosis or fitted psychological parameters.
Python 3.11+, NumPy and SciPy. All seeds and model assumptions are explicit.
"""
import numpy as np
from scipy.special import expit,logit
from scipy.stats import norm

def psychometric(x,alpha=5.,beta=1.2,gamma=.5,lapse=.02):
    """lapse is the upper-asymptote deficit, not every definition of lapse rate."""
    return gamma+(1-gamma-lapse)*expit((np.asarray(x)-alpha)/beta)

def threshold(p=.75,alpha=5.,beta=1.2,gamma=.5,lapse=.02):
    assert gamma<p<1-lapse and beta>0
    return alpha+beta*logit((p-gamma)/(1-gamma-lapse))

def detection(k,d=1.5):
    """Noise N(0,1), signal N(d,1); respond yes iff evidence > k."""
    H,F=norm.sf(np.asarray(k)-d),norm.sf(k)
    return H,F,norm.ppf(H)-norm.ppf(F),-(norm.ppf(H)+norm.ppf(F))/2

def simpson():
    # Axis 0 = A/B training selection, axis 1 = quiet/noise context.
    successes=np.array([[81,1],[19,16]])
    totals=np.array([[90,10],[20,80]])
    return successes,totals,successes/totals,successes.sum(1)/totals.sum(1)

def rw_compound(pretraining=20,compound=15,rate=.2):
    """V_A and V_B, normalized outcome lambda=1; active cues update simultaneously."""
    A=B=0.;history=[(A,B)]
    for _ in range(pretraining):
        A+=rate*(1-A);history.append((A,B))
    for _ in range(compound):
        error=1-A-B
        A+=rate*error;B+=rate*error;history.append((A,B))
    return np.array(history)

def posterior(prior=.1,hit=.8,false_alarm=.2):
    return prior*hit/(prior*hit+(1-prior)*false_alarm)

def diffusion_decision(a,v=1.,s=1.,t0=.3):
    """dX=v dt+s dW, start 0, boundaries +-a, upper boundary correct, v>0.
    Return P(upper) and unconditional mean RT (decision plus nondecision time).
    a: evidence; v: evidence/s; s: evidence/sqrt(s); t0: s.
    """
    a=np.asarray(a)
    assert v>0 and s>0 and np.all(a>0)
    return expit(2*v*a/s**2),t0+(a/v)*np.tanh(a*v/s**2)

def retention(t):
    """Specified mathematical decay only; t in days, not a universal forgetting law."""
    return .15+.85*np.exp(-np.asarray(t)/2)

def overlap(delta=.5,sd=1.):
    return 2*norm.cdf(-abs(delta)/(2*sd))

def clustered_se(n,m=20,rho=.2,sd=1.):
    """Independent participants, exchangeable within-person correlation and equal m."""
    n=np.asarray(n,dtype=float)
    assert np.all(n>0) and m>=1 and 0<=rho<=1 and sd>0
    return sd*np.sqrt((rho+(1-rho)/m)/n),sd/np.sqrt(m*n)

if __name__=='__main__':
    print('75% threshold:',threshold())
    for k in [0.,.75,1.5]:print('k, H, F, dprime, c:',k,*detection(k))
    print('Within-context and pooled rates:',simpson()[2:])
    print('RW after 20 A+, 15 AB+:',rw_compound()[-1])
    print('P(A | cue):',posterior())
    print('DDM Pcorrect, mean RT:',diffusion_decision(np.array([.5,1.,2.])))
    print('Normal overlap:',overlap())
    print('Cluster-aware and naive SE:',clustered_se(50))
