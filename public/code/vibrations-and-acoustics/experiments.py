"""Original SI-unit teaching models. No measured recordings or calibration data.
Python 3.11, NumPy 1.26.4, SciPy 1.17.1. All phasors use peak values and exp(iωt).
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigh
RHO=1.2
C=343.
Z0=RHO*C
MASS=.02
STIFFNESS=80.
OMEGA_N=np.sqrt(STIFFNESS/MASS)

def mechanical_response(omega,zeta):
    b=2*zeta*np.sqrt(MASS*STIFFNESS)
    return 1/(STIFFNESS-MASS*np.asarray(omega)**2+1j*b*np.asarray(omega))

def free_vibration(zeta,t=None):
    if t is None:t=np.linspace(0,.6,3001)
    b=2*zeta*np.sqrt(MASS*STIFFNESS)
    def rhs(t,q):return [q[1],-(b*q[1]+STIFFNESS*q[0])/MASS]
    s=solve_ivp(rhs,(0,float(t[-1])),[.001,0.],method='DOP853',t_eval=t,rtol=1e-11,atol=1e-13,max_step=.001)
    assert s.success
    q,v=s.y;energy=.5*MASS*v*v+.5*STIFFNESS*q*q
    return s.t,q,v,energy

def modal_model():
    mass=np.diag([.02,.03]);stiffness=np.array([[140.,-60.],[-60.,180.]])
    damping=1.*mass+.0005*stiffness
    values,modes=eigh(stiffness,mass)
    for i in range(2):
        if modes[0,i]<0:modes[:,i]*=-1
    return mass,stiffness,damping,values,modes

def modal_response(frequencies):
    mass,stiffness,damping,values,modes=modal_model();force=np.array([1.,0.]);direct=[];modal=[]
    modal_damping=np.diag(modes.T@damping@modes)
    for f in frequencies:
        w=2*np.pi*f;direct.append(np.linalg.solve(stiffness-w*w*mass+1j*w*damping,force))
        modal.append(modes@((modes.T@force)/(values-w*w+1j*w*modal_damping)))
    return np.array(direct),np.array(modal)

def plane_fields(x,reflection=0.,frequency=500.,incident_rms=1.):
    x=np.asarray(x);k=2*np.pi*frequency/C
    forward=np.sqrt(2)*incident_rms*np.exp(-1j*k*x);backward=np.sqrt(2)*incident_rms*reflection*np.exp(1j*k*x)
    return forward+backward,(forward-backward)/Z0

def active_intensity(pressure_peak,velocity_peak):
    return .5*np.real(pressure_peak*np.conj(velocity_peak))

def interface(z1,z2):
    rp=(z2-z1)/(z2+z1);tp=2*z2/(z1+z2)
    reflectance=rp*rp;transmittance=4*z1*z2/(z1+z2)**2
    return rp,tp,reflectance,transmittance

def combined_spl(level1,level2,correlation=0.):
    assert -1<=correlation<=1
    a,b=10**(level1/20),10**(level2/20)
    square=a*a+b*b+2*correlation*a*b
    return float(10*np.log10(square)) if square>0 else float('-inf')

def spherical_fields(radius,frequency=500.,rms_at_one_metre=1.):
    radius=np.asarray(radius);k=2*np.pi*frequency/C
    pressure=np.sqrt(2)*rms_at_one_metre*np.exp(-1j*k*radius)/radius
    velocity=pressure/Z0*(1+1/(1j*k*radius))
    return pressure,velocity

def resonator():
    area=np.pi*.01**2;volume=.001;effective_length=.04
    inertance=RHO*effective_length/area;compliance=volume/(RHO*C*C)
    frequency=1/(2*np.pi*np.sqrt(inertance*compliance))
    return dict(area_m2=area,volume_m3=volume,effective_length_m=effective_length,inertance_kg_per_m4=inertance,compliance_m3_per_Pa=compliance,frequency_Hz=frequency)

def echo_model():
    fs=48000;delay=.004;offset=round(fs*delay);h=np.zeros(offset+1);h[0]=1;h[-1]=.6
    frequencies=np.linspace(0,2000,4001);response=1+.6*np.exp(-2j*np.pi*frequencies*delay)
    return fs,h,frequencies,response

def summary():
    mass,stiffness,damping,values,modes=modal_model();q=.05;wplus=OMEGA_N*(np.sqrt(1+q*q)+q);wminus=OMEGA_N*(np.sqrt(1+q*q)-q)
    direct,modal=modal_response(np.linspace(5,22,301));ri=interface(Z0,3*Z0)
    return dict(mass_kg=MASS,stiffness_N_per_m=STIFFNESS,natural_frequency_Hz=OMEGA_N/(2*np.pi),zeta005=dict(displacement_peak_Hz=OMEGA_N*np.sqrt(1-2*q*q)/(2*np.pi),velocity_peak_Hz=OMEGA_N/(2*np.pi),Q=1/(2*q),velocity_half_power_Hz=[wminus/(2*np.pi),wplus/(2*np.pi)]),modal_frequencies_Hz=(np.sqrt(values)/(2*np.pi)).tolist(),modal_mass_orthogonality_error=float(np.max(abs(modes.T@mass@modes-np.eye(2)))),direct_modal_max_difference=float(np.max(abs(direct-modal))),air=dict(rho=RHO,c=C,Z0=Z0,frequency_Hz=500.,wavelength_m=C/500.,pressure_rms_Pa=1.,velocity_rms_m_per_s=1/Z0,displacement_rms_m=1/(Z0*2*np.pi*500),SPL_dB=20*np.log10(1/20e-6),active_intensity_W_per_m2=1/Z0,intensity_level_dB=10*np.log10(1/Z0/1e-12)),interface_ratio3=dict(rp=ri[0],tp=ri[1],reflectance=ri[2],transmittance=ri[3]),two_70dB=dict(uncorrelated=combined_spl(70,70),in_phase=combined_spl(70,70,1)),distance_doubling_dB=-20*np.log10(2),tube_length_m=.5,open_open_f1_Hz=C,closed_open_f1_Hz=C/2,resonator=resonator(),echo=dict(delay_s=.004,spacing_Hz=250.,peak_relative_dB=20*np.log10(1.6),minimum_relative_dB=20*np.log10(.4)))

if __name__=='__main__':
    import json
    print(json.dumps(summary(),ensure_ascii=False,indent=2))
