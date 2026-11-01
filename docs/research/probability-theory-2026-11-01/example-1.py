from math import comb, erf, sqrt

tail = sum(comb(40, k) for k in range(30, 41)) / 2**40
Phi = lambda z: (1 + erf(z / sqrt(2))) / 2
area = Phi(0.5) - Phi(-0.5)
assert abs(tail - 0.0011107168866146822) < 1e-14
assert abs(area - 0.38292492254802624) < 1e-14
print("机会水平下至少30/40:", tail)
print("声压落在±0.01 Pa内:", area)
