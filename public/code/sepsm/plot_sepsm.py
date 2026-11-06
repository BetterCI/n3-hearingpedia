"""Create teaching figures beside a chosen output directory from compare_sepsm.m results."""
import argparse
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("csv", type=Path)
parser.add_argument("out", type=Path)
args = parser.parse_args()
args.out.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "sans-serif",
                     "font.sans-serif": ["Microsoft YaHei", "Noto Sans CJK SC", "DejaVu Sans"],
                     "axes.spines.top": False, "axes.spines.right": False,
                     "svg.hashsalt": "hearingpedia-sepsm", "axes.unicode_minus": False})
blue, orange = "#126687", "#ad4d16"

def save(fig, name):
    fig.tight_layout(pad=1.6)
    svg = args.out / (name + ".svg")
    fig.savefig(svg, metadata={"Date": None})
    lines = svg.read_text(encoding="utf-8").splitlines()
    svg.write_text("\n".join(line.rstrip() for line in lines) + "\n", encoding="utf-8")
    fig.savefig(args.out / (name + ".png"), dpi=135)
    plt.close(fig)

fig, axes = plt.subplots(1, 2, figsize=(10, 3.3))
t = np.arange(5000) / 10000
for ax, rate in zip(axes, (4, 16)):
    env = 1 + 0.7*np.cos(2*np.pi*rate*t)
    ax.plot(t, env*np.cos(2*np.pi*250*t), color="#84aeba", lw=0.7)
    ax.plot(t, env, color=orange, lw=2, label="正包络")
    ax.set(title=f"载频 250 Hz，调制频率 {rate} Hz", xlabel="时间（秒）",
           ylabel="相对振幅", xlim=(0, .5), ylim=(-1.85,1.85))
    ax.legend(loc="lower right")
save(fig,"carrier-envelope")

fig, ax = plt.subplots(figsize=(10, 3.2))
for row, rate in enumerate((2, 4, 8, 16)):
    for i in range(rate):
        ax.barh(row, 1/rate, left=i/rate, height=.65,
                color=blue if i%2==0 else "#b2d7dd", edgecolor="white")
ax.set(yticks=range(4), yticklabels=["2 Hz　500 ms","4 Hz　250 ms","8 Hz　125 ms","16 Hz　62.5 ms"],
       xlabel="共同的时间轴（秒）", xlim=(0,1), title="各调制通道分别分窗")
ax.invert_yaxis()
save(fig,"resolution")

with args.csv.open(encoding="utf-8-sig",newline="") as src:
    rows = list(csv.DictReader(src))
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)
for ax, key, title in zip(axes, ("sEPSM","mr_sEPSM"), ("长期 sEPSM","多分辨率 mr-sEPSM")):
    for code, label, style, color in [("1","平稳背景","o-",blue),("2","4 Hz 起伏背景","s--",orange)]:
        part = [r for r in rows if r["masker"] == code]
        ax.plot([float(r["acoustic_dB"]) for r in part],
                [10*np.log10(float(r[key])) for r in part],style,color=color,label=label)
    ax.set(title=title,xlabel="输入声学信噪比（dB）",xticks=[-9,-6,-3,0,3])
    ax.grid(axis="y",alpha=.2)
    ax.legend()
axes[0].set_ylabel("总包络信噪比（dB）")
save(fig,"model-comparison")
