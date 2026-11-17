"""Original, synthetic teaching figures; not a clinical map or device interface.

Run: python public/code/cochlear-implant-programming-and-mapping/generate.py
Requires numpy and matplotlib. HEARINGPEDIA_CJK_FONT may specify a CJK font file.
Outputs SVG/PNG plus mapping.csv and results.json beside this script.
"""
import csv
import json
import os
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[1] / 'figures' / 'cochlear-implant-programming-and-mapping'
OUT.mkdir(parents=True, exist_ok=True)
FONT = Path(os.environ.get('HEARINGPEDIA_CJK_FONT', 'C:/Windows/Fonts/msyh.ttc'))
if not FONT.is_file():
    raise FileNotFoundError('Set HEARINGPEDIA_CJK_FONT to an installed CJK font file.')
font_manager.fontManager.addfont(str(FONT))
plt.rcParams.update({'font.family': font_manager.FontProperties(fname=FONT).get_name(),
                     'font.size': 13, 'axes.unicode_minus': False, 'svg.fonttype': 'path',
                     'svg.hashsalt': 'ci-programming-2026', 'figure.facecolor': 'white',
                     'axes.spines.top': False, 'axes.spines.right': False})
BLUE, ORANGE, INK, GREEN = '#226699', '#b95324', '#20334b', '#27806c'


def save(fig, name):
    svg = OUT / f'{name}.svg'
    fig.savefig(svg, metadata={'Date': None})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8')
    fig.savefig(OUT / f'{name}.png', dpi=100)
    plt.close(fig)


fig, ax = plt.subplots(figsize=(12, 6.7))
fig.subplots_adjust(left=.02, right=.98, bottom=.04, top=.97)
ax.set(xlim=(0, 12), ylim=(0, 6.7))
ax.axis('off')
ax.text(.2, 6.15, '从问题出发，用实际表现验证 MAP', fontsize=23, weight='bold', color=INK)
ax.text(.2, 5.55, '临床逻辑示意 · 不是软件操作步骤或固定复诊时间表', color='#52657a')
labels = [('明确问题', '轻声、响度、识别\n日常交流与不适'),
          ('核查装置', '连接与程序版本\n电极及测量条件'),
          ('获取证据', '行为反应\n电学与电生理'),
          ('调整配置', '依据个人证据\n记录参数及理由'),
          ('验证效果', '真实声音与测听\n音质及生活体验')]
xs = np.linspace(.2, 9.8, 5)
for i, (x, (title, body)) in enumerate(zip(xs, labels)):
    ax.add_patch(FancyBboxPatch((x, 2.95), 1.95, 1.65, boxstyle='round,pad=.025',
                               facecolor='#edf3f8', edgecolor='#afc4d5'))
    ax.text(x+.975, 4.18, f'{i+1}  {title}', ha='center', weight='bold', color=INK, fontsize=15)
    ax.text(x+.975, 3.48, body, ha='center', va='center', linespacing=1.7, fontsize=12, color=INK)
    if i < 4:
        ax.add_patch(FancyArrowPatch((x+2.0, 3.8), (xs[i+1]-.05, 3.8),
                                    arrowstyle='-|>', mutation_scale=14, lw=1.5, color=BLUE))
ax.plot([10.775, 10.775, 1.175], [2.9, 1.85, 1.85], color=GREEN, lw=1.6)
ax.add_patch(FancyArrowPatch((1.175, 1.85), (1.175, 2.9), arrowstyle='-|>', mutation_scale=15, color=GREEN, lw=1.6))
ax.text(6, 2.12, '使用与随访反馈：改善了什么？还存在哪些困难？', ha='center', color=GREEN)
ax.text(.2, .8, '技术异常或不适需要先评估；不能把所有问题都归为刺激量不足。', color='#52657a', fontsize=14)
save(fig, '01-workflow')

lower = np.array([18, 22, 16, 25, 20, 28, 21, 17], dtype=float)
upper = np.array([78, 84, 72, 90, 81, 96, 87, 77], dtype=float)
assert np.all(upper > lower)
x = np.linspace(0, 1, 101)
linear = 20+80*x
root = 20+80*np.sqrt(x)
for curve in [linear, root]:
    assert np.isclose(curve[0], 20) and np.isclose(curve[-1], 100)
    assert np.all(np.diff(curve) >= 0)
assert np.isclose(linear[25], 40) and np.isclose(root[25], 60)
with (HERE/'mapping.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['normalized_input', 'linear_output_arbitrary_units', 'sqrt_output_arbitrary_units'])
    writer.writerows(zip(x, linear, root))
fig, axes = plt.subplots(1, 2, figsize=(12, 8))
fig.subplots_adjust(left=.09, right=.97, bottom=.22, top=.78, wspace=.34)
fig.text(.06, .93, '同一组上下限，也可以有不同的输入映射', fontsize=22, weight='bold', color=INK)
fig.text(.06, .86, '全部为任意教学单位；不对应厂商临床标度、电流或听者响度', color='#52657a')
ch = np.arange(1, 9)
axes[0].fill_between(ch, lower, upper, color='#e6eef5')
axes[0].plot(ch, lower, 'o-', color=BLUE, label='下限 T')
axes[0].plot(ch, upper, 's-', color=ORANGE, label='上限 U')
axes[0].set(title='（a）8个虚构通道', xlabel='教学通道编号（无位置含义）',
            ylabel='刺激标度（任意单位）', ylim=(0, 115), xticks=ch)
axes[0].legend(loc='upper left', frameon=False, ncol=2, fontsize=11)
axes[1].plot(x, linear, color=BLUE, label='线性 g(x) = x', lw=2)
axes[1].plot(x, root, '--', color=ORANGE, label='平方根 g(x) = √x', lw=2)
axes[1].plot([.25, .25], [40, 60], ':', color='#52657a')
axes[1].scatter([.25, .25], [40, 60], color=[BLUE, ORANGE], zorder=4)
axes[1].annotate('40', (.25, 40), xytext=(10, -20), textcoords='offset points', color=BLUE)
axes[1].annotate('60', (.25, 60), xytext=(-23, 12), textcoords='offset points', color=ORANGE)
axes[1].set(title='（b）固定 T = 20，U = 100', xlabel='归一化输入 x',
            ylabel='输出 y（任意单位）', xlim=(0, 1), ylim=(0, 115))
axes[1].legend(loc='lower right', frameon=False, fontsize=11)
for ax in axes:
    ax.grid(alpha=.15)
fig.text(.09, .105, '左图：相同数字不等于相同响度。\n右图：x = 0.25时，输出可为40或60；这不预测哪一种更舒适或更清晰。', color=INK, linespacing=1.8)
save(fig, '02-mapping')

current_mA = np.array([.30, .15])
phase_us = np.array([50., 100.])
gap_us = 10.
phase_charge_nC = current_mA*phase_us  # mA * microseconds = nanocoulombs
event_us = 2*phase_us+gap_us
channels, rate_per_second = 6, 1000
occupancy = channels*rate_per_second*event_us*1e-6
assert np.allclose(phase_charge_nC, [15, 15])
assert np.allclose(occupancy, [.66, 1.26])
pulse_coordinates = []
integrated_net_nC = []
for amp, width in zip(current_mA, phase_us):
    times = np.array([-10, 0, 0, width, width, width+gap_us, width+gap_us, 2*width+gap_us, 2*width+gap_us, 225])
    values = np.array([0, 0, -amp, -amp, 0, 0, amp, amp, 0, 0])
    positive_charge = float(np.trapz(np.maximum(values, 0), times))
    negative_charge = float(np.trapz(np.minimum(values, 0), times))
    net_charge = float(np.trapz(values, times))
    assert np.isclose(positive_charge, 15) and np.isclose(negative_charge, -15)
    assert np.isclose(net_charge, 0)
    integrated_net_nC.append(net_charge)
    pulse_coordinates.append((times, values))
results = {'data_type': 'synthetic teaching data; not a clinical recommendation',
           'mapping': {'T': 20, 'U': 100, 'input_example': .25, 'linear_output': 40, 'sqrt_output': 60,
                       'channel_lower_arbitrary_units': lower.tolist(), 'channel_upper_arbitrary_units': upper.tolist()},
           'pulses': {'current_mA': current_mA.tolist(), 'phase_duration_us': phase_us.tolist(),
                      'interphase_gap_us': gap_us, 'charge_per_phase_nC': phase_charge_nC.tolist(),
                      'net_biphasic_charge_nC': integrated_net_nC,
                      'event_duration_us': event_us.tolist()},
           'sequential_timing': {'N': channels, 'r_per_second': rate_per_second, 'occupied_fraction': occupancy.tolist(),
                                 'assumptions': 'non-overlapping rectangular biphasic events; no other overhead'},
           'checks': {'map_endpoints': True, 'map_monotonicity': True, 'equal_phase_charge': True,
                      'balanced_biphasic_charge': True, 'time_budget': True}}
(HERE/'results.json').write_text(json.dumps(results, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
fig = plt.figure(figsize=(12, 8.2))
grid = fig.add_gridspec(2, 2, left=.10, right=.96, top=.78, bottom=.17, hspace=.60, wspace=.25)
axs = [fig.add_subplot(grid[0, 0]), fig.add_subplot(grid[0, 1])]
fig.text(.06, .94, '等电荷，不等于等响，也不等于相同时间占用', fontsize=22, weight='bold', color=INK)
fig.text(.06, .87, '矩形双相脉冲与顺序刺激的数学示例；没有模拟神经响应', color='#52657a')
for i, ax in enumerate(axs):
    amp, width, color = current_mA[i], phase_us[i], [BLUE, ORANGE][i]
    times, values = pulse_coordinates[i]
    ax.plot(times, values, color=color, lw=2)
    ax.fill_between([0, width], -amp, 0, color=color, alpha=.18)
    ax.fill_between([width+gap_us, 2*width+gap_us], 0, amp, color=color, alpha=.18)
    ax.axhline(0, color='#7c8793', lw=.7)
    ax.set(xlim=(-10, 225), ylim=(-.40, .40), xlabel='时间（μs）',
           title=f'（{"a" if i==0 else "b"}）{amp:.2f} mA × {width:.0f} μs = 15 nC')
    ax.grid(alpha=.12)
axs[0].set_ylabel('电流（mA）')
ax = fig.add_subplot(grid[1, :])
ax.barh([1, 0], occupancy*100, height=.46, color=[BLUE, ORANGE])
ax.axvline(100, linestyle='--', color=INK, lw=1)
ax.set(xlim=(0, 145), ylim=(-.65, 1.65), yticks=[1, 0], yticklabels=['50 μs/相', '100 μs/相'],
       xlabel='顺序模型中的时间占用（%）', title='（c）假设 N = 6，r = 1000次/秒，相间隔 = 10 μs')
for y, val in zip([1, 0], occupancy*100):
    ax.text(val+2, y, f'{val:.0f}%', va='center', color=INK)
ax.text(101.5, 1.4, '100%上限', fontsize=11, color=INK)
ax.grid(axis='x', alpha=.12)
fig.text(.10, .045, '长相宽方案在此模型中无法排下；真实设备还有其他时序和电荷约束。', color=INK)
save(fig, '03-pulse-budget')
print(json.dumps(results, ensure_ascii=False, indent=2))
