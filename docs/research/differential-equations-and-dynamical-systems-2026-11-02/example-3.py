import numpy as np
r=3.2
cycle=np.array([(r+1-np.sqrt((r-3)*(r+1)))/(2*r),
                (r+1+np.sqrt((r-3)*(r+1)))/(2*r)])
F=lambda x:r*x*(1-x)
assert np.allclose(F(cycle),cycle[::-1])
multiplier=np.prod(r*(1-2*cycle))
assert np.isclose(multiplier,.16) and abs(multiplier)<1
x=.25
exception=[x]
for _ in range(3):
    x=4*x*(1-x)
    exception.append(x)
assert exception==[.25,.75,.75,.75]
print("two-cycle",cycle,"multiplier",multiplier,"exception",exception)
