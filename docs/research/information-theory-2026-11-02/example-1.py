import numpy as np
def H(p):
    p = np.asarray(p, float)
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))
prior = np.full(4, .25)
W = np.full((4, 4), .1)
np.fill_diagonal(W, .7)
assert np.all(W >= 0) and np.allclose(W.sum(axis=1), 1)
assert np.all(prior >= 0) and np.isclose(prior.sum(), 1)
joint = prior[:, None] * W
hx, hy, hxy = H(joint.sum(axis=1)), H(joint.sum(axis=0)), H(joint.ravel())
print('H(X), H(X|Y), I(X;Y), accuracy:', hx, hxy-hy, hx+hy-hxy, np.trace(joint))
