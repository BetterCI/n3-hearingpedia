"""Five original teaching figures; no empirical data or paper figure reproduction."""
from pathlib import Path
import json, re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/auditory-cortex'
RECORD=ROOT/'docs/research/auditory-cortex-2026-10-09'
OUT.mkdir(parents=True,exist_ok=True)
FONT=FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':FONT.get_name(),'font.size':27,'axes.unicode_minus':False,
 'svg.fonttype':'path','svg.hashsalt':'auditory-cortex-2026-10-09','figure.facecolor':'white',
 'savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
BLUE='#24678d';ORANGE='#b3652d';INK='#263944';GRAY='#627681';PALE='#eaf2f6'
manifest=[]

def save(fig,name,description,parameters=None):
 for ext in ('svg','png'):
  p=OUT/(name+'.'+ext)
  fig.savefig(p,dpi=90,metadata={'Date':None} if ext=='svg' else None)
  if ext=='svg':
   p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
 svg=(OUT/(name+'.svg')).read_text(encoding='utf8')
 vb=re.search(r'viewBox="([^"]+)"',svg).group(1).split()
 manifest.append({'name':name,'files':[name+'.svg',name+'.png'],'svg_viewbox':[float(v) for v in vb],
  'description':description,'parameters':parameters or {},'empirical_data':False,
  'generator':'scripts/generate-auditory-cortex.py','copyright':'原创教学图，未复制来源图片'})
 plt.close(fig)

def canvas(height=960):
 fig=plt.figure(figsize=(1200/72,height/72))
 ax=fig.add_axes([.025,.025,.95,.95]);ax.set_xlim(0,12);ax.set_ylim(0,height/100);ax.axis('off')
 return fig,ax

def box(ax,x,y,text,w=3.4,h=1.4,color=BLUE,fill='white',size=27):
 ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.06',lw=2,
  facecolor=fill,edgecolor=color))
 ax.text(x,y,text,ha='center',va='center',fontsize=size,color=INK)

def arrow(ax,a,b,double=False,dashed=False,color=BLUE):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='<->' if double else '-|>',mutation_scale=25,
  linewidth=2.5,linestyle='--' if dashed else '-',color=color))

fig,ax=canvas()
ax.text(.2,9.12,'区域组织：平行输入与双向联系',fontsize=32,weight='bold',color=INK)
box(ax,6,7.8,'听觉丘脑\n不同分区及投射',w=4,h=1.35,fill=PALE)
box(ax,2,5.5,'核心区 core\nA1 等初级样区域',w=3.35)
box(ax,6,5.5,'带状区 belt\n多个周边区域',w=3.35)
box(ax,10,5.5,'旁带区 parabelt\n更外侧的区域',w=3.35)
arrow(ax,(5,7.1),(2,6.27));arrow(ax,(6,7.1),(6,6.27))
arrow(ax,(3.74,5.5),(4.26,5.5),double=True)
arrow(ax,(7.74,5.5),(8.26,5.5),double=True)
box(ax,8,3.05,'其他皮层网络',w=5,h=1.15,color=ORANGE)
arrow(ax,(6,4.74),(7.15,3.66),double=True,dashed=True,color=ORANGE)
arrow(ax,(10,4.74),(9,3.66),double=True,dashed=True,color=ORANGE)
ax.text(6,1.75,'区域边界：个体解剖＋结构特征＋功能定位',ha='center',fontsize=29,color=INK)
ax.text(6,.65,'灵长类框架的概念图；未列出全部连接\n框的位置与大小不代表解剖距离和面积',ha='center',va='center',fontsize=25,color=GRAY)
save(fig,'01-regions-and-connections','灵长类区域框架与部分平行、双向联系；不是完整连接图或人类固定分区。')

K=np.array([[0,0,.5],[1,-.5,0],[0,0,0]],dtype=float)
XA=np.zeros((3,3));XB=np.zeros((3,3));XA[1,0]=1;XB[1,:2]=1
b=2.;g=10.;drives=[float((K*x).sum()) for x in (XA,XB)]
rates=[max(0,b+g*v) for v in drives]
assert drives==[1.,.5] and rates==[12.,7.]
assert XA[1,0]==XB[1,0] and XA[1,1]!=XB[1,1]
fig=plt.figure(figsize=(1200/72,1200/72))
ax=fig.add_axes([.14,.69,.70,.23])
im=ax.imshow(K,vmin=-1,vmax=1,cmap='RdBu',aspect='auto')
for i in range(3):
 for j in range(3):ax.text(j,i,f'{K[i,j]:g}',ha='center',va='center',fontsize=29,color='white' if abs(K[i,j])>=.8 else INK)
ax.set_xticks(range(3),['0','20','40']);ax.set_yticks(range(3),['0.5','1','2'])
ax.set_xlabel('延迟（ms）',labelpad=4);ax.set_ylabel('频率通道（kHz）')
ax.set_title('（a）教学权重 K：数字保留正负号',loc='left',fontsize=30,pad=17)
cb=fig.colorbar(im,cax=fig.add_axes([.88,.69,.025,.23]));cb.set_ticks([-1,0,1]);cb.ax.tick_params(labelsize=23)
ax=fig.add_axes([.14,.39,.77,.17])
ax.plot([-40,-20,0],XA[1,::-1],'-o',lw=3,ms=11,color=BLUE,label='A：前一采样为 0')
ax.plot([-40,-20,0],XB[1,::-1],'--s',lw=3,ms=10,color=ORANGE,label='B：前一采样为 1')
ax.set_xticks([-40,-20,0]);ax.set_yticks([0,1]);ax.set_ylim(-.1,1.6)
ax.set_xlabel('相对当前采样的时间（ms）');ax.set_ylabel('归一化能量\n（无量纲）')
ax.set_title('（b）当前 1 kHz 特征相同，历史不同',loc='left',fontsize=30,pad=15)
ax.legend(loc='upper left',fontsize=24,frameon=False,ncol=2)
ax=fig.add_axes([.14,.105,.77,.17])
ax.bar(['A','B'],rates,color=[BLUE,ORANGE],width=.5)
ax.axhline(b,color=GRAY,ls='--',lw=2);ax.text(.7,2.6,'基线 b = 2',fontsize=24,color=GRAY)
for i,r in enumerate(rates):ax.text(i,r+.35,f'{r:g}',ha='center',fontsize=29,color=INK)
ax.set_ylim(0,15);ax.set_yticks([0,5,10,15]);ax.set_ylabel('模型放电率\n（spikes/s）')
ax.set_title('（c）按同一权重、基线和增益计算',loc='left',fontsize=30,pad=12)
fig.text(.5,.015,'教学计算：全部参数人为设定，未拟合真实神经数据',ha='center',fontsize=24,color=GRAY)
save(fig,'02-strf-teaching-example','离散声谱时间模型；保持当前特征相同，改变20ms前输入，得到12和7spikes/s。',
 {'frequencies_kHz':[.5,1,2],'lag_ms':[0,20,40],'K':K.tolist(),'XA':XA.tolist(),'XB':XB.tolist(),
  'b_spikes_per_s':b,'g_spikes_per_s_per_unit':g,'weighted_inputs':drives,'predicted_rates_spikes_per_s':rates,
  'stimulus_representation':'手工设置归一化能量特征；未生成或分析真实声波','randomness':'无'})

fig,ax=canvas()
ax.text(.2,9.12,'相同片段，前后背景不同',fontsize=32,weight='bold',color=INK)
def sequence(y,left,right):
 for x,w,label,fc in [(1.9,3.4,left,'#f0f1f2'),(5.7,4.2,'共享片段 X',PALE),(9.5,3.4,right,'#f0f1f2')]:
  ax.add_patch(Rectangle((x-w/2,y-.5),w,1,facecolor=fc,edgecolor=GRAY,lw=2))
  ax.text(x,y,label,ha='center',va='center',fontsize=29,color=INK)
sequence(7.45,'背景 A','背景 B');sequence(5.75,'背景 C','背景 D')
ax.text(5.7,8.25,'X：200 ms（教学设定）',ha='center',fontsize=27,color=INK)
ax.text(.2,4.4,'在 X 中心观察两种窗口',fontsize=29,weight='bold',color=INK)
segment=(0.,200.);center=100.;windows={50:(75.,125.),300:(-50.,250.)}
assert windows[50][0]>=segment[0] and windows[50][1]<=segment[1]
assert windows[300][0]<segment[0] and windows[300][1]>segment[1]
for y,label,x,w,c in [(3.1,'50 ms',5.7,1.05,BLUE),(1.95,'300 ms',5.7,6.3,ORANGE)]:
 ax.add_patch(Rectangle((3.6,y-.3),4.2,.6,facecolor=PALE,edgecolor='none'))
 ax.add_patch(Rectangle((x-w/2,y-.38),w,.76,facecolor='none',edgecolor=c,lw=3,linestyle='--' if w>4 else '-'))
 ax.text(.15,y,label,va='center',fontsize=27,color=c)
 ax.text(9.3,y,'完全在 X 内' if w<4 else '跨入两侧背景',va='center',fontsize=26,color=c)
ax.text(6,.7,'窗口仅表示输入范围；不绘制神经响应或实测相关',ha='center',fontsize=25,color=GRAY)
save(fig,'03-context-and-windows','共享片段与矩形窗口的几何；不生成神经响应或实测整合窗口。',
 {'shared_segment_ms':[0,200],'observation_time_ms':center,'window_bounds_ms':windows,
  'long_window_context_ms_each_side':50,'operation':'几何对照；不模拟TCI估计或核函数'})

fig,ax=canvas()
ax.text(.2,9.12,'重复适应与偏差检测：添加对照',fontsize=32,weight='bold',color=INK)
seqs=[('标准：T 频繁出现',list('TTTTTTTT')),
 ('偏差：T 较少出现',list('SSSTSSSS')),
 ('控制：多个不同频率',list('ABCTDEFG'))]
for y,(label,letters) in zip([7.7,5.95,4.2],seqs):
 ax.text(.3,y+.55,label,fontsize=28,color=INK)
 for j,letter in enumerate(letters):
  x=.75+j*1.47
  ax.add_patch(plt.Circle((x,y-.03),.31,facecolor=PALE if letter=='T' else '#f0f1f2',edgecolor=BLUE if letter=='T' else GRAY,lw=2))
  ax.text(x,y-.03,letter,ha='center',va='center',fontsize=27,color=INK)
  if j==3:ax.add_patch(Rectangle((x-.46,y-.49),.92,.92,fill=False,edgecolor=ORANGE,lw=2.5))
ax.text(6,2.55,'框出的 T：比较同一声音在不同背景中的响应',ha='center',fontsize=27,color=INK)
ax.text(6,1.4,'偏差 − 标准：可能混合重复适应与偏差作用\n偏差 − 控制：进一步约束解释',ha='center',va='center',fontsize=26,color=INK)
ax.text(6,.35,'短序列仅示意角色，不能据此计算实验概率或神经效果',ha='center',fontsize=24,color=GRAY)
save(fig,'04-adaptation-and-controls','同一目标声音在标准、偏差、多标准控制中的角色示意；短序列不是概率实现。',
 {'sequences':['TTTTTTTT','SSSTSSSS','ABCTDEFG'],'highlight_index_zero_based':3,
  'symbols':'同一字母代表同一频率，T为比较目标；未定义实际Hz或完整序列概率'})

fig,ax=canvas()
ax.text(.2,9.12,'三种问题需要不同证据',fontsize=32,weight='bold',color=INK)
rows=[(7.65,'记录','活动是否随刺激\n或任务变量改变？',BLUE),
 (5.9,'解码','记录中能否读出\n刺激或行为信息？',BLUE),
 (4.15,'干预','改变该区域后\n特定任务是否变化？',ORANGE)]
for y,label,question,col in rows:
 box(ax,1.6,y,label,w=2.5,h=1.25,color=col)
 arrow(ax,(2.95,y),(3.75,y),color=col)
 box(ax,7.6,y,question,w=7.4,h=1.25,color=col)
ax.plot([.2,11.8],[3.15,3.15],color='#ccd6dc',lw=2)
ax.text(6,2.7,'短时抑制与永久损伤：各有不同网络条件',ha='center',fontsize=28,color=INK)
ax.text(6,1.65,'核对操作特异性、干预范围、运动和状态\n分别检验任务表现及可能的网络调整',ha='center',va='center',fontsize=27,color=INK)
ax.text(6,.55,'没有行为变化 ≠ 所有听觉功能均不需要该区域',ha='center',fontsize=25,color=GRAY)
save(fig,'05-evidence-and-intervention','活动关联、信息解码与干预的证据问题；不呈现论文效果、不预设补偿机制。')

record={'date':'2026-10-09','figures':manifest,'checks':{
 'teaching_rates_match_formula':rates==[12.,7.],'current_inputs_equal':bool(XA[1,0]==XB[1,0]),
 'short_window_inside_shared_segment':True,'long_window_crosses_both_boundaries':True,
 'finite_K_and_inputs':bool(all(np.isfinite(x).all() for x in (K,XA,XB))),
 'empirical_errorbars_sample_sizes_or_significance':'未生成；全部图为原创教学图'}}
(RECORD/'figure-verification.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'figures':len(manifest),'rates':rates,'verified':True}))
