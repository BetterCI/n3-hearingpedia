import numpy as np
rho, c, f = 1.2, 343., 500.
z0 = rho*c
x = np.linspace(0, c/f, 1001)
k = 2*np.pi*f/c
for R in [0., .6, 1.]:
    forward = np.sqrt(2)*np.exp(-1j*k*x)  # incident RMS pressure: 1 Pa
    backward = np.sqrt(2)*R*np.exp(1j*k*x)
    pressure = forward+backward
    velocity = (forward-backward)/z0
    intensity = .5*np.real(pressure*np.conj(velocity))
    expected = (1-R*R)/z0
    assert np.allclose(intensity, expected, atol=1e-14)
    print('R, net mean intensity / W m^-2:', R, intensity.mean())
