import numpy as np
from scipy import signal
L, M = 3, 2
x = np.array([1., -0.5, 0.25, 0., 0.8])
h = signal.firwin(31, 1/max(L, M), fs=2, window=("kaiser", 5.0))
z = np.zeros((len(x)-1)*L+1)
z[::L] = x
reference = np.convolve(z, L*h)[::M]
polyphase = signal.upfirdn(L*h, x, up=L, down=M)
assert reference.shape == polyphase.shape
assert np.allclose(reference, polyphase, atol=1e-14, rtol=1e-14)
print(len(polyphase), np.max(np.abs(reference-polyphase)))
