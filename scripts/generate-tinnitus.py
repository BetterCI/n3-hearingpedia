"""Original Chinese functional diagrams and synthetic endpoint comparison, without anatomical sketches."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/tinnitus';OUT.mkdir(parents=True,exist_ok=True)
RECORD=ROOT/'docs/research/tinnitus-2026-10-09';RECORD.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':12,'svg.fonttype':'path','axes.unicode_minus':False})
C=['#215e83','#b75637','#457665','#8264a0'];manifest=[]
def save(f,name,params):
 for ext in ['svg','png']:
  p=OUT/(name+'.'+ext);f.savefig(p,dpi=180,bbox_inches='tight',facecolor='white')
  if ext=='svg':p.write_text('\n'.join(l.rstrip() for l in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
 plt.close(f);manifest.append({'file':name+'.svg','nature':'原创教学图','parameters':params,'license':'Project-authored; no external figure reproduced'})
def canvas(h=7):
 f,a=plt.subplots(figsize=(9,h));a.set(xlim=(0,10),ylim=(0,9));a.axis('off');return f,a
def box(a,x,y,w,h,title,sub,c=C[0]):
 a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.03,rounding_size=.10',fc='#f7f9fa',ec=c,lw=1.5))
 a.text(x+w/2,y+h*.73,title,ha='center',va='center',fontsize=14,fontweight='bold',color=c)
 a.text(x+w/2,y+h*.30,sub,ha='center',va='center',fontsize=11.5,linespacing=1.5)
def arrow(a,p,q,c=C[0],dashed=False):a.add_patch(FancyArrowPatch(p,q,arrowstyle='->',lw=1.6,mutation_scale=15,color=c,linestyle='--' if dashed else '-'))
f,a=canvas(8)
a.text(.1,8.6,'耳鸣描述：不同维度分别记录',fontsize=17,fontweight='bold')
rows=[('声音来源','仅本人感知／可检测的体内声源'),('节律','非搏动／搏动；是否与脉搏同步'),('位置','单侧／双侧／头内或难以定位'),('时间过程','起始、持续、间歇与波动'),('功能影响','睡眠、专注、情绪与日常活动')]
for n,(t,s) in enumerate(rows):
 y=6.75-n*1.45;box(a,.35,y,2.5,1.1,t,'观察维度',C[n%4]);box(a,3.7,y,5.95,1.1,'具体描述',s,C[n%4]);arrow(a,(2.9,y+.55),(3.65,y+.55),C[n%4])
a.text(5,.12,'维度可以交叉；搏动性不自动等于客观性或血管病因',ha='center',fontsize=11,color='#536672')
save(f,'description-dimensions',{'dimensions':[r[0] for r in rows],'limitations':'axes overlap; not diagnostic algorithm or prevalence chart'})
f,a=canvas(7.5)
a.text(.1,8.6,'从输入改变到感知与影响：候选功能关系',fontsize=16,fontweight='bold')
box(a,.35,6.1,4.05,1.35,'外周与躯体输入','听觉输入改变／头颈与颌部线索',C[2])
box(a,5.45,6.1,4.15,1.35,'听觉通路与网络调节','增益、抑制、同步等候选过程')
arrow(a,(4.45,6.78),(5.4,6.78))
box(a,5.45,3.5,4.15,1.4,'声音体验','出现、音高、响度与持续性')
arrow(a,(7.52,6.05),(7.52,4.95))
box(a,.35,3.5,4.05,1.4,'注意、情绪与显著性','影响关注、意义赋予与反应',C[3])
arrow(a,(5.4,4.4),(4.45,4.4),C[3],True);arrow(a,(4.45,3.95),(5.4,3.95),C[3],True)
box(a,2.25,.9,5.5,1.35,'生活与功能影响','睡眠、专注、交流及活动参与',C[1])
arrow(a,(2.35,3.45),(3.2,2.3),C[3]);arrow(a,(7.52,3.45),(6.8,2.3))
a.text(5,.25,'功能框架；候选关系不保证在每个人身上同时成立',ha='center',fontsize=11,color='#536672')
save(f,'mechanism-framework',{'layout':'functional hypotheses, not anatomy','dashed':'bidirectional percept/attention modulation; not proof of psychogenic cause','limitations':'no unique tinnitus source or causal weights'})
f,a=canvas(7.6)
a.text(.1,8.6,'测量对象不同，结果不能互相替代',fontsize=17,fontweight='bold')
rows=[('听力与耳部检查','外围功能与可能病因','听阈、耳镜、中耳及其他针对性检查'),('心理声学匹配','声音体验的部分属性','音高、匹配声级、掩蔽与残余抑制'),('主观结局量表','功能影响与困扰','THI、TFI；需验证语言版本和变化解释'),('神经记录与模型','候选编码及机制联系','ABR、EEG、影像；不是通用确诊读数')]
for n,(t,u,s) in enumerate(rows):
 y=6.5-n*1.75;box(a,.35,y,3.25,1.35,t,'主要观察入口',C[n%4]);box(a,4.45,y,5.15,1.35,u,s,C[n%4]);arrow(a,(3.65,y+.68),(4.4,y+.68),C[n%4])
a.text(5,.4,'复测应追踪对应目标；量表下降不等于匹配响度下降',ha='center',fontsize=11,color='#536672')
save(f,'measurement-targets',{'targets':['peripheral function','percept attributes','functional impact','candidate neural mechanisms'],'limitations':'not a clinical test battery or ranking'})
f,axes=plt.subplots(1,2,figsize=(10,5.2),layout='constrained')
before=[6,6,6];after=[6,3,3];ib=[60,60,60];ia=[40,60,40];labels=['情形甲','情形乙','情形丙']
for ax,b,e,title,xmax,unit in [(axes[0],before,after,'（a）感知响度评分',10,'评分（0–10）'),(axes[1],ib,ia,'（b）功能影响指标',100,'评分（0–100）')]:
 for y,(v1,v2) in enumerate(zip(b,e)):
  ax.plot([v1,v2],[y,y],color=C[y],lw=3);ax.plot(v1,y,'o',ms=11,mfc='white',mec=C[y],mew=2);ax.plot(v2,y,'D',ms=7,color=C[y])
  if v1==v2:ax.text(v1+.35 if xmax==10 else v1+3,y+.18,'保持',color=C[y],fontsize=11)
 ax.set(xlim=(-.4,10.5) if xmax==10 else (-5,105),xticks=list(range(0,xmax+1,2 if xmax==10 else 20)),ylim=(-.6,2.6),yticks=range(3),yticklabels=labels,xlabel=unit,title=title);ax.invert_yaxis();ax.grid(axis='x',alpha=.18);ax.spines[['top','right']].set_visible(False)
f.suptitle('教学设定：感知变化与功能变化分别计算',fontsize=17,fontweight='bold')
axes[0].plot([],[],'o',mfc='white',mec='#536672',mew=2,label='前');axes[0].plot([],[],'D',color='#536672',label='后');axes[0].legend(loc='lower right',ncol=2)
save(f,'separate-endpoints',{'synthetic':True,'cases':labels,'percept_rating_before':before,'percept_rating_after':after,'functional_index_before':ib,'functional_index_after':ia,'limitations':'not TFI raw items, treatment outcomes, measurement norms or individual clinical thresholds'})
assert [v-u for u,v in zip(before,after)]==[0,-3,-3]
assert [v-u for u,v in zip(ib,ia)]==[-20,0,-20]
assert 45-30==15 and 45-40==5
(RECORD/'figure-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
