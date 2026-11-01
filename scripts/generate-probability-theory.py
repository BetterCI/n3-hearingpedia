"""Original probability/acoustics teaching figures, audio and calculation records."""
from pathlib import Path
import json
import math
import wave
import numpy as np
import scipy
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/figures/probability-theory'
AUDIO = ROOT / 'public/audio/probability-theory'
REC = ROOT / 'docs/research/probability-theory-2026-11-01'
PREVIEW = ROOT / 'artifacts/probability-theory/figures'
for folder in (OUT, AUDIO, REC, PREVIEW):
    folder.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'Microsoft YaHei', 'font.size': 12,
    'svg.fonttype': 'path', 'svg.hashsalt': 'probability-through-sound',
    'axes.unicode_minus': False, 'axes.spines.top': False, 'axes.spines.right': False})
BLUE, RED, GREEN, GRAY = '#22658c', '#b44e37', '#31755e', '#61727d'

def save(fig, name):
    fig.text(.5, .012, 'n³ Hearingpedia · 原创概率与声学教学计算 · 非听者实测',
             ha='center', color=GRAY, fontsize=10)
    fig.tight_layout(rect=(0, .045, 1, .94), h_pad=2.2, w_pad=3)
    svg_path = OUT / f'{name}.svg'
    fig.savefig(svg_path, metadata={'Date': None}, facecolor='white')
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8')
    fig.savefig(PREVIEW / f'{name}.png', dpi=110, facecolor='white')
    plt.close(fig)

# Fixed seeds are independent between examples; figures do not depend on call order.
responses = np.random.default_rng(20261101).binomial(1, .75, 40)
fig, axes = plt.subplots(2, 1, figsize=(14, 8))
axes[0].scatter(np.arange(1, 41), responses, c=np.where(responses, BLUE, RED), s=36)
axes[0].set(xlabel='固定条件下的试次序号', ylabel='单次反应 X', yticks=[0, 1],
    yticklabels=['错误 0', '正确 1'], ylim=(-.25, 1.25), title='（a）一次模拟的 40 个反应，不是 40 个概率')
k = np.arange(41)
axes[1].bar(k, stats.binom.pmf(k, 40, .75), color=BLUE)
axes[1].axvline(30, color=RED, ls='--', label='理论均值 E[K] = 40 × 0.75 = 30')
axes[1].set(xlabel='40 次中正确的次数 K', ylabel='概率 P(K=k)', xlim=(-1, 41),
    title='（b）设想反复重做整套 40 试次，正确总数服从二项分布')
axes[1].legend(frameon=False)
fig.suptitle('一次反应、一次总数与重复实验的分布，是三个层次', fontsize=18, fontweight='bold')
save(fig, 'trials-and-binomial')

sigma = .02
x = np.linspace(-.075, .075, 1400)
pdf = stats.norm.pdf(x, scale=sigma)
fig, axes = plt.subplots(1, 2, figsize=(14, 6.5))
axes[0].plot(x, pdf, color=BLUE)
axes[0].fill_between(x, 0, pdf, where=(np.abs(x) <= .01), color=GREEN, alpha=.35,
    label='−0.01 到 0.01 Pa：面积约 0.3829')
axes[0].set(xlabel='某一固定时刻的噪声声压 X（Pa）', ylabel='概率密度 f(x)（1/Pa）',
    title='（a）曲线高度可以大于 1，面积才是概率')
axes[0].legend(frameon=False, fontsize=10)
for color, style, label in [(BLUE, '-', '独立高斯样本'), (RED, '--', '相关高斯样本：AR(1)，φ=0.9')]:
    lag = np.arange(31)
    # Display theoretical normalized autocovariance rather than estimated correlation.
    curve = np.where(lag == 0, 1., 0.) if color == BLUE else .9**lag
    axes[1].plot(lag, curve, style, color=color, marker='o', ms=3, label=label)
axes[1].set(xlabel='间隔（样本数）', ylabel='归一化自协方差', ylim=(-.05, 1.08),
    title='（b）两者的单点分布都为 N(0,1)，时间结构不同')
axes[1].legend(frameon=False, fontsize=10)
fig.suptitle('幅值分布告诉你多大，时间相关告诉你怎样连在一起', fontsize=18, fontweight='bold')
save(fig, 'density-and-dependence')

prior = np.linspace(.001, .999, 500)
posterior = .8*prior/(.8*prior+.1*(1-prior))
fig, axes = plt.subplots(1, 2, figsize=(14, 6.8))
labels = ['有声且报有声', '有声且报无声', '无声且报有声', '无声且报无声']
values = [160, 40, 80, 720]
axes[0].barh(labels[::-1], values[::-1], color=[GRAY, RED, GRAY, BLUE])
for i, value in enumerate(values[::-1]):
    axes[0].text(value+9, i, str(value), va='center')
axes[0].set(xlabel='每 1000 次试验的期望次数', xlim=(0, 820),
    title='（a）P(有声)=0.2，命中率0.8，虚报率0.1')
axes[1].plot(prior, posterior, color=BLUE)
axes[1].plot(prior, prior, '--', color=GRAY, label='后验 = 先验')
axes[1].scatter([.02, .2], [.8*.02/(.8*.02+.1*.98), 2/3], color=RED, zorder=3)
axes[1].annotate('先验 0.20 → 后验 0.6667', (.2, 2/3), (.28, .56), fontsize=10)
axes[1].annotate('先验 0.02 → 后验 0.1404', (.02, .8*.02/(.8*.02+.1*.98)), (.18, .18), fontsize=10)
axes[1].set(xlabel='有声的先验概率', ylabel='报告有声后，确实有声的概率',
    xlim=(0, 1), ylim=(0, 1), title='（b）保持两种条件反应率不变，只改变先验')
axes[1].legend(frameon=False, loc='lower right')
fig.suptitle('命中率 80%，不等于每次报告有声都有 80% 可信度', fontsize=18, fontweight='bold')
save(fig, 'bayes-and-base-rate')

fs, seconds, trials, noise_sd, amplitude, rho = 16000, .8, 16, .2, .15, .5
t = np.arange(round(fs*seconds))/fs
tone = amplitude*np.sin(2*np.pi*1000*t)
rng = np.random.default_rng(20261103)
independent = rng.normal(0, noise_sd, (trials, len(t)))
shared = rng.normal(0, noise_sd, len(t))
private = rng.normal(0, noise_sd, (trials, len(t)))
correlated = math.sqrt(rho)*shared + math.sqrt(1-rho)*private
signals = {'one-trial': tone+independent[0],
           'average-16': tone+independent.mean(axis=0),
           'shared-average-16': tone+correlated.mean(axis=0)}
ramp = np.ones(len(t))
edge = round(.01*fs)
ramp[:edge] = np.linspace(0, 1, edge)
ramp[-edge:] = np.linspace(1, 0, edge)
gain = .65
audio_records = {}
for name, values in signals.items():
    played = gain*ramp*values
    assert np.max(np.abs(played)) < 1
    pcm = np.rint(32767*played).astype('<i2')
    with wave.open(str(AUDIO / f'{name}.wav'), 'wb') as f:
        f.setparams((1, 2, fs, len(pcm), 'NONE', 'not compressed'))
        f.writeframes(pcm.tobytes())
    audio_records[name] = {'peak_pcm': int(np.max(np.abs(pcm.astype(int)))),
        'noise_rms_before_ramp_and_gain': float(np.sqrt(np.mean((values-tone)**2)))}
fig, axes = plt.subplots(2, 1, figsize=(14, 8))
show = t < .006
axes[0].plot(t[show]*1000, signals['one-trial'][show], color=GRAY, lw=.85, alpha=.7, label='单次含噪记录')
axes[0].plot(t[show]*1000, signals['average-16'][show], color=BLUE, lw=1.3, label='16 次独立噪声记录平均')
axes[0].plot(t[show]*1000, tone[show], '--', color=GREEN, label='共同目标纯音')
axes[0].set(xlabel='时间（ms）', ylabel='幅值（无量纲）', title='（a）对齐的目标保留，独立噪声的平均幅值通常减小')
axes[0].legend(frameon=False, ncol=3, fontsize=10)
m = np.arange(1, 65)
axes[1].plot(m, noise_sd/np.sqrt(m), color=BLUE, label='独立：σ/√M')
axes[1].plot(m, noise_sd*np.sqrt(rho+(1-rho)/m), '--', color=RED, label='共享成分：ρ=0.5')
axes[1].axhline(noise_sd*math.sqrt(rho), color=RED, ls=':', label='共享噪声留下的极限')
axes[1].set(xlabel='平均的记录次数 M', ylabel='平均后噪声的理论标准差',
    title='（b）ρ 是同一时刻、不同记录之间的相关系数')
axes[1].legend(frameon=False, fontsize=10)
fig.suptitle('平均能减小多少噪声，要先问噪声是否独立', fontsize=18, fontweight='bold')
save(fig, 'averaging-and-covariance')

rng = np.random.default_rng(20261104)
fig, axes = plt.subplots(1, 2, figsize=(14, 6.8))
nn = np.arange(1, 2001)
for i in range(4):
    path = np.cumsum(rng.binomial(1, .75, len(nn)))/nn
    axes[0].plot(nn, path, lw=1, alpha=.8)
axes[0].axhline(.75, color=GRAY, ls='--')
axes[0].set(xlabel='已完成的独立试次数 n', ylabel='累计正确率', ylim=(-.02, 1.02),
    title='（a）大数定律：长期靠近，不要求逐步靠近')
for n_value, color, style in [(10, RED, ':'), (40, BLUE, '-'), (160, GREEN, '--')]:
    kk = np.arange(n_value+1)
    z = (kk-.75*n_value)/math.sqrt(n_value*.75*.25)
    dz = 1/math.sqrt(n_value*.75*.25)
    axes[1].plot(z, stats.binom.pmf(kk,n_value,.75)/dz, style, color=color,
        label=f'n={n_value}：概率质量 ÷ 网格间距')
zz=np.linspace(-4,4,500)
axes[1].plot(zz,stats.norm.pdf(zz),color=GRAY,lw=1,alpha=.8,label='标准正态密度')
axes[1].set(xlabel='标准化偏差 Z_n', ylabel='按网格间距缩放的概率质量', xlim=(-4, 4),
    title='（b）中心极限定理：标准化统计量趋近正态')
axes[1].legend(frameon=False, fontsize=9)
fig.suptitle('大数定律与中心极限定理，回答两个不同的问题', fontsize=18, fontweight='bold')
save(fig, 'law-and-limit')

x=np.linspace(-3.5,5,900)
criteria=np.linspace(-4,6,700)
hit=stats.norm.sf(criteria,loc=1.5)
false_alarm=stats.norm.sf(criteria)
fig,axes=plt.subplots(1,2,figsize=(14,6.8))
for mu,color,label in [(0,GRAY,'无声：N(0,1)'),(1.5,BLUE,'有声：N(1.5,1)')]:
    yy=stats.norm.pdf(x,loc=mu)
    axes[0].plot(x,yy,color=color,label=label)
    axes[0].fill_between(x,0,yy,where=x>1,color=color,alpha=.18)
axes[0].axvline(1,color=RED,ls='--',label='判据 c=1：右侧报有声')
axes[0].set(xlabel='内部证据 Z（模型单位）',ylabel='密度',title='（a）曲线重叠，决定命中与虚报的概率')
axes[0].legend(frameon=False,fontsize=10)
axes[1].plot(false_alarm,hit,color=BLUE,label="固定 d′=1.5，移动判据")
axes[1].plot([0,1],[0,1],'--',color=GRAY)
axes[1].scatter([stats.norm.sf(1)],[stats.norm.sf(-.5)],color=RED,zorder=3)
axes[1].annotate('c=1\nF≈0.1587，H≈0.6915',(.1587,.6915),(.32,.52),fontsize=11)
axes[1].set(xlabel='虚报率 F',ylabel='命中率 H',xlim=(0,1),ylim=(0,1),title='（b）ROC 曲线：命中更多时，也可能虚报更多')
axes[1].legend(frameon=False,fontsize=10,loc='lower right')
fig.suptitle('概率分布的尾部面积，把噪声模型连接到检测行为',fontsize=18,fontweight='bold')
save(fig,'detection-and-roc')

xx=np.linspace(-15,15,600)
gamma,lapse,alpha,beta=.5,.02,0.,3.
psi=gamma+(1-gamma-lapse)*stats.logistic.cdf(xx,loc=alpha,scale=beta)
target=.75
threshold=alpha+beta*math.log(((target-gamma)/(1-gamma-lapse))/(1-(target-gamma)/(1-gamma-lapse)))
fig,axes=plt.subplots(1,2,figsize=(14,6.5))
axes[0].plot(xx,psi,color=BLUE)
for val,label in [(gamma,'机会水平 0.50'),(1-lapse,'上限 0.98')]:
    axes[0].axhline(val,color=GRAY,ls='--')
    axes[0].text(-14,val+.012,label,fontsize=10)
axes[0].scatter([0,threshold],[.74,.75],color=RED)
axes[0].annotate('α=0 对应 0.74', (0,.74),(-12,.81),fontsize=11)
axes[0].annotate('75% 阈值 ≈0.250 dB', (threshold,.75),(3,.66),fontsize=11)
axes[0].set(xlabel='信噪比 x（dB，教学坐标）',ylabel='正确概率 ψ(x)',ylim=(.46,1.03),
    title='（a）位置参数不一定就是指定正确率的阈值')
q=np.linspace(.001,.999,700)
for kval,color,label in [(0,GRAY,'40 次全错'),(30,BLUE,'40 次对 30 次'),(40,RED,'40 次全对')]:
    loglike=stats.binom.logpmf(kval,40,q)
    axes[1].plot(q,np.exp(loglike-loglike.max()),color=color,label=label)
axes[1].set(xlabel='候选正确概率 p',ylabel='相对似然（各曲线峰值为1）',
    title='（b）极端结果仍有不确定性；似然曲线不是后验')
axes[1].legend(frameon=False,fontsize=10)
fig.suptitle('正确率曲线需要说明机会水平、上限和阈值定义',fontsize=18,fontweight='bold')
save(fig,'psychometric-and-likelihood')

def wilson(k,n,z=1.959963984540054):
    phat=k/n
    center=(phat+z*z/(2*n))/(1+z*z/n)
    half=z*math.sqrt(phat*(1-phat)/n+z*z/(4*n*n))/(1+z*z/n)
    return center-half,center+half

wilson_interval=wilson(30,40)
credible=stats.beta.ppf([.025,.975],31,11)
fig,axes=plt.subplots(1,2,figsize=(14,6.5))
axes[0].hlines([1,0],[wilson_interval[0],credible[0]],[wilson_interval[1],credible[1]],
    colors=[BLUE,GREEN],lw=5)
axes[0].scatter([.75,31/42],[1,0],c=[BLUE,GREEN],zorder=3)
axes[0].set(yticks=[0,1],yticklabels=['95% 后验可信区间\n点为后验均值','95% Wilson 置信区间\n点为样本正确率'],
    xlabel='固定条件下的正确概率 p',xlim=(.45,1),ylim=(-.65,1.65),
    title='（a）同一份数据，两种区间的解释不同')
axes[1].plot(q,stats.beta.pdf(q,1,1),'--',color=GRAY,label='先验 Beta(1,1)')
axes[1].plot(q,stats.beta.pdf(q,31,11),color=GREEN,label='后验 Beta(31,11)')
axes[1].set(xlabel='正确概率 p',ylabel='密度',title='（b）先验 × 似然，再归一化，得到后验')
axes[1].legend(frameon=False,fontsize=10)
fig.suptitle('40 次对 30 次，不能把 75% 当作没有误差的真值',fontsize=18,fontweight='bold')
save(fig,'estimation-and-uncertainty')

result={
    'nature':'original synthetic teaching calculations, not participant data',
    'versions':{'numpy':np.__version__,'scipy':scipy.__version__,'matplotlib':matplotlib.__version__},
    'seeds':[20261101,20261103,20261104],
    'binomial':{'n':40,'p':.75,'mean':30,'variance':7.5,
        'example_sequence_correct':int(responses.sum()),
        'one_sided_p_at_chance':float(stats.binom.sf(29,40,.5))},
    'normal':{'sd_Pa':.02,'density_at_zero':float(stats.norm.pdf(0,scale=.02)),
        'prob_within_0_01_Pa':float(stats.norm.cdf(.5)-stats.norm.cdf(-.5))},
    'bayes':{'prior_0_2':2/3,'prior_0_02':float(.8*.02/(.8*.02+.1*.98))},
    'averaging':{'noise_sd':noise_sd,'trials':trials,'rho':rho,
        'independent_sd':noise_sd/math.sqrt(trials),
        'shared_sd':noise_sd*math.sqrt(rho+(1-rho)/trials),
        'independent_power_snr_gain_dB':10*math.log10(trials),
        'shared_power_snr_gain_dB':-10*math.log10(rho+(1-rho)/trials)},
    'detection':{'dprime':1.5,'criterion':1,'F':float(stats.norm.sf(1)),
        'H':float(stats.norm.sf(-.5)),'two_interval_correct':float(stats.norm.cdf(1.5/math.sqrt(2)))},
    'psychometric':{'gamma':gamma,'lapse_upper_gap':lapse,'alpha_dB':alpha,'beta_dB':beta,
        'psi_at_alpha':.74,'threshold_at_0_75_dB':threshold},
    'estimation':{'k':30,'n':40,'wilson_95':wilson_interval,
        'prior_beta':[1,1],'posterior_beta':[31,11],'posterior_mean':31/42,'credible_95':credible.tolist()},
    'audio':{'fs_Hz':fs,'duration_s':seconds,'ramp_ms':10,'common_playback_gain':gain,
        'no_individual_normalization':True,'records':audio_records}
}
(REC/'calculations.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
