from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.unicode_minus':False,'svg.fonttype':'path','savefig.facecolor':'white'})
OUT=Path(__file__).resolve().parent/'figures'
OUT.mkdir(parents=True,exist_ok=True)
blue='#24618c';orange='#b86a2a';gray='#666666'
def save(fig,name):
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight');fig.savefig(OUT/(name+'.png'),dpi=180,bbox_inches='tight');plt.close(fig)
def arrow(ax,a,b,**kw):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=13,color=gray,lw=1.4,**kw))
fig,ax=plt.subplots(figsize=(11.5,4.8));ax.set_xlim(0,12);ax.set_ylim(0,5);ax.axis('off')
labels=[('麦克风',.2,1.35),('数字处理',2.05,3.15),('受话器',5.7,1.35),('耳道声压叠加',7.6,1.75),('鼓膜与中耳\n→ 耳蜗',10,1.65)]
for txt,x,w in labels:
 ax.add_patch(Rectangle((x,2.2),w,1.25,fill=False,ec=blue,lw=1.4));ax.text(x+w/2,2.82,txt,ha='center',va='center',fontsize=12)
for a,b in [((1.55,2.83),(2.05,2.83)),((5.2,2.83),(5.7,2.83)),((7.05,2.83),(7.6,2.83)),((9.35,2.83),(10,2.83))]:arrow(ax,a,b)
ax.text(3.62,1.75,'方向性／降噪、分频压缩等\n处理顺序依设计而异',ha='center',va='top',fontsize=10)
ax.plot([.05,.05,8.48],[3.75,4.5,4.5],color=gray,lw=1.3);arrow(ax,(8.48,4.5),(8.48,3.45));ax.text(4.1,4.62,'环境声经通气孔或开放耳塞直接进入耳道',ha='center',fontsize=11)
ax.plot([6.38,6.38,.87],[2.2,.7,.7],color=orange,lw=1.3,ls='--');arrow(ax,(.87,.7),(.87,2.2),linestyle='--');ax.text(3.6,.36,'声学反馈路径：受话器输出重新到达麦克风',ha='center',color=orange,fontsize=10)
ax.text(.2,0,'概念图：声学路径与主要功能模块；不表示某一产品的完整电路或算法顺序。',fontsize=9,color=gray)
save(fig,'01-signal-and-acoustic-paths')
fig,axs=plt.subplots(1,2,figsize=(11.5,4.5));ax=axs[0];x=np.linspace(30,110,500);y=np.minimum(np.where(x<=50,x+30,80+(x-50)/2),105)
ax.plot(x,x+30,color=gray,ls=':',label='固定增益 30 dB');ax.plot(x,y,color=blue,lw=2,label='压缩 + 输出上限（示意）');ax.axvline(50,color='#aaa',lw=.8,ls='--');ax.axhline(105,color='#aaa',lw=.8,ls='--');ax.text(68,90,'压缩比 2∶1',rotation=22,color=blue);ax.set(xlim=(30,110),ylim=(55,120),xlabel='输入声压级（dB SPL）',ylabel='输出声压级（dB SPL）',title='A  稳态输入—输出关系');ax.legend(fontsize=9,loc='upper left');ax.grid(alpha=.15)
ax=axs[1];t=np.arange(0,2.6,.001);level=np.where((t>=.5)&(t<1.3),80,60);target=80+(level-50)/2-level
for ta,tr,label,col in [(.012,.08,'较快：12 / 80 ms',blue),(.08,.6,'较慢：80 / 600 ms',orange)]:
 g=np.zeros_like(t);g[0]=target[0]
 for i in range(1,len(t)):
  tau=ta if target[i]<g[i-1] else tr;alpha=np.exp(-.001/tau);g[i]=alpha*g[i-1]+(1-alpha)*target[i]
 ax.plot(t,g,label=label,c=col,lw=1.8)
ax.plot(t,target,c=gray,ls=':',label='稳态目标增益');ax.axvspan(.5,1.3,color='#eee',zorder=-2);ax.text(.9,26,'输入从 60 升至 80 dB SPL',ha='center',fontsize=9);ax.set(xlabel='时间（s）',ylabel='增益（dB）',ylim=(13,28),title='B  声级突变后的增益调整');ax.legend(fontsize=9,loc='lower right');ax.grid(alpha=.15)
fig.tight_layout();save(fig,'02-compression-level-and-time')
fig=plt.figure(figsize=(10.5,4.8));ax=fig.add_subplot(121,projection='polar');theta=np.linspace(0,2*np.pi,720);r=(1+np.cos(theta))/2
ax.plot(theta,np.ones_like(theta),ls='--',c=gray,label='理想全向');ax.plot(theta,r,c=blue,lw=2,label='理想心形方向性');ax.set_theta_zero_location('N');ax.set_theta_direction(-1);ax.set_ylim(0,1.12);ax.set_yticks([.25,.5,.75,1]);ax.set_yticklabels(['0.25','0.5','0.75','1']);ax.set_rlabel_position(125);ax.set_title('A  相对幅度响应（线性标度）',pad=22);ax.legend(loc='lower center',bbox_to_anchor=(.5,-.27),fontsize=10)
ax=fig.add_subplot(122);angles=np.array([0,60,90,120,150]);resp=(1+np.cos(np.deg2rad(angles)))/2;adv=-20*np.log10(resp);ax.plot(angles,adv,'o-',c=blue);ax.set(xticks=angles,xlabel='单一噪声的入射方位角（°）',ylabel='理想信噪比改善（dB）',ylim=(0,26),title='B  目标始终来自正前方 0°');ax.grid(alpha=.18);ax.text(.04,.96,'假设：无混响、无声学泄漏\n目标与噪声各一个远场声源\n不含设备噪声与头部散射',transform=ax.transAxes,va='top',fontsize=10)
fig.subplots_adjust(wspace=.4,bottom=.23,top=.84);save(fig,'03-directional-principle')
fig,axs=plt.subplots(2,1,figsize=(10,5.6),sharex=True);f=np.linspace(100,4000,5000)
for ax,tau,col in zip(axs,[.002,.006],[blue,orange]):
 a=.8;mag=20*np.log10(np.abs(1+a*np.exp(-2j*np.pi*f*tau))/(1+a));ax.plot(f/1000,mag,c=col,lw=1.25);ax.set(ylim=(-21,1),ylabel='相对幅度（dB）');ax.text(.98,.08,f'处理路径延迟 {tau*1000:.0f} ms；梳齿间隔 {1/tau:.0f} Hz',transform=ax.transAxes,ha='right',fontsize=10,bbox={'facecolor':'white','alpha':.9,'edgecolor':'none'});ax.grid(alpha=.18)
axs[0].set_title('相干直达声与延迟处理声叠加：简化的梳状滤波');axs[1].set(xlim=(.1,4),xlabel='频率（kHz）');fig.tight_layout();save(fig,'04-open-fitting-delay')
f=np.array([250,500,750,1000,1500,2000,3000,4000,6000]);target=np.array([70,75,78,81,85,88,91,90,84]);before=target+np.array([-1,-2,-3,-5,-8,-10,-12,-11,-9]);after=target+np.array([0,-1,1,-1,0,1,-1,-2,-1])
fig,axs=plt.subplots(1,2,figsize=(11.5,4.3),gridspec_kw={'width_ratios':[1.5,1]});ax=axs[0];ax.semilogx(f,target,'--',c=gray,label='示意目标');ax.semilogx(f,before,'o-',c=orange,label='调整前：高频输出不足');ax.semilogx(f,after,'s-',c=blue,label='调整后：更接近目标');ax.set(xlim=(225,6500),ylim=(55,100),ylabel='耳道输出声压级（dB SPL）',xlabel='频率（Hz）',title='A  真耳助听响应：输入总声级 65 dB SPL');ax.set_xticks([250,500,1000,2000,4000,6000]);ax.set_xticklabels(['250','500','1000','2000','4000','6000']);ax.grid(alpha=.2);ax.legend(fontsize=9,loc='lower left')
ax=axs[1];ax.axhline(0,c=gray,lw=.8);ax.semilogx(f,before-target,'o-',c=orange,label='调整前');ax.semilogx(f,after-target,'s-',c=blue,label='调整后');ax.set(xlim=(225,6500),ylim=(-15,4),xlabel='频率（Hz）',ylabel='相对目标的偏差（dB）',title='B  输出减去目标');ax.set_xticks([250,1000,4000]);ax.set_xticklabels(['250','1000','4000']);ax.grid(alpha=.2);ax.legend(fontsize=9,loc='lower left');fig.tight_layout();save(fig,'05-real-ear-verification')
print('Saved five figures as SVG and PNG.')
