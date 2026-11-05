"""Original, deterministic WDRC teaching figures; not a hearing-aid fitting program.

Run: python public/code/wide-dynamic-range-compression/demo.py
Requires Python 3, numpy, matplotlib. Figures use Microsoft YaHei on Windows;
Noto Sans CJK SC is a fallback. No audio, patient data, or random simulation.
"""
from pathlib import Path
import json
import platform
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'public/figures/wide-dynamic-range-compression'
OUT.mkdir(parents=True, exist_ok=True)
fonts = {f.name for f in font_manager.fontManager.ttflist}
font = next((f for f in ['Microsoft YaHei', 'Noto Sans CJK SC', 'SimHei'] if f in fonts), None)
if not font:
    raise RuntimeError('Install a Chinese font: Microsoft YaHei or Noto Sans CJK SC')
plt.rcParams.update({'font.family': font, 'font.size': 12, 'axes.unicode_minus': False,
                     'svg.fonttype': 'path', 'svg.hashsalt': 'wdrc-20261106',
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.titleweight': 'bold', 'axes.labelcolor': '#243746',
                     'text.color': '#243746', 'axes.edgecolor': '#8997a2',
                     'lines.linewidth': 2.5, 'figure.facecolor': 'white'})
BLUE, ORANGE, GREEN, GRAY = '#2563a6', '#cc641b', '#16836b', '#72818c'

def output_level(level, ratio=2.0, knee=50.0, gain=30.0):
    """Steady-state, one hard knee; same acoustic reference at input/output."""
    level = np.asarray(level, dtype=float)
    return np.where(level <= knee, level + gain, knee + gain + (level-knee)/ratio)

def target_gain(level, ratio=2.0):
    return output_level(level, ratio=ratio)-level

def smooth_gain(level, attack_ms=5.0, release_ms=50.0, dt_ms=0.1):
    """First-order smoothing in dB gain, NOT a standardized attack/release test.

    Input is an already known level trajectory; no waveform level detector.
    State initially equals the first steady-state gain. State is sampled at
    each interval start, then advanced toward that interval's target gain.
    """
    target = target_gain(level)
    gain = np.empty(len(level))
    state = float(target[0])
    for i, wanted in enumerate(target):
        gain[i] = state
        tau = attack_ms if wanted < state else release_ms
        a = np.exp(-dt_ms/tau)
        state = a*state+(1-a)*wanted
    return gain

def style(ax):
    ax.grid(alpha=0.18)
    ax.set_axisbelow(True)

def save(fig, name):
    fig.savefig(OUT/f'{name}.svg', metadata={'Date': None}, facecolor='white')
    fig.savefig(OUT/f'{name}.png', dpi=140, facecolor='white')
    p = OUT/f'{name}.svg'
    p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8')
    plt.close(fig)

# Figure 1: two different slopes: output and gain.
x = np.linspace(30, 100, 701)
fig, axs = plt.subplots(1, 2, figsize=(12, 5.2), layout='constrained')
for ratio, color, ls in [(1, GRAY, ':'), (2, BLUE, '-'), (3, ORANGE, '--')]:
    axs[0].plot(x, output_level(x, ratio), color=color, ls=ls, label=f'{ratio}:1')
    axs[1].plot(x, target_gain(x, ratio), color=color, ls=ls, label=f'{ratio}:1')
for ax in axs:
    ax.axvline(50, color=GRAY, lw=1, ls='--')
    ax.set_xlabel('输入声级（dB SPL）')
    ax.legend(title='压缩比', loc='best', frameon=False)
    style(ax)
axs[0].set(title='（a）输出仍随输入上升', ylabel='稳态输出声级（dB SPL）', ylim=(55, 135))
axs[1].set(title='（b）压缩区的增益随输入下降', ylabel='稳态增益（dB）', ylim=(-6, 35))
fig.suptitle('同一拐点 50 dB SPL；拐点以下增益 30 dB；未加限幅器', fontsize=14)
save(fig, '01-static-curve')

# Figure 2: known-level step, with two release time constants.
dt = 0.1
t = np.arange(0, 1600+dt/2, dt)
level = np.where((t>=200)&(t<600), 80.0, 50.0)
fast = smooth_gain(level, release_ms=50, dt_ms=dt)
slow = smooth_gain(level, release_ms=500, dt_ms=dt)
fig, axs = plt.subplots(3, 1, figsize=(12, 8), sharex=True, layout='constrained')
axs[0].plot(t, level, color=GRAY)
axs[0].set(title='（a）已知输入声级：50 → 80 → 50 dB SPL', ylabel='输入（dB SPL）')
for gain, color, ls, label in [(fast, BLUE, '-', '恢复 τ=50 ms'), (slow, ORANGE, '--', '恢复 τ=500 ms')]:
    axs[1].plot(t, gain, color=color, ls=ls, label=label)
    axs[2].plot(t, level+gain, color=color, ls=ls, label=label)
axs[1].plot(t, target_gain(level), color=GRAY, lw=1.5, ls=':', label='稳态目标')
axs[1].set(title='（b）同一目标增益，不同恢复速度', ylabel='增益（dB）')
axs[1].legend(ncol=3, frameon=False, loc='lower right')
axs[2].plot(t, output_level(level), color=GRAY, lw=1.5, ls=':')
axs[2].set(title='（c）输出存在暂态超调与弱声欠放大', ylabel='输出（dB SPL）', xlabel='时间（ms）')
axs[2].annotate('未模拟输出限制', xy=(200, 110), xytext=(290, 109), fontsize=11,
                arrowprops={'arrowstyle': '->', 'color': GRAY})
for ax in axs:
    style(ax)
    ax.axvline(600, color=GRAY, lw=1, ls=':')
fig.suptitle('增益域教学模型：CR=2:1；启动指数时间常数 τ=5 ms', fontsize=14)
save(fig, '02-dynamics')

# Figure 3: two ideal nonoverlapping bands. No modeled vowel/filter bank.
bands = np.array([70., 50.])
wide_level = 10*np.log10(np.sum(10**(bands/10)))
common_gain = target_gain(wide_level)
shared = bands+common_gain
independent = output_level(bands)
fig, axs = plt.subplots(1, 3, figsize=(12, 5.3), sharey=True, layout='constrained')
for ax, values, title, contrast in zip(axs, [bands, shared, independent],
        ['（a）输入', '（b）同一宽带增益', '（c）两带独立压缩'], [20,20,10]):
    ax.bar([0,1], values, width=.55, color=[BLUE, ORANGE], hatch=['', '//'])
    for j, v in enumerate(values):
        ax.text(j, v+1.5, f'{v:.2f}', ha='center', fontsize=13)
    ax.set(xticks=[0,1], xticklabels=['频带 A','频带 B'], ylim=(0,105), title=title)
    ax.text(.5,.94,f'带间声级差 {contrast} dB', transform=ax.transAxes, ha='center', fontsize=12)
    ax.set_ylabel('带内声级（dB SPL）' if ax is axs[0] else '')
    style(ax)
fig.suptitle('理想稳态示例：两带均用 K=50 dB SPL、低声级增益30 dB、CR=2:1', fontsize=14)
save(fig, '03-spectral-contrast')

# Figure 4: two equal-duration steady segments, uncorrelated source powers.
speech_power, noise_power = np.array([100., 1.]), np.ones(2)
mixture_level = 50+10*np.log10(speech_power+noise_power)
gain_db = target_gain(mixture_level)
power_gain = 10**(gain_db/10)
snr_in = 10*np.log10(speech_power.sum()/noise_power.sum())
snr_out = 10*np.log10(np.dot(power_gain,speech_power)/np.dot(power_gain,noise_power))
fig, axs = plt.subplots(1, 2, figsize=(12, 5.5), sharey=True, layout='constrained')
for ax, extra, title in zip(axs, [np.zeros(2), gain_db], ['（a）输入', '（b）对混合声使用共同增益']):
    ax.plot([0,1], 50+10*np.log10(speech_power)+extra, color=BLUE, marker='o', label='目标分量')
    ax.plot([0,1], 50+10*np.log10(noise_power)+extra, color=ORANGE, marker='s', ls='--', label='噪声分量')
    ax.set(xticks=[0,1], xticklabels=['片段 1','片段 2'], xlim=(-.35,1.35), ylim=(43,98), title=title)
    ax.set_ylabel('分量声级（dB SPL）' if ax is axs[0] else '')
    ax.legend(loc='upper right', frameon=False)
    style(ax)
axs[0].text(.02,.04,f'全程 SNR：{snr_in:.2f} dB', transform=axs[0].transAxes, fontsize=14)
axs[1].text(.02,.04,f'全程 SNR：{snr_out:.2f} dB', transform=axs[1].transAxes, fontsize=14)
fig.suptitle('两个等时长稳态片段；片段内 SNR 均不变，全程 SNR 却改变', fontsize=14)
save(fig, '04-mixture-snr')

# Independent identities / numerical checks, not only smoke checks.
assert np.allclose(output_level(np.array([40.,50.,60.,80.]),2), [70,80,85,95])
assert abs(output_level(50-1e-8)-output_level(50+1e-8)) < 2e-8
assert np.all(np.diff(output_level(x))>0)
h=1e-4
assert abs((output_level(70+h)-output_level(70-h))/(2*h)-.5)<1e-8
assert np.allclose(output_level(x)-x, target_gain(x))
assert abs((output_level(80)-output_level(60))-10)<1e-10
assert abs((shared[0]-shared[1])-20)<1e-10
assert abs((independent[0]-independent[1])-10)<1e-10
step_idx = int(200/dt)
after_tau = int(205/dt)
assert abs(fast[after_tau]-(15+15/np.e))<1e-9
restore_idx=int(650/dt)
assert abs(fast[restore_idx]-(30-15/np.e))<1e-9
assert np.allclose((speech_power*power_gain)/(noise_power*power_gain), speech_power/noise_power)
assert snr_out < snr_in
assert abs(10*np.log10((100*speech_power).sum()/(100*noise_power).sum())-snr_in)<1e-10
report = {
    'nature': 'Original deterministic teaching calculations; no patient or measured device data',
    'python': platform.python_version(), 'numpy': np.__version__, 'matplotlib': matplotlib.__version__,
    'font': font, 'model': {'knee_dB_SPL':50, 'low_level_gain_dB':30, 'compression_ratio':2,
                          'time_step_ms':dt, 'attack_tau_ms':5, 'release_tau_ms':[50,500],
                          'domain':'dB gain smoothing; known input levels; no limiter/filter bank'},
    'static_input_dB_SPL':[40,50,60,80], 'static_output_dB_SPL':[70,80,85,95],
    'attack_gain_after_one_tau_dB':float(fast[after_tau]),
    'gain_50ms_after_fall_dB':{'fast':float(fast[restore_idx]), 'slow':float(slow[restore_idx])},
    'output_50ms_after_fall_dB_SPL':{'fast':float(50+fast[restore_idx]), 'slow':float(50+slow[restore_idx])},
    'spectral':{'wideband_level_dB_SPL':float(wide_level), 'shared_gain_dB':float(common_gain),
                'shared_outputs_dB_SPL':shared.tolist(), 'independent_outputs_dB_SPL':independent.tolist()},
    'mixture':{'relative_speech_powers':speech_power.tolist(), 'relative_noise_powers':noise_power.tolist(),
               'mixture_levels_dB_SPL':mixture_level.tolist(), 'common_gains_dB':gain_db.tolist(),
               'input_SNR_dB':float(snr_in), 'output_SNR_dB':float(snr_out),
               'within_segment_SNR_dB':[20,0], 'SNR_change_dB':float(snr_out-snr_in)},
    'checks':'All assertions passed: continuity, monotonicity, finite-difference slope, CR, gain/level identity, analytical step response, band contrast, constant-gain SNR invariance, time-weighted SNR change',
}
(OUT/'numerical-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
