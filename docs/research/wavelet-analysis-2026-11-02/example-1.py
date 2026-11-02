import numpy as np
import pywt
x = np.array([4., 6., 10., 12., 8., 8., 2., 2.])
c = pywt.wavedec(x, 'haar', mode='periodization', level=3)
expected = np.array([13*np.sqrt(2), 3*np.sqrt(2), -6, 6,
                     -np.sqrt(2), -np.sqrt(2), 0, 0])
assert np.allclose(np.concatenate(c), expected)
y = pywt.waverec(c, 'haar', mode='periodization')
assert np.allclose(y, x)
assert np.isclose(sum(v @ v for v in c), x @ x)
print('Haar coefficients:', np.concatenate(c))
print('Input and coefficient energies:', x @ x, sum(v @ v for v in c))
