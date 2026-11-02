"""Independent analytic, numerical, convention and asset checks for the wavelet entry."""
from pathlib import Path
import importlib.util,sys,json,hashlib,xml.etree.ElementTree as ET
sys.dont_write_bytecode=True
import numpy as np,pywt
from scipy.integrate import quad
from scipy.special import erf
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/wavelet-analysis-2026-11-02'
spec=importlib.util.spec_from_file_location('wa',ROOT/'public/code/wavelet-analysis/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
checks=[]
def check(name,condition,**evidence):
    assert condition,(name,evidence)
    checks.append(dict(name=name,passed=True,**evidence))
A=2/(np.sqrt(3)*np.pi**.25);mex=lambda u:A*(1-u*u)*np.exp(-u*u/2)
check('Mexican hat zero mean and unit L2 norm',abs(quad(mex,-12,12)[0])<1e-12 and abs(quad(lambda u:mex(u)**2,-12,12)[0]-1)<1e-12)
fourier=lambda w:A*np.sqrt(2*np.pi)*w*w*np.exp(-w*w/2)
c=quad(lambda w:fourier(w)**2/w,0,np.inf)[0]
check('Positive-frequency admissibility constant, not double-sided constant',abs(c-4*np.sqrt(np.pi)/3)<1e-11,value=c)
w=.8;numeric=quad(lambda t:mex(t)*np.cos(w*t),-12,12)[0]
check('Mexican hat Fourier convention',abs(numeric-fourier(w))<1e-12)
# Gaussian x: exact time-integrated CWT energy, then independent scale quadrature.
energy=quad(lambda a:A*A*1.5*np.pi**1.5*a**3/(1+a*a)**2.5,0,np.inf)[0]
check('Real-mother CWT energy factor on Gaussian input',abs(energy-c*np.sqrt(np.pi))<1e-9,scale_time_integral=energy,expected=float(c*np.sqrt(np.pi)))
a,b=.8,.3
direct=quad(lambda t:np.exp(-t*t/2)*mex((t-b)/a)/np.sqrt(a),-12,12)[0]
analytic=A*np.sqrt(2*np.pi)*a**2.5/(1+a*a)**1.5*(1-b*b/(1+a*a))*np.exp(-b*b/(2*(1+a*a)))
check('Independent analytic Gaussian-Mexican-hat convolution',abs(direct-analytic)<1e-12)
mean=quad(lambda u:m.morlet(u).real,-12,12)[0];norm=quad(lambda u:abs(m.morlet(u))**2,-12,12)[0]
check('Corrected Morlet zero mean and normalization',abs(mean)<1e-12 and abs(norm-1)<1e-12,mean=mean,norm=norm)
for a in [.25,.5,1.]:
    assert abs(quad(lambda t:abs(m.morlet(t/a)/np.sqrt(a))**2,-12,12)[0]-1)<1e-10
check('Dilation preserves L2 norm',True)
# Sampling at twice the rate approximates the same physical integral at a center point.
sample=[]
for fs in [1024,2048]:
    t=np.arange(-1,1,1/fs);x=np.cos(2*np.pi*60*t);sample.append(m.cwt_physical(x,1/fs,[.016])[0,len(t)//2])
check('Physical dt-weighted CWT invariant under sample-rate refinement',abs(sample[0]-sample[1])<1e-10,absolute_difference=float(abs(sample[0]-sample[1])))
t=np.arange(1024)/1024;x=np.cos(2*np.pi*60*t)
c1,f1=pywt.cwt(x,[8,16,32],'cmor1.5-1.0',sampling_period=1/1024)
c2,f2=pywt.cwt(x,[8,16,32],'cmor1.5-1.0',sampling_period=1/2048)
check('PyWavelets sampling_period alters frequencies, not coefficients',np.array_equal(c1,c2) and np.allclose(f2,2*f1),runtime=pywt.__version__)
U=m.haar_matrix(8);v=np.array([4,6,10,12,8,8,2,2.]);expected=np.array([13*np.sqrt(2),3*np.sqrt(2),-6,6,-np.sqrt(2),-np.sqrt(2),0,0])
check('Haar manual coefficients and orthogonal analysis matrix',np.allclose(U@v,expected) and np.allclose(U.T@U,np.eye(8)))
lib=pywt.wavedec(v,'haar',mode='periodization',level=3)
check('Manual Haar agrees with library coefficients and energy 432',np.allclose(np.concatenate(lib),expected) and np.isclose(v@v,432) and np.isclose(sum(c@c for c in lib),432))
rng=np.random.default_rng(21);v=rng.normal(size=256)
parts=m.filter_bank(v);err=float(np.max(abs(sum(parts)-np.roll(v,1))))
check('Explicit even-phase two-channel filter bank has exactly one-sample delay',err<1e-12,max_error=err)
omega=np.linspace(0,2*np.pi,257);z=np.exp(-1j*omega);h0=(1+z)/np.sqrt(2);h1=(-1+z)/np.sqrt(2)
distortion=(h0*h0-h1*h1)/2;alias=(h0*(1-z)/np.sqrt(2)-h1*(-1-z)/np.sqrt(2))/2
check('Independent z-domain distortion and alias cancellation',np.allclose(distortion,z) and np.max(abs(alias))<1e-14)
_,details=m.moment_example();interior=details['db4'][8:120]
check('db4 four vanishing moments annihilate interior cubic, Haar does not',np.max(abs(interior))<1e-12 and np.max(abs(details['haar'][8:120]))>1e-4,max_db4_interior=float(np.max(abs(interior))))
db=pywt.Wavelet('db4');check('db4 means four moments and eight taps',db.vanishing_moments_psi==4 and db.dec_len==8)
ratios={};reconstruction={}
for name in ['db4','bior4.4']:
    cs=pywt.wavedec(v,name,mode='periodization',level=3);ratios[name]=float(sum(c@c for c in cs)/(v@v));reconstruction[name]=float(np.max(abs(pywt.waverec(cs,name,mode='periodization')-v)))
check('Biorthogonal PR does not imply ordinary coefficient-energy equality',max(reconstruction.values())<1e-10 and abs(ratios['db4']-1)<1e-12 and abs(ratios['bior4.4']-1)>.01,ratios=ratios,reconstruction=reconstruction)
for mode in ['zero','symmetric','periodic','periodization']:
    cs=pywt.wavedec(v,'db4',mode=mode,level=3);assert np.allclose(pywt.waverec(cs,'db4',mode=mode)[:len(v)],v)
check('Four boundary modes each reconstruct with matching analysis and synthesis',True)
sh=m.shift_example();errs={name:float(np.max(abs(sh[name]-sh[name+'_shift']))) for name in ['dwt','swt']}
check('Fixed-threshold circular SWT equivariance versus decimated DWT',errs['swt']<1e-12 and errs['dwt']>.1,max_errors=errs)
swt=pywt.swt(v,'db4',level=3,norm=True,trim_approx=True)
check('SWT energy only with stated orthogonal norm-and-trim settings',np.isclose(sum(c@c for c in swt),v@v))
den=m.denoising_example();manual=np.sign(np.array([-2.,-.2,0,.2,2]))*np.maximum(np.abs([-2.,-.2,0,.2,2])-.7,0)
check('Soft-threshold formula and robust normal MAD constant',np.allclose(manual,pywt.threshold(np.array([-2.,-.2,0,.2,2]),.7,'soft')) and abs(erf(.6744897501960817/np.sqrt(2))-.5)<1e-12)
check('Reproduced fixed-seed denoising values without tuning to truth',abs(den['sigma']-.2019597143928377)<1e-12 and abs(den['mse']['soft']-.005714698295101921)<1e-12,**dict(sigma=den['sigma'],threshold=den['threshold'],mse=den['mse']))
paths,e=m.packet_example();check('Packet frequency order, energy conservation and nonideal passbands',paths==['aaa','aad','add','ada','dda','ddd','dad','daa'] and paths[int(e.argmax())]=='add' and np.isclose(e.sum(),512) and e.max()/e.sum()<.5)
wx=np.array([1+2j,3-1j]);wy=np.array([2-1j,-1+3j]);trivial=abs(wx*np.conj(wy))**2/(abs(wx)**2*abs(wy)**2)
check('Unsmoothed coherence degenerates to one',np.allclose(trivial,1))
check('Independent-test example is numerically correct',abs((1-.95**100)-.994079470779666)<1e-13,probability=float(1-.95**100))
source=json.loads((REC/'source-index.json').read_text(encoding='utf-8'))
for row in source:
    assert row['status']=='fetched';path=ROOT/'artifacts/wavelet-analysis/sources'/(row['id']+('.pdf' if row['kind']=='original_paper' else '.html'))
    assert hashlib.sha256(path.read_bytes()).hexdigest()==row['sha256']
check('All primary-source and official-doc cache hashes match',len(source)==17,files=len(source))
paths=list((ROOT/'public/figures/wavelet-analysis').glob('*.svg'));paths.append(ROOT/'public/figures/foundation-courses/wavelet-analysis.svg')
for path in paths:
    ET.parse(path);s=path.read_text(encoding='utf-8');assert '<script' not in s
check('Eleven original SVG files parse',len(paths)==11)
result=dict(slug='wavelet-analysis',check_groups=len(checks),checks=checks,professional_review='pending')
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(check_groups=len(checks),passed=len(checks),professional_review='pending')))
