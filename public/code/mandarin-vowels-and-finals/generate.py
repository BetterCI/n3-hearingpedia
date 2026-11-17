"""Original teaching figures; all numerical data are synthetic, not norms.

Run from any directory: python public/code/mandarin-vowels-and-finals/generate.py
Requires numpy and matplotlib. Set HEARINGPEDIA_CJK_FONT to a CJK font file if
Microsoft YaHei is unavailable. SVG text is embedded as paths for portability.
"""
import csv
import json
import os
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[1] / 'figures' / 'mandarin-vowels-and-finals'
OUT.mkdir(parents=True, exist_ok=True)
font_path = Path(os.environ.get('HEARINGPEDIA_CJK_FONT', 'C:/Windows/Fonts/msyh.ttc'))
if not font_path.is_file():
    raise FileNotFoundError('Set HEARINGPEDIA_CJK_FONT to an installed CJK font file.')
font_manager.fontManager.addfont(str(font_path))
plt.rcParams.update({'font.family': font_manager.FontProperties(fname=font_path).get_name(),
                     'font.size': 14, 'axes.unicode_minus': False, 'svg.fonttype': 'path',
                     'figure.facecolor': 'white', 'axes.spines.top': False,
                     'axes.spines.right': False, 'svg.hashsalt': 'mandarin-vowels-2026'})
BLUE, ORANGE, INK, GREEN = '#226699', '#b95324', '#20334b', '#27806c'


def save(fig, name):
    svg = OUT / f'{name}.svg'
    fig.savefig(svg, metadata={'Date': None})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8')
    fig.savefig(OUT / f'{name}.png', dpi=100)
    plt.close(fig)


fig, ax = plt.subplots(figsize=(12, 6.4))
fig.subplots_adjust(left=.025, right=.975, bottom=.04, top=.97)
ax.set(xlim=(0, 12), ylim=(0, 6))
ax.axis('off')
ax.text(.2, 5.65, '从完整音节到韵母内部', fontsize=23, weight='bold', color=INK)
ax.text(.2, 5.17, '结构示意 · 拼音分析形式 · 色块宽度不表示时长', color='#52657a')
xs = [2.1, 4.05, 6.0, 7.95, 9.9]
headers = ['声母', '介音 / 韵头', '韵腹', '韵尾', '声调']
for x, label in zip(xs, headers):
    ax.text(x+.75, 4.55, label, ha='center', weight='bold', color=INK)
rows = [('妈 mā', 'm', '—', 'a', '—', '阴平'),
        ('瓜 guā', 'g', 'u', 'a', '—', '阴平'),
        ('关 guān', 'g', 'u', 'a', 'n', '阴平'),
        ('光 guāng', 'g', 'u', 'a', 'ng', '阴平')]
for row, values in enumerate(rows):
    y = 3.65 - row*.78
    ax.text(.2, y+.27, values[0], va='center', fontsize=18, color=INK)
    for j, (x, label) in enumerate(zip(xs, values[1:])):
        fill = '#e7eef5' if j == 0 else '#e6f3ef' if j < 4 else '#fff0df'
        ax.add_patch(FancyBboxPatch((x, y), 1.5, .55, boxstyle='round,pad=.025',
                                   edgecolor='none', facecolor=fill))
        ax.text(x+.75, y+.275, label, va='center', ha='center', fontsize=18, color=INK)
ax.plot([4.05, 9.45], [.85, .85], color=GREEN, lw=2)
ax.text(6.75, .45, '韵母：介音 + 韵腹 + 韵尾（有些位置可以空缺）', ha='center', color=GREEN)
save(fig, '01-structure')

# Deliberately simple anchors; these are NOT estimates from participants.
anchors = {'衣': (300., 2400.), '鱼': (300., 1900.),
           '乌': (350., 800.), '阿': (800., 1300.)}
fig, ax = plt.subplots(figsize=(12, 7.6))
fig.subplots_adjust(left=.12, right=.94, bottom=.20, top=.82)
fig.text(.08, .93, '四个构造锚点的 F1–F2 空间', fontsize=23, weight='bold', color=INK)
fig.text(.08, .87, '教学示意，不是真实说话人数据，不用于判断发音是否达标', color='#52657a')
for label, (f1, f2) in anchors.items():
    ax.scatter(f2, f1, s=130, color=BLUE, zorder=3)
    ax.annotate(f'{label}  ({int(f1)}, {int(f2)})', (f2, f1), xytext=(12, -24),
                textcoords='offset points', color=INK, fontsize=16)
ax.set(xlim=(2800, 400), ylim=(950, 150), xlabel='F2 (Hz)   ← 数值向左增大',
       ylabel='F1 (Hz)   数值向下增大 →')
ax.grid(alpha=.17)
fig.text(.12, .07, '括号内依次为 F1、F2；元音位置受舌形、唇形及声道尺度共同影响。', color='#52657a')
save(fig, '02-formant-space')

t = np.linspace(0, 1, 11)
a = np.column_stack((750-400*t, 1200+1000*t))
b = a[::-1].copy()
duration = {'A': .20, 'B': .30}
lengths = {key: float(np.linalg.norm(np.diff(v, axis=0), axis=1).sum())
           for key, v in [('A', a), ('B', b)]}
assert np.allclose(a[5], b[5])
assert np.allclose(np.diff(a, axis=0), -np.diff(b, axis=0))
assert np.isclose(lengths['A'], lengths['B'])
assert np.isclose(lengths['A'], np.linalg.norm(a[-1]-a[0]))
with (HERE / 'trajectories.csv').open('w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['trajectory', 'normalized_time', 'time_seconds', 'F1_Hz', 'F2_Hz'])
    for key, values in [('A', a), ('B', b)]:
        for ti, (f1, f2) in zip(t, values):
            writer.writerow([key, round(float(ti), 4), round(float(ti)*duration[key], 4), f1, f2])
results = {'data_type': 'synthetic teaching example; no participant measurements',
           'samples_per_trajectory': len(t), 'anchors_F1_F2_Hz': anchors,
           'midpoint_F1_F2_Hz': a[5].tolist(), 'path_length_Hz': lengths,
           'duration_seconds': duration,
           'mean_path_rate_Hz_per_second': {k: lengths[k]/duration[k] for k in lengths},
           'checks': {'same_midpoint': True, 'opposite_direction': True,
                      'same_path_length': True, 'length_equals_endpoint_distance': True}}
(HERE / 'results.json').write_text(json.dumps(results, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
fig, axes = plt.subplots(2, 1, figsize=(12, 8.4), sharex=True)
fig.subplots_adjust(left=.12, right=.95, bottom=.21, top=.80, hspace=.36)
fig.text(.08, .94, '相同中点与路径长度，仍可有不同方向和速度', fontsize=23, weight='bold', color=INK)
fig.text(.08, .88, '两条线性轨迹的数学构造；A、B不对应指定的真实韵母', color='#52657a')
for i, ax in enumerate(axes):
    ax.plot(t, a[:, i], 'o-', label='A：0.20 s', color=BLUE, lw=2)
    ax.plot(t, b[:, i], 's--', label='B：0.30 s', color=ORANGE, lw=2)
    ax.axvline(.5, color='#708090', lw=1, alpha=.5)
    ax.set(ylabel=f'F{i+1} (Hz)', xlim=(-.02, 1.02))
    ax.grid(alpha=.17)
    ax.annotate(f'中点 {a[5, i]:.0f} Hz', (.5, a[5, i]), xytext=(15, 14),
                textcoords='offset points', color=INK,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .9, 'pad': 2})
axes[0].legend(loc='upper right', bbox_to_anchor=(1, 1.24), ncol=2, frameon=False)
axes[1].set_xlabel('归一化时间（0 = 区间起点，1 = 区间终点）')
fig.text(.12, .085, f"路径长度：A = B ≈ {lengths['A']:.1f} Hz\n平均路径变化率：A ≈ {lengths['A']/.2:.0f} Hz/s；B ≈ {lengths['B']/.3:.0f} Hz/s", color=INK)
save(fig, '03-trajectories')
print(json.dumps(results, ensure_ascii=False, indent=2))
