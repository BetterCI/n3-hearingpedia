import numpy as np
import pywt
n = 1024
t = np.arange(n) / 1024
clean = ((t >= .2) & (t < .5)).astype(float)
clean -= .5 * ((t >= .5) & (t < .75))
clean += .5 * np.exp(-.5 * ((t - .63) / .015)**2)
noisy = clean + np.random.default_rng(20261102).normal(0, .2, n)
c = pywt.wavedec(noisy, 'db4', mode='periodization', level=4)
sigma = np.median(np.abs(c[-1] - np.median(c[-1]))) / .6744897501960817
threshold = sigma * np.sqrt(2*np.log(n))
print('sigma, threshold:', sigma, threshold)
print('noisy MSE:', np.mean((noisy-clean)**2))
for mode in ['soft', 'hard']:
    modified = [c[0]] + [pywt.threshold(v, threshold, mode=mode) for v in c[1:]]
    y = pywt.waverec(modified, 'db4', mode='periodization')[:n]
    print(mode, 'MSE:', np.mean((y-clean)**2))
