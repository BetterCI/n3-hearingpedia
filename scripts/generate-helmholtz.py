"""Original teaching plots; no listener data or reconstruction of a historical recording."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/hermann-von-helmholtz'; OUT.mkdir(parents=True,exist_ok=True)
RESEARCH=ROOT/'docs/research/hermann-von-helmholtz-2026-10-09'; RESEARCH.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':12,'svg.fonttype':'path','axes.spines.top':False,'axes.spines.right':False})
FS=48000; F0=200; colors=['#276582','#ad683c']
raw=[np.array([1,.45,.22,.12,.07,.04]),np.array([.45,.8,1,.8,.5,.25])]
amp=[a/np.sqrt(np.sum(a*a)/2) for a in raw]
t=np.arange(FS)/FS
signals=[sum(a[n-1]*np.cos(2*np.pi*n*F0*t) for n in range(1,7)) for a in amp]
assert all(np.isclose(np.sqrt(np.mean(x*x)),1) for x in signals)
assert all(np.allclose(np.abs(np.fft.rfft(x))[np.arange(1,7)*F0]/(FS/2),a) for x,a in zip(signals,amp))

def save(fig,name):
 for ext in ['svg','png']:
  p=OUT/(name+'.'+ext); fig.savefig(p,dpi=160,facecolor='white')
  if ext=='svg':p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
 plt.close(fig)

f,axes=plt.subplots(2,2,figsize=(11.5,7.4));f.subplots_adjust(left=.1,right=.97,top=.85,bottom=.18,wspace=.3,hspace=.65)
f.suptitle('相同基频，不同谐波幅度分配',fontsize=18,y=.97,fontweight='bold')
for i,(a,x) in enumerate(zip(amp,signals)):
 mask=t<.02
 axes[i,0].plot(t[mask]*1000,x[mask],color=colors[i],lw=1.4)
 axes[i,0].set(xlim=(0,20),ylim=(-3.5,3.5),xlabel='时间 / ms',ylabel='合成幅度 / 任意单位',title=f'（{chr(97+i*2)}）组 {"AB"[i]} 的波形')
 axes[i,1].bar(np.arange(1,7)*F0,a,width=65,color=colors[i])
 axes[i,1].set(xticks=np.arange(1,7)*F0,xlim=(100,1300),ylim=(0,1.6),xlabel='频率 / Hz',ylabel='谐波幅度 / 任意单位',title=f'（{chr(98+i*2)}）组 {"AB"[i]} 的幅度谱')
 for ax in axes[i]:ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
f.text(.5,.035,'基频 = 200 Hz；六个谐波；相位 = 0；两组 RMS = 1（不表示等响）\n原创教学计算，不是乐器实测或听者实验结果',ha='center',fontsize=11,color='#526472')
save(f,'harmonics')

x=np.cos(2*np.pi*440*t)+np.cos(2*np.pi*444*t)
envelope=2*np.abs(np.cos(np.pi*4*t))
identity=2*np.cos(2*np.pi*2*t)*np.cos(2*np.pi*442*t)
assert np.allclose(x,identity,atol=1e-12)
# Four amplitude-envelope maxima in the half-open interval [0,1).
peak_indices=np.array([0,12000,24000,36000]); assert np.allclose(envelope[peak_indices],2)
assert np.allclose(envelope[[6000,18000,30000,42000]],0,atol=1e-12)
spec=np.abs(np.fft.rfft(x))/(FS/2);assert np.isclose(spec[440],1) and np.isclose(spec[444],1) and spec[4]<1e-12
f,axes=plt.subplots(2,1,figsize=(11.5,7.4));f.subplots_adjust(left=.11,right=.96,top=.86,bottom=.16,hspace=.6)
f.suptitle('440 Hz + 444 Hz：每秒四次强弱起伏',fontsize=18,y=.97,fontweight='bold')
for i,(ax,lim) in enumerate(zip(axes,[(0,1),(.105,.145)])):
 mask=(t>=lim[0])&(t<=lim[1]);ax.plot(t[mask],x[mask],color=colors[0],lw=.55 if i==0 else 1.3)
 ax.plot(t[mask],envelope[mask],'--',color=colors[1],lw=2,label='包络边界')
 ax.plot(t[mask],-envelope[mask],'--',color=colors[1],lw=2)
 ax.set(xlim=lim,ylim=(-2.25,2.25),xlabel='时间 / s',ylabel='幅度 / 任意单位',title='（a）1 秒的叠加波形与包络' if i==0 else '（b）40 ms 局部放大');ax.grid(alpha=.2)
axes[0].legend(loc='upper right',fontsize=10)
f.text(.5,.035,'两分量各幅度 1；采样率 48 kHz；线性叠加、无噪声\n拍频 |444 − 440| = 4 Hz；声谱中没有新增的 4 Hz 纯音',ha='center',fontsize=11,color='#526472')
save(f,'beats')
manifest=[{'name':'harmonics','nature':'原创正弦合成教学图','fs_hz':FS,'f0_hz':F0,'raw_amplitudes':[a.tolist() for a in raw],'normalized_amplitudes':[a.tolist() for a in amp],'phases_rad':[0]*6,'rms':1,'checks':['RMS verified','FFT amplitude recovered'],'limits':'Not equal perceived loudness; not instrument or listener data','source':'helmholtz-tone-1895'},
 {'name':'beats','nature':'原创线性叠加教学图','fs_hz':FS,'frequencies_hz':[440,444],'amplitudes':[1,1],'beat_rate_hz':4,'envelope':'2*abs(cos(pi*4*t))','checks':['trigonometric identity','four peaks in half-open one-second interval','FFT no 4 Hz component'],'source':'helmholtz-tone-1895'}]
(RESEARCH/'figure-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('2 plots, SVG + PNG; analytic and spectral checks passed')
