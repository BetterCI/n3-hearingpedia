import numpy as np
from scipy.integrate import quad
def G(x, xi):
    return min(x, xi)*(1-max(x, xi))
x = np.linspace(0, 1, 21)
u = np.array([quad(lambda xi: G(xx, xi), 0, 1,
                  points=[xx], epsabs=1e-12)[0] for xx in x])
exact = x*(1-x)/2
print(np.max(np.abs(u-exact)))
assert np.max(np.abs(u-exact)) < 1e-10
assert G(0, .3) == 0 and G(1, .3) == 0
