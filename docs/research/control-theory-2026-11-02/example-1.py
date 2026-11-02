import numpy as np
for gain in [2.,5.,6.,8.]:
    poles=np.roots([1.,3.,2.,gain])
    print(gain,poles)
    if gain<6:
        assert np.max(poles.real)<0
    elif gain>6:
        assert np.count_nonzero(poles.real>0)==2
    else:
        assert np.allclose(np.sort(poles.imag),[-np.sqrt(2),0,np.sqrt(2)])
