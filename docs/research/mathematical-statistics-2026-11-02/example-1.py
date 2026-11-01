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
