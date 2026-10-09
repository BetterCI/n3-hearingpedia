"""Original explanatory figures; Gaussian overlap is a toy model, not measured data."""
from pathlib import Path
import json, re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/auditory-pathway'
RECORD=ROOT/'docs/research/auditory-pathway-rewrite-2026-10-09'
OUT.mkdir(parents=True,exist_ok=True);RECORD.mkdir(parents=True,exist_ok=True)
FONT=FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':FONT.get_name(),'font.size':14,'axes.unicode_minus':False,
 'svg.fonttype':'path','svg.hashsalt':'auditory-pathway-2026-10-09','axes.spines.top':False,
 'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})
BLUE='#266588';ORANGE='#ab612b';INK='#253743';GRAY='#697b84'
manifest=[]
def save(fig,name,description):
 for ext in ['svg','png']:
  p=OUT/(name+'.'+ext)
  fig.savefig(p,dpi=180,metadata={'Date':None} if ext=='svg' else None,bbox_inches='tight',pad_inches=.2)
  if ext=='svg':p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
 manifest.append({'name':name,'files':[name+'.svg',name+'.png'],'type':'original explanatory figure',
  'description':description,'generator':'scripts/generate-auditory-pathway.py','empirical_data':False})
 plt.close(fig)
def canvas(height):
 fig,ax=plt.subplots(figsize=(6.6,height));ax.set_xlim(0,10);ax.set_ylim(0,height);ax.axis('off');return fig,ax
def box(ax,x,y,text,w=2.5,h=.7,color=BLUE):
 ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.08',facecolor='white',edgecolor=color,lw=1.6))
 ax.text(x,y,text,ha='center',va='center',fontsize=14,color=INK)
def arrow(ax,a,b,color=BLUE,style='-',inhibit=False):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-[' if inhibit else '-|>',mutation_scale=15,lw=1.8,color=color,linestyle=style))

fig,ax=canvas(10.8)
ax.text(.1,10.45,'A　内侧上橄榄：比较两耳输入的时间',fontsize=15,weight='bold',color=INK)
box(ax,1.65,9.4,'左耳蜗核\n兴奋性输入');box(ax,8.35,9.4,'右耳蜗核\n兴奋性输入')
box(ax,5,7.75,'内侧上橄榄\nMSO',w=3.1,h=.9)
arrow(ax,(2.4,8.98),(4.2,8.23));arrow(ax,(7.6,8.98),(5.8,8.23))
ax.text(2.9,8.4,'＋',color=BLUE,fontsize=20);ax.text(6.8,8.4,'＋',color=BLUE,fontsize=20)
ax.text(5,6.9,'相对到达时间、突触与膜性质\n共同塑造时差调谐',ha='center',va='center',fontsize=14,color=GRAY)
ax.plot([.2,9.8],[6.15,6.15],color='#cfd9de',lw=1)
ax.text(.1,5.75,'B　外侧上橄榄：兴奋与抑制的平衡',fontsize=15,weight='bold',color=INK)
box(ax,1.65,4.75,'同侧耳蜗核\n兴奋性输入');box(ax,8.35,4.75,'对侧耳蜗核\n兴奋性输入')
box(ax,8.35,3.2,'梯形体内侧核\nMNTB',h=.85,color=ORANGE)
box(ax,3.6,3.2,'外侧上橄榄\nLSO',w=3,h=.85)
arrow(ax,(2.15,4.32),(3.15,3.67));ax.text(2.05,3.8,'＋',color=BLUE,fontsize=20)
arrow(ax,(8.35,4.32),(8.35,3.68));ax.text(8.65,3.96,'＋',color=BLUE,fontsize=20)
arrow(ax,(7.02,3.2),(5.16,3.2),color=ORANGE,inhibit=True)
ax.text(6.15,3.6,'抑制',ha='center',fontsize=14,color=ORANGE)
ax.text(5,2.05,'声级和时序均会影响响应\n下游继续整合多种空间线索',ha='center',va='center',fontsize=14,color=GRAY)
ax.text(5,.8,'箭头：兴奋输入　　横挡：抑制输入\n仅示意经典连接，不列出全部细胞和支路',ha='center',fontsize=12,color=GRAY)
save(fig,'02-binaural-circuits','经典MSO双侧兴奋汇聚与LSO同侧兴奋／对侧经MNTB抑制；非完整解剖图。')

tau=np.linspace(-.8,.8,1601);sigmas=[.08,.20];t=np.arange(-3,3.0005,.0005)
errors=[]
for sigma in sigmas:
 for delay in [-.2,0,.2]:
  for test_tau in [-.4,0,.2,.5]:
   left=np.exp(-(t-delay)**2/(2*sigma**2));right=np.exp(-(t-test_tau)**2/(2*sigma**2))
   numeric=np.trapz(left*right,t)/np.trapz(left*left,t)
   analytic=np.exp(-(test_tau-delay)**2/(4*sigma**2))
   errors.append(abs(numeric-analytic))
assert max(errors)<1e-8
fig,axs=plt.subplots(3,1,figsize=(6.6,10.8),layout='constrained')
display_t=np.linspace(-.5,.7,1201)
axs[0].plot(display_t,np.exp(-display_t**2/(2*.08**2)),color=BLUE,lw=2,label='左输入：0 ms')
axs[0].plot(display_t,np.exp(-(display_t-.2)**2/(2*.08**2)),color=ORANGE,lw=2,ls='--',label='右输入：0.20 ms')
axs[0].set(title='A　输入峰的相对到达时间',xlabel='时间 t（ms）',ylabel='归一化输入',ylim=(-.03,1.12))
axs[0].legend(fontsize=12,loc='upper right')
for sigma,ls,col in zip(sigmas,['-','--'],[BLUE,ORANGE]):
 axs[1].plot(tau,np.exp(-tau**2/(4*sigma**2)),ls=ls,color=col,lw=2,label=f'σ = {sigma:.2f} ms')
axs[1].axhline(.5,color=GRAY,lw=1,ls=':')
axs[1].set(title='B　输入越宽，重叠曲线越宽（d = 0）',xlabel='右减左的到达时差 τ（ms）',ylabel='重叠读出 C',ylim=(-.03,1.12))
axs[1].legend(fontsize=12)
for d,ls,col in zip([-.2,0,.2],[':','-','--'],[GRAY,BLUE,ORANGE]):
 curve=np.exp(-(tau-d)**2/(4*.08**2));assert abs(tau[curve.argmax()]-d)<1e-10
 axs[2].plot(tau,curve,ls=ls,color=col,lw=2,label=f'd = {d:+.2f} ms')
axs[2].set(title='C　内部延迟移动峰值（σ = 0.08 ms）',xlabel='右减左的到达时差 τ（ms）',ylabel='重叠读出 C',ylim=(-.03,1.12))
axs[2].legend(fontsize=12)
for ax in axs:ax.grid(alpha=.15);ax.tick_params(labelsize=12)
save(fig,'03-temporal-overlap','无噪声高斯输入的解析重叠：输入宽度改变半高全宽，内部延迟改变峰值位置；教学参数，非生理实测。')

fig,ax=canvas(9.8)
ax.text(.1,9.45,'上行处理与下行调节形成闭合回路',fontsize=15,weight='bold',color=INK)
for y,text in [(8.35,'听觉皮层'),(6.65,'丘脑内侧膝状体'),(4.95,'下丘'),(3.25,'脑干回路（含上橄榄复合体）'),(1.5,'耳蜗与听神经输入')]:box(ax,5,y,text,w=5.6,h=.7)
for y in [1.5,3.25,4.95,6.65]:arrow(ax,(3.5,y+.43),(3.5,y+1.26),color=BLUE)
arrow(ax,(6.5,7.92),(6.5,7.08),color=ORANGE,style='--')
ax.text(7.8,7.5,'皮层—丘脑',fontsize=12,color=ORANGE,ha='center')
ax.plot([7.88,9.25,9.25],[8.35,8.35,4.95],color=ORANGE,lw=1.8,ls='--')
arrow(ax,(9.25,4.95),(7.88,4.95),color=ORANGE,style='--')
ax.text(9.7,6.6,'皮\n层\n—\n下\n丘',fontsize=12,color=ORANGE,ha='center')
arrow(ax,(6.5,2.82),(6.5,1.93),color=ORANGE,style='--')
ax.text(7.9,2.4,'橄榄耳蜗束',fontsize=12,color=ORANGE,ha='center')
ax.text(5,.35,'实线：上行　　虚线：示例下行联系\n示意连接层级；未显示全部跨侧和中间支路',ha='center',fontsize=12,color=GRAY)
save(fig,'04-feedback-network','皮层丘脑、皮层下丘和橄榄耳蜗反馈示意；不是皮层直接投射耳蜗。')

fig,ax=canvas(9.8)
ax.text(.1,9.45,'不同证据回答不同层面的问题',fontsize=15,weight='bold',color=INK)
rows=[('A　解剖示踪','起点、终点、细胞类型与连接方向','存在连接 ≠ 当前任务中必须使用'),
 ('B　神经活动记录','刺激锁定、选择性、时间与群体表征','能解码行为 ≠ 该区域驱动行为'),
 ('C　可逆干预与损伤','急性必要性、长期保留与学习改变','短时抑制与损伤后表现分别比较')]
for y,(title,readout,limit) in zip([8.3,5.5,2.7],rows):
 box(ax,5,y,title,w=8.3,h=.6)
 ax.text(5,y-1,readout,ha='center',fontsize=14,color=INK)
 ax.text(5,y-1.65,limit,ha='center',fontsize=13,color=GRAY)
ax.text(5,.25,'结论应绑定物种、任务、记录位置和干预时间',ha='center',fontsize=13,color=INK)
save(fig,'05-evidence-design','解剖连接、活动相关和因果干预的证据矩阵；强调急性和长期干预差异。')

report={'model':'normalized Gaussian temporal overlap','units':'all temporal parameters in ms',
 'sigmas_ms':sigmas,'internal_delays_ms':[-.2,0,.2],
 'integration':{'t_range_ms':[-3,3],'dt_ms':.0005,'max_absolute_error':max(errors)},
 'fwhm_ms':{str(s):4*s*np.sqrt(np.log(2)) for s in sigmas},
 'C_at_residual_0_2_ms':{str(s):float(np.exp(-.2**2/(4*s*s))) for s in sigmas},
 'figures':manifest,'original_anatomy':'pathway-openstax.png unchanged; separately credited in article'}
(RECORD/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='figures'},ensure_ascii=False,indent=2))
