import numpy as np
A, B = 0.0, 0.0
for _ in range(20):
    A += 0.2 * (1 - A)
for _ in range(15):
    error = 1 - A - B
    A, B = A + 0.2 * error, B + 0.2 * error
expected_B = 0.8**20 * (1 - 0.6**15) / 2
print(A, B, expected_B)
assert np.isclose(B, expected_B)
