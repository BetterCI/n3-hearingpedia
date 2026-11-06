"""Reproduce the Hearingpedia CARFAC figures with pinned upstream NumPy code.

Requires numpy==2.2.6 and matplotlib==3.10.7. Run from any directory. The third-party source
is downloaded unchanged into artifacts/, retaining its Apache-2.0 header.
Figures are model computations, not experimental human data.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import urllib.request

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
COMMIT = 'a9fba19ac76c6b8052d1d4a2973f91450fb4d1d8'
URL = f'https://raw.githubusercontent.com/google/carfac/{COMMIT}/python/src/carfac/np/carfac.py'
CACHE = ROOT / 'artifacts/carfac-upstream/python/src/carfac/np/carfac.py'
if not CACHE.exists():
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_bytes(urllib.request.urlopen(URL, timeout=45).read())
assert hashlib.sha256(CACHE.read_bytes()).hexdigest() == '40efc645f5fa4e661116a5000c7181360b09f5efc81a0ac7908b55fc5abe9861', 'Upstream source checksum mismatch'
spec = importlib.util.spec_from_file_location('pinned_carfac', CACHE)
carfac = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = carfac
spec.loader.exec_module(carfac)
OUT = ROOT / 'public/figures/carfac'
OUT.mkdir(parents=True, exist_ok=True)
DATA = ROOT / 'docs/research/carfac-2026-11-06'
DATA.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.sans-serif': ['Microsoft YaHei', 'DejaVu Sans'], 'axes.unicode_minus': False,
                     'svg.fonttype': 'none', 'font.size': 12, 'axes.spines.top': False,
                     'axes.spines.right': False, 'figure.facecolor': 'white'})
BLUE, ORANGE, PURPLE = '#276b99', '#ca7130', '#7560a2'
FS = 22050
T = np.arange(round(.12 * FS)) / FS
FREQ = 1000
RAMP = np.minimum(1, np.minimum(T / .005, (.12-T) / .005))

def design(style='two_cap'):
    return carfac.carfac_init(carfac.design_carfac(n_ears=1, fs=FS, ihc_style=style))

def tone(level):
    return 10**(level/20) * np.sin(2*np.pi*FREQ*T) * RAMP

def save(fig, name):
    fig.savefig(OUT / (name+'.svg'), bbox_inches=None)
    svg_path = OUT / (name+'.svg')
    svg_text = svg_path.read_text(encoding='utf-8').replace('width="1008pt" height="360pt"', 'width="1400" height="500"')
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_text.splitlines())+'\n', encoding='utf-8')
    fig.savefig(OUT / (name+'.png'), dpi=140)
    plt.close(fig)

def db(x):
    return 20*np.log10(np.maximum(x, 1e-15))

# An original block diagram; positions show signal flow, not anatomical distance.
fig, ax = plt.subplots(figsize=(14, 5))
ax.set(xlim=(0, 14), ylim=(0, 5)); ax.axis('off')
blocks = [(0.2, '声音输入', '数字幅度与采样率'), (3.0, 'CAR 级联', '非对称谐振器＋快非线性'),
          (6.2, 'IHC', '检测与动态状态'), (9.4, 'NAP', '连续活动表征')]
for x, title, sub in blocks:
    ax.add_patch(FancyBboxPatch((x, 2.5), 2.5, 1.1, boxstyle='round,pad=.08', fc='#f2f5fb', ec=BLUE))
    ax.text(x+1.25, 3.18, title, ha='center', weight='bold', color=BLUE)
    ax.text(x+1.25, 2.77, sub, ha='center', fontsize=10)
for x1, x2 in [(2.7, 2.9), (5.5, 6.1), (8.7, 9.3)]:
    ax.annotate('', (x2,3.05),(x1,3.05), arrowprops={'arrowstyle':'->','color':BLUE})
ax.text(5.75, 3.9, 'BM：IHC 前的滤波输出', ha='center', color=BLUE)
ax.annotate('', (5.6,3.6),(5.6,3.85), arrowprops={'arrowstyle':'->','color':BLUE})
ax.add_patch(FancyBboxPatch((6.2,.5),2.5,1.05,boxstyle='round,pad=.08',fc='#fff5e9',ec=ORANGE))
ax.text(7.45,1.13,'AGC 多时间尺度反馈',ha='center',color=ORANGE)
ax.text(7.45,.77,'随时间与邻近通道平滑',ha='center',fontsize=10)
ax.plot([10.65,10.65,8.8],[2.4,1.05,1.05],color=ORANGE)
ax.annotate('',(8.75,1.05),(8.95,1.05),arrowprops={'arrowstyle':'->','color':ORANGE})
ax.plot([6.1,4.25,4.25],[1.05,1.05,2.2],color=ORANGE)
ax.annotate('',(4.25,2.4),(4.25,2.15),arrowprops={'arrowstyle':'->','color':ORANGE})
ax.text(7,4.6,'CARFAC：前向变换与反馈控制',ha='center',fontsize=18,weight='bold')
fig.subplots_adjust(left=.02,right=.98,top=.98,bottom=.02)
save(fig,'01-processing-chain')

levels = np.array([-80, -65, -50, -35, -20], dtype=float)
profiles=[]; output=[]
for level in levels:
    cf=design(); nap,cf,bm,*_=carfac.run_segment(cf,tone(level))
    freqs=cf.pole_freqs
    rms=np.sqrt(np.mean(bm[(T>=.07)&(T<.11),:,0]**2,axis=0))
    profiles.append(rms)
    idx=int(np.argmin(abs(freqs-FREQ)))
    output.append(float(rms[idx]))
profiles=np.array(profiles)
fig, axes=plt.subplots(1,2,figsize=(14,5))
for level, profile, ls in zip(levels, profiles, ['-', '--', '-.', ':', '-']):
    axes[0].semilogx(freqs,db(profile),label=f'{level:g} dB',linestyle=ls)
axes[0].set(xlim=(150,8000),xlabel='通道极点频率（Hz）',ylabel='BM 稳态 RMS 级（dB re 1）',title='（a）同一 1 kHz 纯音，不同输入峰值级')
axes[0].legend(fontsize=10);axes[0].grid(alpha=.15)
axes[1].plot(levels, db(output),'o-',color=BLUE,label=f'最邻近通道：{freqs[idx]:.1f} Hz')
axes[1].plot(levels, db(output)[0]+levels-levels[0],'--',color=ORANGE,label='经过首点的斜率 1 参照')
axes[1].set(xlabel='输入峰值级（dB re 1）',ylabel='BM 稳态 RMS 级（dB re 1）',title='（b）固定通道的输入—输出关系')
axes[1].legend(fontsize=10);axes[1].grid(alpha=.15)
fig.tight_layout(pad=2)
save(fig,'02-level-response')

# Isolate IHC processing: same stored BM waveform is supplied to both IHC types.
cf=design(); _,cf,bm,*_=carfac.run_segment(cf,tone(-40))
bm_shared=bm[:,idx,0]
ihc_outputs={}
for style in ['one_cap','two_cap']:
    cf_i=design(style); coeff=cf_i.ears[0].ihc_coeffs; state=cf_i.ears[0].ihc_state
    values=[]
    for b in bm_shared:
        ihc_out,state,_=carfac.ihc_step(np.full(cf_i.n_ch,b),coeff,state)
        values.append(float(ihc_out[idx]))
    ihc_outputs[style]=np.array(values)
fig,axes=plt.subplots(1,2,figsize=(14,5))
for style,color in [('one_cap',ORANGE),('two_cap',BLUE)]:
    axes[0].plot(T*1000,ihc_outputs[style],label=style,color=color,lw=1)
axes[0].set(xlim=(70,76),ylim=(-1.3,3.8),xlabel='时间（ms）',ylabel='IHC 输出（模型单位）',title='（a）相同 BM 输入下的 IHC 稳态输出')
axes[0].legend();axes[0].grid(alpha=.15)
f=np.geomspace(50,10000,400)
for tau,color,label in [(80e-6,ORANGE,'one_cap：80 μs × 2'),(200e-6,BLUE,'two_cap：200 μs 与 80 μs')]:
    h=1/np.sqrt((1+(2*np.pi*f*tau)**2)*(1+(2*np.pi*f*80e-6)**2))
    axes[1].semilogx(f,db(h),color=color,label=label)
axes[1].set(xlabel='调制／小信号频率（Hz）',ylabel='连续时间低通近似幅度（dB）',title='（b）仅比较两个平滑环节的解析近似')
axes[1].legend(fontsize=10);axes[1].grid(alpha=.15)
fig.tight_layout(pad=2);save(fig,'03-ihc-comparison')

x=tone(-35);cut=len(x)//2
full=carfac.run_segment(design(),x)[0]
first,cf,*_=carfac.run_segment(design(),x[:cut])
second,cf,*_=carfac.run_segment(cf,x[cut:])
joined=np.concatenate([first,second])
reset=np.concatenate([first,carfac.run_segment(design(),x[cut:])[0]])
np.testing.assert_allclose(full,joined,rtol=0,atol=1e-12)
fig,axes=plt.subplots(1,2,figsize=(14,5))
for data,label,color,ls in [(full,'整段',BLUE,'-'),(joined,'分块保留状态',PURPLE,'--'),(reset,'边界重新初始化',ORANGE,':')]:
    axes[0].plot(T*1000,data[:,idx,0],label=label,color=color,ls=ls,lw=1)
axes[0].axvline(1000*T[cut],color='#777',lw=1)
axes[0].set(xlim=(58,66),xlabel='时间（ms）',ylabel='NAP（模型单位）',title='（a）分块边界附近的通道输出')
axes[0].legend(fontsize=10);axes[0].grid(alpha=.15)
axes[1].plot(T*1000,np.max(abs(joined-full),axis=(1,2)),label='保留状态：全通道最大绝对误差',color=PURPLE)
axes[1].plot(T*1000,np.max(abs(reset-full),axis=(1,2)),label='重置状态：全通道最大绝对误差',color=ORANGE)
axes[1].set(xlabel='时间（ms）',ylabel='与整段输出的差（模型单位）',title='（b）相同刺激，分块策略改变输出')
axes[1].legend(fontsize=10);axes[1].grid(alpha=.15)
fig.tight_layout(pad=2);save(fig,'04-state-continuity')
report={'upstream_commit':COMMIT,'source_url':URL,'source_sha256':hashlib.sha256(CACHE.read_bytes()).hexdigest(),
 'numpy':np.__version__,'matplotlib':matplotlib.__version__,'sample_rate_hz':FS,'duration_s':.12,'tone_hz':FREQ,'ramp_s':.005,
 'input_peak_levels_db_re_1':levels.tolist(),'window_s':[.07,.11],'ihc_style':'two_cap','use_delay_buffer':False,
 'n_channels':cf.n_ch,'channel_index_zero_based':idx,'channel_pole_hz':float(freqs[idx]),
 'output_bm_rms':output,'local_growth_slopes':(np.diff(db(output))/np.diff(levels)).tolist(),
 'preserved_state_max_absolute_error':float(np.max(abs(joined-full))),
 'reset_state_max_absolute_error':float(np.max(abs(reset-full))),
 'all_outputs_finite':bool(np.isfinite(profiles).all() and np.isfinite(full).all()),
 'scope':'Actual pinned NumPy CARFAC with v2 two_cap settings; figure 3b is an independent continuous-time lowpass approximation; no physical SPL calibration, human measurements, or clinical inference.'}
assert report['all_outputs_finite']
(DATA/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
