import numpy as np
from scipy.integrate import quad
L, a, A = 1., .3, .001
def f(x):
    return A*x/a if x <= a else A*(L-x)/(L-a)
n = np.arange(1, 11)
formula = 2*A*L**2*np.sin(n*np.pi*a/L)/(np.pi**2*n*n*a*(L-a))
numeric = np.array([2/L*quad(
    lambda x: f(x)*np.sin(i*np.pi*x/L), 0, L,
    points=[a], epsabs=1e-13)[0] for i in n])
print(formula[:3])
assert np.allclose(formula, numeric, atol=1e-12, rtol=1e-9)
