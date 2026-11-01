import numpy as np
from scipy.integrate import solve_ivp
C, g, EL, I = 10e-12, 1e-9, -.070, 20e-12
tau, final = C/g, EL+I/g
t = np.linspace(0, .05, 501)
sol = solve_ivp(lambda tt, v: [(-g*(v[0]-EL)+I)/C],
                [0, t[-1]], [EL], t_eval=t, rtol=1e-10, atol=1e-12)
exact = final+(EL-final)*np.exp(-t/tau)
leak = g*(exact-EL)
capacitive = I*np.exp(-t/tau)
print(tau, final, np.max(abs(sol.y[0]-exact)))
assert sol.success and np.max(abs(sol.y[0]-exact)) < 1e-8
assert np.allclose(leak+capacitive, I, atol=1e-22, rtol=1e-10)
