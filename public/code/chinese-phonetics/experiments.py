"""Original Chinese-phonetics calculation examples; requires NumPy; no natural speech is generated."""

fs = 16000
release = 800
for periodic_onset in [992, 1840]:
    vot_ms = (periodic_onset - release) / fs * 1000
    print('release ms:', release/fs*1000, 'onset ms:', periodic_onset/fs*1000, 'VOT ms:', vot_ms)


import numpy as np
f0 = np.array([130., 195., np.nan, 260.])
reference_hz = 130.
semitones = np.full_like(f0, np.nan)
valid = np.isfinite(f0) & (f0 > 0)
semitones[valid] = 12 * np.log2(f0[valid] / reference_hz)
t = np.array([.20, .25, .30, .35])
normalized_time = (t-t[0])/(t[-1]-t[0])
print('semitones:', semitones, 'normalized time:', normalized_time)


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
