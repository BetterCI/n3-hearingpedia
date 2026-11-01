from itertools import product
import numpy as np
d = np.array([1,2,3,0,4,2,1,3,2,5,-1,2.])
rng = np.random.default_rng(20261102)
indices = rng.integers(0, len(d), size=(20000, len(d)))
bootstrap_means = d[indices].mean(axis=1)
print('percentile CI:', np.quantile(bootstrap_means, [.025,.975], method='linear'))
signs = np.array(list(product([-1,1], repeat=len(d))))
null_means = signs @ d / len(d)
tail = np.abs(null_means) >= abs(d.mean()) - 1e-12
print('tail count, configurations, p:', tail.sum(), len(tail), tail.mean())
