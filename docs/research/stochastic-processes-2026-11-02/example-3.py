import numpy as np
from scipy.linalg import toeplitz
a, noise_variance, L = .8, .5, 3
r = a**np.arange(L)
R = toeplitz(r)+noise_variance*np.eye(L)
w = np.linalg.solve(R, r)
mse = 1-r @ w
assert np.allclose(R @ w-r, 0.)
assert np.isclose(mse, .2575009037233401)
assert mse < noise_variance
print('Causal coefficients, population MSE:', w, mse)
