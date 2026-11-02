import numpy as np
from scipy.special import expit
X = np.array([[.2, -.4], [1., .3], [-.5, .8]])
y = np.array([0., 1., 1.])
theta = np.array([.3, -.2, .5, .4, .1, -.1, .7, -.6, .05])

def loss_grad(t):
    W, b, v, c = t[:4].reshape(2, 2), t[4:6], t[6:8], t[8]
    h = np.tanh(X @ W + b)
    z = h @ v + c
    delta = (expit(z) - y) / len(y)
    hidden = delta[:, None] * v * (1 - h*h)
    grad = np.r_[(X.T @ hidden).ravel(), hidden.sum(0),
                 h.T @ delta, delta.sum()]
    return np.mean(np.logaddexp(0, z) - y*z), grad

eps = 1e-5
numeric = np.array([(loss_grad(theta + eps*e)[0] -
                     loss_grad(theta - eps*e)[0]) / (2*eps)
                    for e in np.eye(len(theta))])
loss, grad = loss_grad(theta)
print(loss, np.max(np.abs(grad - numeric)))
assert np.allclose(grad, numeric, atol=1e-8)
