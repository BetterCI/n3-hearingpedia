import numpy as np
from scipy.stats import norm
k = np.array([0.0, 0.75, 1.5])
H, F = norm.sf(k - 1.5), norm.sf(k)
dp = norm.ppf(H) - norm.ppf(F)
c = -(norm.ppf(H) + norm.ppf(F)) / 2
print(np.column_stack([k, H, F, dp, c]))
assert np.allclose(dp, 1.5)
assert np.allclose(c, k - 0.75)
