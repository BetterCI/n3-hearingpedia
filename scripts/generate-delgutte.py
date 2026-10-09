"""Original teaching diagrams and exact interval/pulse arithmetic; no measured data."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/bertrand-delgutte'
R=ROOT/'docs/research/bertrand-delgutte-2026-10-10'
for p in [OUT,R]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':13,'svg.fonttype':'path'})
BLUE,ORANGE,GREEN,GRAY='#276582','#af6435','#39846b','#526472'
records=[]
def save(fig,name,parameters):
    for ext in ['svg','png']:
        p=OUT/(name+'.'+ext);fig.savefig(p,dpi=100,facecolor='white')
        if ext=='svg':p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)
    records.append({'name':name,'width':1280,'height':650,'parameters':parameters,'nature':'original functional or arithmetic teaching figure; not measured neural or perceptual data'})
def canvas(title,subtitle):
    fig,ax=plt.subplots(figsize=(12.8,6.5));fig.subplots_adjust(0,0,1,1)
    ax.set(xlim=(0,1280),ylim=(0,650));ax.axis('off')
    ax.text(640,610,title,ha='center',fontsize=23,fontweight='bold')
    ax.text(640,559,subtitle,ha='center',fontsize=14,color=GRAY)
    return fig,ax
def box(ax,x,y,w,h,t,color=BLUE,size=14):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',facecolor='#f3f7fa',edgecolor=color,lw=1.6))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=size,color=color)
def arrow(ax,a,b,col=GRAY):ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.8,'color':col})

fig,ax=canvas('声音、神经与知觉：三层证据','刺激可控、指标可计算、任务可比较；连接不等于证据互相替代')
for x,title,color in [(35,'输入：操纵什么？',BLUE),(470,'神经：记录什么？',GREEN),(905,'知觉：测量什么？',ORANGE)]:
    ax.text(x+170,500,title,ha='center',fontsize=18,color=color,fontweight='bold')
    texts={BLUE:['类元音、复杂音\n共振峰与重复周期','虚拟消声与混响\n包络、双耳关系','双侧电刺激\n脉冲间隔与ITD'],GREEN:['听神经响应\n频率位置、同步与间隔','下丘响应\n调制编码与群体信息','下丘电刺激响应\n持续放电与ITD调谐'],ORANGE:['词句与旋律辨认\n声学嵌合体冲突任务','任务表现的预测\n需要另行行为验证','真实植入者行为\n左／右ITD辨别']}[color]
    for y,t in zip([365,235,105],texts):box(ax,x,y,340,98,t,color)
for y in [414,284,154]:
    arrow(ax,(385,y),(459,y));arrow(ax,(820,y),(894,y))
ax.text(640,43,'归纳多个独立研究；神经记录与行为实验不一定同物种、同个体、同一时刻',ha='center',fontsize=12,color=GRAY)
save(fig,'evidence-framework',{'columns':['controlled input','neural measures','perception and validation'],'not_anatomy':True})

spikes=np.array([0,4,8,16]);first=np.diff(spikes)
allorder=np.array([spikes[j]-spikes[i] for i in range(4) for j in range(i+1,4)])
assert first.tolist()==[4,4,8] and sorted(allorder.tolist())==[4,4,8,8,12,16]
fig=plt.figure(figsize=(12.8,6.5));fig.suptitle('同一放电序列：一阶与全阶间隔',y=.96,fontsize=23,fontweight='bold')
top=fig.add_axes([.10,.66,.84,.13]);top.set(xlim=(-1,18),ylim=(-.1,1.3),xticks=[0,4,8,12,16],yticks=[],xlabel='放电时刻（ms）')
top.vlines(spikes,0,1,color=BLUE,lw=3);top.spines[['left','top','right']].set_visible(False)
top.set_title('教学时刻：0、4、8、16 ms',fontsize=15,color=GRAY)
for x,title,seq,color in [(.10,'（a）一阶：相邻间隔，3个',first,BLUE),(.56,'（b）全阶：所有先后配对，6个',allorder,GREEN)]:
    a=fig.add_axes([x,.20,.36,.32]);lags=[4,8,12,16];counts=[int(np.sum(seq==v)) for v in lags]
    a.bar(lags,counts,width=2.0,color=color,alpha=.85);a.set(xlim=(1,19),ylim=(0,2.7),xticks=lags,yticks=[0,1,2],xlabel='放电间隔（ms）',ylabel='出现次数',title=title)
    a.spines[['top','right']].set_visible(False);a.grid(axis='y',alpha=.15)
    for v,c in zip(lags,counts):a.text(v,c+.1,str(c),ha='center',color=color)
fig.text(.5,.055,'候选周期4 ms → 250 Hz；短列不能唯一判定音高。全阶配对均在同一序列内部。',ha='center',fontsize=12,color=GRAY)
save(fig,'interval-statistics',{'spike_times_ms':spikes.tolist(),'first_order_ms':first.tolist(),'all_order_ms':allorder.tolist(),'candidate_period_ms':4,'candidate_hz':250})

fig,ax=canvas('混响包络研究：匹配什么，比较什么？','输入深度与环境性质需要分开；框图不画假想的神经响应')
for x,title,t,color in [(35,'A　原始消声','原始调幅输入\n耳端深度 m0',BLUE),(470,'B　混响条件','模拟房间处理\n耳端深度 mR',ORANGE),(905,'C　匹配消声','减少原始调制\n耳端深度 mR',GREEN)]:
    ax.text(x+170,500,title,ha='center',fontsize=18,fontweight='bold',color=color)
    box(ax,x,350,340,120,t,color,17)
    box(ax,x,205,340,94,'测量下丘响应\n放电率与调制同步',color,15)
    arrow(ax,(x+170,347),(x+170,303),color)
box(ax,45,65,555,90,'A与B：观察总体退化与相对补偿\n输入深度和其他声学属性同时改变',BLUE,14)
box(ax,670,65,565,90,'B与C：匹配深度后比较额外效应\n仍需控制频谱、包络形状、双耳关系',GREEN,14)
ax.text(640,27,'m0、mR均无量纲；没有指定深度数值或真实房间参数',ha='center',fontsize=12,color=GRAY)
save(fig,'reverberation-controls',{'depth_symbols':['m0','mR'],'matched_property':'modulation depth at ear','recording':'inferior colliculus; no response values plotted'})

base=np.arange(8,dtype=float);added=np.array([2.1,6.1]);sipi=np.sort(np.r_[base,added]);matched=np.arange(10)*.8;itd=.1
assert len(base)==8 and len(sipi)==len(matched)==10
assert abs(np.min(np.diff(sipi))-.1)<1e-8
fig,ax=canvas('短间隔插入：数量与局部时序分别变化','教学图：右侧整体延后100 µs；竖线只表示脉冲起始时刻')
a=fig.add_axes([.23,.17,.73,.61]);a.set(xlim=(-.15,8.25),ylim=(-.1,5.9),xticks=np.arange(9),yticks=[],xlabel='时间（ms）');a.spines[['left','top','right']].set_visible(False);a.grid(axis='x',alpha=.13)
for y,seq,name,rate in [(4.8,base,'基准等间隔',1000),(2.8,sipi,'插入短间隔',1250),(.8,matched,'同平均率等间隔',1250)]:
    a.hlines([y,y-.65],-.1,8.1,color='#c6cfd6',lw=1)
    a.vlines(seq,y,y+.5,color=BLUE,lw=2.2);a.vlines(seq+itd,y-.65,y-.15,color=ORANGE,lw=2.2)
    a.text(-.33,y+.33,'左',ha='right',fontsize=11,color=BLUE);a.text(-.33,y-.43,'右',ha='right',fontsize=11,color=ORANGE)
    fig.text(.025,.17+(y+.12)/6*.61,name+'\n'+str(len(seq))+'个／8 ms\n'+str(rate)+' pps',va='center',fontsize=14,color=GRAY)
    if name=='插入短间隔':
        a.vlines(added,y,y+.5,color=GREEN,lw=3.2)
        a.annotate('额外起始：2.1、6.1 ms',xy=(6.1,y+.5),xytext=(3.1,y+.82),fontsize=11,color=GREEN,arrowprops={'arrowstyle':'->','color':GREEN})
fig.text(.5,.055,'计数用左侧[0, 8) ms参考窗口；图样周期重复。未指定电流、脉宽或临床设置。',ha='center',fontsize=12,color=GRAY)
save(fig,'pulse-timing',{'window_ms':[0,8],'base_times_ms':base.tolist(),'added_times_ms':added.tolist(),'sipi_times_ms':sipi.tolist(),'matched_rate_times_ms':matched.tolist(),'rates_pps':[1000,1250,1250],'itd_us':100,'convention':'tR-tL; positive means left first','not_original_paper_protocol':True})
(R/'figure-parameters.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Generated four original SVG/PNG pairs and parameter record.')
