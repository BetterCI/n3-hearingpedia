import numpy as np
fold = 2/(3*np.sqrt(3))
print('fold h:', -fold, fold)
for h in [-.5, 0., .5]:
    roots = np.roots([1., 0., -1., -h])
    real = np.sort(roots.real[np.abs(roots.imag) < 1e-9])
    derivative = 1-3*real**2
    print('h, equilibria, derivatives:', h, real, derivative)
    if h == 0.:
        assert np.allclose(real, [-1, 0, 1])
        assert np.allclose(derivative, [-2, 1, -2])
