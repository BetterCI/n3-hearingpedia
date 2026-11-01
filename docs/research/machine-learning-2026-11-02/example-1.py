import numpy as np
x = np.array([-2., -1., 0., 1., 2.])
y = np.array([-3.8, -2.2, .2, 1.8, 4.])
n, lam = len(x), 1.
ols = (x @ y) / (x @ x)
ridge = (x @ y) / (x @ x + n * lam)
print(ols, ridge)  # 1.96，约1.3066667；截距均为0且未惩罚
