import numpy as np
from scipy.integrate import solve_ivp
tau, f = .005, 100.
w = 2*np.pi*f
H = 1/(1+1j*w*tau)
t = np.linspace(0, .08, 1601)
sol = solve_ivp(lambda tt, y: [(np.cos(w*tt)-y[0])/tau],
                [0, t[-1]], [0.], t_eval=t,
                rtol=1e-10, atol=1e-12)
steady = np.real(H*np.exp(1j*w*t))
exact = steady-np.real(H)*np.exp(-t/tau)
assert sol.success and np.max(abs(sol.y[0]-exact)) < 1e-8
print(abs(H), np.angle(H), np.max(abs(sol.y[0]-exact)))
