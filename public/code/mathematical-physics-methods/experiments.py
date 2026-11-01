"""Original specified ideal models for Hearingpedia, not measured biological/device data.
Run: python experiments.py. Dependencies: numpy, scipy. SI units unless noted.
"""
import json
import numpy as np
from scipy.special import jn_zeros

def pluck_coeff(n,L=1.,a=.3,A=.001):
    n=np.asarray(n,dtype=float)
    return 2*A*L**2*np.sin(n*np.pi*a/L)/(np.pi**2*n*n*a*(L-a))

def pluck_shape(x,L=1.,a=.3,A=.001):
    x=np.asarray(x)
    return np.where(x<=a,A*x/a,A*(L-x)/(L-a))

def green(x,xi,L=1.):
    return np.minimum(x,xi)*(L-np.maximum(x,xi))/L

def heat_wave(x,t,D=.1,c=1.,L=1.):
    first=np.sin(np.pi*x/L)
    third=.4*np.sin(3*np.pi*x/L)
    heat=first*np.exp(-D*(np.pi/L)**2*t)+third*np.exp(-D*(3*np.pi/L)**2*t)
    wave=first*np.cos(c*np.pi/L*t)+third*np.cos(3*c*np.pi/L*t)
    return heat,wave

def gaussian(x,t,sigma0=.1,D=.1):
    variance=sigma0**2+2*D*t
    return np.exp(-np.asarray(x)**2/(2*variance))/np.sqrt(2*np.pi*variance)

def fd_first(M,L=1.):
    h=L/M
    K=(2*np.eye(M-1)-np.eye(M-1,k=1)-np.eye(M-1,k=-1))/h**2
    return float(np.linalg.eigvalsh(K)[0])

def summary():
    roots=jn_zeros(0,2)
    errors=[abs(fd_first(M)-np.pi**2) for M in [20,40,80]]
    return dict(
        pluck=dict(L_m=1.,a_m=.3,A_m=.001,c_m_per_s=100.,fundamental_Hz=50.,
                   first_coefficients_m=pluck_coeff(np.arange(1,11)).tolist()),
        heat=dict(D_m2_per_s=.1,L_m=1.,t_s=.2,
                  modal_attenuation=np.exp(-.1*(np.array([1.,3.])*np.pi)**2*.2).tolist()),
        membrane=dict(radius_m=.1,c_m_per_s=20.,J0_zeros=roots.tolist(),
                      axisymmetric_Hz=(20*roots/(2*np.pi*.1)).tolist(),
                      ratio=float(roots[1]/roots[0])),
        green=dict(L_m=1.,source_m=.3,peak_m=float(green(.3,.3)),slope_jump=-1.),
        rayleigh=dict(trial_quotient=10.,exact_first=np.pi**2),
        finite_difference=dict(elements=[20,40,80],first_eigenvalues=[fd_first(M) for M in [20,40,80]],
                               errors=errors,error_ratios=(np.array(errors[:-1])/errors[1:]).tolist()),
        gaussian=dict(initial_variance_m2=.01,variance_at_t_point2_m2=.01+2*.1*.2))
if __name__=='__main__':
    print(json.dumps(summary(),ensure_ascii=True,indent=2))
