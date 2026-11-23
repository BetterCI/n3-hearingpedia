"""Original teaching models, not an ANSI SII implementation or fitting prescription."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

OUT = Path(__file__).resolve().parent
font = Path('C:/Windows/Fonts/msyh.ttc')
if font.exists():
    font_manager.fontManager.addfont(str(font))
    plt.rcParams['font.family'] = font_manager.FontProperties(fname=str(font)).get_name()
plt.rcParams.update({'font.size': 13, 'svg.fonttype': 'path', 'axes.unicode_minus': False,
                     'axes.spines.top': False, 'axes.spines.right': False})
blue, orange, green = '#287994', '#b26938', '#61815a'

def save(fig, name):
    fig.savefig(OUT / f'{name}.png', dpi=144)
    fig.savefig(OUT / f'{name}.svg')
    path = OUT / f'{name}.svg'
    path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8')
    plt.close(fig)

f = np.arange(4)
threshold = np.array([40, 45, 55, 65])
unaided = np.array([55, 50, 45, 40])
aided = np.array([65, 65, 70, 75])
fig, axes = plt.subplots(2, 1, figsize=(7, 6), sharex=True, sharey=True, layout='constrained')
for ax, levels, name, color in zip(axes, [unaided, aided], ['（a）未助听', '（b）助听'], [orange, blue]):
    ax.fill_between(f, levels-15, levels+15, color=color, alpha=.18, label='设定言语范围')
    ax.plot(f, levels, 'o-', color=color, label='设定平均声级')
    ax.plot(f, threshold, 's--', color='#333333', label='阈值')
    ax.set(title=name, ylabel='频带声级（dB SPL）', ylim=(20, 105), xticks=f)
    ax.grid(axis='y', alpha=.15)
axes[0].legend(loc='upper left', ncol=3, fontsize=9)
axes[1].set(xticklabels=['0.5', '1', '2', '4'], xlabel='示意频带中心（kHz）')
save(fig, 'speech-range')

x = np.linspace(20, 70, 101)
y1, y2 = 50+(x-20), 50+(x-20)/2
fig, ax = plt.subplots(figsize=(7, 5), layout='constrained')
ax.plot(x, y1, color=orange, label='甲：线性段（斜率1）', linewidth=2)
ax.plot(x, y2, color=blue, label='乙：压缩段（斜率0.5）', linewidth=2)
ax.axhline(50, color='#555555', linestyle='--', label='设定输出检测阈')
ax.scatter([20, 60, 60], [50, 90, 70], color=['#333333', orange, blue], zorder=4)
ax.annotate('共同端点 (20, 50)', (20, 50), (23, 43), fontsize=11)
ax.annotate('90', (60, 90), (61, 92), color=orange)
ax.annotate('70', (60, 70), (61, 67), color=blue)
ax.set(xlim=(15, 75), ylim=(38, 110), xlabel='单频带输入（dB SPL）', ylabel='单频带输出（dB SPL）')
ax.legend(loc='upper left', fontsize=10)
ax.grid(alpha=.15)
save(fig, 'input-output')

w = np.array([.2, .5, .3])
fractions = np.array([[.8, .3, 0], [1, .7, .4], [1, .8, 0], [0, .6, 1]])
parts = fractions*w
totals = parts.sum(axis=1)
fig, axes = plt.subplots(2, 1, figsize=(7, 6), layout='constrained')
for ax, rows, names, title in zip(axes, [parts[:2], parts[2:]], [['未助听', '助听'], ['条件甲', '条件乙']],
                                 ['（a）可用程度的改变', '（b）同总分、不同频带组成']):
    left = np.zeros(2)
    for i, color in enumerate([blue, orange, green]):
        ax.barh(names, rows[:, i], left=left, color=color, label=f'频带{i+1}（权重{w[i]:.1f}）')
        for j, value in enumerate(rows[:, i]):
            if value > 0:
                ax.text(left[j]+value/2, j, f'{value:.2f}', ha='center', va='center', color='white', fontsize=11)
        left += rows[:, i]
    for j, total in enumerate(left):
        ax.text(total+.02, j, f'{total:.2f}', va='center')
    ax.invert_yaxis()
    ax.set(title=title, xlim=(0, 1), xlabel='教学加权指数 Q（不是标准SII）')
axes[0].legend(loc='lower right', fontsize=9)
save(fig, 'weighted-access')

assert np.allclose(totals, [.31, .67, .6, .6])
assert np.isclose(totals[1]-totals[0], .36)
assert 40+5+10 == 55 and 65-55 == 10
assert np.allclose([y1[0], y2[0]], [50, 50])
assert np.isclose((50+40)-(50+40/2), 20)
assert aided[-1]-15 < threshold[-1] < aided[-1]
combined = 10*np.log10(2*10**6)
assert np.isclose(combined, 63.0102999566)
validation = {'model':'synthetic teaching examples; NOT ANSI SII', 'weights':w.tolist(),
              'fractions':fractions.tolist(), 'Q':totals.tolist(), 'Q_gain':float(totals[1]-totals[0]),
              'threshold_conversion_dB_SPL':55, 'sensation_margin_dB':10, 'two_60_dB_bands_total':float(combined),
              'same_threshold_outputs_at_60_dB_SPL':[90,70], 'assertions':'passed'}
(OUT/'validation.json').write_text(json.dumps(validation, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(validation, ensure_ascii=False))
