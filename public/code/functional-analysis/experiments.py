"""Specified ideal examples for Hearingpedia; not physical or clinical measurements.
Run: python experiments.py. Requires numpy, scipy.
"""
import json
import numpy as np
def ramp(t,n):
    return np.clip(n*(np.asarray(t)-.5),0,1)
def spike(t,n):
    return np.maximum(1-n*np.abs(np.asarray(t)-.5),0)
def signal(t):
    t=np.asarray(t)
    return np.sin(2*np.pi*t)+.4*np.cos(4*np.pi*t)+.2*np.sin(6*np.pi*t)
def projection(t):
    t=np.asarray(t)
    return np.sin(2*np.pi*t)+.4*np.cos(4*np.pi*t)
def green(x,xi):
    return np.minimum(x,xi)*(1-np.maximum(x,xi))
def weighted_adjoint():
    A=np.array([[1+1j,2],[-1j,.5]],dtype=complex)
    M=np.diag([2.,1.]);W=np.diag([1.,3.])
    return A,M,W,np.linalg.solve(M,A.conj().T@W)
def regularization(alpha=1e-4):
    n=np.arange(1,61);sigma=np.exp(-.15*n);truth=1/n**2
    eta=np.cos(1.7*n);eta*=.001/np.linalg.norm(eta);y=sigma*truth+eta
    raw=y/sigma;estimate=sigma*y/(sigma**2+alpha)
    return dict(n=n,sigma=sigma,truth=truth,eta=eta,y=y,raw=raw,estimate=estimate,alpha=alpha,
                raw_error=float(np.linalg.norm(raw-truth)),regularized_error=float(np.linalg.norm(estimate-truth)))
def galerkin(M):
    h=1/M;K=(2*np.eye(M-1)-np.eye(M-1,k=1)-np.eye(M-1,k=-1))/h
    load=np.full(M-1,h);ui=np.linalg.solve(K,load)
    x=np.linspace(0,1,M+1);u=np.r_[0,ui,0];slopes=np.diff(u)/h
    energy_error2=h*h/12
    J=.5*ui@K@ui-load@ui
    return dict(x=x,u=u,slopes=slopes,K=K,load=load,energy_error2=energy_error2,J=float(J),J_exact=-1/24)
def summary():
    r=regularization()
    return dict(projection=dict(signal_squared_norm=.6,projection_squared_norm=.58,residual_squared_norm=.02),
        ramp=dict(n=[4,8,32],L2_error2=[1/(3*n) for n in [4,8,32]]),
        spikes=dict(n=[4,16,64],L2_norm2=[2/(3*n) for n in [4,16,64]],peak=1),
        green=dict(operator_norm=1/np.pi**2,first_eigenvalues=(1/(np.pi*np.arange(1,6))**2).tolist()),
        regularization=dict(alpha=r['alpha'],noise_norm=float(np.linalg.norm(r['eta'])),sigma_min=float(r['sigma'][-1]),raw_error=r['raw_error'],regularized_error=r['regularized_error'],noise_gain_bound=1/(2*np.sqrt(r['alpha']))),
        galerkin=[dict(elements=M,energy_error2=galerkin(M)['energy_error2'],J=galerkin(M)['J']) for M in [4,8,16,32]])
if __name__=='__main__':print(json.dumps(summary(),ensure_ascii=True,indent=2))
