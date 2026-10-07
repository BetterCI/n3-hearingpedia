from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

ROOT=Path(__file__).parent
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'path','axes.unicode_minus':False,'figure.facecolor':'white','savefig.facecolor':'white'})
BLUE='#235f83'; RED='#b34c42'; GRAY='#a4acb3'; GREEN='#397666'
def save(fig,name):
    fig.savefig(ROOT/(name+'.svg'),bbox_inches='tight')
    fig.savefig(ROOT/(name+'.png'),dpi=170,bbox_inches='tight')
    plt.close(fig)
def tone(ax,t,f,d=.16,c=BLUE,lw=7): ax.plot([t,t+d],[f,f],color=c,lw=lw,solid_capstyle='butt')

# 1: Source attributes and grouping, abstract time-frequency events, not measured spectra.
fig,axs=plt.subplots(1,2,figsize=(11,4),layout='constrained')
for ax in axs:
    for t in [.15,.65,1.15,1.65]:
        for f in [200,400,600]: tone(ax,t,f,c=BLUE)
    for t in [.35,.85,1.35,1.85]:
        for f in [300,600,900]: tone(ax,t,f,c=RED)
    ax.set(xlim=(0,2.3),ylim=(80,1050),xlabel='时间（s）',ylabel='频率（Hz）')
axs[0].set_title('A  同时分组：一个事件中的多个频率成分',loc='left',pad=18)
axs[0].add_patch(Rectangle((.1,150),.23,510,fill=False,ec=BLUE,lw=1.4))
axs[0].annotate('共同起始的成分',xy=(.32,500),xytext=(.72,1000),arrowprops={'arrowstyle':'->','color':BLUE},color=BLUE)
axs[1].set_title('B  序列分组：跨事件维持声源身份',loc='left',pad=18)
axs[1].plot([.22,.72,1.22,1.72],[200]*4,'--',color=BLUE,lw=1.4)
axs[1].plot([.42,.92,1.42,1.92],[900]*4,'--',color=RED,lw=1.4)
axs[1].text(.72,1010,'蓝色与红色分别表示两组候选成分',fontsize=9,color='#56636c')
save(fig,'01-simultaneous-sequential-grouping')

# 2: Same ABA- stimulus with two interpretations. Frequencies are arbitrary examples.
fig,axs=plt.subplots(3,1,figsize=(10,6),sharex=True,layout='constrained')
events=[]
for k in range(6):
    for offset,f in [(0,600),(.12,900),(.24,600)]: events.append((k*.48+offset,f))
for ax in axs:
    for t,f in events: tone(ax,t,f,d=.085,c=BLUE if f==600 else RED,lw=6)
    ax.set(ylim=(450,1050),yticks=[600,900],ylabel='频率（Hz）')
axs[0].set_title('A  刺激：重复的 A–B–A— 序列',loc='left')
axs[1].set_title('B  一条声流的解释：连接相邻音，形成整体节奏',loc='left')
axs[1].plot([t+.042 for t,f in events],[f for t,f in events],color=GRAY,lw=1,zorder=0)
axs[2].set_title('C  两条声流的解释：分别连接同类音',loc='left')
for f,c in [(600,BLUE),(900,RED)]:
    ts=[t+.042 for t,freq in events if freq==f]
    axs[2].plot(ts,[f]*len(ts),'--',color=c,lw=1,zorder=0)
axs[2].set(xlabel='时间（s）',xlim=(-.07,2.92))
save(fig,'02-aba-streaming')

# 3: Cross-channel temporal relationships, teaching Pearson correlation only.
t=np.linspace(0,2,1000)
a=.5+.4*np.sin(2*np.pi*2*t)
b=.5+.4*np.sin(2*np.pi*2*t)
c=.5+.4*np.sin(2*np.pi*3*t+.6)
fig,axs=plt.subplots(1,2,figsize=(11,3.8),sharey=True,layout='constrained')
for ax,second,title in [(axs[0],b,'A  两通道包络同步变化'),(axs[1],c,'B  两通道包络变化不同')]:
    ax.plot(t,a,color=BLUE,label='通道 1',lw=2)
    ax.plot(t,second,color=RED,label='通道 2',lw=1.7,ls='--')
    ax.set(xlabel='时间（s）',ylabel='归一化包络',ylim=(0,1.12),title=title)
    rval=np.corrcoef(a,second)[0,1]
    label='接近 0' if abs(rval)<.005 else f'{rval:.2f}'
    ax.text(.06,1.03,f'示例相关系数 r = {label}',fontsize=10)
    ax.legend(loc='lower right',fontsize=9,frameon=False)
save(fig,'03-temporal-coherence')

# 4: interrupted source, masking interval, and possible percept, not measured percept.
fig,axs=plt.subplots(3,1,figsize=(10,5.4),sharex=True,layout='constrained')
for ax in axs:
    ax.set(xlim=(0,1.2),ylim=(-.2,1.4),yticks=[0,1],ylabel='存在状态')
    ax.axvspan(.45,.75,color='#e9ecee',zorder=0)
    ax.axhline(0,color='#d7dde0',lw=.7)
axs[0].plot([0,.45,.45,.75,.75,1.2],[1,1,0,0,1,1],color=BLUE,lw=2)
axs[0].set_title('A  物理目标音：中间确实停止',loc='left')
axs[1].plot([0,.45,.45,.75,.75,1.2],[0,0,1,1,0,0],color=RED,lw=2)
axs[1].set_title('B  噪声：在目标音停止期间出现',loc='left')
axs[2].plot([0,.45],[1,1],color=BLUE,lw=2)
axs[2].plot([.75,1.2],[1,1],color=BLUE,lw=2)
axs[2].plot([.45,.75],[1,1],color=GREEN,lw=2,ls='--')
axs[2].set_title('C  可能的连续知觉：虚线为推断的延续',loc='left')
axs[2].set_xlabel('时间（s）')
save(fig,'04-continuity-illusion')

# 5: fixed-seed event matrices; match exact density so total event count cannot cue figure.
rng=np.random.default_rng(42); nrows=24; ncols=40; percol=8; onset=20; repeated=[4,10,16]
ground=np.zeros((nrows,ncols)); figure=ground.copy()
for col in range(ncols):
    ground[rng.choice(nrows,percol,replace=False),col]=1
    if col<onset: figure[:,col]=ground[:,col]
    else:
        pool=np.array([i for i in range(nrows) if i not in repeated])
        figure[repeated,col]=1
        figure[rng.choice(pool,percol-len(repeated),replace=False),col]=1
fig,axs=plt.subplots(2,1,figsize=(10,5.4),sharex=True,layout='constrained')
for ax,data,title in [(axs[0],ground,'A  对照：成分在各时间帧随机变化'),(axs[1],figure,'B  图形条件：后半段包含三个连续重复的成分')]:
    ax.imshow(data,origin='lower',aspect='auto',extent=[0,2,0,nrows],cmap='Greys',vmin=0,vmax=1,interpolation='nearest')
    ax.axvline(1,color=RED,ls='--',lw=1.4)
    ax.set(ylabel='频率成分索引',title=title,yticks=[4.5,10.5,16.5],yticklabels=['5','11','17'])
axs[1].set_xlabel('时间（s）')
save(fig,'05-stochastic-figure-ground')
assert np.all(ground.sum(axis=0)==8) and np.all(figure.sum(axis=0)==8)
assert np.all(figure[repeated,onset:]==1)
(ROOT/'figure-verification.json').write_text(json.dumps({'type':'original synthetic teaching figures','figureCount':5,'abaExampleHz':[600,900],'correlationExamples':[float(np.corrcoef(a,b)[0,1]),float(np.corrcoef(a,c)[0,1])],'SFG':{'seed':42,'frames':40,'frameSeconds':.05,'frequencyComponents':24,'componentsPerFrameBothConditions':8,'repeatedComponentIndicesOneBased':[5,11,17],'onsetSeconds':1},'notClinicalData':True},ensure_ascii=False,indent=2),encoding='utf-8')
print('Generated 5 SVG and 5 PNG figures; numeric assertions passed.')
