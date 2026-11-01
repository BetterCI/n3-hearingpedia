import numpy as np
n = np.arange(8)
B = np.column_stack([np.cos(2*np.pi*1000*n/8000),
                     np.cos(2*np.pi*1100*n/8000)])
y = B @ np.array([0.6, 0.3])
separate = (B.T @ y) / np.sum(B*B, axis=0)
joint = np.linalg.lstsq(B, y, rcond=None)[0]
print(separate)  # 约 [0.89785205, 0.84454225]
print(joint)     # [0.6, 0.3]
assert np.allclose(joint, [0.6, 0.3])
