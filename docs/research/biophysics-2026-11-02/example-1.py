import numpy as np
kB, NA, e = 1.380649e-23, 6.02214076e23, 1.602176634e-19
R, F, T = NA*kB, NA*e, 310.
for name, z, cin, cout in [("K", 1, 140., 5.),
                           ("Na", 1, 12., 145.),
                           ("Cl", -1, 10., 120.)]:
    E = R*T/(z*F)*np.log(cout/cin)
    residual = R*T*np.log(cin/cout)+z*F*E
    print(name, E*1000, "mV", residual, "J/mol")
    assert abs(residual) < 1e-8
