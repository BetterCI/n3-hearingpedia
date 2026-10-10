"""Original analytic teaching figures; no measured or perceptual data."""
from pathlib import Path
import json
import shutil
import sys
import wave
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / 'public/figures/pure-and-complex-tones'
AUDIO = ROOT / 'public/audio/pure-and-complex-tones'
FIG.mkdir(parents=True, exist_ok=True)
AUDIO.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.unicode_minus':False,'svg.fonttype':'path','font.size':11})
C=['#287da8','#d77537','#438872','#985e9c']
FS=48000
def signal(t, freqs, amps=None, phases=None, rms=.1):
    freqs=np.asarray(freqs)
    amps=np.ones(len(freqs)) if amps is None else np.asarray(amps)
    phases=np.zeros(len(freqs)) if phases is None else np.asarray(phases)
    scale=rms/np.sqrt(np.sum(amps**2)/2)
    return scale*np.sum(amps[:,None]*np.cos(2*np.pi*freqs[:,None]*t+phases[:,None]),axis=0),amps*scale
def save(fig,name,footer):
    fig.text(.5,.016,footer,ha='center',fontsize=10,color='#566774')
    fig.tight_layout(rect=(0,.065,1,.95))
    fig.savefig(FIG/(name+'.svg'),facecolor='white')
    fig.savefig(FIG/(name+'.png'),dpi=160,facecolor='white')
    plt.close(fig)

t=np.arange(960)/FS
cases=[('纯音：400 Hz',[400],[1]),('谐波复合音：200、400、600 Hz',[200,400,600],[1,.5,1/3]),('缺失基频：600、800、1000 Hz',[600,800,1000],[1,1,1]),('非谐波例：600、800、1000√2 Hz',[600,800,1000*np.sqrt(2)],[1,1,1])]
fig,ax=plt.subplots(4,2,figsize=(12,9))
for row,(title,freqs,amps) in enumerate(cases):
    x,a=signal(t,freqs,amps)
    ax[row,0].plot(t*1000,x,color=C[row],lw=1.3)
    ax[row,0].set(title=title,ylabel='相对幅度',xlim=(0,20),ylim=(-.3,.3))
    ax[row,0].grid(alpha=.2)
    ax[row,1].stem(freqs,a,linefmt=C[row],markerfmt='o',basefmt=' ')
    ax[row,1].set(title='生成模型中的分量（不是短窗 FFT）',ylabel='分量峰值幅度',xlim=(0,1600),ylim=(0,.16))
    ax[row,1].grid(alpha=.2)
ax[-1,0].set_xlabel('时间（ms）');ax[-1,1].set_xlabel('频率（Hz）')
fig.suptitle('一个波形，可以含一个或多个正弦分量',fontsize=18)
save(fig,'01-components','原创解析教学图｜稳态理论 RMS 均为 0.1｜右列谱线来自生成参数，不是听者感知数据')

n=np.arange(1,9); phi=-np.pi*n*(n-1)/8
t1=np.arange(FS)/FS
x0,a=signal(t1,200*n)
x1,_=signal(t1,200*n,phases=phi)
rms0=float(np.sqrt(np.mean(x0*x0)));rms1=float(np.sqrt(np.mean(x1*x1)))
peak0=float(np.max(np.abs(x0)));peak1=float(np.max(np.abs(x1)))
assert np.isclose(rms0,.1) and np.isclose(rms1,.1)
assert np.allclose(np.abs(np.fft.rfft(x0)),np.abs(np.fft.rfft(x1)),atol=1e-8)
fig,ax=plt.subplots(2,2,figsize=(12,6.8))
for i,(x,title,peak) in enumerate([(x0,'分量余弦相位均为 0',peak0),(x1,'按二次规则分布相位',peak1)]):
    ax[i,0].plot(t1[:720]*1000,x[:720],color=C[i],lw=1.5)
    ax[i,0].set(title=f'{title}｜峰值 {peak:.3f}，RMS 0.100',ylabel='相对幅度',ylim=(-.43,.43),xlim=(0,15))
    ax[i,1].stem(200*n,a,linefmt=C[i],markerfmt='o',basefmt=' ')
    ax[i,1].set(title='相同分量频率与幅度',ylabel='分量峰值幅度',xlim=(0,1800),ylim=(0,.06))
    for z in ax[i]:z.grid(alpha=.2)
ax[-1,0].set_xlabel('时间（ms）');ax[-1,1].set_xlabel('频率（Hz）')
fig.suptitle('幅度频谱相同，相位仍能改变波形与峰值',fontsize=18)
save(fig,'02-phase','原创解析教学图｜F0 = 200 Hz，第 1—8 谐波等幅｜理论 RMS 相等，不按各自峰值归一化')

tb=np.arange(int(.5*FS))/FS
xb,ab=signal(tb,[450,456])
env=2*ab[0]*np.abs(np.cos(np.pi*6*tb))
assert np.max(np.abs(xb))<=2*ab[0]+1e-12
fig,ax=plt.subplots(2,1,figsize=(12,7),gridspec_kw={'height_ratios':[2,1]})
ax[0].plot(tb*1000,xb,color=C[0],lw=.6);ax[0].plot(tb*1000,env,color=C[1],lw=2);ax[0].plot(tb*1000,-env,color=C[1],lw=2)
ax[0].set(title='450 Hz + 456 Hz：幅度包络每秒重复 6 次',xlabel='时间（ms）',ylabel='相对幅度',xlim=(0,500));ax[0].grid(alpha=.2)
ax[1].stem([450,456],ab,linefmt=C[0],markerfmt='o',basefmt=' ')
ax[1].set(title='线性叠加仍只含 450 与 456 Hz；6 Hz 是包络重复率',xlabel='频率（Hz）',ylabel='分量峰值幅度',xlim=(0,500),ylim=(0,.12));ax[1].grid(alpha=.2)
fig.suptitle('拍音：变化的包络不等于新增差频谱线',fontsize=18)
save(fig,'03-beats','原创解析教学图｜等幅、同一接收通道、线性相加｜有符号调制因子为 3 Hz，非负包络拍率为 6 Hz')

N=2400;tw=np.arange(N)/FS; freq=1007
y=np.cos(2*np.pi*freq*tw)
windows={'矩形窗':np.ones(N),'周期 Hann 窗':.5-.5*np.cos(2*np.pi*np.arange(N)/N)}
fig,ax=plt.subplots(1,2,figsize=(12,5.5))
for i,(title,w) in enumerate(windows.items()):
    ax[0].plot(tw*1000,y*w,color=C[i],label=title,lw=1)
    f=np.fft.rfftfreq(N*16,1/FS)
    amp=2*np.abs(np.fft.rfft(y*w,n=N*16))/np.sum(w)
    ax[1].plot(f,20*np.log10(np.maximum(amp,1e-8)),color=C[i],label=title,lw=1.5)
ax[0].set(title='同一 1007 Hz 正弦，观察 50 ms',xlabel='时间（ms）',ylabel='相对幅度',xlim=(0,50));ax[0].grid(alpha=.2)
ax[1].axvline(freq,color='#777777',ls=':',lw=1)
ax[1].set(title='按窗幅度增益校正的单边谱',xlabel='频率（Hz）',ylabel='相对峰值幅度（dB）',xlim=(800,1200),ylim=(-85,3));ax[1].grid(alpha=.2)
for z in ax:z.legend()
fig.suptitle('有限观察窗会使单一载频的频谱展宽',fontsize=18)
save(fig,'04-windowing','原创教学计算｜fs = 48 kHz，N = 2400，原始频点间隔 20 Hz｜16 倍零填充只使曲线采样更密')

audio_records=[]
ta=np.arange(int(1.2*FS))/FS
specs=[('pure-400','400 Hz 纯音',[400],None,None),('complex-200','200 Hz 谐波复合音',[200,400,600],[1,.5,1/3],None),('phase-zero','八谐波余弦同相',200*n,None,None),('phase-quadratic','八谐波二次相位',200*n,None,phi),('beats-6','450 与 456 Hz 拍音',[450,456],None,None)]
ramp_n=int(.02*FS); ramp=.5-.5*np.cos(np.pi*np.arange(ramp_n)/(ramp_n-1))
for name,label,freqs,amps,phases in specs:
    z,_=signal(ta,freqs,amps,phases)
    z[:ramp_n]*=ramp;z[-ramp_n:]*=ramp[::-1]
    assert np.max(np.abs(z))<.95
    pcm=np.round(z*32767).astype('<i2')
    with wave.open(str(AUDIO/(name+'.wav')),'wb') as wf:
        wf.setnchannels(1);wf.setsampwidth(2);wf.setframerate(FS);wf.writeframes(pcm.tobytes())
    audio_records.append({'file':name+'.wav','label':label,'samples':len(z),'sample_rate':FS,'duration_s':1.2,'ramp_ms':20,'theoretical_steady_rms':.1,'file_rms':float(np.sqrt(np.mean(z*z))),'file_peak':float(np.max(np.abs(z)))})
params={'data_type':'original analytic teaching models, not experiments','numpy_version':np.__version__,'matplotlib_version':matplotlib.__version__,'sample_rate':FS,'phase':{'F0_Hz':200,'harmonics':n.tolist(),'rule':'phi_n = -pi*n*(n-1)/8, cosine convention','rms_zero':rms0,'rms_quadratic':rms1,'peak_zero':peak0,'peak_quadratic':peak1,'crest_factor_zero':peak0/rms0,'crest_factor_quadratic':peak1/rms1},'beats':{'frequencies_Hz':[450,456],'signed_modulator_Hz':3,'envelope_rate_Hz':6},'window':{'frequency_Hz':1007,'N':N,'duration_s':.05,'bin_spacing_Hz':20,'zero_padding_factor':16,'amplitude_correction':'2*abs(rfft(x*w))/sum(w), interior positive frequencies'},'audio':audio_records,'checks':['phase FFT magnitudes equal','phase RMS 0.1','beats bounded by analytic envelope','audio does not clip']}
(FIG/'parameters.json').write_text(json.dumps(params,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
shutil.copy2(__file__,FIG/'generate-tones.py')
print(json.dumps({'figures':4,'audio_files':5,'phase':params['phase']},ensure_ascii=False))
