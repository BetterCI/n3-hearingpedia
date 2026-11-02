import numpy as np
from scipy.special import logsumexp
X = np.array([[1., 0.], [0., 1.], [1., 1.], [-1., 1.]])
allow = np.tril(np.ones((4, 4), dtype=bool))

def attend(x, causal):
    scores = x @ x.T / np.sqrt(x.shape[1])
    if causal:
        scores = np.where(allow, scores, -np.inf)
    A = np.exp(scores - logsumexp(scores, axis=1, keepdims=True))
    return A @ x

changed = X.copy()
changed[-1] = [6., -5.]
assert np.allclose(attend(X, True)[:3], attend(changed, True)[:3])
print("完整注意力前缀变化：",
      np.max(np.abs(attend(X, False)[:3] - attend(changed, False)[:3])))
