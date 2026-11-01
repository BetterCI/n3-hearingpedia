import numpy as np
from scipy.integrate import quad
f = lambda t: np.sin(2*np.pi*t)+.4*np.cos(4*np.pi*t)+.2*np.sin(6*np.pi*t)
e = [lambda t: np.sqrt(2)*np.sin(2*np.pi*t),
     lambda t: np.sqrt(2)*np.cos(4*np.pi*t)]
c = np.array([quad(lambda t: g(t)*f(t), 0, 1)[0] for g in e])
p = lambda t: sum(cc*g(t) for cc, g in zip(c, e))
residual2 = quad(lambda t: (f(t)-p(t))**2, 0, 1)[0]
print(c, residual2)
assert np.allclose(c, [1/np.sqrt(2), .4/np.sqrt(2)])
assert np.isclose(residual2, .02)
for g in e:
    assert abs(quad(lambda t: g(t)*(f(t)-p(t)), 0, 1)[0]) < 1e-10
