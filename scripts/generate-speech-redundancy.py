"""Original teaching figures; finite discrete examples, no participant data."""
from pathlib import Path
import json, re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/speech-redundancy'
RECORD=ROOT/'docs/research/speech-redundancy-2026-10-09'
OUT.mkdir(parents=True,exist_ok=True); RECORD.mkdir(parents=True,exist_ok=True)
FONT=FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':FONT.get_name(),'font.size':25,'axes.unicode_minus':False,
 'svg.fonttype':'path','svg.hashsalt':'speech-redundancy-2026-10-09',
 'figure.facecolor':'white','savefig.facecolor':'white'})
BLUE='#24678d'; ORANGE='#b3652d'; GREEN='#39775a'; GRAY='#65747d'; INK='#263944'; PALE='#eaf2f6'
manifest=[]

def canvas(height=840):
 fig=plt.figure(figsize=(1200/72,height/72)); ax=fig.add_axes([.02,.025,.96,.95])
 ax.set_xlim(0,12); ax.set_ylim(0,height/100); ax.axis('off'); return fig,ax

def box(ax,x,y,text,w=3.3,h=1.2,color=BLUE,fill='white',size=25):
 ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.06',lw=2,facecolor=fill,edgecolor=color))
 ax.text(x,y,text,ha='center',va='center',fontsize=size,color=INK)

def arrow(ax,a,b,color=BLUE):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=24,linewidth=2.4,color=color))

def save(fig,name,description,parameters):
 for ext in ('svg','png'):
  p=OUT/(name+'.'+ext); fig.savefig(p,dpi=90,metadata={'Date':None} if ext=='svg' else None)
  if ext=='svg': p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
 svg=(OUT/(name+'.svg')).read_text(encoding='utf8')
 manifest.append({'name':name,'files':[name+'.svg',name+'.png'],
  'svg_viewbox':[float(x) for x in re.search(r'viewBox="([^"]+)"',svg).group(1).split()],
  'description':description,'parameters':parameters,'empirical_data':False,
  'generator':'scripts/generate-speech-redundancy.py','attribution':'n³ Hearingpedia；AI 辅助编写与绘图',
  'copyright':'原创教学图；未转载论文图片',
  'usage':'用于本站词条展示和教学计算复现；对外开放许可证依项目约定，尚待维护者确定'})
 plt.close(fig)

fig,ax=canvas()
ax.text(.2,7.8,'语音冗余性：先说明层次，再说明任务',fontsize=31,weight='bold',color=INK)
box(ax,2,6.25,'声学线索\n时域、频谱、韵律',fill=PALE)
box(ax,6,6.25,'语言约束\n音系、词汇、句子',fill=PALE)
box(ax,10,6.25,'其他输入\n口形、场景、双耳',fill=PALE)
box(ax,6,3.55,'可用线索与听者知识\n重复、互补或协同',w=5.8,h=1.4,color=GREEN)
arrow(ax,(2,5.58),(4.2,4.32)); arrow(ax,(6,5.58),(6,4.32)); arrow(ax,(10,5.58),(7.8,4.32))
arrow(ax,(6,2.8),(6,1.9),GREEN)
ax.text(6,1.4,'任务：识词、理解、辨声调、辨说话人……',ha='center',fontsize=28,color=INK)
ax.text(6,.55,'识别正确率、连续感与聆听努力分别测量',ha='center',fontsize=26,color=GRAY)
save(fig,'01-levels-and-task','分层框图；箭头不编码效应大小或独立神经通路。',{'data':None})

fig,ax=canvas(900)
ax.text(.2,8.35,'相同保留比例，可以有不同的缺失结构',fontsize=31,weight='bold',color=INK)
start=2.8; width=8.5; duration=1.; duty=.5
for y,f in [(6.95,2),(5.45,10)]:
 ax.text(.1,y,'慢中断：2 Hz' if f==2 else '快中断：10 Hz',va='center',fontsize=25,color=INK)
 for i in range(f):
  left=start+width*i/f
  ax.add_patch(Rectangle((left,y-.28),width*duty/f,.56,color=BLUE))
  ax.add_patch(Rectangle((left+width*duty/f,y-.28),width*(1-duty)/f,.56,facecolor='#f1f2f3',edgecolor='#bdc7cc'))
 ax.text(7,y-.66,f'每周期：保留 {1000*duty/f:.0f} ms ＋ 删除 {1000*(1-duty)/f:.0f} ms',ha='center',fontsize=23,color=GRAY)
ax.plot([start,start+width],[4.25,4.25],color=GRAY,lw=1.5)
for t in [0,.5,1]:
 x=start+width*t; ax.plot([x,x],[4.15,4.35],color=GRAY); ax.text(x,3.9,f'{t:g}',ha='center',fontsize=23,color=GRAY)
ax.text(7,3.45,'时间（s）；两种示例都保留总时长的 50%',ha='center',fontsize=25,color=INK)
box(ax,3.1,2,'删除段填静音\n缺口中没有目标语音',w=4.4,h=1.25)
box(ax,8.7,2,'删除段填噪声\n缺口中仍没有目标语音',w=4.4,h=1.25,color=ORANGE)
ax.text(6,.6,'填噪声与在完整语音上叠加噪声，是两种操作',ha='center',fontsize=26,color=GRAY)
save(fig,'02-interruption-patterns','1秒教学时间条；50%占空比，非语音波形、无识别结果。',
 {'duration_s':1,'interruption_rates_hz':[2,10],'speech_duty_cycle':.5,'retained_durations_ms':[250,50],
 'gap_durations_ms':[250,50],'blue':'保留原片段','pale':'删除原片段后填静音或噪声','prediction_of_performance':False})

def entropy(values):
 p=np.array(values,float); p=p[p>0]; return float(-np.sum(p*np.log2(p)))
def info(rows):
 # Uniform rows list (target, cueA, cueB); calculate from distributions.
 def h(idx):
  keys=[tuple(row[i] for i in idx) for row in rows]
  return entropy([keys.count(k)/len(keys) for k in set(keys)])
 hs=h([0]); return {'H_target':hs,'I_A':hs+h([1])-h([0,1]),'I_B':hs+h([2])-h([0,2]),
  'I_AB':hs+h([1,2])-h([0,1,2])}
duplicate=info([(s,s//2,s//2) for s in range(4)])
complement=info([(s,s//2,s%2) for s in range(4)])
xor=info([(a^b,a,b) for a in range(2) for b in range(2)])
assert duplicate=={'H_target':2,'I_A':1,'I_B':1,'I_AB':1}
assert complement=={'H_target':2,'I_A':1,'I_B':1,'I_AB':2}
assert xor=={'H_target':1,'I_A':0,'I_B':0,'I_AB':1}
fig,ax=canvas(900)
ax.text(.2,8.35,'重复、互补与协同：三个离散教学例子',fontsize=31,weight='bold',color=INK)
for x,title,rule,result,color in [
 (2,'重复','S = 两位标签\nA = 首位，B = 首位','单独：1 bit、1 bit\n共同：1 bit',BLUE),
 (6,'互补','S = 两位标签\nA = 首位，B = 次位','单独：1 bit、1 bit\n共同：2 bit',GREEN),
 (10,'协同','S = A 异或 B\nA、B 为独立公平位','单独：0 bit、0 bit\n共同：1 bit',ORANGE)]:
  box(ax,x,6.65,title,w=3.1,h=.85,color=color,fill=PALE,size=30)
  ax.text(x,5.05,rule,ha='center',va='center',fontsize=25,color=INK,linespacing=1.8)
  arrow(ax,(x,4.25),(x,3.45),color)
  box(ax,x,2.7,result,w=3.3,h=1.4,color=color,size=25)
ax.text(6,1.25,'左、中目标熵为 2 bit；右侧目标熵为 1 bit',ha='center',fontsize=26,color=INK)
ax.text(6,.5,'数值为互信息；不是语音实验数据或人类识别正确率',ha='center',fontsize=25,color=GRAY)
save(fig,'03-information-examples','三个完整有限概率模型的互信息计算。',
 {'duplicate':duplicate,'complement':complement,'xor':xor,'row_probability':.25,'noise':None})

fig,ax=canvas(900)
ax.text(.2,8.35,'实验设计：把语境获益与填充噪声获益分开',fontsize=30,weight='bold',color=INK)
ax.text(4.35,7.25,'删除段填静音',ha='center',fontsize=27,color=BLUE)
ax.text(9.05,7.25,'删除段填噪声',ha='center',fontsize=27,color=ORANGE)
for y,context,letter1,letter2 in [(5.95,'低预测语境','A','B'),(3.85,'高预测语境','C','D')]:
 ax.text(.1,y,context,fontsize=25,color=INK,va='center')
 box(ax,4.35,y,f'{letter1}：关键词正确率',w=3.95,h=1.15)
 box(ax,9.05,y,f'{letter2}：关键词正确率',w=3.95,h=1.15,color=ORANGE)
 arrow(ax,(6.45,y),(6.95,y),GRAY)
ax.text(6,2.4,'填充噪声差值：B − A；D − C（百分点）',ha='center',fontsize=26,color=INK)
ax.text(6,1.6,'语境差值：C − A；D − B（百分点）',ha='center',fontsize=26,color=INK)
ax.text(6,.7,'材料匹配、列表平衡；另测连续感与努力，不预设差值为正',ha='center',fontsize=24,color=GRAY)
save(fig,'04-factorial-design','2×2条件框图；字母占位，无伪造分数或统计显著性。',
 {'context_levels':['低预测','高预测'],'gap_fill':['静音','噪声'],'outcome':'关键词正确率（%）',
 'difference_unit':'百分点','empirical_scores':None,'causal_claim':'需材料匹配与随机平衡，不以该图证明机制'})
context_h=entropy([.7,.1,.1,.1]); assert np.isclose(context_h,1.3567796494470397)
(RECORD/'figure-verification.json').write_text(json.dumps({'figures':manifest,
 'numerical_checks':{'uniform_four_target_entropy_bits':2,'single_context_entropy_bits':context_h,
 'single_context_difference_bits':2-context_h,'duplicate':duplicate,'complement':complement,'xor':xor},
 'visual_review':'pending'},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Generated four SVG + PNG figures; all finite-probability and time-window checks passed.')
