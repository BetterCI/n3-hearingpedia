"""Reproducible teaching examples for phase locking; no biological data or fitted model."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/figures/phase-locking'
RESEARCH = ROOT / 'docs/research/phase-locking-2026-10-10'
OUT.mkdir(parents=True, exist_ok=True)
RESEARCH.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'Microsoft YaHei', 'font.size': 13,
    'svg.fonttype': 'path', 'axes.spines.top': False, 'axes.spines.right': False,
    'axes.unicode_minus': False})
BLUE, ORANGE, GREEN, GRAY = '#286a9b', '#b65d2e', '#327965', '#687481'

def stats(degrees):
    phi = np.deg2rad(np.asarray(degrees))
    mean = np.mean(np.exp(1j*phi))
    return {'n': len(phi), 'R': float(abs(mean)),
        'R2': float(abs(np.mean(np.exp(2j*phi)))),
        'mean_phase_degrees': float(np.rad2deg(np.angle(mean)) % 360) if abs(mean)>1e-12 else None,
        'ppc': float((len(phi)*abs(mean)**2-1)/(len(phi)-1)) if len(phi)>1 else None}

def save(fig, name):
    for ext in ['svg', 'png']:
        fig.savefig(OUT / f'{name}.{ext}', dpi=160, facecolor='white', bbox_inches='tight')
    path=OUT/f'{name}.svg'
    path.write_text('\n'.join(line.rstrip() for line in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)

used_cycles=np.array([0,1,3,5,8,9,10,11])
center=np.array([60,70,80,90,90,100,110,120])
uniform=np.arange(8)*45
concentrated=np.tile(center,8)
dispersed=np.tile(uniform,8)
delayed=(concentrated+36)%360
# Equal weight opposing clusters: use mirrored offsets in both half cycles.
antipodal=np.tile([80,90,100,90,260,270,280,270],8)
examples={name:stats(data) for name,data in [('concentrated',concentrated),('uniform',dispersed),('delayed',delayed),('antipodal',antipodal)]}
assert examples['concentrated']['n']==examples['uniform']['n']==64
assert np.isclose(examples['concentrated']['R'],examples['delayed']['R'])
assert examples['uniform']['R']<1e-12 and examples['antipodal']['R']<1e-12
assert examples['antipodal']['R2']>.95

fig=plt.figure(figsize=(13,8.5))
gs=fig.add_gridspec(3,2,height_ratios=[.8,1.5,1.2],hspace=.65,wspace=.22)
ax=fig.add_subplot(gs[0,:]);t=np.linspace(0,.12,2400)
ax.plot(t*1000,np.sin(2*np.pi*100*t),color=GRAY,lw=1.7)
ax.set(xlim=(0,120),ylim=(-1.2,1.2),ylabel='相对声压',title='100 Hz 参照：12 个周期，每周期 10 ms')
for col,phases,color,title in [(0,center,BLUE,'（a）相位集中：允许跳过周期'),(1,uniform,ORANGE,'（b）相位分散：事件数完全相同')]:
    ax=fig.add_subplot(gs[1,col]);allph=[]
    for trial in range(8):
        ph=np.roll(phases,trial);times=(used_cycles+ph/360)/100
        ax.vlines(times*1000,trial+.7,trial+1.3,color=color,lw=1.7)
        allph.extend(ph)
    ax.set(xlim=(0,120),ylim=(.4,8.6),yticks=[1,4,8],xlabel='时间 / ms',ylabel='合成试次',title=title)
    for boundary in range(0,121,10):ax.axvline(boundary,color='#ddd',lw=.6,zorder=0)
    ax=fig.add_subplot(gs[2,col]);counts,edges=np.histogram(allph,bins=np.arange(0,361,30))
    ax.bar(edges[:-1]+15,counts/64,width=27,color=color,alpha=.8)
    ax.set(xlim=(0,360),ylim=(0,.38),xticks=[0,90,180,270,360],xlabel='周期内相位 / °',ylabel='事件比例')
    ax.set_title(f'N = 64，平均率 66.7 次/s，R = {stats(allph)["R"]:.3f}',fontsize=13)
fig.text(.5,.013,'每条件 8 试次 × 120 ms；每试次 8 事件。全部为确定性的教学事件，非神经记录。',ha='center',fontsize=12)
fig.subplots_adjust(top=.94,bottom=.1)
save(fig,'01-timing-and-histogram')

fig,axes=plt.subplots(2,2,figsize=(11,9),subplot_kw={'projection':'polar'})
for ax,(name,data,color,title) in zip(axes.flat,[
    ('concentrated',concentrated,BLUE,'（a）集中在约 90°'),
    ('delayed',delayed,GREEN,'（b）固定延迟：整体转过 36°'),
    ('uniform',dispersed,GRAY,'（c）均匀覆盖一个周期'),
    ('antipodal',antipodal,ORANGE,'（d）相反两峰：一阶向量相消')]):
    angles=np.deg2rad(np.unique(data));ax.scatter(angles,np.ones(len(angles)),s=65,color=color,zorder=3)
    mean=np.mean(np.exp(1j*np.deg2rad(data)))
    if abs(mean)>1e-12:ax.annotate('',xy=(np.angle(mean),abs(mean)),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':3,'color':color})
    ax.set_ylim(0,1.12);ax.set_yticks([.5,1]);ax.set_yticklabels([])
    ax.set_thetagrids([0,90,180,270]);ax.set_title(title,pad=25,fontsize=14)
    s=stats(data);ax.text(.5,-.16,f'N = 64，R = {s["R"]:.3f}，R2 = {s["R2"]:.3f}',ha='center',transform=ax.transAxes,fontsize=13)
fig.text(.5,.017,'同一角度的重复事件以一个点表示；箭头是事件平均向量。无稳定一阶方向时不画箭头。',ha='center',fontsize=11)
fig.subplots_adjust(hspace=.65,wspace=.3,bottom=.1,top=.9)
save(fig,'02-phase-vectors')

fig,axes=plt.subplots(1,2,figsize=(13,5))
freq=np.geomspace(100,4000,400)
for sigma,color,style in zip([50e-6,100e-6,200e-6],[GREEN,BLUE,ORANGE],['-', '--', ':']):
    r=np.exp(-.5*(2*np.pi*freq*sigma)**2)
    axes[0].semilogx(freq,r,color=color,lw=2.6,ls=style,label=rf'$\sigma_t$ = {sigma*1e6:.0f} μs')
axes[0].set(xlim=(100,4000),ylim=(0,1.05),xlabel='参照频率 / Hz',ylabel='理论总体 R',title='（a）固定时间抖动：高频下相位更分散')
axes[0].set_xticks([100,500,1000,2000,4000],['100','500','1000','2000','4000']);axes[0].legend(loc='lower left',fontsize=11)
axes[0].grid(alpha=.18)
delay=np.linspace(0,2,160)
axes[1].plot(delay,36*delay,color=BLUE,lw=2.6,label='相位偏移 Δφ / °')
axes[1].set(xlim=(0,2),ylim=(0,85),xlabel='固定延迟 / ms',ylabel='相位偏移 / °',title='（b）100 Hz：固定延迟改变方向')
axr=axes[1].twinx();axr.plot(delay,np.ones_like(delay),color=GREEN,lw=2.3,ls='--');axr.set(ylim=(0,1.3),ylabel='R（原始事件完全锁定）')
axes[1].annotate('1 ms → 36°',xy=(1,36),xytext=(.2,62),arrowprops={'arrowstyle':'->','color':BLUE},fontsize=13)
axes[1].text(.06,.08,'固定延迟不使分布变宽：R 保持 1',transform=axes[1].transAxes,color=GREEN,fontsize=11)
fig.text(.5,.015,'独立零均值高斯时间抖动的解析计算；忽略膜、突触、不应期与选择偏差，不是生理截止曲线。',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.055,1,1));save(fig,'03-delay-and-jitter')

fig,axes=plt.subplots(2,1,figsize=(12,6),sharex=True)
t=np.arange(0,.03,1/100000);envelope=(1+.8*np.cos(2*np.pi*100*t))/1.8
axes[0].plot(t*1000,np.cos(2*np.pi*100*t),color=BLUE,lw=2)
axes[0].set(ylim=(-1.2,1.35),ylabel='相对声压',title='（a）100 Hz 纯音：参照可以是载波周期（10 ms）')
axes[1].plot(t*1000,envelope*np.sin(2*np.pi*4000*t),color=GRAY,lw=.75)
axes[1].plot(t*1000,envelope,color=ORANGE,lw=2.3,label='100 Hz 幅度包络')
axes[1].plot(t*1000,-envelope,color=ORANGE,lw=2.3,ls='--')
axes[1].set(xlim=(0,30),ylim=(-1.2,1.35),xlabel='时间 / ms',ylabel='相对声压',title='（b）4000 Hz 载波 + 100 Hz 调幅：两个不同参照')
axes[1].legend(loc='upper right',fontsize=11)
for ax in axes:ax.grid(alpha=.14)
fig.text(.5,.012,'调制深度 m = 0.8，采样率 100 kHz；仅示出声学刺激，没有画神经响应或推断锁相能力。',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.05,1,1));save(fig,'04-carrier-and-envelope')

parameters={'generator':'scripts/generate-phase-locking.py','data_type':'original deterministic teaching events and analytic calculations; not empirical',
    'numpy_version':np.__version__,'matplotlib_version':matplotlib.__version__,
    'raster':{'frequency_hz':100,'window_ms':120,'trials':8,'events_per_trial':8,'used_cycles':used_cycles.tolist(),'center_phase_degrees':center.tolist(),'uniform_phase_degrees':uniform.tolist(),'event_rate_per_second':8/.12},
    'examples':examples,'jitter':{'distribution':'independent zero-mean Gaussian','sigma_seconds':[50e-6,100e-6,200e-6],'formula':'R=exp(-0.5*(2*pi*f*sigma_t)**2)','frequency_hz':[100,4000],'at_sigma_100us':{str(f):float(np.exp(-.5*(2*np.pi*f*100e-6)**2)) for f in [100,1000,4000]}},
    'stimulus':{'fs_hz':100000,'duration_seconds':.03,'carrier_hz':4000,'modulation_hz':100,'depth':.8,'normalizer':1.8},
    'scope':'No complete auditory model was run. No cutoff, normal range, patient data, or device settings are predicted.'}
(RESEARCH/'figure-parameters.json').write_text(json.dumps(parameters,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
np.savez_compressed(OUT/'teaching-events.npz',concentrated=concentrated,uniform=dispersed,delayed=delayed,antipodal=antipodal,used_cycles=used_cycles)
print(json.dumps({'figures':4,'examples':examples,'jitter':parameters['jitter']['at_sigma_100us']},ensure_ascii=False))
