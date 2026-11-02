import numpy as np
from scipy.optimize import minimize
b=np.array([2.,1.])
res=minimize(lambda x:.5*np.dot(x-b,x-b),[.3,.3],
    jac=lambda x:x-b,method="SLSQP",bounds=[(0,None)]*2,
    constraints=[{"type":"ineq","fun":lambda x:2-x.sum(),
                  "jac":lambda x:-np.ones(2)}],
    options={"ftol":1e-12,"maxiter":200})
mu=.5
primal=max(0.,res.x.sum()-2,-res.x.min())
stationary=np.max(np.abs(res.x-b+mu))
complementary=abs(mu*(res.x.sum()-2))
gap=res.fun-(mu-mu*mu)
assert res.success and max(primal,stationary,complementary,abs(gap))<1e-9
print(res.x,res.fun,primal,stationary,complementary,gap)
