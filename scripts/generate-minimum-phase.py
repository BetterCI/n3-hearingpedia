"""Analytic teaching examples; no measured or clinical data."""
from pathlib import Path
import json
import numpy as np
import scipy
from scipy import signal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/minimum-phase-system'
REC=ROOT/'docs/research/minimum-phase-2026-10-29'
OUT.mkdir(parents=True,exist_ok=True); REC.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':12,'svg.fonttype':'path','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False,'svg.hashsalt':'minimum-phase'})
B,O,G='#22658c','#b45b36','#397a66'
def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),facecolor='white',metadata={'Date':None})
    fig.savefig(OUT/(name+'.png'),facecolor='white',dpi=140)
    plt.close(fig)

w=np.linspace(0,np.pi,4097)
hm=np.array([1.,-.8]); hn=np.array([.8,-1.])
_,Hm=signal.freqz(hm,worN=w); _,Hn=signal.freqz(hn,worN=w)
err=float(np.max(abs(abs(Hm)-abs(Hn))))
assert err<1e-12
fig,ax=plt.subplots(1,3,figsize=(13,4.4),layout='constrained')
ax[0].plot(w/np.pi,20*np.log10(abs(Hm)),color=B,label='最小相位 [1, −0.8]')
ax[0].plot(w/np.pi,20*np.log10(abs(Hn)),color=O,ls='--',label='非最小相位 [0.8, −1]')
ax[0].set(title='（a）幅度相同',xlabel='归一化角频率 ω/π',ylabel='幅度（dB）');ax[0].legend(fontsize=9)
for H,c,l in [(Hm,B,'最小相位'),(Hn,O,'非最小相位')]:
    ax[1].plot(w/np.pi,np.unwrap(np.angle(H)),color=c,label=l)
ax[1].set(title='（b）相位不同',xlabel='归一化角频率 ω/π',ylabel='相位（rad）');ax[1].legend()
for h,c,offset,l in [(hm,B,-.07,'最小相位'),(hn,O,.07,'非最小相位')]:
    ax[2].vlines(np.arange(2)+offset,0,h,color=c,lw=3,label=l);ax[2].plot(np.arange(2)+offset,h,'o',color=c)
ax[2].axhline(0,color='gray',lw=.7);ax[2].set(title='（c）能量先后分布不同',xlabel='样本 n（横向微移便于区分）',ylabel='脉冲响应',xticks=[0,1],xlim=(-.3,1.3));ax[2].legend(fontsize=10)
for a in ax:a.grid(alpha=.15)
save(fig,'01-same-magnitude')

fig,ax=plt.subplots(1,2,figsize=(11,4.4),layout='constrained')
t=np.linspace(0,2*np.pi,300)
ax[0].plot(np.cos(t),np.sin(t),color='gray',lw=1)
ax[0].plot([.8],[0],'o',color=B,label='反射后零点：0.8');ax[0].plot([1.25],[0],'o',mfc='white',mec=O,label='原零点：1.25')
ax[0].annotate('',xy=(.83,.05),xytext=(1.23,.05),arrowprops={'arrowstyle':'->','color':O})
ax[0].axhline(0,color='gray',lw=.5);ax[0].axvline(0,color='gray',lw=.5)
ax[0].set(aspect='equal',xlim=(-1.4,1.6),ylim=(-1.25,1.25),xlabel='Re(z)',ylabel='Im(z)',title='（a）零点经单位圆反射');ax[0].legend(fontsize=10,loc='lower left')
gd_m=signal.group_delay((hm,[1]),w=w)[1];gd_n=signal.group_delay((hn,[1]),w=w)[1]
gd_a=(1-.8**2)/(1+.8**2-1.6*np.cos(w))
assert np.max(abs(gd_n-gd_m-gd_a))<1e-11
ax[1].plot(w/np.pi,gd_m,color=B,label='最小相位');ax[1].plot(w/np.pi,gd_n,color=O,label='非最小相位');ax[1].plot(w/np.pi,gd_a,color=G,ls='--',label='两者之差：全通群延迟')
ax[1].set(title='（b）最小是相同幅度下的比较',xlabel='归一化角频率 ω/π',ylabel='群延迟（样本）');ax[1].legend(fontsize=10);ax[1].grid(alpha=.15)
save(fig,'02-zeros-delay')

# Even-N real-cepstrum reconstruction of the nonminimum-phase two-tap FIR.
N=4096; mag=abs(np.fft.fft(hn,N));c=np.fft.ifft(np.log(mag)).real
cm=np.zeros(N);cm[0]=c[0];cm[1:N//2]=2*c[1:N//2];cm[N//2]=c[N//2]
recon=np.fft.ifft(np.exp(np.fft.fft(cm))).real
recon_error=float(np.max(abs(recon[:2]-hm)));tail=float(np.linalg.norm(recon[2:]))
assert recon_error<1e-12 and tail<1e-12
fig,ax=plt.subplots(1,2,figsize=(11,4.3),layout='constrained')
ns=np.arange(-15,16);ax[0].stem(ns,c[ns%N],linefmt=B,markerfmt='o',basefmt=' ')
ax[0].set(title='（a）实倒谱：正负倒频对称',xlabel='倒频索引 q（样本）',ylabel='实倒谱')
ax[1].stem(ns,cm[ns%N],linefmt=O,markerfmt='o',basefmt=' ')
ax[1].set(title='（b）构造因果复倒谱',xlabel='倒频索引 q（样本）',ylabel='重建用倒谱')
for a in ax:a.grid(alpha=.15)
save(fig,'03-cepstrum')

radii=np.array([.5,.8,.95,.99])
fig,ax=plt.subplots(1,2,figsize=(11,4.3),layout='constrained')
for r in radii:
    g=r**np.arange(150)
    ax[0].plot(np.arange(150),g,label=f'r = {r:g}')
ax[0].set(title='（a）稳定逆的尾部也可能很长',xlabel='样本 n',ylabel='逆系统脉冲响应 rⁿ');ax[0].legend(fontsize=10)
ax[1].plot(radii,20*np.log10(1/(1-radii)),'o-',color=O)
ax[1].set(title='（b）低频逆增益随零点靠近单位圆增大',xlabel='零点半径 r',ylabel='直流逆增益（dB）')
for a in ax:a.grid(alpha=.15)
save(fig,'04-inverse-conditioning')
report={'nature':'Analytic teaching examples, no measurements','versions':{'numpy':np.__version__,'scipy':scipy.__version__,'matplotlib':matplotlib.__version__},'same_magnitude_error':err,'group_delay_difference_error':float(np.max(abs(gd_n-gd_m-gd_a))),'dc_delays_samples':{'minimum':float(gd_m[0]),'nonminimum':float(gd_n[0]),'allpass':float(gd_a[0])},'early_energy':[1.,.64],'total_energy':1.64,'cepstrum':{'N':N,'coefficient_error':recon_error,'tail_l2':tail},'inverse_dc_gain_db':dict(zip(map(str,radii),map(float,20*np.log10(1/(1-radii))))),'figures':sorted(p.name for p in OUT.glob('*.svg'))}
(REC/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
