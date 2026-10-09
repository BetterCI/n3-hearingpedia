"""Reproducible teaching calculations; no room, listener or scattering measurements."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/manfred-r-schroeder';OUT.mkdir(parents=True,exist_ok=True)
R=ROOT/'docs/research/manfred-r-schroeder-2026-10-09';R.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':13,'svg.fonttype':'path','axes.spines.top':False,'axes.spines.right':False})
BLUE='#276582';ORANGE='#ad683c';GREEN='#477e63';FS=48000
def save(fig,name):
 for ext in ['svg','png']:
  p=OUT/(name+'.'+ext);fig.savefig(p,dpi=140,facecolor='white')
  if ext=='svg':p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
 plt.close(fig)
def grid(ax):ax.grid(alpha=.18);ax.set_axisbelow(True)

t=np.arange(2*FS)/FS;T=.6;seed=1926
h=np.random.default_rng(seed).standard_normal(len(t))*np.exp(-3*np.log(10)*t/T)
e=np.cumsum((h*h)[::-1])[::-1];db=10*np.log10(e/e[0]);sel=(db>=-25)&(db<=-5)
b,a=np.polyfit(t[sel],db[sel],1);T20=-60/b
assert np.all(np.diff(e)<=0) and abs(T20-T)<.025
f,ax=plt.subplots(1,2,figsize=(12.8,6.5));f.subplots_adjust(left=.09,right=.97,top=.8,bottom=.21,wspace=.32)
f.suptitle('逆向积分：从起伏响应到能量衰减',fontsize=21,y=.96,fontweight='bold')
show=t<=.6;ax[0].plot(t[show],h[show],lw=.4,color=BLUE)
ax[0].set(xlim=(0,.6),xlabel='时间 / s',ylabel='响应幅度 / 任意单位',title='（a）合成的指数衰减响应')
ax[1].plot(t,db,color=BLUE,lw=2,label='逆向积分')
ax[1].plot(t,a+b*t,color=ORANGE,ls='--',lw=1.7,label=f'拟合：T20 = {T20:.3f} s')
ax[1].axhspan(-25,-5,color=ORANGE,alpha=.13)
ax[1].set(xlim=(0,.7),ylim=(-70,3),xlabel='时间 / s',ylabel='归一化能量 / dB',title='（b）衰减曲线与 T20 拟合')
ax[1].legend(loc='lower left',fontsize=11)
for p in ax:grid(p)
f.text(.5,.065,'设定衰减参数 0.60 s；48 kHz；2 s；随机种子 1926\n原创教学信号，不是房间实测；未模拟测量噪声或频带滤波',ha='center',fontsize=12,color='#526472')
save(f,'energy-decay')

N=20;F0=100;period=FS//F0;tp=np.arange(period)/FS;n=np.arange(1,N+1)
xs=[np.sqrt(2/N)*np.cos(2*np.pi*tp[:,None]*n*F0+C*np.pi*n*(n-1)/N).sum(axis=1) for C in [0,1,-1]]
rms=[float(np.sqrt(np.mean(x*x))) for x in xs];cf=[float(np.max(np.abs(x))/r) for x,r in zip(xs,rms)]
spectra=[np.abs(np.fft.rfft(x))[n]/(period/2) for x in xs]
assert np.allclose(rms,1) and all(np.allclose(s,np.sqrt(2/N),atol=1e-12) for s in spectra)
assert np.allclose(xs[1][(-np.arange(period))%period],xs[2],atol=1e-12)
f,ax=plt.subplots(2,2,figsize=(12.8,8.5));f.subplots_adjust(left=.09,right=.97,top=.85,bottom=.17,wspace=.27,hspace=.6)
f.suptitle('固定谐波幅度，只改变相位',fontsize=21,y=.97,fontweight='bold')
for i,(p,x,label,col) in enumerate(zip(ax.flat,xs,['余弦同相 C = 0','正相位 C = +1','负相位 C = −1'],[BLUE,ORANGE,GREEN])):
 p.plot(tp*1000,x,color=col,lw=1.7);p.set(xlim=(0,10),ylim=(-6.7,6.7),xlabel='时间 / ms',ylabel='幅度 / 任意单位',title=f'（{"abc"[i]}）{label}；CF = {cf[i]:.2f}');grid(p)
p=ax[1,1]
for spec,col,marker,label in zip(spectra,[BLUE,ORANGE,GREEN],['o','x','+'],['C = 0','C = +1','C = −1']):p.plot(n*F0,spec,color=col,marker=marker,ls='--',markersize=7,lw=1,label=label,markerfacecolor='none')
p.set(xlim=(0,2100),ylim=(0,.45),xlabel='频率 / Hz',ylabel='单边谐波幅度 / 任意单位',title='（d）相同的幅度谱');grid(p);p.legend(loc='lower right',fontsize=10)
f.text(.5,.045,'基频 100 Hz；20 个等幅谐波；48 kHz；三个信号 RMS = 1\n共用振幅尺度；CF = 采样峰值 / RMS；未经过听觉滤波或加入边缘处理',ha='center',fontsize=12,color='#526472')
save(f,'harmonic-phase')

p=7;indices=np.arange(p);residues=indices**2%p;wavelength=343/1000;depth=wavelength*residues/(2*p)
assert residues.tolist()==[0,1,4,2,2,4,1]
assert np.allclose(depth*100,[0,2.45,9.8,4.9,4.9,9.8,2.45])
gauss=np.abs(np.fft.fft(np.exp(2j*np.pi*residues/p)));assert np.allclose(gauss,np.sqrt(p))
f,ax=plt.subplots(1,2,figsize=(12.8,6.5));f.subplots_adjust(left=.08,right=.97,top=.79,bottom=.21,wspace=.3)
f.suptitle('二次剩余：数学序列到深度序列',fontsize=21,y=.96,fontweight='bold')
ax[0].bar(indices,residues,color=BLUE,width=.62);ax[0].set(xticks=indices,yticks=np.arange(5),ylim=(0,5),xlabel='序号 n',ylabel='二次剩余 s(n)',title='（a）s(n) = n² mod 7')
ax[1].bar(indices,depth*100,color=ORANGE,width=.62);ax[1].set(xticks=indices,ylim=(11,0),xlabel='槽序号 n（未规定槽宽）',ylabel='槽深 / cm（向下增加）',title='（b）d(n) = λ0 s(n) / (2p)')
for i,s in enumerate(residues):ax[0].text(i,s+.16,str(s),ha='center',fontsize=13)
for i,d in enumerate(depth*100):ax[1].text(i,d+.45,f'{d:.2f}',ha='center',va='top',fontsize=12)
for a in ax:grid(a)
f.text(.5,.055,'p = 7；设计频率 1 kHz；声速 343 m/s；设计波长 λ0 = 34.3 cm\n原创教学深度序列；不是制造图或实测散射指向图',ha='center',fontsize=12,color='#526472')
save(f,'quadratic-residue')
manifest=[{'name':'energy-decay','fs_hz':FS,'duration_s':2,'seed':seed,'decay_parameter_s':T,'fit_db':[-5,-25],'fitted_T20_s':T20,'checks':['reverse energy monotone','fit within 25 ms of set parameter'],'nature':'synthetic random-noise response with exponential envelope','source_ids':['room-acoustics-schroeder','room-acoustics-rew-rt']},
 {'name':'harmonic-phase','fs_hz':FS,'f0_hz':F0,'harmonics':N,'phase':'C*pi*n*(n-1)/N; cosine synthesis','C':[0,1,-1],'rms':rms,'sampled_crest_factor':cf,'checks':['equal FFT amplitudes','RMS unity','circular time reversal'],'source_ids':['schroeder-phase-1970','schroeder-green-2013']},
 {'name':'quadratic-residue','p':p,'design_frequency_hz':1000,'sound_speed_m_s':343,'residues':residues.tolist(),'depth_cm':(depth*100).tolist(),'checks':['residue sequence','depth mapping','DFT Gauss magnitudes equal sqrt(p)'],'limits':'Normal-incidence ideal relation; not a performance or manufacturing prediction','source_ids':['schroeder-diffusers-1979']}]
(R/'figure-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'T20':T20,'RMS':rms,'crest_factors':cf,'plots':3,'all_assertions':'passed'}))
