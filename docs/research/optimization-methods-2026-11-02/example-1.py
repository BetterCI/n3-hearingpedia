import numpy as np
q=np.array([1.,20.]);x0=np.array([3.,1.])
for alpha in [.05,.09,.105]:
    x=x0.copy()
    for _ in range(60):
        x-=alpha*q*x
    exact=x0*(1-alpha*q)**60
    assert np.allclose(x,exact,rtol=1e-12,atol=1e-12)
    print(alpha,x,.5*np.dot(q*x,x))
