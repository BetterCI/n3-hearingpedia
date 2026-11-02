import numpy as np
from scipy.special import logsumexp
z = np.array([[[2., 0.], [100., -100.], [-100., 100.]],
              [[0., 2.], [2., 0.], [0., 2.]]])
y = np.array([[0, 0, 0], [1, 0, 1]])
valid = np.arange(3)[None, :] < np.array([1, 3])[:, None]
scores, labels = z[valid], y[valid]
loss = np.mean(logsumexp(scores, axis=1) -
               scores[np.arange(len(labels)), labels])
print(valid.sum(), loss)
assert valid.sum() == 4
assert np.isclose(loss, np.logaddexp(0, -2))
