"""Original, reproducible teaching figures; continuous-time responses sampled for plotting."""
from pathlib import Path
import json
import numpy as np
import scipy
from scipy import signal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'public/figures/phase-and-group-delay'
RESEARCH = ROOT/'docs/research/phase-and-group-delay-2026-10-27'
OUT.mkdir(parents=True, exist_ok=True)
RESEARCH.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei', 'font.size':12,
    'svg.fonttype':'path', 'axes.unicode_minus':False, 'axes.spines.top':False,
    'axes.spines.right':False, 'savefig.dpi':160, 'svg.hashsalt':'phase-group-delay'})
BLUE, ORANGE, GREEN = '#22658c', '#b45b36', '#397a66'
manifest=[]
def save(fig, name, params):
    fig.savefig(OUT/(name+'.svg'), facecolor='white', metadata={'Date':None})
    svg_path = OUT/(name+'.svg')
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8')
    fig.savefig(OUT/(name+'.png'), facecolor='white')
    plt.close(fig)
    manifest.append({'file':name+'.svg', 'preview':name+'.png', 'nature':'原创解析/数值教学图，非实测', 'parameters':params})
def grid(ax):
    ax.grid(alpha=.16)

# 1: pure delay; the unwrapped phase is recovered from the plotted samples.
freq=np.arange(0,2000.1,5.)
tau=.002
H=np.exp(-2j*np.pi*freq*tau)
wrapped=np.angle(H)
phase=np.unwrap(wrapped)
gd=-np.gradient(phase,freq)/(2*np.pi)
assert np.max(np.abs(gd-tau)) < 1e-12
fig,axs=plt.subplots(1,2,figsize=(12,4.4),layout='constrained')
for indices in np.split(np.arange(len(freq)),np.flatnonzero(np.abs(np.diff(wrapped))>np.pi)+1):
    axs[0].plot(freq[indices]/1000,wrapped[indices]/np.pi,color=ORANGE,lw=1.6)
axs[0].set(title='（a）包裹相位',xlabel='频率 f（kHz）',ylabel='相位（π rad）',ylim=(-1.15,1.15),yticks=[-1,0,1])
axs[1].plot(freq/1000,phase/np.pi,color=BLUE,lw=2)
axs[1].scatter([0,1],[0,-4],color=BLUE,zorder=4)
axs[1].text(.12,-6.5,'f = 1 kHz：φ = −4π rad\n相位延迟 = 群延迟 = 2 ms',fontsize=11,color=BLUE)
axs[1].set(title='（b）展开后的同一组样本',xlabel='频率 f（kHz）',ylabel='相位（π rad）',yticks=[0,-2,-4,-6,-8])
for ax in axs:grid(ax)
save(fig,'01-pure-delay',{'delay_s':tau,'frequency_step_Hz':5,'phase_at_1000Hz_rad':float(phase[200]),'max_delay_error_s':float(np.max(abs(gd-tau)))})

# 2: geometric explanation using negative phase, so both slopes equal delays.
# Original analytic plot; the user's reference supplied the secant/tangent layout.
wn=2*np.pi*1000;zeta=.5
u=np.linspace(0,2.15,1201);omega=u*wn
negative_phase=2*np.arctan2(2*zeta*u,1-u*u)
H2=(1-u*u-2j*zeta*u)/(1-u*u+2j*zeta*u)
assert np.allclose(H2,np.exp(-1j*negative_phase),atol=1e-12)
u0=.85;omega0=u0*wn
psi0=2*np.arctan2(2*zeta*u0,1-u0*u0)
secant_delay=psi0/omega0
tangent_delay=4*zeta*(1+u0*u0)/((1-u0*u0)**2+4*zeta*zeta*u0*u0)/wn
delta=1e-5
numerical_slope=(2*np.arctan2(2*zeta*(u0+delta),1-(u0+delta)**2)-2*np.arctan2(2*zeta*(u0-delta),1-(u0-delta)**2))/(2*delta*wn)
assert tangent_delay>secant_delay>0
assert abs(numerical_slope-tangent_delay)<1e-10
fig,ax=plt.subplots(figsize=(10,5.6))
fig.subplots_adjust(left=.04,right=.98,bottom=.06,top=.98)
ax.set(xlim=(-.14*wn,2.31*wn),ylim=(-.65,6.0));ax.axis('off')
arrow={'arrowstyle':'->','color':'#1d252b','lw':1.8,'mutation_scale':18}
ax.annotate('',xy=(2.25*wn,0),xytext=(0,0),arrowprops=arrow)
ax.annotate('',xy=(0,5.75),xytext=(0,0),arrowprops=arrow)
ax.text(2.22*wn,-.25,r'$\omega$ (rad/s)',ha='right',va='top',fontsize=16)
ax.text(-.02*wn,5.77,r'$-\phi$ (rad)',ha='left',va='bottom',fontsize=16)
ax.text(-.025*wn,-.17,'0',ha='right',va='top',fontsize=14)
ax.plot(omega,negative_phase,color=BLUE,lw=3.5,solid_capstyle='round')
ax.plot([0,omega0],[0,psi0],color=GREEN,ls=(0,(4,3)),lw=2.6)
tangent_w=np.array([.33,1.47])*wn
ax.plot(tangent_w,psi0+tangent_delay*(tangent_w-omega0),color=ORANGE,lw=2.8)
ax.plot([omega0,omega0],[0,psi0],color='#8a959d',ls=(0,(3,4)),lw=1.4)
ax.scatter([omega0],[psi0],s=90,color=BLUE,zorder=5)
ax.text(omega0,-.20,r'$\omega_0$',ha='center',va='top',fontsize=17)
ax.text(.10*wn,1.45,'割线斜率\n'+r'$=\tau_p(\omega_0)$',color=GREEN,fontsize=18,linespacing=1.5)
ax.text(1.15*wn,2.0,'切线斜率\n'+r'$=\tau_g(\omega_0)$',color=ORANGE,fontsize=18,linespacing=1.5)
ax.text(1.78*wn,4.55,r'$-\phi(\omega)$',color=BLUE,fontsize=21)
save(fig,'secant-tangent',{'reference':'User-supplied conceptual secant/tangent layout; independently calculated and redrawn, not a copy of the raster image','vertical_axis':'negative unwrapped phase (rad), positive upward','horizontal_axis':'angular frequency (rad/s), positive rightward','model':'H(jw)=(wn^2-w^2-j*2*zeta*wn*w)/(wn^2-w^2+j*2*zeta*wn*w)','wn_rad_per_s':wn,'zeta':zeta,'omega0_rad_per_s':omega0,'phase_delay_s':float(secant_delay),'group_delay_s':float(tangent_delay),'tangent_finite_difference_error_s':float(abs(numerical_slope-tangent_delay)),'ticks_omitted_for_conceptual_explanation':True,'clinical_or_device_norm':False})

# 3: independently specified first-order analog allpass H=(a-jw)/(a+jw).
a=2*np.pi*1000
freq=np.linspace(1,4000,4000)
w=2*np.pi*freq
phi=-2*np.arctan(w/a)
tp=-phi/w
tg=2*a/(a*a+w*w)
fig,axs=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
axs[0].plot(freq/1000,phi/np.pi,color=BLUE,lw=2,label='相位曲线')
f0=1000.;w0=2*np.pi*f0;phi0=-np.pi/2;tg0=1/a
sel=(freq>=250)&(freq<=2200)
axs[0].plot(freq[sel]/1000,(phi0-tg0*(w[sel]-w0))/np.pi,'--',color=ORANGE,label='1 kHz处的切线')
axs[0].plot([0,1],[0,-.5],':',color=GREEN,lw=2,label='原点到该点的割线')
axs[0].scatter([1],[-.5],color=BLUE,zorder=4)
axs[0].set(title='（a）割线与切线的斜率不同',xlabel='频率 f（kHz）',ylabel='相位（π rad）',xlim=(0,4),ylim=(-1,.08))
axs[0].legend(fontsize=10,loc='lower left')
axs[1].plot(freq/1000,tp*1000,color=BLUE,lw=2,label='相位延迟')
axs[1].plot(freq/1000,tg*1000,'--',color=ORANGE,lw=2,label='群延迟')
axs[1].scatter([1,1],[.25,1000/a],color=[BLUE,ORANGE],zorder=4)
axs[1].annotate('0.250 ms',xy=(1,.25),xytext=(1.75,.26),arrowprops={'arrowstyle':'->','color':BLUE},fontsize=11,color=BLUE)
axs[1].annotate('0.159 ms',xy=(1,1000/a),xytext=(1.75,.14),arrowprops={'arrowstyle':'->','color':ORANGE},fontsize=11,color=ORANGE)
axs[1].set(title='（b）幅度恒为1，延迟仍随频率变化',xlabel='频率 f（kHz）',ylabel='延迟（ms）',xlim=(0,4),ylim=(0,.36))
axs[1].legend(fontsize=10)
for ax in axs:grid(ax)
assert np.isclose(-phi0/w0,.00025)
assert np.isclose(tg0,.00015915494309189535)
save(fig,'02-allpass-delay',{'a_rad_per_s':a,'model':'H(jw)=(a-jw)/(a+jw)','phase_delay_at_1000Hz_ms':.25,'group_delay_at_1000Hz_ms':tg0*1000,'unity_magnitude':True})

# 4: use an oversampled long record to approximate continuous-time filtering.
fs=192000
n=32768
t=(np.arange(n)-n//2)/fs
sigma=.0015
carrier=1000
env=np.exp(-.5*(t/sigma)**2)
z=env*np.exp(2j*np.pi*carrier*t)
ww=2*np.pi*np.fft.fftfreq(n,1/fs)
HH=(a-1j*ww)/(a+1j*ww)
out=np.fft.ifft(np.fft.fft(z)*HH)
approx=np.exp(-.5*((t-tg0)/sigma)**2)*np.exp(1j*(2*np.pi*carrier*t+phi0))
err=float(np.linalg.norm(out-approx)/np.linalg.norm(out))
assert err < .01
energy_error=float(abs(np.sum(abs(out)**2)/np.sum(abs(z)**2)-1))
assert energy_error < 1e-12
peak_delay=float(t[np.argmax(abs(out))])
fig,axs=plt.subplots(2,1,figsize=(11,6.7),layout='constrained')
sel=abs(t)<.0055
axs[0].plot(t[sel]*1000,env[sel],color=BLUE,lw=2,label='输入包络')
axs[0].plot(t[sel]*1000,abs(out[sel]),color=ORANGE,lw=2,label='数值输出包络')
axs[0].plot(t[sel]*1000,abs(approx[sel]),'--',color=GREEN,lw=1.6,label='群延迟近似')
axs[0].axvline(0,color=BLUE,lw=.9,ls=':')
axs[0].axvline(tg0*1000,color=ORANGE,lw=.9,ls=':')
axs[0].set(title='（a）包络的延迟约为0.159 ms',xlabel='时间（ms）',ylabel='复音包幅度',ylim=(-.03,1.12))
axs[0].legend(fontsize=10,loc='upper left')
sel=abs(t)<.0016
axs[1].plot(t[sel]*1000,z.real[sel],color=BLUE,lw=1.8,label='输入波形')
axs[1].plot(t[sel]*1000,out.real[sel],color=ORANGE,lw=1.8,label='数值输出波形')
axs[1].plot(t[sel]*1000,approx.real[sel],'--',color=GREEN,lw=1.4,label='载波/包络分别延迟的近似')
axs[1].set(title='（b）载波相位改变−π/2：等效相位延迟0.250 ms',xlabel='时间（ms）',ylabel='实部波形',ylim=(-1.1,1.1))
axs[1].legend(fontsize=10,loc='lower left')
for ax in axs:grid(ax)
save(fig,'03-carrier-envelope',{'fs_Hz':fs,'record_samples':n,'carrier_Hz':carrier,'gaussian_sigma_s':sigma,'same_allpass_as_figure3':True,'finite_record_fft':True,'periodic_boundary_negligible_due_to_long_zero_tails':True,'input_normalization':'Gaussian complex-envelope peak = 1; no independent output scaling','relative_L2_error_of_narrowband_approximation':err,'sampled_envelope_peak_delay_ms':peak_delay*1000,'energy_relative_error':energy_error})

# 5: sum of direct and delayed paths; group delay from analytic differentiation.
freq=np.linspace(0,1000,10001)
T=.005; gain=.8;theta=2*np.pi*freq*T
mix=1+gain*np.exp(-1j*theta)
mix_gd=T*(gain**2+gain*np.cos(theta))/(1+gain**2+2*gain*np.cos(theta))
numeric=-np.gradient(np.unwrap(np.angle(mix)),freq)/(2*np.pi)
assert np.max(abs(numeric[1:-1]-mix_gd[1:-1])) < 3e-6
assert np.isclose(mix_gd[1000],-.020)
fig,axs=plt.subplots(2,1,figsize=(11,6.6),layout='constrained')
axs[0].plot(freq,20*np.log10(abs(mix)),color=BLUE,lw=1.8)
axs[0].set(title='（a）H(f) = 1 + 0.8 exp(−j2πfT)，T = 5 ms',ylabel='相对单位直达声的幅度级（dB）',ylim=(-16,7))
axs[0].annotate('梳齿间隔 1/T = 200 Hz',xy=(400,5.105),xytext=(510,1.3),arrowprops={'arrowstyle':'->','color':'#55636d'},fontsize=11)
axs[1].plot(freq,mix_gd*1000,color=ORANGE,lw=1.8,label='混合响应群延迟')
axs[1].axhline(5,color=GREEN,ls='--',lw=1.5,label='延迟支路本身：5 ms')
axs[1].axhline(0,color='#73818a',lw=.8)
axs[1].set(title='（b）干涉可产生局部负群延迟',xlabel='频率 f（Hz）',ylabel='群延迟（ms）',ylim=(-23,8))
axs[1].annotate('100 Hz处：−20 ms',xy=(100,-20),xytext=(170,-12),arrowprops={'arrowstyle':'->','color':ORANGE},fontsize=11,color=ORANGE)
axs[1].legend(fontsize=10,loc='lower right')
for ax in axs:ax.set_xlim(0,1000);grid(ax)
save(fig,'04-two-paths',{'direct_gain':1,'delayed_gain':gain,'path_delay_s':T,'comb_spacing_Hz':1/T,'notch_at_100Hz_delay_ms':mix_gd[1000]*1000,'magnitude_not_independently_normalized':True,'ear_canal_model':False,'maximum_finite_difference_error_s':float(np.max(abs(numeric[1:-1]-mix_gd[1:-1])))})

# Check digital units and a linear-phase FIR without inferring phase at its zeros.
b=signal.firwin(97,3000,fs=48000)
fcheck=np.array([100.,500.,1000.,2000.])
_,gd_samples=signal.group_delay((b,[1.]),w=fcheck,fs=48000)
assert np.allclose(gd_samples,48,atol=1e-8)
# Two-tone derivation: independently check phasor sum against shifted slow factor.
tt=np.linspace(-.02,.02,10001)
f1,f2=950.,1050.
w1,w2=2*np.pi*np.array([f1,f2]);wc=(w1+w2)/2;dw=w2-w1
p1,p2=-2*np.arctan(np.array([w1,w2])/a)
direct=np.real(((a-1j*w1)/(a+1j*w1))*np.exp(1j*w1*tt)+((a-1j*w2)/(a+1j*w2))*np.exp(1j*w2*tt))
envelope_form=2*np.cos((dw*tt+p2-p1)/2)*np.cos(wc*tt+(p1+p2)/2)
tone_error=float(np.max(abs(direct-envelope_form)))
assert tone_error<1e-11
convergence=[]
for spacing in [100.,10.,1.]:
    pair_w=2*np.pi*np.array([1000-spacing/2,1000+spacing/2])
    pair_phi=-2*np.arctan(pair_w/a)
    pair_delay=-np.diff(pair_phi)[0]/np.diff(pair_w)[0]
    convergence.append({'frequency_spacing_Hz':spacing,'finite_difference_delay_ms':float(pair_delay*1000),'absolute_error_ms':float(abs(pair_delay-1/a)*1000)})
assert all(convergence[k+1]['absolute_error_ms']<convergence[k]['absolute_error_ms'] for k in range(2))
report={'figures':manifest,'two_tone_check':{'frequencies_Hz':[f1,f2],'max_waveform_identity_error':tone_error,'group_delay_limit_ms':1000/a,'difference_quotient_convergence':convergence},'digital_FIR_check':{'fs_Hz':48000,'taps':97,'order':96,'frequencies_Hz':fcheck.tolist(),'group_delay_samples':gd_samples.tolist(),'group_delay_ms':(gd_samples/48000*1000).tolist()},'versions':{'numpy':np.__version__,'scipy':scipy.__version__,'matplotlib':matplotlib.__version__}}
(RESEARCH/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':len(manifest),'packet_relative_error':err,'FIR_delay_ms':(gd_samples/48000*1000).tolist()},indent=2))
