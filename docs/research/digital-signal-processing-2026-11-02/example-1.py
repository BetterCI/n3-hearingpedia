import numpy as np
from scipy import signal
fs, N = 16000, 256
n = np.arange(N)
x = 0.8 * np.cos(2*np.pi*2000*n/fs)
w = signal.windows.hann(N, sym=False)
X = np.fft.rfft(w*x)
amplitude = 2*abs(X[32])/w.sum()  # 内部正频率，不适用于DC/Nyquist
f, psd = signal.periodogram(x, fs=fs, window=w, detrend=False,
                            return_onesided=True, scaling="density")
integral = psd.sum()*(f[1]-f[0])
weighted_ms = np.sum((w*x)**2)/np.sum(w*w)
assert np.isclose(amplitude, 0.8)
assert np.isclose(integral, weighted_ms)
print(amplitude, fs*np.sum(w*w)/w.sum()**2, integral)
