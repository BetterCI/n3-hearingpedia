"""Original FFR teaching figures, no human data. Python 3.11, NumPy, Matplotlib.

Run from a repository checkout: python public/code/frequency-following-response/demo.py
All SVG/PNG outputs are derived from explicit equations or seeded simulations.
"""
from pathlib import Path
import json, re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE=Path(__file__).resolve().parent
OUT=HERE.parents[1]/'figures'/'frequency-following-response'
OUT.mkdir(parents=True,exist_ok=True)
available={f.name for f in font_manager.fontManager.ttflist}
font=next((f for f in ['Microsoft YaHei','Noto Sans CJK SC','SimHei'] if f in available),None)
if font is None: raise RuntimeError('Install Microsoft YaHei or Noto Sans CJK SC for Chinese labels.')
plt.rcParams.update({'font.family':font,'font.size':15,'axes.titlesize':17,
 'axes.labelsize':15,'xtick.labelsize':13,'ytick.labelsize':13,
 'legend.fontsize':12,'axes.spines.top':False,'axes.spines.right':False,
 'svg.fonttype':'none','svg.hashsalt':'hearingpedia-ffr-20261106','axes.unicode_minus':False})
BLUE='#2769a0'; ORANGE='#d37629'; GREEN='#397e6a'; GRAY='#747e89'
def base(title):
    fig,ax=plt.subplots(1,2,figsize=(14,6.3),dpi=100)
    fig.subplots_adjust(left=.075,right=.975,bottom=.20,top=.78,wspace=.29)
    fig.suptitle(title,x=.075,y=.96,ha='left',fontsize=23,fontweight='bold',color='#22344b')
    return fig,ax
def style(ax): ax.grid(alpha=.19);ax.set_axisbelow(True)
def save(fig,name,note):
    fig.text(.075,.045,note,fontsize=13,color='#52606f')
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None,'Creator':'Hearingpedia original teaching computation'})
    p=OUT/(name+'.svg'); s=p.read_text(encoding='utf-8')
    s=s.replace('width="1008pt" height="453.6pt"','width="1400" height="630"')
    p.write_text('\n'.join(line.rstrip() for line in s.splitlines())+'\n',encoding='utf-8')
    fig.savefig(OUT/(name+'.png'),dpi=100,metadata={'Software':'Hearingpedia'})
    plt.close(fig)

fs=20000; t=np.arange(0,.020,1/fs); delay=.002
a=np.cos(2*np.pi*250*t); b=np.cos(2*np.pi*250*(t-delay))
fig,ax=base('来源不变，合成幅度也能变化')
ax[0].plot(t*1000,a,color=BLUE,label='来源1')
ax[0].plot(t*1000,b,'--',color=ORANGE,label='来源2：延迟2 ms')
ax[0].plot(t*1000,a+b,color=GREEN,lw=2,label='合成')
ax[0].set(title='（a）250 Hz：反相抵消',xlabel='时间（ms）',ylabel='幅度（任意单位）',ylim=(-2.2,2.2))
ax[0].legend(loc='upper right',frameon=False)
f=np.linspace(0,1000,1001); amp=2*np.abs(np.cos(np.pi*f*delay))
ax[1].plot(f,amp,color=BLUE,lw=2.3)
ax[1].scatter([250,500],[0,2],color=[ORANGE,GREEN],zorder=3,s=50)
ax[1].annotate('250 Hz：0',(250,0),(280,.35),fontsize=13,arrowprops={'arrowstyle':'-','color':GRAY})
ax[1].annotate('500 Hz：2',(500,2),(600,2.12),fontsize=13)
ax[1].set(title='（b）两源延迟差固定为2 ms',xlabel='频率（Hz）',ylabel='合成幅度（任意单位）',ylim=(-.12,2.5),xlim=(0,1000))
for item in ax: style(item)
save(fig,'source-summation','两来源均为单位幅度、权重为1；解析教学例子，不是解剖模型或实测FFR。')

E=np.cos(2*np.pi*100*t); T=.5*np.cos(2*np.pi*500*(t-.008)); A=.6*np.cos(2*np.pi*500*t)
rp=E+T+A; rm=E-T-A; added=(rp+rm)/2; diff=(rp-rm)/2
fig,ax=base('极性相减：目标与伪迹可以一起留下')
for y,c,ls,label in [(E,BLUE,'-','E：不翻转'),(T,GREEN,'--','T：极性敏感神经分量'),(A,ORANGE,':','A：极性敏感伪迹')]:
    ax[0].plot(t*1000,y,color=c,ls=ls,lw=2,label=label)
ax[0].set(title='（a）自设的三个分量',xlabel='时间（ms）',ylabel='幅度（任意单位）',ylim=(-1.65,1.65))
ax[0].legend(loc='upper center',ncol=1,frameon=False,fontsize=11,bbox_to_anchor=(.5,1.03))
ax[1].plot(t*1000,added,color=BLUE,lw=2,label='相加 / 2 = E')
ax[1].plot(t*1000,diff,'--',color=ORANGE,lw=2,label='相减 / 2 = T + A')
ax[1].set(title='（b）组合后的记录',xlabel='时间（ms）',ylabel='幅度（任意单位）',ylim=(-1.65,1.65))
ax[1].legend(loc='upper right',frameon=False,fontsize=11)
for item in ax: style(item)
save(fig,'polarity','E为100 Hz；T、A为500 Hz；相减保留伪迹。理想代数示意，不是实际来源分离结果。')

fig,ax=base('平均降噪与时间抖动是两件不同的事')
Ns=np.array([1,4,16,64,256,1024]); noise=1/np.sqrt(Ns)
ax[0].loglog(Ns,noise,'o-',color=BLUE,lw=2,label='独立噪声标准差')
ax[0].loglog(Ns,np.ones(len(Ns)),'--',color=ORANGE,lw=2,label='固定同步成分')
ax[0].set(title='（a）噪声独立且等方差',xlabel='平均试次数 N',ylabel='相对单次的幅度',ylim=(.02,2))
ax[0].set_xticks([1,16,256,1024],[1,16,256,1024]);ax[0].legend(loc='lower left',frameon=False)
f=np.linspace(0,1500,601)
for sig,c,ls in [(.00005,BLUE,'-'),(.0002,ORANGE,'--'),(.0005,GREEN,':')]:
    ax[1].plot(f,np.exp(-.5*(2*np.pi*f*sig)**2),color=c,ls=ls,lw=2.3,label=f'抖动标准差 {sig*1000:g} ms')
ax[1].set(title='（b）零均值高斯时间抖动',xlabel='频率（Hz）',ylabel='相干平均幅度保留比例',ylim=(-.03,1.05),xlim=(0,1500))
ax[1].legend(loc='lower left',frameon=False)
for item in ax: style(item)
save(fig,'averaging-jitter','左：噪声标准差按1/√N下降；右：相位抵消的解析预测。更多试次不会使右图曲线恢复为1。')

rng=np.random.default_rng(20261106); ph=rng.uniform(-np.pi,np.pi,8); z=np.exp(1j*ph).mean()
fig=plt.figure(figsize=(14,6.3),dpi=100)
fig.subplots_adjust(left=.075,right=.975,bottom=.20,top=.78,wspace=.42)
fig.suptitle('随机相位，也可能得到非零PLV',x=.075,y=.96,ha='left',fontsize=23,fontweight='bold',color='#22344b')
ax0=fig.add_subplot(121,projection='polar'); ax1=fig.add_subplot(122)
for p in ph: ax0.plot([p,p],[0,1],color=BLUE,alpha=.6,lw=1.8)
ax0.plot([np.angle(z),np.angle(z)],[0,abs(z)],color=ORANGE,lw=5,label=f'平均向量：PLV={abs(z):.2f}')
ax0.set_ylim(0,1.12);ax0.set_yticks([.5,1]); ax0.set_title('（a）8个独立均匀相位',pad=25)
ax0.legend(loc='lower center',bbox_to_anchor=(.5,-.20),frameon=False)
counts=np.array([4,8,16,32,64,128,256]); rows=[]
for n in counts:
    phase=rng.uniform(-np.pi,np.pi,(5000,n)); plv2=np.abs(np.exp(1j*phase).mean(axis=1))**2
    ppc=(n*plv2-1)/(n-1)
    rows.append({'N':int(n),'mean_squared_PLV':float(plv2.mean()),'theoretical_squared_PLV':float(1/n),'mean_PPC':float(ppc.mean()),'monte_carlo_SE_squared_PLV':float(plv2.std(ddof=1)/np.sqrt(5000))})
ax1.semilogx(counts,[r['mean_squared_PLV'] for r in rows],'o-',color=BLUE,label='模拟：平方PLV均值')
ax1.semilogx(counts,1/counts,'--',color=GRAY,label='理论：1/N')
ax1.semilogx(counts,[r['mean_PPC'] for r in rows],'s-',color=GREEN,label='模拟：PPC均值')
ax1.axhline(0,color=GRAY,lw=.8)
ax1.set(title='（b）每个N重复5000次模拟',xlabel='试次数 N（对数坐标）',ylabel='无量纲统计量',ylim=(-.025,.29))
ax1.set_xticks(counts,[str(n) for n in counts]);ax1.legend(loc='upper right',frameon=False,fontsize=11);style(ax1)
save(fig,'phase-bias','独立均匀相位，固定种子20261106。PPC可为负；去除样本量偏差不等于去除测量噪声。')

checks={
 'source_cancellation_250Hz_max_abs':float(np.max(np.abs(a+b))),
 'source_amplitude_500Hz':float(2*abs(np.cos(np.pi*500*delay))),
 'polarity_sum_error':float(np.max(np.abs(added-E))),
 'polarity_difference_error':float(np.max(np.abs(diff-(T+A)))),
 'noise_SD_ratio_N4_to_N1':.5,
 'amplitude_SNR_gain_for_fourfold_N_dB':float(20*np.log10(2)),
 'jitter_0p2ms_gain_100Hz':float(np.exp(-.5*(2*np.pi*100*.0002)**2)),
 'jitter_0p2ms_gain_1000Hz':float(np.exp(-.5*(2*np.pi*1000*.0002)**2)),
 'random_phase_results':rows,
}
assert checks['source_cancellation_250Hz_max_abs']<1e-12
assert checks['polarity_sum_error']<1e-12 and checks['polarity_difference_error']<1e-12
assert all(abs(r['mean_squared_PLV']-1/r['N'])<5*r['monte_carlo_SE_squared_PLV'] for r in rows)
result={'date':'2026-11-06','data_type':'Original analytic and synthetic teaching examples; no human data',
 'sampling_rate_Hz':fs,'random_seed':20261106,'simulation_repetitions_per_N':5000,'checks':checks,'passed':True}
(HERE/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
