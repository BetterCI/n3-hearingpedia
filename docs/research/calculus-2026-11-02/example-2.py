import numpy as np
from scipy.integrate import trapezoid
T = 0.01
t = np.linspace(0, T, 481)
p = np.sin(2*np.pi*t/T)  # Pa，幅度1
net = trapezoid(p, x=t)  # Pa*s
square = trapezoid(p*p, x=t)  # Pa**2*s
rms = np.sqrt(square/T)  # Pa
assert abs(net) < 1e-14
assert np.isclose(square, 0.005)
assert np.isclose(rms, 1/np.sqrt(2))
print(net, square, rms)
