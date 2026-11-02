import numpy as np
from scipy.integrate import solve_ivp
mu, omega = .2, 2*np.pi
def augmented(t, z):
    x, y = z[:2]
    r2 = x*x+y*y
    state = [(mu-r2)*x-omega*y, omega*x+(mu-r2)*y]
    jac = np.array([[mu-3*x*x-y*y, -omega-2*x*y],
                    [omega-2*x*y, mu-x*x-3*y*y]])
    return np.r_[state, (jac @ z[2:].reshape(2, 2)).ravel()]
initial = np.r_[np.sqrt(mu), 0., np.eye(2).ravel()]
sol = solve_ivp(augmented, (0, 1), initial, method='DOP853',
                rtol=1e-11, atol=1e-13, max_step=.02)
assert sol.success
multipliers = np.linalg.eigvals(sol.y[2:, -1].reshape(2, 2))
assert np.allclose(np.sort(multipliers.real), [np.exp(-.4), 1], atol=1e-9)
assert np.max(np.abs(multipliers.imag)) < 1e-10
print('Floquet multipliers:', multipliers)
