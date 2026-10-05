from pathlib import Path
import json, hashlib
import numpy as np
from scipy.signal import hilbert
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

OUT=Path(__file__).resolve().parent
font=FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':font.get_name(),'font.size':10,'svg.fonttype':'none',
 'axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False,
 'figure.facecolor':'white','savefig.facecolor':'white','path.simplify':True})
blue,orange,green,ink='#286f9b','#b37528','#45785a','#26323c'
def save(fig,name):
 svg=OUT/(name+'.svg')
 fig.savefig(svg,bbox_inches='tight')
 svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8',newline='\n')
 fig.savefig(OUT/(name+'.png'),bbox_inches='tight',dpi=180)
 plt.close(fig)
def axis(ax,title,lim=(0,100)):
 ax.set(title=title,xlim=lim,xlabel='时间（毫秒）',ylabel='相对幅度',ylim=(-1.08,1.08),yticks=[-1,0,1])
 ax.grid(alpha=.13)

fs=48000;t=np.arange(fs)/fs
a=(1+.7*np.cos(2*np.pi*20*t))/1.7
c=np.cos(2*np.pi*400*t);x=a*c
z=hilbert(x);ah=np.abs(z);ch=np.cos(np.angle(z))
fig,axs=plt.subplots(3,1,figsize=(10,6.4),layout='constrained')
sel=t<=.1;tt=t[sel]*1000
axs[0].plot(tt,x[sel],color=ink,lw=.9,label='原波形')
axs[0].plot(tt,a[sel],color=orange,lw=1.7,label='包络及其负值')
axs[0].plot(tt,-a[sel],color=orange,lw=1.2,ls='--')
axis(axs[0],'A  同一信号中的幅度起伏与快速振荡')
fig.legend(*axs[0].get_legend_handles_labels(),frameon=False,loc='lower center',bbox_to_anchor=(.5,-.055),ncol=2,fontsize=9)
axs[1].plot(tt,a[sel],color=orange,lw=1.7)
axis(axs[1],'B  时域包络：每秒起伏20次');axs[1].set(ylim=(0,1.08),yticks=[0,.5,1])
axs[2].plot(tt,c[sel],color=blue,lw=1)
axis(axs[2],'C  归一化精细结构：每秒振荡400次')
save(fig,'01-envelope-tfs-decomposition')

# Exact ideal separation of two discrete components; not an empirical cochlear filter.
x1=.5*np.cos(2*np.pi*900*t);x2=.5*np.cos(2*np.pi*1000*t);pair=x1+x2
ep=np.abs(hilbert(pair));sel=t<=.04;tt=t[sel]*1000
fig,axs=plt.subplots(3,1,figsize=(10,6.4),layout='constrained')
axs[0].plot(tt,pair[sel],color=ink,lw=.85)
axs[0].plot(tt,ep[sel],color=orange,lw=1.6)
axs[0].plot(tt,-ep[sel],color=orange,lw=1,ls='--')
axis(axs[0],'A  同带保留900和1000赫兹：包络每10毫秒重复一次',(0,40))
for ax,xx,f in [(axs[1],x1,900),(axs[2],x2,1000)]:
 ax.plot(tt,xx[sel],color=blue,lw=.9)
 ax.axhline(.5,color=orange,lw=1.6);ax.axhline(-.5,color=orange,lw=1,ls='--')
 axis(ax,f'分开分析：仅保留{f}赫兹，包络恒为0.5',(0,40))
axs[1].set_title('B  '+axs[1].get_title());axs[2].set_title('C  '+axs[2].get_title())
save(fig,'02-bandwidth-and-beating')

# Constant-amplitude FM through a specified, zero-phase Gaussian magnitude response.
fm=50.;fc=1000.;beta=2.
phase=2*np.pi*fc*t+beta*np.sin(2*np.pi*fm*t)
xfm=np.cos(phase);efm=np.abs(hilbert(xfm))
freq=np.fft.rfftfreq(len(t),1/fs)
H=np.exp(-.5*((freq-1100)/80)**2)
y=np.fft.irfft(np.fft.rfft(xfm)*H,n=len(t));ey=np.abs(hilbert(y))
fi=fc+beta*fm*np.cos(2*np.pi*fm*t)
sel=t<=.06;tt=t[sel]*1000
fig,axs=plt.subplots(3,1,figsize=(10,6.4),layout='constrained')
axs[0].plot(tt,xfm[sel],color=ink,lw=.65)
axs[0].plot(tt,efm[sel],color=orange,lw=1.5)
axis(axs[0],'A  输入：等幅调频信号，解析包络约为1',(0,60))
axs[1].plot(tt,fi[sel],color=blue,lw=1.6)
axs[1].set(xlim=(0,60),ylim=(870,1130),yticks=[900,1000,1100],xlabel='时间（毫秒）',ylabel='瞬时频率（赫兹）',title='B  输入相位的变化：瞬时频率在900—1100赫兹之间变化')
axs[1].grid(alpha=.13)
axs[2].plot(tt,y[sel],color=ink,lw=.65)
axs[2].plot(tt,ey[sel],color=green,lw=1.6)
axs[2].plot(tt,-ey[sel],color=green,lw=1,ls='--')
axis(axs[2],'C  经过非平坦频率响应后：输出出现幅度起伏',(0,60))
save(fig,'03-filtering-creates-envelope')

tau=.00025;f=500.
left=np.cos(2*np.pi*f*t);right=np.cos(2*np.pi*f*(t-tau))
fig,axs=plt.subplots(2,1,figsize=(10,4.8),layout='constrained')
sel=t<=.1
axs[0].plot(t[sel]*1000,a[sel],color=blue,lw=2.7,label='左耳包络')
axs[0].plot(t[sel]*1000,a[sel],color=orange,ls='--',lw=1.5,label='右耳包络（相同）')
axis(axs[0],'A  两耳使用相同包络');axs[0].set(ylim=(0,1.08),yticks=[0,.5,1])
sel=t<=.006
axs[1].plot(t[sel]*1000,left[sel],color=blue,lw=1.5,label='左耳精细结构')
axs[1].plot(t[sel]*1000,right[sel],color=orange,lw=1.5,ls='--',label='右耳精细结构')
axis(axs[1],'B  500赫兹精细结构具有45°耳间相位差',(0,6))
ha,la=axs[0].get_legend_handles_labels();hb,lb=axs[1].get_legend_handles_labels()
fig.legend(ha+hb,la+lb,frameon=False,loc='lower center',bbox_to_anchor=(.5,-.13),ncol=2,fontsize=9)
save(fig,'04-binaural-envelope-and-phase')

checks={'sample_rate_Hz':fs,'duration_s':1,'am_fc_Hz':400,'am_fm_Hz':20,'am_depth':.7,
 'am_envelope_error_max':float(np.max(abs(ah-a))),'am_reconstruction_error_max':float(np.max(abs(x-ah*ch))),
 'all_waveform_peaks':{k:float(np.max(abs(v))) for k,v in {'am':x,'carrier':c,'two_tone':pair,'tone_900':x1,'tone_1000':x2,'fm_input':xfm,'fm_output':y,'left_carrier':left,'right_carrier':right}.items()},
 'two_tone_envelope_error_max':float(np.max(abs(ep-abs(np.cos(2*np.pi*50*t))))),
 'fm_input_envelope_ripple_max':float(np.max(abs(efm-1))), 'fm_output_envelope_range':[float(ey.min()),float(ey.max())],
 'filter_magnitude_center_Hz':1100,'filter_magnitude_sigma_Hz':80,'filter_phase':'zero phase; periodic FFT demonstration',
 'binaural_carrier_Hz':500,'carrier_delay_s':tau,'binaural_phase_difference_deg':360*f*tau,
 'data_status':'Original analytic teaching signals; no human/animal measurements or fitted perception outcomes.'}
assert checks['am_envelope_error_max']<1e-10 and checks['am_reconstruction_error_max']<1e-10
assert checks['two_tone_envelope_error_max']<1e-10 and checks['fm_input_envelope_ripple_max']<1e-10
assert all(v<=1+1e-10 for v in checks['all_waveform_peaks'].values())
assert np.ptp(ey)>.5
(OUT/'figure-verification.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf8')
manifest=[{'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source':'Original Hearingpedia teaching diagram; build-figures.py','data':'analytic synthetic signals, not measurements'} for p in OUT.glob('*.svg')]
(OUT/'image-sources.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(checks))
