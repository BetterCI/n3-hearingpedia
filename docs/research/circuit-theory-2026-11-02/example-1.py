import numpy as np
G = np.array([[1/1000+1/2000+1/1000, -1/1000],
              [-1/1000, 1/1000+1/1000]])
VA, VB = np.linalg.solve(G, np.array([1/1000, .0002]))
i = np.array([(1-VA)/1000, VA/2000, (VA-VB)/1000, VB/1000])
loss = np.sum(i*i*np.array([1000., 2000., 1000., 1000.]))
supply = 1*i[0] + VB*.0002
print(VA, VB)           # 约0.55 V、0.375 V
print(loss, supply)     # 均约0.000525 W
assert np.isclose(loss, supply)
