"""Original mechanical and acoustic figures with explicit units and conventions."""
from pathlib import Path
import importlib.util,sys,json
sys.dont_write_bytecode=True
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Arc
ROOT=Path(__file__).resolve().parents[1];spec=importlib.util.spec_from_file_location('va',ROOT/'public/code/vibrations-and-acoustics/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures/vibrations-and-acoustics';PRE=ROOT/'artifacts/vibrations-and-acoustics/figures';REC=ROOT/'docs/research/vibrations-and-acoustics-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'vibrations-acoustics-course','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创振动与声学教学图 · 指定理想模型，非器件/房间/听者实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2);path=FIG/(name+'.svg');fig.savefig(path,metadata={'Date':None},facecolor='white');path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8');fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
# 1 Free vibration and physical energy, same initial conditions for every damping ratio.
fig,axes=plt.subplots(1,2,figsize=(14,5.5))
for zeta,col in [(.05,B),(.3,G),(1,R),(1.5,P)]:
    t,q,v,E=m.free_vibration(zeta);axes[0].plot(t,q*1000,color=col,label=f'ζ={zeta:g}');axes[1].plot(t,E*1e6,color=col,label=f'ζ={zeta:g}')
axes[0].set(xlabel='时间 / s',ylabel='位移 / mm',title='（a）m=0.02 kg，k=80 N/m，q₀=1 mm，v₀=0');axes[1].set(xlabel='时间 / s',ylabel='动能+弹性势能 / μJ',title='（b）E′=−b v²；此处只有黏性阻尼');axes[0].legend(fontsize=10);axes[1].legend(fontsize=10)
fig.suptitle('自由振动：是否往复与能量怎样衰减是两个观察量',fontsize=18,fontweight='bold');save(fig,'free-vibration-energy')
# 2 Constant force, displacement response; define Q and velocity bandwidth in text.
r=np.geomspace(.1,3,1000);fig,axes=plt.subplots(1,2,figsize=(14,5.5))
for zeta,col in [(.05,B),(.2,G),(.8,R)]:
    H=m.mechanical_response(r*m.OMEGA_N,zeta);axes[0].semilogx(r,m.STIFFNESS*abs(H),color=col,label=f'ζ={zeta:g}');axes[1].semilogx(r,-np.angle(H)*180/np.pi,color=col,label=f'ζ={zeta:g}')
for ax in axes:ax.axvline(1,color=M,ls=':',lw=1);ax.set_xlabel('频率比 ω/ωₙ')
axes[0].set(ylabel='位移幅度 / 静态幅度 F₀/k',title='（a）固定驱动力幅度；位移峰不总在ωₙ');axes[1].set(ylabel='位移相对力的滞后 / °',title='（b）ω=ωₙ时滞后90°');axes[0].legend();axes[1].legend()
fig.suptitle('共振必须说明输入与输出：位移、速度和功率的峰不同',fontsize=18,fontweight='bold');save(fig,'resonance-response')
# 3 Exact two-DOF model, modal equality tested separately.
mass,stiffness,damping,values,modes=m.modal_model();fig,axes=plt.subplots(1,2,figsize=(14,5.5))
for i,col in enumerate([B,P]):
    shape=modes[:,i]/np.max(abs(modes[:,i]));axes[0].plot([1,2],shape,'o-',color=col,lw=2,ms=8,label=f'第{i+1}模态 {np.sqrt(values[i])/(2*np.pi):.3f} Hz')
axes[0].axhline(0,color=M,lw=.7);axes[0].set(xticks=[1,2],xticklabels=['质量1：0.02 kg','质量2：0.03 kg'],ylabel='模态形状（每列最大绝对值归一）',title='（a）相对形状，不是实际位移');axes[0].legend(fontsize=10)
freq=np.linspace(5,22,2001);direct,modal=m.modal_response(freq)
for i,col in enumerate([B,P]):axes[1].semilogy(freq,abs(direct[:,i])*1000,color=col,label=f'|q{i+1}/F₁|')
axes[1].set(xlabel='驱动频率 / Hz',ylabel='位移/力 / mm·N⁻¹',title='（b）仅驱动质量1，比例阻尼C=M+0.0005K');axes[1].legend()
fig.suptitle('多自由度：模态、激励位置和测点共同决定响应',fontsize=18,fontweight='bold');save(fig,'coupled-modes')
# 4 Wave versus local particle motion, physical displacement kept in micrometres.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));x=np.linspace(0,1.4,1200);f=500.;omega=2*np.pi*f;k=omega/m.C
for t,col in [(0,B),(.0005,P)]:axes[0].plot(x,np.sqrt(2)*np.cos(omega*t-k*x),color=col,label=f't={1000*t:g} ms')
axes[0].set(xlabel='位置 x / m',ylabel='声压 / Pa',title='（a）500 Hz行波：0.5 ms前进0.1715 m');axes[0].legend()
t=np.linspace(0,.004,1001);xi=np.sqrt(2)/(m.Z0*omega)*np.sin(omega*t);axes[1].plot(t*1000,xi*1e6,color=G);axes[1].set(xlabel='时间 / ms',ylabel='固定位置质点位移 / μm',title='（b）p_rms=1 Pa：局部往复，不随波峰远行')
fig.suptitle('振动发生在局部，声波传播的是扰动与能量',fontsize=18,fontweight='bold');save(fig,'wave-particle-motion')
# 5 Standing wave versus active flux; ordinary pressure-only shortcut fails in general.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));x=np.linspace(0,m.C/500,1001);p,u=m.plane_fields(x,1.)
axes[0].plot(x,abs(p)/np.sqrt(2),color=B,label='p_rms / Pa');axes[0].plot(x,m.Z0*abs(u)/np.sqrt(2),color=P,label='ρc·u_rms / Pa');axes[0].set(xlabel='位置 x / m',ylabel='压力或压力等效尺度 / Pa',title='（a）完全反射R=1：压力与速度节点错开');axes[0].legend(fontsize=10)
p,u=m.plane_fields(x,.6);I=m.active_intensity(p,u);shortcut=abs(p)**2/(2*m.Z0);axes[1].plot(x,I*1000,color=G,lw=2,label='净平均声强：Re(PU*)/2');axes[1].plot(x,shortcut*1000,color=R,ls='--',label='单用p_rms²/(ρc)的误用');axes[1].set(xlabel='位置 x / m',ylabel='W/m² × 10⁻³',title='（b）另取R=0.6：净通量恒定，声压平方起伏');axes[1].legend(fontsize=9)
fig.suptitle('驻波可以有储能而无平均净通量；声压大小不等于净声强',fontsize=18,fontweight='bold');save(fig,'standing-wave-intensity')
# 6 Lossless normal incidence, equal interface area; pressure amplitude is not power.
ratio=np.geomspace(.01,100,500);rp,tp,Rpower,Tpower=m.interface(1,ratio);fig,axes=plt.subplots(1,2,figsize=(14,5.5));axes[0].semilogx(ratio,rp,color=B,label='压力反射系数 rₚ');axes[0].semilogx(ratio,tp,color=P,label='压力透射系数 tₚ');axes[0].axhline(0,color=M,lw=.7);axes[0].set(xlabel='比声阻抗比 z₂/z₁',ylabel='压力幅度比',title='（a）压力透射幅度可大于1');axes[0].legend(fontsize=10)
axes[1].semilogx(ratio,Rpower,color=R,label='反射能流比');axes[1].semilogx(ratio,Tpower,color=G,label='透射能流比');axes[1].semilogx(ratio,Rpower+Tpower,color=M,ls=':',label='总和=1');axes[1].set(xlabel='比声阻抗比 z₂/z₁',ylabel='能流比',title='（b）两无损流体、法向入射');axes[1].legend(fontsize=10)
fig.suptitle('边界守恒检查：压力连续、法向速度连续，再核对功率',fontsize=18,fontweight='bold');save(fig,'reflection-transmission')
# 7 Pressure cross term, exactly specified correlation.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));phase=np.linspace(0,np.pi,1001);relative=20*np.log10(np.maximum(2*abs(np.cos(phase/2)),.01));axes[0].plot(phase/np.pi,relative,color=B,lw=2);axes[0].set(xlabel='等幅同频两声压的相位差 / π',ylabel='总声压级 − 单个声压级 / dB',ylim=(-42,8),title='（a）显示下限−40 dB；π处理想值为−∞')
levels=[70,m.combined_spl(70,70),m.combined_spl(70,70,1)];axes[1].bar(['一个70 dB','两路不相关','两路同相'],levels,color=[M,G,P],width=.6)
for i,v in enumerate(levels):axes[1].text(i,v+.4,f'{v:.3f}',ha='center')
axes[1].set(ylabel='声压级 / dB re 20 μPa',ylim=(60,80),title='（b）同一接收位置，相同参考与时间窗口')
fig.suptitle('分贝不能直接相加：相关性决定均方声压交叉项',fontsize=18,fontweight='bold');save(fig,'decibels-correlation')
# 8 Pure outgoing spherical wave has reactive velocity and the stated exact active intensity.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));r=np.geomspace(.25,8,300);p,u=m.spherical_fields(r);lp=20*np.log10(abs(p)/np.sqrt(2)/20e-6);axes[0].semilogx(r,lp,color=B,lw=2);axes[0].set(xlabel='半径 r / m',ylabel='声压级 / dB re 20 μPa',title='（a）纯外向球面波：距离翻倍−6.021 dB')
kr=np.geomspace(.01,100,500);z=1/(1+1/(1j*kr));axes[1].semilogx(kr,z.real,color=G,label='Re(z_s)/(ρc)');axes[1].semilogx(kr,z.imag,color=P,label='Im(z_s)/(ρc)');axes[1].axvline(1,color=M,ls=':');axes[1].set(xlabel='无量纲 kr',ylabel='归一化局部比声阻抗',title='（b）近场含反应性；这里是单极外向球面模型');axes[1].legend(fontsize=10)
fig.suptitle('几何扩散与近场相位：特例的精确关系不推广到所有声源',fontsize=18,fontweight='bold');save(fig,'spherical-near-field')
# 9 Ideal pressure eigenfunctions, real end correction is outside the drawing.
L=.5;x=np.linspace(0,L,501);fig,axes=plt.subplots(1,2,figsize=(14,5.5))
for n,col in [(1,B),(2,G),(3,P)]:
    axes[0].plot(x,np.sin(n*np.pi*x/L),color=col,label=f'n={n}: {n*m.C/(2*L):g} Hz');axes[1].plot(x,np.cos((2*n-1)*np.pi*x/(2*L)),color=col,label=f'n={n}: {(2*n-1)*m.C/(4*L):g} Hz')
for ax in axes:ax.axhline(0,color=M,lw=.6);ax.set(xlabel='管内位置 x / m',ylabel='归一化压力模态形状');ax.legend(fontsize=9)
axes[0].set_title('（a）理想开—开：两端压力节点');axes[1].set_title('（b）理想闭—开：左压力腹、右压力节')
fig.suptitle('管道本征频率来自边界条件，不是只按长度猜一条公式',fontsize=18,fontweight='bold');save(fig,'pipe-boundaries')
# 10 Digital two-tap path, not physical Dirac impulse height.
fs,h,f,H=m.echo_model();fig,axes=plt.subplots(1,2,figsize=(14,5.5));marker,stems,base=axes[0].stem([0,1000*(len(h)-1)/fs],[1,.6],basefmt=' ');plt.setp(stems,color=B);plt.setp(marker,color=B);axes[0].set(xlabel='采样延迟换成的时间 / ms',ylabel='无量纲离散脉冲权重',xlim=(-.5,5),ylim=(0,1.2),title='（a）fs=48 kHz：第0点和第192点')
axes[1].plot(f,20*np.log10(abs(H)),color=P);axes[1].set(xlabel='频率 / Hz',ylabel='相对直达支路增益 / dB',title='（b）H=1+0.6 exp(−i2πf·0.004)，间距250 Hz')
fig.suptitle('两路径干涉就能产生峰谷：频谱峰不自动等于结构模态',fontsize=18,fontweight='bold');save(fig,'measurement-paths')
# Course sketch, native vector spring, mass and outward arcs.
fig,ax=plt.subplots(figsize=(6.4,3.6));ax.axis('off');ax.set(xlim=(0,10),ylim=(0,5));ax.plot([.8,.8],[1.4,3.6],color=M,lw=2);sx=np.linspace(.8,4.1,31);sy=np.full(31,2.5);sy[1:-1:2]+=.35;sy[2:-1:2]-=.35;ax.plot(sx,sy,color=B,lw=2);ax.add_patch(Rectangle((4.1,1.7),1.3,1.6,ec=G,fc='#edf4ef',lw=2));ax.annotate('',xy=(6,2.5),xytext=(5.4,2.5),arrowprops=dict(arrowstyle='->',color=G,lw=2))
for rad in [1.4,2.3,3.2]:ax.add_patch(Arc((5.7,2.5),2*rad,2*rad,theta1=-38,theta2=38,color=P,lw=2))
ax.text(.7,4.3,'振动与声学基础',fontsize=18,fontweight='bold',color=B);fig.tight_layout();path=ROOT/'public/figures/foundation-courses/vibrations-and-acoustics.svg';fig.savefig(path,metadata={'Date':None},transparent=True);path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8');plt.close(fig)
(REC/'calculations.json').write_text(json.dumps(m.summary(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(m.summary(),ensure_ascii=False))
