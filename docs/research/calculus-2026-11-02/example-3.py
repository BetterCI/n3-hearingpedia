import numpy as np
from scipy.integrate import solve_ivp
tau = 0.005
t = np.linspace(0, 0.03, 301)
sol = solve_ivp(lambda t, y: (1-y)/tau, (0, 0.03), [0.4],
                method="RK45", t_eval=t, max_step=0.001,
                rtol=1e-9, atol=1e-12)
assert sol.success
exact = 1-0.6*np.exp(-t/tau)
error = np.max(np.abs(sol.y[0]-exact))
assert error < 1e-8
print(error)
