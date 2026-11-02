import numpy as np
from scipy.linalg import toeplitz
a, N = .8, 64
k = np.arange(1, N)
formula = (N+2*np.sum((N-k)*a**k))/N**2
covariance = toeplitz(a**np.arange(N))
matrix_result = np.ones(N) @ covariance @ np.ones(N) / N**2
assert np.isclose(formula, matrix_result)
print('AR variance of mean, iid value, mean-specific effective N:',
      formula, 1/N, 1/formula)
