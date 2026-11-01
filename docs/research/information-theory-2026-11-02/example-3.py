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
