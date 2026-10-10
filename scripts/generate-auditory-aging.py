"""Three original teaching diagrams and one redraw of published trial estimates."""
from pathlib import Path
import json,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/auditory-aging'
DOC=ROOT/'docs/research/auditory-aging-2026-10-10'
OUT.mkdir(parents=True,exist_ok=True);DOC.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':18,'svg.fonttype':'path',
 'axes.spines.top':False,'axes.spines.right':False,'axes.unicode_minus':False})
BLUE,ORANGE,GREEN,GRAY='#286a9b','#b65d2e','#327965','#687481'

def save(fig,name,height):
 fig.savefig(OUT/(name+'.png'),dpi=100,facecolor='white')
 fig.savefig(OUT/(name+'.svg'),facecolor='white')
 p=OUT/(name+'.svg');s=p.read_text(encoding='utf-8')
 s=re.sub(r'width="[^"]+" height="[^"]+"',f'width="1400" height="{height}"',s,count=1)
 p.write_text(s,encoding='utf-8');plt.close(fig)

# Functional map; positions do not encode anatomy or effect size.
fig,ax=plt.subplots(figsize=(14,7.8));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.965,'（a）声音到任务表现：观察不同环节',ha='center',fontsize=26)
titles=['声音输入','外周编码','中枢组织','任务表现']
body=['声级与频谱\n背景声与空间','毛细胞与离子环境\n突触与听神经','时序与声源分组\n注意、记忆及语境','检测与识别\n努力、体验与参与']
positions=[.025,.275,.525,.775]
for i,x in enumerate(positions):
 ax.add_patch(FancyBboxPatch((x,.62),.2,.23,boxstyle='round,pad=.012',facecolor='#eef4f8',edgecolor=BLUE,lw=1.5))
 ax.text(x+.1,.795,titles[i],ha='center',fontsize=23,color=BLUE)
 ax.text(x+.1,.705,body[i],ha='center',va='center',fontsize=18,linespacing=1.65)
 if i<3:ax.annotate('',xy=(x+.24,.735),xytext=(x+.215,.735),arrowprops={'arrowstyle':'->','color':GRAY,'lw':1.6})
ax.text(.5,.53,'（b）测量提供互补证据，不是病变位置的一一对应表',ha='center',fontsize=24)
rows=[('听阈与耳声发射','可听度和外周功能的线索'),('行为与神经记录','处理表现及响应，需要任务与声级控制'),('自述与随访','日常困难、实际参与和个体变化')]
for y,(label,note) in zip([.405,.285,.165],rows):
 ax.add_patch(FancyBboxPatch((.035,y-.046),.93,.092,boxstyle='round,pad=.005',facecolor='#f6f7f8',edgecolor='#ccd3d9'))
 ax.text(.07,y,label,va='center',fontsize=21,color=GREEN)
 ax.text(.325,y,note,va='center',fontsize=20)
ax.text(.5,.035,'功能框架；箭头表示一般处理顺序，不表示每位听者都受损或各因素的因果强度。',ha='center',fontsize=16,color=GRAY)
fig.subplots_adjust(left=.025,right=.975,bottom=.02,top=.98)
save(fig,'01-functional-framework',780)

# Artificial psychometric functions, no listeners or fitted data.
r=np.linspace(-12,10,441);k=.6;theta_a=-4.;theta_b=0.
pa=1/(1+np.exp(-k*(r-theta_a)));pb=1/(1+np.exp(-k*(r-theta_b)))
fig,ax=plt.subplots(figsize=(14,7))
ax.plot(r,100*pa,color=BLUE,lw=3,label='教学听者 A：50% 点 −4 dB')
ax.plot(r,100*pb,color=ORANGE,lw=3,ls='--',label='教学听者 B：50% 点 0 dB')
ax.axhline(50,color=GRAY,lw=1,ls=':')
for t,c in [(theta_a,BLUE),(theta_b,ORANGE)]:
 ax.vlines(t,0,50,color=c,ls=':',lw=1.5);ax.scatter([t],[50],color=c,s=65,zorder=4)
ax.annotate('',xy=(0,58),xytext=(-4,58),arrowprops={'arrowstyle':'<->','lw':1.4,'color':GRAY})
ax.text(-2,62,'ΔSRT = 4 dB',ha='center',fontsize=20,color=GRAY)
ax.set(xlim=(-12,10),ylim=(0,103),xlabel='信噪比 / dB',ylabel='关键词识别率 / %')
ax.set_title('同样的纯音听阈，不限定同样的噪声中言语表现',fontsize=25,pad=22)
ax.legend(loc='upper left',fontsize=18);ax.grid(alpha=.15)
fig.subplots_adjust(left=.09,right=.97,top=.86,bottom=.19)
fig.text(.5,.045,'人为设定的逻辑函数；不是年龄组均值、临床常模或真实听者的数据。',ha='center',fontsize=17,color=GRAY)
save(fig,'02-speech-functions',700)

# Units: all levels are dB SPL for the same stimulus and measurement reference.
thresholds=np.array([20.,50.]);fixed=np.array([65.,65.]);equal=thresholds+30
fig,axs=plt.subplots(1,2,figsize=(14,7.6),sharey=True)
for ax,levels,title in zip(axs,[fixed,equal],['（a）同一声压级：65 dB SPL','（b）同一感觉级：30 dB SL']):
 for i,(t,l,c) in enumerate(zip(thresholds,levels,[BLUE,ORANGE])):
  ax.vlines(i,t,l,color=c,lw=5)
  ax.scatter(i,t,color=GRAY,s=80,marker='o',zorder=3)
  ax.scatter(i,l,color=c,s=95,marker='s',zorder=3)
  ax.text(i+.08,(l+t)/2,f'{l-t:.0f} dB SL',va='center',fontsize=19,color=c)
  ax.text(i-.09,t-5,f'阈值 {t:.0f}',ha='right',va='top',fontsize=16,color=GRAY)
  ax.text(i,l+5,f'呈现 {l:.0f}',ha='center',fontsize=17,color=c)
 ax.set(xlim=(-.45,1.65),ylim=(0,100),xticks=[0,1],xticklabels=['虚拟听者 A','虚拟听者 B'])
 ax.set_title(title,fontsize=23,pad=20);ax.grid(axis='y',alpha=.15)
axs[0].set_ylabel('同一刺激的声压级 / dB SPL')
handles=[Line2D([0],[0],marker='o',color=GRAY,lw=0,label='该刺激的检测阈'),Line2D([0],[0],marker='s',color=BLUE,lw=0,label='呈现声压级')]
fig.legend(handles=handles,loc='upper center',bbox_to_anchor=(.5,.985),ncol=2,fontsize=17,frameon=False)
fig.subplots_adjust(left=.095,right=.965,top=.84,bottom=.19,wspace=.25)
fig.text(.5,.065,'感觉级 = 呈现级 − 同一刺激的检测阈；等感觉级仍不保证相同响度或内在编码。',ha='center',fontsize=17,color=GRAY)
fig.text(.5,.025,'数值人为设定；没有年龄含义，不把 dB HL 与 dB SPL 混减，也不构成推荐呈现级。',ha='center',fontsize=16,color=GRAY)
save(fig,'03-level-control',760)

# Published between-arm estimates: true CIs, no invented patient data.
trial=[{'outcome':'global cognition 3-year change','estimate':.002,'lower':-.077,'upper':.081,'doi':'10.1016/S0140-6736(23)01406-X'},
 {'outcome':'HHIE-S baseline-to-year-3 change','estimate':-9.5,'lower':-11.,'upper':-8.,'doi':'10.1111/jgs.19185'}]
fig,axs=plt.subplots(1,2,figsize=(14,7.2))
for ax,row,title,limits,xlabel in zip(axs,trial,['（a）整体主要认知结局','（b）次级自评交流结局'],[(-.13,.13),(-12,2)],['组间变化差 / 标准差单位','HHIE-S 变化的组间差 / 分']):
 est,lo,hi=row['estimate'],row['lower'],row['upper']
 ax.axvline(0,color=GRAY,lw=1.4,ls='--',ymin=.32,ymax=.62)
 ax.errorbar(est,.5,xerr=[[est-lo],[hi-est]],fmt='D',ms=10,color=BLUE,lw=2.8,capsize=9)
 ax.text(sum(limits)/2,.72,f'{est:g}  [95% CI: {lo:g}, {hi:g}]',ha='center',fontsize=19)
 ax.text(sum(limits)/2,.25,'区间跨越 0' if lo<0<hi else '区间未跨越 0',ha='center',fontsize=20,color=GRAY)
 ax.set(xlim=limits,ylim=(0,1),yticks=[],xlabel=xlabel)
 ax.spines['left'].set_visible(False);ax.set_title(title,fontsize=23,pad=20)
 ax.text(sum(limits)/2,.05,'正值方向表示较少认知下降' if limits[0]>-1 else '负值方向表示自评困难减少',ha='center',fontsize=17,color=GREEN)
fig.subplots_adjust(left=.07,right=.98,top=.84,bottom=.25,wspace=.28)
fig.text(.5,.115,'同一 ACHIEVE 试验的不同结局；各用自己的单位与尺度，区间不是个体变化范围。',ha='center',fontsize=17,color=GRAY)
fig.text(.5,.065,'据 Lin 等（2023）和 Sanchez 等（2024）的原始摘要组间估计独立重绘；没有生成个体数据。',ha='center',fontsize=16,color=GRAY)
save(fig,'04-trial-outcomes',720)

assert np.isclose(1/(1+np.exp(-k*(theta_a-theta_a))),.5)
assert np.isclose(theta_b-theta_a,4)
assert np.allclose(fixed-thresholds,[45,15]) and np.allclose(equal-thresholds,[30,30])
assert trial[0]['lower']<0<trial[0]['upper'] and trial[1]['upper']<0
report={'figures':4,'teaching_figures':[1,2,3],'published_estimates_redrawn':[4],
 'psychometric':{'function':'1/(1+exp(-k*(r-theta)))','k_per_db':k,'theta_db':[theta_a,theta_b],'difference_db':4,'at_0_db':[float(pa[np.argmin(abs(r))]),float(pb[np.argmin(abs(r))])]},
 'level_control':{'threshold_spl_db':thresholds.tolist(),'fixed_spl_db':fixed.tolist(),'fixed_sl_db':(fixed-thresholds).tolist(),'equal_sl_spl_db':equal.tolist(),'equal_sl_db':30},
 'published_estimates':trial,'checks_passed':True}
(DOC/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':4,'checks_passed':True}))
