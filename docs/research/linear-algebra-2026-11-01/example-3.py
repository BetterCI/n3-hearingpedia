import numpy as np
G = np.array([[1., .995], [.995, 1.]])
truth = np.array([1., .2])
observed = G @ truth + np.array([.001, -.001])
print(np.linalg.cond(G, 2))           # 约 399
print(np.linalg.solve(G, observed))  # 约 [1.2, 0.0]
lam = 1e-5
augmented = np.vstack([G, np.sqrt(lam)*np.eye(2)])
target = np.r_[observed, np.zeros(2)]
print(np.linalg.lstsq(augmented, target, rcond=None)[0])
# 约 [1.02856992, 0.17142706]；用增广最小二乘避免直接求逆
