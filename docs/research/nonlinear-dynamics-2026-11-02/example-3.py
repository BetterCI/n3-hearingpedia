import numpy as np
def series(r, n=20000):
    x = .1234567
    for _ in range(1000):
        x = r*x*(1-x)
    values = []
    for _ in range(n):
        values.append(x)
        x = r*x*(1-x)
    return np.array(values)
r = 3.2
x = series(r)
multiplier = np.prod(r*(1-2*x[-2:]))
assert np.isclose(multiplier, -r*r+2*r+4)
print('r=3.2 cycle and multiplier:', x[-2:], multiplier)
y = series(4.)
exponent = np.mean(np.log(np.abs(4*(1-2*y))))
print('r=4 finite estimate, typical exact value:', exponent, np.log(2))
assert abs(exponent-np.log(2)) < .005
assert 4*.75*(1-.75) == .75
