import numpy as np
fs = 16000
n = 7200
u = np.arange(n)/(n-1)
f0 = 140 + 50*u
phase = 2*np.pi*np.cumsum(f0)/fs
sound = sum(np.sin(k*phase)/k for k in range(1,9))
recovered_hz = np.diff(phase)*fs/(2*np.pi)
assert np.allclose(recovered_hz, f0[1:])
print('samples:', len(sound), 'F0 endpoints:', f0[0], f0[-1])
