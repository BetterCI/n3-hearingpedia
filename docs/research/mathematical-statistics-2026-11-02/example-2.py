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
