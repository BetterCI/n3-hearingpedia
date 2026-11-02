import numpy as np
from scipy.signal import cont2discrete
A=np.array([[-1.]])
B=C=np.array([[1.]])
D=np.array([[0.]])
for h in [.1,.4,.6]:
    Ad,Bd,_,_,_=cont2discrete((A,B,C,D),h,method="zoh")
    pole=float((Ad-4*Bd)[0,0])
    assert np.isclose(pole,5*np.exp(-h)-4)
    print(h,pole,"stable",abs(pole)<1,"continuous",np.exp(-5*h))
