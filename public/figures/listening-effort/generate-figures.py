from pathlib import Path
import numpy as np,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).parent
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.unicode_minus':False,'svg.fonttype':'path','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':150})
C=['#276a8c','#b75c3c','#59785b'];reports={}
def save(fig,name):
 fig.savefig(ROOT/(name+'.svg'),bbox_inches='tight');fig.savefig(ROOT/(name+'.png'),bbox_inches='tight');plt.close(fig)
def clean(ax):ax.grid(axis='y',alpha=.17);ax.set_axisbelow(True)
fig,axs=plt.subplots(1,2,figsize=(9.2,4.6),layout='constrained')
axs[0].bar(['条件 A','条件 B'],[90,90],color=C[:2],width=.5);axs[0].set(ylim=(0,105),ylabel='识别正确率 / %',title='A  相同的任务成绩')
axs[1].bar(['条件 A','条件 B'],[3,7],color=C[:2],width=.5);axs[1].set(ylim=(0,10),ylabel='主观努力评分（0—10）',title='B  不同的主观体验')
for ax,vals in zip(axs,[[90,90],[3,7]]):
 for i,v in enumerate(vals):ax.text(i,v+.02*ax.get_ylim()[1],str(v),ha='center')
 clean(ax)
fig.suptitle('说明性数据：成绩相同，努力可以不同',fontsize=13);save(fig,'01-performance-effort')
reports['performance']={'illustrative_not_observed':True,'accuracy_percent':[90,90],'subjective_effort_0_10':[3,7]}
x=np.linspace(0,1,401);d=.15+.8*x;e=.08+1.25*x*np.exp(-((x-.42)/.43)**2)
fig,ax=plt.subplots(figsize=(9.2,4.7),layout='constrained');ax.plot(x,d,'--',color='#6f7980',label='外部任务要求（示意）');ax.plot(x,e,color=C[0],lw=2.4,label='实际投入的一个可能模式')
ax.axvspan(.77,1,color='#edf0f2');ax.text(.87,.91,'可能减少投入',ha='center',fontsize=10);ax.set(xlim=(0,1),ylim=(0,1.08),xticks=[.05,.5,.95],xticklabels=['容易','较难但可完成','极难'],yticks=[],xlabel='任务难度逐渐增加',ylabel='示意相对水平（无量纲）',title='任务要求与实际投入并不等同');ax.legend(loc='upper left',fontsize=10);save(fig,'02-demand-engagement')
reports['demand']={'schematic_not_universal':True,'peak_difficulty':float(x[np.argmax(e)]),'not_FUEL_fitted_equation':True}
fig,axs=plt.subplots(1,2,figsize=(9.2,4.8),layout='constrained')
axs[0].bar(['单独视觉任务','听言语＋视觉任务'],[400,480],color=[C[2],C[0]],width=.5);axs[0].set(ylim=(0,560),ylabel='正确反应的反应时间 / ms',title='A  次任务的反应时间')
for i,v in enumerate([400,480]):axs[0].text(i,v+10,str(v),ha='center')
axs[1].bar(['单独言语任务','言语＋视觉任务'],[90,90],color=[C[2],C[0]],width=.5);axs[1].set(ylim=(0,105),ylabel='言语识别正确率 / %',title='B  同时检查主任务表现')
for i,v in enumerate([90,90]):axs[1].text(i,v+2,str(v),ha='center')
for ax in axs:clean(ax);ax.tick_params(axis='x',labelsize=9)
fig.suptitle('说明性数据：次任务反应时间成本 = (480 − 400) / 400 = 20%',fontsize=12);save(fig,'03-dual-task')
reports['dual_task']={'illustrative_not_observed':True,'baseline_rt_ms':400,'dual_rt_ms':480,'rt_cost_percent':20,'speech_accuracy_percent':[90,90]}
t=np.arange(-1,8,.01)
def kernel(t,amp,shift):
 z=np.maximum(t-shift,0);return amp*(z/1.5)**3*np.exp(3-2*z)
a=kernel(t,.18,0);b=kernel(t,.32,0)+kernel(t,.09,2.8);baseline=3.5
fig,axs=plt.subplots(2,1,figsize=(9.2,6.3),layout='constrained')
for ax,offset in [(axs[0],baseline),(axs[1],0)]:
 ax.plot(t,a+offset,color=C[0],lw=2,label='条件 A');ax.plot(t,b+offset,color=C[1],lw=2,label='条件 B');ax.axvspan(-.8,-.1,color='#e7ecee');ax.axvspan(0,2.5,color='#eff5f7');ax.axvline(2.5,color='#808c94',ls=':',lw=1);ax.set(xlim=(-1,8));clean(ax)
axs[0].set(title='A  合成的原始瞳孔直径',ylabel='瞳孔直径 / mm',ylim=(3.48,3.96));axs[0].legend(fontsize=10,loc='lower right');axs[0].text(-.45,3.92,'基线',ha='center',fontsize=9);axs[0].text(1.25,3.92,'声音呈现',ha='center',fontsize=9);axs[0].text(5.2,3.92,'声音结束后仍可存在响应',ha='center',fontsize=9)
axs[1].set(title='B  减去各试次基线后的变化量',ylabel='相对基线的直径变化 / mm',xlabel='相对声音开始的时间 / s');axs[1].axhline(0,color='#8c969c',ls=':',lw=1);save(fig,'04-pupil-time-course')
reports['pupil']={'synthetic_not_observed':True,'baseline_mm':baseline,'sound_interval_s':[0,2.5],'baseline_interval_s':[-.8,-.1],'min_delta_mm':float(min(a.min(),b.min())),'not_neural_latency':True}
x=np.linspace(-8,8,401);pa=100/(1+np.exp(-(x+1.5)/2));pb=100/(1+np.exp(-(x-1)/2));target=85;xa=2*np.log(target/(100-target))-1.5;xb=2*np.log(target/(100-target))+1
fig,axs=plt.subplots(1,2,figsize=(10,4.8),layout='constrained')
for ax in axs:
 ax.plot(x,pa,color=C[0],lw=2,label='处理 A');ax.plot(x,pb,color=C[1],lw=2,label='处理 B');ax.set(xlim=(-8,8),ylim=(0,105),xlabel='输入信噪比 / dB',ylabel='言语识别正确率 / %');clean(ax)
axs[0].axvline(0,color='#747e85',ls=':');axs[0].scatter([0,0],[np.interp(0,x,pa),np.interp(0,x,pb)],color=C[:2],zorder=3);axs[0].set_title('A  相同环境：固定输入信噪比');axs[0].legend(loc='lower right',fontsize=10)
axs[1].axhline(target,color='#747e85',ls=':');axs[1].scatter([xa,xb],[target,target],color=C[:2],zorder=3)
for v,c in [(xa,C[0]),(xb,C[1])]:axs[1].plot([v,v],[0,target],ls=':',color=c,lw=1)
axs[1].text(-7,88,'匹配 85% 正确率',fontsize=10);axs[1].set_title('B  相同性能：分别调整输入信噪比');save(fig,'05-comparison-design')
reports['design']={'synthetic_psychometric_curves':True,'accuracy_target_percent':target,'snr_A_dB':float(xa),'snr_B_dB':float(xb),'matched_accuracy_check':[float(100/(1+np.exp(-(xa+1.5)/2))),float(100/(1+np.exp(-(xb-1)/2)))]}
assert all(abs(v-85)<1e-10 for v in reports['design']['matched_accuracy_check'])
(ROOT/'figure-verification.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf8');print('Generated 5 SVG/PNG figures; illustrative data labeled; numerical checks passed.')
