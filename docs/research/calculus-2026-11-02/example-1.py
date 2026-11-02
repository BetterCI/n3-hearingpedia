import numpy as np
A, tau, a, h = 1.0, 0.002, 0.002, 1e-5
def p(t):
    return A*np.exp(-t*t/(2*tau*tau))
analytic = -a*p(a)/(tau*tau)
central = (p(a+h)-p(a-h))/(2*h)
assert np.isclose(central, analytic, rtol=1e-4)
print(analytic, central)  # Pa/s
