"""Render the published figure(s) from the adjacent AMT result tables."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[1] / "figures" / HERE.name
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({
    "font.family": ["Microsoft YaHei", "Noto Sans CJK SC", "DejaVu Sans"],
    "svg.fonttype": "path", "svg.hashsalt": "hearingpedia", "axes.spines.top": False,
    "axes.spines.right": False, "axes.unicode_minus": False, "font.size": 11,
})

data = pd.read_csv(HERE / "comparison.csv")
fig, axes = plt.subplots(1, 3, figsize=(11, 3.6), layout="constrained")
for ax, column, unit in zip(axes, ["STOI", "sEPSM", "mr_sEPSM"], ["相关指数", "线性包络功率比", "线性包络功率比"]):
    for masker, label, style, color in [(1, "原始载体", "o-", "#246a89"), (2, "4 Hz 起伏", "s--", "#b95528")]:
        rows = data[data.masker == masker]
        ax.plot(rows.acoustic_dB, rows[column], style, color=color, label=label)
    ax.set(title=column.replace("_", "-"), ylabel=unit, xlabel="声学信噪比（dB）", xticks=[-9, -6, -3, 0, 3])
    ax.grid(axis="y", alpha=.2)
axes[0].legend(frameon=False)
path = OUT / "comparison.svg"
fig.savefig(path, metadata={"Date": None})
lines = path.read_text(encoding="utf-8").splitlines()
path.write_text("\n".join(line.rstrip() for line in lines) + "\n", encoding="utf-8")

# Illustrative logistic curves, not fitted to listening data.
snr = np.linspace(-14, 6, 201)
fig, ax = plt.subplots(figsize=(7, 3.5), layout="constrained")
for threshold, slope, label, style, color in [
        (-5, .7, "阈值 −5 dB，较陡", "-", "#246a89"),
        (-2, .7, "阈值 −2 dB，较陡", "--", "#b95528"),
        (-5, .35, "阈值 −5 dB，较缓", ":", "#277556")]:
    prob = 100 / (1 + np.exp(-slope * (snr - threshold)))
    ax.plot(snr, prob, style, color=color, label=label)
ax.axhline(50, color="#666666", lw=.8)
ax.set(xlabel="声学信噪比（dB）", ylabel="示例正确率（%）", ylim=(0, 100))
ax.legend(frameon=False)
path = OUT / "calibration.svg"
fig.savefig(path, metadata={"Date": None})
lines = path.read_text(encoding="utf-8").splitlines()
path.write_text("\n".join(line.rstrip() for line in lines) + "\n", encoding="utf-8")
