"""Original teaching figures, synthetic signals only. Run from the repository root."""
from pathlib import Path
import json, wave
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/figures/spectrogram'
OUT.mkdir(parents=True, exist_ok=True)
font_manager.fontManager.addfont('C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family': 'Microsoft YaHei', 'font.size': 12,
                     'axes.unicode_minus': False, 'svg.fonttype': 'path',
                     'figure.facecolor': 'white', 'axes.facecolor': 'white'})
FS = 16000
rng = np.random.default_rng(20261009)
manifest = []

def psd(x, length_ms, hop_ms=1, nfft=2048):
    n = round(FS * length_ms / 1000)
    hop = round(FS * hop_ms / 1000)
    w = np.hanning(n)
    starts = np.arange(0, len(x)-n+1, hop)
    frames = np.array([x[i:i+n]*w for i in starts])
    z = np.fft.rfft(frames, nfft, axis=1)
    p = abs(z)**2 / (FS * np.sum(w*w))
    p[:, 1:-1] *= 2  # All calls use an even NFFT, retaining DC/Nyquist.
    return np.fft.rfftfreq(nfft, 1/FS), (starts+(n-1)/2)/FS, p.T

def draw(ax, x, ms, upper=4500, dynamic=65, ref=None):
    f,t,p = psd(x, ms)
    ref = p.max() if ref is None else ref
    db = 10*np.log10(np.maximum(p/ref, 1e-12))
    im = ax.pcolormesh(t, f, db, cmap='magma', vmin=-dynamic, vmax=0, shading='auto', rasterized=True)
    ax.set_ylim(0, upper); ax.set_ylabel('频率 / Hz'); ax.set_xlabel('时间 / s')
    ax.set_xlim(0,len(x)/FS)
    return im,ref

def save(fig, name, parameters, caption):
    fig.savefig(OUT/(name+'.svg'), bbox_inches='tight')
    fig.savefig(OUT/(name+'.png'), dpi=170, bbox_inches='tight')
    plt.close(fig)
    manifest.append({'name':name,'files':[name+'.svg',name+'.png'],
        'data_type':'synthetic teaching signal; not a human recording',
        'sample_rate_hz':FS,'parameters':parameters,'caption':caption,
        'creator':'n³ Hearingpedia, AI-assisted original calculation',
        'license':'CC BY 4.0','seed':20261009})

# A stationary harmonic source shaped by a prescribed smooth spectral envelope,
# followed by high-frequency noise. This is not a physiological vocal-tract model.
t = np.arange(round(1.2*FS))/FS
x = np.zeros_like(t); f0=140
for k in range(1, 51):
    f=k*f0
    amp=(0.035 + 1.3*np.exp(-.5*((f-700)/100)**2)
         +np.exp(-.5*((f-1800)/150)**2)+.65*np.exp(-.5*((f-2800)/180)**2))/np.sqrt(k)
    x += amp*np.sin(2*np.pi*f*t)
env = np.zeros_like(t)
sel=(t>=.12)&(t<.72); env[sel]=np.sin(np.pi*(t[sel]-.12)/.60)**.25
x *= env
noise=rng.normal(size=len(t)); spec=np.fft.rfft(noise)
freq=np.fft.rfftfreq(len(t),1/FS); spec[(freq<3000)|(freq>6500)]=0
noise=np.fft.irfft(spec,len(t)); noise/=np.std(noise)
sel=(t>=.82)&(t<1.08); x[sel]+=.22*noise[sel]*np.sin(np.pi*(t[sel]-.82)/.26)**.5
x /= np.max(abs(x))/0.8
with wave.open(str(OUT/'synthetic-example.wav'),'wb') as wav:
    wav.setnchannels(1);wav.setsampwidth(2);wav.setframerate(FS)
    wav.writeframes((x*32767).astype('<i2').tobytes())
np.savez_compressed(OUT/'synthetic-data.npz',time=t,signal=x)
fig,ax=plt.subplots(3,1,figsize=(11.8,9.2),layout='constrained',gridspec_kw={'height_ratios':[1,2,2]})
ax[0].plot(t,x,lw=.6,color='#246c87');ax[0].set(xlim=(0,1.2),ylim=(-.9,.9),ylabel='数字幅度',title='同一合成信号：波形、短窗与长窗')
ax[0].text(.40,.66,'周期段：F0 = 140 Hz',ha='center');ax[0].text(.95,.66,'高频噪声段',ha='center')
im,_=draw(ax[1],x,5,7000);ax[1].set_title('5 ms Hann 窗：突出包络增强带与时间变化',loc='left')
im,_=draw(ax[2],x,30,7000);ax[2].set_title('30 ms Hann 窗：周期段可见间隔约 140 Hz 的谐波',loc='left')
fig.colorbar(im,ax=ax[1:],label='相对各图最大 PSD / dB',shrink=.85)
save(fig,'01-reading',{'f0_hz':140,'envelope_centers_hz':[700,1800,2800],
    'noise_band_hz':[3000,6500],'windows_ms':[5,30],'window':'numpy.hanning (symmetric)',
    'hop_ms':1,'nfft':2048,'display_range_db':65,'normalization':'each panel maximum; not an amplitude comparison'},
    'Figure 1: Same synthetic signal, two analysis windows. Envelope centers are prescribed, not fitted formants.')

t=np.arange(FS)/FS
y=.15*(np.sin(2*np.pi*1000*t)+np.sin(2*np.pi*1040*t))
for c in [.45,.48]: y+=.9*np.exp(-.5*((t-c)/.00015)**2)
fig,ax=plt.subplots(2,1,figsize=(11.8,7.2),layout='constrained')
for a,ms in zip(ax,[20,80]):
    im,_=draw(a,y,ms,2200);a.set_title(f'{ms} ms Hann 窗；两音相差 40 Hz；两短脉冲相隔 30 ms',loc='left')
    a.axvline(.45,color='white',lw=.8,ls=':');a.axvline(.48,color='white',lw=.8,ls=':')
fig.colorbar(im,ax=ax,label='相对各图最大 PSD / dB',shrink=.8)
save(fig,'02-window-tradeoff',{'tones_hz':[1000,1040],'pulse_centers_s':[.45,.48],
    'pulse_sigma_s':.00015,'windows_ms':[20,80],'hop_ms':1,'nfft':2048,'display_range_db':65},
    'Figure 2: Longer windows separate the two steady tones but spread the brief events in time.')

fig,ax=plt.subplots(1,3,figsize=(13,4.6),layout='constrained',sharey=True)
for a,ms,nfft in zip(ax,[20,20,80],[512,4096,4096]):
    n=round(FS*ms/1000); tt=(np.arange(n)-(n-1)/2)/FS
    segment=np.cos(2*np.pi*1000*tt)+np.cos(2*np.pi*1040*tt)
    z=abs(np.fft.rfft(segment*np.hanning(n),nfft));z=20*np.log10(np.maximum(z/z.max(),1e-6))
    f=np.fft.rfftfreq(nfft,1/FS)
    a.plot(f,z,'o-' if nfft==512 else '-',ms=3,color='#246c87',lw=1.5)
    a.set(xlim=(850,1190),ylim=(-50,3),xlabel='频率 / Hz',title=f'{ms} ms；NFFT = {nfft}\n频率采样间隔 {FS/nfft:g} Hz')
    for freq in [1000,1040]: a.axvline(freq,lw=.8,ls=':',color='#ae4d16')
    a.grid(alpha=.18)
ax[0].set_ylabel('相对各谱最大幅度 / dB')
save(fig,'03-zero-padding',{'tones_hz':[1000,1040],'windows_ms':[20,20,80],
    'nfft':[512,4096,4096],'phase':'cosines centered on frame','display_range_db':50},
    'Figure 3: Zero padding makes the same short-window spectrum denser; lengthening the data window resolves the tones.')

t=np.arange(FS)/FS
y=.5*np.sin(2*np.pi*1000*t)+.0015*np.sin(2*np.pi*2500*t)+rng.normal(0,1e-4,len(t))
_,_,p=psd(y,30);ref=p.max()
fig,ax=plt.subplots(2,1,figsize=(11.8,6.8),layout='constrained')
for a,dynamic in zip(ax,[40,80]):
    im,_=draw(a,y,30,4000,dynamic,ref)
    a.set_title(f'显示范围 {dynamic} dB；相同数据、窗长及参考值',loc='left')
    fig.colorbar(im,ax=a,label='相对共同最大 PSD / dB')
save(fig,'04-display-range',{'tones_hz':[1000,2500],'amplitudes':[.5,.0015],
    'noise_rms':1e-4,'window_ms':30,'hop_ms':1,'nfft':2048,
    'display_range_db':[40,80],'normalization':'shared maximum PSD',
    'weak_to_strong_amplitude_db':float(20*np.log10(.0015/.5))},
    'Figure 4: A weak component can disappear because of display clipping, with no change to the signal.')

from matplotlib.patches import FancyBboxPatch
fig,ax=plt.subplots(figsize=(12,6.6));ax.set(xlim=(0,12),ylim=(0,6));ax.axis('off')
rows=[(4.55,'早期可视化路线',['声音输入','记录与\n重复读取','依次或并行\n频带分析','强度与\n位置同步','纸面或\n荧光屏记录']),
      (2.85,'现代 STFT 路线',['数字音频','分帧\n加窗','短时\n傅里叶变换','谱量与\n分贝标度','颜色\n时频图']),
      (1.15,'图案回放路线',['预设或修改\n谱图案','光源与音轮\n扫描图案','光电接收\n组合成分','电信号\n驱动扬声器','合成声音\n供听者评价'])]
for y,label,texts in rows:
    ax.text(.15,y+.71,label,fontsize=14,weight='bold',color='#153f54')
    for i,label in enumerate(texts):
        left=.18+i*2.36
        box=FancyBboxPatch((left,y-.37),2.0,.85,boxstyle='round,pad=0.08',fc='#edf5f7',ec='#47758a',lw=1.3)
        ax.add_patch(box);ax.text(left+1,y+.055,label,ha='center',va='center',fontsize=13)
        if i<4:ax.annotate('',xy=(left+2.29,y+.04),xytext=(left+2.08,y+.04),arrowprops={'arrowstyle':'->','color':'#47758a','lw':1.5})
ax.text(.15,.14,'功能比较示意：不复刻任何特定型号电路；各路线的存储、滤波及显示实现可以不同。',fontsize=12,color='#50626b')
save(fig,'05-historical-routes',{'type':'original functional diagram','sources':['US2403986A','US3021478A','Philip Rubin Pattern Playback operating principles'],
    'scope':'conceptual functional routes, not a historical circuit reproduction'},
    'Figure 5: Comparison of early spectrographic analysis, modern STFT and optical pattern playback.')
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':len(manifest),'output':str(OUT)},ensure_ascii=False))
