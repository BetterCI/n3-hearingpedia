"""Complex analysis through acoustics. Synthetic teaching models, not measurements.
Requires Python 3.10+, NumPy and SciPy. No files are read or written.
"""
import numpy as np
from scipy import signal, integrate

def main():
    t=np.arange(16000)/16000
    P=.02*np.exp(1j*np.pi/3)
    wave=np.real(P*np.exp(1j*2*np.pi*1000*t))
    np.testing.assert_allclose(wave,.02*np.cos(2*np.pi*1000*t+np.pi/3),atol=1e-12)
    V=1e-4*np.exp(-1j*np.pi/3)
    print('Specific impedance (Pa s/m):',.02/V)
    print('Mean intensity (W/m^2), peak phasors:',.5*np.real(.02*np.conj(V)))
    for phase in [0,2*np.pi/3,np.pi]:
        print('Phase difference and sum amplitude:',phase,abs(.2*(1+np.exp(1j*phase))))

    z1=np.exp(1j*3*np.pi/4)
    gap=2*np.log(z1)-np.log(z1*z1)
    np.testing.assert_allclose(gap,2j*np.pi,atol=1e-12)
    print('Principal log product-rule discrepancy:',gap)

    a=.8
    angle=2*np.pi*np.arange(8192)/8192
    def coefficient(n,radius):
        z=radius*np.exp(1j*angle)
        return np.mean(z/(z-a)*z**n)
    for n in [-2,-1,0,1,2]:
        outside,inside=coefficient(n,1.2),coefficient(n,.4)
        assert abs(outside-(a**n if n>=0 else 0))<1e-10
        assert abs(inside-(-a**n if n<=-1 else 0))<1e-10
        print('Inverse-Z n, causal, anticausal:',n,outside.real,inside.real)

    fs=16000
    theta0=np.pi/8
    for r in [.95,.995]:
        den=[1,-2*r*np.cos(theta0),r*r]
        n=np.arange(1000)
        impulse=np.zeros(len(n));impulse[0]=1
        h=signal.lfilter([1],den,impulse)
        manual=np.zeros(len(n))
        for k in range(len(n)):
            manual[k]=impulse[k]
            if k>=1: manual[k]-=den[1]*manual[k-1]
            if k>=2: manual[k]-=den[2]*manual[k-2]
        exact=r**n*np.sin((n+1)*theta0)/np.sin(theta0)
        np.testing.assert_allclose(h,manual,atol=1e-11)
        np.testing.assert_allclose(h,exact,atol=1e-11)
        f=np.array([600.,1000.,1400.])
        _,H=signal.freqz([1],den,worN=f,fs=fs)
        z=np.exp(1j*2*np.pi*f/fs)
        np.testing.assert_allclose(H,1/(1+den[1]/z+den[2]/z**2),atol=1e-11)
        peak=fs/(2*np.pi)*np.arccos((1+r*r)*np.cos(theta0)/(2*r))
        print('r, pole-angle Hz, exact peak Hz, decay ms:',r,1000,peak,-1000/(fs*np.log(r)))

    area,error=integrate.quad(lambda u:1/(1+u*u),0,np.inf)
    assert abs(area-np.pi/2)<1e-10
    print('Lowpass one-sided squared-response area, fc=1000 Hz:',1000*area,'Hz')
    print('All checks use explicit time, phase and region-of-convergence conventions.')

if __name__=='__main__': main()
