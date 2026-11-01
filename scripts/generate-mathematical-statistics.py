"""Original statistical teaching figures. All observations are invented or simulated."""
from pathlib import Path
from itertools import product
import json
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
FIG=ROOT/'public/figures/mathematical-statistics'
PRE=ROOT/'artifacts/mathematical-statistics/figures'
REC=ROOT/'docs/research/mathematical-statistics-2026-11-02'
for p in (FIG,PRE,REC):p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':12,'svg.fonttype':'path',
 'svg.hashsalt':'mathematical-statistics-course','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,M,P='#22658c','#31755e','#b44e37','#61727d','#79639d'

def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创数理统计教学图 · 虚构数据或指定模型，非听者实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.05,1,.91),w_pad=3,h_pad=3)
    path=FIG/f'{name}.svg';fig.savefig(path,metadata={'Date':None},facecolor='white')
    path.write_text('\n'.join(line.rstrip() for line in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/f'{name}.png',dpi=105,facecolor='white');plt.close(fig)

d=np.array([1,2,3,0,4,2,1,3,2,5,-1,2.])
n=len(d);mean=d.mean();sd=d.std(ddof=1);se=sd/np.sqrt(n);tc=stats.t.ppf(.975,n-1)
ci=np.array([mean-tc*se,mean+tc*se]);tstat=mean/se;pval=2*stats.t.sf(abs(tstat),n-1)
before=np.array([-1,2,-3,0,-2,1,-4,3,-2,0,2,-1.]);after=before-d
boot_rng=np.random.default_rng(20261102)
boot_index=boot_rng.integers(0,n,size=(20000,n));boot=d[boot_index].mean(axis=1)
boot_ci=np.quantile(boot,[.025,.975],method='linear')
signs=np.array(list(product([-1,1],repeat=n)));null=(signs@d)/n
sign_p=np.mean(np.abs(null)>=abs(mean)-1e-12)
wilson=stats.binomtest(60,80).proportion_ci(method='wilson')
post=stats.beta.ppf([.025,.975],61,21)

fig,ax=plt.subplots(figsize=(14,6));ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
def box(x,y,w,h,text,color=B):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',ec=color,fc='#f7f9fc',lw=1.5))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',color=color,fontsize=14)
box(.02,.58,.22,.24,'目标总体\n指定人群与任务',P)
box(.37,.58,.25,.24,'12 位听者\n每人得到一对阈值',B)
box(.75,.58,.22,.24,'12 个配对差\n估计总体平均差',G)
for x1,x2 in [(.25,.36),(.63,.74)]:ax.annotate('',xy=(x2,.70),xytext=(x1,.70),arrowprops={'arrowstyle':'->','color':M})
box(.31,.12,.38,.23,'每人可有很多次原始反应\n试次嵌套在听者之内',R)
ax.annotate('',xy=(.5,.57),xytext=(.5,.36),arrowprops={'arrowstyle':'->','color':M})
ax.text(.83,.24,'抽样方式与相关结构\n决定推断适用范围',ha='center',color=M)
fig.suptitle('先确定研究对象与独立信息来自哪里',fontsize=18,fontweight='bold');save(fig,'sampling-units')

fig,axes=plt.subplots(1,2,figsize=(14,5.8));x=np.linspace(-8,12,1000)
axes[0].plot(x,stats.norm.pdf(x,2,3),color=B,lw=2);axes[0].axvline(2,color=M,ls='--')
axes[0].set(title='单个听者的模型分布：SD = 3 dB',xlabel='个体阈值差 / dB',ylabel='概率密度 / dB⁻¹')
for count,color in [(12,G),(48,P)]:axes[1].plot(x,stats.norm.pdf(x,2,3/np.sqrt(count)),label=f'n = {count}，SE = {3/np.sqrt(count):.3f} dB',color=color,lw=2)
axes[1].axvline(2,color=M,ls='--');axes[1].set(xlim=(-1,5),title='重复抽样时样本均值的分布',xlabel='样本平均阈值差 / dB',ylabel='概率密度 / dB⁻¹');axes[1].legend()
fig.suptitle('标准差描述个体差异，标准误描述估计量的抽样波动',fontsize=18,fontweight='bold');save(fig,'sampling-distributions')

fig,axes=plt.subplots(1,2,figsize=(14,5.8));p=np.linspace(.001,.999,1000)
loglik=60*np.log(p)+20*np.log1p(-p);logmax=60*np.log(.75)+20*np.log(.25)
axes[0].plot(p,np.exp(loglik-logmax),color=B,lw=2);axes[0].axvline(.75,color=M,ls='--');axes[0].set(title='60 / 80：以最大值缩放的似然',xlabel='候选正确概率 p',ylabel='L(p) / L(0.75)')
axes[1].plot(p,stats.beta.pdf(p,1,1),label='先验 Beta(1, 1)',color=M,ls='--')
axes[1].plot(p,stats.beta.pdf(p,61,21),label='后验 Beta(61, 21)',color=G,lw=2)
axes[1].fill_between(p,0,stats.beta.pdf(p,61,21),where=(p>=post[0])&(p<=post[1]),color=G,alpha=.2)
axes[1].set(title='指定先验后，才能谈后验概率',xlabel='正确概率 p',ylabel='概率密度');axes[1].legend()
fig.suptitle('似然不是参数概率分布，归一化与先验要分清',fontsize=18,fontweight='bold');save(fig,'likelihood-and-posterior')

cov_rng=np.random.default_rng(20261103);samples=cov_rng.normal(2,3,size=(40,12));means=samples.mean(axis=1)
half=tc*samples.std(axis=1,ddof=1)/np.sqrt(12);cover=(means-half<=2)&(means+half>=2)
fig,ax=plt.subplots(figsize=(13,7))
for i in range(40):ax.errorbar(means[i],i+1,xerr=half[i],fmt='o',ms=3,color=G if cover[i] else R,capsize=2,lw=1.3)
ax.axvline(2,color=M,ls='--',label='固定真均值 μ = 2 dB');ax.set(xlabel='每批样本得到的均值及 95% t 区间 / dB',ylabel='独立模拟批次',ylim=(0,41));ax.legend(loc='lower right')
fig.suptitle(f'40 批独立正态样本：{cover.sum()} 个区间覆盖固定真值（不要求恰好 38 个）',fontsize=18,fontweight='bold');save(fig,'confidence-coverage')

fig,axes=plt.subplots(1,2,figsize=(14,6.4))
for i,(a,b) in enumerate(zip(before,after)):axes[0].plot([0,1],[a,b],marker='o',color=P,alpha=.55)
axes[0].set(xticks=[0,1],xticklabels=['条件 A','条件 B'],ylabel='虚构噪声中言语阈值 / dB SNR',title='同一条线连接同一位听者')
axes[1].scatter(d,np.arange(1,13),color=B,s=35,label='每位听者：A − B')
axes[1].errorbar(mean,0,xerr=tc*se,fmt='D',ms=7,color=G,capsize=6,label='平均差及 95% t 区间')
axes[1].axvline(0,color=M,ls='--');axes[1].set(xlabel='阈值差 / dB，正值表示 B 阈值更低',ylabel='听者编号；0 行为总体均值估计',yticks=range(13),title=f'平均差 {mean:.2f} dB，区间 [{ci[0]:.2f}, {ci[1]:.2f}] dB');axes[1].legend(loc='upper left',fontsize=10)
fig.suptitle('配对分析使用差值的波动，不把两个条件当成两批独立听者',fontsize=18,fontweight='bold');save(fig,'paired-differences')

def power(count,effect,scale=3):
    critical=stats.t.ppf(.975,count-1);nc=effect*np.sqrt(count)/scale
    return stats.nct.sf(critical,count-1,nc)+stats.nct.cdf(-critical,count-1,nc)
effects=np.linspace(0,3,180)
fig,ax=plt.subplots(figsize=(12,5.7))
for count,color in [(12,B),(24,P),(48,G)]:ax.plot(effects,power(count,effects),label=f'n = {count}',color=color,lw=2)
ax.axhline(.8,color=M,ls=':');ax.axvline(1.5,color=M,ls='--');ax.set(xlabel='指定的真实平均差 δ / dB',ylabel='功效 Pδ（拒绝零均值）',ylim=(0,1.02));ax.legend(title='独立配对数')
fig.suptitle('正态差值模型：σD = 3 dB，双侧 t 检验 α = 0.05',fontsize=18,fontweight='bold');save(fig,'power-and-effect')

fig,axes=plt.subplots(1,2,figsize=(14,5.8))
axes[0].hist(boot,bins=np.arange(-.55,4.61,.1),density=True,color=G,alpha=.65)
axes[0].axvline(mean,color=M,ls='--');axes[0].axvline(boot_ci[0],color=G,ls=':');axes[0].axvline(boot_ci[1],color=G,ls=':')
axes[0].set(title='Bootstrap：有放回抽取 12 个听者差值',xlabel='重抽样均值 / dB',ylabel='密度 / dB⁻¹')
values,counts=np.unique(null,return_counts=True);axes[1].bar(values,counts/len(null),width=.065,color=B,alpha=.65)
axes[1].axvline(mean,color=R,ls='--');axes[1].axvline(-mean,color=R,ls='--')
axes[1].set(title=f'符号翻转：4096 种，双侧尾部比例 {sign_p:.4f}',xlabel='零假设下的平均差 / dB',ylabel='概率质量')
fig.suptitle('估计抽样波动和构造零分布，是两种不同的重采样问题',fontsize=18,fontweight='bold');save(fig,'bootstrap-and-randomization')

rx=np.linspace(20,70,20);rrng=np.random.default_rng(20261104);ry=-8+.08*(rx-45)+rrng.normal(0,1.2,len(rx))
X=np.column_stack([np.ones(len(rx)),rx-45]);coef=np.linalg.lstsq(X,ry,rcond=None)[0];resid=ry-X@coef
rs=np.sqrt(resid@resid/(len(rx)-2));gx=np.linspace(20,70,200);xp=np.column_stack([np.ones(len(gx)),gx-45])
pred=xp@coef;h=np.sum((xp@np.linalg.inv(X.T@X))*xp,axis=1);rc=stats.t.ppf(.975,len(rx)-2)
mean_half=rc*rs*np.sqrt(h);pred_half=rc*rs*np.sqrt(1+h)
fig,ax=plt.subplots(figsize=(12,6))
ax.fill_between(gx,pred-pred_half,pred+pred_half,color=B,alpha=.12,label='单个新听者的点态 95% 预测区间')
ax.fill_between(gx,pred-mean_half,pred+mean_half,color=G,alpha=.3,label='条件均值的点态 95% 置信区间')
ax.plot(gx,pred,color=G,lw=2,label='拟合均值');ax.scatter(rx,ry,color=B,s=30)
ax.set(xlabel='虚构听者年龄 / 岁',ylabel='虚构阈值 / dB SNR');ax.legend(loc='upper left',fontsize=11)
fig.suptitle('均值估计的不确定性，小于同条件下一个新个体的预测不确定性',fontsize=17,fontweight='bold');save(fig,'regression-intervals')

report={'seed_bootstrap':20261102,'differences_dB':d.tolist(),'condition_A_dB_SNR':before.tolist(),'condition_B_dB_SNR':after.tolist(),
 'n':n,'mean_dB':mean,'sample_sd_dB':sd,'se_dB':se,'t_critical':tc,'t_statistic':tstat,'t_p_two_sided':pval,'t_ci_95_dB':ci.tolist(),
 'variance_unbiased':sd**2,'variance_mle':np.var(d),'wilson_60_80':[wilson.low,wilson.high],'posterior_beta':[61,21],
 'posterior_mean':61/82,'posterior_equal_tail_95':post.tolist(),'relative_likelihood_p05':float(np.exp(80*np.log(.5)-logmax)),
 'bootstrap_resamples':20000,'bootstrap_ci_95_dB':boot_ci.tolist(),'bootstrap_sd_dB':float(boot.std(ddof=1)),
 'sign_configurations':len(null),'sign_tail_count':int(np.sum(np.abs(null)>=abs(mean)-1e-12)),'sign_p_two_sided':sign_p,
 'coverage_seed':20261103,'coverage_batches':40,'coverage_count':int(cover.sum()),'coverage_means':means.tolist(),'coverage_halfwidths':half.tolist(),
 'power_sd_dB':3,'power_target_dB':1.5,'power_by_n':{str(k):float(power(k,1.5)) for k in [12,24,32,33,34,48]},
 'sample_size_normal_approx':float(((stats.norm.ppf(.975)+stats.norm.ppf(.8))*3/1.5)**2),
 'regression_seed':20261104,'regression_x':rx.tolist(),'regression_y':ry.tolist(),'regression_coefficients':coef.tolist(),'regression_residual_sd':rs,
 'cluster_m':20,'cluster_K':12,'cluster_rho':.4,'design_effect':8.6,'mean_equivalent_n':240/8.6}
(REC/'calculations.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ['coverage_means','coverage_halfwidths','regression_x','regression_y']},ensure_ascii=True,indent=2))
