"""ISO 226:2023 calculations and an attributed real-speech analysis.
Source and processing records are saved alongside the figures. No clinical data.
"""
from pathlib import Path
import json,hashlib,csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from scipy.signal import spectrogram,find_peaks
from scipy.interpolate import PchipInterpolator
import soundfile as sf
import parselmouth

P=Path(__file__).resolve().parent;F=P.parent/'figures'
plt.rcParams.update({'font.family':FontProperties(fname='C:/Windows/Fonts/msyh.ttc').get_name(),
 'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.unicode_minus':False,
 'svg.fonttype':'none','svg.hashsalt':'hearingpedia-equal-loudness-speech-20261006',
 'axes.titlepad':11,'axes.labelpad':8,'legend.frameon':False})
def save(fig,name):
 fig.savefig(F/(name+'.svg'),bbox_inches='tight',metadata={'Date':None})
 fig.savefig(F/(name+'.png'),dpi=160,bbox_inches='tight');plt.close(fig)

# Parameters transcribed from the publicly accessible ISO 226:2023 preview,
# Table 1 (printed page 4). Formula (1), printed page 2: final exponent is alpha_f.
freq=np.array([20,25,31.5,40,50,63,80,100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150,4000,5000,6300,8000,10000,12500])
alpha=np.array([.635,.602,.569,.537,.509,.482,.456,.433,.412,.391,.373,.357,.343,.330,.320,.311,.303,.300,.295,.292,.290,.290,.289,.289,.289,.293,.303,.323,.354])
lu=np.array([-31.5,-27.2,-23.1,-19.3,-16.1,-13.1,-10.4,-8.2,-6.3,-4.6,-3.2,-2.1,-1.2,-.5,0,.4,.5,0,-2.7,-4.2,-1.2,1.4,2.3,1,-2.3,-7.2,-11.2,-10.9,-3.5])
threshold=np.array([78.1,68.7,59.5,51.1,44,37.5,31.5,26.5,22.1,17.9,14.4,11.4,8.6,6.2,4.4,3,2.2,2.4,3.5,1.7,-1.3,-4.2,-6,-5.4,-1.5,6,12.6,13.9,12.3])
def equal_loudness(phon):
 return 10/alpha*np.log10((4e-10)**(.3-alpha)*(10**(.03*phon)-10**.072)+10**(alpha*(threshold+lu)/10))-lu
levels=[20,40,60,80];curves={n:equal_loudness(n) for n in levels}
assert all(abs(curves[n][17]-n)<1e-10 for n in levels)
assert np.all(np.diff(np.array(list(curves.values())),axis=0)>0)
assert np.allclose(equal_loudness(2.4),threshold)
with (P/'iso226-2023-calculated.csv').open('w',newline='',encoding='utf-8') as out:
 w=csv.writer(out);w.writerow(['frequency_Hz','alpha_f','L_U_dB','T_f_dB']+[f'{n}_phon_dBSPL' for n in levels])
 w.writerows(zip(freq,alpha,lu,threshold,*curves.values()))
fig,ax=plt.subplots(figsize=(10.5,6.5))
colors=['#3478a5','#248a72','#af7720','#ac4660'];dense=np.geomspace(20,12500,800)
for n,c in zip(levels,colors):
 y=curves[n];smooth=PchipInterpolator(np.log10(freq),y)(np.log10(dense))
 ax.plot(dense,smooth,color=c,lw=2,label=f'{n} 方');ax.plot(freq,y,'.',color=c,ms=3)
 ax.text(13800,y[-1],f'{n} 方',color=c,va='center')
ax.axvline(1000,color='#888',ls=':',lw=1)
ax.scatter([100,1000],[curves[40][7],40],facecolors='white',edgecolors=colors[1],s=65,zorder=5)
ax.annotate(f'100 赫兹\n约 {curves[40][7]:.0f} 分贝',xy=(100,curves[40][7]),xytext=(140,62),arrowprops={'arrowstyle':'-','color':colors[1]},fontsize=10,color=colors[1])
ax.annotate('1000 赫兹：40 分贝',xy=(1000,40),xytext=(380,29),arrowprops={'arrowstyle':'-','color':colors[1]},fontsize=10,color=colors[1])
ax.set_xscale('log');ax.set_xlim(20,21000);ax.set_ylim(0,125)
ax.set_xticks([20,50,100,200,500,1000,2000,5000,10000],['20','50','100','200','500','1000','2000','5000','10000'])
ax.set_yticks(np.arange(0,121,20));ax.grid(which='major',alpha=.18)
ax.set_xlabel('纯音频率（赫兹；对数轴）');ax.set_ylabel('声压级（dB SPL）')
ax.set_title('等响曲线：同一条曲线上的纯音具有相同响度级',loc='left',fontweight='bold')
fig.text(.5,.02,'依据 ISO 226:2023 公式 (1) 与表 1 计算 · 点为规定频率值，连线作视觉插值\n自由场、正前方来声、双耳聆听；18—25 岁耳科正常人群的平均关系',ha='center',fontsize=9,color='#555')
fig.tight_layout(rect=(0,.085,1,1));save(fig,'loudness-equal-contours')

# Real speech, CC BY 4.0. Source metadata differ on chapter number; cite recording
# identifier and work/reader without asserting an unverified chapter number.
full,fs=sf.read(P/'libri1.ogg');assert full.ndim==1
start,end=3.3,4.8;start_i,end_i=round(start*fs),round(end*fs)
y=full[start_i:end_i];y=y/np.max(np.abs(y))*.98
assert np.max(abs(y))<=1
sf.write(P/'speech-excerpt.wav',y,fs,subtype='PCM_16')
pitch=parselmouth.Sound(full,fs).to_pitch_ac(time_step=.005,pitch_floor=60,pitch_ceiling=350,voicing_threshold=.6,silence_threshold=.03)
pt=pitch.xs();pf=pitch.selected_array['frequency'];selected=(pt>=start)&(pt<=end)
tp=pt[selected]-start;fp=pf[selected];fp=np.where(fp>0,fp,np.nan)
center=.43;duration=.08;idx=(tp>=center-duration/2)&(tp<=center+duration/2)
f0=float(np.nanmedian(fp[idx]));assert 60<f0<140
nwin=round(.08*fs);hop=round(.005*fs)
ff,tt,S=spectrogram(y,fs,window='hann',nperseg=nwin,noverlap=nwin-hop,nfft=8192,mode='psd',detrend=False)
Sdb=10*np.log10(np.maximum(S/S.max(),1e-12))
a,b=round((center-duration/2)*fs),round((center+duration/2)*fs)
frame=y[a:b];spec=np.abs(np.fft.rfft(frame*np.hanning(len(frame)),32768))**2
sfreq=np.fft.rfftfreq(32768,1/fs);sdb=10*np.log10(np.maximum(spec/spec.max(),1e-12))
peaks,_=find_peaks(sdb,distance=round(.6*f0/(fs/32768)))
observed=[]
for n in range(1,11):
 cand=peaks[(sfreq[peaks]>n*f0-.3*f0)&(sfreq[peaks]<n*f0+.3*f0)]
 if len(cand):observed.append(float(sfreq[cand[np.argmax(sdb[cand])]]))

fig=plt.figure(figsize=(11,11.5));grid=fig.add_gridspec(4,2,width_ratios=[1,.024],height_ratios=[1,2.5,1,1.6],hspace=.57,wspace=.055)
axs=[fig.add_subplot(grid[i,0]) for i in range(4)];cax=fig.add_subplot(grid[1,1])
time=np.arange(len(y))/fs;axs[0].plot(time,y,color='#276b8c',lw=.6);axs[0].set_ylim(-1.05,1.05);axs[0].set_ylabel('相对幅度');axs[0].set_title('A  真实语音片段：波形',loc='left',fontweight='bold')
im=axs[1].pcolormesh(tt,ff,Sdb,cmap='Greys',vmin=-55,vmax=0,shading='auto',rasterized=True)
axs[1].set_ylim(0,1600);axs[1].set_ylabel('频率（赫兹）');axs[1].set_title('B  窄带语谱图：浊音段中的近似等间距谐波条纹',loc='left',fontweight='bold')
fig.colorbar(im,cax=cax,label='相对谱功率（分贝）')
axs[2].plot(tp,fp,color='#be542f',lw=1.7);axs[2].set_ylim(50,150);axs[2].set_ylabel('基频（赫兹）');axs[2].set_xlabel('相对片段起点的时间（秒）');axs[2].set_title('C  自相关法估计的基频轨迹；未检出有声时留空',loc='left',fontweight='bold')
for ax in axs[:3]:
 ax.set_xlim(0,end-start);ax.set_xticks(np.arange(0,1.51,.25))
 ax.axvspan(center-duration/2,center+duration/2,color='#c19b34',alpha=.17)
axs[3].plot(sfreq,sdb,color='#276b8c',lw=1.2)
for n in range(1,13):
 axs[3].axvline(n*f0,color='#bd694a',lw=.65,alpha=.65,ls='--')
 if n in [1,2,3,4,6,8,10]:axs[3].text(n*f0,2,str(n),ha='center',fontsize=9,color='#914326')
axs[3].set_xlim(0,1200);axs[3].set_ylim(-50,6);axs[3].set_xlabel('频率（赫兹）');axs[3].set_ylabel('相对谱功率（分贝）')
axs[3].set_title(f'D  阴影内 80 毫秒片段的频谱；虚线为估计基频 {f0:.0f} 赫兹的整数倍',loc='left',fontweight='bold')
fig.text(.5,.015,'录音：LibriSpeech 5703-47212-0000／librosa libri1，Garth Comira 朗读，CC BY 4.0\n截取源文件 3.3—4.8 秒，峰值归一化；语谱与基频由本项目计算，轨迹不是人工标注真值',ha='center',fontsize=9,color='#555')
fig.subplots_adjust(left=.09,right=.9,bottom=.10,top=.96)
save(fig,'fundamental-frequency-speech-spectrogram')
np.savetxt(P/'speech-f0-estimate.csv',np.c_[tp,fp],delimiter=',',header='time_s,estimated_f0_Hz',comments='')
record={'date':'2026-10-06','equal_loudness':{'source':'https://www.iso.org/standard/83117.html','public_preview':'https://cdn.standards.iteh.ai/samples/83117/6afa5bd94e0e4f32812c28c3b0a7b8ac/ISO-226-2023.pdf','scope':'Formula (1), Table 1, published pages 2–4; visually checked. Preview, not full standard.','phon':levels,'at100Hz40phon_dBSPL':float(curves[40][7]),'one_kHz_error_max':max(abs(curves[n][17]-n) for n in levels),'lines':'PCHIP on log10 frequency, visual interpolation only'},'speech':{'source_url':'https://raw.githubusercontent.com/librosa/data/main/audio/5703-47212-0000.ogg','source_sha256':hashlib.sha256((P/'libri1.ogg').read_bytes()).hexdigest(),'recording_id':'5703-47212-0000','work':'The Ashiel Mystery','reader':'Garth Comira','license':'CC BY 4.0','license_url':'https://creativecommons.org/licenses/by/4.0/','source_sample_rate':fs,'excerpt_seconds':[start,end],'peak':float(max(abs(y))),'spectrogram':{'window':'Hann','window_ms':80,'hop_samples':hop,'hop_ms':hop/fs*1000,'nfft':8192,'preemphasis':False,'dynamic_range_dB':55},'pitch':{'algorithm':'Praat raw autocorrelation via Parselmouth Sound.to_pitch_ac','parselmouth':parselmouth.__version__,'praat':parselmouth.PRAAT_VERSION,'step_ms':5,'floor_Hz':60,'ceiling_Hz':350,'voicing_threshold':.6,'silence_threshold':.03,'selected_frame_start_s':center-duration/2,'selected_frame_end_s':center+duration/2,'selected_median_f0_Hz':f0,'observed_spectral_peaks_Hz':observed,'mean_first_four_peak_spacing_Hz':float(np.mean(np.diff(observed[:4])))}}}
for name in ['loudness-equal-contours','fundamental-frequency-speech-spectrogram']:
 record.setdefault('outputs',[]).append({'svg':name+'.svg','sha256':hashlib.sha256((F/(name+'.svg')).read_bytes()).hexdigest()})
(P/'supplementary-figure-provenance.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'equal40at100Hz':float(curves[40][7]),'f0':f0,'harmonic_peaks':observed,'first_four_spacing':float(np.mean(np.diff(observed[:4]))),'peak':float(max(abs(y)))},ensure_ascii=False))
