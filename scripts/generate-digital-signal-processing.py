"""Original DSP teaching figures, derived from fully specified numerical models."""
from pathlib import Path
import sys,importlib.util,json
sys.dont_write_bytecode=True
import numpy as np
from scipy import signal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyBboxPatch
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('dsp',ROOT/'public/code/digital-signal-processing/experiments.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures/digital-signal-processing';PRE=ROOT/'artifacts/digital-signal-processing/figures';REC=ROOT/'docs/research/digital-signal-processing-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'digital-signal-processing','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创数字信号处理教学图 · 指定理想模型，非生理或器件实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2)
    p=FIG/(name+'.svg');fig.savefig(p,metadata={'Date':None},facecolor='white')
    p.write_text('\n'.join(l.rstrip() for l in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
def db(x):return 20*np.log10(np.maximum(abs(x),1e-7))
def stem(a,x,y,col=B,label=None):
    markers,lines,base=a.stem(x,y,basefmt=' ',label=label)
    plt.setp(markers,color=col,markersize=4);plt.setp(lines,color=col,linewidth=1.3)

# 1 Workflow with explicit numerical metadata.
fig,a=plt.subplots(figsize=(14,5.5));a.set(xlim=(0,14),ylim=(0,5));a.axis('off')
for i,(title,txt,col) in enumerate([
    ('定义输入','fs=16 kHz\n样值与单位\n保留／抑制的频带',B),
    ('分块与状态','B=64样本\n过去输入与内部状态\n记录起点才初始化',G),
    ('选择算法','直接卷积／FFT\nSOS／STFT／多相\n精度与运算预算',P),
    ('验证输出','增益、相位与尾部\n整段与分块一致性\n独立数据与端到端延迟',R)]):
    x=.2+i*3.5
    a.add_patch(FancyBboxPatch((x,1.45),3.05,2.3,boxstyle='round,pad=.05',fc=col+'12',ec=col,lw=1.5))
    a.text(x+1.525,3.28,title,ha='center',fontsize=15,color=col,fontweight='bold')
    a.text(x+1.525,2.35,txt,ha='center',va='center',linespacing=1.9)
    if i<3:a.annotate('',xy=(x+3.45,2.6),xytext=(x+3.08,2.6),arrowprops={'arrowstyle':'->','color':M,'lw':2})
a.text(7,.65,'模拟抗混叠 → ADC → 数字处理 → DAC与重建滤波 → 声学输出',ha='center',fontsize=14,color=M)
fig.suptitle('数字信号处理：从任务规格到可复核的实现',fontsize=18,fontweight='bold');save(fig,'processing-chain')
# 2 Window leakage, amplitude normalization.
n,x,windows=m.spectral_demo();fs=m.FS;fig,ax=plt.subplots(1,2,figsize=(14,5.5))
for (name,w),col in zip(windows.items(),[B,R]):
    ax[0].plot(n,w,color=col,lw=2,label=name)
    f=np.fft.rfftfreq(8192,1/fs);v=2*abs(np.fft.rfft(w*x,8192))/w.sum()
    ax[1].plot(f/1000,db(v),color=col,lw=1.6,label=name)
ax[0].set(xlabel='样本索引 n',ylabel='窗权重',title='（a）256点窗：相干增益1与0.5');ax[0].legend()
ax[1].set(xlim=(1,3.1),ylim=(-100,3),xlabel='频率 / kHz',ylabel='幅度 / dB，参考1',title='（b）同一2050 Hz余弦，补零细画');ax[1].legend()
fig.suptitle('窗函数：增益、主瓣与旁瓣一起改变',fontsize=18,fontweight='bold');save(fig,'spectral-window')
# 3 FIR specifications.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));summary=m.summary()
for ((name,h),row,col) in zip(m.fir_designs(),summary['FIR'],[B,G,R]):
    f,H=signal.freqz(h,worN=65536,fs=m.FS)
    ax[0].plot(f/1000,db(H),color=col,label=name,lw=1.5)
    ax[1].scatter(row['delay_ms'],row['stopband_attenuation_dB'],color=col,s=60)
    ax[1].annotate(name,(row['delay_ms'],row['stopband_attenuation_dB']),xytext=(9,0),textcoords='offset points',va='center',fontsize=10)
ax[0].axvspan(0,2.5,color=G,alpha=.08);ax[0].axvspan(3.5,8,color=R,alpha=.07)
ax[0].set(xlim=(0,8),ylim=(-115,5),xlabel='频率 / kHz',ylabel='幅度增益 / dB',title='（a）fc=3 kHz：半幅度附近');ax[0].legend(fontsize=9)
ax[1].set(xlim=(1.6,5.7),ylim=(35,100),xlabel='线性相位群延迟 / ms',ylabel='最差阻带衰减 / dB',title='（b）指定阻带：3.5—8 kHz');ax[1].grid(alpha=.2)
fig.suptitle('FIR设计：同一个截止参数，不同的误差与代价',fontsize=18,fontweight='bold');save(fig,'fir-design')
# 4 IIR single vs double pass; causal poles only.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));sos=m.iir_design();f,H=signal.sosfreqz(sos,worN=8192,fs=m.FS)
ax[0].plot(f/1000,db(H),color=B,label='单次 |H|',lw=2);ax[0].plot(f/1000,db(abs(H)**2),color=R,label='双向内部 |H|²',lw=2)
ax[0].scatter([3,3],[-10*np.log10(2),-20*np.log10(2)],color=[B,R],zorder=4)
ax[0].set(xlim=(0,8),ylim=(-100,3),xlabel='频率 / kHz',ylabel='幅度增益 / dB',title='（a）六阶Butterworth，fs=16 kHz');ax[0].legend()
z,p,k=signal.sos2zpk(sos);ax[1].add_patch(Circle((0,0),1,fill=False,color=M,ls='--'));ax[1].scatter(p.real,p.imag,marker='x',s=70,color=B,label='单次因果系统极点')
ax[1].axhline(0,color=M,lw=.6);ax[1].axvline(0,color=M,lw=.6);ax[1].set(aspect='equal',xlim=(-1.2,1.2),ylim=(-1.2,1.2),xlabel='Re z',ylabel='Im z',title='（b）三节SOS，极点严格在单位圆内');ax[1].legend(fontsize=9)
fig.suptitle('离线双向滤波：幅度平方，需要未来样本',fontsize=18,fontweight='bold');save(fig,'iir-offline')
# 5 OLA with M>B and partial final input block.
rng=np.random.default_rng(44);x=rng.normal(0,.3,257);h=m.fir_designs()[1][1];direct=np.convolve(x,h);ola=m.overlap_add(x,h,64)
fig,ax=plt.subplots(2,1,figsize=(14,5.5),gridspec_kw={'height_ratios':[2,1]})
for q in range(0,len(x),64):ax[0].axvspan(q,min(q+64,len(x)),color=[B,G,P,R][(q//64)%4],alpha=.08)
ax[0].plot(np.arange(len(direct)),direct,color=B,lw=2,label='直接完整卷积');ax[0].plot(ola,color=R,ls='--',lw=1,label='FFT重叠相加')
ax[0].axvline(256,color=M,ls=':',label='最后输入样本');ax[0].set(ylabel='无单位输出',title='（a）B=64，M=129，NFFT=256，尾部累加到索引384');ax[0].legend(ncol=3,fontsize=9)
ax[1].plot(ola-direct,color=P,lw=1);ax[1].set(xlabel='输出样本索引 n',ylabel='浮点差值',title='（b）重叠相加 − 直接卷积');ax[1].ticklabel_format(axis='y',style='sci',scilimits=(0,0))
fig.suptitle('分块卷积保留跨块记忆与最后尾部',fontsize=18,fontweight='bold');save(fig,'block-convolution')
# 6 STFT WOLA.
sd=m.stft_demo();x,y,den,X,t,f,w,hop,nfft=[sd[k] for k in ['x','y','den','X','times','frequencies','window','hop','nfft']];fig,ax=plt.subplots(1,2,figsize=(14,5.5))
image=db(abs(X.T)/abs(X).max());mesh=ax[0].pcolormesh(t*1000,f/1000,image,shading='auto',vmin=-80,vmax=0,cmap='magma',rasterized=True)
ax[0].set(xlim=(0,len(x)/m.FS*1000),ylim=(0,5),xlabel='帧中心时间 / ms',ylabel='频率 / kHz',title='（a）1 kHz → 3 kHz，零补边');fig.colorbar(mesh,ax=ax[0],label='相对全图最大谱幅度 / dB')
ax[1].plot(np.arange(len(x))/m.FS*1000,y-x,color=B,lw=.8);ax[1].set(xlabel='原记录时间 / ms',ylabel='重建 − 原信号',title='（b）同窗合成并除以平方窗重叠和')
ax[1].ticklabel_format(axis='y',style='sci',scilimits=(0,0));ax[1].text(.5,.91,'原记录内归一化分母 ≈ 1.5',transform=ax[1].transAxes,ha='center',fontsize=11)
fig.suptitle('STFT：明确窗、步长、FFT与重建归一化',fontsize=18,fontweight='bold');save(fig,'stft-reconstruction')
# 7 Rate conversion.
fs,x,h,naive,filtered=m.multirate_demo();fig,ax=plt.subplots(1,2,figsize=(14,5.5));f,H=signal.freqz(h,worN=8192,fs=fs)
ax[0].plot(f/1000,db(H),color=G,lw=2);ax[0].axvline(8,color=R,ls='--',label='输出Nyquist 8 kHz');ax[0].set(xlim=(0,16),ylim=(-125,5),xlabel='输入物理频率 / kHz',ylabel='滤波器增益 / dB',title='（a）129点Kaiser，fc=7 kHz');ax[0].legend()
for xx,col,label in [(naive,B,'直接抽取：13 kHz → 3 kHz'),(filtered,R,'先低通再抽取')]:
    seg=xx[1024:3072];f=np.fft.rfftfreq(len(seg),1/16000);sel=(f>0)&(f<8000)
    ax[1].plot(f[sel]/1000,db(2*abs(np.fft.rfft(seg))[sel]/len(seg)),color=col,lw=1.5,label=label)
ax[1].set(xlim=(0,8),ylim=(-130,3),xlabel='输出物理频率 / kHz',ylabel='幅度 / dB，参考1',title='（b）输出中央2048点，fs=16 kHz');ax[1].legend(fontsize=9)
fig.suptitle('32 kHz降为16 kHz：先滤波，避免高频折入',fontsize=18,fontweight='bold');save(fig,'multirate-alias')
# 8 Error structure.
x,q,e,r=m.quantization_demo();n=np.arange(len(x));fig,ax=plt.subplots(1,2,figsize=(14,5.5))
ax[0].plot(n[:96],x[:96],color=B,label='输入，幅度0.1',lw=1.8);ax[0].step(n[:96],q[:96],where='mid',color=R,label='量化输出，Δ=0.25',lw=1.8)
ax[0].set(xlabel='样本索引 n',ylabel='无单位幅度',title='（a）八级中升型，无输出级0');ax[0].legend()
stem(ax[1],n[:97],r[:97],P);ax[1].set(xlabel='延迟 / 样本',ylabel='有偏自相关 / 零延迟值',title='（b）512点误差的周期结构，非白噪声')
fig.suptitle('低幅周期信号：不能自动把量化误差当白噪声',fontsize=18,fontweight='bold');save(fig,'quantization-error')
# 9 Coefficient rounding (not full fixed-point arithmetic).
a,aq,imp,impq,step,stepq=m.coefficient_demo();n=np.arange(len(imp));fig,ax=plt.subplots(1,2,figsize=(14,5.5))
for axy,orig,rounded,title in [(ax[0],imp,impq,'（a）单位样本输入：aⁿ'),(ax[1],step,stepq,'（b）单位阶跃输入：累积响应')]:
    axy.plot(n,orig,color=B,label='a=0.9997',lw=2);axy.plot(n,rounded,color=R,label='舍入为a=1',lw=2);axy.set(xlabel='样本索引 n',ylabel='无单位输出',title=title);axy.legend()
fig.suptitle('只量化一个系数，也可能改变BIBO稳定性',fontsize=18,fontweight='bold');save(fig,'coefficient-rounding')
# 10 Independent frozen validation.
d=m.adaptive_demo();fig,ax=plt.subplots(1,2,figsize=(14,5.5))
stem(ax[0],np.arange(16)-.08,d['h'],B,'指定真值');stem(ax[0],np.arange(16)+.08,d['w'],R,'训练后冻结系数')
ax[0].set(xlabel='抽头索引',ylabel='系数',title='（a）16抽头，NLMS μ=0.2');ax[0].legend()
for key,col,label,ls in [('validation_observed',M,'带噪观测',':'),('validation_clean',B,'无噪声目标','-'),('prediction',R,'冻结模型预测','--')]:
    ax[1].plot(np.arange(80),d[key][:80],color=col,label=label,ls=ls,lw=1.5)
ax[1].set(xlabel='独立验证样本索引',ylabel='无单位输出',title='（b）仅展示验证记录前80点');ax[1].legend(fontsize=9)
fig.suptitle('自适应系统辨识：不把训练误差当推广证据',fontsize=18,fontweight='bold');save(fig,'adaptive-validation')
(REC/'calculations.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Characteristic native vector sketch for the single foundation-course card.
sketch=ROOT/'public/figures/foundation-courses/digital-signal-processing.svg'
sketch.write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="180" viewBox="0 0 320 180" role="img" aria-labelledby="t d">
<title id="t">数字信号处理简笔画</title><desc id="d">离散样本经过三个滤波抽头，再以频率响应表示其作用。</desc>
<rect width="320" height="180" fill="#f3f1f8"/><g fill="none" stroke="#79639d" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
<path d="M20 110h73M28 110V85m14 25V61m14 49V77m14 33v14m14-14v25"/><path d="M102 91h21m-6-5 6 5-6 5"/>
<rect x="132" y="51" width="56" height="80" rx="8"/><path d="M142 108h36m-30 0V87m12 21V67m12 41V94"/>
<path d="M197 91h21m-6-5 6 5-6 5M228 125h73M231 124V59m4 12h23q12 0 15 24t22 22"/>
</g><g fill="#79639d"><circle cx="28" cy="85" r="3"/><circle cx="42" cy="61" r="3"/><circle cx="56" cy="77" r="3"/><circle cx="70" cy="124" r="3"/><circle cx="84" cy="135" r="3"/><circle cx="148" cy="87" r="3"/><circle cx="160" cy="67" r="3"/><circle cx="172" cy="94" r="3"/></g>
<g font-family="sans-serif" font-size="12" fill="#61727d" text-anchor="middle"><text x="56" y="157">x[n]</text><text x="160" y="157">h[n]</text><text x="263" y="157">H(f)</text></g></svg>
''',encoding='utf-8')
