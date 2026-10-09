"""Reproducible SDT teaching figures; analytic models, not listener data."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from scipy.stats import norm

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'public/figures/signal-detection-theory'
OUT.mkdir(parents=True,exist_ok=True)
FONT = FontProperties(fname='C:/Windows/Fonts/msyh.ttc').get_name()
plt.rcParams.update({'font.family':FONT,'font.size':12,'axes.spines.top':False,
                     'axes.spines.right':False,'svg.fonttype':'none','axes.unicode_minus':False})
BLUE, ORANGE, GREEN = '#356b91','#bf703a','#438277'
manifest = []

def save(fig,name,parameters):
    fig.savefig(OUT/(name+'.svg'),bbox_inches='tight')
    fig.savefig(OUT/(name+'.png'),dpi=160,bbox_inches='tight')
    plt.close(fig)
    manifest.append({'name':name,'files':[name+'.svg',name+'.png'],
                     'parameters':parameters,'data_type':'original analytic teaching model; no measured human data',
                     'creator':'n³ Hearingpedia, AI-assisted calculation','license':'CC BY 4.0'})

def rates(mu,k,sigma=1):
    f=norm.sf(k);h=norm.sf((k-mu)/sigma)
    dp=norm.ppf(h)-norm.ppf(f);c=-(norm.ppf(h)+norm.ppf(f))/2
    return {'criterion_k':float(k),'hit_rate':float(h),'false_alarm_rate':float(f),
            'd_prime':float(dp),'c':float(c)}

x=np.linspace(-3.5,5.5,1001)
fig,axs=plt.subplots(1,2,figsize=(14,5.7),layout='constrained')
points=[]
for ax,k,label in zip(axs,[.2,1.2],['（a）较宽松的报告标准','（b）较保守的报告标准']):
    q=rates(1.5,k);points.append(q)
    ax.plot(x,norm.pdf(x),color=BLUE,label='无目标 N(0, 1)')
    ax.plot(x,norm.pdf(x-1.5),'--',color=ORANGE,label='有目标 N(1.5, 1)')
    ax.fill_between(x,0,norm.pdf(x),where=x>k,color=BLUE,alpha=.18)
    ax.fill_between(x,0,norm.pdf(x-1.5),where=x>k,color=ORANGE,alpha=.18)
    ax.axvline(k,color='#333333',linestyle=':',label=f'判据 k={k:.1f}')
    ax.set(title=label,xlabel='内部证据 x / 共同标准差单位',ylabel='概率密度',xlim=(-3.5,5.5),ylim=(0,.57))
    ax.text(.03,.96,f"H={q['hit_rate']:.3f}，F={q['false_alarm_rate']:.3f}\nd′=1.500，c={q['c']:.2f}",transform=ax.transAxes,va='top')
    ax.legend(loc='upper right',fontsize=10)
save(fig,'01-evidence-and-criterion',{'noise_mean':0,'signal_mean':1.5,'common_sd':1,'points':points,'shading':'evidence above upper criterion for each distribution'})

k=np.linspace(-6,8,1401)
fig,ax=plt.subplots(figsize=(10,7),layout='constrained')
for d,color,style in zip([.75,1.5,2.25],[BLUE,ORANGE,GREEN],['-','--','-.']):
    ax.plot(norm.sf(k),norm.sf(k-d),color=color,linestyle=style,label=f'd′={d:.2f}')
for q,m in zip(points,['o','s']):
    ax.plot(q['false_alarm_rate'],q['hit_rate'],m,color=ORANGE,ms=9)
    ax.annotate(f"k={q['criterion_k']:.1f}",(q['false_alarm_rate'],q['hit_rate']),xytext=(8,-22),textcoords='offset points')
ax.plot([0,1],[0,1],':',color='#888888',label='d′=0 参照')
ax.set(xlim=(0,1),ylim=(0,1),xlabel='虚报率 F',ylabel='命中率 H',title='同一条 ROC 上移动：改变判据；曲线之间比较：改变可分离程度')
ax.set_aspect('equal');ax.legend(loc='lower right');ax.grid(alpha=.15)
save(fig,'02-roc',{'equal_variance_gaussian':True,'d_prime_values':[.75,1.5,2.25],'points':points})

d=np.linspace(0,3.5,401)
pc_ifc=norm.cdf(d/np.sqrt(2));pc_yn=norm.cdf(d/2)
dp75_ifc=float(np.sqrt(2)*norm.ppf(.75));dp75_yn=float(2*norm.ppf(.75))
fig,axs=plt.subplots(1,2,figsize=(14,5.8),layout='constrained')
y=np.linspace(-5,6,801)
axs[0].plot(y,norm.pdf(y,loc=1.5,scale=np.sqrt(2)),color=GREEN)
axs[0].fill_between(y,0,norm.pdf(y,loc=1.5,scale=np.sqrt(2)),where=y>0,color=GREEN,alpha=.23)
axs[0].axvline(0,linestyle=':',color='#444444')
axs[0].set(title='（a）二时段比较：有目标证据 − 无目标证据',xlabel='证据差 D / 单时段标准差单位',ylabel='概率密度',ylim=(0,.38))
axs[0].text(.03,.95,f'D ~ N(1.5, 2)\nP(D>0)={norm.cdf(1.5/np.sqrt(2)):.3f}',transform=axs[0].transAxes,va='top')
axs[1].plot(d,pc_ifc,color=GREEN,label='2IFC：独立、无时段偏向')
axs[1].plot(d,pc_yn,'--',color=BLUE,label='是／否：等先验、对称代价、居中判据')
axs[1].axhline(.75,linestyle=':',color='#888888')
for v,color in [(dp75_ifc,GREEN),(dp75_yn,BLUE)]:
    axs[1].plot(v,.75,'o',color=color)
    axs[1].annotate(f'd′={v:.3f}',(v,.75),xytext=(2,14 if color==GREEN else -24),textcoords='offset points',color=color)
axs[1].set(title='（b）同样 75% 正确率，不同任务的换算不同',xlabel='单时段分布可分离程度 d′',ylabel='正确率',xlim=(0,3.5),ylim=(.48,1.02))
axs[1].legend(loc='lower right',fontsize=10);axs[1].grid(alpha=.15)
save(fig,'03-task-conversion',{'single_interval_sd':1,'difference_variance':2,'example_d_prime':1.5,'pc75_d_prime_2ifc':dp75_ifc,'pc75_d_prime_yes_no':dp75_yn,'assumptions':'independent equal-variance normal evidence; no interval bias; yes/no equal priors and symmetric costs with midpoint criterion'})

mu,sigma=1.5,1.4
fig,axs=plt.subplots(1,2,figsize=(14,5.8),layout='constrained')
zF=np.linspace(-3,3,301)
axs[0].plot(zF,1.5+zF,'--',color=BLUE,label='σS=1：斜率 1')
axs[0].plot(zF,mu/sigma+zF/sigma,color=ORANGE,label='σS=1.4：斜率 1/1.4')
axs[0].set(title='（a）zROC：斜率等于无目标与有目标的标准差比',xlabel='z(F)',ylabel='z(H)',xlim=(-3,3),ylim=(-2.5,4.8))
axs[0].legend(loc='upper left',fontsize=10);axs[0].grid(alpha=.15)
ks=np.linspace(-1,3,301)
axs[1].plot(ks,mu/sigma+ks*(1-1/sigma),color=ORANGE,label='σS=1.4：常规 d′ 随 k 变化')
axs[1].axhline(1.5,linestyle='--',color=BLUE,label='σS=1：d′ 保持 1.5')
unequal_points=[rates(mu,v,sigma) for v in [-.5,.75,2]]
for q in unequal_points:
    axs[1].plot(q['criterion_k'],q['d_prime'],'o',color=ORANGE)
    axs[1].annotate(f"{q['d_prime']:.3f}",(q['criterion_k'],q['d_prime']),xytext=(6,-18),textcoords='offset points')
axs[1].set(title='（b）同一组不等方差分布，不同判据给出不同 d′',xlabel='判据 k / 无目标标准差单位',ylabel='z(H) − z(F)',xlim=(-1,3),ylim=(.6,2.1))
axs[1].legend(loc='upper left',fontsize=10);axs[1].grid(alpha=.15)
save(fig,'04-unequal-variance',{'noise_mean':0,'noise_sd':1,'signal_mean':mu,'signal_sd':sigma,'upper_criterion_rule':True,'points':unequal_points,'zroc_slope':1/sigma,'da':mu/np.sqrt((1+sigma**2)/2)})

# Finite-count worked example; not simulated or measured observations.
counts={'A':{'hits':181,'misses':19,'false_alarms':84,'correct_rejections':116},
        'B':{'hits':124,'misses':76,'false_alarms':23,'correct_rejections':177},
        'C':{'hits':166,'misses':34,'false_alarms':23,'correct_rejections':177}}
analysis={}
for name,row in counts.items():
    ns=row['hits']+row['misses'];nn=row['false_alarms']+row['correct_rejections']
    h=row['hits']/ns;f=row['false_alarms']/nn
    hc=(row['hits']+.5)/(ns+1);fc=(row['false_alarms']+.5)/(nn+1)
    analysis[name]={**row,'signal_trials':ns,'noise_trials':nn,'H':h,'F':f,
                    'd_prime_uncorrected':float(norm.ppf(h)-norm.ppf(f)),
                    'c_uncorrected':float(-(norm.ppf(h)+norm.ppf(f))/2),
                    'correct_fraction':(row['hits']+row['correct_rejections'])/(ns+nn),
                    'd_prime_loglinear':float(norm.ppf(hc)-norm.ppf(fc))}
assert all(abs(q['d_prime']-1.5)<1e-12 for q in points)
assert abs(dp75_ifc-.9538725524)<1e-9
assert abs(dp75_yn-1.3489795004)<1e-9
assert abs(analysis['A']['d_prime_uncorrected']-analysis['B']['d_prime_uncorrected'])<.03
assert analysis['C']['d_prime_uncorrected']>analysis['B']['d_prime_uncorrected']+.5
assert norm.sf(1.2)<norm.sf(.2)
report={'date':'2026-10-09','example_type':'explicitly constructed teaching counts, not experimental data',
        'figure_generation':'passed','assertions':'analytic d-prime recovery, task conversion, worked example relationships',
        'counts':analysis,'equal_variance_points':points,'unequal_variance_points':unequal_points,
        'normalization':'noise mean zero and noise standard deviation one; d-prime has no physical unit',
        'software':{'numpy':np.__version__,'scipy':__import__('scipy').__version__,'matplotlib':matplotlib.__version__},
        'figures':manifest}
(OUT/'manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'generated_figures':len(manifest),'counts':analysis,'checks':'passed'},ensure_ascii=False))
