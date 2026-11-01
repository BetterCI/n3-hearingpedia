"""Independent enumerations, coding bounds, quadrature, distortion and PCM checks."""
from pathlib import Path
from itertools import product
import math
import json
import wave
import xml.etree.ElementTree as ET
import numpy as np
from scipy import integrate, optimize
from scipy.stats import binom

ROOT=Path(__file__).resolve().parents[1]
REC=ROOT/'docs/research/information-theory-2026-11-02'
d=json.loads((REC/'calculations.json').read_text(encoding='utf-8'))
checks=[]
def near(name,actual,expected,atol=1e-10):
    np.testing.assert_allclose(actual,expected,atol=atol,rtol=0);checks.append(name)
def require(name,value):
    assert value,name;checks.append(name)
def entropy(values):
    return -math.fsum(float(p)*math.log2(float(p)) for p in np.asarray(values).ravel() if p>0)
def direct_mi(joint):
    joint=np.asarray(joint);px=joint.sum(axis=1);py=joint.sum(axis=0)
    return math.fsum(joint[i,j]*math.log2(joint[i,j]/(px[i]*py[j]))
        for i,j in product(range(len(px)),range(len(py))) if joint[i,j]>0)
def kl(p,q):return math.fsum(a*math.log2(a/b) for a,b in zip(p,q) if a>0)

near('surprisal of probability one eighth',-math.log2(.125),3)
near('binary entropy p=.1',entropy([.1,.9]),d['entropy']['binary_p01'])
near('uniform four entropy',entropy([.25]*4),2)
near('certain entropy',entropy([0,1,0]),0)
near('one-to-one amplitude scaling preserves discrete entropy',entropy([.6,.2,.1,.1]),entropy([.1,.6,.1,.2]))
near('pressure gain two means square gain four',np.mean((2*np.arange(-5,6))**2),4*np.mean(np.arange(-5,6)**2))

counts=np.full((4,4),10);np.fill_diagonal(counts,70);joint=counts/400
near('joint table normalization',joint.sum(),1)
near('joint table direct KL mutual information',direct_mi(joint),d['confusion']['I_XY'])
post=joint/joint.sum(axis=0)[None,:]
cond=math.fsum(joint.sum(axis=0)[j]*entropy(post[:,j]) for j in range(4))
near('posterior-averaged conditional entropy',cond,d['confusion']['H_X_given_Y'])
near('chain rule from posterior distributions',entropy(joint),entropy(joint.sum(axis=0))+cond)
near('four-class Fano equality',cond,entropy([.3,.7])+.3*math.log2(3))
near('accuracy not an information percentage',np.trace(joint),.7)
require('incorrect accuracy-times-entropy formula differs',abs(.7*2-direct_mi(joint))>.5)
# A valid observation can increase posterior entropy while reducing it on average.
j=np.array([[.05,.85],[.05,.05]])
near('rare observation gives uniform posterior entropy',entropy(j[:,0]/j[:,0].sum()),1)
require('conditioning decreases entropy on average',sum(j[:,k].sum()*entropy(j[:,k]/j[:,k].sum()) for k in range(2))<entropy(j.sum(axis=1)))

p=np.array([.6,.2,.1,.1]);q=np.full(4,.25)
near('KL mismatch directly',kl(p,q),d['mismatch']['KL_PQ'])
near('reverse KL differs',kl(q,p),d['mismatch']['KL_QP'])
near('cross entropy decomposition',-sum(p*np.log2(q)),entropy(p)+kl(p,q))
near('entropy maximum through uniform KL',entropy(p)+kl(p,q),2)
near('identical distributions zero KL',kl(p,p),0)
flipped=np.array([[0,.5],[.5,0]])
near('invertible label reversal has full information',direct_mi(flipped),1)
near('invertible label reversal has zero literal accuracy',np.trace(flipped),0)
near('independent positive joint table zero information',direct_mi(np.outer(p,q)),0)

for prior,key in [(np.array([.5,.5]),'prior_half'),(np.array([.9,.1]),'prior_tenth')]:
    w=np.array([[.8,.2],[.2,.8]]);j=prior[:,None]*w
    near('detection MI '+key,direct_mi(j),d['detection'][key]['I_XY'])
    near('detection accuracy '+key,np.trace(j),.8)
triples={(x,y,z):.5*(.8 if x==y else .2)*(.9 if y==z else .1) for x,y,z in product(range(2),repeat=3)}
xz=np.array([[sum(triples[x,y,z] for y in range(2)) for z in range(2)] for x in range(2)])
near('enumerated cascade flip probability',xz[0,1]+xz[1,0],.26)
near('enumerated cascade information',direct_mi(xz),d['detection']['cascade']['I_XY'])
require('cascade obeys data processing',direct_mi(xz)<d['detection']['prior_half']['I_XY'])
xor={(x,z):x^z for x,z in product(range(2),repeat=2)}
xy=np.zeros((2,2))
for (x,z),y in xor.items():xy[x,y]+=.25
near('XOR unconditional MI',direct_mi(xy),0)
near('XOR conditional MI',sum(.5*direct_mi(np.array([[.5 if (x^z)==y else 0 for y in range(2)] for x in range(2)])) for z in range(2)),1)

# Exhaustive 2^12 state sequences, independent of the closed-form joint entropy.
probs=[]
for seq in product(range(2),repeat=12):
    prob=.5
    for a,b in zip(seq,seq[1:]):prob*=.9 if a==b else .1
    probs.append(prob)
near('Markov sequence normalization',sum(probs),1)
near('Markov entropy by exhaustive paths',entropy(probs),1+11*d['markov']['entropy_rate'])
near('20-step chain entropy',1+19*entropy([.1,.9]),d['markov']['H20'])
words=d['prefix']['codewords'];lengths=list(map(len,words))
require('code is prefix-free',all(not b.startswith(a) for a,b in product(words,repeat=2) if a!=b))
near('prefix Kraft equality',sum(2**(-v) for v in lengths),1)
near('expected prefix length',sum(a*b for a,b in zip(p,lengths)),1.6)
# Exhaustive feasible code lengths 1..7, rather than repeating the Huffman merge algorithm.
minimum=min(sum(a*b for a,b in zip(p,ls)) for ls in product(range(1,8),repeat=4) if sum(2**(-v) for v in ls)<=1)
near('prefix optimality by integer enumeration',minimum,1.6)
require('prefix entropy bounds',entropy(p)<=minimum<entropy(p)+1)

def bsc_mi(px,epsilon):return direct_mi(np.array([1-px,px])[:,None]*np.array([[1-epsilon,epsilon],[epsilon,1-epsilon]]))
opt=optimize.minimize_scalar(lambda v:-bsc_mi(v,.1),bounds=(.00001,.99999),method='bounded')
near('BSC capacity through independent input optimization',-opt.fun,d['capacity']['BSC_eps01'])
near('BSC half flips zero capacity',bsc_mi(.5,.5),0)
near('BSC full flips capacity one',bsc_mi(.5,1),1)
near('power ratio from ten dB',10**(10/10),10)
near('continuous Gaussian capacity',3000*math.log(11)/math.log(2),d['capacity']['AWGN_bit_per_s'])
# Gaussian differential entropy and a backward Gaussian test channel.
normal=lambda x:math.exp(-x*x/2)/math.sqrt(2*math.pi)
normal_h=integrate.quad(lambda x:-normal(x)*math.log2(normal(x)),-12,12,epsabs=1e-10)[0]
near('Gaussian entropy by numerical quadrature',normal_h,.5*math.log2(2*math.pi*math.e))
near('Gaussian rate distortion from entropy difference',normal_h-.5*math.log2(2*math.pi*math.e*.25),d['rate_distortion']['Gaussian_bit_per_sample'])
near('negative uniform differential entropy',-integrate.quad(lambda x:4*math.log2(4),0,.25)[0],-2)
near('differential entropy scale shift',math.log2(1000*.25)-math.log2(.25),math.log2(1000))

fs=d['audio']['fs_Hz'];t=np.arange(fs)/fs
source=np.sin(2*np.pi*220*t)+.35*np.sin(2*np.pi*440*t)+.2*np.sin(2*np.pi*880*t)
source=.65*source/np.max(np.abs(source));edge=np.sin(np.linspace(0,np.pi/2,160))**2
source[:160]*=edge;source[-160:]*=edge[::-1]
near('original sample power',np.mean(source**2),d['audio']['source_mean_square'])
for bits,name in [(16,'source'),(2,'quantized-2bit'),(4,'quantized-4bit')]:
    if name=='source':values=source
    else:
        # Nearest-level search independent of the generator's round-and-clip implementation.
        m=2**(bits-1);levels=np.arange(-m,m)/m
        values=levels[np.argmin(np.abs(source[:,None]-levels[None,:]),axis=1)]
        near(f'{bits}-bit sample distortion',np.mean((source-values)**2),d['audio']['quantizer_mse'][str(bits)])
        require(f'{bits}-bit sample error bounded without overload',np.max(np.abs(source-values))<=1/(2*m)+1e-12)
    expected=np.rint(.85*values*32767).astype('<i2')
    with wave.open(str(ROOT/'public/audio/information-theory'/f'{name}.wav'),'rb') as w:
        require(name+' WAV header',(w.getnchannels(),w.getsampwidth(),w.getframerate(),w.getnframes())==(1,2,fs,fs))
        actual=np.frombuffer(w.readframes(fs),dtype='<i2')
    require(name+' common-gain PCM exact bytes',np.array_equal(expected,actual))
    require(name+' PCM no clipping',max(abs(actual.astype(np.int32)))<32767)
near('2-bit nominal raw rate',fs*2,32000)
near('4-bit nominal raw rate',fs*4,64000)
near('fixed full-support independence bias leading coefficient',9/(2*math.log(2)),6.4921276840003355)
exact_null_means=[]
for n,empirical,tolerance in zip([40,200,1000],d['null_estimation']['means'],[.015,.004,.001]):
    k=np.arange(1,n+1);terms=-(k/n)*np.log2(k/n)
    # Each cell count has a binomial marginal; linearity of expectation is exact.
    expected_h=lambda categories:float(categories*np.dot(terms,binom.pmf(k,n,1/categories)))
    exact=2*expected_h(4)-expected_h(16);exact_null_means.append(exact)
    require(f'N={n} simulated null mean consistent with exact expectation',abs(empirical-exact)<tolerance)
require('null simulation means decrease with sample size',d['null_estimation']['means'][0]>d['null_estimation']['means'][1]>d['null_estimation']['means'][2]>0)
require('large-N null bias near asymptotic first term',abs(d['null_estimation']['means'][2]-d['null_estimation']['asymptotic_bias'][2])<.0006)
for path in sorted((ROOT/'public/figures/information-theory').glob('*.svg')):
    require('valid SVG '+path.name,ET.parse(path).getroot().tag.endswith('svg'))
result={'status':'passed','count':len(checks),'exact_null_MI_expectations':exact_null_means,'checks':checks}
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
