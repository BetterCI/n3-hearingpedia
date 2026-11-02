import numpy as np
b=np.array([1.2,.15,-.08]);lam=.2
x=np.sign(b)*np.maximum(np.abs(b)-lam,0)
nz=x!=0
assert np.max(np.abs(x[nz]-b[nz]+lam*np.sign(x[nz])))<1e-12
assert np.all(np.abs(b[~nz])<=lam)
print("L1",x,"L2",b/(1+lam))
