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

def save(fig, name):
    path = OUT / (name + ".svg")
    fig.savefig(path, metadata={"Date": None})
    lines = path.read_text(encoding="utf-8").splitlines()
    path.write_text("\n".join(line.rstrip() for line in lines) + "\n", encoding="utf-8")
    plt.close(fig)

# Continuous-time CN kernel for a unit impulse. Time and density are in ms.
time = np.linspace(0, 9, 901)
def alpha(t, tau):
    age = np.maximum(t, 0)
    return age * np.exp(-age/tau) / tau**2

exc = 1.5 * alpha(time, .5)
inh = 1.5 * .6 * alpha(time - 1, 2)
fig, axes = plt.subplots(1, 2, figsize=(9, 3.6), sharey=True, layout="constrained")
axes[0].plot(time, exc, color="#246a89", label="兴奋")
axes[0].plot(time, inh, "--", color="#b95528", label="延迟抑制（幅值）")
axes[1].plot(time, exc-inh, "--", color="#b95528", label="兴奋减抑制")
axes[1].plot(time, np.maximum(exc-inh, 0), color="#246a89", label="半波整流后")
axes[0].set_ylabel("每毫秒的响应密度")
for ax in axes:
    ax.set_xlabel("脉冲到达后的时间（ms）")
    ax.axhline(0, color="#666666", lw=.6)
    ax.legend(frameon=False)
save(fig, "kernel")

sweep = pd.read_csv(HERE / "sweep.csv")
fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
for ax, column, title in zip(axes, ["be_mean", "bs_mean"], ["增强型单元 BE", "抑制型单元 BS"]):
    for (bmf, data), color, marker in zip(sweep.groupby("bmf_Hz"), ["#246a89", "#b95528", "#277556"], ["o", "s", "^"]):
        ax.plot(data.fm_Hz, data[column], marker=marker, ms=4, color=color, label=f"{bmf} Hz")
    ax.set(xlabel="调制频率（Hz）", ylabel="模型平均率", title=title)
    ax.grid(axis="y", alpha=.2)
axes[0].legend(title="设定 BMF", frameon=False)
save(fig, "sweep")

profile = pd.read_csv(HERE / "profile.csv")
fig, axes = plt.subplots(2, 2, figsize=(10, 6), sharex=True, layout="constrained")
columns = ["an_mean", "an_f0_amplitude", "be_mean", "bs_mean"]
titles = ["听神经平均率", "听神经 100 Hz 起伏幅值", "下丘 BE 平均率", "下丘 BS 平均率"]
for ax, column, title in zip(axes.flat, columns, titles):
    for (peak, data), color, marker in zip(profile.groupby("upper_peak_Hz"), ["#246a89", "#b95528"], ["o", "s"]):
        ax.plot(data.cf_Hz, data[column], marker=marker, ms=3, color=color, label=f"上方谱峰 {peak} Hz")
    ax.set_title(title)
    ax.set_ylabel("模型率单位")
    ax.grid(axis="y", alpha=.2)
for ax in axes[1]:
    ax.set_xlabel("特征频率 CF（Hz）")
axes[0, 0].legend(frameon=False, fontsize=9)
save(fig, "profile")
