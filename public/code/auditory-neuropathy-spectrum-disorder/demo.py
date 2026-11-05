"""Original ANSD teaching figures; no patient data or clinical prediction.

Python 3.11 + NumPy + Matplotlib. Run from any directory.
The numeric demonstration is a linear sum of shifted Gaussian pulses, not an ABR model.
"""
from pathlib import Path
import json, re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

HERE=Path(__file__).resolve().parent
OUT=HERE.parents[1]/'figures'/'auditory-neuropathy-spectrum-disorder'
OUT.mkdir(parents=True,exist_ok=True)
available={f.name for f in font_manager.fontManager.ttflist}
font=next((f for f in ['Microsoft YaHei','Noto Sans CJK SC','SimHei'] if f in available),None)
if not font: raise RuntimeError('Install a Chinese font: Microsoft YaHei or Noto Sans CJK SC')
plt.rcParams.update({'font.family':font,'font.size':16,'axes.titlesize':18,'axes.labelsize':16,
 'xtick.labelsize':14,'ytick.labelsize':14,'legend.fontsize':13,'svg.fonttype':'none',
 'svg.hashsalt':'hearingpedia-ansd-20261106','axes.unicode_minus':False,
 'axes.spines.top':False,'axes.spines.right':False})
BLUE='#2769a0'; ORANGE='#bb6229'; GREEN='#397e6a'; GRAY='#647181'; INK='#22344b'

def canvas(title):
    fig,ax=plt.subplots(figsize=(14,7),dpi=100)
    fig.subplots_adjust(left=.05,right=.95,bottom=.14,top=.84)
    ax.set(xlim=(0,100),ylim=(0,100));ax.axis('off')
    fig.suptitle(title,x=.055,y=.96,ha='left',fontsize=25,fontweight='bold',color=INK)
    return fig,ax

def box(ax,x,y,w,h,label,color=BLUE,size=16):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.5,rounding_size=1.5',
        facecolor=color+'0d',edgecolor=color,linewidth=1.5))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=size,color=INK,linespacing=1.6)

def arrow(ax,x1,y1,x2,y2,color=GRAY):
    ax.annotate('',(x2,y2),(x1,y1),arrowprops={'arrowstyle':'->','color':color,'lw':1.7})

def save(fig,name,note):
    fig.text(.055,.042,note,fontsize=13,color=GRAY)
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None,'Creator':'Hearingpedia original teaching figure'})
    p=OUT/(name+'.svg');s=p.read_text(encoding='utf-8')
    s=re.sub(r'width="[\d.]+pt" height="[\d.]+pt"','width="1400" height="700"',s,count=1)
    p.write_text('\n'.join(line.rstrip() for line in s.splitlines())+'\n',encoding='utf-8')
    fig.savefig(OUT/(name+'.png'),dpi=100);plt.close(fig)

fig,ax=canvas('受体活动保留，不代表神经传递完整')
box(ax,1,64,20,22,'外毛细胞\n耳蜗放大',GREEN)
box(ax,28,64,20,22,'内毛细胞\n受体转导',BLUE)
box(ax,55,64,20,22,'带状突触\n递质释放',ORANGE)
box(ax,82,64,17,22,'听神经\n传向脑干',BLUE)
for a,b in [(21,28),(48,55),(75,82)]:arrow(ax,a,75,b,75)
ax.text(24.5,90,'机械作用',ha='center',fontsize=12,color=GRAY)
box(ax,1,28,20,19,'OAE\n耳道声压',GREEN)
box(ax,28,28,30,19,'CM\n毛细胞相关电位',GREEN)
box(ax,65,28,34,19,'ABR\n同步的群体神经电位',BLUE)
arrow(ax,11,64,11,47,GREEN)
arrow(ax,38,64,43,47,GREEN)
arrow(ax,14,64,35,47,GREEN)
arrow(ax,90,64,83,47,BLUE)
ax.text(50,8,'ANSD：OAE 和／或 CM 有证据，ABR 缺失或严重异常\n病变定位仍需病因、影像与其他生理证据',ha='center',va='center',fontsize=17,color=INK)
save(fig,'measurement-map','结构与测量关系示意；非按解剖比例绘制。OAE、CM 和 ABR 不是同一种信号。')

fs=20000;t=np.arange(0,.012,1/fs)
def burst(delay,duration):
    u=t-delay;return np.where((u>=0)&(u<=duration),np.sin(2*np.pi*500*u)*np.sin(np.pi*np.clip(u/duration,0,1))**2,0)
cm=burst(.003,.008);artifact=.65*burst(0,.008)
opened=cm+artifact;blocked=artifact.copy()
fig,axs=plt.subplots(2,2,figsize=(14,7),dpi=100,sharex=True,sharey=True)
fig.subplots_adjust(left=.08,right=.97,bottom=.19,top=.80,wspace=.20,hspace=.48)
fig.suptitle('波形随极性翻转，还不足以确认 CM',x=.055,y=.96,ha='left',fontsize=25,fontweight='bold',color=INK)
for ax,y,title in zip(axs.flat,[cm,artifact,opened,blocked],['（a）自设 CM：声学延迟 3 ms','（b）自设电磁伪迹：无声学延迟','（c）声路开放：CM + 伪迹','（d）阻断声路：只剩伪迹']):
    ax.plot(t*1000,y,color=BLUE,lw=2,label='正极性')
    ax.plot(t*1000,-y,color=ORANGE,ls='--',lw=1.8,label='负极性')
    ax.set(title=title,ylim=(-1.1,1.1),xlim=(0,12));ax.grid(alpha=.15)
axs[0,0].legend(ncol=2,frameon=False,loc='upper right',fontsize=11)
for ax in axs[:,0]:ax.set_ylabel('幅度（任意单位）')
for ax in axs[1,:]:ax.set_xlabel('时间（ms）')
save(fig,'cm-control','500 Hz 合成信号；采样率 20 kHz。声路阻断时保持电驱动不变。理想示意，不是诊断波形。')

rng=np.random.default_rng(20261106);n=40;z=rng.standard_normal(n);z-=z.mean()
sigmas=[.10,1.0];grid=np.arange(0,12,.01);width=.15
pulses=[];times=[]
for sd in sigmas:
    shifts=6+sd*z;times.append(shifts)
    pulses.append(np.exp(-.5*((grid[None,:]-shifts[:,None])/width)**2).mean(axis=0))
fig,axs=plt.subplots(1,2,figsize=(14,7),dpi=100)
fig.subplots_adjust(left=.08,right=.97,bottom=.21,top=.80,wspace=.24)
fig.suptitle('活动数量相同，群体峰值仍可不同',x=.055,y=.96,ha='left',fontsize=25,fontweight='bold',color=INK)
for shifts,c,offset,label in zip(times,[BLUE,ORANGE],[0,48],['抖动较小','抖动较大']):
    axs[0].vlines(shifts,np.arange(n)+offset,np.arange(n)+offset+.8,color=c,lw=2,label=label)
axs[0].set(xlim=(2,10),ylim=(-2,91),xlabel='事件时间（ms）',ylabel='来源编号（分两块显示）',title='（a）每个来源都产生一个事件')
axs[0].set_yticks([0,39,48,87],['1','40','1','40']);axs[0].legend(frameon=False,fontsize=12)
for p,c,ls,label in zip(pulses,[BLUE,ORANGE],['-','--'],['抖动尺度 0.10 ms','抖动尺度 1.00 ms']):
    axs[1].plot(grid,p,color=c,ls=ls,lw=2.3,label=label)
axs[1].set(xlim=(2,10),ylim=(0,1),xlabel='时间（ms）',ylabel='平均幅度（任意单位）',title='（b）相同单源波形的线性平均')
axs[1].legend(frameon=False,fontsize=12)
for ax in axs:ax.grid(alpha=.15)
save(fig,'synchrony','40 个来源，单脉冲宽度参数 0.15 ms；共用随机数，种子 20261106。非真实神经放电或 ABR 模型。')

fig,ax=canvas('把诊断证据与交流获益放在同一随访中')
box(ax,1,57,43,30,'生理证据\n中耳、OAE／CM、ABR\n记录可靠性与复测变化',BLUE)
box(ax,56,57,43,30,'病因与结构\n围产史、遗传、神经系统\n必要的耳蜗神经影像',ORANGE)
box(ax,1,6,43,30,'听觉功能\n行为听阈、安静与噪声言语\n设备验证和实际使用',GREEN)
box(ax,56,6,43,30,'交流与发展\n可及的口语／手语\n语言、参与和家庭目标',BLUE)
arrow(ax,44,72,56,72);arrow(ax,77,57,77,36)
arrow(ax,56,21,44,21);arrow(ax,22,36,22,57)
ax.text(50,46,'联合评估 → 调整支持 → 再评价',ha='center',va='center',fontsize=19,fontweight='bold',color=INK)
save(fig,'follow-up','评估框架示意；四个维度并行更新，箭头不规定临床检查顺序，也不构成个体诊疗算法。')

checks={'nature':'synthetic teaching signals; no patient data','sample_rate_hz':fs,'cm_frequency_hz':500,
 'cm_delay_ms':3,'burst_duration_ms':8,'artifact_amplitude':.65,'blocked_equals_artifact':bool(np.array_equal(blocked,artifact)),
 'open_minus_blocked_equals_cm':bool(np.allclose(opened-blocked,cm)),
 'seed':20261106,'source_count':n,'event_counts':[len(a) for a in times],
 'jitter_scale_ms':sigmas,'pulse_width_parameter_ms':width,
 'mean_peaks':[float(p.max()) for p in pulses],
 'integrals_ms':[float(np.trapz(p,grid)) for p in pulses],
 'figures':['measurement-map','cm-control','synchrony','follow-up']}
assert checks['blocked_equals_artifact'] and checks['open_minus_blocked_equals_cm']
assert checks['event_counts']==[40,40] and checks['mean_peaks'][0]>checks['mean_peaks'][1]
assert np.allclose(checks['integrals_ms'][0],checks['integrals_ms'][1],rtol=1e-5)
(HERE/'validation.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(checks,ensure_ascii=False,indent=2))
