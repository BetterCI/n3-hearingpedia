import numpy as np

x = np.array([1., 2., 0., -1.])
A = np.column_stack((x, np.r_[0., x[:-1]]))  # 原激励、延迟一格的副本
observed = np.array([0.82, 1.89, 0.63, -0.82])
h, _, rank, _ = np.linalg.lstsq(A, observed, rcond=None)
residual = observed - A @ h
print(h, rank)                 # [0.8  0.31]，秩为 2
print(residual @ residual)     # 约 0.0013
print(A.T @ residual)          # 两项均接近 0
