"""Checks of synthetic acoustic examples, units and media; not a linguistic peer review."""
from pathlib import Path
import json
import math
import wave
import xml.etree.ElementTree as ET
import numpy as np
from scipy import signal

ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'docs/research/chinese-phonetics-2026-11-02'
d=json.loads((REC/'calculations.json').read_text(encoding='utf-8'));checks=[]
def near(name,actual,expected,atol=1e-9):
    np.testing.assert_allclose(actual,expected,atol=atol,rtol=0);checks.append(name)
def require(name,value):
    assert value,name;checks.append(name)
fs=d['fs_Hz']
initials=[v for group in d['initial_groups'] for v in group['pinyin']]
require('21 unique conventional onset spellings',len(initials)==len(set(initials))==21)
require('y w ng are outside the conventional onset table',not set(['y','w','ng'])&set(initials))
near('130 Hz period in milliseconds',1000/130,7.6923076923076925)
near('one octave error in semitones',12*math.log2(260/130),d['octave_error_semitones'])
near('frequency ratio three halves in semitones',12*math.log2(195/130),7.019550008653875)
near('one sample duration in milliseconds',1000/fs,.0625)
for key,expected in [('12',(800,992)),('65',(800,1840))]:
    record=d['VOT'][key]
    require('VOT '+key+' original markers',(record['release_sample'],record['periodic_onset_sample'])==expected)
    near('VOT '+key+' marker time difference',(expected[1]-expected[0])*1000/fs,float(key))
near('negative VOT has voicing before release',(560-800)*1000/fs,-15)
for record in d['spectrograms']:
    ms=record['duration_ms'];n=record['samples']
    near(str(ms)+' ms window sample count',fs*ms/1000,n)
    near(str(ms)+' ms periodic Hann analytic ENBW',1.5*fs/n,record['ENBW_Hz'])
    # Periodic Hann discrete sums are N/2 and 3N/8, independent of the recorded ENBW formula.
    w=.5-.5*np.cos(2*np.pi*np.arange(n)/n)
    near(str(ms)+' ms Hann sum',sum(w),n/2)
    near(str(ms)+' ms Hann square sum',sum(w*w),3*n/8)
    near(str(ms)+' ms FFT grid',fs/2048,record['FFT_grid_Hz'])
require('same FFT grid with different analysis bandwidth',d['spectrograms'][0]['FFT_grid_Hz']==d['spectrograms'][1]['FFT_grid_Hz'] and d['spectrograms'][0]['ENBW_Hz']>d['spectrograms'][1]['ENBW_Hz'])

t=np.arange(d['vowel_samples'])/fs
source=np.array([math.fsum(math.sin(2*math.pi*k*130*tt)/k for k in range(1,31)) for tt in t])
spectrum=2*np.abs(np.fft.rfft(source))/len(source);grid=np.fft.rfftfreq(len(source),1/fs)
for k in [1,2,3,8,30]:
    ix=int(round(k*130*len(source)/fs));near('source harmonic amplitude '+str(k),spectrum[ix],1/k,1e-11)
require('highest synthetic harmonic below Nyquist',30*130<fs/2)
edge=np.sin(np.linspace(0,np.pi/2,320))**2;envelope=np.ones(len(t));envelope[:320]=edge;envelope[-320:]=edge[::-1]
def direct_response(a,b,freq):
    z=np.exp(-2j*np.pi*np.asarray(freq)/fs)
    return b/sum(c*z**i for i,c in enumerate(a))
def recurrence(a,b,x):
    out=np.zeros(len(x))
    for n in range(len(x)):
        out[n]=(b*x[n]-math.fsum(a[k]*out[n-k] for k in range(1,min(n+1,len(a)))))/a[0]
    return out
wave_arrays={}
for name,setting in d['resonators'].items():
    a=np.array(setting['denominator']);b=setting['numerator_gain'];roots=np.roots(a)
    require(name+' all poles inside unit circle',np.all(np.abs(roots)<1))
    expected=[]
    for f,bw in zip(setting['frequency_parameters_Hz'],setting['bandwidth_parameters_Hz']):
        radius=math.exp(-math.pi*bw/fs);expected.extend([radius*np.exp(2j*np.pi*f/fs),radius*np.exp(-2j*np.pi*f/fs)])
    near(name+' pole locations from polynomial roots',sorted(roots,key=np.angle),sorted(expected,key=np.angle),2e-9)
    frequencies=np.array([130,350,800,2200,3000,3900])
    _,reference=signal.freqz([b],a,worN=frequencies,fs=fs)
    near(name+' polynomial versus library frequency response',direct_response(a,b,frequencies),reference,5e-10)
    manual=recurrence(a,b,source);library=signal.lfilter([b],a,source)
    near(name+' hand recurrence versus lfilter',manual,library,2e-9)
    waveform=manual*envelope*d['vowel_pair_common_gain'];wave_arrays['resonance-'+name]=waveform
    near(name+' peak after common playback gain',np.max(np.abs(waveform)),d['audio']['resonance-'+name]['peak'],2e-9)
    require(name+' endpoint ramp reaches zero',waveform[0]==0 and waveform[-1]==0)
require('vowel pair level is comparable without per-file normalization',.8<d['audio']['resonance-front']['peak']/d['audio']['resonance-back']['peak']<1.2)

N=d['tone_samples_each'];parts=[];control_knots=[[(0,200),(N-1,200)],[(0,140),(N-1,190)],[(0,135),(.55*(N-1),105),(N-1,165)],[(0,205),(N-1,110)]]
for i,knots in enumerate(control_knots):
    f=[]
    for n in range(N):
        left,right=next((a,b) for a,b in zip(knots,knots[1:]) if a[0]<=n<=b[0])
        f.append(left[1]+(right[1]-left[1])*(n-left[0])/(right[0]-left[0]))
    near('tone '+str(i+1)+' F0 endpoints',[f[0],min(f),f[-1]],d['tone_contour_endpoints_Hz'][i])
    phase=0;values=[]
    for frequency in f:
        phase+=2*math.pi*frequency/fs
        values.append(math.fsum(math.sin(k*phase)/k for k in range(1,9)))
    values=np.array(values);env=np.ones(N);env[:320]=edge;env[-320:]=edge[::-1];values*=env*d['tone_common_gain'];parts.append(values)
    require('tone '+str(i+1)+' harmonics below Nyquist',8*max(f)<fs/2)
pause=np.zeros(d['tone_pause_samples']);sequence=np.concatenate([v for i,part in enumerate(parts) for v in ((part,pause) if i<3 else (part,))]);wave_arrays['tone-contours']=sequence
near('tone sequence duration',len(sequence)/fs,2.4)
near('tone sequence sample count',len(sequence),d['tone_sequence_samples'])
for i in range(3):
    start=(i+1)*N+i*len(pause);require('inter-tone pause '+str(i+1)+' is silent',np.all(sequence[start:start+len(pause)]==0))
for name,expected in wave_arrays.items():
    path=ROOT/'public/audio/chinese-phonetics'/f'{name}.wav'
    with wave.open(str(path),'rb') as wav:
        require(name+' WAV format',(wav.getnchannels(),wav.getsampwidth(),wav.getframerate(),wav.getnframes())==(1,2,fs,len(expected)))
        actual=np.frombuffer(wav.readframes(len(expected)),dtype='<i2').astype(np.int32)
    pcm=np.rint(expected*32767).astype(np.int32)
    require(name+' independent synthesis within one PCM unit',np.max(abs(actual-pcm))<=1)
    require(name+' no clipping',np.max(abs(actual))<32767)
    near(name+' correct sample count',len(actual),d['audio'][name]['samples'])
for path in sorted((ROOT/'public/figures/chinese-phonetics').glob('*.svg')):
    require('well-formed figure '+path.name,ET.parse(path).getroot().tag.endswith('svg'))
require('well-formed course thumbnail',ET.parse(ROOT/'public/figures/foundation-courses/chinese-phonetics.svg').getroot().tag.endswith('svg'))
result={'status':'passed','count':len(checks),'scope':'synthetic acoustic examples, units and media; linguistic claims reviewed separately against sources','checks':checks}
(REC/'numerical-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,ensure_ascii=False,indent=2))
