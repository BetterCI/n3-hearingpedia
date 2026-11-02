import numpy as np
from scipy.integrate import solve_ivp
def rhs(t,z):
    x,y=z
    r2=x*x+y*y
    return [(1-r2)*x-2*y,2*x+(1-r2)*y]
def crossing(t,z):
    return z[1]
crossing.direction=1
crossing.terminal=False
t=np.linspace(0,12,601)
sol=solve_ivp(rhs,(0,12),[.2,0.],t_eval=t,events=crossing,
    method="DOP853",rtol=1e-10,atol=1e-12,max_step=.03)
radius=np.linalg.norm(sol.y,axis=0)
exact=1/np.sqrt(1+24*np.exp(-2*t))
events=sol.t_events[0]
events=events[events>1e-8]
assert sol.success and np.max(np.abs(radius-exact))<1e-8
assert np.allclose(np.diff(events),np.pi,atol=1e-8,rtol=0)
print("returns",events,"radius error",np.max(np.abs(radius-exact)))
