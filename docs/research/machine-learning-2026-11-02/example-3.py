import numpy as np
X = np.array([(a, b) for a in [-3., -1., 1., 3.] for b in [-.2, .2]])
labels = (X[:, 1] > 0).astype(int)
Xc = X - X.mean(axis=0)
U, s, Vt = np.linalg.svd(Xc, full_matrices=False)
Z = Xc @ Vt[:1].T
reconstruction = Z @ Vt[:1]
print("variance fraction", s[0]**2 / np.sum(s*s))  # 约0.99206349
print("MSE per entry", np.mean((Xc-reconstruction)**2))  # 0.02
print(np.column_stack([Z[:, 0], labels]))
