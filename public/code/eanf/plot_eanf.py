"""Draw analytic field and AMT result figures. Usage: python plot_eanf.py CSV_DIR OUT_DIR"""
import argparse
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("data", type=Path)
parser.add_argument("out", type=Path)
args = parser.parse_args()
args.out.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "sans-serif",
                     "font.sans-serif": ["Microsoft YaHei", "Noto Sans CJK SC", "DejaVu Sans"],
                     "axes.unicode_minus": False, "svg.hashsalt": "hearingpedia-eanf"})
blue, orange = "#1c6580", "#a94623"


def columns(name):
    with (args.data / (name + ".csv")).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return {key: np.array([float(row[key]) for row in rows]) for key in rows[0]}


def save(fig, name):
    fig.tight_layout(pad=1.5)
    svg = args.out / (name + ".svg")
    fig.savefig(svg, metadata={"Date": None})
    lines = svg.read_text(encoding="utf8").splitlines()
    svg.write_text("\n".join(line.rstrip() for line in lines)+"\n", encoding="utf8")
    fig.savefig(args.out / (name + ".png"), dpi=140)
    plt.close(fig)


fig, (a,b) = plt.subplots(1,2,figsize=(9,3.3))
x = np.linspace(-4,4,401)
for d,color,style in [(1,blue,"-"),(2,orange,"--")]:
    potential = -1 / np.sqrt(x*x + d*d)
    curvature = (d*d - 2*x*x)/(x*x + d*d)**2.5
    np.testing.assert_allclose(curvature[len(x)//2],1/d**3)
    a.plot(x,potential,style,color=color,label=f"距离 d = {d}")
    b.plot(x,curvature,style,color=color,label=f"距离 d = {d}")
for ax in (a,b):
    ax.set_xlabel("沿直纤维的位置 x（相对长度）")
    ax.axhline(0,color="grey",lw=.6)
    ax.legend()
a.set(ylabel="细胞外电位（相对量）",title="同一阴极点源，不同距离")
b.set(ylabel="电位的空间二阶导数（相对量）",title="纤维上各处的初始驱动")
save(fig,"field")

single = columns("single")
dur = columns("duration")
fig, (a,b) = plt.subplots(1,2,figsize=(9,3.3))
a.plot(single["mA"],single["p_spike"],"o-",color=blue,ms=3)
a.axhline(.5,color="grey",ls=":")
a.set(xlabel="每相电流幅值（mA）",ylabel="单脉冲放电概率",title="固定相宽 100 μs",ylim=(-.04,1.04))
b.plot(dur["phase_us"],dur["threshold50_mA"],"s-",color=orange)
b.set(xlabel="每相持续时间（μs）",ylabel="50% 阈电流（mA）",title="延长相宽，阈电流下降",xticks=dur["phase_us"])
save(fig,"single")

pair, train = columns("paired"), columns("train")
fig, (a,b) = plt.subplots(1,2,figsize=(9.5,3.55))
for amp,color,style in [(.58,blue,"o-"),(.72,orange,"s--")]:
    mask = np.isclose(pair["first_mA"],amp)
    a.plot(pair["onset_interval_ms"][mask],pair["p_probe"][mask],style,color=color,
           ms=4,label=f"首脉冲 {amp:.2f} mA")
a.axhline(.5,color="grey",ls=":",label="单独测试脉冲")
a.set(xlabel="两个脉冲的起始间隔（ms）",ylabel="测试脉冲放电概率",title="同一测试脉冲，改变前序刺激")
for rate,color,style in [(500,blue,"o-"),(1000,orange,"s--")]:
    mask = train["pps"]==rate
    b.plot(train["pulse_number"][mask],train["p_spike"][mask],style,color=color,
           ms=4,label=f"{rate} 脉冲/秒")
b.set(xlabel="脉冲序号",ylabel="逐脉冲放电概率",title="同为 12 个脉冲，每相 0.64 mA",xticks=[1,3,6,9,12])
for ax in (a,b):
    ax.legend(fontsize=8)
    ax.set_ylim(-.04,1.05)
save(fig,"history")
