import numpy as np
from scipy.integrate import solve_ivp
t=np.linspace(0,6,301)
for x0 in [0.,.15,.6,1.4]:
    sol=solve_ivp(lambda t,x:1.2*x*(1-x),(0,6),[x0],
        t_eval=t,method="DOP853",rtol=1e-10,atol=1e-12,max_step=.05)
    exact=np.zeros_like(t) if x0==0 else 1/(1+(1/x0-1)*np.exp(-1.2*t))
    error=np.max(np.abs(sol.y[0]-exact))
    assert sol.success and error<1e-8
    print(x0,error,sol.y[0,-1])
