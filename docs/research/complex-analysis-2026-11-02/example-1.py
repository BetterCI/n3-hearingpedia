import numpy as np

f = 1000
t = np.arange(16000) / 16000
P = 0.02 * np.exp(1j*np.pi/3)
wave = np.real(P * np.exp(1j*2*np.pi*f*t))
assert np.max(np.abs(wave - 0.02*np.cos(2*np.pi*f*t+np.pi/3))) < 1e-12
V = 1e-4 * np.exp(-1j*np.pi/3)
pressure = 0.02 + 0j
Zs = pressure / V
intensity = 0.5 * np.real(pressure * np.conj(V))
assert abs(intensity - 5e-7) < 1e-18
print("比声阻抗 Pa s/m:", Zs)
print("平均声强 W/m^2:", intensity)
