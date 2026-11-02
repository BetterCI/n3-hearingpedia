import numpy as np
from scipy.signal import place_poles
A=np.array([[0.,1.],[-2.,-.6]])
B=np.array([[0.],[1.]])
C=np.array([[1.,0.]])
assert np.linalg.matrix_rank(np.hstack([B,A@B]))==2
assert np.linalg.matrix_rank(np.vstack([C,C@A]))==2
K=place_poles(A,B,[-2.,-3.],method="YT").gain_matrix
Lo=place_poles(A.T,C.T,[-4.,-5.],method="YT").gain_matrix.T
F=np.block([[A-B@K,B@K],[np.zeros((2,2)),A-Lo@C]])
assert np.allclose(np.sort(np.linalg.eigvals(F)),[-5,-4,-3,-2])
print("K",K,"Lo",Lo,"poles",np.linalg.eigvals(F))
