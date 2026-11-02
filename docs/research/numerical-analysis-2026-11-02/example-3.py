import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
errors = []
for N in [16, 32, 64]:
    h = 1/N
    x = np.arange(1, N)*h
    A = diags([-np.ones(N-2), 2*np.ones(N-1), -np.ones(N-2)],
              [-1, 0, 1], format="csc")/(h*h)
    y = spsolve(A, np.pi**2*np.sin(np.pi*x))
    errors.append(np.max(np.abs(y-np.sin(np.pi*x))))
ratios = np.array(errors[:-1])/np.array(errors[1:])
assert np.all((ratios > 3.9) & (ratios < 4.1))
print(errors, ratios)
