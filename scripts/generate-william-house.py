"""Original functional diagrams: no anatomical reconstruction or patient data."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/william-f-house';OUT.mkdir(parents=True,exist_ok=True)
R=ROOT/'docs/research/william-f-house-2026-10-09';R.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':15,'svg.fonttype':'path'})
INK='#203c50';BLUE='#eaf3f8';ORANGE='#fff1df';GRAY='#526472'

def canvas(height):
 f,ax=plt.subplots(figsize=(11.2,height),dpi=100);f.subplots_adjust(0,0,1,1)
 ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off');return f,ax

def box(ax,x,y,w,h,title,text,color=BLUE):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.008,rounding_size=0.012',facecolor=color,edgecolor='#bed0da',lw=1.2))
 ax.text(x+w/2,y+h*.74,title,ha='center',va='center',fontsize=16,fontweight='bold',color=INK)
 ax.text(x+w/2,y+h*.32,text,ha='center',va='center',fontsize=14,color=GRAY,linespacing=1.6)

def arrow(ax,x0,y,x1):
 ax.annotate('',(x1,y),(x0,y),arrowprops={'arrowstyle':'->','color':'#527a93','lw':1.8})

def save(f,name):
 for ext in ['svg','png']:
  p=OUT/(name+'.'+ext);f.savefig(p,dpi=160,facecolor='white')
  if ext=='svg':p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
 plt.close(f)

f,ax=canvas(7.2)
ax.text(.5,.94,'听觉植入：功能链与评价问题',ha='center',fontsize=23,fontweight='bold',color=INK)
ax.text(.05,.83,'功能关系',fontsize=16,color=GRAY)
xs=[.05,.29,.53,.77];w=.18
for x,(title,text) in zip(xs,[('声音输入','环境声或言语'),('信号处理','转为电刺激信号'),('电极与组织','施加电刺激'),('神经活动','形成听觉输入')]):box(ax,x,.59,w,.19,title,text)
for i in range(3):arrow(ax,xs[i]+w+.006,.685,xs[i+1]-.012)
ax.text(.5,.50,'输入存在 ≠ 信息可分辨 ≠ 交流任务完成',ha='center',fontsize=18,color='#986029')
ax.text(.05,.42,'分别检验的证据',fontsize=16,color=GRAY)
cards=[('装置能否持续使用','材料、接口与佩戴\n长期运行及随访'),('能否利用声音线索','检测与环境声识别\n时长、强弱等差别'),('能否改善交流','仅听、仅视觉、视听联合\n任务成绩与使用者体验')]
for x,(title,text) in zip([.05,.37,.69],cards):box(ax,x,.14,.26,.22,title,text,ORANGE)
ax.text(.5,.045,'原创教学框图；非历史装置复原、解剖图或患者实测结果',ha='center',fontsize=13,color=GRAY)
save(f,'system-and-evidence')

f,ax=canvas(6.4)
ax.text(.5,.94,'CI 与 ABI：接入听觉通路的位置不同',ha='center',fontsize=23,fontweight='bold',color=INK)
rows=[(.55,'CI：人工耳蜗',[('声音转换','外部处理'),('耳蜗内电极','电刺激接入'),('听神经','传递神经信息'),('耳蜗核及后续','继续处理输入')]),(.19,'ABI：听觉脑干植入',[('声音转换','外部处理'),('脑干植入电极','电刺激接入'),('耳蜗核附近','刺激目标区域'),('后续听觉通路','继续处理输入')])]
for y,label,blocks in rows:
 ax.text(.05,y+.23,label,fontsize=17,fontweight='bold',color=INK)
 for x,(title,text) in zip(xs,blocks):box(ax,x,y,w,.18,title,text,BLUE if y>.4 else ORANGE)
 for i in range(3):arrow(ax,xs[i]+w+.006,y+.09,xs[i+1]-.012)
ax.text(.5,.07,'功能框图，不表示解剖比例、手术路线或电极形状',ha='center',fontsize=14,color=GRAY)
ax.text(.5,.025,'刺激位置更中枢，不自动意味着言语理解更好；两个系统需分别评价',ha='center',fontsize=13,color='#986029')
save(f,'stimulation-sites')
manifest=[{'name':'system-and-evidence','nature':'原创功能与证据层次框图','empirical_data':False,'anatomical_reconstruction':False,'source_ids':['zeng-2008','house-bilger-performance-1977'],'exports':['svg','png']},{'name':'stimulation-sites','nature':'原创CI与ABI功能接入位置框图','empirical_data':False,'anatomical_reconstruction':False,'source_ids':['house-hitselberger-1984','house-shannon-2015','zeng-2008'],'exports':['svg','png']}]
(R/'figure-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Generated two original functional diagrams (SVG and PNG).')
