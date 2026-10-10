"""Original deterministic teaching figures, not empirical music-perception results."""
from pathlib import Path
import json,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/music-perception'
DOC=ROOT/'docs/research/music-perception-2026-10-10'
OUT.mkdir(parents=True,exist_ok=True);DOC.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':17,'svg.fonttype':'path',
 'axes.spines.top':False,'axes.spines.right':False,'axes.unicode_minus':False})
BLUE,ORANGE,GREEN,GRAY='#286a9b','#b65d2e','#327965','#687481'
def save(fig,name,height=720):
 fig.savefig(OUT/(name+'.png'),dpi=100,facecolor='white')
 fig.savefig(OUT/(name+'.svg'),facecolor='white')
 p=OUT/(name+'.svg');s=p.read_text(encoding='utf-8')
 s=re.sub(r'width="[^"]+" height="[^"]+"',f'width="1400" height="{height}"',s,count=1)
 p.write_text(s,encoding='utf-8');plt.close(fig)

notes=np.arange(1,8);base=np.array([0,2,4,7,4,2,0]);alter=np.array([0,1,3,5,3,1,0]);shift=5
freq=220*2**(base/12);trans=220*2**((base+shift)/12)
fig,axs=plt.subplots(1,2,figsize=(14,7.2))
axs[0].plot(notes,base,'o-',color=BLUE,lw=3,label='原序列')
axs[0].plot(notes,base+shift,'s--',color=ORANGE,lw=3,label='整体升高 5 半音')
axs[0].set(title='（a）移调：每个音都升高同样的间隔',ylabel='相对 220 Hz 的位置 / 半音',ylim=(-1,14))
axs[0].text(6.9,13,'所有频率乘以约 1.335',ha='right',fontsize=16,color=GRAY)
axs[1].plot(notes,base,'o-',color=BLUE,lw=3,label='原序列：0, 2, 4, 7, 4, 2, 0')
axs[1].plot(notes,alter,'^--',color=GREEN,lw=3,label='改间隔：0, 1, 3, 5, 3, 1, 0')
axs[1].set(title='（b）方向相同，不保证间隔相同',ylabel='相对各自首音的位置 / 半音',ylim=(-1,9))
for ax in axs:
 ax.set(xlabel='音符序号',xticks=notes,xlim=(.7,7.3));ax.grid(alpha=.18)
 ax.legend(loc='upper left',fontsize=14)
fig.subplots_adjust(left=.08,right=.98,bottom=.18,top=.84,wspace=.27)
fig.text(.5,.055,'人工设定的 7 音序列；图示频率关系，不预测移调后的识别成绩。',ha='center',fontsize=17,color=GRAY)
save(fig,'01-melody-relations')

events=np.array([0,.5,.75,1.5,2,2.5,2.75,3.5]);beats=np.arange(8)*.5
async_ms=np.array([20,-10,20,-20,10,-10,30,-20]);taps=beats+async_ms/1000
fig,axs=plt.subplots(3,1,figsize=(14,9),gridspec_kw={'height_ratios':[1,1,1.5]})
axs[0].vlines(events,0,1,color=BLUE,lw=3);axs[0].scatter(events,np.ones(8),color=BLUE,s=35)
axs[0].set_title('（a）物理事件：长短间隔组成节奏',loc='left',pad=12)
axs[1].vlines(beats,0,1,color=ORANGE,lw=2,linestyle='--');axs[1].scatter([1,3],[1,1],facecolors='white',edgecolors=ORANGE,s=110,lw=2,zorder=3)
axs[1].set_title('（b）假设的节拍参照：每 0.5 s 一拍，即 120 BPM',loc='left',pad=12)
axs[1].text(1,.35,'无物理事件',ha='center',fontsize=15,color=ORANGE)
axs[1].text(3,.35,'无物理事件',ha='center',fontsize=15,color=ORANGE)
for ax in axs[:2]:
 ax.set(xlim=(-.15,3.85),ylim=(-.1,1.25),yticks=[],xticks=np.arange(0,4,.5),xlabel='时间 / s')
 ax.spines['left'].set_visible(False)
axs[2].bar(np.arange(1,9),async_ms,color=[BLUE if a>=0 else ORANGE for a in async_ms],width=.55)
axs[2].axhline(0,color=GRAY,lw=1.5);axs[2].set(title='（c）教学敲击误差：正值晚于参照，负值早于参照',
 xlabel='对应节拍序号',ylabel='敲击时刻 − 参照时刻 / ms',xticks=np.arange(1,9),ylim=(-35,40))
axs[2].grid(axis='y',alpha=.15)
fig.subplots_adjust(left=.1,right=.975,top=.93,bottom=.17,hspace=.72)
fig.text(.5,.035,'节拍网格与敲击时刻均人为设定；听者可能选择其他速度或分组，图中没有实测敲击。',ha='center',fontsize=16,color=GRAY)
save(fig,'02-rhythm-beat',900)

fs=16000;t=np.arange(int(.75*fs))/fs
wave=np.sin(2*np.pi*220*t)+np.sin(2*np.pi*224*t)
env=2*np.abs(np.cos(np.pi*4*t))
fig=plt.figure(figsize=(14,8.2));ax=fig.add_axes([.09,.58,.85,.28])
ax.plot(t,wave,color=BLUE,lw=.65,alpha=.65);ax.plot(t,env,color=ORANGE,lw=2.5,label='解析振幅包络')
ax.plot(t,-env,color=ORANGE,lw=2.5)
ax.set(title='（a）220 Hz 与 224 Hz 同相相加：每秒 4 次慢拍',xlabel='时间 / s',ylabel='相对振幅',xlim=(0,.75),ylim=(-2.4,2.4))
ax.legend(loc='upper right',fontsize=15)
ax2=fig.add_axes([.09,.16,.85,.25])
harm=np.array([220,440,660,880]);inharm=np.array([220,440,693,880])
for f in harm:ax2.vlines(f,0,1,color=BLUE,lw=2.5)
for f in inharm:ax2.vlines(f,0,-1,color=GREEN,lw=2.5,linestyle='--')
ax2.axhline(0,color=GRAY,lw=1)
ax2.set(title='（b）谱结构：仅改变一个分量，改变对 220 Hz 谐波列的匹配',xlabel='频率 / Hz',ylabel='分量标记',xlim=(100,1100),ylim=(-1.3,1.3),yticks=[-1,1],yticklabels=['改变后','谐波列'])
ax2.set_xticks([220,440,660,880]);ax2.text(710,-1.18,'693 Hz',fontsize=15,color=GREEN)
fig.text(.5,.045,'慢拍、谐波匹配与偏好是不同对象；下图标记无实际振幅含义，不是协和度评分。',ha='center',fontsize=16,color=GRAY)
save(fig,'03-acoustic-organization',820)

probs=[np.array([.8,.1,.1]),np.array([1/3]*3)]
entropy=lambda p:float(-np.sum(p*np.log2(p)))
fig=plt.figure(figsize=(14,7.2));ax=fig.add_axes([.08,.2,.48,.63]);xx=np.arange(3)
ax.bar(xx-.18,probs[0],.34,color=BLUE,label='语境 A：0.8, 0.1, 0.1')
ax.bar(xx+.18,probs[1],.34,color=ORANGE,hatch='//',label='语境 B：各为 1/3')
ax.set(title='（a）事件出现前：可能性的分布',ylabel='模型给出的条件概率',xticks=xx,xticklabels=['候选 X','候选 Y','候选 Z'],ylim=(0,1))
ax.legend(loc='upper right',fontsize=14);ax.grid(axis='y',alpha=.15)
ax2=fig.add_axes([.64,.18,.32,.65]);ax2.axis('off')
ax2.text(0,1,'（b）事件出现后的意外度',fontsize=20,weight='bold',va='top')
ax2.text(0,.82,'语境 A：不确定性 0.922 bit\n\n出现 X → 意外度 0.322 bit\n出现 Y → 意外度 3.322 bit',fontsize=18,va='top',linespacing=1.5)
ax2.text(0,.37,'语境 B：不确定性 1.585 bit\n\n出现任一候选\n→ 意外度 1.585 bit',fontsize=18,va='top',linespacing=1.5)
fig.text(.5,.055,'三候选解析算例；概率人为设定，没有训练语料，也没有预测愉悦评分。',ha='center',fontsize=17,color=GRAY)
save(fig,'04-expectation')

assert np.allclose(np.diff(base),np.diff(base+shift))
assert np.array_equal(np.sign(np.diff(base)),np.sign(np.diff(alter)))
assert not np.array_equal(np.diff(base),np.diff(alter))
assert np.allclose(trans/freq,2**(5/12))
assert np.allclose((taps-beats)*1000,async_ms)
assert np.allclose(wave,2*np.cos(np.pi*4*t)*np.sin(2*np.pi*222*t))
assert abs(entropy(probs[0])-.9219280949)<1e-9
report={'data_type':'deterministic teaching examples; no participant data or fitted results',
 'melody':{'base_semitones':base.tolist(),'transposition_semitones':5,'changed_semitones':alter.tolist(),'reference_hz':220,'frequencies_hz':freq.tolist(),'transposition_ratio':2**(5/12)},
 'rhythm':{'event_times_s':events.tolist(),'reference_beat_times_s':beats.tolist(),'assumed_bpm':120,'asynchronies_ms':async_ms.tolist(),'mean_asynchrony_ms':float(async_ms.mean()),'sample_sd_ms':float(async_ms.std(ddof=1))},
 'acoustics':{'fs_hz':fs,'duration_s':.75,'tones_hz':[220,224],'beat_rate_hz':4,'harmonic_frequencies_hz':harm.tolist(),'altered_frequencies_hz':inharm.tolist()},
 'expectation':{'distributions':[p.tolist() for p in probs],'entropy_bits':[entropy(p) for p in probs],'surprise_x_a_bits':float(-np.log2(.8)),'surprise_y_a_bits':float(-np.log2(.1))},
 'checks':'transposition, interval directions, timing units, analytic beating identity and entropy verified'}
(DOC/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':4,'verified':True,'mean_asynchrony_ms':async_ms.mean(),'sample_sd_ms':async_ms.std(ddof=1)},ensure_ascii=True))
