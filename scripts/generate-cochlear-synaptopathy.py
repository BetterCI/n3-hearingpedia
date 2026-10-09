"""Original functional/evidence diagrams and declared toy calculations; no anatomy or clinical norms."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/cochlear-synaptopathy'; OUT.mkdir(parents=True,exist_ok=True)
RECORD=ROOT/'docs/research/cochlear-synaptopathy-2026-10-09'; RECORD.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':12,'svg.fonttype':'path',
                     'axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
C=['#215e83','#b75637','#457665','#8264a0'];manifest=[]

def save(f,name,params):
    for ext in ['svg','png']:
        p=OUT/(name+'.'+ext);f.savefig(p,dpi=180,bbox_inches='tight',facecolor='white')
        if ext=='svg':p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(f);manifest.append({'file':name+'.svg','nature':'原创教学图','parameters':params,
                                'license':'Project-authored; no external figure reproduced'})

def canvas(h=7):
    f,a=plt.subplots(figsize=(9,h));a.set(xlim=(0,10),ylim=(0,8));a.axis('off');return f,a

def box(a,x,y,w,h,title,sub,color=C[0]):
    a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.03,rounding_size=.10',fc='#f7f9fa',ec=color,lw=1.5))
    a.text(x+w/2,y+h*.7,title,ha='center',va='center',fontsize=14,fontweight='bold',color=color)
    a.text(x+w/2,y+h*.27,sub,ha='center',va='center',fontsize=11.5,linespacing=1.5)

def arrow(a,p,q,c=C[0]):a.add_patch(FancyArrowPatch(p,q,arrowstyle='->',lw=1.6,mutation_scale=15,color=c))

f,a=canvas()
a.text(.1,7.6,'突触病变：损伤环节与测量对象',fontsize=17,fontweight='bold')
box(a,.3,5.65,4.1,1.1,'耳蜗机械输入','受外毛细胞与声学传输影响',C[2])
box(a,5.4,5.65,4.3,1.1,'内毛细胞换能','把机械输入转换为细胞信号')
arrow(a,(4.45,6.2),(5.35,6.2));arrow(a,(7.55,5.6),(7.55,4.85))
box(a,5.4,3.6,4.3,1.2,'突触传递 → 传入听神经','本词条关注的连接与信息传递',C[1])
box(a,.3,3.6,4.1,1.2,'耳声发射','声学输出；不直接统计突触',C[2])
arrow(a,(2.35,5.6),(2.35,4.85),C[2])
box(a,5.4,1.55,4.3,1.1,'脑干与更高级处理','响应还受同步和中枢调节影响',C[3])
arrow(a,(7.55,3.55),(7.55,2.7),C[1])
box(a,.3,1.55,4.1,1.1,'ABR、EFR 等群体指标','需说明刺激、发生源与记录条件')
arrow(a,(5.35,2.1),(4.45,2.1))
arrow(a,(5.35,3.55),(4.1,2.7),C[1])
a.text(5,.65,'功能框图，不表示解剖尺度；临床检测不直接读出连接数量',ha='center',fontsize=11.5,color='#536672')
save(f,'functional-measurement',{'layout':'functional path with measurement branches; EFR/ABR are aggregate and stimulus-dependent, no single-source localization'})

f,a=canvas(7)
a.text(.1,7.6,'三种证据：能直接观察的对象不同',fontsize=17,fontweight='bold')
box(a,.4,5.35,3,1.3,'动物模型','实验暴露／年龄／干预')
box(a,4.2,5.35,5.4,1.3,'结构与功能可以配对','同模型组织标记、神经及行为测量')
arrow(a,(3.45,6),(4.15,6))
box(a,.4,3.15,3,1.3,'人类死后组织','颞骨、病史与取材条件',C[2])
box(a,4.2,3.15,5.4,1.3,'直接结构证据','支持病变存在；缺少完整生前功能配对',C[2])
arrow(a,(3.45,3.8),(4.15,3.8),C[2])
box(a,.4,.95,3,1.3,'活体人类研究','生理指标、暴露与行为',C[1])
box(a,4.2,.95,5.4,1.3,'间接功能证据','需检验可靠性、替代解释与独立预测',C[1])
arrow(a,(3.45,1.6),(4.15,1.6),C[1])
a.text(5,.3,'三条证据线相互约束，不能把同名指标当作同等验证',ha='center',fontsize=11,color='#536672')
save(f,'evidence-levels',{'types':['animal structure/function','human postmortem structure','living human proxy'],'arrows':'measurement relationship, not a ranking score'})

f,a=plt.subplots(figsize=(9,5.8),layout='constrained')
fraction=np.linspace(0,1,101)
for q,c,ls in [(1,C[0],'-'),(.8,C[2],'--'),(.6,C[1],':')]:
    a.plot(fraction,fraction*q,color=c,ls=ls,lw=2.3,label=f'同步权重 q = {q:g}')
a.plot([.6,1],[.6,.6],'o',color='#263843',ms=8)
a.axhline(.6,color='#73858e',ls='--',lw=1)
a.annotate('n = 0.6，q = 1',xy=(.6,.6),xytext=(.4,.8),arrowprops={'arrowstyle':'->','color':'#536672'},fontsize=12)
a.annotate('n = 1，q = 0.6',xy=(1,.6),xytext=(.64,.34),arrowprops={'arrowstyle':'->','color':'#536672'},fontsize=12)
a.set(xlim=(0,1.04),ylim=(0,1.04),xlabel='有效连接比例 n（无量纲）',ylabel='归一化响应 A = n × q（无量纲）',title='同一响应值可以由不同参数组合产生')
a.legend(loc='upper left',fontsize=11);a.grid(alpha=.18)
save(f,'response-ambiguity',{'toy_model':'A=n*q, unit recording factor g=1; all variables normalized','same_response':[{'n':.6,'q':1,'A':.6},{'n':1,'q':.6,'A':.6}],'limitations':'not an ABR/connection calibration; ignores many nonlinear processes'})

f,a=plt.subplots(figsize=(9,5.5),layout='constrained')
sem=np.array([.005,.02]);mdc=1.96*np.sqrt(2)*sem;diff=.03
for y,lim,c,label in [(1,mdc[0],C[0],'误差较小：SEM = 0.005 μV'),(0,mdc[1],C[1],'误差较大：SEM = 0.020 μV')]:
    a.plot([-lim,lim],[y,y],color=c,lw=9,alpha=.35,solid_capstyle='butt')
    a.plot([-lim,lim],[y,y],'|',color=c,ms=24,mew=2)
    a.plot(diff,y,'D',color='#263843',ms=9)
    a.text(-.065,y+.24,label,fontsize=12)
    a.text(.065,y,f'±MDC95\n±{lim:.3f} μV',ha='left',va='center',fontsize=11)
a.axvline(0,color='#536672',lw=1);a.axvline(diff,color='#263843',ls=':',lw=1)
a.set(xlim=(-.07,.09),ylim=(-.5,1.7),yticks=[],xlabel='两次测量的差值（μV）',title='同一 0.030 μV 差值，需放回测量误差判断')
a.text(.03,1.58,'◆ 教学设定的观察差值',ha='center',fontsize=11)
a.grid(axis='x',alpha=.18)
save(f,'measurement-error',{'synthetic':True,'SEM_uV':sem.tolist(),'MDC95_uV':mdc.tolist(),'observed_difference_uV':diff,'assumptions':'independent Gaussian errors of equal variance, no systematic drift; not diagnostic cutoffs'})
assert abs(.6*1-1*.6)<1e-12
assert mdc[0]<diff<mdc[1]
(RECORD/'figure-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
