import numpy as np
R, C = 100e6, 200e-12
EL, reset, threshold = -.065, -.065, -.050
current, refractory = .2e-9, .002
tau = R*C
steady = EL + R*current
assert steady > threshold > reset
crossing = tau*np.log((steady-reset)/(steady-threshold))
print('tau, first event (ms):', tau*1000, crossing*1000)
print('steady rate (Hz):', 1/(refractory+crossing))
