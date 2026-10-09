"""Original conceptual diagrams and declared synthetic teaching data; no patient predictions."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/figures/auditory-plasticity'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'Microsoft YaHei', 'font.size': 12,
                     'svg.fonttype': 'path', 'axes.unicode_minus': False,
                     'axes.spines.top': False, 'axes.spines.right': False})
C = ['#215e83', '#b75637', '#457665', '#8264a0']
manifest = []

def save(fig, name, params):
    for ext in ['svg', 'png']:
        path = OUT / f'{name}.{ext}'
        fig.savefig(path, dpi=180, bbox_inches='tight', facecolor='white')
        if ext == 'svg':
            path.write_text('\n'.join(line.rstrip() for line in path.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8')
    plt.close(fig)
    manifest.append({'file': name+'.svg', 'nature': '原创教学图', 'parameters': params,
                     'license': 'Project-authored; no external image reproduced'})

def canvas(h=6.5):
    f, ax = plt.subplots(figsize=(9, h)); ax.set(xlim=(0,10), ylim=(0,8)); ax.axis('off'); return f, ax

def box(ax, x, y, w, h, title, subtitle, color=C[0]):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.04,rounding_size=.10',ec=color,fc='#f7f9fa',lw=1.4))
    ax.text(x+w/2,y+h*.69,title,ha='center',va='center',fontsize=14,fontweight='bold',color=color)
    ax.text(x+w/2,y+h*.28,subtitle,ha='center',va='center',fontsize=11.5,linespacing=1.5)

def arrow(ax, a, b, color=C[0]):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='->',mutation_scale=15,lw=1.6,color=color))

f,a=canvas()
a.text(.2,7.65,'从输入变化到功能：需要逐层建立证据',fontsize=17,fontweight='bold')
box(a,2.5,5.8,5,1.15,'输入与经验','声学输入、设备、训练、任务状态')
box(a,2.5,3.8,5,1.15,'候选神经机制','突触效能、抑制调节、网络权重',C[2])
arrow(a,(5,5.75),(5,5));a.text(5.3,5.3,'机制实验约束',fontsize=11)
box(a,.3,1.6,4.3,1.25,'神经测量','放电、诱发电位、功能连接',C[0])
box(a,5.4,1.6,4.3,1.25,'行为与生活结果','辨别、言语识别、参与体验',C[1])
arrow(a,(3.7,3.75),(2.45,2.92));arrow(a,(6.3,3.75),(7.55,2.92),C[1])
a.text(5,1.05,'共同变化可支持联系；确定原因还需对照或干预',ha='center',fontsize=12)
a.text(5,.38,'框图不表示真实解剖，也不表示每次神经变化都改善行为',ha='center',fontsize=11,color='#536672')
save(f,'evidence-chain',{'layout':'functional evidence hierarchy; arrows are candidate relationships, not measured connectivity'})

f,a=canvas(7)
a.text(.2,7.65,'改变怎样发生：不同调节过程可以并存',fontsize=17,fontweight='bold')
box(a,.3,5.65,4.3,1.25,'关联性突触改变','哪些输入与输出一起活动？',C[0])
box(a,5.4,5.65,4.3,1.25,'稳态调节','总体活动偏离原有范围了吗？',C[1])
box(a,.3,3.45,4.3,1.25,'抑制与神经调质门控','当前状态允许改变吗？',C[2])
box(a,5.4,3.45,4.3,1.25,'连接与结构约束','已有通路和发育状态支持什么？',C[3])
# The four processes are parallel explanatory dimensions, not a causal sequence.
box(a,2,1.3,6,1.1,'共同约束响应与学习','特征选择、响应增益、时序与任务读出','#536672')
a.text(5,2.82,'不同过程可以并存，相互作用需由实验检验',ha='center',fontsize=12)
a.text(5,.65,'框图无权重、年龄刻度或治疗剂量含义',ha='center',fontsize=11,color='#536672')
save(f,'mechanism-framework',{'sources':'Froemke 2015; Persic et al. 2020; conceptual synthesis, no anatomical geometry'})

f,a=canvas(6.3)
a.text(.2,7.65,'训练研究：把获得、迁移和保持分开测量',fontsize=17,fontweight='bold')
stages=[(.25,'重复基线','确认起点'),(2.75,'干预阶段','训练／主动对照'),(5.25,'即时复测','测训练与新材料'),(7.75,'延迟复测','检查保持')]
for x,t,s in stages:box(a,x,5.4,2,1.35,t,s)
for x in [.25,2.75,5.25]:arrow(a,(x+2.05,6.08),(x+2.45,6.08))
box(a,.4,2.9,4.25,1.3,'训练材料与任务','回答：练过的技能是否提高？',C[0])
box(a,5.35,2.9,4.25,1.3,'未训练材料与任务','回答：收益迁移到哪里？',C[1])
box(a,1.5,.8,7,1.3,'各阶段记录可听性、设备、测试条件与实际练习','延迟测试期间是否继续练习，也应记录',C[2])
arrow(a,(6.25,5.35),(2.5,4.25));arrow(a,(6.25,5.35),(7.5,4.25),C[1])
save(f,'study-design',{'timeline':'qualitative stages; spacing does not encode duration','active_control':'matched contact and attention; both groups measured at all stages'})

f,axs=plt.subplots(2,1,figsize=(9,8),layout='constrained')
times=np.arange(3); labels=['基线','即时复测','延迟复测']
data={'训练组：[40,70,65]':([40,70,65],C[0],'o','-'), '主动对照：[45,55,55]':([45,55,55],C[1],'s','--')}
for name,(v,c,m,ls) in data.items():axs[0].plot(times,v,color=c,marker=m,ls=ls,lw=2.2,label=name)
axs[0].set(title='（a）训练材料：扣除对照的共同变化',ylabel='正确率（%）',ylim=(0,100),xticks=times,xticklabels=labels)
axs[0].legend(loc='upper left',fontsize=11);axs[0].grid(axis='y',alpha=.18)
groups=['训练材料','新说话者\n同一任务','新背景噪声\n同一任务']; vals=[20,10,0]
bars=axs[1].bar(groups,vals,color=[C[0],C[2],C[3]],width=.5,edgecolor='#263843')
for b,v in zip(bars,vals):axs[1].text(b.get_x()+b.get_width()/2,v+1,str(v),ha='center')
axs[1].set(title='（b）即时增益的组间差：迁移依测试条件而异',ylabel='增益差（百分点）',ylim=(-3,30))
axs[1].axhline(0,color='#536672',lw=1);axs[1].grid(axis='y',alpha=.18)
f.suptitle('教学设定数据：不代表任何训练疗效',fontsize=16,fontweight='bold')
save(f,'training-transfer',{'synthetic':True,'trained_group_pct':[40,70,65],'control_group_pct':[45,55,55],'test_stages':['baseline','immediate','delayed'],'immediate_difference_in_changes_pp':[20,10,0],'uncertainty':'no sampling or error bars; schematic values only'})
assert (70-40)-(55-45) == 20
assert (65-40)-(55-45) == 15
assert abs((80-(80-40)*np.exp(-3/3))-65.28482235) < 1e-7
record=ROOT/'docs/research/auditory-plasticity-2026-10-09';record.mkdir(parents=True,exist_ok=True)
(record/'figure-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
