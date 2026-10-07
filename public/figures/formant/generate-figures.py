from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import freqz,lfilter,spectrogram
ROOT=Path(__file__).parent
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'path','axes.unicode_minus':False})
BLUE='#235f83';RED='#b34c42';GREEN='#397666'; fs=16000
def save(fig,n):
    for ext in ['svg','png']:fig.savefig(ROOT/(n+'.'+ext),dpi=170,bbox_inches='tight',facecolor='white')
    plt.close(fig)
def filt(F,B):
    a=np.array([1.])
    for f,b in zip(F,B):
        r=np.exp(-np.pi*b/fs);theta=2*np.pi*f/fs
        a=np.convolve(a,[1,-2*r*np.cos(theta),r*r])
    return a
def response(F,B,f):
    a=filt(F,B)
    _,h=freqz([1],a,worN=2*np.pi*f/fs)
    return np.abs(h)
def synth(F,B,f0,d=.45):
    t=np.arange(round(fs*d))/fs
    source=sum(np.sin(2*np.pi*k*f0*t)/k for k in range(1,int(fs/2/f0)))
    y=lfilter([1],filt(F,B),source)
    fade=np.minimum(1,t/.025)*np.minimum(1,(d-t)/.025)
    y*=fade
    return .9*y/max(np.max(np.abs(y)),1e-12)
F=[700,1200,2500];B=[80,100,140];f=np.linspace(30,4000,5000)
h=response(F,B,f);harm=np.arange(120,4000,120)
src=-20*np.log10(harm/120); hd=20*np.log10(h/h.max()); out=src+20*np.log10(response(F,B,harm)/h.max())
fig,axs=plt.subplots(3,1,figsize=(10,6.5),sharex=True,layout='constrained')
axs[0].vlines(harm,-65,src,color=BLUE,lw=1.2);axs[0].set_title('A  周期声源：谐波间隔为基频 120 Hz',loc='left')
axs[1].plot(f,hd,color=GREEN,lw=2);axs[1].set_title('B  声道滤波模型：在共振附近增强',loc='left')
for j,fi in enumerate(F,1):
    axs[1].axvline(fi,color='#99b5aa',ls='--',lw=.8)
    level=20*np.log10(response(F,B,np.array([fi]))[0]/h.max())
    axs[1].text(fi+45,level+3,f'F{j}',color=GREEN,fontsize=10)
axs[2].vlines(harm,-65,out,color=BLUE,lw=1.2);axs[2].plot(f,-20*np.log10(f/120)+hd,color=RED,lw=1.5,label='声源谱倾斜 × 滤波响应');axs[2].legend(frameon=False,fontsize=9)
axs[2].set_title('C  输出：谐波幅度沿谱包络变化',loc='left')
for ax in axs:ax.set(ylim=(-65,8),ylabel='相对幅度（dB）',xlim=(0,4000))
axs[-1].set_xlabel('频率（Hz）');save(fig,'01-source-filter-spectrum')
fig,axs=plt.subplots(2,1,figsize=(10,5),sharex=True,layout='constrained')
for ax,f0 in zip(axs,[120,400]):
    freq=np.arange(f0,4000,f0)
    env=hd-20*np.log10(f/120)
    vals=20*np.log10(response(F,B,freq)/h.max())-20*np.log10(freq/120)
    ax.plot(f,env,color=GREEN,lw=1.8,label='相同的模型谱包络')
    ax.vlines(freq,-65,vals,color=BLUE,lw=1.4)
    for j,fi in enumerate(F,1):
        ax.axvline(fi,color='#b4bfc4',ls='--',lw=.8)
        ax.text(fi+35,1,f'F{j}',fontsize=10,color='#65737c')
    ax.set(title=f'基频 {f0} Hz：谐波采样'+('较密' if f0==120 else '较稀疏'),ylabel='相对幅度（dB）',ylim=(-65,8),xlim=(0,4000))
axs[0].legend(frameon=False,fontsize=9);axs[-1].set_xlabel('频率（Hz）');save(fig,'02-harmonic-sampling')
vowels={'i':([330,2300,3000],[70,110,150]),'a':([750,1200,2600],[90,120,160]),'u':([350,800,2400],[70,100,140])}
fig,ax=plt.subplots(figsize=(7.5,5),layout='constrained')
for label,(vf,vb) in vowels.items():
    ax.scatter(vf[1],vf[0],s=95,color=BLUE);ax.annotate(label,(vf[1],vf[0]),xytext=(9,7),textcoords='offset points',fontsize=15)
ax.set(xlim=(2600,500),ylim=(950,200),xlabel='第二共振峰 F2（Hz）',ylabel='第一共振峰 F1（Hz）',title='示意元音空间：横纵轴均反向排列')
ax.grid(alpha=.18);save(fig,'03-vowel-space')
segments=[];ranges=[];pos=0
for label,(vf,vb) in vowels.items():
    y=synth(vf,vb,130);segments.append(y);ranges.append((label,pos,pos+.45,vf));segments.append(np.zeros(round(.08*fs)));pos+=.53
y=np.concatenate(segments);t=np.arange(len(y))/fs
fig,axs=plt.subplots(3,1,figsize=(10,7),sharex=True,layout='constrained',gridspec_kw={'height_ratios':[.8,1.5,1.5]})
axs[0].plot(t,y,color=BLUE,lw=.45);axs[0].set(ylim=(-1,1),ylabel='相对幅度',title='A  合成元音 i、a、u：基频均为 130 Hz')
for ax,win,title in [(axs[1],.008,'B  短窗语谱图：便于观察宽带能量与起止'),(axs[2],.04,'C  长窗语谱图：可分辨较细的谐波条纹')]:
    ff,tt,ss=spectrogram(y,fs,nperseg=round(fs*win),noverlap=round(fs*win*.85),nfft=2048,window='hann',mode='magnitude')
    db=20*np.log10(np.maximum(ss,1e-12));db-=db.max()
    mesh=ax.pcolormesh(tt,ff,db,vmin=-65,vmax=0,cmap='Greys',shading='auto',rasterized=True)
    for label,start,end,vf in ranges:
        ax.text((start+end)/2,3500,label,ha='center',color=BLUE,fontsize=13,bbox={'facecolor':'white','alpha':.85,'edgecolor':'none'})
        if ax==axs[1]:
            for fi in vf:ax.plot([start+.04,end-.04],[fi,fi],ls='--',color=RED,lw=1.1)
    ax.set(ylim=(0,3800),ylabel='频率（Hz）',title=title)
axs[-1].set_xlabel('时间（s）');fig.colorbar(mesh,ax=axs[1:],label='相对谱幅度（dB）',fraction=.025,pad=.02)
save(fig,'04-synthetic-vowel-spectrogram')
fig,ax=plt.subplots(figsize=(9,4),layout='constrained');freq=np.linspace(600,1400,2000)
for bw,c in [(60,BLUE),(180,RED)]:
    db=-10*np.log10(1+(2*(freq-1000)/bw)**2)
    ax.plot(freq,db,color=c,lw=2,label=f'带宽 {bw} Hz')
    ax.plot([1000-bw/2,1000+bw/2],[-3.0103]*2,color=c,lw=3,marker='|',markersize=12)
ax.axhline(-3.0103,color='#919da5',ls='--',lw=.8)
ax.set(xlabel='频率（Hz）',ylabel='相对峰值幅度（dB）',ylim=(-25,2),title='理想单峰的中心频率与半功率带宽');ax.legend(frameon=False)
save(fig,'05-formant-bandwidth')
assert np.max(np.abs(y))<=1 and all(np.all(np.abs(np.roots(filt(vf,vb)))<1) for vf,vb in vowels.values())
(ROOT/'figure-verification.json').write_text(json.dumps({'figures':5,'type':'synthetic teaching data','sampleRate':fs,'waveformPeak':float(np.abs(y).max()),'spectrogramWindowSeconds':[.008,.04],'spectrogramF0':130,'spectrogramVowels':vowels,'fixedFilterPoleFrequencies':F,'fixedFilterBandwidthParameters':B,'harmonicSamplingF0':[120,400],'allFiltersStable':True,'waveformWithinUnitRange':True},ensure_ascii=False,indent=2),encoding='utf-8')
print('5 SVG/PNG pairs generated. Stable filters, normalized waveform confirmed.')
