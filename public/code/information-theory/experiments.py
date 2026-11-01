"""Runnable information-theory examples; requires NumPy. Original synthetic teaching models."""

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


codes = {'A': '0', 'B': '10', 'C': '110', 'D': '111'}
words = list(codes.values())
assert all(not b.startswith(a) for a in words for b in words if a != b)
message = 'ABACADABAA'
stream = ''.join(codes[c] for c in message)
inverse = {v: k for k, v in codes.items()}
decoded, prefix = '', ''
for bit in stream:
    prefix += bit
    if prefix in inverse:
        decoded += inverse[prefix]
        prefix = ''
assert not prefix and decoded == message
print('Encoded bits:', len(stream), 'Fixed length:', 2*len(message))


import numpy as np
def H(p):
    p = np.asarray(p, float)
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))
rng = np.random.default_rng(20261102)
for N in [40, 200, 1000]:
    estimates = []
    for _ in range(400):
        joint = rng.multinomial(N, np.full(16, 1/16)).reshape(4, 4) / N
        estimates.append(H(joint.sum(axis=1)) + H(joint.sum(axis=0)) - H(joint.ravel()))
    print(N, float(np.mean(estimates)), 'True MI: 0')
