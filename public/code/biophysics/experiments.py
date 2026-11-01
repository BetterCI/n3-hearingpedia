"""Original specified biophysical models, not biological measurements. numpy/scipy required."""
import json
import numpy as np
from scipy.special import expit
kB=1.380649e-23;NA=6.02214076e23;e=1.602176634e-19;R=kB*NA;F=e*NA;T=310.
def open_prob(deltaG):return expit(-np.asarray(deltaG)/(kB*T))
def diffusion(x,t,D=100.):return np.exp(-np.asarray(x)**2/(4*D*t))/np.sqrt(4*np.pi*D*t)
def binding(t,scale=1.,c=2e-6):
    kon=scale*1e6;koff=scale;rate=kon*c+koff;eq=kon*c/rate
    return eq*(1-np.exp(-rate*np.asarray(t)))
def nernst(z,cin,cout):return R*T/(z*F)*np.log(np.asarray(cout)/cin)
def ghk(Ko=5.,PK=1.,PNa=.04,PCl=.45):
    return R*T/F*np.log((PK*np.asarray(Ko)+PNa*145+PCl*10)/(PK*140+PNa*12+PCl*120))
def passive(t):
    C=10e-12;g=1e-9;EL=-.070;I=20e-12;t=np.asarray(t);tau=C/g;final=EL+I/g
    V=final+(EL-final)*np.exp(-t/tau);cap=I*np.exp(-t/tau)
    return V,cap,g*(V-EL)
def gate(t,p0=.2,alpha=100.,beta=50.):
    eq=alpha/(alpha+beta)
    return eq+(p0-eq)*np.exp(-(alpha+beta)*np.asarray(t))

def channel_moments(N,p=.2,i=-1e-12):
    """Independent identical channels at fixed probability; currents in A."""
    return N*p*i, np.sqrt(N*p*(1-p)*i*i)
def cable(x,f):
    a=1e-6;RM=1.;rhoi=1.;CM=.01;lam=np.sqrt(a*RM/(2*rhoi));tau=RM*CM
    return np.exp(-np.asarray(x)*np.sqrt(1+2j*np.pi*f*tau)/lam)
def mechanics():
    zeta=6*np.pi*.001*.5e-6;k=1e-5
    return dict(zeta=zeta,k=k,tau=zeta/k,variance=kB*T/k,rms=np.sqrt(kB*T/k),force=.2e-12,mean=.2e-12/k)
def transduction(x,EMET=.080):
    p=expit(.3e-12*(np.asarray(x)-10e-9)/(kB*T));g=10e-9*p;gK=20e-9;EK=-.080
    V=(gK*EK+g*EMET)/(gK+g)
    return p,V
def summary():
    C=.01*1000e-12;charge=C*.070;N=charge/e;ions=.140*1e-12*NA
    return dict(constants=dict(kB=kB,NA=NA,e=e,R=R,F=F,T=T,kBT_J=kB*T,kBT_pN_nm=kB*T/1e-21,RT_J_per_mol=R*T),
        diffusion=dict(D_stokes_um2_per_s=kB*T/(6*np.pi*.001*5e-9)*1e12,time_10um_s=.5,time_100um_s=50.),
        nernst_mV=dict(K=float(nernst(1,140,5)*1000),Na=float(nernst(1,12,145)*1000),Cl=float(nernst(-1,10,120)*1000)),
        GHK_mV=float(ghk()*1000),osmotic_1mM_Pa=R*T,
        membrane=dict(C_F=C,charge_C=charge,elementary_charges=N,total_K_ions=ions,fraction=N/ions,tau_s=.01,V_at_tau_mV=float(passive(.01)[0]*1000)),
        channel=dict(p_inf=100/(100+50),tau_s=1/(100+50),
            mean_pA_100=float(channel_moments(100)[0]*1e12),sd_pA_100=float(channel_moments(100)[1]*1e12),
            mean_pA_10000=float(channel_moments(10000)[0]*1e12),sd_pA_10000=float(channel_moments(10000)[1]*1e12)),
        cable=dict(lambda_m=float(np.sqrt(1e-6/2)),tau_s=.01),
        mechanics=mechanics(),transduction=dict(width_nm=kB*T/(.3e-12)*1e9,half_voltage_mV=float(transduction(10e-9)[1]*1000)))
if __name__=='__main__':print(json.dumps(summary(),ensure_ascii=True,indent=2))
