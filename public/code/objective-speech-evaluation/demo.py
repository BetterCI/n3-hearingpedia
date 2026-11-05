"""Four original teaching figures, not scores from a speech evaluation package.

Run: python public/code/objective-speech-evaluation/demo.py
Dependencies: NumPy, Matplotlib. Font: Microsoft YaHei (or install a CJK font).
No audio data, model weights, randomness, or human observations are used.
"""
from pathlib import Path
import json, platform
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT/'public/figures/objective-speech-evaluation'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei', 'font.size':13,
                     'axes.spines.top':False, 'axes.spines.right':False,
                     'axes.unicode_minus':False,'svg.fonttype':'none',
                     'svg.hashsalt':'objective-speech-evaluation-v1'})
BLUE, ORANGE, GREEN, GRAY = '#28689b', '#bd6430', '#238579', '#657482'

def save(fig, name):
    fig.savefig(OUT/(name+'.svg'), metadata={'Date':None})
    fig.savefig(OUT/(name+'.png'), dpi=160)
    p=OUT/(name+'.svg')
    p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)

fig,ax=plt.subplots(figsize=(12,5.2)); ax.set(xlim=(0,12),ylim=(0,5.2));ax.axis('off')
boxes=[(0.2,'1 目标与听者','识别正确率？\n音质？努力？',BLUE),
       (3.2,'2 输入与参考','内容、声级、对齐\n语言、听力与失真',GREEN),
       (6.2,'3 模型与输出','版本、权重、前处理\n指数／预测分／dB',ORANGE),
       (9.2,'4 独立验证','听辨、评分、误差\n分层结果与适用边界',BLUE)]
for x,title,body,color in boxes:
    ax.add_patch(FancyBboxPatch((x,1.6),2.6,2.4,boxstyle='round,pad=0.08',ec=color,fc='white',lw=1.7))
    ax.text(x+1.3,3.45,title,ha='center',weight='bold',color=color,fontsize=14)
    ax.text(x+1.3,2.55,body,ha='center',va='center',linespacing=1.8,fontsize=13)
    if x<9: ax.annotate('',xy=(x+2.94,2.8),xytext=(x+2.7,2.8),arrowprops={'arrowstyle':'->','color':GRAY,'lw':1.6})
ax.text(6,0.65,'同一分数，只有在目标、条件与验证相容时，才有明确解释。',ha='center',color=GRAY,fontsize=14)
fig.subplots_adjust(left=.02,right=.98,bottom=.03,top=.97)
save(fig,'01-evaluation-chain')

x=np.array([1.,2.,4.,3.,1.,5.,2.,4.])
signals=[x,.2*x,x+2,np.roll(x,2)]
labels=['原序列','0.2倍缩放','增加常量2','循环错位2点']
colors=[BLUE,ORANGE,GREEN,GRAY]; styles=['-','--','-.',':']
corr=np.array([np.corrcoef(x,y)[0,1] for y in signals])
assert np.allclose(corr[:3],1)
fig,axes=plt.subplots(1,2,figsize=(12,5.2),gridspec_kw={'width_ratios':[1.2,1]})
for y,l,c,ls in zip(signals,labels,colors,styles):axes[0].plot(np.arange(1,9),y,label=l,color=c,ls=ls,marker='o',ms=4)
axes[0].set(xlabel='样点序号',ylabel='非负包络值（任意单位）',title='（a）共用幅度坐标')
axes[0].legend(fontsize=11,ncol=2,loc='upper left');axes[0].set_ylim(0,9)
axes[1].barh(labels,corr,color=colors,height=.55)
axes[1].set(xlim=(-1.1,1.25),xlabel='普通Pearson相关（无量纲）',title='（b）只检验去均值后的形状')
axes[1].axvline(0,color=GRAY,lw=.7)
for i,v in enumerate(corr):axes[1].text(v+(.04 if v>=0 else -.04),i,f'{v:.3f}',va='center',ha='left' if v>=0 else 'right',fontsize=11)
fig.tight_layout(pad=2);save(fig,'02-envelope-correlation')

fs=16000;n=np.arange(fs)
s=np.sin(2*np.pi*500*n/fs);noise=np.sin(2*np.pi*900*n/fs)
s/=np.linalg.norm(s);noise/=np.linalg.norm(noise)
assert abs(s.mean())<1e-12 and abs(noise.mean())<1e-12
assert abs(s@noise)<1e-12
def sisdr(target, estimate):
    # Defined here only for nonzero target, nonzero projection and residual.
    a=estimate@target/(target@target);res=estimate-a*target
    assert abs(target@res)<1e-10
    return 10*np.log10(np.sum((a*target)**2)/np.sum(res**2))
gains=np.linspace(.05,2,100)
ratio=np.array([10*np.log10((s@s)/np.sum((g*(s+noise)-s)**2)) for g in gains])
si=np.array([sisdr(s,g*(s+noise)) for g in gains])
analytic=10*np.log10(1/((gains-1)**2+gains**2))
assert np.allclose(ratio,analytic,atol=1e-11)
assert np.allclose(si,0,atol=1e-11)
fig,ax=plt.subplots(figsize=(12,5.2))
ax.plot(gains,ratio,color=BLUE,lw=2.5,label='固定参考误差比')
ax.plot(gains,si,color=ORANGE,lw=2.5,ls='--',label='SI-SDR')
ax.scatter([.5,1],[10*np.log10(2),0],color=BLUE,zorder=4)
ax.annotate('g = 0.5：3.01 dB',(.5,10*np.log10(2)),xytext=(.68,3.7),arrowprops={'arrowstyle':'->','color':GRAY})
ax.set(xlabel='整体增益 g（线性幅度乘数）',ylabel='评价值（dB）',xlim=(.05,2),ylim=(-8,5))
ax.legend(loc='lower left');ax.grid(alpha=.17);fig.tight_layout(pad=2)
save(fig,'03-gain-metrics')

obs=np.array([1.,1.8,2.6,3.4,4.2]);pred=obs+.5
obs_group=np.array([1.,1.5,2.,4.,4.5,5.]);pred_group=np.array([2.,1.5,1.,5.,4.5,4.])
rmse=np.sqrt(np.mean((pred-obs)**2));global_r=np.corrcoef(obs_group,pred_group)[0,1]
within=[np.corrcoef(obs_group[i:i+3],pred_group[i:i+3])[0,1] for i in [0,3]]
assert np.isclose(rmse,.5) and np.isclose(np.corrcoef(obs,pred)[0,1],1)
assert global_r>0 and np.allclose(within,-1)
fig,axes=plt.subplots(1,2,figsize=(12,5.2))
axes[0].scatter(obs,pred,c=BLUE,s=55,label='预测 = 观察 + 0.5')
axes[0].set_title('（a）r = 1，RMSE = 0.5')
for start,c,marker,label in [(0,BLUE,'o','假想条件 A'),(3,ORANGE,'s','假想条件 B')]:
    axes[1].plot(obs_group[start:start+3],pred_group[start:start+3],color=c,marker=marker,label=label,lw=1)
axes[1].set_title(f'（b）总体 r = {global_r:.3f}；组内 r = −1')
for ax in axes:
    ax.plot([.5,5.5],[.5,5.5],ls='--',color=GRAY,lw=1,label='预测 = 观察')
    ax.set(xlim=(.5,5.5),ylim=(.5,5.5),xlabel='观察评分（教学设定）',ylabel='预测评分（教学设定）')
    ax.legend(fontsize=10,loc='upper left');ax.grid(alpha=.15)
fig.tight_layout(pad=2);save(fig,'04-validation')

checks={'nature':'Original deterministic teaching calculations; no human data and no execution of STOI/HASPI/PESQ/neural metrics',
 'python':platform.python_version(),'numpy':np.__version__,'matplotlib':matplotlib.__version__,
 'envelope':{'x':x.tolist(),'correlations':dict(zip(labels,corr.tolist()))},
 'gain':{'fs_hz':fs,'samples':len(n),'frequencies_hz':[500,900],'signal_energy':float(s@s),'noise_energy':float(noise@noise),'inner_product':float(s@noise),'maximum_si_sdr_abs_db':float(np.max(abs(si))),'maximum_analytic_error_db':float(np.max(abs(ratio-analytic))),'g_half_error_ratio_db':float(10*np.log10(2))},
 'validation':{'observed':obs.tolist(),'predicted':pred.tolist(),'rmse':float(rmse),'group_observed':obs_group.tolist(),'group_predicted':pred_group.tolist(),'global_pearson':float(global_r),'within_group_pearson':within},
 'assertions':'passed'}
(OUT/'numerical-checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(checks,ensure_ascii=False,indent=2))
