"""Original teaching models and simulated data. Requires NumPy and SciPy."""

import numpy as np
R, C = 100e6, 200e-12
EL, reset, threshold = -.065, -.065, -.050
current, refractory = .2e-9, .002
tau = R*C
steady = EL + R*current
assert steady > threshold > reset
crossing = tau*np.log((steady-reset)/(steady-threshold))
print('tau, first event (ms):', tau*1000, crossing*1000)
print('steady rate (Hz):', 1/(refractory+crossing))

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

import numpy as np
rng = np.random.default_rng(20261108)
frequency = 500.
for sigma in [.0001, .0005]:
    timing_error = rng.normal(0, sigma, 2000)
    phase = 2*np.pi*frequency*timing_error
    sample_vs = abs(np.exp(1j*phase).mean())
    population_vs = np.exp(-.5*(2*np.pi*frequency*sigma)**2)
    print('sigma (ms), sample VS, population VS:', sigma*1000, sample_vs, population_vs)
print('single phase sample VS:', abs(np.exp(1j*.7)))
