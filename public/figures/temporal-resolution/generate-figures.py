from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import lfilter
ROOT=Path(__file__).parent
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.unicode_minus':False,'svg.fonttype':'path','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':140})
C=['#236b8e','#b75a38','#537c57'];reports={}
def save(fig,name):
 fig.savefig(ROOT/(name+'.svg'),bbox_inches='tight');fig.savefig(ROOT/(name+'.png'),bbox_inches='tight');plt.close(fig)
def clean(ax):ax.grid(alpha=.16);ax.set_axisbelow(True)
fs=48000;t=np.arange(0,.1,1/fs);tm=t*1000;g=(t>=.046)&(t<.054)
env=np.ones_like(t);env[g]=0
for a,b,invert in [(.044,.046,True),(.054,.056,False)]:
 mask=(t>=a)&(t<b);u=(t[mask]-a)/(b-a);env[mask]=(.5+.5*np.cos(np.pi*u)) if invert else (.5-.5*np.cos(np.pi*u))
x=.85*np.sin(2*np.pi*1000*t)*env
y=.85*np.sin(2*np.pi*np.where(t<.05,1000,2300)*t)*env
fig,axs=plt.subplots(3,1,figsize=(9.3,7.2),layout='constrained')
for ax,s,title in zip(axs,[x,y,env],['A  同频带标记声：前后均为 1 kHz','B  不同频带标记声：1 kHz → 2.3 kHz','C  幅度门控：完全静默段与边沿分开定义']):
 ax.plot(tm,s,color=C[0],lw=.9);ax.axvspan(46,54,color=C[1],alpha=.13);ax.set_title(title,loc='left',fontsize=12);ax.set_xlim(30,70);ax.set_ylim((-1,1) if ax!=axs[2] else (-.08,1.15));ax.set_ylabel('相对幅度');clean(ax)
axs[2].annotate('完全静默 8 ms',xy=(50,.12),xytext=(50,.62),ha='center',arrowprops={'arrowstyle':'->','color':C[1]},color=C[1]);axs[-1].set_xlabel('时间 / ms')
save(fig,'01-gap-markers');reports['gap']={'silent_ms':float(g.sum()/fs*1000),'ramp_ms':2,'peak':float(max(abs(x).max(),abs(y).max()))}
# First-order causal smoothing of amplitude gate, explicitly a teaching model.
t=np.arange(0,.08,1/fs);u=np.ones_like(t);u[(t>=.035)&(t<.043)]=0
fig,axs=plt.subplots(1,2,figsize=(10,4.2),layout='constrained')
for tau,c in zip([.002,.008],C):
 a=np.exp(-1/(fs*tau));v,_=lfilter([1-a],[1,-a],u,zi=[a]);axs[0].plot(t*1000,v,label=f'时间常数 {tau*1000:g} ms',color=c,lw=2)
axs[0].plot(t*1000,u,'--',color='#85919b',label='输入幅度门控');axs[0].set(xlim=(27,59),ylim=(-.05,1.08),xlabel='时间 / ms',ylabel='相对幅度门控响应',title='A  8 ms 间隙的平滑响应');axs[0].legend(fontsize=9)
f=np.geomspace(1,500,250)
for tau,c in zip([.002,.008],C):axs[1].semilogx(f,20*np.log10(1/np.sqrt(1+(2*np.pi*f*tau)**2)),color=c,label=f'{tau*1000:g} ms',lw=2)
axs[1].set(xlabel='调制频率 / Hz',ylabel='幅度传递增益 / dB',title='B  同一平滑器的频率响应');axs[1].legend(fontsize=9)
for ax in axs:clean(ax)
save(fig,'02-temporal-smoothing');reports['smoothing']={'tau_ms':[2,8],'model':'first-order causal low-pass; not threshold data'}
fig,axs=plt.subplots(3,1,figsize=(9.3,7),layout='constrained');t=np.arange(0,.25,1/fs)
for ax,(m,fm) in zip(axs,[(.2,10),(.8,10),(.8,40)]):
 e=(1+m*np.cos(2*np.pi*fm*t))/(1+m);s=e*np.sin(2*np.pi*700*t)
 assert abs(s).max()<=1+1e-12
 ax.plot(t*1000,s,color=C[0],lw=.55,alpha=.7);ax.plot(t*1000,e,color=C[1],lw=1.5);ax.plot(t*1000,-e,color=C[1],lw=1.5);ax.set(xlim=(0,250),ylim=(-1.03,1.03),ylabel='相对幅度',title=f'调制深度 m = {m:g}，调制频率 {fm:g} Hz');clean(ax)
axs[-1].set_xlabel('时间 / ms');save(fig,'03-modulation');reports['modulation']={'carrier_Hz':700,'peak_normalized':True,'conditions':[[.2,10],[.8,10],[.8,40]]}
fig,ax=plt.subplots(figsize=(8.4,4.5),layout='constrained');d=np.linspace(0,16,400)
for scale,c,label in [(5,C[0],'示例曲线 A'),(9,C[1],'示例曲线 B')]:
 p=.5+.48*(1-np.exp(-(d/scale)**3));ax.plot(d,p*100,color=c,lw=2,label=label)
 criterion=.75;threshold=scale*(-np.log(1-(criterion-.5)/.48))**(1/3)
 ax.plot([threshold,threshold],[50,75],'--',color=c);ax.scatter([threshold],[75],color=c,zorder=4)
 ax.text(threshold+.3,56,f'{threshold:.1f} ms',color=c)
ax.axhline(75,color='#66727c',ls=':',label='本图采用的 75% 判据');ax.axhline(50,color='#aeb6bc',ls='--');ax.set(xlim=(0,16),ylim=(47,100),xlabel='间隙时长 / ms',ylabel='正确率 / %',title='二选一任务中的心理测量函数（合成示例）');ax.legend(loc='lower right',fontsize=10);clean(ax);save(fig,'04-psychometric');reports['psychometric']={'chance':.5,'lapse':.02,'criterion':.75,'simulated':True}
fig,axs=plt.subplots(3,1,figsize=(9.2,6.7),layout='constrained');t=np.linspace(0,150,1501)
for ax,title,a,b in zip(axs,['A  间隙检测：是否出现短暂停顿？','B  顺序辨别：高音和低音谁先出现？','C  双耳相关变化：两耳均有声，关系短暂改变'],[(0,65),(15,55),(0,150)],[(75,150),(70,110),(0,150)]):
 ax.set(xlim=(0,150),ylim=(0,2.5),yticks=[.65,1.65]);clean(ax);ax.set_title(title,loc='left',fontsize=12)
 if ax==axs[0]:
  ax.broken_barh([(0,65),(75,75)],(.3,.7),facecolors=C[0]);ax.set_yticklabels(['同一标记声','']);ax.axvspan(65,75,color=C[1],alpha=.12)
 elif ax==axs[1]:
  ax.broken_barh([(15,40)],(1.3,.7),facecolors=C[1]);ax.broken_barh([(70,40)],(.3,.7),facecolors=C[0]);ax.set_yticklabels(['低音','高音'])
 else:
  ax.broken_barh([(0,150)],(.3,.7),facecolors=C[0],alpha=.7);ax.broken_barh([(0,150)],(1.3,.7),facecolors=C[0],alpha=.7);ax.axvspan(65,85,color=C[1],alpha=.45);ax.set_yticklabels(['右耳有声','左耳有声']);ax.text(75,2.22,'相关性改变',ha='center',fontsize=10)
axs[-1].set_xlabel('时间 / ms');save(fig,'05-task-boundaries');reports['task_boundaries']={'schematic':True,'binaural_gap':'interaural correlation change, no silence'}
(ROOT/'figure-verification.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf8')
print('5 SVG + 5 PNG generated; amplitude bounds checked')
