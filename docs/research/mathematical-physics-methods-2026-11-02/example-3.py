import numpy as np
errors = []
for M in [20, 40, 80]:
    h = 1/M
    K = (2*np.eye(M-1)-np.eye(M-1, k=1)-np.eye(M-1, k=-1))/h**2
    first = np.linalg.eigvalsh(K)[0]
    errors.append(abs(first-np.pi**2))
print(errors, np.array(errors[:-1])/errors[1:])
assert 3.9 < errors[0]/errors[1] < 4.1
assert 3.9 < errors[1]/errors[2] < 4.1
