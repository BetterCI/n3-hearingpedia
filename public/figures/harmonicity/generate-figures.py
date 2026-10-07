from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import stft
ROOT=Path(__file__).parent
plt.rcParams.update({'font.family':'Microsoft YaHei','svg.fonttype':'path','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.unicode_minus':False})
B='#245c85';O='#bc6137';G='#68757d';fs=24000;t=np.arange(fs)/fs
def synth(freq,a,phase=None,time=t):
 return np.sum(np.asarray(a)[:,None]*np.cos(2*np.pi*np.asarray(freq)[:,None]*time+(np.zeros(len(freq)) if phase is None else phase)[:,None]),axis=0)
def save(fig,name):
 fig.savefig(ROOT/(name+'.svg'),bbox_inches='tight');fig.savefig(ROOT/(name+'.png'),dpi=150,bbox_inches='tight');plt.close(fig)
 p=ROOT/(name+'.svg');p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
def wave(ax,x,title,color=B):
 ax.plot(t[:360]*1000,x[:360],color=color,lw=1);ax.set(xlim=(0,15),ylim=(-1,1),xlabel='时间（ms）',ylabel='相对幅度',title=title)
 ax.axhline(0,color=G,lw=.5)
 for k in (5,10):ax.axvline(k,color=G,lw=.7,ls=':')
n=np.arange(1,9);f=n*200;a=1/n;x=synth(f,a);y=synth(f[2:],a[2:]);scale=max(abs(x).max(),abs(y).max())/.9
fig,axs=plt.subplots(2,2,figsize=(10,6),layout='constrained')
for row,(freq,amp,signal,label) in enumerate([(f,a,x,'完整序列'),(f[2:],a[2:],y,'缺少第 1、2 谐波')]):
 ax=axs[row,0];ax.vlines(freq,0,amp,color=B,lw=2);ax.scatter(freq,amp,color=B,s=14);ax.set(xlim=(0,1800),ylim=(0,1.1),xlabel='频率（Hz）',ylabel='分量幅度（统一尺度）',title=label)
 ax.axvline(200,color=G,ls=':',lw=1);wave(axs[row,1],signal/scale,'共同周期为 5 ms')
save(fig,'01-harmonic-series')
env=lambda freq:.04+.85*np.exp(-.5*((freq-600)/110)**2)+.60*np.exp(-.5*((freq-1600)/180)**2)
fig=plt.figure(figsize=(10,7),layout='constrained');gs=fig.add_gridspec(2,2,height_ratios=(1,1.5));grid=np.linspace(0,3000,1000)
for col,f0 in enumerate((100,200)):
 ax=fig.add_subplot(gs[0,col]);freq=np.arange(1,int(3000/f0)+1)*f0;ax.plot(grid,env(grid),color=G,ls='--',label='同一谱包络');ax.vlines(freq,0,env(freq),color=B,lw=1.4)
 for c in (600,1600):ax.axvline(c,color=O,lw=.8,ls=':')
 ax.set(xlim=(0,3000),ylim=(0,1),xlabel='频率（Hz）',ylabel='幅度',title=f'基频 {f0} Hz');ax.legend(fontsize=9)
tv=np.arange(int(fs*1.5))/fs;f0=100+100*tv/1.5;phase=2*np.pi*(100*tv+100*tv**2/3);voice=sum(env(k*f0)*np.cos(k*phase) for k in range(1,41));voice/=np.max(abs(voice))
freq,tm,z=stft(voice,fs=fs,window='hann',nperseg=1920,noverlap=1680,boundary=None);db=20*np.log10(np.maximum(abs(z),1e-12)/abs(z).max())
ax=fig.add_subplot(gs[1,:]);p=ax.pcolormesh(tm,freq,db,cmap='magma',vmin=-65,vmax=0,shading='auto',rasterized=True);ax.set(ylim=(0,3000),xlim=(0,1.5),xlabel='时间（s）',ylabel='频率（Hz）',title='合成有声信号：基频由 100 Hz 连续升至 200 Hz')
for c in (600,1600):ax.axhline(c,color='#b7e1df',ls='--',lw=.9)
fig.colorbar(p,ax=ax,label='相对幅度级（dB）');save(fig,'02-harmonics-formants')
phase=np.pi*n*(n-1)/8;xp=synth(f,a,phase);fm=f.copy();fm[2]=620;xm=synth(fm,a);scale=max(np.max(abs(q)) for q in (x,xp,xm))/.9
fig,axs=plt.subplots(2,2,figsize=(10,6.5),layout='constrained')
for ax,other,title in [(axs[0,0],xp,'相位改变：频率与分量幅度相同'),(axs[0,1],xm,'失谐：600 Hz 分量移至 620 Hz')]:
 wave(ax,x/scale,title);ax.plot(t[:360]*1000,other[:360]/scale,color=O,lw=.9,alpha=.85);ax.legend(['原信号','零线','原周期边界','原周期边界','改变后'],fontsize=8) if False else None
 for line in ax.lines[2:4]:line.set_color(O)
 ax.text(.98,.95,'蓝：原信号　橙：改变后',transform=ax.transAxes,ha='right',va='top',fontsize=9)
axs[1,0].vlines(f,0,a,color=B,lw=2);axs[1,0].scatter(f,a,color=O,s=30,facecolors='none');axs[1,0].set(xlabel='频率（Hz）',ylabel='分量幅度',title='两套相位的幅度谱重合',xlim=(0,1800))
ax=axs[1,1];ax.vlines([600,620],0,[a[2],a[2]],color=[B,O],lw=2);ax.set(xlim=(450,750),ylim=(0,.45),xlabel='频率（Hz）',ylabel='分量幅度',title='第 3 分量的谱线偏移');ax.annotate('600 → 620 Hz',xy=(620,.34),xytext=(660,.39),ha='center',arrowprops={'arrowstyle':'->','color':G});save(fig,'03-phase-mistuning')
fig,axs=plt.subplots(2,2,figsize=(10,6.5),layout='constrained');nf=np.arange(1,51)*100;outputs=[];weights=[];widths=[]
for fc in (600,3000):
 width=24.7*(4.37*fc/1000+1);w=np.exp(-4*np.log(2)*((nf-fc)/width)**2);weights.append(w);widths.append(width);outputs.append(np.sum(w[:,None]*np.exp(2j*np.pi*nf[:,None]*t),axis=0))
scale=max(abs(z.real).max() for z in outputs)/.9
for col,fc in enumerate((600,3000)):
 ax=axs[0,col];xx=np.linspace(fc-500,fc+500,1000);ax.plot(xx,np.exp(-4*np.log(2)*((xx-fc)/widths[col])**2),color=G);ax.vlines(nf,0,weights[col],color=B);ax.set(xlim=(fc-500,fc+500),ylim=(0,1.1),xlabel='频率（Hz）',ylabel='假设幅度权重',title=f'中心 {fc} Hz；示意半高全宽 {widths[col]:.1f} Hz')
 ax=axs[1,col];ax.plot(t[:480]*1000,outputs[col].real[:480]/scale,color=B,lw=.7);ax.plot(t[:480]*1000,abs(outputs[col][:480])/scale,color=O,lw=1.2);ax.set(xlim=(0,20),ylim=(-1,1),xlabel='时间（ms）',ylabel='相对幅度',title='加权分量之和（蓝）与解析包络（橙）')
save(fig,'04-resolvability')
u=y;v=synth(fm[2:],a[2:]);lagmax=int(.015*fs);corr=[]
for sig in (u,v):
 corr.append(np.array([1 if k==0 else np.dot(sig[k:],sig[:-k])/np.sqrt(np.dot(sig[k:],sig[k:])*np.dot(sig[:-k],sig[:-k])) for k in range(lagmax+1)]))
k=fs//200;levels=[]
for sig in (u,v):
 residual=sig[k:]-sig[:-k];ratio=np.mean(residual**2)/np.mean(sig[k:]**2);levels.append(10*np.log10(max(ratio,1e-10)))
fig,axs=plt.subplots(1,2,figsize=(10,4),layout='constrained');ax=axs[0]
for c,color,label in zip(corr,(B,O),('理想谐波','600 → 620 Hz')):ax.plot(np.arange(lagmax+1)/fs*1000,c,color=color,label=label)
ax.axvline(5,color=G,ls='--',lw=.8);ax.set(xlabel='延迟（ms）',ylabel='归一化相关',xlim=(0,15),ylim=(-1,1.08));ax.legend(fontsize=9)
ax=axs[1];ax.bar([0,1],levels,color=[B,O],width=.55);ax.set(xticks=[0,1],xticklabels=['理想谐波','600 → 620 Hz'],ylim=(-105,2),ylabel='延迟相减后有效值级（dB，相对输入）');ax.axhline(0,color=G,lw=.7)
for i,value in enumerate(levels):ax.text(i,value+3,'≤ −100 dB' if i==0 else f'{value:.1f} dB',ha='center',fontsize=10)
save(fig,'05-period-models')
assert np.max(abs(u[k:]-u[:-k]))<1e-10
assert np.max(abs(v[k:]-v[:-k]))>.01
assert np.allclose(np.mean(x*x),np.mean(xp*xp),atol=1e-10)
report={'samplingRate':fs,'waveformAmplitudeLimit':[-1,1],'periodMs':5,'phaseRmsEqual':True,'mistunedCommonPeriodMs':50,'stftWindowMs':80,'stftHopMs':10,'illustrativeGaussianFwhmHz':widths,'cancellationRelativeDb':levels,'figures':5,'note':'理想合成例；简化高斯权重不是实测听觉滤波器。'}
(ROOT/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(report,ensure_ascii=False))
