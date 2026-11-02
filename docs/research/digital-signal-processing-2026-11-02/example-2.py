import numpy as np
from scipy import signal
sos = signal.butter(6, 3000, fs=16000, output="sos")
x = np.random.default_rng(1003).normal(size=2048)
whole = signal.sosfilt(sos, x)
zi = np.zeros((len(sos), 2))
blocks = []
for start in range(0, len(x), 127):
    y, zi = signal.sosfilt(sos, x[start:start+127], zi=zi)
    blocks.append(y)
stream = np.concatenate(blocks)
assert np.allclose(stream, whole, atol=1e-12, rtol=1e-12)
print(np.max(np.abs(stream-whole)))
