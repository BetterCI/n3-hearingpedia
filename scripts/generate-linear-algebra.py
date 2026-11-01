"""Reproducible acoustic teaching examples, not measured recordings."""
from pathlib import Path
import json
import wave
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/figures/linear-algebra'
AUDIO = ROOT / 'public/audio/linear-algebra'
REC = ROOT / 'docs/research/linear-algebra-2026-11-01'
for folder in (OUT, AUDIO, REC):
    folder.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'Microsoft YaHei', 'font.size': 12,
                     'svg.fonttype': 'path', 'svg.hashsalt': 'linear-algebra-sound',
                     'axes.unicode_minus': False, 'axes.spines.top': False,
                     'axes.spines.right': False})
BLUE, RED, GREEN = '#22658c', '#b44e37', '#31755e'

def save(fig, name):
    fig.text(0.5, 0.018, 'n³ Hearingpedia · 原创声学教学计算 · 非实测数据', ha='center', color='#526370', fontsize=10)
    fig.savefig(OUT / (name + '.svg'), metadata={'Date': None}, facecolor='white')
    fig.savefig(OUT / (name + '.png'), dpi=100, facecolor='white')
    plt.close(fig)

fs = 8000
n = np.arange(8)
a = np.cos(2*np.pi*1000*n/fs)
b = np.cos(2*np.pi*2000*n/fs)
y = .6*a + .3*b
np.testing.assert_allclose([a@a, b@b, a@b], [4, 4, 0], atol=1e-12)
np.testing.assert_allclose([a@y/4, b@y/4], [.6, .3], atol=1e-12)
np.testing.assert_allclose(y@y, 1.8, atol=1e-12)
phase = np.sin(2*np.pi*1000*n/fs)
np.testing.assert_allclose([a@phase, phase@phase], [0, 4], atol=1e-12)

# The vector calculation uses eight samples. Show two repetitions in the waveform figure.
ns = np.arange(16)
t = np.linspace(0, 15/fs, 1200)
fig, axes = plt.subplots(3, 1, figsize=(14, 8.5), sharex=True)
curves = [(.6*np.cos(2*np.pi*1000*t), .6*np.cos(2*np.pi*1000*ns/fs), BLUE, 'A　1000 Hz：0.6a'),
          (.3*np.cos(2*np.pi*2000*t), .3*np.cos(2*np.pi*2000*ns/fs), GREEN, 'B　2000 Hz：0.3b'),
          (.6*np.cos(2*np.pi*1000*t)+.3*np.cos(2*np.pi*2000*t),
           .6*np.cos(2*np.pi*1000*ns/fs)+.3*np.cos(2*np.pi*2000*ns/fs), RED, 'C　逐点相加：y = 0.6a + 0.3b')]
for ax, (curve, samples, color, title) in zip(axes, curves):
    ax.plot(1000*t, curve, color=color, lw=1.4, alpha=.65)
    ax.vlines(1000*ns/fs, 0, samples, color=color, lw=1)
    ax.scatter(1000*ns/fs, samples, color=color, s=30, zorder=3)
    ax.axhline(0, color='#d3dce1', lw=.8)
    ax.set(ylim=(-1.05, 1.05), ylabel='幅值（无量纲）', title=title)
    ax.grid(axis='x', alpha=.13)
axes[-1].set_xlabel('时间（ms）；圆点为采样值')
fig.suptitle('向量相加，就是把两个声音在相同时刻的样本相加', fontsize=18, fontweight='bold')
fig.tight_layout(rect=(0, .045, 1, .95), h_pad=1.8)
save(fig, 'tone-vectors')

fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True)
width=.34
axes[0].bar(n-width/2, a*y, width, label='1000 Hz 参考 × 混合声：a[n]y[n]', color=BLUE)
axes[0].bar(n+width/2, b*y, width, label='2000 Hz 参考 × 混合声：b[n]y[n]', color=GREEN)
axes[0].set(ylabel='逐点乘积（无量纲）', title='A　每一项都来自同一时刻的两个样本')
axes[0].axhline(0,color='#9ba8af',lw=.8)
axes[0].legend(frameon=False, loc='upper right')
axes[1].plot(n,np.cumsum(a*y),'o-',color=BLUE,label='1000 Hz 参考的累加')
axes[1].plot(n,np.cumsum(b*y),'s-',color=GREEN,label='2000 Hz 参考的累加')
axes[1].annotate('2.4 ÷ 4 = 0.6',xy=(7,2.4),xytext=(5.5,2.67),color=BLUE,fontsize=13)
axes[1].annotate('1.2 ÷ 4 = 0.3',xy=(7,1.2),xytext=(5.5,1.45),color=GREEN,fontsize=13)
axes[1].set(ylabel='累计内积（无量纲）',xlabel='样本序号 n',ylim=(-.1,3.1),xticks=n,title='B　加到最后，再除以参考自身的平方和')
axes[1].legend(frameon=False, loc='upper left')
fig.suptitle('在混合声中寻找一个纯音：逐点相乘，再相加', fontsize=18, fontweight='bold')
fig.tight_layout(rect=(0,.05,1,.94),h_pad=2)
save(fig,'tone-projection')

G=np.array([[1.,.5],[.5,1.]])
G0=np.array([[1.,.5],[1.,.5]])
np.testing.assert_allclose(G@np.array([1.,.2]),[1.1,.7])
np.testing.assert_allclose(np.linalg.solve(G,[1.1,.7]),[1.,.2])
np.testing.assert_allclose(G0@np.array([1.,0.]),G0@np.array([.5,1.]))
assert np.linalg.matrix_rank(G)==2 and np.linalg.matrix_rank(G0)==1
fig, axes=plt.subplots(1,2,figsize=(14,6.5))
u=np.linspace(-.3,1.5,200)
axes[0].plot(u,(1.1-u)/.5,color=BLUE,label='麦克风 1：s1 + 0.5s2 = 1.1')
axes[0].plot(u,.7-.5*u,color=GREEN,label='麦克风 2：0.5s1 + s2 = 0.7')
axes[0].scatter([1],[.2],c=RED,s=65,zorder=4)
axes[0].annotate('唯一交点 (1, 0.2)',xy=(1,.2),xytext=(.45,-.2),color=RED)
axes[0].set_title('A　两个不同约束 → 秩为 2')
axes[1].plot(u,(1-u)/.5,color=BLUE,lw=4,label='麦克风 1：s1 + 0.5s2 = 1')
axes[1].plot(u,(1-u)/.5,'--',color=GREEN,lw=2,label='麦克风 2：同一个约束')
axes[1].scatter([1,.5],[0,1],c=RED,s=60,zorder=4)
axes[1].annotate('(1, 0)',xy=(1,0),xytext=(1.06,.1),color=RED)
axes[1].annotate('(0.5, 1)',xy=(.5,1),xytext=(.57,1.1),color=RED)
axes[1].set_title('B　两个约束重合 → 秩为 1')
for ax in axes:
    ax.set(xlim=(-.2,1.4),ylim=(-.35,1.65),xlabel='声源 1 的瞬时幅值 s1',ylabel='声源 2 的瞬时幅值 s2')
    ax.legend(frameon=False,loc='upper right',fontsize=10)
    ax.grid(alpha=.15)
fig.suptitle('两支麦克风是否给出两个独立约束？',fontsize=18,fontweight='bold')
fig.tight_layout(rect=(0,.06,1,.94),w_pad=3)
save(fig,'microphone-rank')

# Same gain for all audition files; short ramps only at the start and end.
audio_fs=16000
tt=np.arange(int(.7*audio_fs))/audio_fs
ramp=int(.01*audio_fs)
envelope=np.ones(tt.size)
envelope[:ramp]=np.linspace(0,1,ramp)
envelope[-ramp:]=np.linspace(1,0,ramp)
s1=.6*np.cos(2*np.pi*1000*tt)
s2=.3*np.cos(2*np.pi*2000*tt)
for name, audio in [('tone-1000',s1),('tone-2000',s2),('tone-mixture',s1+s2)]:
    pcm=np.rint(.45*envelope*audio*32767).astype('<i2')
    with wave.open(str(AUDIO/(name+'.wav')),'wb') as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(audio_fs); f.writeframes(pcm.tobytes())

x=np.array([1.,2.,0.,-1.])
A=np.column_stack((x,np.r_[0.,x[:-1]]))
observed=np.array([.82,1.89,.63,-.82])
h,_,rank,_=np.linalg.lstsq(A,observed,rcond=None)
residual=observed-A@h
np.testing.assert_allclose(h,[.8,.31],atol=1e-12)
np.testing.assert_allclose(A.T@residual,0,atol=1e-12)
np.testing.assert_allclose(residual@residual,.0013)
# Multichannel PCA with 1/N convention, explicitly used in the article.
s=.6*a; v=.2*b
X=np.column_stack((s+v,s-v))
C=X.T@X/8
np.testing.assert_allclose(C,[[.20,.16],[.16,.20]],atol=1e-12)
evals,_=np.linalg.eigh(C)
np.testing.assert_allclose(evals,[.04,.36],atol=1e-12)
np.testing.assert_allclose(np.linalg.svd(G,compute_uv=False),[1.5,.5])
report={'data_type':'original acoustic teaching calculations',
    'sample_rate_hz':fs,'analysis_samples':8,'tone_1000_vector':a.tolist(),'tone_2000_vector':b.tolist(),
    'mixture':y.tolist(),'inner_products':[float(a@y),float(b@y)],'recovered_coefficients':[float(a@y/4),float(b@y/4)],
    'mixture_squared_norm':float(y@y),'mixture_rms':float(np.sqrt(np.mean(y*y))),
    'mixing_matrix':G.tolist(),'duplicate_matrix_rank':int(np.linalg.matrix_rank(G0)),
    'echo_coefficients':h.tolist(),'echo_residual_sum_squares':float(residual@residual),
    'pca_covariance_1_over_N':C.tolist(),'pca_eigenvalues':evals.tolist(),
    'audio':{'sample_rate_hz':audio_fs,'duration_s':.7,'ramp_s':.01,'common_playback_gain':.45},
    'numpy_version':np.__version__}
(REC/'calculation-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Verified tone projections, phase, norms, source inversion/rank, echo fit, PCA and SVD; generated 3 figures and 3 WAV files.')


# Deep-entry comparisons share the downloadable numerical experiment definitions.
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT/'public/code/linear-algebra'))
from experiments import run_experiments
experiments, data = run_experiments()

fig, axes = plt.subplots(1, 2, figsize=(14, 6.5))
na=np.arange(8)
axes[0].plot(na,np.cos(2*np.pi*1000*na/fs),'o-',color=BLUE,label='1000 Hz')
axes[0].plot(na,np.cos(2*np.pi*1100*na/fs),'s--',color=GREEN,label='1100 Hz')
axes[0].set(xlabel='样本序号 n',ylabel='单位参考幅值',title='A　八点里，两种参考十分相似',xticks=na)
axes[0].legend(frameon=False)
positions=np.arange(2)
for index,(values,label,color) in enumerate([
    (experiments['nonorthogonal'][0]['separate'],'8 点：分别投影',RED),
    (experiments['nonorthogonal'][0]['joint'],'8 点：联合拟合',BLUE),
    (experiments['nonorthogonal'][1]['separate'],'80 点：分别投影',GREEN)]):
    axes[1].bar(positions+(index-1)*.23,values,width=.23,label=label,color=color)
axes[1].scatter(positions,[.6,.3],marker='_',s=160,color='black',zorder=5,label='设定系数')
axes[1].set(xticks=positions,xticklabels=['1000 Hz 系数','1100 Hz 系数'],ylabel='估计系数',ylim=(0,1.1),title='B　分别投影不一定等于分解系数')
axes[1].legend(frameon=False,fontsize=10,loc='upper right')
fig.suptitle('参考不正交时，需要联合求解它们的系数',fontsize=18,fontweight='bold')
fig.tight_layout(rect=(0,.06,1,.94),w_pad=3)
save(fig,'nonorthogonal-tones')

fig, axes = plt.subplots(1, 2, figsize=(14, 7))
indices=np.arange(65);time_ms=indices/fs*1000
axes[0].vlines(time_ms,0,data['h_true'],color=BLUE,lw=3,label='设定响应')
axes[0].plot(time_ms,data['h_estimated'],'x',color=RED,label='带噪训练记录估计',markersize=4)
axes[0].set(xlabel='路径延迟（ms）',ylabel='无量纲增益',title='A　65 个抽头：0、3、7 ms 三条路径')
axes[0].legend(frameon=False,fontsize=10)
show=np.arange(80)
axes[1].plot(show/fs*1000,data['validation_clean'][:80],color=BLUE,lw=1.6,label='独立记录的无噪声输出')
axes[1].scatter(show/fs*1000,data['validation_observed'][:80],color='#9ca7af',s=14,alpha=.7,label='独立带噪观测')
axes[1].plot(show/fs*1000,data['validation_prediction'][:80],'--',color=RED,lw=1.3,label='锁定系数后的预测')
axes[1].set(xlabel='验证片段内的相对时间（ms）',ylabel='输出幅值（无量纲）',title='B　换一段激励，预测仍应成立')
axes[1].legend(frameon=False,fontsize=10,loc='lower left')
fig.suptitle('反射响应辨识：训练拟合之后，用独立记录验证',fontsize=18,fontweight='bold')
fig.tight_layout(rect=(0,.06,1,.94),w_pad=3)
save(fig,'echo-validation')

fig, axes = plt.subplots(1, 2, figsize=(14, 7))
rhos=np.linspace(0,.999,300)
axes[0].plot(rhos,1+rhos,color=BLUE,label='共同模式增益 1 + ρ')
axes[0].plot(rhos,1-rhos,color=GREEN,label='差异模式增益 1 − ρ')
axes[0].axvline(.995,color=RED,ls=':',alpha=.6)
axes[0].set(xlabel='两条声路的交叉混合增益 ρ',ylabel='模式增益',title='A　两路越来越相似，差异越来越弱')
axes[0].legend(frameon=False,fontsize=11)
last=experiments['modal_noise'][-1]
for index,(values,label,color) in enumerate([
    (last['direct'],'直接求解',RED),
    (last['ridge_1e-5'],r'$\lambda=10^{-5}$',BLUE),
    (last['ridge_1e-3'],r'$\lambda=10^{-3}$',GREEN)]):
    axes[1].bar(np.arange(2)+(index-1)*.23,values,width=.23,color=color,label=label)
axes[1].scatter(np.arange(2),[1,.2],color='black',marker='_',s=180,zorder=5,label='教学真值')
axes[1].set(xticks=[0,1],xticklabels=['声源 1','声源 2'],ylabel='估计瞬时幅值',ylim=(-.05,1.45),title='B　同一小误差，三种处理结果（ρ = 0.995）')
axes[1].legend(frameon=False,fontsize=11)
fig.suptitle('正则化压住不稳定的差异模式，也会改变真实差异',fontsize=18,fontweight='bold')
fig.tight_layout(rect=(0,.06,1,.94),w_pad=3)
save(fig,'noise-and-regularization')

phase_audio=.6*np.sin(2*np.pi*1000*tt)+s2
pcm=np.rint(.45*envelope*phase_audio*32767).astype('<i2')
with wave.open(str(AUDIO/'tone-phase-shift.wav'),'wb') as f:
    f.setnchannels(1);f.setsampwidth(2);f.setframerate(audio_fs);f.writeframes(pcm.tobytes())
(REC/'deep-experiment-results.json').write_text(json.dumps(experiments,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Deep comparisons verified: generated 6 current figures and 4 audition files in total.')
