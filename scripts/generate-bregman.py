"""Original teaching figures and synthesized sounds; no listener measurements."""
from pathlib import Path
import json, wave, hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/albert-bregman'
AUDIO=ROOT/'public/audio/albert-bregman'
RESEARCH=ROOT/'docs/research/albert-bregman-2026-10-10'
for p in [OUT,AUDIO,RESEARCH]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':13,'svg.fonttype':'path'})
BLUE,ORANGE,GRAY='#276582','#af6435','#526472'
figures=[]
def save(fig,name,parameters):
    for ext in ['svg','png']:
        p=OUT/(name+'.'+ext);fig.savefig(p,dpi=100,facecolor='white')
        if ext=='svg':p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)
    figures.append({'name':name,'width':1280,'height':650,'parameters':parameters,'nature':'original teaching example; no measured perception or original experimental figure'})
def pair(title,subtitle):
    fig,axs=plt.subplots(1,2,figsize=(12.8,6.5));fig.subplots_adjust(left=.08,right=.97,bottom=.19,top=.74,wspace=.28)
    fig.suptitle(title,fontsize=23,fontweight='bold',y=.96)
    fig.text(.5,.865,subtitle,ha='center',fontsize=14,color=GRAY)
    for ax in axs:
        ax.set_xlabel('时间（s）');ax.set_ylabel('频率（Hz）')
        ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.16)
    return fig,axs
def bar(ax,t,f,d=.1,color=BLUE):
    ax.plot([t,t+d],[f,f],color=color,lw=8,solid_capstyle='butt',zorder=3)
def bracket(ax,t,lo,hi):
    ax.plot([t+.025,t,t,t+.025],[lo,lo,hi,hi],color=GRAY,lw=1.6)

fig,axs=pair('同一时刻融合，还是跨时间连接？','两类问题可以使用不同报告任务')
ax=axs[0];ax.set(xlim=(0,1.3),ylim=(200,1750),yticks=[500,1000,1500]);ax.set_title('（a）同时成分的候选融合',pad=18)
for t in [.2,.6,1.0]:
    for f in [500,1000,1500]:bar(ax,t,f)
    bracket(ax,t-.07,500,1500)
ax=axs[1];ax.set(xlim=(0,1.3),ylim=(200,1750),yticks=[500,900,1500]);ax.set_title('（b）同频事件的候选连接',pad=18)
times=np.arange(6)*.2+.05;freqs=np.tile([500,900],3)
for t,f in zip(times,freqs):bar(ax,t,f,color=BLUE if f==900 else ORANGE)
for f,c in [(500,ORANGE),(900,BLUE)]:
    ts=times[freqs==f]+.05;ax.plot(ts,[f]*3,'--',color=c,lw=1.8)
fig.text(.5,.055,'原创教学设定；括号与虚线表示候选关系，不表示实测知觉或神经连线',ha='center',fontsize=12,color=GRAY)
save(fig,'grouping-directions',{'simultaneous_hz':[500,1000,1500],'simultaneous_onsets_s':[.2,.6,1.0],'sequential_hz':[500,900]*3,'sequential_onsets_s':times.tolist(),'tone_duration_s':.1})

seq=np.array([900,300,1100,350,1300,400]*2);ts=np.arange(12)*.1
fig,axs=pair('同一个六音输入，两种组织解释','H1–L1–H2–L2–H3–L3重复；每音100 ms，无额外间隔')
for ax,title in zip(axs,['（a）按物理事件顺序连接','（b）按高、低频组分别连接']):
    ax.set(xlim=(-.03,1.25),ylim=(180,1470),yticks=[300,400,900,1100,1300]);ax.set_title(title,pad=18)
    for t,f in zip(ts,seq):bar(ax,t,f,color=BLUE if f>500 else ORANGE)
axs[0].plot(ts+.05,seq,'--',color=GRAY,lw=1.2,alpha=.7)
for mask,c in [(seq>500,BLUE),(seq<500,ORANGE)]:axs[1].plot(ts[mask]+.05,seq[mask],'--',color=c,lw=1.7)
fig.text(.5,.055,'两面板的时间、频率完全相同；线表示候选组织，不是听者数据或必然体验',ha='center',fontsize=12,color=GRAY)
save(fig,'six-tone-streams',{'hz':seq.tolist(),'onsets_s':ts.tolist(),'duration_s':.1,'same_input_in_both_panels':True})

fig,axs=pair('先行音与同步成分：分组线索可以竞争','B=900 Hz、C=1400 Hz，在0.35 s同步开始；仅改变A的频率')
for ax,af,title in zip(axs,[900,400],['（a）A=900 Hz：与B同频','（b）A=400 Hz：远离B']):
    ax.set(xlim=(-.04,.66),ylim=(200,1620),yticks=[400,900,1400]);ax.set_title(title,pad=18)
    for t,f,label in [(0,af,'A'),(.35,900,'B'),(.35,1400,'C')]:
        bar(ax,t,f,d=.12,color=ORANGE if label=='A' else BLUE)
        ax.text(t+.06,f+65,label,ha='center',fontsize=17,fontweight='bold')
    bracket(ax,.51,900,1400)
    if af==900:ax.plot([.12,.35],[900,900],'--',color=ORANGE,lw=1.9)
fig.text(.5,.055,'B、C保持不变；虚线与括号表示候选联系，不表示测得的融合强度',ha='center',fontsize=12,color=GRAY)
save(fig,'grouping-competition',{'A_hz':[900,400],'A_onset_s':0,'B_hz':900,'C_hz':1400,'BC_onset_s':.35,'all_durations_s':.12})

fig,axs=plt.subplots(3,1,figsize=(12.8,6.5),sharex=True);fig.subplots_adjust(left=.31,right=.94,bottom=.17,top=.76,hspace=.55)
fig.suptitle('目标实际存在，与目标听起来连续',fontsize=23,fontweight='bold',y=.96)
fig.text(.5,.865,'700 Hz目标；中央0.35—0.65 s为对照时段',ha='center',fontsize=14,color=GRAY)
for i,(ax,label) in enumerate(zip(axs,['（a）目标缺失，静音','（b）目标缺失，填入噪声','（c）目标连续，叠加噪声'])):
    ax.set(xlim=(0,1),ylim=(0,1),yticks=[]);ax.spines[['top','right','left']].set_visible(False)
    ax.text(-.045,.5,label,ha='right',va='center',transform=ax.transAxes,fontsize=14)
    if i:
        ax.add_patch(Rectangle((.35,.12),.3,.76,facecolor='#dce2e7',edgecolor=GRAY,alpha=.8))
        ax.text(.5,.8,'噪声',ha='center',fontsize=11,color=GRAY)
    if i==2:ax.plot([0,1],[.5,.5],color=BLUE,lw=4)
    else:
        for a,b in [(0,.35),(.65,1)]:ax.plot([a,b],[.5,.5],color=BLUE,lw=4)
    if i==1:ax.plot([.35,.65],[.5,.5],'--',color=ORANGE,lw=2)
    if i<2:ax.tick_params(labelbottom=False)
axs[2].set_xlabel('时间（s）')
fig.text(.5,.045,'蓝实线：物理目标存在　灰区域：物理噪声存在　橙虚线：候选连续性解释',ha='center',fontsize=12,color=GRAY)
save(fig,'continuity-conditions',{'target_hz':700,'gap_start_s':.35,'gap_end_s':.65,'conditions':['target absent + silence','target absent + noise','target present + noise'],'dashed_line_is_not_a_physical_signal':True})
(RESEARCH/'figure-manifest.json').write_text(json.dumps(figures,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

FS=44100;RAMP=round(.005*FS);SEED=20261010
edge=np.sin(np.linspace(0,np.pi/2,RAMP))**2
def window(n):
    w=np.ones(n);w[:RAMP]=edge;w[-RAMP:]=edge[::-1];return w
sounds=[]
def write_sound(name,x,params):
    assert np.isfinite(x).all() and np.max(np.abs(x))<1
    pcm=np.rint(x*32767).astype('<i2');p=AUDIO/(name+'.wav')
    with wave.open(str(p),'wb') as w:
        w.setnchannels(1);w.setsampwidth(2);w.setframerate(FS);w.writeframes(pcm.tobytes())
    with wave.open(str(p),'rb') as w:
        assert w.getframerate()==FS and w.getnchannels()==1 and w.getsampwidth()==2 and w.getnframes()==len(x)
        read=np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').astype(float)/32767
    assert np.max(np.abs(read-x))<=.5/32767+1e-12 and not np.any(np.abs(pcm.astype(int))==32767)
    sounds.append({'file':p.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'sample_rate_hz':FS,'channels':1,'pcm_bits':16,'duration_s':len(x)/FS,'peak_abs':float(np.max(np.abs(x))),'rms':float(np.sqrt(np.mean(x*x))),'clipped_samples':0,'parameters':params,'nature':'new synthesized teaching sound; no hearing test or calibrated SPL; no original archive recording reused'})
for name,dur,cycles in [('six-tones-slow',.3,6),('six-tones-fast',.1,20)]:
    n=round(dur*FS);t=np.arange(n)/FS
    x=np.concatenate([.2*np.sin(2*np.pi*f*t)*window(n) for f in [900,300,1100,350,1300,400]*cycles])
    assert len(x)==6*cycles*n and abs(np.max(np.abs(x))-.2)<.001
    write_sound(name,x,{'hz':[900,300,1100,350,1300,400],'duration_s':dur,'SOA_s':dur,'cycles':cycles,'tone_peak':.2,'ramp_s':.005,'equal_loudness_matched':False})
n=3*FS;t=np.arange(n)/FS;envelope=window(n);gaps=[]
for unit in range(3):
    a=round((unit+.35)*FS);b=round((unit+.65)*FS);gaps.append((a,b));envelope[a:b]=0
    envelope[a-RAMP:a]=edge[::-1];envelope[b:b+RAMP]=edge
target=.08*np.sin(2*np.pi*700*t)*envelope
noise=np.zeros(n);rng=np.random.default_rng(SEED);gap_rms=[]
for a,b in gaps:
    y=rng.standard_normal(b-a)*window(b-a);y*=.12/np.sqrt(np.mean(y*y));noise[a:b]=y
    gap_rms.append(float(np.sqrt(np.mean(y*y))));assert np.all(target[a:b]==0)
assert np.allclose(gap_rms,.12,rtol=0,atol=1e-12)
outside=np.ones(n,dtype=bool)
for a,b in gaps:outside[a:b]=False
assert np.array_equal(target[outside],(target+noise)[outside])
params={'target_hz':700,'target_peak':.08,'unit_s':1,'repetitions':3,'gap_s':[.35,.65],'ramp_s':.005,'noise_seed':SEED,'noise_rms_per_windowed_gap':gap_rms,'masking_threshold_calibrated':False}
write_sound('continuity-silence',target,{**params,'gap_filling':'silence'})
write_sound('continuity-noise',target+noise,{**params,'gap_filling':'new white noise'})
(RESEARCH/'audio-manifest.json').write_text(json.dumps(sounds,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':len(figures),'audio_durations_s':[s['duration_s'] for s in sounds],'clipped_samples':0}))
