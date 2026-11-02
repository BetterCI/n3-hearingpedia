"""Ten original stochastic-process figures and native ensemble course sketch."""
from pathlib import Path
import importlib.util,sys,json
sys.dont_write_bytecode=True
import numpy as np
from scipy.signal import periodogram,welch
from scipy.stats import norm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];spec=importlib.util.spec_from_file_location('sp',ROOT/'public/code/stochastic-processes/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures/stochastic-processes';PRE=ROOT/'artifacts/stochastic-processes/figures';REC=ROOT/'docs/research/stochastic-processes-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'stochastic-processes-course','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创随机过程教学图 · 指定概率模型/模拟，非录音或神经与听者实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2);path=FIG/(name+'.svg');fig.savefig(path,metadata={'Date':None},facecolor='white');path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8');fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
# 1 Stationary initialization means the cross-sectional law is N(0,1) from sample zero.
x=m.ar1(n=300,paths=4000);fig,axes=plt.subplots(1,2,figsize=(14,5.5));t=np.arange(300)/m.FS
for j,col in enumerate([B,G,R,P]):axes[0].plot(t,x[j],color=col,lw=1,label=f'实现{j+1}')
axes[0].axvline(.1,color=M,ls=':');axes[0].set(xlabel='时间 / s',ylabel='X[n] / Pa',title='（a）同一AR(1)模型的四条实现');axes[0].legend(fontsize=9)
axes[1].hist(x[:,100],bins=45,density=True,color=B,alpha=.45,label='4000条实现的n=100切片');q=np.linspace(-4,4,501);axes[1].plot(q,norm.pdf(q),color=R,label='已知总体N(0,1)');axes[1].set(xlabel='固定时刻的取值 / Pa',ylabel='概率密度 / Pa⁻¹',title='（b）横切总体，不是沿一条记录扫时间');axes[1].legend(fontsize=9)
fig.suptitle('过程、实现与固定时刻随机变量：三个层次要分开',fontsize=18,fontweight='bold');save(fig,'ensemble-realizations')
# 2 Shared random amplitude gives whiteness without independence or power ergodicity.
amplitudes,x=m.mixture_white();n=np.arange(1,x.shape[1]+1);fig,axes=plt.subplots(1,2,figsize=(14,5.5))
for i in range(6):
    col=B if amplitudes[i]==1 else P;axes[0].plot(n,np.cumsum(x[i])/n,color=col,alpha=.65,lw=1);axes[1].plot(n,np.cumsum(x[i]**2)/n,color=col,alpha=.65,lw=1)
axes[0].axhline(0,color=G,ls='--');axes[0].set(xlabel='记录长度 N',ylabel='时间样本均值',xscale='log',title='（a）均值可趋近总体0')
for v,col,label in [(1,B,'条件功率A²=1'),(4,P,'条件功率A²=4'),(2.5,R,'总体均方值E[A²]=2.5')]:axes[1].axhline(v,color=col,ls='--',label=label)
axes[1].set(xlabel='记录长度 N',ylabel='时间样本均方值',xscale='log',ylim=(0,5.5),title='（b）单条记录功率不趋向总体2.5');axes[1].legend(fontsize=9)
fig.suptitle('X[n]=A·W[n]：严格平稳且白，但样本依赖、功率不遍历',fontsize=18,fontweight='bold');save(fig,'white-not-independent')
# 3 Correlation limits averaging benefit, using exact finite-N variance.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));lag=np.arange(21);axes[0].stem(lag,m.AR**lag,basefmt=' ',linefmt=B,markerfmt='o');axes[0].set(xlabel='滞后 k / 样本',ylabel='C[k] / Pa²',title='（a）a=0.8、Var(X)=1：相关跨多个样本')
N=np.arange(1,513);exact=np.array([m.mean_variance(int(n)) for n in N]);axes[1].loglog(N,exact,color=B,label='AR(1)精确均值方差');axes[1].loglog(N,1/N,color=G,ls='--',label='独立同方差1/N');axes[1].loglog(N,9/N,color=P,ls=':',label='大N渐近9/N');axes[1].set(xlabel='平均的样本数 N',ylabel='Var(样本均值) / Pa²',title='（b）相关使平均降噪不同于独立样本');axes[1].legend(fontsize=9)
fig.suptitle('相关函数决定时间平均的精度，不仅是曲线是否平滑',fontsize=18,fontweight='bold');save(fig,'correlation-averaging')
# 4 Stationary spectra and population filtering formula, no single-record FFT called truth.
f=np.linspace(-m.FS/2,m.FS/2,4001);S=m.ar_psd(f);H=m.moving_average_H(f);fig,axes=plt.subplots(1,2,figsize=(14,5.5));axes[0].semilogy(f,np.full_like(f,m.INNOVATION_VARIANCE/m.FS),color=M,label='白创新谱q/fₛ');axes[0].semilogy(f,S,color=B,label='因果AR(1)输出谱');axes[0].set(xlabel='频率 / Hz（双侧）',ylabel='PSD / Pa²·Hz⁻¹',title='（a）R[k]=0.8^|k|对应有色谱');axes[0].legend(fontsize=9)
axes[1].semilogy(f,S,color=B,alpha=.5,label='输入Sₓ');axes[1].semilogy(f,np.maximum(abs(H)**2*S,1e-10),color=G,label='8点平均输出|H|²Sₓ');axes[1].set(xlabel='频率 / Hz（双侧）',ylabel='PSD / Pa²·Hz⁻¹',title=f'（b）输出方差约{m.mean_variance(8):.5f}，并非1/8');axes[1].legend(fontsize=9)
fig.suptitle('随机输入经过LTI：改变相关和谱，不自动变成独立噪声',fontsize=18,fontweight='bold');save(fig,'lti-colored-spectra')
# 5 Dirac line mass is not an ordinary finite-height density.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));axes[0].stem([-125,125],[.5,.5],basefmt=' ',linefmt=B,markerfmt='o');axes[0].set(xlabel='频率 / Hz',ylabel='离散谱质量 / Pa²',xlim=(-250,250),ylim=(0,.65),title='（a）随机相位正弦：双侧各0.5 Pa²')
for n,col in [(256,G),(1024,P)]:
    f,s=periodogram(m.random_phase_tone(n),fs=m.FS,window='boxcar',detrend=False,scaling='density');axes[1].plot(f,s,'o-',color=col,ms=3,label=f'N={n}, Δf={m.FS/n:g} Hz')
axes[1].set(xlabel='频率 / Hz（单侧）',ylabel='有限记录PSD / Pa²·Hz⁻¹',xlim=(110,140),title='（b）峰高随N变，积分均方值均为1 Pa²');axes[1].legend(fontsize=9)
fig.suptitle('平稳过程也可以有谱线：有限FFT峰高不是Dirac的高度',fontsize=18,fontweight='bold');save(fig,'spectral-lines')
# 6 Sampling in physical Hz has an alias sum with no extra 1/fs factor.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));f=np.linspace(-1300,1300,2601);axes[0].plot(f,.001*(abs(f)<=750),color=B,lw=2);axes[0].axvspan(-500,500,color=G,alpha=.1);axes[0].set(xlabel='连续时间频率 / Hz',ylabel='PSD / Pa²·Hz⁻¹',ylim=(-.0001,.0014),title='（a）带限白谱：±750 Hz，总方差1.5 Pa²')
f=np.linspace(-500,500,2001);axes[1].plot(f,m.alias_density(f),color=R,label='fs=1000 Hz直接采样后的折叠谱');axes[1].plot(f,.001*(abs(f)<=450),color=G,ls='--',label='先理想低通至±450 Hz');axes[1].set(xlabel='采样后的基带频率 / Hz',ylabel='PSD / Pa²·Hz⁻¹',ylim=(-.0001,.0025),title='（b）折叠保持此例总方差；预滤波则删除带外量');axes[1].legend(fontsize=9)
fig.suptitle('连续白噪声、带限噪声与离散白序列不是同一个对象',fontsize=18,fontweight='bold');save(fig,'sampling-aliasing')
# 7 Population MSE, not fit-to-truth or a fair same-information algorithm contest.
w=m.wiener_example();fig,axes=plt.subplots(1,2,figsize=(14,5.5));n=np.arange(200,400);axes[0].plot(n,w['observed'][n],color=M,alpha=.45,lw=.7,label='观测z=s+v');axes[0].plot(n,w['clean'][n],color=B,lw=1.3,label='模拟已知s');axes[0].plot(n,w['estimate'][n],color=G,lw=1.1,label='已知模型三抽头因果LMMSE');axes[0].set(xlabel='离散时刻 n',ylabel='指定幅值 / Pa',title='（a）去掉历史不全的最初2点后取片段');axes[0].legend(fontsize=9)
values=[w['noisy_mse'],w['causal_mse'],w['noncausal_mse']];axes[1].bar(['直接观测','因果3抽头','理想全时域非因果'],values,color=[M,G,P])
for i,v in enumerate(values):axes[1].text(i,v+.012,f'{v:.6f}',ha='center')
axes[1].set(ylabel='模型总体MSE / Pa²',ylim=(0,.6),title='（b）来自精确二阶模型，不是这段样本的评分')
fig.suptitle('最优性必须指定信息和模型：线性最优、因果性与总体风险',fontsize=18,fontweight='bold');save(fig,'wiener-estimation')
# 8 Poisson event times versus Brownian Gaussian increments; both nonstationary states.
events,t,paths=m.count_and_brownian();fig,axes=plt.subplots(1,2,figsize=(14,5.5))
for i,col in enumerate([B,G,R,P]):
    e=events[i];axes[0].step(np.r_[0,e,1],np.r_[0,np.arange(1,len(e)+1),len(e)],where='post',color=col,lw=1);axes[1].plot(t,paths[i],color=col,lw=.8)
axes[0].plot(t,20*t,color=M,ls='--',label='总体均值λt');axes[0].set(xlabel='时间 / s',ylabel='累计计数N(t)',title='（a）λ=20 s⁻¹：连续时间、离散取值');axes[0].legend(fontsize=9)
axes[1].set(xlabel='时间（模型单位）',ylabel='标准Brownian状态B(t)',title='（b）Δt=0.001网格，增量方差Δt')
fig.suptitle('平稳增量不等于状态平稳：Poisson计数与Brownian运动',fontsize=18,fontweight='bold');save(fig,'poisson-brownian')
# 9 Finite realization estimators and a counterexample for zero-extended unbiased correlations.
x=m.ar1()[0];fig,axes=plt.subplots(1,2,figsize=(14,5.5));f,p=periodogram(x,fs=m.FS,window='boxcar',detrend=False,scaling='density');fw,pw=welch(x,fs=m.FS,window='hann',nperseg=512,noverlap=256,detrend=False,scaling='density')
axes[0].semilogy(f,p,color=M,alpha=.35,lw=.5,label='整段矩形周期图N=8192');axes[0].semilogy(fw,pw,color=B,lw=1.2,label='Welch：512点Hann、50%重叠');axes[0].semilogy(fw[1:-1],2*m.ar_psd(fw[1:-1]),color=R,ls='--',label='总体双侧谱×2（仅内部频率）');axes[0].set(xlabel='频率 / Hz（单侧）',ylabel='PSD / Pa²·Hz⁻¹',xlim=(2,500),ylim=(1e-8,.1),title='（a）同一条实现：方差与分辨率取舍');axes[0].legend(fontsize=8)
_,b,u,theta,sb,su=m.finite_correlations();axes[1].plot(theta/np.pi,sb,color=G,label='固定分母N，区间外置0');axes[1].plot(theta/np.pi,su,color=P,label='分母N−|k|，区间外置0');axes[1].axhline(0,color=M,lw=.7);axes[1].set(xlabel='归一化角频率 ω/π',ylabel='相关估计的傅里叶级数值',title='（b）x=[1,−1,1]：无偏逐滞后估计可产生负谱');axes[1].legend(fontsize=8)
fig.suptitle('有限记录的估计值不是总体定律：无偏与合法谱也不是一回事',fontsize=18,fontweight='bold');save(fig,'finite-estimation')
# 10 Stationary initial law versus time-homogeneous transitions alone.
Pmat,pi,states=m.markov_example();fig,axes=plt.subplots(1,2,figsize=(14,5.5));axes[0].step(np.arange(len(states)),states,where='post',color=B);axes[0].set(xlabel='离散步 n',ylabel='状态',yticks=[0,1],ylim=(-.2,1.2),title='（a）初始按π=(2/3,1/3)抽取的一条链')
n=np.arange(61)
for init,col in [(0,G),(1,P)]:prob=[(np.eye(2)[init]@np.linalg.matrix_power(Pmat,int(k)))[1] for k in n];axes[1].plot(n,prob,color=col,label=f'固定初态{init}')
axes[1].axhline(1/3,color=R,ls='--',label='平稳初分布：Pr(状态1)=1/3');axes[1].set(xlabel='离散步 n',ylabel='Pr(状态1)',title='（b）同一转移矩阵，初始分布改变早期统计');axes[1].legend(fontsize=9)
fig.suptitle('Markov是条件依赖结构；时间齐次不自动保证过程已平稳',fontsize=18,fontweight='bold');save(fig,'markov-stationarity')
# Original course thumbnail: ensemble paths and a vertical random-variable slice.
fig,ax=plt.subplots(figsize=(6.4,3.6));ax.axis('off');ax.set(xlim=(0,1),ylim=(-3,3.5));paths=m.ar1(n=90,paths=4,seed=91);tt=np.linspace(.05,.9,90)
for row,col in zip(paths,[B,G,R,P]):ax.plot(tt,.8*row,color=col,lw=1.5,alpha=.85)
ax.plot([.62,.62],[-2.7,2.7],color=M,ls='--',lw=1.3);ax.text(.06,2.9,'随机过程',fontsize=18,fontweight='bold',color=B);fig.tight_layout();path=ROOT/'public/figures/foundation-courses/stochastic-processes.svg';fig.savefig(path,metadata={'Date':None},transparent=True);path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8');plt.close(fig)
(REC/'calculations.json').write_text(json.dumps(m.summary(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(m.summary(),ensure_ascii=False))
