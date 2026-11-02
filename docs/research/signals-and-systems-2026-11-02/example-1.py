import numpy as np
n = np.arange(160)
x = np.exp(-.5*((n-24)/6)**2)
h = np.zeros(97)
h[[0, 40, 96]] = [1., .55, -.25]
y = np.convolve(x, h)
A = np.zeros((len(x)+len(h)-1, len(x)))
for k in range(len(x)):
    A[k:k+len(h), k] = h
assert np.max(abs(y-A@x)) < 1e-12
print(len(y), np.sum(h), np.sum(y)-np.sum(x)*np.sum(h))
