"""Original explanatory figures and synthetic WAVs, not participant measurements."""
from pathlib import Path
import json,re,wave
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/auditory-illusion'; AUDIO=ROOT/'public/audio/auditory-illusion'
DOC=ROOT/'docs/research/auditory-illusion-2026-10-10'
for d in [OUT,AUDIO,DOC]:d.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':18,'svg.fonttype':'path','axes.spines.top':False,'axes.spines.right':False,'axes.unicode_minus':False})
BLUE,ORANGE,GREEN,GRAY='#286a9b','#b65d2e','#327965','#687481'
fs=44100;audio_records=[]
def save(fig,name,h):
 fig.savefig(OUT/(name+'.png'),dpi=100,facecolor='white');fig.savefig(OUT/(name+'.svg'),facecolor='white')
 p=OUT/(name+'.svg');s=p.read_text(encoding='utf-8');p.write_text(re.sub(r'width="[^"]+" height="[^"]+"',f'width="1400" height="{h}"',s,count=1),encoding='utf-8');plt.close(fig)
def wav(name,x):
 assert np.max(np.abs(x))<.99
 with wave.open(str(AUDIO/(name+'.wav')),'wb') as w:
  w.setnchannels(1 if x.ndim==1 else x.shape[1]);w.setsampwidth(2);w.setframerate(fs);w.writeframes(np.round(x*32767).astype('<i2').tobytes())
 audio_records.append({'file':name+'.wav','sample_rate':fs,'channels':1 if x.ndim==1 else x.shape[1],'duration_s':len(x)/fs,'peak':float(np.max(np.abs(x))),'rms':float(np.sqrt(np.mean(x*x)))})
def ramp(n,ms=10):
 r=int(fs*ms/1000);env=np.ones(n);edge=.5-.5*np.cos(np.linspace(0,np.pi,r));env[:r]=edge;env[-r:]=edge[::-1];return env

# Three conditions share one target amplitude, one noise realization and one gain.
t=np.arange(int(4.7*fs))/fs;tone=.045*np.sin(2*np.pi*1000*t)*ramp(len(t))
gate=np.ones(len(t));ngate=np.zeros(len(t));gaps=[(.8,1.1),(2.2,2.5),(3.6,3.9)]
edge=int(.01*fs)
for start,end in gaps:
 a,b=int(start*fs),int(end*fs);gate[a:b]=0;gate[a-edge:a]=.5+.5*np.cos(np.linspace(0,np.pi,edge));gate[b:b+edge]=.5-.5*np.cos(np.linspace(0,np.pi,edge));ngate[a:b]=ramp(b-a)
rng=np.random.default_rng(20261010);white=rng.standard_normal(len(t));spec=np.fft.rfft(white);freq=np.fft.rfftfreq(len(t),1/fs)
spec[(freq<300)|(freq>5000)]=0;noise=np.fft.irfft(spec,n=len(t));noise*=.09/np.sqrt(np.mean(noise**2));noise*=ngate
conditions=[tone*gate,tone*gate+noise,tone+noise];gain=.6/max(np.max(np.abs(s)) for s in conditions)
for name,s in zip(['continuity-silence','continuity-noise','continuity-present'],conditions):wav(name,s*gain)
assert all(np.all((tone*gate)[int(a*fs):int(b*fs)]==0) for a,b in gaps)
assert np.allclose(conditions[1]-conditions[0],noise,atol=1e-15)
fig,axs=plt.subplots(3,1,figsize=(14,7.6),sharex=True)
for i,(ax,label) in enumerate(zip(axs,['（a）删去目标音：静音缺口','（b）删去目标音：缺口内只有噪声','（c）保留目标音：噪声叠加在目标上'])):
 ax.plot(t,(gate if i<2 else np.ones(len(t)))*ramp(len(t)),color=BLUE,lw=2.5,label='目标幅度包络 / 相对值')
 if i>0:
  for a,b in gaps:ax.axvspan(a,b,facecolor=ORANGE,alpha=.18,label='噪声时段' if a==gaps[0][0] else None)
 ax.set(ylim=(-.1,1.45),yticks=[0,1],ylabel='目标 / 相对值',title=label);ax.grid(alpha=.13)
fig.legend(*axs[1].get_legend_handles_labels(),loc='upper center',ncol=2,fontsize=15,bbox_to_anchor=(.5,1))
axs[2].set(xlabel='时间 / s',xlim=(0,4.7))
fig.text(.5,.026,'蓝线仅表示物理目标包络；橙区表示噪声时段，不是知觉或神经响应。',ha='center',fontsize=18,color=GRAY)
fig.subplots_adjust(left=.11,right=.96,bottom=.14,top=.86,hspace=.8);save(fig,'01-continuity-controls',760)

# Fixed spectral envelope and octave-spaced partials, four repeated 12-step cycles.
pitches=np.arange(12);ks=np.arange(8);fq=55*2**(ks[:,None]+pitches[None,:]/12);amp=np.exp(-.5*(np.log2(fq/880)/1.1)**2)
note_n=int(.18*fs);nt=np.arange(note_n)/fs;tones=[]
for p in pitches:tones.append(np.sum(amp[:,p,None]*np.sin(2*np.pi*fq[:,p,None]*nt),axis=0)*ramp(note_n))
sg=.38/max(np.max(np.abs(s)) for s in tones);sequence=np.concatenate([np.concatenate([s*sg,np.zeros(int(.02*fs))]) for s in tones]);wav('shepard-ascending',np.tile(sequence,4))
assert np.max(fq)<fs/2
fig,axs=plt.subplots(1,2,figsize=(14,7.1),gridspec_kw={'width_ratios':[1.4,1]})
for k in ks:
 axs[0].plot(pitches,np.log2(fq[k]/55),color=GRAY,alpha=.45,lw=1)
 axs[0].scatter(pitches,np.log2(fq[k]/55),s=12+200*amp[k],c=amp[k],cmap='Blues',vmin=0,vmax=1,edgecolors=BLUE,lw=.5)
axs[0].set(title='（a）每一步包含多组八度成分',xlabel='循环内的半音步 p',ylabel='频率 / Hz（对数轴）',xticks=[0,3,6,9,11],yticks=np.arange(9),yticklabels=[str(int(55*2**k)) for k in range(9)],xlim=(-.6,11.6),ylim=(-.3,9.2));axs[0].grid(alpha=.13)
grid=np.geomspace(45,22000,500);axs[1].plot(np.log2(grid/55),np.exp(-.5*(np.log2(grid/880)/1.1)**2),color=BLUE,lw=3)
axs[1].set(title='（b）固定频率包络',xlabel='频率 / Hz（对数轴）',ylabel='分量幅度 / 相对值',xticks=[0,2,4,6,8],xticklabels=['55','220','880','3520','14080'],xlim=(-.3,8.7),ylim=(0,1.1));axs[1].grid(alpha=.13)
fig.text(.5,.08,'半音步序列 0 → 1 → … → 11 → 0；高低端分量减弱，整体谱形保持相近。',ha='center',fontsize=18,color=GREEN)
fig.text(.5,.025,'教学合成的物理成分与幅度；点大小不是听者报告、响度或神经活动。',ha='center',fontsize=17,color=GRAY)
fig.subplots_adjust(left=.085,right=.97,bottom=.23,top=.90,wspace=.34);save(fig,'02-shepard-components',710)

# Original re-synthesis of the ascending/descending scale routing principle.
midi=np.array([60,62,64,65,67,69,71,72]);up=440*2**((midi-69)/12);down=up[::-1];steps=np.arange(8)
left=np.where(steps%2==0,up,down);right=np.where(steps%2==0,down,up);upper=np.maximum(left,right);lower=np.minimum(left,right)
nn=int(.25*fs);tt=np.arange(nn)/fs
def line(freqs):return np.concatenate([.16*np.sin(2*np.pi*f*tt)*ramp(nn) for f in freqs])
l,r=line(left),line(right);stereo=np.column_stack([np.tile(l,4),np.tile(r,4)])
wav('scale-stereo',stereo);wav('scale-left',np.tile(l,4));wav('scale-right',np.tile(r,4))
assert np.allclose(np.sort(np.stack([left,right]),axis=0),np.sort(np.stack([up,down]),axis=0))
fig,axs=plt.subplots(2,1,figsize=(14,8),sharex=True)
for ax,a,b,labels in [(axs[0],left,right,['左声道输入','右声道输入']),(axs[1],upper,lower,['高线组织示意','低线组织示意'])]:
 for v,c,ls,marker,label in [(a,BLUE,'-','o',labels[0]),(b,ORANGE,'--','s',labels[1])]:
  ax.plot(steps+1,69+12*np.log2(v/440),color=c,ls=ls,marker=marker,lw=2.5,ms=8,label=label)
 ax.set(yticks=midi,yticklabels=['C4','D4','E4','F4','G4','A4','B4','C5'],ylabel='等律音级（半音坐标）',ylim=(59,73));ax.tick_params(axis='y',labelsize=14);ax.grid(alpha=.15);ax.legend(loc='center left',bbox_to_anchor=(1.015,.5),fontsize=15)
axs[0].set_title('（a）两条音阶逐时交换声道');axs[1].set_title('（b）按音高邻近连接的一种知觉组织示意');axs[1].set(xlabel='事件序号',xticks=np.arange(1,9),xlim=(.7,8.3))
fig.text(.5,.026,'下排不是新增声音，也不是所有人的报告；连线表示事件组织，不是连续滑音。',ha='center',fontsize=18,color=GRAY)
fig.subplots_adjust(left=.10,right=.78,bottom=.17,top=.93,hspace=.47);save(fig,'03-scale-routing',800)

fig,ax=plt.subplots(figsize=(14,6.8));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.955,'相同声音可以接受不同任务；每个指标回答不同问题',ha='center',fontsize=26)
rows=[(.75,'物理输入','声道、频谱、缺口与声级','记录：实际呈现了什么',BLUE),(.54,'知觉报告','连续性、声流、方向或歌唱感','记录：听起来是什么',ORANGE),(.33,'任务表现','识别、辨别、匹配或信心','记录：怎样作答与利用',GREEN),(.12,'神经证据','单元、脑电或群体成像','记录：哪类响应随条件改变',GRAY)]
for y,label,body,end,c in rows:
 ax.add_patch(FancyBboxPatch((.025,y-.075),.95,.15,boxstyle='round,pad=.008',facecolor='#f6f7f8',edgecolor=c,lw=1.3));ax.text(.055,y,label,va='center',color=c,fontsize=23);ax.text(.22,y,body,va='center',fontsize=20);ax.text(.66,y,end,va='center',fontsize=18)
fig.subplots_adjust(left=.025,right=.975,bottom=.04,top=.97);save(fig,'04-evidence-levels',680)
report={'nature':'Original teaching stimuli and explanatory figures; no empirical dataset','figures':4,'sample_rate':fs,'random_seed':20261010,'continuity':{'target_Hz':1000,'duration_s':4.7,'gaps_s':gaps,'ramps_ms':10,'noise_band_Hz':[300,5000],'tone_peak_before_gain':.045,'noise_RMS_before_gate':.09,'common_gain':float(gain),'target_absent_in_deleted_intervals':True,'shared_noise':True},'shepard':{'base_Hz':55,'partials_k':[0,7],'steps':12,'center_Hz':880,'sigma_octaves':1.1,'tone_s':.18,'gap_s':.02,'cycles':4,'max_component_Hz':float(np.max(fq)),'common_gain':float(sg)},'scale':{'midi_up':midi.tolist(),'left_Hz':left.tolist(),'right_Hz':right.tolist(),'tone_s':.25,'cycles':4,'ramps_ms':10,'channel_pair_matches_original_scales':True},'audio':audio_records,'checks_passed':True}
(DOC/'figure-audio-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'figures':4,'audio_files':len(audio_records),'checks_passed':True}))
