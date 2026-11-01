"""Original low-voltage lumped circuit examples. NumPy/SciPy, SI units.
Run: python experiments.py. No measured devices or listening-level prescription.
"""
import numpy as np
from scipy.integrate import solve_ivp
KB=1.380649e-23

def resistive_network():
    g1,g2,g3,g4=1/1000,1/2000,1/1000,1/1000
    G=np.array([[g1+g2+g3,-g3],[-g3,g3+g4]])
    rhs=np.array([g1*1.,.0002])
    va,vb=np.linalg.solve(G,rhs)
    currents=np.array([(1-va)/1000,va/2000,(va-vb)/1000,vb/1000])
    powers=currents**2*np.array([1000,2000,1000,1000])
    return {'va_V':float(va),'vb_V':float(vb),'currents_A':currents.tolist(),
      'resistor_powers_W':powers.tolist(),'total_dissipation_W':float(sum(powers)),
      'supplied_power_W':float(currents[0]*1+.0002*vb)}

def first_order():
    R,C,Vs=1e4,1e-6,1.
    tau=R*C
    t=np.linspace(0,5*tau,501)
    vc=Vs*(1-np.exp(-t/tau));current=(Vs-vc)/R
    return {'R_ohm':R,'C_F':C,'tau_s':tau,'v_at_tau_V':float(Vs*(1-np.exp(-1))),
       'i_at_tau_A':float(Vs/R*np.exp(-1)),'t_s':t.tolist(),'vc_V':vc.tolist(),'i_A':current.tolist(),
       'stored_energy_final_J':C*Vs**2/2,'dissipated_energy_total_J':C*Vs**2/2}

def frequency_response():
    f=np.logspace(0,6,601);R,C,RL=1e4,1e-8,1e4;s=2j*np.pi*f
    lp=1/(1+s*R*C);hp=s*R*C/(1+s*R*C)
    loaded=RL/(R+RL+s*R*RL*C)
    return {'f_Hz':f.tolist(),'lp':lp,'hp':hp,'loaded':loaded,
       'fc_Hz':1/(2*np.pi*R*C),'loaded_fc_Hz':1/(2*np.pi*(R*RL/(R+RL))*C),
       'coupling_20Hz_gain':float(abs((2j*np.pi*20*1e4*1e-6)/(1+2j*np.pi*20*1e4*1e-6)))}

def rlc_step(R=40.):
    L,C=.01,1e-6
    t=np.linspace(0,.006,1201)
    def derivative(t,state):
        vc,current=state
        return [current/C,(1-R*current-vc)/L]
    solution=solve_ivp(derivative,[0,t[-1]],[0,0],t_eval=t,rtol=1e-10,atol=1e-12)
    assert solution.success
    return {'R_ohm':R,'L_H':L,'C_F':C,'t_s':t.tolist(),'vc_V':solution.y[0].tolist(),'i_A':solution.y[1].tolist(),
      'omega0_rad_s':1/np.sqrt(L*C),'f0_Hz':1/(2*np.pi*np.sqrt(L*C)),
      'alpha_per_s':R/(2*L),'zeta':R/2*np.sqrt(C/L),'Q':np.sqrt(L/C)/R,
      'bandwidth_Hz':R/(2*np.pi*L)}

def power_example():
    voltage=1+0j;impedance=32+24j;current=voltage/impedance
    complex_power=voltage*np.conj(current)
    return {'impedance_ohm':[32.,24.],'current_A':[float(current.real),float(current.imag)],
      'P_W':float(complex_power.real),'Q_var':float(complex_power.imag),'S_VA':float(abs(complex_power)),
      'power_factor':float(complex_power.real/abs(complex_power))}

def measurements():
    R,C,T=1e4,1e-8,300.
    rp,cp=1e6,100e-12
    eqR=R*rp/(R+rp)
    noise_density=np.sqrt(4*KB*T*R)
    return {'noise_density_V_per_sqrtHz':float(noise_density),'noise_20kHz_V_rms':float(noise_density*np.sqrt(2e4)),
      'rc_noise_bandwidth_Hz':1/(4*R*C),'rc_noise_V_rms':float(np.sqrt(KB*T/C)),
      'probe_dc_gain':rp/(R+rp),'probe_pole_Hz':1/(2*np.pi*eqR*cp)}

if __name__=='__main__':
    import json
    values={'network':resistive_network(),'rc':first_order(),'rlc':rlc_step(),'power':power_example(),'measurement':measurements()}
    for key in ('rc','rlc'):
        for name in ('t_s','vc_V','i_A'):values[key].pop(name)
    f=frequency_response()
    values['frequency']={k:v for k,v in f.items() if k not in ['f_Hz','lp','hp','loaded']}
    print(json.dumps(values,indent=2))
