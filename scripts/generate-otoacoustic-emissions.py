"""Reproducible teaching figures and attributed published measurements; no complete auditory model."""
from pathlib import Path
import json,shutil
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
ROOT=Path(__file__).resolve().parents[1]; local=ROOT/'docs/drafts/assets'
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':10,'svg.fonttype':'path','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False,'savefig.dpi':160})
C=['#215e83','#b75637','#457665','#8264a0']; rng=np.random.default_rng(20261009);manifest=[]
def panel(n=1,h=3.5,w=9):
 f,a=plt.subplots(1,n,figsize=(w,h),layout='constrained');return f,np.atleast_1d(a)
def save(f,s,n,params):
 d=ROOT/'public/figures'/s;d.mkdir(parents=True,exist_ok=True);l=local/s;l.mkdir(parents=True,exist_ok=True)
 for ext in ['svg','png']:
  p=d/(n+'.'+ext);f.savefig(p,bbox_inches='tight',facecolor='white')
  if ext=='svg':p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
  shutil.copy2(p,l/p.name)
 plt.close(f);manifest.append({'slug':s,'file':n+'.svg','source':'Original analytic or synthetic pedagogical illustration','parameters':params})
def node(ax,x,y,text):ax.text(x,y,text,ha='center',va='center',bbox={'boxstyle':'round,pad=.5','fc':'white','ec':'#8b9ba5'},fontsize=11)
def arrow(ax,x,y,u,v,color=C[0],label=None):
 ax.add_patch(FancyArrowPatch((x,y),(u,v),arrowstyle='->',mutation_scale=13,color=color,lw=1.5))
 if label:ax.text((x+u)/2,(y+v)/2+.12,label,ha='center',fontsize=9,color=color)
s='otoacoustic-emissions'
f,axs=panel(w=9.5,h=6.5);ax=axs[0]
ax.axis('off');ax.set(xlim=(0,10),ylim=(0,6.9))
ax.text(.05,6.62,'耳声发射：从刺激传入到结果判读',fontsize=15,fontweight='bold',color='#263843')
def flow_block(x,y,w,h,title,subtitle,color,edge):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.045,rounding_size=.10',fc=color,ec=edge,lw=1.4))
 ax.text(x+w/2,y+h*.65,title,ha='center',va='center',fontsize=13,fontweight='bold',color='#263843')
 ax.text(x+w/2,y+h*.27,subtitle,ha='center',va='center',fontsize=11,color='#536672')
flow_block(.3,5.12,2.6,1.1,'探头扬声器','呈现已校准刺激','#eef4f7',C[0])
flow_block(3.7,5.12,2.6,1.1,'向内声学传输','外耳 → 中耳','#eef4f7',C[0])
flow_block(.3,3.27,2.6,1.1,'探头传声器','记录耳道混合声压','#faf2ee',C[1])
flow_block(3.7,3.27,2.6,1.1,'向外声学传输','中耳 → 外耳','#faf2ee',C[1])
# One mechanical-source block joins the two acoustic paths.
ax.add_patch(FancyBboxPatch((7.1,3.27),2.6,2.95,boxstyle='round,pad=.045,rounding_size=.10',fc='#f1f6f3',ec=C[2],lw=1.5))
ax.text(8.4,5.61,'耳蜗机械源',ha='center',va='center',fontsize=13,fontweight='bold',color='#263843')
ax.text(8.4,4.82,'外毛细胞相关的\n主动机械过程',ha='center',va='center',fontsize=12,color='#536672',linespacing=1.5)
ax.text(8.4,3.87,'产生声学输出',ha='center',va='center',fontsize=11.5,color=C[2])
for x1,x2 in [(2.99,3.61),(6.39,7.01)]:arrow(ax,x1,5.67,x2,5.67,C[0])
for x1,x2 in [(7.01,6.39),(3.61,2.99)]:arrow(ax,x1,3.82,x2,3.82,C[1])
# Continue the same chain from the microphone into quality control and analysis.
flow_block(.3,1.32,2.6,1.1,'采集质量控制','刺激稳定、伪迹与噪声','#f5f7f7','#73858e')
flow_block(3.7,1.32,2.6,1.1,'发射成分提取','按类型分离刺激与响应','#f5f7f7','#73858e')
flow_block(7.1,1.32,2.6,1.1,'报告与判读','耳别、频点、响应与判据','#f1f6f3',C[2])
arrow(ax,1.6,3.18,1.6,2.51,'#647b87')
for x1,x2 in [(2.99,3.61),(6.39,7.01)]:arrow(ax,x1,1.87,x2,1.87,'#647b87')
ax.text(5,.65,'记录声压 = 刺激残余 + 耳声发射 + 噪声 + 设备误差',ha='center',fontsize=11.5,color='#263843')
ax.text(5,.15,'质量不足时，先核对探头、校准、环境与中耳状态。',ha='center',fontsize=10.5,color='#536672')
save(f,s,'oae-transfer',{'functional_block_diagram':True,'anatomical_drawing':False,'single_integrated_panel':True,'blocks':8,'path':'stimulus -> inward transmission -> cochlear source -> outward transmission -> microphone -> quality control -> emission extraction -> reporting','probe_speaker_and_microphone_distinguished':True,'separate_inward_outward_transmission_blocks':True,'single_cochlear_mechanical_source_block':True,'mixed_pressure_equation':True,'quality_control_precedes_interpretation':True,'direction_is_schematic_not_claim_of_simple_reverse_wave':True})
f,a=panel(3,w=11.5,h=3.9);fs=48000;t=np.arange(4800)/fs;x=(np.cos(2*np.pi*1000*t)+np.cos(2*np.pi*1200*t))/2;y=x+.3*x**3
freq=np.fft.rfftfreq(len(t),1/fs);specs=[2*np.abs(np.fft.rfft(z))/len(z) for z in [x,y]]
for ax,spec,title in zip(a[:2],specs,['A  双原音输入','B  非线性输出（局部频谱）']):
 sel=(freq>=500)&(freq<=1600)&(spec>1e-5)
 ax.stem(freq[sel],spec[sel],basefmt=' ',linefmt=C[0],markerfmt='o')
 ax.set(xlabel='频率 (Hz)',ylabel='分量峰值幅度（归一化）',title=title,xlim=(650,1550),ylim=(0,.68),xticks=[800,1000,1200,1400]);ax.grid(axis='y',alpha=.18)
for ax in a[:2]:
 for hz,label in [(1000,'$f_1$'),(1200,'$f_2$')]:ax.text(hz,specs[0 if ax is a[0] else 1][int(hz*.1)]+.025,label,ha='center',color=C[0])
dp_freq=np.array([800,1400]);dp_amp=specs[1][(dp_freq*.1).astype(int)]
assert np.allclose(dp_amp,.028125,atol=1e-12) and np.max(np.abs(x))<=1
a[2].stem(dp_freq,dp_amp,basefmt=' ',linefmt=C[1],markerfmt='o')
a[2].set(xlabel='频率 (Hz)',ylabel='分量峰值幅度（归一化）',title='C  组合分量放大',xlim=(650,1550),ylim=(0,.038),xticks=[800,1000,1200,1400]);a[2].grid(axis='y',alpha=.18)
for hz,label in [(800,'$2f_1-f_2$'),(1400,'$2f_2-f_1$')]:a[2].text(hz,.0305,label,ha='center',color=C[1],fontsize=9)
a[2].text(1100,.004,'纵轴范围已放大',ha='center',fontsize=9,color='#53616b')
save(f,s,'oae-distortion',{'f1_Hz':1000,'f2_Hz':1200,'fs':fs,'duration_s':.1,'model':'y=x+0.3*x^3','spectrum_quantity':'component peak amplitude, normalized digital variable','shown_frequency_range_Hz':[650,1550],'dp_peak_amplitudes':dp_amp.tolist(),'zoom_panel_separate_y_scale':True,'no_clinical_calibration':True})
f,a=panel(2,h=3.8);phase=np.linspace(0,2*np.pi,401);mag=np.abs(1+.8*np.exp(1j*phase))
a[0].plot(np.rad2deg(phase),mag,c=C[0]);a[1].plot(np.rad2deg(phase),20*np.log10(mag),c=C[1])
for ax in a:ax.set(xlabel='两个源的相位差 (°)',xticks=[0,90,180,270,360]);ax.grid(alpha=.2)
a[0].set(ylabel='总响应的相对线幅度',title='A  线幅度',ylim=(0,2));a[1].set(ylabel='相对于单位幅度的级 (dB)',title='B  幅度级',ylim=(-16,7))
for ax,values in zip(a,[mag,20*np.log10(mag)]):
 ax.plot(180,values[200],'o',c=ax.lines[0].get_color(),ms=4)
 ax.annotate(f'{values[200]:.1f}'+(' dB' if ax is a[1] else ''),xy=(180,values[200]),xytext=(210,values[200]+(3 if ax is a[1] else .3)),arrowprops={'arrowstyle':'->','color':'#657781'},fontsize=9)
save(f,s,'oae-interference',{'source_magnitudes':[1,.8],'model':'abs(1+0.8exp(i phase))','minimum_linear':float(mag.min()),'maximum_linear':float(mag.max()),'phase_grid_includes_pi':True})
f,a=panel(h=4,w=9);freq=np.array([1,1.5,2,3,4,6]);sig=np.array([-4,-5,-2,-7,-12,-8]);noise=np.array([-14,-15,-14,-16,-15,-18]);ax=a[0]
ax.plot(freq,sig,'-',c=C[0],lw=1.1);large=freq!=4
ax.plot(freq[large],sig[large],'o',c=C[0],label='假设响应级')
ax.plot(freq[~large],sig[~large],'o',mec=C[0],mfc='white',ms=7,label='差值较小的示例点')
ax.plot(freq,noise,'o--',c=C[1],label='假设噪声底',lw=1.1)
ax.annotate('',xy=(1.5,-5),xytext=(1.5,-15),arrowprops={'arrowstyle':'<->','color':'#555','shrinkA':5,'shrinkB':5})
ax.text(1.68,-10,'差值 10 dB',fontsize=10);ax.annotate('差值 3 dB',xy=(4,-12),xytext=(3.3,-5),arrowprops={'arrowstyle':'->','color':'#657781'},fontsize=9)
ax.set_xscale('log',base=2);ax.set(xlabel='第二原音频率 $f_2$ (kHz)',ylabel='声压级 (dB SPL)',ylim=(-23,5),xticks=freq,xticklabels=['1','1.5','2','3','4','6'],title='教学示例：原音频率比 $f_2/f_1 = 1.2$')
ax.grid(axis='y',alpha=.18);ax.legend(loc='lower left',fontsize=9,ncol=3)
save(f,s,'oae-noise',{'f2_frequencies_kHz':freq.tolist(),'primary_ratio':1.2,'readout_frequencies_kHz':((2/1.2-1)*freq).tolist(),'response_dB_SPL':sig.tolist(),'noise_dB_SPL':noise.tolist(),'open_point_example_f2_kHz':4,'not_pass_criteria':True})
f,a=panel(2,h=3.8);freq=np.linspace(1,4,601);ph=-2*np.pi*freq*5 # kHz * ms
# Round only the branch coordinate to avoid floating-point sign ambiguity at ±pi.
wrapped=(np.remainder(np.round(ph/np.pi,12)+1,2)-1)*np.pi
assert np.allclose(np.exp(1j*wrapped),np.exp(1j*ph),atol=1e-12)
unwrapped=np.unwrap(wrapped);unwrapped-=unwrapped[0]
# Break a plotted line at each wrap; compute the right panel from the actual samples.
breaks=np.flatnonzero(np.abs(np.diff(wrapped))>np.pi)+1
for idx in np.split(np.arange(len(freq)),breaks):a[0].plot(freq[idx],wrapped[idx],c=C[1],lw=1.3)
recovered_ms=-np.gradient(unwrapped,freq)/(2*np.pi);assert np.allclose(recovered_ms,5,atol=1e-10)
a[0].set(xlabel='响应频率 (kHz)',ylabel='相位 (rad)',title='A  相位限制在 ±π 内',ylim=(-np.pi-.3,np.pi+.3),yticks=[-np.pi,0,np.pi],yticklabels=['−π','0','π'])
a[1].plot(freq,unwrapped,c=C[0]);a[1].set(xlabel='响应频率 (kHz)',ylabel='相对展开相位 (rad)',title='B  实际展开，首点设为零')
a[1].text(1.1,-65,'斜率 = −10π rad/kHz\n恢复延迟 = 5 ms',color=C[0],fontsize=10)
for ax in a:ax.grid(alpha=.18)
save(f,s,'oae-phase-delay',{'delay_ms':5,'analytic_phase_only':True,'phase_samples':len(freq),'wrapped_plot_breaks':len(breaks),'unwrap_method':'numpy.unwrap; subtract first value','frequency_step_Hz':5,'maximum_recovery_error_ms':float(np.max(np.abs(recovered_ms-5)))})
# A licensed published measurement is retained unchanged, separate from the teaching plots.
source_record=ROOT/'docs/research/otoacoustic-emissions-2026-10-09/oae-figure-source.json'
if source_record.is_file():manifest.append(json.loads(source_record.read_text(encoding='utf-8')))
published_records=ROOT/'docs/research/otoacoustic-emissions-2026-10-09/oae-published-figures.json'
if published_records.is_file():manifest.extend(json.loads(published_records.read_text(encoding='utf-8')))

report=ROOT/'docs/research/otoacoustic-emissions-2026-10-09/figure-manifest.json'
report.parent.mkdir(parents=True,exist_ok=True)
report.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Generated 5 OAE teaching figures; retained 3 licensed source figures.')
