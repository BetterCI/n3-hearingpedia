"""Deterministic editorial teaching diagrams, with no fitted or measured data."""
from pathlib import Path
import json, re, html
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/speech-perception'
RESEARCH=ROOT/'docs/research/speech-perception-2026-10-10'
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':16,'svg.fonttype':'path',
 'axes.spines.top':False,'axes.spines.right':False,'axes.unicode_minus':False})
BLUE,ORANGE,GREEN,GRAY='#286a9b','#b65d2e','#327965','#687481'
def logistic(x):return 1/(1+np.exp(-x))
def save(fig,name,w=1400,h=700):
 fig.savefig(OUT/(name+'.png'),dpi=100,facecolor='white')
 fig.savefig(OUT/(name+'.svg'),facecolor='white')
 path=OUT/(name+'.svg');svg=path.read_text(encoding='utf-8')
 svg=re.sub(r'width="[^"]+" height="[^"]+"',f'width="{w}" height="{h}"',svg,count=1)
 path.write_text(svg,encoding='utf-8');plt.close(fig)

fig=plt.figure(figsize=(14,8.2));ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1400),ylim=(820,0));ax.axis('off')
def box(x,y,w,h,title,lines,color):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',
  edgecolor=color,facecolor='#fbfcfd',linewidth=1.8))
 ax.text(x+w/2,y+40,title,ha='center',va='center',color=color,fontsize=20,weight='bold')
 ax.text(x+w/2,y+85,'\n'.join(lines),ha='center',va='top',fontsize=17,linespacing=1.7,color='#253743')
ax.text(55,55,'（a）解释对象：从输入到语言判断',fontsize=21,weight='bold')
for x,title,lines,color in [
 (55,'声学输入与分析',['谱结构 · 起止时序','周期性 · 强度起伏'],GRAY),
 (390,'线索与语音类别',['多条线索的整合','连续差异与类别判断'],BLUE),
 (725,'词语候选与分割',['可能的词语','随输入更新与竞争'],ORANGE),
 (1060,'内容理解',['词句的意义','记忆与交流任务'],GREEN)]:box(x,105,285,180,title,lines,color)
for x in [347,682,1017]:ax.annotate('',xy=(x+35,195),xytext=(x,195),arrowprops={'arrowstyle':'->','color':GRAY,'lw':2})
box(260,340,880,135,'语言经验 · 前后语境 · 视觉信息 · 注意',['可参与不同阶段，具体联系需要实验检验'],GREEN)
for x in [197,532,867,1202]:ax.annotate('',xy=(x,293),xytext=(700,330),arrowprops={'arrowstyle':'->','color':GREEN,'lw':1.3,'linestyle':'--'})
ax.text(55,545,'（b）观察入口：不同记录回答不同问题',fontsize=21,weight='bold')
for x,title,lines,color in [
 (55,'声学观察',['语谱图 · 时间标记','核对可用线索'],GRAY),
 (500,'行为观察',['类别 · 辨别 · 词句任务','记录响应与错误'],BLUE),
 (945,'神经观察',['诱发活动 · 特征编码','与行为及模型相互约束'],ORANGE)]:box(x,590,400,155,title,lines,color)
ax.text(700,790,'概念框图；箭头不指定唯一顺序、解剖位置或已证实的反馈通路。',ha='center',fontsize=16,color=GRAY)
save(fig,'01-levels',1400,820)

grid=np.linspace(0,1,201);x,y=np.meshgrid(grid,grid)
fig,axs=plt.subplots(1,2,figsize=(14,7),sharex=True,sharey=True)
for ax,(a,b,label) in zip(axs,[(8,3,'（a）线索 1 的系数较大'),(3,8,'（b）线索 2 的系数较大')]):
 p=logistic(a*(x-.5)+b*(y-.5))
 im=ax.imshow(p,origin='lower',extent=[0,1,0,1],vmin=0,vmax=1,cmap='cividis',aspect='equal')
 ax.contour(x,y,p,levels=[.5],colors=['white'],linewidths=2,linestyles='--')
 ax.scatter([.8],[.2],s=110,facecolors='none',edgecolors='white',linewidths=2)
 ax.set(title=label,xlabel='线索 1 / 教学坐标',xticks=[0,.5,1],yticks=[0,.5,1])
 ax.text(.04,.93,f'系数 {a} 与 {b}',transform=ax.transAxes,color='white',fontsize=17)
 ax.text(.04,.04,f'冲突点 (0.8, 0.2)：P(B) = {logistic(a*.3-b*.3):.3f}',transform=ax.transAxes,
  fontsize=15,color='white',bbox={'facecolor':'#253743','alpha':.8,'edgecolor':'none','pad':5})
axs[0].set_ylabel('线索 2 / 教学坐标')
fig.subplots_adjust(left=.075,right=.85,bottom=.15,top=.86,wspace=.2)
cax=fig.add_axes([.89,.25,.025,.48]);fig.colorbar(im,cax=cax,ticks=[0,.5,1],label='选择 B 的模型概率')
fig.text(.5,.04,'两图共享线索与概率尺度；虚线是 50% 等值线。权重人为设定，非听者拟合。',ha='center',fontsize=16,color=GRAY)
save(fig,'02-cue-integration')

v=np.linspace(0,80,401)
fig,axs=plt.subplots(1,2,figsize=(14,7),sharex=True,sharey=True)
for beta,color,style in [(0.1,BLUE,'-'),(.2,ORANGE,'--')]:
 axs[0].plot(v,logistic(beta*(v-40)),color=color,lw=3,ls=style,label=f'系数 {beta:.2f} / ms')
axs[0].axvline(40,color=GRAY,ls=':',lw=1.5);axs[0].set_title('（a）中点相同，斜率不同',pad=20)
f1=logistic(.25*(v-25));f2=logistic(.25*(v-55))
axs[1].plot(v,f1,color=BLUE,lw=2.5,label='个体 A：中点 25 ms')
axs[1].plot(v,f2,color=ORANGE,lw=2.5,label='个体 B：中点 55 ms')
axs[1].plot(v,(f1+f2)/2,color=GRAY,lw=3,ls='--',label='等权平均')
axs[1].set_title('（b）边界差异使平均曲线变宽',pad=20)
for ax in axs:
 ax.axhline(.5,color='#c5cdd3',ls=':',lw=1.5)
 ax.set(xlim=(0,80),ylim=(0,1),xlabel='起声时间 / ms',yticks=[0,.5,1])
 ax.legend(loc='upper left',fontsize=15);ax.grid(alpha=.15)
axs[0].set_ylabel('选择 B 的响应概率')
fig.subplots_adjust(left=.08,right=.975,top=.85,bottom=.18,wspace=.2)
fig.text(.5,.055,'解析教学曲线：纵轴不是正确率；没有真实个体、辨别数据或误差线。',ha='center',fontsize=16,color=GRAY)
save(fig,'03-category-functions')

ratio=np.geomspace(.01,100,401)
def posterior(likelihood,prior):
 odds=likelihood*prior/(1-prior);return odds/(1+odds)
fig=plt.figure(figsize=(14,7));ax=fig.add_axes([.08,.18,.53,.67])
for prior,color,style in [(.5,BLUE,'-'),(.8,ORANGE,'--')]:
 ax.semilogx(ratio,posterior(ratio,prior),color=color,lw=3,ls=style,label=f'A 的先验 = {prior:.1f}')
 for r in [.05,.4]:ax.scatter([r],[posterior(r,prior)],color=color,s=85,zorder=5)
ax.axvline(1,color=GRAY,ls=':',lw=1.5);ax.axhline(.5,color='#c5cdd3',ls=':',lw=1.5)
ax.set(xlim=(.01,100),ylim=(0,1),xlabel='声学似然比：支持 A / 支持 B',ylabel='A 的后验概率',title='（a）同一声学证据，与不同先验组合')
ax.set_xticks([.01,.1,1,10,100],['0.01','0.1','1','10','100']);ax.legend(fontsize=16);ax.grid(alpha=.15)
ax2=fig.add_axes([.68,.18,.3,.67]);ax2.axis('off')
ax2.text(0,1,'（b）两组教学算例',fontsize=20,va='top',weight='bold')
ax2.text(0,.85,'模糊证据：似然比 0.4\n\n先验 0.5 → 后验 0.286\n先验 0.8 → 后验 0.615',fontsize=17,va='top',linespacing=1.5)
ax2.text(0,.38,'更支持 B：似然比 0.05\n\n先验 0.8 → 后验 0.167',fontsize=17,va='top',linespacing=1.5)
fig.text(.5,.05,'两候选解析模型；先验与似然比均人为设定，后验不是实测正确率。',ha='center',fontsize=16,color=GRAY)
save(fig,'04-context-evidence')

report={'nature':'original deterministic teaching calculations; no measured data',
 'cue_coefficients':[[8,3],[3,8]],'cue_coordinates':[0,1],
 'category_midpoint_ms':40,'category_beta_per_ms':[.1,.2],
 'individual_midpoints_ms':[25,55],'individual_beta_per_ms':.25,
 'priors_A':[.5,.8], 'posterior_examples':{
  'ratio_0.4_prior_0.5':posterior(.4,.5),'ratio_0.4_prior_0.8':posterior(.4,.8),
  'ratio_0.05_prior_0.8':posterior(.05,.8)},
 'category_examples':{'35ms_beta_0.2':float(logistic(.2*(35-40))),
  '45ms_beta_0.2':float(logistic(.2*(45-40))), '35ms_beta_0.1':float(logistic(.1*(35-40))),
  '45ms_beta_0.1':float(logistic(.1*(45-40)))},
 'figure_sizes':{'01-levels':[1400,820],'02-cue-integration':[1400,700],
 '03-category-functions':[1400,700],'04-context-evidence':[1400,700]},
 'randomness':'none','fonts':'Microsoft YaHei; SVG text converted to paths',
 'license':'original editorial figures; no reproduced source images'}
assert np.isclose(posterior(.4,.8),8/13)
assert np.isclose(posterior(.05,.8),1/6)
assert np.isclose(logistic(.2*(40-40)),.5)
assert np.all(np.diff((f1+f2)/2)>0)
(RESEARCH/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=True))
