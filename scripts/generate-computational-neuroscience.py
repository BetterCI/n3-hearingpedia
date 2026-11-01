"""Original model demonstrations, not physiological recordings or fitted patient data."""
from pathlib import Path
import json
import numpy as np
from scipy import optimize, stats, linalg
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
FIG=ROOT/'public/figures/computational-neuroscience';PRE=ROOT/'artifacts/computational-neuroscience/figures'
REC=ROOT/'docs/research/computational-neuroscience-2026-11-02'
for p in (FIG,PRE,REC):p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':12,'svg.fonttype':'path',
 'svg.hashsalt':'computational-neuroscience-course','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,M,P='#22658c','#31755e','#b44e37','#61727d','#79639d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创计算神经科学教学图 · 指定模型或模拟数据，非生理实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.055,1,.91),w_pad=3,h_pad=3)
    path=FIG/f'{name}.svg';fig.savefig(path,metadata={'Date':None},facecolor='white')
    path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/f'{name}.png',dpi=105,facecolor='white');plt.close(fig)

fig,ax=plt.subplots(figsize=(14,6));ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
def box(x,y,w,h,text,color=B):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',ec=color,fc='#f7f9fc',lw=1.5))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=14,color=color)
box(.02,.58,.24,.24,'输入与条件\n声音、注入电流或任务',B)
box(.38,.58,.24,.24,'模型状态与规则\n膜电位、脉冲或网络',P)
box(.74,.58,.24,.24,'可检验输出\n响应、统计量或行为',G)
box(.34,.12,.32,.22,'独立数据与干预\n比较基线，检查失败',R)
for start,end in [((.27,.70),(.37,.70)),((.63,.70),(.73,.70)),((.85,.57),(.65,.35)),((.35,.23),(.1,.57))]:
    ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':M})
ax.text(.83,.22,'预测相似\n不自动等于机制相同',ha='center',color=M)
fig.suptitle('把假设写成模型，再让模型接受独立检验',fontsize=18,fontweight='bold');save(fig,'model-loop')

R_Mohm,C_pF=100.,200.;tau_ms=R_Mohm*C_pF/1000;EL=-65.;reset=-65.;threshold=-50.;ref_ms=2.;I_nA=.2
v_inf=EL+R_Mohm*I_nA;cross_ms=tau_ms*np.log((v_inf-reset)/(v_inf-threshold));period_ms=cross_ms+ref_ms
t=np.linspace(0,150,3001);spikes=np.arange(cross_ms,t[-1]+1e-10,period_ms)
voltage=np.empty_like(t)
for i,time in enumerate(t):
    past=spikes[spikes<=time]
    start=0 if len(past)==0 else past[-1]+ref_ms
    voltage[i]=reset if time<start else v_inf+(reset-v_inf)*np.exp(-(time-start)/tau_ms)
passive=v_inf+(reset-v_inf)*np.exp(-t/tau_ms)
currents=np.linspace(0,.5,501);rates=np.zeros_like(currents);valid=EL+R_Mohm*currents>threshold
rates[valid]=1000/(ref_ms+tau_ms*np.log((EL+R_Mohm*currents[valid]-reset)/(EL+R_Mohm*currents[valid]-threshold)))
fig,axes=plt.subplots(1,2,figsize=(14,6))
axes[0].plot(t,passive,color=M,ls='--',label='只作被动充电，不加阈值');axes[0].plot(t,voltage,color=B,label='LIF阈值与复位')
axes[0].axhline(threshold,color=R,ls=':');axes[0].scatter(spikes,np.full(len(spikes),threshold),marker='|',s=180,color=R,label='发放事件；未画动作电位形状')
axes[0].set(xlabel='时间 / ms',ylabel='膜电位 / mV',title='恒定电流 0.2 nA：首发约 27.73 ms');axes[0].legend(fontsize=9,loc='lower right')
axes[1].plot(currents,rates,color=G,lw=2);axes[1].axvline(.15,color=M,ls='--');axes[1].scatter([.2],[1000/period_ms],color=R)
axes[1].set(xlabel='恒定注入电流 / nA',ylabel='稳态发放率 / Hz',title='电流阈值 0.15 nA；0.2 nA 时约 33.64 Hz')
fig.suptitle('积分发放：微分方程、阈值、复位和不应期缺一不可',fontsize=18,fontweight='bold');save(fig,'lif-and-rate')

st=np.linspace(0,60,601);gL,gE=10.,5.;EE,EI=0.,-65.;shunt=[]
fig,ax=plt.subplots(figsize=(12,5.8))
for gI,color in [(0,B),(10,G)]:
    total=gL+gE+gI;steady=(gL*EL+gE*EE+gI*EI)/total;effective_tau=C_pF/total
    curve=steady+(EL-steady)*np.exp(-st/effective_tau)
    ax.plot(st,curve,color=color,lw=2,label=f'gI = {gI} nS：V∞ = {steady:.2f} mV，τ = {effective_tau:.2f} ms')
    shunt.append({'gI_nS':gI,'steady_mV':steady,'tau_ms':effective_tau})
ax.axhline(EL,color=M,ls='--');ax.set(xlabel='电导阶跃后时间 / ms',ylabel='被动膜电位 / mV');ax.legend(loc='lower right')
fig.suptitle('分流抑制示意：EI = 静息电位，仍可压低兴奋响应并缩短时间常数',fontsize=17,fontweight='bold');save(fig,'synaptic-shunt')

prng=np.random.default_rng(20261106);trials=[];segments=[(0,.05,5),(.05,.15,40),(.15,.25,5)]
for repeat in range(200):
    events=[]
    for start,end,rate in segments:
        count=prng.poisson((end-start)*rate);events.extend(prng.uniform(start,end,count))
    trials.append(np.sort(events))
bins=np.linspace(0,.25,26);psth=np.histogram(np.concatenate(trials),bins=bins)[0]/(200*.01)
counts=np.array([len(v) for v in trials]);fano=counts.var(ddof=1)/counts.mean()
fig,axes=plt.subplots(1,2,figsize=(14,5.8));axes[0].eventplot(trials[:30],colors=B,linewidths=.8)
axes[0].set(xlim=(0,.25),xlabel='刺激对齐时间 / s',ylabel='模拟试次（前30次）',title='同一确定速率函数，脉冲时刻仍不同')
axes[1].stairs(psth,bins,color=G,lw=2,label='200次试验，10 ms PSTH')
axes[1].plot([0,.05,.05,.15,.15,.25],[5,5,40,40,5,5],color=R,ls='--',label='设定强度 λ(t)')
axes[1].set(xlabel='时间 / s',ylabel='每秒事件数 / Hz',title=f'整窗期望4.75；样本均值{counts.mean():.2f}，Fano {fano:.2f}');axes[1].legend(fontsize=10)
fig.suptitle('非齐次Poisson模型：跨重复平均与单次脉冲列不是同一个量',fontsize=18,fontweight='bold');save(fig,'spikes-and-psth')

lags=np.arange(8)*5;frequencies=np.arange(1,7);f,ll=np.meshgrid(frequencies,lags,indexing='ij')
kernel=np.exp(-.5*((f-3.5)/.9)**2-.5*((ll-10)/6)**2)-.7*np.exp(-.5*((f-3.5)/1.2)**2-.5*((ll-27)/6)**2)
kernel/=np.linalg.norm(kernel)
grng=np.random.default_rng(20261105);x=grng.uniform(-1,1,4000);X=np.column_stack([np.ones(4000),x]);dt=.01
truth=np.array([np.log(30),.8]);lam=np.exp(X@truth);y=grng.poisson(lam*dt);train=X[:2000];yt=y[:2000]
def objective(beta):return np.sum(dt*np.exp(train@beta)-yt*(train@beta))
def gradient(beta):return train.T@(dt*np.exp(train@beta)-yt)
fit=optimize.minimize(objective,[np.log(yt.mean()/dt),0],jac=gradient,method='BFGS',options={'gtol':1e-9})
assert fit.success,fit.message
test_mu=np.exp(X[2000:]@fit.x)*dt;null_mu=yt.mean()
gain=np.sum(y[2000:]*np.log(test_mu/null_mu)-test_mu+null_mu);bits_per_spike=gain/np.log(2)/y[2000:].sum()
fig,axes=plt.subplots(1,2,figsize=(14,5.8));vmax=np.abs(kernel).max()
im=axes[0].imshow(kernel,origin='lower',aspect='auto',cmap='RdBu_r',vmin=-vmax,vmax=vmax,extent=(-2.5,37.5,.5,6.5))
axes[0].set(xlabel='因果滞后 / ms',ylabel='频带编号（不表示Hz刻度）',title='人工指定的单位范数时频权重 K');fig.colorbar(im,ax=axes[0],label='特征权重（无量纲）')
grid=np.linspace(-1,1,200);axes[1].plot(grid,30*np.exp(.8*grid),color=R,ls='--',label='设定生成率')
axes[1].plot(grid,np.exp(fit.x[0]+fit.x[1]*grid),color=B,label='训练集MLE');axes[1].axhline(null_mu/dt,color=M,ls=':',label='训练集常数率基线')
axes[1].set(xlabel='设定的无量纲投影特征 x',ylabel='条件发放强度 / Hz',title=f'独立测试集：相对基线 {bits_per_spike:.3f} bit/spike');axes[1].legend(fontsize=10)
fig.suptitle('编码模型：从特征权重到非负强度，再到有噪声的计数',fontsize=18,fontweight='bold');save(fig,'encoding-model')

T=.1;means_plus=np.array([20,5])*T;means_minus=means_plus[::-1]
drng=np.random.default_rng(20261107);cp=drng.poisson(means_plus,size=(500,2));cm=drng.poisson(means_minus,size=(500,2))
accuracy=stats.skellam.sf(0,*means_plus)+.5*stats.skellam.pmf(0,*means_plus)
fig,axes=plt.subplots(1,2,figsize=(14,5.8));jitter=drng.uniform(-.18,.18,(1000,2))
axes[0].scatter(cp[:,0]+jitter[:500,0],cp[:,1]+jitter[:500,1],color=B,s=10,alpha=.2,label='类别 +：平均计数 (2, 0.5)')
axes[0].scatter(cm[:,0]+jitter[500:,0],cm[:,1]+jitter[500:,1],color=R,s=10,alpha=.2,label='类别 −：平均计数 (0.5, 2)')
axes[0].plot([0,8],[0,8],color=M,ls='--');axes[0].set(xlabel='神经元1计数（显示加少量抖动）',ylabel='神经元2计数（显示加少量抖动）',xlim=(-.4,8),ylim=(-.4,8),title='等先验、条件独立Poisson；对角线为决策界');axes[0].legend(fontsize=9)
dur=np.linspace(.005,.4,150);acc=stats.skellam.sf(0,20*dur,5*dur)+.5*stats.skellam.pmf(0,20*dur,5*dur)
axes[1].plot(dur,acc,color=G,lw=2);axes[1].scatter([T],[accuracy],color=R);axes[1].set(xlabel='固定读出窗 / s',ylabel='模型最优分类正确概率',ylim=(.5,1),title=f'100 ms：{accuracy:.4f}；平局随机选择')
fig.suptitle('群体读出依赖联合分布、先验、观察窗与决策损失',fontsize=18,fontweight='bold');save(fig,'population-readout')

Ws=[np.array([[1.2,-1],[1,-.5]]),np.array([[1.8,-.3],[.6,-.3]])];network=[];nt=np.linspace(0,100,401)
fig,axes=plt.subplots(1,2,figsize=(14,5.8))
for W,color,name in zip(Ws,[G,R],['稳定线性化','不稳定线性化']):
    A=(W-np.eye(2))/20;eig=np.linalg.eigvals(A);delta=np.array([linalg.expm(A*time)@np.array([1.,0.]) for time in nt])
    axes[0].scatter(eig.real,eig.imag,color=color,s=70,label=name)
    axes[1].plot(nt,np.linalg.norm(delta,axis=1),color=color,lw=2,label=name)
    network.append({'W':W.tolist(),'A_per_ms':A.tolist(),'eig_real_per_ms':eig.real.tolist(),'eig_imag_per_ms':eig.imag.tolist(),'perturbation_norm_100ms':float(np.linalg.norm(delta[-1]))})
axes[0].axvline(0,color=M,ls='--');axes[0].axhline(0,color=M,lw=.7);axes[0].set(xlabel='特征值实部 / ms⁻¹',ylabel='特征值虚部 / ms⁻¹',title='固定点附近的Jacobian特征值');axes[0].legend(fontsize=10)
axes[1].set(xlabel='时间 / ms',ylabel='线性扰动范数 / 初始范数',yscale='log',title='扰动是偏离量，可有正负分量');axes[1].legend(fontsize=10)
fig.suptitle('兴奋与抑制同时存在，不保证网络固定点稳定',fontsize=18,fontweight='bold');save(fig,'network-stability')

negative=np.linspace(-80,-.01,500);positive=np.linspace(.01,80,500);Aplus,Aminus=.01,.012;stdp_tau=20.
fig,axes=plt.subplots(1,2,figsize=(14,5.8))
axes[0].plot(negative,-Aminus*np.exp(negative/stdp_tau),color=R,lw=2,label='post先于pre')
axes[0].plot(positive,Aplus*np.exp(-positive/stdp_tau),color=G,lw=2,label='pre先于post');axes[0].axhline(0,color=M,lw=.8);axes[0].axvline(0,color=M,ls=':')
axes[0].set(xlabel='Δt = tpost − tpre / ms',ylabel='单个配对的权重变化（无量纲）',title='双指数配对STDP；零时差另约定');axes[0].legend(fontsize=10)
number=np.arange(301);unbounded=.5+number*.01;bounded=np.clip(unbounded,0,1)
axes[1].plot(number,unbounded,color=R,ls='--',label='每次固定 +0.01，无约束')
axes[1].plot(number,bounded,color=B,label='人为截断到 [0,1]');axes[1].set(xlabel='重复正向更新次数',ylabel='模型权重',title='权重约束是额外规则，不能省略');axes[1].legend(fontsize=10)
fig.suptitle('学习规则描述如何改变参数，不能只写“共同活动就增强”',fontsize=18,fontweight='bold');save(fig,'plasticity-rules')

vrng=np.random.default_rng(20261108);phase_stats=[]
fig=plt.figure(figsize=(15,5.8));axes=[fig.add_subplot(1,3,1,projection='polar'),fig.add_subplot(1,3,2,projection='polar'),fig.add_subplot(1,3,3)]
for sigma,ax,color in zip([.0001,.0005],axes[:2],[B,R]):
    errors=vrng.normal(0,sigma,2000);angles=np.mod(2*np.pi*500*errors,2*np.pi);vs=abs(np.exp(1j*angles).mean())
    hist,edges=np.histogram(angles,bins=np.linspace(0,2*np.pi,25));ax.bar(edges[:-1],hist/len(angles),width=np.diff(edges),align='edge',color=color,alpha=.6)
    ax.set_title(f'500 Hz；σ = {sigma*1000:.1f} ms\n样本VS = {vs:.3f}',pad=22);ax.set_ylim(0,.35);ax.set_yticklabels([])
    phase_stats.append({'jitter_sd_s':sigma,'sample_vs':float(vs),'population_vs_500Hz':float(np.exp(-.5*(2*np.pi*500*sigma)**2))})
freq=np.linspace(0,4000,500)
for sigma,color in [(.0001,B),(.0005,R)]:axes[2].plot(freq,np.exp(-.5*(2*np.pi*freq*sigma)**2),color=color,label=f'σ = {sigma*1000:.1f} ms')
axes[2].set(xlabel='参考周期频率 / Hz',ylabel='指定抖动模型的总体VS',ylim=(0,1.02),title='同一时间抖动，对高频影响更大');axes[2].legend(fontsize=10)
fig.suptitle('相位锁定：相位集中不等于每个声音周期都放电',fontsize=18,fontweight='bold');save(fig,'phase-and-jitter')

report={'R_Mohm':R_Mohm,'C_pF':C_pF,'tau_ms':tau_ms,'rest_mV':EL,'reset_mV':reset,'threshold_mV':threshold,'refractory_ms':ref_ms,
 'current_nA':I_nA,'steady_mV':v_inf,'rheobase_nA':(threshold-EL)/R_Mohm,'first_spike_ms':cross_ms,'period_ms':period_ms,'steady_rate_Hz':1000/period_ms,'spike_times_ms':spikes.tolist(),
 'shunt':shunt,'poisson_seed':20261106,'poisson_trials':200,'poisson_duration_s':.25,'poisson_segments':segments,'poisson_expected_count':4.75,
 'poisson_count_mean':float(counts.mean()),'poisson_count_variance':float(counts.var(ddof=1)),'poisson_fano':float(fano),'psth_bin_s':.01,'psth_Hz':psth.tolist(),'poisson_counts':counts.tolist(),
 'glm_seed':20261105,'glm_dt_s':dt,'glm_total_bins':4000,'glm_train_bins':2000,'glm_test_bins':2000,'glm_true_coefficients':truth.tolist(),'glm_fitted_coefficients':fit.x.tolist(),
 'glm_train_baseline_Hz':float(null_mu/dt),'glm_test_spikes':int(y[2000:].sum()),'glm_test_gain_nats':float(gain),'glm_test_gain_bits_per_spike':float(bits_per_spike),'glm_gradient_norm':float(np.linalg.norm(gradient(fit.x))),
 'strf_kernel':kernel.tolist(),'population_rates_plus_Hz':[20,5],'population_rates_minus_Hz':[5,20],'population_window_s':T,'population_optimal_accuracy':float(accuracy),'population_seed':20261107,
 'network_tau_ms':20,'network':network,'stdp_Aplus':Aplus,'stdp_Aminus':Aminus,'stdp_tau_ms':stdp_tau,'stdp_plus_10ms':float(Aplus*np.exp(-.5)),'stdp_minus_10ms':float(-Aminus*np.exp(-.5)),
 'phase_seed':20261108,'phase_samples':2000,'phase_statistics':phase_stats,'delay_s':.0002,'delay_reference_Hz':500,'delay_degrees':36.}
(REC/'calculations.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ['poisson_counts','psth_Hz','strf_kernel','network']},ensure_ascii=True,indent=2))
