"""Reproduce four teaching figures and numeric checks; no participant data.

Python + numpy/scipy/matplotlib. Run from repository root:
    python public/code/psychometric-function/demo.py
All intervals condition on gamma=.5, lambda=.02 and the fixed stimulus grid.
"""
from pathlib import Path
import json
import numpy as np
from scipy.special import expit, logit, gammaln
from scipy.optimize import minimize
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'public/figures/psychometric-function'
OUT.mkdir(parents=True,exist_ok=True)
available={f.name for f in font_manager.fontManager.ttflist}
plt.rcParams.update({'font.family':next((f for f in ['Microsoft YaHei','Noto Sans CJK SC','SimHei'] if f in available),'DejaVu Sans'),'font.size':12,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','axes.unicode_minus':False})
COLORS=['#20639b','#ba4b26','#30735b']
STYLES=['-','--','-.']
def pf(x,a=-6,b=1.5,g=.5,l=.02):return g+(1-g-l)*expit((np.asarray(x)-a)/b)
def threshold(q,a=-6,b=1.5,g=.5,l=.02):
    if not g<q<1-l:raise ValueError('target outside open asymptotic range')
    return a+b*logit((q-g)/(1-g-l))
def save(fig,name):
    svg=OUT/(name+'.svg')
    fig.savefig(svg,bbox_inches='tight',facecolor='white')
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(OUT/(name+'.png'),dpi=150,bbox_inches='tight',facecolor='white')
    plt.close(fig)
def axes():
    fig,ax=plt.subplots(1,2,figsize=(12,4.8));fig.subplots_adjust(wspace=.27,bottom=.18)
    return fig,ax
x=np.linspace(-16,6,500)
fig,ax=axes()
for a,c,ls in zip([-8,-6,-4],COLORS,STYLES):ax[0].plot(x,pf(x,a=a),color=c,ls=ls,label=f'α={a} dB SNR')
for b,c,ls in zip([.8,1.5,3],COLORS,STYLES):ax[1].plot(x,pf(x,b=b),color=c,ls=ls,label=f'β={b} dB')
for i,z in enumerate(ax):
    z.set(xlabel='信噪比（dB SNR）',ylabel='正确反应概率',ylim=(.45,1.01),title=['（a）改变位置参数','（b）改变尺度参数'][i]);z.axhline(.74,color='#777',ls=':',lw=1);z.legend();z.grid(alpha=.15)
save(fig,'01-location-scale')
fig,ax=axes()
for l,c,ls in zip([0,.02,.10],COLORS,STYLES):
    ax[0].plot(x,pf(x,l=l),color=c,ls=ls,label=f'λ={l:.2f}；α处={pf(-6,l=l):.2f}')
ax[0].axvline(-6,color='#777',ls=':');ax[0].axhline(.75,color='#777',ls='--',lw=1)
ax[0].set(xlabel='信噪比（dB SNR）',ylabel='正确反应概率',ylim=(.45,1.01),title='（a）上端失误改变原始正确率中点');ax[0].legend(fontsize=10)
q=np.linspace(.501,.979,300)
ax[1].plot(q*100,[threshold(v) for v in q],color=COLORS[0])
for target,offset in zip([.74,.75,.90],[(-90,24),(12,-28),(-80,22)]):
    t=threshold(target);ax[1].plot(target*100,t,'o',color=COLORS[1]);ax[1].annotate(f'{target*100:.0f}%：{t:.2f} dB',(target*100,t),xytext=offset,textcoords='offset points',fontsize=10,arrowprops={'arrowstyle':'-','color':'#555','lw':.8})
ax[1].set(xlabel='指定的原始正确率（%）',ylabel='对应阈值（dB SNR）',title='（b）同一曲线有不同目标阈值',xlim=(50,99),ylim=(-13,4))
save(fig,'02-target-thresholds')

levels=np.array([-12.,-9.,-6.,-3.,0.]); n=np.full(5,40)
rng=np.random.default_rng(20261106);k=rng.binomial(n,pf(levels))
def fit(counts):
    def loss(t):
        p=pf(levels,*t)
        return -np.sum(counts*np.log(p)+(n-counts)*np.log1p(-p))
    results=[minimize(loss,[a,b],method='L-BFGS-B',bounds=[(-24,12),(.25,12)]) for a,b in [(-6,1.5),(-9,3),(-3,.7)]]
    valid=[r for r in results if r.success and np.isfinite(r.fun)]
    if not valid: raise RuntimeError('optimization failed')
    best=min(valid,key=lambda r:r.fun)
    return best.x,best.fun
est,nll=fit(k)
B=400;boot=np.array([fit(rng.binomial(n,pf(levels,*est)))[0] for _ in range(B)])
tboot=np.array([threshold(.75,*t) for t in boot]);ci=np.quantile(tboot,[.025,.975])
curves=np.array([pf(x,*t) for t in boot]);band=np.quantile(curves,[.025,.975],axis=0)
fig,ax=axes()
ax[0].fill_between(x,band[0],band[1],alpha=.18,color=COLORS[0],label='逐点95% bootstrap分位带')
ax[0].plot(x,pf(x,*est),color=COLORS[0],label='二项最大似然拟合')
ax[0].scatter(levels,k/n,s=48,color=COLORS[1],zorder=4,label='每水平40次模拟反应')
ax[0].set(xlabel='信噪比（dB SNR）',ylabel='正确率／预测概率',ylim=(.45,1.01),title='（a）有限试次与模型曲线');ax[0].legend(fontsize=10)
ax[1].hist(tboot,bins=24,color=COLORS[0],alpha=.8)
for t in ci:ax[1].axvline(t,color=COLORS[1],ls='--')
ax[1].set(xlabel='75%正确率阈值（dB SNR）',ylabel='重采样次数',title='（b）固定设计下的参数bootstrap')
save(fig,'03-fit-bootstrap')
fig,ax=axes()
for a,c,ls in zip([-9,-3],COLORS,STYLES):ax[0].plot(x,pf(x,a=a),color=c,ls=ls,label=f'等权子条件：α={a} dB')
pool=.5*(pf(x,a=-9)+pf(x,a=-3))
ax[0].plot(x,pool,color=COLORS[2],lw=2.5,label='两条概率曲线的等权平均')
ax[1].plot(x,pf(x),color=COLORS[0],label='单一α=−6 dB，β=1.5 dB')
ax[1].plot(x,pool,color=COLORS[2],ls='--',label='位置变化后平均；β仍各为1.5 dB')
for i,z in enumerate(ax):z.set(xlabel='信噪比（dB SNR）',ylabel='正确反应概率',ylim=(.45,1.01),title=['（a）不同位置的两条曲线','（b）平均可表现得更平缓'][i]);z.legend(fontsize=9)
save(fig,'04-pooling')

# Verify inverse, derivative, asymptotes, binomial likelihood and mixture example.
targets=[.60,.74,.75,.90]
assert all(abs(pf(threshold(q))-q)<1e-12 for q in targets)
assert abs(pf(-6)-.74)<1e-12
assert abs(threshold(.75)-(-6+1.5*np.log(25/23)))<1e-12
derivative=(pf(-6+1e-5)-pf(-6-1e-5))/(2e-5)
assert abs(derivative-.48/(4*1.5))<1e-9
assert np.all(np.diff(pf(x))>0)
assert np.allclose(pf(np.array([-1e6,1e6])),[.5,.98])
logchoose=gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1)
p=pf(levels,*est); sat=np.clip(k/n,1e-12,1-1e-12)
deviance=2*np.sum(k*np.log(sat/p)+(n-k)*np.log((1-sat)/(1-p)))
report={'data_kind':'Synthetic Bernoulli responses; no human data','seed':20261106,'gamma':.5,'lambda':.02,'generating_alpha':-6,'generating_beta':1.5,'levels':levels.tolist(),'trials':n.tolist(),'correct':k.tolist(),'fitted_alpha':float(est[0]),'fitted_beta':float(est[1]),'threshold_75':threshold(.75,*est),'threshold_75_percentile_ci':ci.tolist(),'bootstrap_replicates':B,'bootstrap_boundary_fits':int(np.sum(np.any(np.isclose(boot,[-24,.25])|np.isclose(boot,[12,12]),axis=1))),'negative_log_likelihood_without_binomial_constants':float(nll),'log_likelihood_with_constants':float(-nll+np.sum(logchoose)),'deviance':float(deviance),'analytic_examples':{'threshold_74':threshold(.74),'threshold_75':threshold(.75),'threshold_90':threshold(.9),'slope_at_alpha_per_dB':float(derivative),'lapse_event_fraction_2afc':.02/(1-.5),'mixture_slope_at_minus6':float(.5*(.48/1.5)*(expit(2)*(1-expit(2))+expit(-2)*(1-expit(-2))))},'checks':'inverse, derivative, monotonicity, asymptotes and explicit binomial likelihood pass','versions':{'numpy':np.__version__}}
(OUT/'numerical-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
