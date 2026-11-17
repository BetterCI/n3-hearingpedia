"""Reproducible synthetic ridge-decoding lesson, NOT measured EEG or a benchmark.

Run: python public/code/auditory-attention-decoding/generate.py
Requires numpy and matplotlib; HEARINGPEDIA_CJK_FONT selects a CJK font file.
Independent trials are split BEFORE lag construction and model selection.
The future EEG lags make this an offline example with 250 ms look-ahead.
"""
import csv
import json
import os
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[1] / 'figures' / 'auditory-attention-decoding'
OUT.mkdir(parents=True, exist_ok=True)
font = Path(os.environ.get('HEARINGPEDIA_CJK_FONT', 'C:/Windows/Fonts/msyh.ttc'))
if not font.is_file():
    raise FileNotFoundError('Set HEARINGPEDIA_CJK_FONT to an installed CJK font file.')
font_manager.fontManager.addfont(str(font))
plt.rcParams.update({'font.family': font_manager.FontProperties(fname=font).get_name(), 'font.size': 13,
    'axes.unicode_minus': False, 'svg.fonttype': 'path', 'svg.hashsalt': 'attention-decoding-2026',
    'figure.facecolor': 'white', 'axes.spines.top': False, 'axes.spines.right': False})
BLUE, ORANGE, GREEN, INK = '#246697', '#b85525', '#287966', '#24364c'


def save(fig, name):
    p = OUT/f'{name}.svg'
    fig.savefig(p, metadata={'Date': None})
    p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8')
    fig.savefig(OUT/f'{name}.png', dpi=100)
    plt.close(fig)


fig, ax = plt.subplots(figsize=(12, 7.2))
fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.98)
ax.set(xlim=(0, 12), ylim=(0, 7.2)); ax.axis('off')
ax.text(.25, 6.65, '听觉注意力解码：从神经记录到候选选择', fontsize=23, weight='bold', color=INK)
ax.text(.25, 6.07, '包络重建路线示意 · 输出目标估计，不直接生成语音文本', color='#53687b')


def box(x, y, w, h, title, subtitle, color='#edf3f8'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=.025', facecolor=color, edgecolor='#a9bece'))
    ax.text(x+w/2, y+h*.7, title, ha='center', va='center', fontsize=16, weight='bold', color=INK)
    ax.text(x+w/2, y+h*.3, subtitle, ha='center', va='center', fontsize=12)


def arrow(a, b):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=17, color='#6b8296'))


box(.25, 3.7, 2.2, 1.4, '神经记录', '多通道 EEG + 时间同步')
box(3.1, 3.7, 2.3, 1.4, '重建模型', '预处理、时延与权重')
box(6.05, 3.7, 2.3, 1.4, '重建特征', '估计被关注包络')
box(9, 3.7, 2.7, 1.4, '比较与决策', '候选相关、拒判与平滑')
arrow((2.5, 4.4), (3.05, 4.4)); arrow((5.45, 4.4), (6, 4.4)); arrow((8.4, 4.4), (8.95, 4.4))
box(.25, 1.35, 5.15, 1.35, '候选声音 → 包络', '实验原始声轨，或实际系统中的声源估计', '#f5efe8')
arrow((5.45, 2.0), (10.35, 2.0)); arrow((10.35, 2.0), (10.35, 3.65))
ax.text(6.5, 2.35, '候选身份必须持续对应', fontsize=12, color=ORANGE)
ax.text(.25, .55, '训练标签与独立验证决定可信度；选择正确还需经过增强、输出和真实听觉验证。', fontsize=13, color='#53687b')
save(fig, '01-decoding-pipeline')

FS, CHANNELS, SAMPLES, MAX_LAG = 32, 6, 960, 8
SEED = 20261117
train_ids, val_ids, test_ids = list(range(8)), list(range(8, 12)), list(range(12, 20))
assert not(set(train_ids)&set(val_ids) or set(train_ids)&set(test_ids) or set(val_ids)&set(test_ids))
gains = np.array([1., -.8, .6, 1.1, -.7, .9])
delays = np.array([2, 3, 4, 5, 3, 4])
kernel = np.exp(-.5*(np.arange(-6, 7)/2)**2)
kernel /= kernel.sum()


def trial(i):
    rng = np.random.default_rng(np.random.SeedSequence([SEED, i]))
    envelopes = np.stack([np.convolve(rng.normal(size=SAMPLES), kernel, mode='same') for _ in range(2)], axis=1)
    envelopes = (envelopes-envelopes.mean(axis=0))/envelopes.std(axis=0)
    label = i % 2
    eeg = np.zeros((SAMPLES, CHANNELS))
    for c, (g, d) in enumerate(zip(gains, delays)):
        eeg[d:, c] = g*(envelopes[:-d, label]+.25*envelopes[:-d, 1-label])
    eeg += 2.0*rng.normal(size=eeg.shape)
    # X[t] contains EEG[t+lag], never data from another trial.
    x = np.concatenate([eeg[l:SAMPLES-MAX_LAG+l] for l in range(MAX_LAG+1)], axis=1)
    assert np.array_equal(x[:, :CHANNELS], eeg[:SAMPLES-MAX_LAG])
    assert np.array_equal(x[:, -CHANNELS:], eeg[MAX_LAG:])
    return x, envelopes[:SAMPLES-MAX_LAG], label


trials = {i: trial(i) for i in range(20)}
x = np.concatenate([trials[i][0] for i in train_ids])
y = np.concatenate([trials[i][1][:, trials[i][2]] for i in train_ids])
xmean, xstd = x.mean(axis=0), x.std(axis=0)
ymean, ystd = y.mean(), y.std()
x = (x-xmean)/xstd; y = (y-ymean)/ystd
n, p = x.shape
grid = [.001, .01, .1, 1., 10.]
weights, validation = [], []


def predict(i, w):
    return ((trials[i][0]-xmean)/xstd)@w*ystd+ymean


def corr(a, b):
    return float(np.corrcoef(a, b)[0, 1])


for lam in grid:
    lhs, rhs = x.T@x/n+lam*np.eye(p), x.T@y/n
    w = np.linalg.solve(lhs, rhs)
    # Independently solve augmented least squares for the identical objective.
    augmented_w = np.linalg.lstsq(np.vstack([x/np.sqrt(n), np.sqrt(lam)*np.eye(p)]), np.r_[y/np.sqrt(n), np.zeros(p)], rcond=None)[0]
    assert np.allclose(w, augmented_w, atol=1e-10)
    weights.append(w)
    validation.append(float(np.mean([corr(predict(i, w), trials[i][1][:, trials[i][2]]) for i in val_ids])))
best = int(np.argmax(validation)); w = weights[best]
results = []
for i in test_ids:
    estimate = predict(i, w)
    candidate_r = [corr(estimate, trials[i][1][:, k]) for k in range(2)]
    choice = int(np.argmax(candidate_r))
    results.append({'trial': i, 'target': trials[i][2], 'correlations': candidate_r, 'prediction': choice})
assert all(np.isfinite(v) for r in results for v in r['correlations'])
demo_id = test_ids[0]
estimate = predict(demo_id, w)
demo_envelopes = trials[demo_id][1]
with (HERE/'reconstruction.csv').open('w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f); writer.writerow(['time_seconds', 'candidate_1', 'candidate_2', 'reconstruction'])
    writer.writerows(zip(np.arange(len(estimate))/FS, demo_envelopes[:, 0], demo_envelopes[:, 1], estimate))

fig, axes = plt.subplots(2, 1, figsize=(12, 8.2), gridspec_kw={'height_ratios': [1.1, 1]})
fig.subplots_adjust(left=.09, right=.96, bottom=.17, top=.82, hspace=.62)
fig.suptitle('合成记录：先重建，再比较候选包络', x=.05, ha='left', y=.97, fontsize=23, weight='bold', color=INK)
fig.text(.05, .89, '模拟数据 · 独立试次留出 · 不代表实际 EEG 的准确率', color='#53687b')
k = np.arange(FS*8)
axes[0].plot(k/FS, demo_envelopes[k, 0], color=BLUE, lw=1.6, label='候选1（设定目标）')
axes[0].plot(k/FS, demo_envelopes[k, 1], color=ORANGE, lw=1.2, alpha=.7, ls=':', label='候选2')
axes[0].plot(k/FS, estimate[k], color=INK, lw=1.4, ls='--', label='模型重建')
axes[0].set(title='（a）测试试次12的前8秒；相关系数使用整个有效片段', xlabel='时间（秒）', ylabel='特征幅值（任意单位）', xlim=(0, 8), ylim=(-2.6, 3.8))
axes[0].legend(ncol=3, loc='upper right', fontsize=11, frameon=False)
positions = np.arange(len(results))
att = [r['correlations'][r['target']] for r in results]
ign = [r['correlations'][1-r['target']] for r in results]
axes[1].plot(positions, att, 'o-', color=BLUE, label='设定目标')
axes[1].plot(positions, ign, 's--', color=ORANGE, label='另一候选')
axes[1].axhline(0, color='#aab6c0', lw=.8)
axes[1].set(title='（b）8个独立测试试次的候选相关', xlabel='测试试次编号', ylabel='Pearson相关系数', xticks=positions, xticklabels=test_ids, ylim=(-.2, 1.3), yticks=[0, .25, .5, .75, 1])
axes[1].legend(loc='upper right', fontsize=11, frameon=False)
fig.text(.05, .07, '32 Hz，6个合成通道，0—250 ms未来时延；8/4/8试次用于训练/验证/测试。', fontsize=13, color='#53687b')
save(fig, '02-synthetic-reconstruction')

fig, ax = plt.subplots(figsize=(12, 7.4))
fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.98)
ax.set(xlim=(0, 12), ylim=(0, 7.4)); ax.axis('off')
ax.text(.25, 6.85, '划分的单位，决定泛化结论', fontsize=23, weight='bold', color=INK)
ax.text(.25, 6.25, '训练 / 验证 / 测试先按目标隔离，再在各自集合内切窗', color='#53687b')
colors = [BLUE, GREEN, ORANGE]
for i, (c, label) in enumerate(zip(colors, ['训练', '验证：选参数', '测试：最终评价'])):
    ax.add_patch(Rectangle((.4+i*3.7, 5.48), .26, .26, facecolor=c))
    ax.text(.78+i*3.7, 5.61, label, va='center', fontsize=14)
ax.text(.25, 4.72, '（a）同一试次先切窗再混分：即使不重叠，也可能保留试次指纹', fontsize=15, color=INK)
for j in range(12):
    c = colors[[0, 2, 0, 1, 0, 2, 1, 0, 2, 0, 1, 2][j]]
    ax.add_patch(Rectangle((.4+j*.93, 3.8), .86, .5, facecolor=c))
ax.text(6, 3.36, '同一试次T1的片段进入多个集合，不能证明跨试次泛化', ha='center', color=ORANGE, fontsize=14)
ax.text(.25, 2.65, '（b）先留出整个试次：各集合的试次身份不交叉', fontsize=15, color=INK)
for i, (c, label) in enumerate(zip(colors, ['T1、T2、T3', 'T4', 'T5、T6'])):
    ax.add_patch(Rectangle((.4+i*3.8, 1.72), 3.5, .58, facecolor=c))
    ax.text(2.15+i*3.8, 2.01, label, color='white', ha='center', va='center', fontsize=17)
ax.text(.25, .82, '若声称跨被试、跨会话或跨材料，还必须按对应对象进一步隔离。', fontsize=15, color=INK)
ax.text(.25, .28, '概念示意；没有模拟或测量泄漏造成的准确率差值。', fontsize=13, color='#53687b')
save(fig, '03-validation-splits')

report = {'type': 'synthetic teaching example, NOT real EEG', 'seed': SEED, 'fs_hz': FS, 'channels': CHANNELS,
    'samples_per_trial': SAMPLES, 'trial_seconds': SAMPLES/FS, 'effective_samples': SAMPLES-MAX_LAG,
    'future_lags_samples': list(range(MAX_LAG+1)), 'lookahead_ms': MAX_LAG/FS*1000,
    'train_ids': train_ids, 'validation_ids': val_ids, 'test_ids': test_ids, 'ridge_grid': grid,
    'validation_target_correlations': validation, 'selected_lambda': grid[best], 'test_results': results,
    'test_correct': sum(r['target']==r['prediction'] for r in results),
    'checks': ['disjoint trial sets', 'lag endpoints remain within trial', 'ridge agrees with augmented least squares to 1e-10', 'finite test correlations'],
    'limitations': ['envelopes and neural mixtures are synthesized', 'target contribution intentionally exceeds distractor', 'no head or eye artifacts', 'offline look-ahead', 'not fitted to human data']}
(HERE/'results.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'selected_lambda': grid[best], 'first_test': results[0], 'test_correct': report['test_correct'], 'checks': 'passed'}))
