import numpy as np
U, Z = 1+0j, 32+24j       # U采用RMS相量
I = U/Z
S = U*np.conj(I)
f = 1000.
t = np.arange(10000)/(10000*f)  # 一个周期，不重复末端点
u = np.sqrt(2)*np.real(U*np.exp(2j*np.pi*f*t))
i = np.sqrt(2)*np.real(I*np.exp(2j*np.pi*f*t))
print(I, S, np.mean(u*i))       # 0.02-0.015j A；0.02+0.015j VA；0.02 W
assert np.isclose(np.mean(u*i), S.real)
