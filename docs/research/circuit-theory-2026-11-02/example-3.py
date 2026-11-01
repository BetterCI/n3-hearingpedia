import numpy as np
from scipy.integrate import solve_ivp
R, C, Vs = 1e4, 1e-6, 1.
t = np.linspace(0, .05, 501)
sol = solve_ivp(lambda t, u: [(Vs-u[0])/(R*C)],
                [0, t[-1]], [0.], t_eval=t, rtol=1e-9, atol=1e-11)
assert sol.success
exact = Vs*(1-np.exp(-t/(R*C)))
error = np.max(np.abs(sol.y[0]-exact))
print("maximum error / V", error)
assert error < 1e-7
