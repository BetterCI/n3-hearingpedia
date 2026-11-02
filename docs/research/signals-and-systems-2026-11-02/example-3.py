import numpy as np
fs = 8000.
t = np.arange(64)/fs
assert np.max(abs(np.cos(2*np.pi*6000*t)
                  -np.cos(2*np.pi*2000*t))) < 1e-11
x, h = np.array([1., 2., 3.]), np.array([1., -.5, .25])
linear = np.convolve(x, h)
circular = np.fft.ifft(np.fft.fft(x, 3)*np.fft.fft(h, 3)).real
padded = np.fft.ifft(np.fft.fft(x, 5)*np.fft.fft(h, 5)).real
folded = np.array([linear[i::3].sum() for i in range(3)])
assert np.allclose(circular, folded)
assert np.allclose(padded, linear)
print(linear, circular)
