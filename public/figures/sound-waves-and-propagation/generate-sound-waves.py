"""Original analytical teaching figures; no measured acoustic or biological data."""
from pathlib import Path
import shutil
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = next((p for p in Path(__file__).resolve().parents if (p / 'package.json').exists()), Path.cwd())
OUT = ROOT / 'public/figures/sound-waves-and-propagation'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'Microsoft YaHei', 'font.size': 13,
    'svg.fonttype': 'path', 'axes.unicode_minus': False,
    'axes.spines.top': False, 'axes.spines.right': False})
BLUE, ORANGE, GRAY = '#286a9b', '#b65d2e', '#6c7881'
c, f = 343., 500.
period, wavelength = 1 / f, c / f
omega, k = 2 * np.pi * f, 2 * np.pi / wavelength
step = period / 4

def save(fig, name):
    fig.savefig(OUT / f'{name}.svg', facecolor='white')
    fig.savefig(OUT / f'{name}.png', dpi=160, facecolor='white')
    plt.close(fig)

fig, axes = plt.subplots(3, 1, figsize=(9.4, 11.6),
    gridspec_kw={'height_ratios': [1, .75, 1]})
fig.subplots_adjust(left=.16, right=.97, top=.95, bottom=.075, hspace=.68)
x = np.linspace(0, 1.5, 1500)
ax = axes[0]
ax.plot(x, np.cos(-k*x), color=BLUE, lw=2.5, label='t = 0')
ax.plot(x, np.cos(omega*step-k*x), color=ORANGE, lw=2.5,
        ls='--', label='t = 0.5 ms')
ax.annotate('', xy=(wavelength, 1.22), xytext=(0, 1.22),
            arrowprops={'arrowstyle': '<->', 'color': GRAY})
ax.text(wavelength/2, 1.32, 'λ = 0.686 m', ha='center')
ax.annotate('', xy=(wavelength+c*step, .78), xytext=(wavelength, .78),
            arrowprops={'arrowstyle': '->', 'color': GRAY})
ax.set(xlim=(0, 1.5), ylim=(-1.35, 1.7), xlabel='位置 x（m）',
       ylabel='归一化声压', title='（a）空间快照：波峰向右传播')
ax.legend(loc='lower right', ncol=2, fontsize=12)
ax.axhline(0, color=GRAY, lw=.6)
ax.grid(alpha=.16)

ax = axes[1]
# A deliberately exaggerated displacement field: s = a sin(ωt-kq).
# q is the equilibrium label of each continuum element, not a molecule.
q = np.linspace(.04, 1.46, 78)
display_amplitude = .025
for when, height, color, label in [(0, 1, BLUE, 't = 0'), (step, 0, ORANGE, 't = 0.5 ms')]:
    positions = q + display_amplitude * np.sin(omega*when-k*q)
    ax.scatter(q, np.full_like(q, height), s=18, marker='|', color='#bbc3c9')
    ax.scatter(positions, np.full_like(q, height+.13), s=15, color=color)
    idx = 35
    ax.plot([q[idx], positions[idx]], [height+.13, height+.13], color=color, lw=2)
    ax.scatter([positions[idx]], [height+.13], s=64, color=color, edgecolor='black', zorder=3)
    ax.text(-.05, height+.13, label, ha='right', va='center', fontsize=12)
ax.annotate('同一介质小单元', xy=(q[35]+display_amplitude*np.sin(-k*q[35]), 1.13),
            xytext=(.82, 1.63), fontsize=12,
            arrowprops={'arrowstyle': '->', 'color': GRAY})
ax.set(xlim=(0, 1.5), ylim=(-.3, 1.85), xlabel='平衡位置及夸大的位移（m）',
       title='（b）质点示意：沿传播方向往复运动')
ax.set_yticks([])
ax.spines['left'].set_visible(False)

ax = axes[2]
t = np.linspace(0, .006, 1500)
ax.plot(t*1000, np.cos(omega*t), lw=2.5, color=BLUE)
ax.annotate('', xy=(2, 1.2), xytext=(0, 1.2),
            arrowprops={'arrowstyle': '<->', 'color': GRAY})
ax.text(1, 1.32, 'T = 2 ms', ha='center')
ax.set(xlim=(0, 6), ylim=(-1.25, 1.7), xlabel='时间 t（ms）',
       ylabel='归一化声压', title='（c）固定位置 x = 0：随时间重复')
ax.axhline(0, color=GRAY, lw=.6)
ax.grid(alpha=.16)
fig.text(.5, .019, '500 Hz；c = 343 m/s；理想平面行波。质点位移夸大，未指定绝对声压。',
         ha='center', fontsize=11.5, color=GRAY)
save(fig, '01-space-time')

fig, axes = plt.subplots(2, 1, figsize=(9.4, 8.6))
fig.subplots_adjust(left=.16, right=.97, top=.94, bottom=.18, hspace=.5)
r = np.linspace(1, 8, 700)
landmarks = np.array([1, 2, 4, 8])
for ax in axes:
    ax.set_xlim(.8, 8.3)
    ax.set_xticks(landmarks)
    ax.set_xlabel('距离 r（m）')
    ax.grid(alpha=.16)
axes[0].plot(r, 1/r, color=BLUE, lw=2.5)
axes[0].scatter(landmarks, 1/landmarks, color=BLUE, zorder=3)
for rr in landmarks:
    axes[0].annotate(f'{1/rr:g}', (rr, 1/rr), xytext=(0, 9), textcoords='offset points', ha='center')
axes[0].set(ylabel='相对声压有效值', ylim=(0, 1.18),
            title='（a）相对于 1 m：声压按 1/r 下降')
levels = -20*np.log10(r)
axes[1].plot(r, levels, color=ORANGE, lw=2.5)
axes[1].scatter(landmarks, -20*np.log10(landmarks), color=ORANGE, zorder=3)
for rr in landmarks:
    value = -20*np.log10(rr)
    axes[1].annotate(f'{value:.2f} dB' if rr > 1 else '0 dB', (rr, value),
                    xytext=(0, 12), textcoords='offset points', ha='center')
axes[1].set(ylabel='声压级差（dB）', ylim=(-21, 5),
            title='（b）相对于 1 m：每次距离翻倍约降低 6.02 dB')
fig.text(.5, .025, '理想点声源、自由场远场；输出恒定，无介质吸收与反射。\n1 m 仅为计算基准，不是所有实际声源的远场起点。',
         ha='center', fontsize=11.5, color=GRAY)
save(fig, '02-distance')

# Pure outward spherical wave, peak phasors with exp(+j omega t).
kr = np.geomspace(.01, 100, 1200)
normalized_impedance = 1 / (1 + 1 / (1j * kr))
phase_deg = np.angle(normalized_impedance, deg=True)
assert np.isclose(np.angle(1 / (1 + 1 / 1j), deg=True), 45)
assert np.allclose(normalized_impedance.real, kr**2 / (1 + kr**2))
assert np.allclose(normalized_impedance.imag, kr / (1 + kr**2))
# The active intensity remains p_rms^2/(rho*c) in this particular solution.
assert np.allclose(np.real(1 / normalized_impedance), 1)
fig, axes = plt.subplots(2, 1, figsize=(9.4, 8.8))
fig.subplots_adjust(left=.16, right=.97, top=.94, bottom=.16, hspace=.48)
axes[0].semilogx(kr, normalized_impedance.real, color=BLUE, lw=2.5, label='实部')
axes[0].semilogx(kr, normalized_impedance.imag, color=ORANGE, lw=2.5, ls='--', label='虚部')
axes[0].set(ylabel='归一化比声阻抗', ylim=(0, 1.15),
            title=r'（a）$Z_s / (\rho_0 c)$：远处实部趋近 1，虚部趋近 0')
axes[0].legend(loc='upper left', ncol=2)
axes[1].semilogx(kr, phase_deg, lw=2.5, color=BLUE)
axes[1].scatter([1], [45], color=BLUE, zorder=3)
axes[1].annotate('kr = 1：45°', (1, 45), xytext=(12, 10), textcoords='offset points')
axes[1].set(ylabel='压力相对于速度的相位（°）', ylim=(0, 95),
            title='（b）相位差随 kr 增大而减小')
for ax in axes:
    ax.set(xlim=(.01, 100), xlabel='无量纲距离 kr（对数尺度）')
    ax.axvline(1, color=GRAY, ls=':', lw=1)
    ax.grid(alpha=.16, which='major')
fig.text(.5, .035, '纯外向、无损球面对称波；采用 exp(+jωt) 约定。\nkr = 1 是计算标记，不是所有声源的统一近远场分界。',
         ha='center', fontsize=11.5, color=GRAY)
save(fig, '03-spherical-impedance')

reflection_gain, reflection_delay = .6, .005
frequency_grid = np.linspace(0, 1000, 4001)
two_path_transfer = 1 + reflection_gain * np.exp(-2j*np.pi*frequency_grid*reflection_delay)
two_path_levels = 20*np.log10(np.abs(two_path_transfer))
comb_spacing = 1/reflection_delay
comb_peak = 20*np.log10(1+reflection_gain)
comb_trough = 20*np.log10(1-reflection_gain)
assert np.isclose(two_path_levels[400], comb_trough)  # 100 Hz
assert np.isclose(two_path_levels[800], comb_peak)   # 200 Hz
fig, axes = plt.subplots(2, 1, figsize=(9.4, 8.8))
fig.subplots_adjust(left=.16, right=.97, top=.94, bottom=.16, hspace=.48)
for when, gain, color, label in [(0, 1, BLUE, '直达：1'), (5, .6, ORANGE, '反射：0.6')]:
    axes[0].annotate('', xy=(when, gain), xytext=(when, 0),
                     arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2.5})
    axes[0].text(when, gain+.07, label, ha='center', color=color)
axes[0].axhline(0, color=GRAY, lw=.7)
axes[0].set(xlim=(-1, 9), ylim=(-.08, 1.25), xticks=[0, 5],
            xlabel='相对于直达声的时间（ms）', ylabel='理想脉冲权重',
            title='（a）两条路径：反射延迟 5 ms')
axes[1].plot(frequency_grid, two_path_levels, color=BLUE, lw=2.5)
axes[1].axhline(0, color=GRAY, lw=.7)
axes[1].scatter([200, 300], [comb_peak, comb_trough], color=ORANGE, zorder=3)
axes[1].annotate(f'峰：+{comb_peak:.2f} dB', (200, comb_peak),
                 xytext=(0, 15), textcoords='offset points', ha='center')
axes[1].annotate(f'谷：{comb_trough:.2f} dB', (300, comb_trough),
                 xytext=(15, -14), textcoords='offset points', ha='left')
axes[1].set(xlim=(0, 1000), ylim=(-11, 9), xticks=np.arange(0, 1001, 200),
            xlabel='频率（Hz）', ylabel='相对于直达声的幅度（dB）',
            title='（b）频率响应：相邻峰间隔 200 Hz')
axes[1].grid(alpha=.16)
fig.text(.5, .035, '两路径解析教学计算；反射无额外反相，增益不随频率变化。\n箭头表示理想脉冲权重；不包含设备响应、吸收及其他反射。',
         ha='center', fontsize=11.5, color=GRAY)
save(fig, '04-two-path')

parameters = {
    'nature': 'analytical teaching example, not measured data',
    'speed_m_s': c, 'frequency_Hz': f, 'period_s': period,
    'wavelength_m': wavelength, 'snapshot_step_s': step,
    'wavefront_shift_m': c*step, 'display_particle_displacement_m': display_amplitude,
    'particle_displacement_is_exaggerated': True,
    'distance_m': landmarks.tolist(), 'relative_pressure': (1/landmarks).tolist(),
    'level_difference_dB': (-20*np.log10(landmarks)).tolist(),
    'arrival_time_ms': (landmarks/c*1000).tolist(),
    'spherical_wave': {
        'phasor_convention': 'Re(P exp(+j omega t)); peak amplitude',
        'kr_range': [.01, 100], 'normalized_impedance': '1/(1+1/(j*kr))',
        'kr_1_phase_degrees': 45, 'kr_1_distance_500Hz_m': c/(2*np.pi*500),
        'kr_1_distance_100Hz_m': c/(2*np.pi*100),
        'pure_outward_active_intensity_pressure_conversion': True,
    },
    'two_path': {'direct_gain': 1, 'reflection_gain': reflection_gain,
        'relative_delay_s': reflection_delay, 'path_length_difference_m': c*reflection_delay,
        'frequency_Hz_range': [0, 1000], 'frequency_grid_step_Hz': .25,
        'comb_spacing_Hz': comb_spacing, 'peak_dB': comb_peak, 'trough_dB': comb_trough,
        'first_trough_Hz': comb_spacing/2, 'frequency_independent_positive_reflection': True},
    'timing_uncertainty_example': {'distance_m': 1, 'distance_standard_uncertainty_m': .001,
        'delay_s': 1/c, 'time_standard_uncertainty_s': .00001,
        'independent_relative_standard_uncertainty': float(np.hypot(.001, .00001/(1/c)))},
    'numpy_version': np.__version__, 'matplotlib_version': matplotlib.__version__,
}
(OUT / 'parameters.json').write_text(json.dumps(parameters, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
if Path(__file__).resolve() != (OUT / 'generate-sound-waves.py').resolve():
    shutil.copyfile(__file__, OUT / 'generate-sound-waves.py')
print(json.dumps(parameters, ensure_ascii=False))
