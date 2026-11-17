"""Original teaching models, NOT human data or clinical age recommendations.

Run from the repository: python public/code/auditory-development-and-sensitive-periods/generate.py
Requires numpy and matplotlib; HEARINGPEDIA_CJK_FONT can override the font path.
The two integrals are checked independently against the analytic erf solution.
"""
import csv
import json
import math
import os
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[1] / 'figures' / 'auditory-development-and-sensitive-periods'
OUT.mkdir(parents=True, exist_ok=True)
font = Path(os.environ.get('HEARINGPEDIA_CJK_FONT', 'C:/Windows/Fonts/msyh.ttc'))
if not font.is_file():
    raise FileNotFoundError('Set HEARINGPEDIA_CJK_FONT to an installed CJK font file')
font_manager.fontManager.addfont(str(font))
plt.rcParams.update({'font.family': font_manager.FontProperties(fname=font).get_name(),
                     'font.size': 14, 'axes.unicode_minus': False, 'svg.fonttype': 'path',
                     'svg.hashsalt': 'auditory-sensitive-period-2026', 'figure.facecolor': 'white',
                     'axes.spines.top': False, 'axes.spines.right': False})
BLUE, ORANGE, GREEN, INK = '#246697', '#b85525', '#287966', '#24364c'


def save(fig, name):
    target = OUT / f'{name}.svg'
    fig.savefig(target, metadata={'Date': None})
    target.write_text('\n'.join(s.rstrip() for s in target.read_text(encoding='utf-8').splitlines()) + '\n', encoding='utf-8')
    fig.savefig(OUT / f'{name}.png', dpi=100)
    plt.close(fig)


fig, ax = plt.subplots(figsize=(12, 7.2))
fig.subplots_adjust(left=.02, right=.98, top=.98, bottom=.02)
ax.set(xlim=(0, 12), ylim=(0, 7.2))
ax.axis('off')
ax.text(.25, 6.65, '敏感期研究：输入变了，哪一层也改变了？', fontsize=23, weight='bold', color=INK)
ax.text(.25, 6.08, '概念框架 · 没有统一年龄刻度或因果效应量', color='#55667a')
boxes = [('声音输入', '可听度与模式\n起点、时长与质量', '声学与设备验证'),
         ('回路组织', '连接与选择性\n兴奋、抑制与协作', '细胞与回路测量'),
         ('神经响应', '潜伏期与形态\n对声音变化的响应', '电生理与脑成像'),
         ('实际功能', '辨别、语言与定位\n日常交流和参与', '行为与生活评价')]
for i, (title, body, measure) in enumerate(boxes):
    x = .25 + i * 3
    ax.add_patch(FancyBboxPatch((x, 3.2), 2.5, 2.2, boxstyle='round,pad=.025', facecolor='#edf3f8', edgecolor='#a9c0d0'))
    ax.text(x+1.25, 4.91, title, ha='center', fontsize=19, weight='bold', color=INK)
    ax.text(x+1.25, 4.12, body, ha='center', va='center', linespacing=1.7)
    ax.text(x+1.25, 2.72, measure, ha='center', color=BLUE, fontsize=15)
    if i < 3:
        ax.add_patch(FancyArrowPatch((x+2.57, 4.25), (x+2.95, 4.25), arrowstyle='-|>', mutation_scale=16, color='#74899b'))
ax.add_patch(FancyBboxPatch((.25, .85), 11.5, 1.13, boxstyle='round,pad=.025', facecolor='#f4f1e9', edgecolor='#cbbd9d'))
ax.text(6, 1.48, '共同解释条件：发育阶段  ·  既往经验  ·  物种与病因  ·  测量任务', ha='center', va='center', fontsize=17, color=INK)
ax.text(.25, .25, '箭头表示需要检验的联系；某一层变化不能自动替代下一层的结论。', fontsize=13, color='#55667a')
save(fig, '01-evidence-levels')


def weight(t):
    return .2 + .8 * np.exp(-((t - 3) / 2)**2)


def analytic(a, b):
    return .2 * (b-a) + .8 * math.sqrt(math.pi) * (math.erf((b-3)/2)-math.erf((a-3)/2))


intervals = [(2., 4.), (6., 8.)]
integrals = []
for a, b in intervals:
    grid = np.linspace(a, b, 20001)
    value = float(np.trapz(weight(grid), grid))
    assert math.isclose(value, analytic(a, b), abs_tol=1e-8)
    assert math.isclose(float(np.trapz(np.ones_like(grid), grid)), 2., abs_tol=1e-12)
    integrals.append(value)
assert integrals[0] > integrals[1] > 0
t = np.linspace(0, 10, 1001)
assert np.min(weight(t)) >= .2 and np.max(weight(t)) <= 1
with (HERE/'model.csv').open('w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['synthetic_time_not_human_age', 'weight'])
    writer.writerows(zip(t, weight(t)))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 7.6), gridspec_kw={'width_ratios': [1.25, 1]})
fig.subplots_adjust(left=.09, right=.97, bottom=.27, top=.78, wspace=.38)
fig.suptitle('相同输入量，不同的经验时点', x=.05, ha='left', y=.96, fontsize=23, weight='bold', color=INK)
fig.text(.05, .88, '纯教学权重模型 · 时间轴不对应人类年龄 · 不预测疗效', color='#55667a')
ax1.plot(t, weight(t), color=INK, lw=2.5, label='敏感权重 w(t)')
for (a, b), color, label in zip(intervals, [BLUE, ORANGE], ['甲：t = 2 至 4', '乙：t = 6 至 8']):
    x = np.linspace(a, b, 501)
    ax1.fill_between(x, 0, weight(x), color=color, alpha=.23)
    ax1.plot([a, a, b, b], [0, 1, 1, 0], color=color, ls='--', lw=1.8, label=label)
ax1.set(title='（a）权重与输入区间', xlabel='示意时间 t（任意单位）', ylabel='权重 / 输入强度（无量纲）', xlim=(0, 10), ylim=(0, 1.5), yticks=[0, .5, 1])
ax1.legend(loc='upper right', fontsize=11, frameon=False)
x = np.arange(2)
bars1 = ax2.bar(x-.18, [2, 2], .34, label='累计输入 D', color='#aebac5')
bars2 = ax2.bar(x+.18, integrals, .34, label='加权输入 E', color=[BLUE, ORANGE])
for bar in [*bars1, *bars2]:
    ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+.06, f'{bar.get_height():.3f}', ha='center', fontsize=12)
ax2.set(title='（b）量相等，加权量不同', xticks=x, xticklabels=['方案甲', '方案乙'], ylabel='积分值（教学单位）', ylim=(0, 2.8))
ax2.legend(loc='upper right', frameon=False, fontsize=12)
fig.text(.05, .14, 'w(t) = 0.2 + 0.8 exp[−((t − 3)/2)²]；输入区间内 q(t) = 1，其余为 0。', fontsize=13)
fig.text(.05, .08, '如果 w(t) 恒为 1，两种方案的加权量均为 2；本图的差异来自明确设定的权重。', fontsize=13, color='#55667a')
save(fig, '02-weighted-experience')

starts = np.array([1., 3.])
age_fixed = np.array([6., 6.])
experience_a = age_fixed-starts
experience_b = np.array([3., 3.])
age_b = starts+experience_b
scores_a = 10*age_fixed+20*experience_a
scores_b = 10*age_b+20*experience_b
assert np.array_equal(scores_a, [160, 120])
assert np.array_equal(scores_b, [100, 120])
assert np.allclose(age_fixed, starts+experience_a)
assert np.allclose(age_b, starts+experience_b)
design = {'fixed_test_age': {'start_age': starts.tolist(), 'test_age': age_fixed.tolist(), 'experience_years': experience_a.tolist(), 'output': scores_a.tolist()},
          'fixed_experience': {'start_age': starts.tolist(), 'test_age': age_b.tolist(), 'experience_years': experience_b.tolist(), 'output': scores_b.tolist()}}
fig, axes = plt.subplots(1, 2, figsize=(12, 7.6), sharey=True)
fig.subplots_adjust(left=.09, right=.97, bottom=.29, top=.78, wspace=.25)
fig.suptitle('没有敏感期项，也能出现开始年龄关联', x=.05, ha='left', y=.96, fontsize=23, weight='bold', color=INK)
fig.text(.05, .88, '虚构算例：Y = 10A + 20H，且 A = I + H；两幅图共用纵轴', color='#55667a')
for ax, ys, ages, exp, title in zip(axes, [scores_a, scores_b], [age_fixed, age_b], [experience_a, experience_b], ['（a）固定测试年龄 A = 6 岁', '（b）固定经验时长 H = 3 年']):
    bars = ax.bar([0, 1], ys, width=.5, color=[BLUE, ORANGE])
    for i, bar in enumerate(bars):
        ax.text(i, ys[i]+4, f'{ys[i]:.0f}', ha='center', fontsize=17, weight='bold', color=INK)
    ax.set(title=title, xticks=[0, 1], xticklabels=[f'I = 1 岁\nA = {ages[0]:.0f} 岁，H = {exp[0]:.0f} 年', f'I = 3 岁\nA = {ages[1]:.0f} 岁，H = {exp[1]:.0f} 年'], ylim=(0, 185))
    ax.tick_params(axis='x', labelsize=12)
axes[0].set_ylabel('模型输出 Y（任意单位）')
fig.text(.05, .14, 'I：输入开始年龄；A：测试年龄；H：开始后的时间。系数 10 与 20 均为教学设定。', fontsize=13)
fig.text(.05, .08, '不含实际儿童数据、噪声或疗效估计；关联方向随比较口径改变。', fontsize=13, color='#55667a')
save(fig, '03-age-experience')

(HERE/'results.json').write_text(json.dumps({'data_type': 'synthetic teaching model, not clinical data',
    'weight': {'baseline': .2, 'amplitude': .8, 'center': 3, 'scale': 2, 'time_unit': 'arbitrary, NOT human age'},
    'intervals': intervals, 'raw_input': [2, 2], 'weighted_input': integrals,
    'analytic_integrals': [analytic(a, b) for a, b in intervals], 'design_comparison': design,
    'checks': ['numeric quadrature matches independent erf integral within 1e-8', 'equal raw input and positive later weight', 'both age identities', 'comparison outputs 160/120 and 100/120']}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'weighted_input': integrals, 'figures': 3, 'checks': 'passed'}))
