import numpy as np
n = np.arange(1, 61)
sigma = np.exp(-.15*n)
truth = 1/n**2
eta = np.cos(1.7*n)
eta *= .001/np.linalg.norm(eta)
y = sigma*truth+eta
alpha = 1e-4
modal = sigma*y/(sigma**2+alpha)
matrix = np.linalg.solve(np.diag(sigma**2)+alpha*np.eye(len(n)), sigma*y)
raw = y/sigma
print(np.linalg.norm(raw-truth), np.linalg.norm(modal-truth))
assert np.allclose(modal, matrix)
assert np.linalg.norm(modal-truth) < np.linalg.norm(raw-truth)
