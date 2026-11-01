import numpy as np
from scipy.integrate import solve_ivp
c, t = 2e-6, np.linspace(0, 2, 301)
for scale in [.2, 1., 5.]:
    kon, koff = scale*1e6, scale*1.
    eq, tau = kon*c/(kon*c+koff), 1/(kon*c+koff)
    sol = solve_ivp(lambda tt, y: [kon*c*(1-y[0])-koff*y[0]],
                    [0, t[-1]], [0.], t_eval=t, rtol=1e-9, atol=1e-11)
    exact = eq*(1-np.exp(-t/tau))
    print(koff/kon, tau)
    assert sol.success and np.max(abs(sol.y[0]-exact)) < 1e-7
