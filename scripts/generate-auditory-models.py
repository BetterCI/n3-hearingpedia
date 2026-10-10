"""Original teaching figures; no experimental or patient data."""
from pathlib import Path
import json,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/auditory-computational-models'
DOC=ROOT/'docs/research/auditory-computational-models-2026-10-10'
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':18,'svg.fonttype':'path','axes.spines.top':False,'axes.spines.right':False,'axes.unicode_minus':False})
BLUE,ORANGE,GREEN,GRAY='#286a9b','#b65d2e','#327965','#687481'
def save(fig,name,h):
 fig.savefig(OUT/(name+'.png'),dpi=100,facecolor='white')
 fig.savefig(OUT/(name+'.svg'),facecolor='white')
 p=OUT/(name+'.svg');s=p.read_text(encoding='utf-8')
 p.write_text(re.sub(r'width="[^"]+" height="[^"]+"',f'width="1400" height="{h}"',s,count=1),encoding='utf-8')
 plt.close(fig)

fig,ax=plt.subplots(figsize=(14,7.6));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.965,'听觉计算模型：从指定输入预测指定对象',ha='center',fontsize=27)
blocks=[(.025,'输入与条件','声压、左右耳信号\n人群、任务与状态'),(.28,'内部处理','滤波、非线性、适应\n神经或学习表征'),(.535,'读出与预测','响应、判别变量\n概率、阈值或指标'),(.79,'独立证据','行为、神经或声学数据\n新材料与新条件')]
for x,title,body in blocks:
 ax.add_patch(FancyBboxPatch((x,.61),.18,.25,boxstyle='round,pad=.009',facecolor='#eef4f8',edgecolor=BLUE,lw=1.5))
 ax.text(x+.09,.795,title,ha='center',fontsize=22,color=BLUE)
 ax.text(x+.09,.70,body,ha='center',va='center',fontsize=16,linespacing=1.8)
 if x<.75:ax.annotate('',xy=(x+.24,.73),xytext=(x+.195,.73),arrowprops={'arrowstyle':'->','color':GRAY,'lw':1.5})
ax.text(.5,.50,'内部输出的单位，不会因模型名称自动变成感知结论',ha='center',fontsize=23,color=GREEN)
for y,l,b in [(.36,'生理目标','基底膜位移、受体电位、放电率或群体电位：逐层比较'),(.235,'功能目标','检测、辨别与言语表现：需要任务读出、噪声和评分规则'),(.11,'学习目标','任务标签、神经记录或教师模型：训练来源决定验证对象')]:
 ax.add_patch(FancyBboxPatch((.035,y-.045),.93,.09,boxstyle='round,pad=.005',facecolor='#f6f7f8',edgecolor='#ccd3d9'))
 ax.text(.065,y,l,va='center',fontsize=20,color=GREEN);ax.text(.255,y,b,va='center',fontsize=17)
fig.subplots_adjust(left=.02,right=.98,bottom=.03,top=.98);save(fig,'01-model-framework',760)

levels=np.linspace(0,60,301);x=10**(levels/20);alpha=.3
fig,axs=plt.subplots(1,2,figsize=(14,6.8))
for exponent,color,label,style in [(1,BLUE,'线性 α = 1','-'),(alpha,ORANGE,'压缩 α = 0.3','--')]:
 y=x**exponent
 axs[0].plot(levels,20*np.log10(y),color=color,lw=3,label=label,ls=style)
 axs[1].plot(levels,20*np.log10(y/x),color=color,lw=3,label=label,ls=style)
axs[0].set(title='（a）相对输出增长',xlabel='输入相对参考的增量 / dB',ylabel='输出相对参考的增量 / dB',xlim=(0,60),ylim=(-3,65))
axs[1].set(title='（b）相对增益',xlabel='输入相对参考的增量 / dB',ylabel='相对增益 / dB',xlim=(0,60),ylim=(-45,5))
for a in axs:a.grid(alpha=.13);a.legend(fontsize=16)
axs[0].scatter([20,20],[20,6],color=[BLUE,ORANGE],s=70)
axs[0].text(36,23,'输入 +20 dB\n压缩输出 +6 dB',fontsize=17,color=ORANGE)
fig.text(.5,.08,'教学幂律 y = x^α；x、y 为相对参考的正幅度，无量纲',ha='center',color=GREEN,fontsize=19)
fig.text(.5,.025,'没有滤波、适应或生理拟合；曲线不是听阈、响度或设备处方。',ha='center',color=GRAY,fontsize=17)
fig.subplots_adjust(left=.085,right=.97,bottom=.23,top=.89,wspace=.28);save(fig,'02-compression',680)

xx=np.linspace(0,2.5,400);params=[(1,0),(1.5,.5),(2,1)]
fig,axs=plt.subplots(1,2,figsize=(14,7))
for (aa,bb),color,style in zip(params,[BLUE,ORANGE,GREEN],['-','--',':']):
 axs[0].plot(xx,aa*xx/(1+bb*xx),color=color,lw=3,ls=style,label=f'a = {aa:g}，b = {bb:g}')
axs[0].scatter([1],[1],color='black',s=85,zorder=5);axs[0].axvline(1,color=GRAY,ls=':',lw=1)
axs[0].set(title='（a）同一个约束，多条预测',xlabel='教学输入 x / 无量纲',ylabel='教学输出 y / 无量纲',xlim=(0,2.5),ylim=(0,2.65))
axs[0].legend(loc='upper left',fontsize=16);axs[0].grid(alpha=.13)
bb=np.linspace(0,1.5,100);axs[1].plot(bb,1+bb,color=GRAY,lw=2)
for (aa,b),c in zip(params,[BLUE,ORANGE,GREEN]):axs[1].scatter([b],[aa],color=c,s=100,zorder=4)
axs[1].set(title='（b）满足 y(1) = 1 的参数',xlabel='参数 b / 无量纲',ylabel='参数 a / 无量纲',xlim=(-.05,1.55),ylim=(.85,2.6))
axs[1].text(.8,1.28,'整条线 a = 1 + b\n都满足同一输入点',fontsize=20,color=GRAY);axs[1].grid(alpha=.13)
fig.text(.5,.075,'增加未参与拟合的输入点，可检验候选参数的不同预测。',ha='center',color=GREEN,fontsize=20)
fig.text(.5,.025,'人为函数 y = ax / (1 + bx)；不是耳蜗机制、患者参数或置信区间。',ha='center',color=GRAY,fontsize=17)
fig.subplots_adjust(left=.08,right=.97,bottom=.23,top=.89,wspace=.27);save(fig,'03-identifiability',700)

obs=np.array([10,30,50,70,90],dtype=float);pa=obs.copy();pb=.5*obs+25
fig,axs=plt.subplots(1,2,figsize=(14,6.8))
metrics=[]
for ax,pred,c,title in zip(axs,[pa,pb],[BLUE,ORANGE],['（a）预测 A：数值一致','（b）预测 B：范围压缩']):
 r=float(np.corrcoef(obs,pred)[0,1]);rmse=float(np.sqrt(np.mean((obs-pred)**2)));metrics.append({'correlation':r,'rmse_percentage_points':rmse})
 ax.plot([0,100],[0,100],ls='--',color=GRAY,lw=1.5);ax.scatter(obs,pred,s=100,color=c)
 ax.set(title=title,xlabel='教学目标值 / %',ylabel='预测值 / %',xlim=(0,100),ylim=(0,100),aspect='equal');ax.grid(alpha=.13)
 ax.text(.045,.94,f'r = {r:.2f}\nRMSE = {rmse:.2f} 百分点',transform=ax.transAxes,va='top',fontsize=18,color=c)
fig.text(.5,.07,'相关描述共同变化；数值误差与校准需要另行检验。',ha='center',color=GREEN,fontsize=20)
fig.text(.5,.022,'五个人为设定的目标值；不是听者实验、模型排行榜或临床预测。',ha='center',color=GRAY,fontsize=17)
fig.subplots_adjust(left=.07,right=.97,bottom=.25,top=.89,wspace=.25);save(fig,'04-validation-metrics',680)

assert np.isclose(20*np.log10(10**alpha),6)
assert all(np.isclose(a/(1+b),1) for a,b in params)
assert all(np.isclose(m['correlation'],1) for m in metrics)
assert np.isclose(metrics[1]['rmse_percentage_points'],np.sqrt(200))
report={'data_nature':'Original synthetic teaching functions; no empirical dataset','figures':4,'compression':{'alpha':alpha,'input_20dB_amplitude_ratio':10,'output_ratio':10**alpha,'output_increment_dB':6},'identifiability':{'function':'a*x/(1+b*x)','constraint':'y(1)=1','parameter_sets':params},'calibration':{'targets_percent':obs.tolist(),'prediction_A_percent':pa.tolist(),'prediction_B_percent':pb.tolist(),'metrics':metrics},'checks_passed':True}
(DOC/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':4,'checks_passed':True}))
