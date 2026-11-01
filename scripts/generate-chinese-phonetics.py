"""Original conceptual phonetics figures and explicitly synthetic acoustic demonstrations."""
from pathlib import Path
import json
import wave
import numpy as np
from scipy import signal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
FIG=ROOT/'public/figures/chinese-phonetics'; AUDIO=ROOT/'public/audio/chinese-phonetics'
REC=ROOT/'docs/research/chinese-phonetics-2026-11-02'; PRE=ROOT/'artifacts/chinese-phonetics/figures'
for p in (FIG,AUDIO,REC,PRE):p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':12,'svg.fonttype':'path',
 'svg.hashsalt':'chinese-phonetics-course','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,M,P='#22658c','#31755e','#b44e37','#61727d','#79639d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创汉语语音学教学示意 / 合成计算 · 非说话人实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.05,1,.93),w_pad=3,h_pad=3)
    p=FIG/f'{name}.svg';fig.savefig(p,metadata={'Date':None},facecolor='white')
    p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/f'{name}.png',dpi=105,facecolor='white');plt.close(fig)
def box(ax,x,y,w,h,text,color=B):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',ec=color,fc='#f7f9fc',lw=1.5));ax.text(x+w/2,y+h/2,text,ha='center',va='center',color=color,fontsize=15)

fig,ax=plt.subplots(figsize=(14,6));ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
box(ax,.36,.77,.28,.12,'光 guāng：一个音节',P)
box(ax,.08,.47,.19,.15,'声母 g',B);box(ax,.36,.47,.47,.15,'韵母 uang',G)
box(ax,.35,.13,.14,.16,'韵头 u',G);box(ax,.53,.13,.14,.16,'韵腹 a',G);box(ax,.71,.13,.14,.16,'韵尾 ng',G)
for start,end in [((.44,.77),(.18,.63)),((.56,.77),(.6,.63)),((.46,.47),(.42,.30)),((.6,.47),(.6,.30)),((.75,.47),(.78,.30))]:
    ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':M})
ax.text(.91,.54,'声调：阴平\n叠加在音节上',ha='center',color=R,fontsize=14)
ax.text(.07,.11,'传统结构分解\n不是逐字母的实际音值',color=M,fontsize=13)
fig.suptitle('声母、韵母、声调与音素不在同一个分析层次',fontsize=18,fontweight='bold');save(fig,'syllable-and-spelling')

groups=[('双唇',['b','p','m']),('唇齿',['f']),('舌尖中',['d','t','n','l']),('舌根',['g','k','h']),('舌面前',['j','q','x']),('舌尖后',['zh','ch','sh','r']),('舌尖前',['z','c','s'])]
rows=['塞音','塞擦音','擦音','鼻音','近音／边近音'];cells={(0,0):'b / p',(0,2):'d / t',(0,3):'g / k',(1,4):'j / q',(1,5):'zh / ch',(1,6):'z / c',(2,1):'f',(2,3):'h',(2,4):'x',(2,5):'sh',(2,6):'s',(3,0):'m',(3,2):'n',(4,2):'l',(4,5):'r *'}
fig,ax=plt.subplots(figsize=(14,6));ax.set(xlim=(-.5,6.5),ylim=(4.5,-.5),xticks=range(7),xticklabels=[g[0] for g in groups],yticks=range(5),yticklabels=rows)
for (r,c),text in cells.items():ax.text(c,r,text,ha='center',va='center',color=B,fontsize=17,bbox={'facecolor':'#edf3f7','edgecolor':'none','boxstyle':'round,pad=.4'})
ax.set_xticks(np.arange(-.5,7),minor=True);ax.set_yticks(np.arange(-.5,5),minor=True);ax.grid(which='minor',color='#e4e8ed');ax.tick_params(which='both',length=0)
ax.set_title('拼音分组；* r 的实际实现也可带摩擦，不是所有说话人的唯一窄式音值',fontsize=13,pad=18)
fig.suptitle('同一部位可以有不同方式，同一方式可以出现在不同部位',fontsize=18,fontweight='bold');save(fig,'consonant-dimensions')

fs=16000;duration=.6;t=np.arange(round(fs*duration))/fs;f0=130
source=sum(np.sin(2*np.pi*k*f0*t)/k for k in range(1,31))
settings={'front':([350,2200,3000],[80,120,150]),'back':([350,800,2200],[80,120,150])}
filters={};filter_gains={};waves={};freq=np.linspace(0,5000,10001)
for name,(formants,bws) in settings.items():
    a=np.array([1.])
    for f,bw in zip(formants,bws):
        radius=np.exp(-np.pi*bw/fs);a=np.convolve(a,[1,-2*radius*np.cos(2*np.pi*f/fs),radius**2])
    _,hh=signal.freqz([1],a,worN=32769,fs=fs);filter_gains[name]=1/np.max(abs(hh))
    filters[name]=a;waves[name]=signal.lfilter([filter_gains[name]],a,source)
edge=np.sin(np.linspace(0,np.pi/2,320))**2;envelope=np.ones(len(t));envelope[:320]=edge;envelope[-320:]=edge[::-1]
waves={name:values*envelope for name,values in waves.items()};vowel_gain=.6/max(np.max(abs(v)) for v in waves.values())
fig,ax=plt.subplots(1,2,figsize=(14,6));k=np.arange(1,31)
ax[0].stem(k*f0,20*np.log10(1/k),basefmt=' ');ax[0].set(xlabel='频率（Hz）',ylabel='源谐波幅度（相对 dB）',title='（a）两段声音共用 F0=130 Hz 的谐波声源',xlim=(0,4000))
for name,color,label in [('front',B,'滤波器 A：350 / 2200 / 3000 Hz'),('back',G,'滤波器 B：350 / 800 / 2200 Hz')]:
    _,h=signal.freqz([1],filters[name],worN=freq,fs=fs);db=20*np.log10(abs(h));ax[1].plot(freq,db-db.max(),color=color,label=label)
ax[1].set(xlabel='频率（Hz）',ylabel='滤波器幅度（各自最大值归零 dB）',title='（b）改变共振器参数，保留同一声源',ylim=(-65,3));ax[1].legend(fontsize=10)
fig.suptitle('基频决定声源周期，共振结构改变谱包络',fontsize=18,fontweight='bold');save(fig,'source-and-resonance')

vowels={'i（衣）':(300,2300),'ü（迂）':(300,1800),'u（乌）':(350,800),'a（啊）':(800,1300)}
fig,ax=plt.subplots(figsize=(12,6.5))
for label,(f1,f2) in vowels.items():ax.scatter(f2,f1,s=90,color=B);ax.annotate(label,(f2,f1),xytext=(8,12),textcoords='offset points',fontsize=16)
ax.set(xlim=(2600,500),ylim=(1000,180),xlabel='第二共振峰参数 F2（Hz；左高右低）',ylabel='第一共振峰参数 F1（Hz；上低下高）')
ax.grid(color='#e3e8ed');ax.text(.02,.03,'点为教学设定，不是普通话人群均值或音位边界\n该坐标不是舌头的照片或按比例位置图',transform=ax.transAxes,color=M,fontsize=12)
fig.suptitle('用 F1–F2 空间比较元音，同时保留发音与声学的区别',fontsize=18,fontweight='bold');save(fig,'vowel-space')

toneN=7200;u=np.arange(toneN)/(toneN-1);tone_f0=[np.full(toneN,200.),np.interp(u,[0,1],[140,190]),np.interp(u,[0,.55,1],[135,105,165]),np.interp(u,[0,1],[205,110])]
tone_names=['阴平：常见教学记值 55','阳平：常见教学记值 35','上声：常见教学记值 214','去声：常见教学记值 51']
tone_waves=[]
fig,axes=plt.subplots(2,2,figsize=(14,8))
for i,(ax,f,label,color) in enumerate(zip(axes.ravel(),tone_f0,tone_names,[B,G,P,R])):
    ax.plot(u,f,color=color,lw=2);ax.set(xlabel='归一化音节时间',ylabel='合成 F0（Hz）',title=label,ylim=(90,220))
    phase=2*np.pi*np.cumsum(f)/fs;values=sum(np.sin(k*phase)/k for k in range(1,9));env=np.ones(toneN);env[:320]=edge;env[-320:]=edge[::-1];tone_waves.append(values*env)
fig.suptitle('调类、五度记值与具体 F0 曲线需要分开理解',fontsize=18,fontweight='bold');save(fig,'four-tone-contours')
tone_gain=.55/max(np.max(abs(v)) for v in tone_waves);pause=np.zeros(3200)
tone_sequence=np.concatenate([part for i,v in enumerate(tone_waves) for part in ((v*tone_gain,pause) if i<3 else (v*tone_gain,))])

fig,ax=plt.subplots(1,2,figsize=(14,6));q=np.linspace(0,1,300)
for a,nexttone,title in [(ax[0],3,'（a）你好：同一变调域内 /3+3/'),(ax[1],1,'（b）老师：/3+1/ 的常见实现')]:
    first=np.interp(q,[0,1],[.25,.72]) if nexttone==3 else np.interp(q,[0,1],[.35,.12])
    second=np.interp(q,[0,.6,1],[.35,.12,.45]) if nexttone==3 else np.full(len(q),.82)
    a.plot(q,first,color=B);a.plot(1.15+q,second,color=G);a.set(xlim=(0,2.15),ylim=(0,1),xlabel='两个音节的示意时间',ylabel='相对高低（无物理单位）',title=title)
    a.text(.5,.92,'首音节呈升调' if nexttone==3 else '首音节常保持低段',ha='center',color=B,fontsize=12)
fig.suptitle('连读形式受相邻声调、语速及韵律分组约束',fontsize=18,fontweight='bold');save(fig,'connected-tone-patterns')

rng=np.random.default_rng(20261102);vot_cases={};tv=np.arange(3200)/fs;release=800
fig,axes=plt.subplots(2,1,figsize=(14,7))
for ax,vot,color in zip(axes,[12,65],[B,G]):
    onset=release+round(vot*fs/1000);samples=np.zeros(len(tv));samples[release:onset]=.06*rng.standard_normal(onset-release);samples[release]=.45
    samples[onset:]=.25*np.sin(2*np.pi*150*np.arange(len(tv)-onset)/fs)
    ax.plot(tv*1000,samples,color=color,lw=.8);ax.axvline(tv[release]*1000,color=M,ls='--');ax.axvline(tv[onset]*1000,color=R,ls='--')
    ax.annotate('',xy=(tv[onset]*1000,.36),xytext=(tv[release]*1000,.36),arrowprops={'arrowstyle':'<->','color':R});ax.text((tv[release]+tv[onset])*500,.4,f'VOT = {vot} ms',ha='center',color=R)
    ax.set(xlabel='时间（ms）',ylabel='合成幅度',xlim=(25,160),ylim=(-.4,.55));vot_cases[str(vot)]={'release_sample':release,'periodic_onset_sample':onset}
fig.suptitle('释放时刻与周期发声起点之间的时间，不是气流强弱的分数',fontsize=18,fontweight='bold');save(fig,'vot-landmarks')

fig,axes=plt.subplots(1,2,figsize=(14,6));window_records=[]
for ax,ms in zip(axes,[5,40]):
    n=round(fs*ms/1000);w=signal.windows.hann(n,sym=False)
    f,tt,z=signal.stft(waves['front']*vowel_gain,fs=fs,window=w,nperseg=n,noverlap=n-32,nfft=2048,boundary=None,padded=False)
    db=20*np.log10(np.maximum(abs(z),1e-8));db-=db.max();ax.pcolormesh(tt,f,db,vmin=-55,vmax=0,shading='auto',cmap='magma',rasterized=True)
    ax.set(xlabel='时间（s）',ylabel='频率（Hz）',ylim=(0,4000),xlim=(.05,.25),title=f'{ms} ms 周期 Hann 窗；相同合成信号')
    window_records.append({'duration_ms':ms,'samples':n,'ENBW_Hz':float(fs*np.sum(w*w)/np.sum(w)**2),'FFT_grid_Hz':fs/2048})
fig.suptitle('短窗与长窗显示不同细节，FFT网格不等于分析带宽',fontsize=18,fontweight='bold');save(fig,'spectrogram-windows')

audio_arrays={'tone-contours':tone_sequence,'resonance-front':waves['front']*vowel_gain,'resonance-back':waves['back']*vowel_gain}
for name,values in audio_arrays.items():
    pcm=np.rint(values*32767).astype('<i2')
    with wave.open(str(AUDIO/f'{name}.wav'),'wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(fs);w.writeframes(pcm.tobytes())
result={'fs_Hz':fs,'initial_groups':[{'label':label,'pinyin':items} for label,items in groups],
 'vowel_space_parameters_Hz':{label:{'F1':v[0],'F2':v[1]} for label,v in vowels.items()},
 'resonators':{name:{'frequency_parameters_Hz':v[0],'bandwidth_parameters_Hz':v[1],'denominator':filters[name].tolist(),'numerator_gain':float(filter_gains[name])} for name,v in settings.items()},
 'vowel_source_F0_Hz':f0,'vowel_samples':len(t),'vowel_pair_common_gain':float(vowel_gain),
 'tone_samples_each':toneN,'tone_pause_samples':len(pause),'tone_common_gain':float(tone_gain),
 'tone_contour_endpoints_Hz':[[float(v[0]),float(v.min()),float(v[-1])] for v in tone_f0],
 'tone_sequence_samples':len(tone_sequence),'VOT':vot_cases,'spectrograms':window_records,
 'octave_error_semitones':float(12*np.log2(260/130)),
 'audio':{name:{'samples':len(v),'peak':float(np.max(abs(v)))} for name,v in audio_arrays.items()}}
(REC/'calculations.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
