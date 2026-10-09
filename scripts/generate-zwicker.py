"""Original teaching figures; analytic examples, not empirical data or ISO implementation."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/figures/eberhard-zwicker'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'Microsoft YaHei', 'font.size': 13,
                     'svg.fonttype': 'path', 'axes.spines.top': False,
                     'axes.spines.right': False, 'axes.unicode_minus': False})
BLUE, ORANGE, GREEN = '#286a9b', '#bb622d', '#3f8169'

def save(fig, name):
    for ext in ['svg', 'png']:
        fig.savefig(OUT / f'{name}.{ext}', dpi=160, facecolor='white', bbox_inches='tight')
    p = OUT / f'{name}.svg'
    p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines()) + '\n', encoding='utf-8')
    plt.close(fig)

fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
for ax, widelevel, title, note in zip(axes, [30, 40],
        ['A  固定总声压级：均为 60 dB SPL', 'B  固定谱级：扩宽后总级增加'],
        ['100 Hz：谱级 40 dB\n1000 Hz：谱级 30 dB', '100 Hz：总级 60 dB SPL\n1000 Hz：总级 70 dB SPL']):
    ax.plot([1000, 1000, 2000, 2000], [0, widelevel, widelevel, 0], color=ORANGE, lw=3, label='宽带 1000 Hz')
    ax.plot([1450, 1450, 1550, 1550], [0, 40, 40, 0], color=BLUE, lw=3, label='窄带 100 Hz')
    ax.set(xlim=(900, 2100), ylim=(0, 58), xlabel='频率 / Hz', ylabel='谱级 / dB，参考 p0²/Hz', title=title)
    ax.text(0.05, 0.87, note, transform=ax.transAxes, va='top', fontsize=11)
    ax.legend(loc='lower center', fontsize=10)
fig.text(0.5, 0.01, '理想平坦带通噪声；中心 1500 Hz。图示为声学算术，不是实测响度曲线。', ha='center', fontsize=11)
fig.tight_layout(rect=(0, 0.05, 1, 1)); save(fig, 'bandwidth-controls')

def bark(f):
    return 13*np.arctan(0.00076*f) + 3.5*np.arctan((f/7500)**2)
def cbw(f):
    return 25 + 75*(1 + 1.4*(f/1000)**2)**0.69
f = np.geomspace(100, 15500, 600)
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
for ax, values, ylabel in zip(axes, [bark(f), cbw(f)], ['临界带率 z / Bark', '经典临界带宽 Δf / Hz']):
    ax.semilogx(f, values, color=BLUE, lw=2.5)
    ax.set(xlabel='频率 / Hz（对数轴）', ylabel=ylabel)
    ax.set_xticks([100, 500, 1000, 4000, 10000], ['100', '500', '1000', '4000', '10000'])
    ax.tick_params(axis='x', labelsize=10); ax.grid(alpha=0.2)
    for v in [1000, 4000]:
        y = bark(v) if ylabel.startswith('临界带率') else cbw(v)
        ax.plot(v, y, 'o', color=ORANGE)
        ax.annotate(f'{y:.2f}' if ylabel.startswith('临界带率') else f'{y:.0f} Hz', (v, y), xytext=(8, 8), textcoords='offset points', fontsize=11)
fig.suptitle('Zwicker–Terhardt 1980：两个不同的频率函数', fontsize=16)
fig.text(0.5, 0.01, '解析公式计算；不是个体听觉滤波器测量，也不把极端频率外推当作实验证据。', ha='center', fontsize=11)
fig.tight_layout(rect=(0, 0.05, 1, 0.95)); save(fig, 'bark-bandwidth')

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), sharey=True)
for ax, left, right, height, title, color in zip(axes, [7, 4], [9, 12], [1, 0.25],
        ['A  高而窄：1 × 2 = 2 sone', 'B  低而宽：0.25 × 8 = 2 sone'], [BLUE, GREEN]):
    ax.fill_between([left, right], [height, height], color=color, alpha=0.25)
    ax.plot([0, left, left, right, right, 24], [0, 0, height, height, 0, 0], color=color, lw=2.5)
    ax.set(xlim=(0, 24), ylim=(0, 1.25), xlabel='临界带率 z / Bark', title=title)
    ax.set_xticks([0, 4, 8, 12, 16, 20, 24]); ax.grid(alpha=0.15)
axes[0].set_ylabel("特定响度 N′ / (sone/Bark)")
fig.text(0.5, 0.01, '人为指定的两条特定响度轮廓；只演示面积积分，未从声压谱运行响度模型。', ha='center', fontsize=11)
fig.tight_layout(rect=(0, 0.05, 1, 1)); save(fig, 'specific-loudness')

fig, axes = plt.subplots(2, 1, figsize=(11, 6.7), gridspec_kw={'height_ratios': [1.4, 1]})
ax = axes[0]
ax.plot([0.2, 2, 2, 3, 3, 8], [1, 1, 0, 0, 1, 1], color=BLUE, lw=3)
ax.axvspan(2, 3, color=ORANGE, alpha=0.12)
ax.text(2.5, 0.52, '谱凹口', ha='center', color=ORANGE)
ax.set(xlim=(0, 8.2), ylim=(-0.1, 1.35), xlabel='频率 / kHz', ylabel='相对功率谱密度', title='A  诱发刺激：宽带噪声中缺少一段频率能量')
ax.text(0.25, 1.15, '理想示意；凹口 2–3 kHz，不是原论文刺激复现', fontsize=11)
ax = axes[1]
ax.set(xlim=(0, 10), ylim=(0, 2.7), yticks=[0.65, 1.9], yticklabels=['主观报告', '外部刺激'], xticks=[], xlabel='先后顺序（非定量时间轴）')
ax.plot([0.5, 5], [1.9, 1.9], color=BLUE, lw=7, solid_capstyle='butt')
ax.plot([5, 9.5], [1.9, 1.9], color='#aaa', lw=2)
ax.plot([5.2, 8.8], [0.65, 0.65], color=ORANGE, lw=4, ls='--')
ax.axvline(5, color='#666', lw=1, ls=':')
ax.text(2.7, 2.14, '凹口噪声呈现', ha='center', fontsize=11)
ax.text(7.1, 2.14, '噪声停止', ha='center', fontsize=11)
ax.text(7, 1.0, '部分听者报告短暂音调', ha='center', color=ORANGE, fontsize=11)
fig.text(0.5, 0.01, '虚线表示知觉报告，不是麦克风记录的声波；不表示耳鸣诊断或持续时间测量。', ha='center', fontsize=11)
fig.tight_layout(rect=(0, 0.05, 1, 1)); save(fig, 'zwicker-afterimage')

assert abs(60 - 10*np.log10(100) - 40) < 1e-10
assert abs(60 - 10*np.log10(1000) - 30) < 1e-10
assert 1*(9-7) == 0.25*(12-4) == 2
params = {'generator':'scripts/generate-zwicker.py', 'not_empirical_data':True,
    'bandwidth_controls':{'center_hz':1500,'widths_hz':[100,1000],'fixed_total_db_spl':60,'fixed_spectrum_level_db':40,'reference_pressure_pa':20e-6,'rectangular_flat_band_assumption':True},
    'bark_bandwidth':{'formula_source_doi':'10.1121/1.385079','formula_checked_in':'Völk 2015 equations 1 and 9','plotted_hz':[100,15500],'examples':[{ 'frequency_hz':v,'bark':float(bark(v)),'cbw_hz':float(cbw(v))} for v in [1000,4000]]},
    'specific_loudness':{'profiles':[{'z_start':7,'z_end':9,'sone_per_bark':1},{'z_start':4,'z_end':12,'sone_per_bark':0.25}],'total_sone':[2,2],'no_iso_model_run':True},
    'afterimage':{'ideal_notch_hz':[2000,3000],'time_axis':'qualitative sequence only','perceptual_report_not_physical_signal':True}}
R = ROOT / 'docs/research/eberhard-zwicker-2026-10-10'; R.mkdir(parents=True, exist_ok=True)
(R / 'figure-parameters.json').write_text(json.dumps(params, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(params['bark_bandwidth']['examples']))
