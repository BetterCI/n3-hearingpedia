"""Fit and evaluate a shared auditory STRF with two readouts on NEMS demo data.

Run: python fit_strf.py TAR010c-18-2.npz output_directory
Dependencies: numpy, scipy, matplotlib. For Chinese labels use a CJK font.
"""
import argparse
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from scipy.optimize import least_squares

SOURCE_HASH = "efb9e42ec70a66076f67c9577a79f811dd23871b0ba89e1a7b47f0dbdaaaba12"
LAGS = 12
BLOCK = 50
RIDGE = 0.1
BLUE, RED = "#19637a", "#ac472b"


def make_rows(features, target):
    """Keep full histories inside each artificial 0.5 s analysis block."""
    n, channels = features.shape
    assert n % BLOCK == 0
    blocks = features.reshape(-1, BLOCK, channels)
    past = sliding_window_view(blocks, LAGS, axis=1)[..., ::-1]
    indices = np.arange(n).reshape(-1, BLOCK)[:, LAGS-1:].ravel()
    design = past.reshape(len(indices), channels * LAGS)
    np.testing.assert_allclose(design[0, :LAGS], features[:LAGS, 0][::-1])
    return design, target.ravel()[indices], indices


def rectified(params, drive):
    gain, threshold, floor = params
    return floor + gain * np.maximum(drive - threshold, 0)


def scores(truth, prediction):
    return {"r": None if np.ptp(prediction) == 0 else float(np.corrcoef(truth, prediction)[0, 1]),
            "rmse": float(np.sqrt(np.mean((prediction - truth)**2))),
            "mean": float(np.mean(prediction))}


def save(fig, out, name):
    fig.tight_layout(pad=1.3)
    svg = out / (name + ".svg")
    fig.savefig(svg, metadata={"Date": None})
    lines = svg.read_text(encoding="utf8").splitlines()
    svg.write_text("\n".join(line.rstrip() for line in lines) + "\n", encoding="utf8")
    fig.savefig(out / (name + ".png"), dpi=140)
    plt.close(fig)


def figures(out, weights, drive, calibration, line, params, yt, pred, indices):
    plt.rcParams.update({"font.family": "sans-serif",
                         "font.sans-serif": ["Microsoft YaHei", "Noto Sans CJK SC", "DejaVu Sans"],
                         "axes.unicode_minus": False, "svg.hashsalt": "hearingpedia-strf"})
    # A hand-specified kernel and two histories; x-axis runs from past to now.
    kernel = np.array([[.6, -.2], [-.4, .8]])
    up = np.eye(2)
    down = np.fliplr(up)
    np.testing.assert_allclose([(up*kernel).sum(), (down*kernel).sum()], [1.4, -.6])
    fig, axes = plt.subplots(1, 3, figsize=(9, 2.9))
    for ax, data, title in zip(axes, [kernel,up,down],
                               ["权重", "先低后高：驱动 1.4","先高后低：驱动 −0.6"]):
        ax.imshow(data, origin="lower", cmap="RdBu_r", vmin=-1, vmax=1, aspect="auto")
        for (i,j), v in np.ndenumerate(data):
            ax.text(j,i,f"{v:g}",ha="center",va="center",color="white" if v>=.6 else "black")
        ax.set(title=title, xticks=[0,1], xticklabels=["前一帧","当前帧"],
               yticks=[0,1], yticklabels=["低频","高频"])
    save(fig,out,"two-histories")

    fig, (a,b) = plt.subplots(1,2,figsize=(9.2,3.5))
    bound = np.abs(weights).max()
    im = a.imshow(weights,origin="lower",aspect="auto",cmap="RdBu_r",vmin=-bound,vmax=bound,
                  extent=(-5,115,.5,18.5))
    a.set(xlabel="滞后（毫秒，0 表示当前帧）", ylabel="声频通道编号",title="估计出的线性权重")
    a.set_yticks([1,4,7,10,13,16,18])
    fig.colorbar(im,ax=a,shrink=.75)
    x = np.linspace(*np.quantile(drive,[.002,.998]),200)
    b.plot(x, line[0]*x+line[1],color=BLUE,ls="--",label="仿射")
    b.plot(x, rectified(params,x),color=RED,label="整流")
    bins = np.array_split(np.argsort(drive),20)
    b.scatter([drive[i].mean() for i in bins],[calibration[i].mean() for i in bins],
              color="#353535",s=12,label="校准集分箱均值")
    b.set(xlabel="线性驱动",ylabel="响应（原数据单位）",title="同一驱动的两种读出")
    b.legend(fontsize=8)
    save(fig,out,"kernel-readout")

    fig, ax = plt.subplots(figsize=(9.2,3.1))
    for values, color, label in [(yt,"#727272","记录的 PSTH"),(pred,RED,"整流模型")]:
        trace = np.full(indices.max()+1,np.nan)
        trace[indices] = values
        ax.plot(np.arange(350)/100,trace[:350],lw=1.2,color=color,label=label)
    ax.set(xlabel="测试序列时间（秒）",ylabel="响应（原数据单位）",title="预先固定的测试集首 3.5 秒")
    ax.legend()
    save(fig,out,"held-out-response")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("data",type=Path)
    p.add_argument("out",type=Path)
    args = p.parse_args()
    if hashlib.sha256(args.data.read_bytes()).hexdigest() != SOURCE_HASH:
        raise ValueError("Unexpected NEMS input file (SHA-256 mismatch)")
    args.out.mkdir(exist_ok=True,parents=True)
    with np.load(args.data,allow_pickle=False) as z:
        fit, cal = np.split(np.log1p(z["X_est"]),[39600])
        yfit, ycal = np.split(z["Y_est"],[39600])
        test, ytest = np.log1p(z["X_val"]), z["Y_val"]
    mean, sd = fit.mean(axis=0), fit.std(axis=0)
    X, y, _ = make_rows((fit-mean)/sd,yfit)
    C, yc, _ = make_rows((cal-mean)/sd,ycal)
    T, yt, frames = make_rows((test-mean)/sd,ytest)
    center = X.mean(axis=0)
    X -= center
    weights = np.linalg.solve(X.T@X/len(y)+RIDGE*np.eye(X.shape[1]),X.T@(y-y.mean())/len(y))
    cd, td = (C-center)@weights+y.mean(), (T-center)@weights+y.mean()
    line = np.polyfit(cd,yc,1)
    opt = least_squares(lambda v: rectified(v,cd)-yc, [1,.05,.01],
                        bounds=([0,-np.inf,0],[np.inf,np.inf,np.inf]))
    if not opt.success:
        raise RuntimeError(opt.message)
    pred = rectified(opt.x,td)
    metrics = {"sha256": SOURCE_HASH, "rows_fit_cal_test": [len(y),len(yc),len(yt)],
               "ridge": RIDGE, "lags": LAGS, "calibration_mean": float(yc.mean()),
               "test_mean": float(yt.mean()), "affine_slope_intercept": line.tolist(),
               "gain_threshold_floor": opt.x.tolist(),
               "constant": scores(yt,np.full_like(yt,yc.mean())),
               "affine": scores(yt,np.polyval(line,td)), "rectified": scores(yt,pred)}
    assert np.all(np.isfinite(pred)) and np.all(pred>=0)
    (args.out/"metrics.json").write_text(json.dumps(metrics,indent=2,allow_nan=False)+"\n",encoding="utf8")
    figures(args.out,weights.reshape(18,LAGS),cd,yc,line,opt.x,yt,pred,frames)
    print(json.dumps(metrics,indent=2))


if __name__ == "__main__":
    main()
