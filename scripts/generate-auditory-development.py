"""Original developmental framework, age and exposure teaching diagrams; published LOCHI estimates."""
from pathlib import Path
from statistics import NormalDist
import json,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/auditory-development';DOC=ROOT/'docs/research/auditory-development-2026-10-10'
OUT.mkdir(parents=True,exist_ok=True);DOC.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':18,'svg.fonttype':'path','axes.spines.top':False,'axes.spines.right':False,'axes.unicode_minus':False})
BLUE,ORANGE,GREEN,GRAY='#286a9b','#b65d2e','#327965','#687481'
def save(fig,name,h):
 fig.savefig(OUT/(name+'.png'),dpi=100,facecolor='white');fig.savefig(OUT/(name+'.svg'),facecolor='white')
 p=OUT/(name+'.svg');s=p.read_text(encoding='utf-8');p.write_text(re.sub(r'width="[^"]+" height="[^"]+"',f'width="1400" height="{h}"',s,count=1),encoding='utf-8');plt.close(fig)

fig,ax=plt.subplots(figsize=(14,7.8));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.965,'听觉发育：不同层次共同变化，终点由测量问题决定',ha='center',fontsize=26)
for x,title,body in zip([.025,.275,.525,.775],['声音的到达','神经编码','选择与学习','交流与参与'],['外耳与中耳传递\n耳蜗转导','听神经与脑干\n皮层响应组织','检测、辨别与分组\n注意、记忆与经验','词句理解与表达\n互动、学习与活动']):
 ax.add_patch(FancyBboxPatch((x,.60),.2,.25,boxstyle='round,pad=.012',facecolor='#eef4f8',edgecolor=BLUE,lw=1.5))
 ax.text(x+.1,.79,title,ha='center',fontsize=23,color=BLUE);ax.text(x+.1,.69,body,ha='center',va='center',fontsize=18,linespacing=1.7)
 if x<.7:ax.annotate('',xy=(x+.24,.72),xytext=(x+.215,.72),arrowprops={'arrowstyle':'->','lw':1.5,'color':GRAY})
ax.text(.5,.50,'生理成熟、可用经验与任务条件均需要观察',ha='center',fontsize=24,color=GREEN)
for y,label,body in [(.37,'生理与年龄','结构、传递和响应随发育改变；成熟时间并不完全同步'),(.245,'经验与环境','可听输入、语言和互动；有声音不等于信息可用'),(.12,'测量与反应','刺激、任务、状态和响应方式；没有反应不等于没有检测')]:
 ax.add_patch(FancyBboxPatch((.035,y-.045),.93,.09,boxstyle='round,pad=.005',facecolor='#f6f7f8',edgecolor='#ccd3d9'))
 ax.text(.07,y,label,va='center',fontsize=21,color=GREEN);ax.text(.28,y,body,va='center',fontsize=19)
fig.subplots_adjust(left=.02,right=.98,bottom=.03,top=.98);save(fig,'01-development-framework',780)

# Artificial infant: born at 34 gestational weeks, assessed 12 weeks later, fitted at week 9 after birth.
birth,due,fitting,test=34,40,43,46
fig,ax=plt.subplots(figsize=(14,7.2))
for y,start,color,label in [(3,birth,BLUE,'实际年龄：12 周'),(2,due,ORANGE,'矫正年龄：6 周'),(1,fitting,GREEN,'设备使用时长：3 周')]:
 ax.plot([start,test],[y,y],color=color,lw=5);ax.scatter([start,test],[y,y],color=color,s=90)
 ax.text((start+test)/2,y+.18,label,ha='center',fontsize=21,color=color)
for x,label in [(birth,'出生\n孕 34 周'),(due,'预产期参考\n40 周'),(fitting,'假设开始用助听器\n出生后第 9 周'),(test,'同一次评估\n月经后年龄 46 周')]:
 ax.vlines(x,.4,3.6,color=GRAY,lw=1,ls=':');ax.text(x,.05,label,ha='center',va='top',fontsize=17,color=GRAY)
ax.set(xlim=(31.5,49.5),ylim=(-.65,3.95),yticks=[],xticks=[32,34,36,38,40,42,44,46,48],xlabel='月经后年龄 / 周 = 出生时孕周 + 出生后周数')
ax.spines['left'].set_visible(False);ax.set_title('同一个孩子、同一次评估，可以有不同的时间起点',fontsize=25,pad=22)
fig.subplots_adjust(left=.06,right=.97,top=.85,bottom=.23)
fig.text(.5,.055,'全部时间人为设定；矫正年龄用于相应发育比较，不用于自行延后筛查或诊断。',ha='center',fontsize=17,color=GRAY)
fig.text(.5,.02,'设备使用时长只记录时间，不等于经过验证的可听度、每日佩戴量或完整听觉经验。',ha='center',fontsize=16,color=GRAY)
save(fig,'02-age-clocks',720)

x=np.arange(1,9);uni=np.array([.02,.08,.16,.24,.24,.16,.08,.02]);bi=np.array([.04,.16,.24,.06,.06,.24,.16,.04])
fig,axs=plt.subplots(1,2,figsize=(14,7),sharex=True,sharey=True)
for ax,p,title,c in zip(axs,[uni,bi],['（a）单峰的接触分布','（b）双峰的接触分布'],[BLUE,ORANGE]):
 ax.bar(x,p*100,color=c,width=.7);ax.set(xlim=(.4,8.6),ylim=(0,29),xticks=x,xlabel='语音连续体的教学位置 / 无量纲')
 ax.set_title(title,fontsize=24,pad=20);ax.grid(axis='y',alpha=.15)
 ax.text(4.5,26.4,'概率合计 100%；平均位置 4.5',ha='center',fontsize=18,color=GRAY)
axs[0].set_ylabel('接触概率 / %')
fig.subplots_adjust(left=.09,right=.97,top=.84,bottom=.27,wspace=.19)
fig.text(.5,.105,'平均值和取值范围相同，频率分布仍然不同：研究应控制接触量并检验后续辨别。',ha='center',fontsize=18,color=GREEN)
fig.text(.5,.045,'依据分布学习问题独立绘制；概率人为设定，不是 Maye 等的刺激次数或儿童表现。',ha='center',fontsize=16,color=GRAY)
save(fig,'03-exposure-distributions',700)

rows=[{'label':'助听器：50 dB HL','early_months':3,'later_months':24,'estimate':-6.8,'lower':-10.8,'upper':-2.8},
{'label':'助听器：70 dB HL','early_months':3,'later_months':24,'estimate':-11.8,'lower':-18.7,'upper':-4.8},
{'label':'人工耳蜗组','early_months':6,'later_months':24,'estimate':-21.4,'lower':-33.8,'upper':-9.0}]
fig,ax=plt.subplots(figsize=(14,7.6));ax.axvline(0,color=GRAY,lw=1.2,ls='--')
for y,r,c in zip([2,1,0],rows,[BLUE,BLUE,ORANGE]):
 est,lo,hi=r['estimate'],r['lower'],r['upper'];ax.errorbar(est,y,xerr=[[est-lo],[hi-est]],fmt='D',color=c,lw=3,capsize=8,ms=9)
 ax.text(-40,y+.13,r['label'],ha='left',fontsize=20,color=c)
 ax.text(-40,y-.20,f"{r['later_months']} 月 − {r['early_months']} 月",ha='left',fontsize=17,color=GRAY)
 ax.text(3.5,y+.11,f'{est:g}',ha='left',fontsize=20,color=c)
 ax.text(3.5,y-.19,f'[{lo:g}, {hi:g}]',ha='left',fontsize=17,color=GRAY)
ax.set(xlim=(-41,15),ylim=(-.6,2.65),yticks=[],xlabel='5 岁综合语言评分的调整后组间差 / 分（较晚 − 较早）',xticks=[-30,-20,-10,0,10]);ax.spines['left'].set_visible(False)
ax.set_title('LOCHI：干预时间与后续语言结局的关系',fontsize=25,pad=24)
fig.subplots_adjust(left=.06,right=.98,top=.85,bottom=.25)
fig.text(.5,.13,'负值表示较晚组评分较低；横线为原研究报告的 95% 置信区间。',ha='center',fontsize=18,color=GREEN)
fig.text(.5,.075,'据 Ching 等（2017）原始摘要独立重绘；前瞻性队列的模型估计，不是随机延迟干预。',ha='center',fontsize=16,color=GRAY)
fig.text(.5,.025,'三行的听力状态、设备和早期时间点不同，不能据此比较助听器与人工耳蜗的优劣。',ha='center',fontsize=16,color=GRAY)
save(fig,'04-intervention-estimates',760)

assert test-birth==12 and test-due==6 and test-fitting==3
assert np.isclose(uni.sum(),1) and np.isclose(bi.sum(),1)
assert np.isclose(np.dot(x,uni),4.5) and np.isclose(np.dot(x,bi),4.5)
assert all(r['lower']<r['estimate']<r['upper']<0 for r in rows)
dprime=NormalDist().inv_cdf(.8)-NormalDist().inv_cdf(.2)
assert abs(dprime-1.683242467)<1e-8
report={'figures':4,'teaching_figures':[1,2,3],'published_estimates_redrawn':[4],'age_weeks':{'gestational_at_birth':birth,'postnatal':12,'postmenstrual':test,'reference_due':due,'corrected':6,'device_use':3},'distributions':{'positions':x.tolist(),'unimodal':uni.tolist(),'bimodal':bi.tolist(),'both_means':4.5},'published_estimates':rows,'estimate_source_doi':'10.1542/peds.2016-4274','checks_passed':True}
(DOC/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report['worked_examples']={'transition_probability':[18/20,5/20],'hit_rate':16/20,'false_alarm_rate':4/20,'dprime':dprime}
(DOC/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':4,'checks_passed':True}))
