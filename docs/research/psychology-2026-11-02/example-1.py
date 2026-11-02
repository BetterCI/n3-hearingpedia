import numpy as np
ok = np.array([[81, 1], [19, 16]])
total = np.array([[90, 10], [20, 80]])
print("分层比例：", ok / total)
print("合并比例：", ok.sum(axis=1) / total.sum(axis=1))
print("两情境等权：", (ok / total).mean(axis=1))
assert np.all((ok / total)[1] > (ok / total)[0])
assert ok[0].sum() / total[0].sum() > ok[1].sum() / total[1].sum()
