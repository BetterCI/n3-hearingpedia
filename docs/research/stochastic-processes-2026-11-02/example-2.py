import numpy as np
from scipy.signal import periodogram
fs, f0 = 1000., 125.
for N in [256, 1024]:
    x = np.sqrt(2)*np.cos(2*np.pi*f0*np.arange(N)/fs+.7)
    f, S = periodogram(x, fs=fs, window='boxcar',
                       detrend=False, scaling='density')
    df = fs/N
    integral = S.sum()*df
    assert np.isclose(integral, np.mean(x*x))
    assert np.isclose(integral, 1.)
    assert np.isclose(S.max(), N/fs)
    print('N, peak Pa^2/Hz, integrated Pa^2:', N, S.max(), integral)
