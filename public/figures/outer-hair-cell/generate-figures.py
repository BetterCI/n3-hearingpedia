from pathlib import Path
import numpy as np,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse,Polygon,FancyArrowPatch
ROOT=Path(__file__).parent
plt.rcParams.update({'font.family':'Microsoft YaHei','svg.fonttype':'path','font.size':10,'axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B='#285f83';O='#b9613b';G='#627078';T='#347b70'
def save(fig,name):
 fig.savefig(ROOT/(name+'.svg'),bbox_inches='tight');fig.savefig(ROOT/(name+'.png'),bbox_inches='tight',dpi=160);plt.close(fig)
 p=ROOT/(name+'.svg');p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
def arrow(ax,start,end,color=G,style='->'):
 ax.add_patch(FancyArrowPatch(start,end,arrowstyle=style,mutation_scale=12,lw=1.3,color=color))
def label(ax,text,xy,position):ax.annotate(text,xy=xy,xytext=position,ha='center',va='center',arrowprops={'arrowstyle':'-','color':G,'lw':.8},fontsize=10)
# 图 1 采用 Zha 等（2012）开放获取论文原图，来源见 image-sources.json。
v=np.linspace(-120,120,1201);s=25.;p=1/(1+np.exp(-v/s));length=1-.03*p;cnl=4*p*(1-p)
fig,axs=plt.subplots(1,2,figsize=(10,4.1),layout='constrained')
axs[0].plot(v,length,color=B,lw=2);axs[0].set(xlabel='相对模型中点的电压（mV）',ylabel='示意相对长度',ylim=(.965,1.005));axs[0].text(-105,1.002,'较超极化：较长',fontsize=10);axs[0].text(25,.978,'较去极化：较短',fontsize=10)
axs[1].plot(v,cnl,color=O,lw=2);axs[1].set(xlabel='相对模型中点的电压（mV）',ylabel='归一化非线性电容项',ylim=(0,1.1))
for ax in axs:ax.axvline(0,color=G,ls=':',lw=1)
save(fig,'02-voltage-motility')
freq=np.linspace(.3,1.7,1400);zetaA=.035;zetaP=.25
resp=lambda z:1/np.sqrt((1-freq**2)**2+(2*z*freq)**2)
inp=np.linspace(-80,80,801);a=10**(inp/20);gain=1+99/(1+a**(2/3));out=20*np.log10(a*gain)
fig,axs=plt.subplots(1,2,figsize=(10,4.2),layout='constrained')
axs[0].plot(freq,20*np.log10(resp(zetaA)),color=B,label='较小阻尼');axs[0].plot(freq,20*np.log10(resp(zetaP)),color=O,label='较大阻尼');axs[0].set(xlabel='频率 / 共振频率',ylabel='响应幅度级（dB，任意共同参考）',xlim=(.3,1.7));axs[0].legend(fontsize=9)
axs[1].plot(inp,out,color=B,label='输入相关的示意增益');axs[1].plot(inp,inp,color=O,ls='--',label='线性参考：输出级 = 输入级');axs[1].set(xlabel='输入幅度级（dB，任意参考）',ylabel='输出幅度级（dB，同一参考）',xlim=(-80,80));axs[1].legend(fontsize=9)
save(fig,'03-gain-compression')
fig=plt.figure(figsize=(10,6),layout='constrained');gs=fig.add_gridspec(2,3,height_ratios=(1,1));tt=np.linspace(0,1,2000,endpoint=False);velocity=np.cos(2*np.pi*tt);powers=[]
for col,phase in enumerate((0,np.pi/2,np.pi)):
 ax=fig.add_subplot(gs[0,col]);force=np.cos(2*np.pi*tt+phase);powers.append(float(np.mean(force*velocity)));ax.plot(tt,velocity,color=B,lw=1.5,label='速度');ax.plot(tt,force,color=O,ls='--',lw=1.3,label='力');ax.set(xlim=(0,1),ylim=(-1.05,1.05),xlabel='时间 / 周期',ylabel='归一化幅度',title=f'力—速度相位差 {int(phase/np.pi*180)}°');ax.legend(fontsize=8,loc='lower left')
ax=fig.add_subplot(gs[1,:]);ax.bar([0,1,2],powers,color=[T,G,O],width=.5);ax.axhline(0,color=G,lw=.7);ax.set(xticks=[0,1,2],xticklabels=['0°：正平均功率','90°：零平均功率','180°：负平均功率'],ylim=(-.65,.65),ylabel='平均功率（任意单位）')
for i,value in enumerate(powers):ax.text(i,value+(.04 if value>=0 else -.07),f'{value:.1f}',ha='center')
save(fig,'04-phase-power')
fs=48000;t=np.arange(fs)/fs;x=.4*(np.cos(2*np.pi*2000*t)+np.cos(2*np.pi*2400*t));y=x+.3*x**3
spec=lambda sig:2*abs(np.fft.rfft(sig))/len(sig);xx=spec(x);yy=spec(y);freqs=np.fft.rfftfreq(len(t),1/fs);ref=xx[2000]
fig=plt.figure(figsize=(10,6.3),layout='constrained');gs=fig.add_gridspec(2,2,height_ratios=(1.5,1))
for col,(specv,title) in enumerate([(xx,'输入：2000 与 2400 Hz 双音'),(yy,'输出：示意三次非线性')]):
 ax=fig.add_subplot(gs[0,col]);ids=np.flatnonzero((specv>ref*1e-5)&(freqs>=800)&(freqs<=4200));levels=20*np.log10(specv[ids]/ref);ax.vlines(freqs[ids],-80,levels,color=B,lw=1.7);ax.set(xlim=(800,4200),ylim=(-80,8),xlabel='频率（Hz）',ylabel='幅度级（dB，相对输入主分量）',title=title)
 ax.axvline(1600,color=O,lw=.8,ls=':')
 if col==1:ax.annotate(r'$2f_1-f_2=1600$ Hz',xy=(1600,20*np.log10(yy[1600]/ref)),xytext=(1000,-12),arrowprops={'arrowstyle':'->','color':O},fontsize=9)
ax=fig.add_subplot(gs[1,:]);ax.set(xlim=(-.5,10.5),ylim=(-1.5,2.4));ax.axis('off')
for xpos,text in [(0,'声源与探头'),(3,'耳道／中耳'),(6,'耳蜗来源'),(10,'记录分析')]:ax.text(xpos,.65,text,ha='center',fontsize=11)
for start,end in [((.4,1.35),(2.6,1.35)),((3.4,1.35),(5.6,1.35))]:arrow(ax,start,end,B)
ax.text(3,1.9,'刺激正向进入',ha='center',color=B)
for start,end in [((5.6,-.2),(3.4,-.2)),((2.6,-.2),(.4,-.2))]:arrow(ax,start,end,O)
ax.text(3,-.7,'发射经传播返回',ha='center',color=O)
arrow(ax,(.2,-1.1),(9.7,-1.1),G);ax.text(7,-.7,'麦克风信号 → 分析',ha='center',fontsize=10,color=G)
save(fig,'05-emission-measurement')
assert np.all(np.diff(length)<0);assert np.isclose(cnl.max(),1)
assert np.all(np.diff(out)>0)
assert np.allclose(powers,[.5,0,-.5],atol=1e-12)
assert yy[1600]>ref*.001 and xx[1600]<1e-10
report={'figures':5,'originalFigures':4,'sourcedFigures':1,'allData':'图 2—5 为原创数学示意；图 1 为公开论文原图','motilitySlopeSign':'depolarization shortens','boltzmannScaleMv':s,'illustrativeLengthRange':[float(length.min()),float(length.max())],'compressionOutputMonotonic':True,'powerMeans':powers,'intermodulationHz':1600,'intermodulationDb':float(20*np.log10(yy[1600]/ref)),'normalizedWaveformRange':[-1,1]}
(ROOT/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(report,ensure_ascii=False))
