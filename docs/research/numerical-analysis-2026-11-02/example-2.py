import numpy as np
t = np.linspace(-1, 1, 31)
A = np.column_stack([np.ones_like(t), t, t*t])
truth = np.array([0.3, 0.8, -0.2])
b = A@truth + np.random.default_rng(20261102).normal(0, 0.02, len(t))
Q, R = np.linalg.qr(A, mode="reduced")
x = np.linalg.solve(R, Q.T@b)
reference = np.linalg.lstsq(A, b, rcond=None)[0]
assert np.allclose(x, reference, atol=1e-12, rtol=1e-12)
assert np.linalg.norm(A.T@(b-A@x)) < 1e-12
print(x, np.linalg.norm(b-A@x))
