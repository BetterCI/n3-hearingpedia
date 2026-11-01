"""Invented teaching data, not listener measurements. Requires NumPy and SciPy."""

import numpy as np
from scipy import stats
d = np.array([1,2,3,0,4,2,1,3,2,5,-1,2.])
n = len(d)
mean, sd = d.mean(), d.std(ddof=1)
se = sd / np.sqrt(n)
critical = stats.t.ppf(.975, n-1)
interval = mean + np.array([-1, 1])*critical*se
p = 2*stats.t.sf(abs(mean/se), n-1)
print('mean, SD, SE (dB):', mean, sd, se)
print('df, t, p, CI:', n-1, mean/se, p, interval)

import numpy as np
from scipy import stats
k, n = 60, 80
phat, z = k/n, stats.norm.ppf(.975)
center = (phat + z*z/(2*n))/(1+z*z/n)
half = z*np.sqrt(phat*(1-phat)/n+z*z/(4*n*n))/(1+z*z/n)
wilson = np.array([center-half, center+half])
check = stats.binomtest(k, n).proportion_ci(method='wilson')
assert np.allclose(wilson, [check.low, check.high])
print('Wilson:', wilson)
print('Beta posterior mean, equal-tail CI:', (k+1)/(n+2), stats.beta.ppf([.025,.975], k+1, n-k+1))

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
