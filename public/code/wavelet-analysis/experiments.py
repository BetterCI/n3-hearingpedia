"""Original wavelet teaching experiments. Python 3.11, NumPy, SciPy, PyWavelets 1.8.0.
No recordings, participant data or trained models. Run as a script for summary JSON.
"""
import numpy as np
import pywt
from scipy.signal import fftconvolve,chirp

def morlet(u,w0=6.):
    norm=np.sqrt(1+np.exp(-w0*w0)-2*np.exp(-3*w0*w0/4))
    return np.pi**(-.25)*(np.exp(1j*w0*u)-np.exp(-w0*w0/2))*np.exp(-u*u/2)/norm

def cwt_physical(x,dt,scales):
    """Riemann-sum approximation: integral x(t) conj(psi_ab(t)) dt; zero exterior."""
    rows=[]
    for a in scales:
        radius=int(np.ceil(8*a/dt));lag=np.arange(-radius,radius+1)*dt
        kernel=np.conj(morlet(-lag/a))*dt/np.sqrt(a)
        rows.append(fftconvolve(x,kernel,mode='same'))
    return np.asarray(rows)

def sound_example():
    fs=1024;n=2048;t=np.arange(n)/fs
    x=.7*chirp(t,f0=20,f1=120,t1=2,method='linear')
    x+=1.2*np.exp(-.5*((t-1.3)/.025)**2)*np.cos(2*np.pi*100*(t-1.3))
    frequencies=np.geomspace(15,160,128)
    kappa=(6+np.sqrt(38))/(4*np.pi);scales=kappa/frequencies
    w=cwt_physical(x,1/fs,scales)
    return t,x,frequencies,scales,w

def haar_matrix(n):
    assert n>0 and n&(n-1)==0
    rows=[]
    for x in np.eye(n):
        a=x.copy();details=[]
        while len(a)>1:
            details.append((a[::2]-a[1::2])/np.sqrt(2));a=(a[::2]+a[1::2])/np.sqrt(2)
        rows.append(np.concatenate([a]+details[::-1]))
    return np.asarray(rows).T

def filter_bank(x):
    """Circular, causal FIRs; retain even-indexed samples; one-sample PR delay."""
    h0=np.array([1.,1.])/np.sqrt(2);h1=np.array([-1.,1.])/np.sqrt(2)
    def filt(x,h):return sum(v*np.roll(x,k) for k,v in enumerate(h))
    parts=[]
    for h,g in [(h0,h0),(h1,-h1)]:
        a=filt(x,h)[::2];up=np.zeros_like(x);up[::2]=a;parts.append(filt(up,g))
    return parts

def denoising_example():
    n=1024;t=np.arange(n)/1024
    clean=np.where((t>=.2)&(t<.5),1.,0.)+np.where((t>=.5)&(t<.75),-.5,0.)
    clean+=.5*np.exp(-.5*((t-.63)/.015)**2)
    noisy=clean+np.random.default_rng(20261102).normal(0,.2,n)
    c=pywt.wavedec(noisy,'db4',mode='periodization',level=4)
    sigma=np.median(np.abs(c[-1]-np.median(c[-1])))/.6744897501960817
    threshold=sigma*np.sqrt(2*np.log(n));out={}
    for mode in ['soft','hard']:
        changed=[c[0]]+[pywt.threshold(d,threshold,mode=mode) for d in c[1:]]
        out[mode]=pywt.waverec(changed,'db4',mode='periodization')[:n]
    mse={key:float(np.mean((v-clean)**2)) for key,v in dict(noisy=noisy,**out).items()}
    return dict(t=t,clean=clean,noisy=noisy,sigma=float(sigma),threshold=float(threshold),mse=mse,**out)

def shift_example():
    n=256;t=np.arange(n);x=np.exp(-.5*((t-93)/5)**2)+.4*(t>=160)
    def den(x,stationary):
        if stationary:
            c=pywt.swt(x,'haar',level=3,norm=False)
            return pywt.iswt([(a,pywt.threshold(d,.2,'soft')) for a,d in c],'haar',norm=False)
        c=pywt.wavedec(x,'haar',mode='periodization',level=3)
        return pywt.waverec([c[0]]+[pywt.threshold(d,.2,'soft') for d in c[1:]],'haar',mode='periodization')
    return dict(x=x,dwt=den(x,False),dwt_shift=np.roll(den(np.roll(x,1),False),-1),swt=den(x,True),swt_shift=np.roll(den(np.roll(x,1),True),-1))

def packet_example():
    fs=1024;t=np.arange(1024)/fs;x=np.cos(2*np.pi*160*t)
    wp=pywt.WaveletPacket(x,'haar',mode='periodization',maxlevel=3)
    nodes=wp.get_level(3,order='freq');energy=np.array([np.sum(p.data**2) for p in nodes])
    return [p.path for p in nodes],energy

def boundary_example():
    x=np.linspace(0,1,128);out={}
    for mode in ['zero','symmetric','periodization']:
        c=pywt.wavedec(x,'db4',mode=mode,level=3)
        out[mode]=pywt.waverec([c[0]]+[np.zeros_like(d) for d in c[1:]],'db4',mode=mode)[:len(x)]
    return x,out

def moment_example():
    x=(np.arange(256)/255)**3;out={}
    for name in ['haar','db4']:
        _,d=pywt.dwt(x,name,mode='zero');out[name]=d
    return x,out

def summary():
    x=np.array([4.,6.,10.,12.,8.,8.,2.,2.]);u=haar_matrix(8);den=denoising_example();sh=shift_example();paths,e=packet_example()
    rng=np.random.default_rng(21);v=rng.normal(size=256);bior=pywt.wavedec(v,'bior4.4',mode='periodization',level=3)
    return dict(haar_coefficients=(u@x).tolist(),haar_energy=float(x@x),haar_orthogonality_error=float(np.max(abs(u@u.T-np.eye(8)))),
        filterbank_max_error=float(np.max(abs(sum(filter_bank(v))-np.roll(v,1)))),
        denoising=dict(sigma=den['sigma'],threshold=den['threshold'],mse=den['mse']),
        shift_max_error={name:float(np.max(abs(sh[name]-sh[name+'_shift']))) for name in ['dwt','swt']},
        packet_paths=paths,packet_energy_fraction=(e/e.sum()).tolist(),
        biorthogonal_energy_ratio=float(sum(c@c for c in bior)/(v@v)),biorthogonal_reconstruction_error=float(np.max(abs(pywt.waverec(bior,'bior4.4',mode='periodization')-v))))

if __name__=='__main__':
    import json
    print(json.dumps(summary(),ensure_ascii=False,indent=2))
