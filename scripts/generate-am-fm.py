"""Original AM/FM teaching calculations; no listener measurements or model fitting."""
from pathlib import Path
import json, sys
import numpy as np
import scipy
from scipy import signal, special
from scipy.io import wavfile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1]
MEDIA='amplitude-and-frequency-modulation'
OUT=ROOT/'public/figures'/MEDIA
AUDIO=ROOT/'public/audio'/MEDIA
OUT.mkdir(parents=True,exist_ok=True)
AUDIO.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.unicode_minus':False,'svg.fonttype':'path','font.size':11})
FS=48000
B,O,G='#287da8','#d77537','#438872'
records={'nature':'original synthetic teaching calculations; not experimental results',
         'fs_hz':FS,'numpy_version':np.__version__,'scipy_version':scipy.__version__}

def save(fig,name,footer):
    fig.text(.5,.015,footer,ha='center',fontsize=10,color='#566774')
    fig.tight_layout(rect=(0,.07,1,.95))
    fig.savefig(OUT/(name+'.svg'),facecolor='white')
    p=OUT/(name+'.svg')
    p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(OUT/(name+'.png'),dpi=150,facecolor='white')
    plt.close(fig)

t=np.arange(FS)/FS
fc,fm,a,m,dev=1000,20,.2,.6,60
am=a*(1+m*np.cos(2*np.pi*fm*t))*np.cos(2*np.pi*fc*t)
fmwave=a*np.cos(2*np.pi*fc*t+(dev/fm)*np.sin(2*np.pi*fm*t))
fig,ax=plt.subplots(3,2,figsize=(12,8),sharex=True)
ix=t<.1
for j,(x,name,c) in enumerate([(am,'AM：幅度变化',B),(fmwave,'FM：频率变化',O)]):
    ax[0,j].plot(t[ix]*1000,x[ix],color=c,lw=.7)
    ax[0,j].set_title(name);ax[0,j].set_ylabel('声压 / Pa');ax[0,j].set_ylim(-.34,.34)
    env=a*(1+m*np.cos(2*np.pi*fm*t)) if j==0 else np.full_like(t,a)
    inst=np.full_like(t,fc) if j==0 else fc+dev*np.cos(2*np.pi*fm*t)
    ax[1,j].plot(t[ix]*1000,env[ix],color=c);ax[1,j].set_ylabel('模型幅度 / Pa');ax[1,j].set_ylim(0,.35)
    ax[2,j].plot(t[ix]*1000,inst[ix],color=c);ax[2,j].set_ylabel('瞬时频率 / Hz');ax[2,j].set_ylim(930,1070);ax[2,j].set_xlabel('时间 / ms')
    for q in ax[:,j]:q.grid(alpha=.2)
save(fig,'01-wave-envelope-frequency','fc = 1000 Hz，fm = 20 Hz；AM：m = 0.6；FM：Δf = 60 Hz、β = 3。两列载波幅度相同，RMS 不同。')
assert np.isclose(np.mean(am**2),a*a/2*(1+m*m/2),rtol=1e-10)
assert np.isclose(np.mean(fmwave**2),a*a/2,rtol=1e-10)
records['waveform']={'carrier_hz':fc,'modulation_hz':fm,'carrier_amplitude_pa':a,'am_depth':m,'fm_peak_deviation_hz':dev,'fm_index':dev/fm,
                     'am_mean_square_pa2':float(np.mean(am**2)),'fm_mean_square_pa2':float(np.mean(fmwave**2))}

k=np.arange(-8,9)
fig,axs=plt.subplots(3,1,figsize=(12,8),sharex=True)
checks=[]
for ax,name,beta in zip(axs,['AM：m = 0.3','FM：β = 0.3（Δf = 6 Hz）','FM：β = 3（Δf = 60 Hz）'],[None,.3,3]):
    if beta is None:
        coeff=np.where(k==0,1,np.where(abs(k)==1,.15,0))
        x=(1+.3*np.cos(2*np.pi*20*t))*np.cos(2*np.pi*1000*t)
    else:
        coeff=special.jv(k,beta)
        x=np.cos(2*np.pi*1000*t+beta*np.sin(2*np.pi*20*t))
        assert np.isclose(np.sum(special.jv(np.arange(-60,61),beta)**2),1,atol=1e-12)
    ft=np.fft.rfft(x)*2/len(x)
    actual=ft[(1000+k*20).astype(int)]
    err=float(np.max(abs(actual-coeff)))
    assert err<1e-10
    checks.append({'signal':name,'max_fft_coefficient_error':err})
    freqs=1000+k*20
    ax.vlines(freqs,0,coeff,color=[B if c>=0 else O for c in coeff],lw=2)
    ax.scatter(freqs,coeff,color=[B if c>=0 else O for c in coeff],s=20)
    ax.axhline(0,color='#71808a',lw=.8);ax.set_ylim(-.55,1.1);ax.set_title(name,loc='left');ax.set_ylabel('余弦系数 / A');ax.grid(alpha=.2)
axs[-1].set_xlabel('频率 / Hz（仅画出 k = −8…8；FM 仍有更远边带）')
save(fig,'02-sidebands','正负表示相位关系；负系数相当于相位差 π，不表示负功率。fc = 1000 Hz，fm = 20 Hz。')
records['sidebands']={'carrier_hz':1000,'modulation_hz':20,'drawn_orders':[-8,8],'checks':checks,'bessel_power_check_orders':[-60,60]}

t2=np.arange(FS*2)/FS
x=.2*np.cos(2*np.pi*1000*t2+6*np.sin(2*np.pi*5*t2))
f=np.fft.rfftfreq(len(x),1/FS)
fig,ax=plt.subplots(2,1,figsize=(12,7))
envs=[]
for cf,c in zip([940,1000,1060],[B,G,O]):
    h=np.exp(-.5*((f-cf)/70)**2)
    y=np.fft.irfft(np.fft.rfft(x)*h,n=len(x))
    env=abs(signal.hilbert(y));envs.append(env)
    ii=(f>=850)&(f<=1150)
    ax[0].plot(f[ii],h[ii],color=c,label=f'滤波中心 {cf} Hz')
    ix=t2<.4
    ax[1].plot(t2[ix],env[ix],color=c,label=f'滤波中心 {cf} Hz')
ax[0].axvspan(970,1030,color='#d5dee5',alpha=.4,label='瞬时频率范围');ax[0].set_xlabel('频率 / Hz');ax[0].set_ylabel('滤波幅度增益')
ax[1].axhline(.2,color='#71808a',ls='--',label='输入模型幅度');ax[1].set_xlabel('时间 / s');ax[1].set_ylabel('Hilbert 包络 / Pa');ax[1].set_ylim(0,.225)
for q in ax:q.legend(ncol=2,fontsize=10);q.grid(alpha=.2)
save(fig,'03-filter-conversion','FM：fc = 1000 Hz，fm = 5 Hz，Δf = 30 Hz。周期 FFT + 零相位高斯滤波，σ = 70 Hz；不是耳蜗模型。')
cor=float(np.corrcoef(envs[0],envs[2])[0,1]);assert cor<-.9
peaks=[]
for env in envs:
    spec=abs(np.fft.rfft(env-env.mean()));peaks.append(float(f[np.argmax(spec)]))
assert peaks==[5,10,5]
records['filter_conversion']={'carrier_hz':1000,'modulation_hz':5,'peak_deviation_hz':30,'gaussian_sigma_hz':70,
                             'filter_centres_hz':[940,1000,1060],'off_centre_envelope_correlation':cor,'dominant_envelope_frequencies_hz':peaks,
                             'implementation':'periodic FFT, real even zero-phase Gaussian response; not a causal cochlear filter'}

depth=np.linspace(0,1,201);rate=np.linspace(1,40,200)
fig,ax=plt.subplots(1,2,figsize=(12,5.5))
for amp,label,c in [(np.full_like(depth,.2),'固定载波幅度 A = 0.2 Pa',B),(.2/(1+depth),'固定最大包络 0.2 Pa',O),(.2/np.sqrt(1+depth**2/2),'固定 RMS = 0.2/√2 Pa',G)]:
    ax[0].plot(depth,amp/np.sqrt(2)*np.sqrt(1+depth**2/2),label=label,color=c)
ax[0].set_xlabel('AM 深度 m');ax[0].set_ylabel('周期平均 RMS / Pa');ax[0].set_title('“相同强度”需要指明约束')
ax[1].plot(rate,np.full_like(rate,20),label='固定 Δf = 20 Hz（β 随 fm 变化）',color=B)
ax[1].plot(rate,rate,label='固定 β = 1（Δf 随 fm 变化）',color=O)
ax[1].set_xlabel('FM 调制频率 fm / Hz');ax[1].set_ylabel('单侧峰值频偏 Δf / Hz');ax[1].set_title('“相同 FM 深度”有不同定义')
for q in ax:q.legend(fontsize=9,loc='best');q.grid(alpha=.2)
save(fig,'04-parameter-controls','左：满足周期平均条件的正弦 AM；右：β = Δf / fm。均为解析参数关系，不是听觉阈值曲线。')
records['parameter_controls']={'am_carrier_amplitude_pa':.2,'am_depth_range':[0,1],'fm_rate_range_hz':[1,40],'fixed_peak_deviation_hz':20,'fixed_fm_index':1}

ta=np.arange(2*FS)/FS;fade=np.ones(len(ta));n=int(.02*FS)
fade[:n]=.5-.5*np.cos(np.linspace(0,np.pi,n));fade[-n:]=fade[:n][::-1]
aud=[]
for rate in [5,40]:
    for mode in ['am','fm']:
        if mode=='am': raw=(1+.6*np.cos(2*np.pi*rate*ta))*np.cos(2*np.pi*1000*ta)
        else: raw=np.cos(2*np.pi*1000*ta+(30/rate)*np.sin(2*np.pi*rate*ta))
        raw*=fade;raw*=.1/np.sqrt(np.mean(raw**2))
        assert np.max(abs(raw))<1
        pcm=np.rint(raw*32767).astype(np.int16)
        name=f'{mode}-{rate}.wav';wavfile.write(AUDIO/name,FS,pcm)
        rms=float(np.sqrt(np.mean((pcm.astype(float)/32767)**2)));assert abs(rms-.1)<2e-5
        aud.append({'file':name,'carrier_hz':1000,'modulation_hz':rate,'am_depth':.6 if mode=='am' else None,
                    'fm_peak_deviation_hz':30 if mode=='fm' else None,'fm_index':30/rate if mode=='fm' else None,
                    'duration_s':2,'fade_ms':20,'digital_rms':rms,'digital_peak':float(np.max(abs(pcm.astype(float)/32767))),
                    'normalization':'whole-record digital RMS after fades; not calibrated SPL or equal loudness'})
records['audio']=aud
(OUT/'parameters.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(records,ensure_ascii=False,indent=2))
