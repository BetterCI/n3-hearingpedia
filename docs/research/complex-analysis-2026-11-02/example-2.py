import numpy as np

a = 0.8
theta = 2*np.pi*np.arange(8192) / 8192
def coefficient(n, radius):
    z = radius*np.exp(1j*theta)
    H = z/(z-a)
    return np.mean(H * z**n)

for n in (-2, -1, 0, 1, 2):
    outer = coefficient(n, 1.2)
    inner = coefficient(n, 0.4)
    expected_outer = a**n if n >= 0 else 0.0
    expected_inner = -a**n if n <= -1 else 0.0
    assert abs(outer-expected_outer) < 1e-10
    assert abs(inner-expected_inner) < 1e-10
    print(n, outer.real, inner.real)
