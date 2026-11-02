import numpy as np
from scipy.linalg import eigh
M = np.diag([.02, .03])
K = np.array([[140., -60.], [-60., 180.]])
values, modes = eigh(K, M)
frequencies = np.sqrt(values)/(2*np.pi)
assert np.allclose(K @ modes, (M @ modes) * values)
assert np.allclose(modes.T @ M @ modes, np.eye(2))
assert np.allclose(values, [4000., 9000.])
print('Natural frequencies / Hz:', frequencies)
print('Mass-normalized modes:', modes)
