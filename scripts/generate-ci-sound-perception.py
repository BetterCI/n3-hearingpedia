"""Reproducible original diagrams and licensed channel-vocoder demonstration.

Requires numpy, scipy, matplotlib and soundfile. Run from any directory.
The only participant data are published means/SDs from Kopsch et al. (2025).
Other diagrams are conceptual; audio is a teaching implementation, not a CI model.
"""
from pathlib import Path
import json, hashlib
import numpy as np
from scipy.signal import butter, sosfiltfilt, resample_poly
import soundfile as sf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/cochlear-implant-sound-perception'
OUT.mkdir(parents=True,exist_ok=True)
AUDIO=ROOT/'public/audio/cochlear-implant-sound-perception'
AUDIO.mkdir(parents=True,exist_ok=True)
FONT=Path('C:/Windows/Fonts/msyh.ttc')
if FONT.exists():
    font_manager.fontManager.addfont(str(FONT))
    family=font_manager.FontProperties(fname=str(FONT)).get_name()
else: family='Noto Sans CJK SC'
plt.rcParams.update({'font.family':family,'font.size':26,'svg.fonttype':'path',
 'svg.hashsalt':'hearingpedia-ci-perception-20261009','axes.unicode_minus':False,
 'axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})
BLUE,ORANGE,GREY='#1865a2','#b85a16','#576779'
sizes={}
def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None,'Creator':'Hearingpedia original figure'})
    svg=OUT/(name+'.svg')
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
    fig.savefig(OUT/(name+'.png'),dpi=100)
    sizes[name]={'svg_viewbox':[round(v*72) for v in fig.get_size_inches()],
                 'png_pixels':[round(v*100) for v in fig.get_size_inches()]}
    plt.close(fig)
def canvas():
    fig,ax=plt.subplots(figsize=(20,10));fig.subplots_adjust(left=.02,right=.98,bottom=.03,top=.98)
    ax.set(xlim=(0,20),ylim=(0,10));ax.axis('off');return fig,ax
def box(ax,x,y,w,h,title,body,color=BLUE):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',facecolor='#f3f7fb' if color==BLUE else '#fff6ec',edgecolor=color,lw=2))
    ax.text(x+w/2,y+h-.6,title,ha='center',va='center',weight='bold',fontsize=32)
    ax.text(x+w/2,y+(h-.8)/2,body,ha='center',va='center',fontsize=28,linespacing=1.6)

fig,ax=canvas()
box(ax,.5,5.4,5.7,3.6,'输入与神经接口','分频与压缩\n电极位置、时序\n神经状态与交互')
box(ax,7.15,5.4,5.7,3.6,'基本感知维度','音高、音色、响度\n粗糙感与空间感\n可用线索与辨别')
box(ax,13.8,5.4,5.7,3.6,'情境中的体验','理解与声源识别\n自然度、愉悦度\n努力、熟悉与参与')
for x in [6.3,12.95]:ax.annotate('',(x+.7,7.2),(x,7.2),arrowprops={'arrowstyle':'<->','lw':2,'color':GREY})
box(ax,3,1.45,14,2.5,'经验、任务与聆听配置','语前／语后聋 · 单侧／双侧／双模式 · 声音材料',ORANGE)
ax.text(10,.45,'概念分层；箭头不表示已经定位的单向因果通路',ha='center',color=GREY,fontsize=25)
save(fig,'01-perceptual-levels')

fig,ax=canvas()
ax.text(10,9.35,'识别得分与自然度分别测量',ha='center',weight='bold',fontsize=34)
box(ax,2,5.55,7.3,2.45,'识别较好、较自然','两个目标在该条件下均达到',BLUE)
box(ax,10.7,5.55,7.3,2.45,'识别较差、较自然','声音熟悉，但词句仍可能被遮蔽',ORANGE)
box(ax,2,2.4,7.3,2.45,'识别较好、较不自然','理解信息与熟悉音色可以分离',ORANGE)
box(ax,10.7,2.4,7.3,2.45,'识别较差、较不自然','两个目标均需进一步评价',BLUE)
ax.text(10,.8,'逻辑上的四种组合；没有样本频数、相关系数或临床分界值',ha='center',color=GREY,fontsize=25)
save(fig,'02-separate-outcomes')

fig,ax=canvas()
box(ax,.65,6.8,5,2.2,'同一段语音','内容与说话人固定')
box(ax,7.15,6.8,5.6,2.2,'原始语音 → CI','处理器输入／电听觉')
box(ax,7.15,3.1,5.6,2.7,'调整后的语音 → 对侧耳','滤波、音高、频谱等\n声学输入／残余听力')
box(ax,14.2,4.9,5.1,3.2,'听者比较','哪一版更相似？\n调整参数与重测',ORANGE)
for start,end in [((5.8,7.9),(7,7.9)),((3.2,6.65),(7,4.5)),((12.9,7.9),(14,6.9)),((12.9,4.5),(14,5.6))]:
    ax.annotate('',end,start,arrowprops={'arrowstyle':'->','lw':2.5,'color':GREY})
ax.text(10,1.65,'输出：匹配参数、相似性评分、重复性与新材料泛化',ha='center',fontsize=28)
ax.text(10,.65,'需控制两耳声级、延迟与可听带宽；高分仍来自主观判断',ha='center',fontsize=25,color=GREY)
save(fig,'03-interaural-matching')

# Published descriptive statistics, not a simulated cohort. SD, not SEM or CI.
means=np.array([9.7,8.4,8.9]); sds=np.array([.5,1.5,1.3]); n=15
fig,ax=plt.subplots(figsize=(20,10));fig.subplots_adjust(left=.1,right=.96,top=.88,bottom=.23)
bars=ax.bar([0,1,2],means,color=[BLUE,ORANGE,ORANGE],width=.55,edgecolor='white')
# Descriptive SD intervals may exceed the bounded scale; do not truncate them.
ax.errorbar([0,1,2],means,yerr=sds,fmt='none',color=GREY,lw=2.5,capsize=10)
for i,(m,s) in enumerate(zip(means,sds)):ax.text(i,m-s-.6,f'{m:.1f} ± {s:.1f}',ha='center',fontsize=30,weight='bold')
ax.set(ylim=(0,11),ylabel='相似性评分（1—10）')
ax.set_yticks([1,3,5,7,9,10]);ax.axhline(10,ls=':',color=GREY,lw=1)
ax.set_xticks([0,1,2],['句子 1\n用于逐人优化','句子 2\n沿用匹配参数','句子 3\n沿用匹配参数'])
ax.set_title('同一说话人换一句话，匹配程度也可能改变',loc='left',fontsize=32,pad=22)
fig.text(.52,.045,'15 位成人 SSD-CI 使用者 · Kopsch 等（2025）\n柱为均值，误差线为 ±1 标准差；个体评分仍限制在 1—10',ha='center',fontsize=25,color=GREY)
save(fig,'04-match-generalization')
(OUT/'match-generalization.csv').write_text('sentence,mean,SD,n\n1,9.7,0.5,15\n2,8.4,1.5,15\n3,8.9,1.3,15\n',encoding='utf8')

# Reuse the repository's already licensed recording; no new recording is fetched.
source=ROOT/'public/figures/core-eight/additions/libri1.ogg'
full,fs0=sf.read(source);assert fs0==22050 and full.ndim==1
start,end=3.3,9.3
x=resample_poly(full[round(start*fs0):round(end*fs0)],320,441)
fs=16000;assert len(x)==fs*6
ramp=min(160,len(x)//2);fade=np.ones(len(x));fade[:ramp]=np.linspace(0,1,ramp);fade[-ramp:]=np.linspace(1,0,ramp)
low,high=200.,7000.
x=sosfiltfilt(butter(4,[low,high],btype='bandpass',fs=fs,output='sos'),x)*fade
seed=20261009
outputs={'reference':x};boundaries={}
for count in [4,8,16]:
    edges=np.geomspace(low,high,count+1);boundaries[str(count)]=edges.tolist()
    rng=np.random.default_rng(seed+count);out=np.zeros_like(x)
    for lo,hi in zip(edges[:-1],edges[1:]):
        bp=butter(4,[lo,hi],btype='bandpass',fs=fs,output='sos')
        signal=sosfiltfilt(bp,x)
        env=sosfiltfilt(butter(2,160,btype='lowpass',fs=fs,output='sos'),np.abs(signal))
        env=np.maximum(env,0)
        carrier=sosfiltfilt(bp,rng.standard_normal(len(x)))
        carrier/=np.sqrt(np.mean(carrier**2))
        out+=sosfiltfilt(bp,env*carrier)
    outputs[str(count)]=out*fade
rms=lambda a:float(np.sqrt(np.mean(a*a)))
unit={key:a/rms(a) for key,a in outputs.items()}
target=min(.06,.85/max(float(np.max(abs(a))) for a in unit.values()))
records={}
for key,a in unit.items():
    a=a*target;assert np.isfinite(a).all() and np.max(abs(a))<=.85+1e-10
    name='reference.wav' if key=='reference' else f'noise-{key}.wav'
    sf.write(AUDIO/name,a,fs,subtype='PCM_16')
    stored,stored_fs=sf.read(AUDIO/name);assert stored_fs==fs and len(stored)==fs*6
    records[key]={'file':name,'rms':rms(stored),'peak':float(np.max(abs(stored))),
                  'sha256':hashlib.sha256((AUDIO/name).read_bytes()).hexdigest()}
assert max(v['rms'] for v in records.values())-min(v['rms'] for v in records.values())<2e-6
provenance={'checked_at':'2026-10-09','figures':sizes,
 'published_data':{'source_doi':'10.1038/s41598-025-25711-z','location':'Results; similarity scores after optimization and on two further sentences','n':n,'means':means.tolist(),'SD':sds.tolist(),'paired_tests':'Use published paired tests; not inferable from summary SDs.'},
 'audio':{'source_url':'https://raw.githubusercontent.com/librosa/data/main/audio/5703-47212-0000.ogg',
  'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'work':'The Ashiel Mystery',
  'reader':'Garth Comira','recording_id':'5703-47212-0000','license':'CC BY 4.0',
  'license_url':'https://creativecommons.org/licenses/by/4.0/','excerpt_seconds':[start,end],
  'modifications':'Excerpt, resampling, common bandpass, fades, RMS normalization; noise channel vocoding for 4/8/16 outputs.',
  'sample_rate_Hz':fs,'duration_seconds':6,'band_Hz':[low,high],
  'band_spacing':'logarithmic','boundaries_Hz':boundaries,
  'filters':'4th-order Butterworth analysis/synthesis; 2nd-order envelope LP; offline SOS forward-backward filtering (effective responses differ from single pass).',
  'envelope':'full-wave rectification, 160 Hz lowpass, negative values clipped to zero',
  'noise_seed_base':seed,'noise_seed_rule':'base + channel count','fades_ms':10,
  'normalization':'equal RMS over complete 6 s after common preprocessing; not perceptual equal loudness or SPL calibration',
  'files':records,'target_rms':target,'claims':'Teaching example only; no implant user, clinical processor, frequency mismatch or current-spread model.'}}
(OUT/'figure-and-audio-verification.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'figures':sizes,'audio':records,'equal_RMS_tolerance':2e-6},ensure_ascii=False))
