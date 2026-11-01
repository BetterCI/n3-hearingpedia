import numpy as np
rng = np.random.default_rng(20261108)
frequency = 500.
for sigma in [.0001, .0005]:
    timing_error = rng.normal(0, sigma, 2000)
    phase = 2*np.pi*frequency*timing_error
    sample_vs = abs(np.exp(1j*phase).mean())
    population_vs = np.exp(-.5*(2*np.pi*frequency*sigma)**2)
    print('sigma (ms), sample VS, population VS:', sigma*1000, sample_vs, population_vs)
print('single phase sample VS:', abs(np.exp(1j*.7)))
