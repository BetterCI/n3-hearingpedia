import numpy as np
def total_spl(L1, L2, r12):
    assert -1 <= r12 <= 1
    a, b = 10**(L1/20), 10**(L2/20)
    mean_square_ratio = a*a+b*b+2*r12*a*b
    return 10*np.log10(mean_square_ratio) if mean_square_ratio > 0 else -np.inf
uncorrelated = total_spl(70, 70, 0)
in_phase = total_spl(70, 70, 1)
opposite = total_spl(70, 70, -1)
assert np.isclose(uncorrelated, 73.0102999566)
assert np.isclose(in_phase, 76.0205999133)
assert np.isneginf(opposite)
print('Uncorrelated, in phase, ideal opposite / dB:', uncorrelated, in_phase, opposite)
