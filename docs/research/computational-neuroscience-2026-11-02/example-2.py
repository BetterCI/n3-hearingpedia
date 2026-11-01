import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(20261105)
x = rng.uniform(-1, 1, 4000)
X, dt = np.column_stack([np.ones(4000), x]), .01
y = rng.poisson(dt*np.exp(X @ np.array([np.log(30), .8])))
A, b = X[:2000], y[:2000]
fit = minimize(lambda w: np.sum(dt*np.exp(A@w)-b*(A@w)),
    [np.log(b.mean()/dt), 0.], jac=lambda w: A.T@(dt*np.exp(A@w)-b),
    method='BFGS', options={'gtol': 1e-9})
assert fit.success, fit.message
mu, baseline = dt*np.exp(X[2000:]@fit.x), b.mean()
gain = np.sum(y[2000:]*np.log(mu/baseline)-mu+baseline)
print('coefficients:', fit.x, 'test bits/spike:', gain/(np.log(2)*y[2000:].sum()))
