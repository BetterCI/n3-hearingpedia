import numpy as np

rng = np.random.default_rng(20261105)
sets, M, sigma, rho = 50000, 16, 0.2, 0.5
ind = rng.normal(0, sigma, (sets, M))
common = rng.normal(0, sigma * np.sqrt(rho), (sets, 1))
private = rng.normal(0, sigma * np.sqrt(1-rho), (sets, M))
sd_ind = ind.mean(axis=1).std(ddof=1)
sd_shared = (common + private).mean(axis=1).std(ddof=1)
theory = sigma * np.sqrt(rho + (1-rho)/M)
assert abs(sd_ind - sigma/np.sqrt(M)) < 0.002
assert abs(sd_shared - theory) < 0.003
print("独立与共享噪声平均后的模拟标准差:", sd_ind, sd_shared)
print("相应理论值:", sigma/np.sqrt(M), theory)
