from pathlib import Path
import numpy as np, matplotlib.pyplot as plt, json
from scipy.signal import correlate,correlation_lags,butter,sosfiltfilt
ROOT=Path(__file__).parent
plt.rcParams.update({'font.sans-serif':['Microsoft YaHei'],'axes.unicode_minus':False,'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'path','savefig.facecolor':'white'})
blue='#28688a';green='#317767';red='#b64e44';gray='#697982'
def save(fig,name):
    fig.savefig(ROOT/(name+'.svg'),bbox_inches='tight');fig.savefig(ROOT/(name+'.png'),dpi=150,bbox_inches='tight');plt.close(fig)
# Conceptual geometry and exact signal manipulations, not an HRTF calculation.
fig=plt.figure(figsize=(10,6.8));gs=fig.add_gridspec(2,2,height_ratios=[1,1.25]);a=fig.add_subplot(gs[0,:]);a.set_aspect('equal');a.set_xlim(-1.8,1.8);a.set_ylim(-.7,1.15);a.axis('off')
a.add_patch(plt.Circle((0,0),.48,fill=False,color=gray,lw=1.5));a.plot([-.48,.48],[0,0],'o',color=blue);a.text(-.62,-.25,'左耳',ha='center');a.text(.62,-.25,'右耳',ha='center');a.plot([0,.1,-.1,0],[.48,.59,.59,.48],color=gray);a.scatter([1.35],[.75],s=70,color=red);a.text(1.35,1,'右前方声源',ha='center')
for xy in [(-.48,0),(.48,0)]:a.annotate('',xy=xy,xytext=(1.3,.7),arrowprops={'arrowstyle':'->','color':gray,'lw':1.3})
a.text(-1.75,.9,'A  声源到两耳的传播路径不同',va='top');a.text(-1.65,-.57,'示意几何；箭头不表示真实绕射路径',fontsize=10,color=gray)
t=np.linspace(0,.006,1200);R=.8*np.sin(2*np.pi*500*t);L=.4*np.sin(2*np.pi*500*(t-.0003));a=fig.add_subplot(gs[1,0]);a.plot(t*1000,R,color=red,label='右耳');a.plot(t*1000,L,color=blue,label='左耳');a.set(xlabel='时间（ms）',ylabel='相对幅度',ylim=(-1,1),title='B  右耳领先 0.30 ms，右耳声级较高');a.legend(frameon=False)
a=fig.add_subplot(gs[1,1]);a.bar(['左耳','右耳'],[-6.0206,0],color=[blue,red],width=.5);a.set(ylabel='相对 RMS 声级（dB）',ylim=(-8,1),title='C  声级差由 RMS 幅度比计算');a.text(.5,-3,'右耳 − 左耳 = +6.02 dB',ha='center');fig.tight_layout();save(fig,'01-two-ear-cues')
# Ideal equalization/cancellation demo. Same fixed noise and signal in every input.
rng=np.random.default_rng(37);fs=16000;n=1600;tt=np.arange(n)/fs;noise=sosfiltfilt(butter(3,1800,fs=fs,output='sos'),rng.normal(size=n));noise=noise/np.max(np.abs(noise))*.55;s=.15*np.sin(2*np.pi*500*tt);left=noise+s;right_same=noise+s;right_anti=noise-s
fig,axs=plt.subplots(2,2,figsize=(10,6.2),sharex=True,sharey=True)
for a,data,title in [(axs[0,0],right_same,'A  N0S0：两耳噪声和目标均同相'),(axs[0,1],right_anti,'B  N0Sπ：噪声同相、目标反相')]:
    a.plot(tt[:320]*1000,left[:320],color=blue,label='左耳',lw=1);a.plot(tt[:320]*1000,data[:320],color=red,label='右耳',lw=.9,alpha=.8);a.set_title(title,fontsize=11);a.legend(frameon=False,ncol=2)
axs[1,0].plot(tt[:320]*1000,(left-right_same)[:320],color=green);axs[1,0].set_title('C  理想相减：共同噪声与目标均消失',fontsize=11)
axs[1,1].plot(tt[:320]*1000,(left-right_anti)[:320],color=green);axs[1,1].set_title('D  理想相减：共同噪声消失、目标保留',fontsize=11)
for a in axs.ravel():a.set_ylim(-1,1);a.set_ylabel('相对幅度')
for a in axs[1]:a.set_xlabel('时间（ms）')
fig.tight_layout();save(fig,'02-phase-and-cancellation')
# Explicit artificial threshold differences: use identical geometry for single-ear comparisons.
fig,axs=plt.subplots(1,2,figsize=(10,4.5),gridspec_kw={'width_ratios':[1.2,1]});a=axs[0];vals=[0,-4,2,-6];a.bar(np.arange(4),vals,color=[gray,blue,red,green],width=.55);a.axhline(0,color='#ccd3d7',lw=.8);a.set_xticks(range(4),['同位\n双耳','分离\n左单耳','分离\n右单耳','分离\n双耳']);a.set(ylabel='示意 SRT（dB SNR）',ylim=(-8,4),title='A  人工构造的配对测试条件')
for i,v in enumerate(vals):a.text(i,v+(.35 if v>=0 else -.8),f'{v:+d}',ha='center')
a=axs[1];a.barh([2,1,0],[6,2,6],color=[blue,green,gray],height=.5);a.set_yticks([2,1,0],['分离条件：左右单耳差','分离条件：超出较好单耳','同位至分离：双耳阈值差']);a.set(xlabel='阈值差（dB）',xlim=(0,8),title='B  对照不同，差值含义不同')
for y,v in zip([2,1,0],[6,2,6]):a.text(v+.15,y,str(v),va='center')
fig.tight_layout();save(fig,'03-benefit-baselines')
# Correlation convention matches C_LR(tau)=E[L(t)R(t-tau)].
fs=48000;n=24000;tt=np.arange(n)/fs;d=round(.0003*fs);src=sosfiltfilt(butter(4,[150,5000],btype='bandpass',fs=fs,output='sos'),rng.normal(size=n));l=np.r_[np.zeros(d),src[:-d]];r=src.copy();c=correlate(l,r,mode='full',method='fft')/np.sqrt(np.sum(l*l)*np.sum(r*r));lags=correlation_lags(n,n)/fs*1000;sel=np.abs(lags)<=3
fig,axs=plt.subplots(1,2,figsize=(10,4.2));axs[0].plot(lags[sel],c[sel],color=blue);axs[0].axvline(d/fs*1000,color=gray,ls='--');axs[0].set(title='A  同一宽带信号的延迟副本',xlabel='相关计算延迟 τ（ms）',ylabel='归一化互相关',ylim=(-1.05,1.05));axs[0].text(.55,.8,f'峰值约 +{d/fs*1000:.3f} ms',color=blue)
tau=np.linspace(-3,3,2000);cs=np.cos(2*np.pi*500*(tau*.001-d/fs));axs[1].plot(tau,cs,color=green);axs[1].axvline(d/fs*1000,color=gray,ls='--');axs[1].set(title='B  理想 500 Hz 正弦：周期性多峰',xlabel='相关计算延迟 τ（ms）',ylabel='无限长正弦的归一化互相关',ylim=(-1.05,1.05));fig.tight_layout();save(fig,'04-correlation-and-ambiguity')
# Independent gain and delay can alter ear-to-ear cues; ideal parameters, no commercial device data.
fig,axs=plt.subplots(1,2,figsize=(10,4.5));levels=np.linspace(35,90,200);leftgain=25-.4*(levels-35);rightgain=20-.2*(levels-35);inputILD=6;outILD=inputILD+rightgain-leftgain;a=axs[0];a.plot(levels,np.full_like(levels,inputILD),color=gray,ls='--',label='输入声级差');a.plot(levels,outILD,color=blue,label='加入两耳不同增益后');a.set(xlabel='左耳输入声级（dB，示意参考）',ylabel='右耳 − 左耳声级差（dB）',title='A  两耳增益之差会改变输出声级差');a.legend(frameon=False)
a=axs[1];lags0=[.3,.3+2-5,.3+2-2];a.bar(range(3),lags0,color=[gray,red,green],width=.5);a.axhline(0,color=gray,lw=.7);a.set_xticks(range(3),['输入','左延迟2 ms\n右延迟5 ms','两耳均\n延迟2 ms']);a.set(ylabel='左耳 − 右耳到达时差（ms）',ylim=(-3.5,1),title='B  附加延迟的差值改变输出时差')
for i,v in enumerate(lags0):a.text(i,v+(.12 if v>=0 else -.32),f'{v:+.1f}',ha='center')
fig.tight_layout();save(fig,'05-device-cue-changes')
assert max(np.max(np.abs(x)) for x in [L,R,left,right_same,right_anti,left-right_anti])<=1
assert np.argmax(c)==len(r)-1+d
report={'figureCount':5,'signalPeakMax':float(max(np.max(np.abs(x)) for x in [L,R,left,right_same,right_anti,left-right_anti])),'figure1ILDdB':float(20*np.log10(.8/.4)),'figure2InputTargetNoiseRmsMatched':True,'figure3SrtValues':[0,-4,2,-6],'figure4DelaySamples':d,'figure4DelayMs':d/fs*1000,'figure5OutputDelaysMs':lags0,'interpretation':'All figures are original synthetic teaching examples, not measured anatomy, human benefits, or commercial device output.'}
(ROOT/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
