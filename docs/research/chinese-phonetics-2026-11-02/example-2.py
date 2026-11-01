import numpy as np
f0 = np.array([130., 195., np.nan, 260.])
reference_hz = 130.
semitones = np.full_like(f0, np.nan)
valid = np.isfinite(f0) & (f0 > 0)
semitones[valid] = 12 * np.log2(f0[valid] / reference_hz)
t = np.array([.20, .25, .30, .35])
normalized_time = (t-t[0])/(t[-1]-t[0])
print('semitones:', semitones, 'normalized time:', normalized_time)
