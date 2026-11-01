"""Independent checks of model mathematics, dimensions and original demonstrations."""
from pathlib import Path
import importlib.util,sys,json,math
import numpy as np
from scipy import integrate,optimize,linalg,signal
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/circuit-theory-2026-11-02';sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('ct_example',ROOT/'public/code/circuit-theory/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
data=json.loads((REC/'calculations.json').read_text(encoding='utf-8'));checks=[]
def check(name,condition,detail=None):
    if not bool(condition):raise AssertionError((name,detail))
    checks.append({'name':name,'passed':True,'detail':detail})
def close(name,a,b,atol=1e-10,rtol=1e-7):
    check(name,np.allclose(a,b,atol=atol,rtol=rtol),{'max_abs_error':float(np.max(np.abs(np.asarray(a)-np.asarray(b))))})
# Nodal result against independent branch-current KCL/KVL formulation.
B=np.array([[1,-1,-1,0],[0,0,1,-1],[1000,2000,0,0],[0,2000,-1000,-1000]],float)
branch=np.linalg.solve(B,[0,-.0002,1,0]);stored=np.array(data['network']['currents_A'])
close('branch-current solution against node solution',branch,stored)
close('KCL at A',branch[0],branch[1]+branch[2])
close('KCL at B',branch[2]+.0002,branch[3])
close('KVL source-A-ground',1000*branch[0]+2000*branch[1],1)
close('KVL A-B-ground',2000*branch[1]-1000*branch[2]-1000*branch[3],0)
close('node A from branch',2000*branch[1],data['network']['va_V'])
close('node B from branch',1000*branch[3],data['network']['vb_V'])
power=branch@np.diag([1000,2000,1000,1000])@branch
close('total energy balance',power,branch[0]+.0002*1000*branch[3])
close('supplied power recorded',power,data['network']['supplied_power_W'])
close('superposition of independent sources',np.linalg.solve(B,[0,0,1,0])+np.linalg.solve(B,[0,-.0002,0,0]),branch)
# Divider/Thevenin: independent branch-current circuit solve for diverse loads.
for rl in [100,1000,5000,10000,100000,1e6]:
    # Unknown current through R1, R2, RL, and port voltage.
    A=np.array([[1,-1,-1,0],[1e4,0,0,1],[0,1e4,0,-1],[0,0,rl,-1]])
    sol=np.linalg.solve(A,[0,1,0,0])
    close(f'Thevenin port with load {rl}',sol[-1],.5*rl/(5000+rl))
close('divider open output',.5,data['divider']['open_V'])
close('divider 10k output',1/3,data['divider']['loaded_10k_V'])
# Dependent-source one-port: retain gm when calculating test resistance.
for gm in [0,.0005,.002]:
    conductance=1/1000-gm;test_current=conductance*.2
    close(f'test-source dependent gm {gm}',.2/test_current,1/conductance)
check('dependent source can give negative incremental R',1/(.001-.002)<0)
# Source resistance and microphone voltage loading.
close('microphone 10k loading',10000/(2000+10000),5/6)
close('microphone 100k loading',100000/(2000+100000),50/51)
# RC analytical versus independent ODE solutions with several initial states.
tau=.01
for v0 in [0,.3,-.2,1.5]:
    t=np.linspace(0,.05,401);sol=integrate.solve_ivp(lambda t,y:[(1-y[0])/.01],[0,.05],[v0],t_eval=t,rtol=1e-10,atol=1e-12)
    close(f'RC arbitrary initial {v0}',sol.y[0],1+(v0-1)*np.exp(-t/tau),atol=2e-9)
close('RC at one time constant',data['rc']['v_at_tau_V'],1-math.exp(-1))
close('RC current at one time constant',data['rc']['i_at_tau_A'],1e-4/math.e)
close('5tau fraction',1-math.exp(-5),.9932620530009145)
# Independent quadrature in normalized time, integrals on [0,infinity).
supply=1e-6*integrate.quad(lambda z:np.exp(-z),0,np.inf,epsabs=1e-12)[0]
loss=1e-6*integrate.quad(lambda z:np.exp(-2*z),0,np.inf,epsabs=1e-12)[0]
close('RC source energy integral',supply,1e-6,atol=1e-13)
close('RC resistor energy integral',loss,data['rc']['dissipated_energy_total_J'],atol=1e-13)
close('RC stored energy balance',supply-loss,data['rc']['stored_energy_final_J'],atol=1e-13)
# Phasor capacitor output via complex KCL, no reuse of transfer formula.
for f in [1,20,1591.5494309189535,3183.098861837907,20000,1e6]:
    s=2j*np.pi*f;R=1e4;C=1e-8
    v=(1/R)/(1/R+s*C)
    vl=(1/R)/(1/R+1/1e4+s*C)
    close(f'RC LP impedance solve f={f}',v,1/(1+s*R*C))
    close(f'RC loaded impedance solve f={f}',vl,.5/(1+s*5000*C))
    close(f'RC complementary outputs f={f}',v+s*R*C/(1+s*R*C),1)
close('RC unloaded cutoff magnitude',abs(1/(1+1j)),1/np.sqrt(2))
close('RC cutoff dB',20*np.log10(1/np.sqrt(2)),-3.010299956639812)
close('loaded pole from C seen R',1/(2*np.pi*5000*1e-8),data['frequency']['loaded_fc_Hz'])
close('coupling 20Hz gain',1e4/abs(1e4+1/(2j*np.pi*20*1e-6)),data['frequency']['coupling_20Hz_gain'])
# RLC: closed-form/modal matrix exponential independent of solve_ivp.
for R in [40.,200.,500.]:
    model=m.rlc_step(R);t=np.array(model['t_s']);L=.01;C=1e-6
    A=np.array([[0,1/C],[-1/L,-R/L]])
    for time in [.0001,.0005,.001,.003,.006]:
        idx=np.argmin(abs(t-time));ref=np.array([1.,0])+linalg.expm(A*t[idx])@np.array([-1.,0])
        close(f'RLC matrix exp R={R},t={time}',[model['vc_V'][idx],model['i_A'][idx]],ref,atol=3e-9)
    roots=np.roots([1,R/L,1/(L*C)])
    close(f'RLC roots trace R={R}',sum(roots),-R/L)
    close(f'RLC roots product R={R}',np.prod(roots),1/(L*C),atol=1e-7)
    check(f'RLC stable real parts R={R}',np.all(roots.real<0))
# Exact half-power current roots by scalar numerical solve.
R,L,C=40.,.01,1e-6;w0=1/np.sqrt(L*C)
magnitude=lambda w:R/np.sqrt(R**2+(w*L-1/(w*C))**2)
low=optimize.brentq(lambda w:magnitude(w)-1/np.sqrt(2),1,w0)
high=optimize.brentq(lambda w:magnitude(w)-1/np.sqrt(2),w0,1e6)
close('RLC half-power bandwidth roots',(high-low)/(2*np.pi),data['rlc'][0]['bandwidth_Hz'])
close('RLC Q via bandwidth',w0/(high-low),data['rlc'][0]['Q'])
resonance=optimize.minimize_scalar(lambda w:-magnitude(w),bounds=(1000,30000),method='bounded').x
close('RLC resistor output resonance',resonance,w0,atol=.01)
vc_peak=optimize.minimize_scalar(lambda w:-1/np.sqrt((1-w*w*L*C)**2+(w*R*C)**2),bounds=(1000,20000),method='bounded').x
close('RLC capacitor voltage peak',vc_peak,w0*np.sqrt(1-2*.2**2),atol=.01)
# Initial-value Laplace identity for a charged RC and full versus zero state.
u0=.3;s=120+80j
u_transform=1/s+(u0-1)/(s+100)
close('Laplace capacitor initial term',1e-6*(s*u_transform-u0),(1/s-u_transform)/1e4)
# Passive coupled inductor matrix and ideal transformer port balance.
Lmat=np.array([[.01,.012],[.012,.04]])
check('mutual inductance PSD bound',np.min(np.linalg.eigvalsh(Lmat))>=0 and .012**2<=.01*.04)
curr=np.array([.2,-.3]);close('coupled energy quadratic',.5*curr@Lmat@curr,.5*(.01*.2**2+.04*.3**2+2*.012*.2*(-.3)))
n=3.;u2=2.;i2=-.05;u1=n*u2;i1=-i2/n
close('ideal transformer port power',u1*i1+u2*i2,0)
close('ideal transformer reflected resistance',u1/i1,n*n*(u2/(-i2)))
# AC power from numerical integration and RMS, not the complex product.
U=1.;Iamp=.025;phase=np.arctan2(24,32)
avg=integrate.quad(lambda theta:2*U*Iamp*np.cos(theta)*np.cos(theta-phase),0,2*np.pi)[0]/(2*np.pi)
close('AC average power time integral',avg,data['power']['P_W'])
close('AC current real and imaginary',[.025*np.cos(-phase),.025*np.sin(-phase)],data['power']['current_A'])
close('AC reactive power',U*Iamp*np.sin(phase),data['power']['Q_var'])
close('apparent power triangle',np.hypot(data['power']['P_W'],data['power']['Q_var']),data['power']['S_VA'])
close('RMS voltage integration',np.sqrt(integrate.quad(lambda t:2*np.cos(t)**2,0,2*np.pi)[0]/(2*np.pi)),1)
# Maximum power by direct scalar optimization.
source_r=5000.
opt=optimize.minimize_scalar(lambda load:-.5**2*load/(source_r+load)**2,bounds=(1,1e5),method='bounded')
close('maximum resistor power at matching',opt.x,source_r,atol=.01)
close('matching source and load dissipation',(.5/(source_r+source_r))**2*source_r,-opt.fun,atol=1e-12)
# Finite-gain op amp, directly solve input/error/feedback equations.
a0,fp,beta=1e5,10.,.1
for f in [0,20,1000,20000,100010,1e6]:
    A=a0/(1+1j*f/fp);vout=np.linalg.solve(np.array([[1/A,1],[-beta,1]],complex),[1,0])[0]
    close(f'opamp feedback constraint f={f}',vout,(a0/(1+beta*a0))/(1+1j*f/(fp*(1+beta*a0))))
close('slew requirement',2*np.pi*20000*1/1e6,data['opamp']['required_slew_20kHz_1Vpk_V_per_us'])
# Probe via impedance vs its normalized pole/DC form.
rp,cp,rs=1e6,100e-12,1e4
for f in [0,20000,160746.49252281428,1e6]:
    zp=1/(1/rp+2j*np.pi*f*cp);direct=zp/(rs+zp)
    close(f'probe normalized pole f={f}',direct,(rp/(rs+rp))/(1+2j*np.pi*f*(rs*rp/(rs+rp))*cp))
# Noise bandwidth: normalized adaptive integration and independently derived kT/C.
kb,T,R,C=1.380649e-23,300.,1e4,1e-8;fc=1/(2*np.pi*R*C)
integral=integrate.quad(lambda x:1/(1+x*x),0,np.inf)[0]*fc
close('one-pole equivalent noise bandwidth',integral,data['measurement']['rc_noise_bandwidth_Hz'])
variance=4*kb*T*R*integral
close('kT/C noise variance',variance,kb*T/C,atol=1e-23)
close('filtered noise RMS',np.sqrt(variance),data['measurement']['rc_noise_V_rms'],atol=1e-16)
close('20k rectangular noise RMS',np.sqrt(4*kb*T*R*20000),data['measurement']['noise_20kHz_V_rms'],atol=1e-16)
close('one-sided noise density units/numeric',np.sqrt(4*kb*T*R),data['measurement']['noise_density_V_per_sqrtHz'],atol=1e-18)
for ratio in [.001,.1,1,10,1000]:
    fraction=integrate.quad(lambda x:1/(1+x*x),0,ratio)[0]/(np.pi/2)
    close(f'cumulative noise integral x={ratio}',fraction,2/np.pi*np.arctan(ratio))
# Model dimensional checks using independent SI scaling.
close('kohm-microfarad to seconds',(10*1e3)*(1*1e-6),.01)
close('millihenry-microfarad natural angular frequency',1/np.sqrt((10*1e-3)*(1*1e-6)),10000)
close('audio propagation wavelength',2e8/20000,10000)
# SVG parse and resource inventory.
for p in sorted((ROOT/'public/figures/circuit-theory').glob('*.svg')):
    check('SVG parse '+p.name,ET.parse(p).getroot().tag.endswith('svg'))
check('ten article SVGs',len(list((ROOT/'public/figures/circuit-theory').glob('*.svg')))==10)
check('course line sketch XML',ET.parse(ROOT/'public/figures/foundation-courses/circuit-theory.svg').getroot().tag.endswith('svg'))
result={'scope':'Specified ideal circuits and mathematics; independent formulations, ODE/modal solutions, time/frequency integration and media checks. Not measured hardware or professional review.','total':len(checks),'passed':len(checks),'checks':checks}
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'total':len(checks),'passed':len(checks)}))
