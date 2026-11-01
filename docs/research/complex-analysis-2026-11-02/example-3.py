import numpy as np
from scipy import signal

fs, r, theta0 = 16000, 0.95, np.pi/8
den = [1, -2*r*np.cos(theta0), r*r]
n = np.arange(1000)
delta = np.zeros(len(n)); delta[0] = 1
h = signal.lfilter([1], den, delta)
exact = r**n * np.sin((n+1)*theta0)/np.sin(theta0)
np.testing.assert_allclose(h, exact, atol=1e-12)
f = np.array([600., 1000., 1400.])
_, response = signal.freqz([1], den, worN=f, fs=fs)
z = np.exp(1j*2*np.pi*f/fs)
formula = 1/(1-2*r*np.cos(theta0)/z+r*r/z**2)
np.testing.assert_allclose(response, formula, atol=1e-12)
print("3个频率的增益:", np.abs(response))
