"""Original teaching simulation; no audio output. Run from the repository root.
Dependencies: numpy, matplotlib. Fixed-step 2-down 1-up, reset after each move.
"""
from pathlib import Path
import csv
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
FIG = ROOT / 'public/figures/adaptive-psychophysical-measurement'
FIG.mkdir(parents=True, exist_ok=True)
font = next((f.name for f in font_manager.fontManager.ttflist if f.name in ['Microsoft YaHei', 'SimHei', 'Noto Sans CJK SC']), 'DejaVu Sans')
plt.rcParams.update({'font.family': font, 'svg.fonttype': 'path', 'svg.hashsalt': 'adaptive-20261117', 'axes.unicode_minus': False, 'font.size': 14})
TARGET_P = 2 ** -.5
TARGET = -6 + 2 * np.log((TARGET_P - .5) / (.98 - TARGET_P))

def prob(x):
    return .5 + .48 / (1 + np.exp(-(x + 6) / 2))

def run(seed, trials=100, step=2., fixed_p=None):
    rng = np.random.default_rng(seed)
    x, count, direction = 2., 0, 0
    rows, reversals = [], []
    for t in range(trials):
        correct = int(rng.random() < (prob(x) if fixed_p is None else fixed_p))
        count = count + 1 if correct else 0
        move = -1 if count == 2 else (1 if not correct else 0)
        if move:
            count = 0
        requested = x + move * step
        new_x = float(np.clip(requested, -20, 10)) if fixed_p is None else requested
        actual = int(np.sign(new_x - x))
        reverse = bool(actual and direction and actual != direction)
        if reverse:
            reversals.append(x)
        rows.append([t + 1, x, correct, requested, new_x, int(reverse), int(requested != new_x)])
        if actual:
            direction = actual
        x = new_x
    estimate = float(np.mean(reversals[-8:])) if len(reversals) >= 12 else None
    return np.array(rows), estimate

def write_csv(name, data, header):
    with (OUT / name).open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(header); w.writerows(data)

def save(fig, name):
    fig.tight_layout()
    svg = FIG / (name + '.svg')
    fig.savefig(svg, metadata={'Date': None})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines()) + '\n', encoding='utf-8')
    fig.savefig(FIG / (name + '.png'), dpi=150)
    plt.close(fig)

trace, estimate = run(20261117)
write_csv('trajectory.csv', trace, ['trial', 'presented_db_snr', 'correct', 'requested_next', 'actual_next', 'reversal', 'boundary'])
fig, ax = plt.subplots(figsize=(12, 6.5))
ax.step(trace[:, 0], trace[:, 1], where='post', color='#2477a5', label='呈现水平')
rev = trace[:, 5].astype(bool)
ax.scatter(trace[rev, 0], trace[rev, 1], facecolors='white', edgecolors='#c66a24', zorder=3, label='反转试次')
ax.axhline(TARGET, color='#303d4e', ls='--', label='真实70.7%阈值')
ax.set(xlabel='试次', ylabel='信噪比（dB SNR）', title='二下一上：固定2 dB步长的教学轨迹')
ax.legend(loc='upper right'); ax.grid(alpha=.2)
save(fig, '01-staircase')

estimates = [run(seed)[1] for seed in range(20261118, 20261618)]
values = np.array([v for v in estimates if v is not None])
write_csv('estimates.csv', [[s, v] for s, v in zip(range(20261118, 20261618), estimates)], ['seed', 'threshold_db_snr_or_missing'])
fig, ax = plt.subplots(figsize=(12, 6.5))
bins = np.arange(np.floor(values.min()) - .5, np.ceil(values.max()) + 1, .5)
assert np.histogram(values, bins=bins)[0].sum() == len(values)
ax.hist(values, bins=bins, color='#2477a5', edgecolor='white')
ax.axvline(TARGET, color='#c66a24', ls='--', label='真实70.7%阈值')
ax.set(xlabel='最后8个反转的平均（dB SNR）', ylabel='成功轨迹数', title='500次独立教学模拟：估计存在变异')
ax.legend(); ax.grid(axis='y', alpha=.2)
save(fig, '02-estimates')

# Independent checks: analytic inverse and observed move balance under constant p.
assert abs(prob(TARGET) - TARGET_P) < 1e-12
assert abs(TARGET - (-6.552)) < .001
constant, _ = run(99, trials=200000, step=1, fixed_p=TARGET_P)
moves = constant[:, 4] - constant[:, 1]
down_fraction = float(np.sum(moves < 0) / np.sum(moves != 0))
assert abs(down_fraction - .5) < .01
# A known deterministic response sequence verifies counter resets independently.
count, level, levels = 0, 0, []
for response in [1, 1, 1, 0, 1, 1, 0]:
    count = count + 1 if response else 0
    if not response: level += 1
    elif count == 2: level -= 1; count = 0
    levels.append(level)
assert levels == [0, -1, -1, 0, 0, -1, 0]
result = dict(target_probability=TARGET_P, target_db_snr=float(TARGET), trajectory_estimate=estimate,
              repetitions=500, success=len(values), failures=500-len(values),
              bias_db=float(np.mean(values)-TARGET), sd_db=float(np.std(values, ddof=1)),
              rmse_db=float(np.sqrt(np.mean((values-TARGET)**2))),
              constant_probability_down_fraction=down_fraction, checks='passed',
              parameters=dict(gamma=.5, upper_error=.02, alpha_db=-6, scale_db=2, start_db=2,
                              step_db=2, trials=100, min_db=-20, max_db=10, minimum_reversals=12, final_reversals=8),
              numpy_version=np.__version__, matplotlib_version=matplotlib.__version__)
(OUT / 'results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
