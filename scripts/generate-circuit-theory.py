"""Original scientific diagrams/curves. Specified circuits; not device measurements."""
from pathlib import Path
import importlib.util,json,sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Polygon
ROOT=Path(__file__).resolve().parents[1];sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('ct_examples',ROOT/'public/code/circuit-theory/experiments.py')
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
FIG=ROOT/'public/figures/circuit-theory';PRE=ROOT/'artifacts/circuit-theory/figures';REC=ROOT/'docs/research/circuit-theory-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':12,'svg.fonttype':'path','svg.hashsalt':'circuit-theory-course','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,M,P='#22658c','#31755e','#b44e37','#61727d','#79639d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创电路原理教学图 · 指定理想模型或数值模拟，非器件实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.055,1,.90),w_pad=3,h_pad=3)
    p=FIG/(name+'.svg');fig.savefig(p,metadata={'Date':None},facecolor='white')
    p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
def wire(ax,a,b,c=M):ax.plot([a[0],b[0]],[a[1],b[1]],color=c,lw=1.6)
def dot(ax,p):ax.plot(*p,'o',color=M,ms=4)
def resistor(ax,a,b,label,offset=(0,.25)):
    aa=np.array(a);bb=np.array(b);dv=bb-aa;length=np.linalg.norm(dv);u=dv/length;v=np.array([-u[1],u[0]])
    pts=[aa,aa+.22*dv]
    for t,sign in zip(np.linspace(.25,.75,9),[0,1,-1,1,-1,1,-1,1,0]):pts.append(aa+t*dv+sign*.09*v)
    pts += [aa+.78*dv,bb];pts=np.array(pts);ax.plot(pts[:,0],pts[:,1],color=M,lw=1.6)
    mid=(aa+bb)/2+np.array(offset);ax.text(*mid,label,ha='center',va='center',fontsize=11,color=B)
def cap(ax,a,b,label,offset=(.35,0)):
    aa=np.array(a);bb=np.array(b);dv=bb-aa;u=dv/np.linalg.norm(dv);v=np.array([-u[1],u[0]]);mid=(aa+bb)/2
    p1=mid-.05*u;p2=mid+.05*u;wire(ax,aa,p1);wire(ax,p2,bb)
    wire(ax,p1-.17*v,p1+.17*v);wire(ax,p2-.17*v,p2+.17*v)
    ax.text(*(mid+np.array(offset)),label,ha='center',va='center',fontsize=11,color=B)
def ground(ax,x,y):
    wire(ax,(x,y),(x,y-.10))
    for j,w in enumerate([.22,.14,.06]):wire(ax,(x-w/2,y-.10-j*.06),(x+w/2,y-.10-j*.06))
def source(ax,x,y,label):
    ax.add_patch(Circle((x,y),.25,fill=False,ec=M,lw=1.6));ax.text(x,y+.09,'+',ha='center',va='center');ax.text(x,y-.10,'−',ha='center',va='center')
    ax.text(x-.45,y,label,ha='right',va='center',color=B,fontsize=11)
def clean(ax,lim=(0,6,0,3)):
    ax.axis('off');ax.set(xlim=lim[:2],ylim=lim[2:]);ax.set_aspect('equal')
# 1 Reference sign and basic elements.
fig,axes=plt.subplots(1,3,figsize=(14,5.2))
for ax,title in zip(axes,['（a）电阻：耗散','（b）电容：电场储能','（c）电感：磁场储能']):
    clean(ax,(0,3,0,2.4));ax.set_title(title)
    ax.text(.5,1.65,'+',fontsize=18);ax.text(2.4,1.65,'−',fontsize=18)
    ax.annotate('i',xy=(1.2,1.3),xytext=(.4,1.3),arrowprops={'arrowstyle':'->','color':B},color=B)
    ax.text(1.5,.85,'u：左端电位减右端电位',ha='center',fontsize=10)
resistor(axes[0],(.4,1.6),(2.6,1.6),'',offset=(0,0));cap(axes[1],(.4,1.6),(2.6,1.6),'',offset=(0,0))
ax=axes[2];xx=np.linspace(.8,2.2,300);yy=1.6+.13*np.sin(np.linspace(0,8*np.pi,300));wire(ax,(.4,1.6),(.8,1.6));ax.plot(xx,yy,color=M);wire(ax,(2.2,1.6),(2.6,1.6))
for ax,txt in zip(axes,['p = ui = Ri² ≥ 0','i = C du/dt；W = Cu²/2','u = L di/dt；W = Li²/2']):ax.text(1.5,.32,txt,ha='center',fontsize=12,color=G)
fig.suptitle('先规定参考方向：电流流入电压的正参考端，p = ui 表示吸收功率',fontsize=17,fontweight='bold');save(fig,'reference-and-elements')
# 2 Divider topology and load dependence.
fig,axes=plt.subplots(1,2,figsize=(14,5.8));ax=axes[0];clean(ax,(-.5,5.3,-.5,3.2))
source(ax,.6,1.5,'Vs = 1 V');wire(ax,(.6,1.75),(.6,2.5));resistor(ax,(.6,2.5),(2.8,2.5),'R1 = 10 kΩ')
wire(ax,(.6,1.25),(.6,.3));wire(ax,(.6,.3),(4.4,.3));resistor(ax,(2.8,2.5),(2.8,.3),'R2\n10 kΩ',offset=(-.5,0))
wire(ax,(2.8,2.5),(4.4,2.5));resistor(ax,(4.4,2.5),(4.4,.3),'RL',offset=(.35,0));dot(ax,(2.8,2.5));ground(ax,2.8,.3);ax.text(3.6,2.82,'输出 uo',ha='center',color=R);ax.set_title('（a）负载与R2并联，不与R1串联')
loads=np.logspace(2,7,400);out=.5*loads/(loads+5000);axes[1].semilogx(loads/1000,out,color=B,lw=2);axes[1].axhline(.5,color=M,ls='--',label='开路 0.5 V');axes[1].scatter([10],[1/3],color=R,label='RL = 10 kΩ：1/3 V')
axes[1].set(xlabel='负载电阻 RL / kΩ',ylabel='输出直流电压 / V',title='（b）戴维南等效：Vth = 0.5 V，Rth = 5 kΩ');axes[1].legend(fontsize=10)
fig.suptitle('接上负载后，原来的“半电压”不再保持',fontsize=18,fontweight='bold');save(fig,'divider-and-load')
# 3 Nodal network.
net=model.resistive_network();fig,axes=plt.subplots(1,2,figsize=(14,5.8));ax=axes[0];clean(ax,(-.8,6.8,-.6,3.2))
source(ax,.6,1.5,'1 V');wire(ax,(.6,1.75),(.6,2.5));wire(ax,(.6,1.25),(.6,.2));resistor(ax,(.6,2.5),(2.6,2.5),'R1 = 1 kΩ')
resistor(ax,(2.6,2.5),(2.6,.2),'R2\n2 kΩ',offset=(-.42,0));resistor(ax,(2.6,2.5),(4.6,2.5),'R3 = 1 kΩ');resistor(ax,(4.6,2.5),(4.6,.2),'R4\n1 kΩ',offset=(-.42,0))
wire(ax,(4.6,2.5),(6,2.5));wire(ax,(6,2.5),(6,1.6));wire(ax,(6,1.1),(6,.2));ax.add_patch(Circle((6,1.35),.25,fill=False,ec=M,lw=1.6));ax.annotate('',xy=(6,1.52),xytext=(6,1.18),arrowprops={'arrowstyle':'->','color':B});ax.text(6.3,1.35,'0.2 mA\n向上注入',fontsize=10,va='center')
wire(ax,(.6,.2),(6,.2));ground(ax,3.6,.2);dot(ax,(2.6,2.5));dot(ax,(4.6,2.5));ax.text(2.6,2.9,'Va',ha='center',color=R);ax.text(4.6,2.9,'Vb',ha='center',color=R);ax.set_title('（a）两个未知节点，地为同一个节点')
curr=np.array(net['currents_A'])*1000;axes[1].bar(['R1→Va','Va→地','Va→Vb','Vb→地'],curr,color=[B,G,R,P])
for j,v in enumerate(curr):axes[1].text(j,v+.01,f'{v:.3f}',ha='center')
axes[1].set(ylabel='按所标方向的电流 / mA',ylim=(0,.57),title='（b）Va = 0.550 V，Vb = 0.375 V')
fig.suptitle('节点法：把每条支路写成电位差，再逐节点列KCL',fontsize=18,fontweight='bold');save(fig,'nodal-network')
# 4 First order voltage, current and energy.
rc=model.first_order();t=np.array(rc['t_s']);vc=np.array(rc['vc_V']);ii=np.array(rc['i_A'])
fig,axes=plt.subplots(1,2,figsize=(13,5.7));axes[0].plot(t*1000,vc,color=B,label='电容电压');axes[0].scatter([10],[1-np.exp(-1)],color=R);axes[0].axhline(1,color=M,ls='--')
axes[0].set(xlabel='阶跃后时间 / ms',ylabel='电容电压 / V',title='（a）R = 10 kΩ，C = 1 µF，τ = 10 ms')
axes[1].plot(t*1000,ii*1e6,color=G);axes[1].axvline(10,color=M,ls=':');axes[1].set(xlabel='阶跃后时间 / ms',ylabel='流入电容正端的电流 / µA',title='（b）电流从100 µA衰减，电压连续')
fig.suptitle('一阶阶跃：uC(0) = 0，理想源从0跳到1 V',fontsize=18,fontweight='bold');save(fig,'rc-transient')
# 5 Frequency gain and phase.
freq=model.frequency_response();f=np.array(freq['f_Hz']);fig,axes=plt.subplots(1,2,figsize=(14,5.8))
for key,c,label in [('lp',B,'低通：空载输出跨C'),('hp',G,'高通：空载输出跨R'),('loaded',R,'低通：RL = 10 kΩ')]:
    h=freq[key];axes[0].semilogx(f,20*np.log10(abs(h)),color=c,label=label);axes[1].semilogx(f,np.angle(h)*180/np.pi,color=c,label=label)
for ax in axes:ax.axvline(freq['fc_Hz'],color=M,ls=':');ax.set(xlabel='频率 / Hz')
axes[0].set(ylabel='电压幅值比 / dB',ylim=(-65,4),title='（a）R = 10 kΩ，C = 10 nF');axes[0].legend(fontsize=9)
axes[1].set(ylabel='输出相对输入的相位 / °',title='（b）负载同时改变增益和极点')
fig.suptitle('同一组R和C，取样端与负载决定传递函数',fontsize=18,fontweight='bold');save(fig,'rc-frequency')
# 6 RLC damping and resistor-output resonance.
fig,axes=plt.subplots(1,2,figsize=(14,5.9));responses=[]
for resistance,c,label in [(40,B,'40 Ω：欠阻尼'),(200,G,'200 Ω：临界阻尼'),(500,R,'500 Ω：过阻尼')]:
    data=model.rlc_step(resistance);responses.append(data);axes[0].plot(np.array(data['t_s'])*1e3,data['vc_V'],color=c,label=label)
axes[0].set(xlabel='时间 / ms',ylabel='电容电压 / V',title='（a）1 V阶跃，L = 10 mH，C = 1 µF');axes[0].legend(fontsize=9)
ff=np.logspace(2,5,700);ww=2*np.pi*ff
for resistance,c in [(40,B),(200,G),(500,R)]:
    h=resistance/(resistance+1j*(ww*.01-1/(ww*1e-6)));axes[1].semilogx(ff,abs(h),color=c,label=f'R = {resistance} Ω')
axes[1].axvline(responses[0]['f0_Hz'],ls=':',color=M);axes[1].set(xlabel='频率 / Hz',ylabel='跨R电压 / 输入电压',title='（b）串联电流共振在约1591.55 Hz');axes[1].legend(fontsize=9)
fig.suptitle('阻尼、自然频率与共振：先说清观察哪个输出',fontsize=18,fontweight='bold');save(fig,'rlc-damping')
# 7 Complex power and time average.
power=model.power_example();tt=np.linspace(0,.003,1201);phi=np.arctan2(24,32);voltage=np.sqrt(2)*np.cos(2*np.pi*1000*tt);current=np.sqrt(2)*.025*np.cos(2*np.pi*1000*tt-phi)
fig,axes=plt.subplots(1,2,figsize=(14,5.7));ax=axes[0];right=ax.twinx()
l1=ax.plot(tt*1000,voltage,color=B,label='电压 / V');l2=right.plot(tt*1000,current*1000,color=G,ls='--',label='电流 / mA')
ax.set(xlabel='时间 / ms',ylabel='电压 / V',title='（a）1 kHz，电流滞后36.87°');right.set_ylabel('电流 / mA');ax.legend(l1+l2,[l.get_label() for l in l1+l2],fontsize=9,loc='lower left')
axes[1].plot(tt*1000,voltage*current*1000,color=P);axes[1].axhline(20,color=R,ls='--',label='平均有功功率20 mW');axes[1].axhline(0,color=M,lw=.7);axes[1].set(xlabel='时间 / ms',ylabel='瞬时吸收功率 / mW',title='（b）瞬时功率可为负，有功均值为正');axes[1].legend(fontsize=9)
fig.suptitle('RMS相量：Z = 32 + j24 Ω，P = 20 mW，Q = 15 mvar',fontsize=18,fontweight='bold');save(fig,'phasor-and-power')
# 8 Finite op amp gain and clipping constraints.
fig,axes=plt.subplots(1,2,figsize=(14,5.7));ff=np.logspace(0,7,700);a0=1e5;fp=10.;beta=.1;a=a0/(1+1j*ff/fp);cl=a/(1+beta*a)
axes[0].semilogx(ff,20*np.log10(abs(cl)),color=B,label='单主极点模型闭环增益');axes[0].axhline(20,color=M,ls='--',label='理想增益10，即20 dB');axes[0].set(xlabel='频率 / Hz',ylabel='电压增益 / dB',title='（a）A0 = 10⁵，ft = 1 MHz，噪声增益10');axes[0].legend(fontsize=9)
xin=np.linspace(-.4,.4,400);axes[1].plot(xin,10*xin,color=M,ls='--',label='理想：10倍');axes[1].plot(xin,np.clip(10*xin,-2,2),color=R,label='人为设定输出限幅±2 V')
axes[1].set(xlabel='输入电压 / V',ylabel='输出电压 / V',title='（b）静态限幅示意；未模拟压摆率');axes[1].legend(fontsize=9)
fig.suptitle('运放的“虚短”需要负反馈、线性范围与稳定性',fontsize=18,fontweight='bold');save(fig,'opamp-limits')
# 9 Probe load.
meas=model.measurements();ff=np.logspace(0,7,600);rsource=1e4
fig,axes=plt.subplots(1,2,figsize=(14,5.7))
for rp,cp,c,label in [(1e6,100e-12,B,'1 MΩ ∥ 100 pF'),(10e6,10e-12,G,'10 MΩ ∥ 10 pF')]:
    zp=1/(1/rp+2j*np.pi*ff*cp);h=zp/(rsource+zp);axes[0].semilogx(ff,20*np.log10(abs(h)),color=c,label=label)
    axes[1].semilogx(ff,np.angle(h)*180/np.pi,color=c,label=label)
axes[0].set(xlabel='频率 / Hz',ylabel='被测节点电压 / 原开路电压 / dB',ylim=(-55,2),title='（a）源电阻10 kΩ，探头接入即成负载');axes[0].legend(fontsize=9)
axes[1].set(xlabel='频率 / Hz',ylabel='相对开路信号的相位 / °',title='（b）小电容在高频也会影响结果')
fig.suptitle('测量会改变电路：输入电阻与电容须一起考虑',fontsize=18,fontweight='bold');save(fig,'probe-loading')
# 10 Noise integral.
fig,axes=plt.subplots(1,2,figsize=(14,5.7));ff=np.logspace(0,7,700);fc=1/(2*np.pi*1e4*1e-8)
density=meas['noise_density_V_per_sqrtHz'];filtered=density/np.sqrt(1+(ff/fc)**2)
axes[0].loglog(ff,filtered*1e9,color=B,label='跨C输出噪声幅度谱密度');axes[0].axhline(density*1e9,color=M,ls='--',label='未滤波电阻噪声');axes[0].set(xlabel='频率 / Hz',ylabel='噪声幅度谱密度 / nV/√Hz',title='（a）R = 10 kΩ，C = 10 nF，T = 300 K');axes[0].legend(fontsize=9)
ratio=np.logspace(-3,4,500);cumulative=(2/np.pi)*np.arctan(ratio);axes[1].semilogx(ratio,cumulative,color=G);axes[1].axhline(1,color=M,ls='--');axes[1].set(xlabel='积分上限 / fc',ylabel='累计噪声方差 / (kBT/C)',title='（b）积分功率谱，得到均方值而非幅度和')
fig.suptitle('热噪声与带宽：一阶低通的等效噪声带宽 = πfc/2',fontsize=18,fontweight='bold');save(fig,'thermal-noise')
# Characteristic course sketch: source, resistor, capacitor and waveform.
(ROOT/'public/figures/foundation-courses/circuit-theory.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 180" role="img"><title>电路原理：电源、电阻、电容与充电曲线</title><rect width="320" height="180" fill="#f3f1f8"/><g fill="none" stroke="#716286" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M54 67V42H92l7-8 10 16 10-16 10 16 10-16 9 8h30v42m0 10v44H54V107"/><circle cx="54" cy="87" r="20"/><path d="M48 81h12m-6-6v12m-6 8h12M163 84h30m-30 10h30M111 138v8m-12 0h24m-19 5h14m-10 5h6"/></g><path d="M221 133V52m0 81h70" fill="none" stroke="#a6a0b0" stroke-width="1.7"/><path d="M223 130c8-37 23-54 62-57" fill="none" stroke="#437b91" stroke-width="2.5"/><path d="M224 70h64" fill="none" stroke="#b58258" stroke-width="1.6" stroke-dasharray="4 4"/></svg>\n''',encoding='utf-8')
small_rc={k:v for k,v in rc.items() if k not in ('t_s','vc_V','i_A')}
small_rlc=[{k:v for k,v in d.items() if k not in ('t_s','vc_V','i_A')} for d in responses]
vals={'network':net,'divider':{'open_V':.5,'Rth_ohm':5000,'loaded_10k_V':1/3},'rc':small_rc,'frequency':{k:v for k,v in freq.items() if k not in ('f_Hz','lp','hp','loaded')},'rlc':small_rlc,'power':power,'measurement':meas,
'opamp':{'A0':a0,'fp_Hz':fp,'ft_Hz':a0*fp,'beta':beta,'dc_closed_gain':a0/(1+beta*a0),'closed_pole_Hz':fp*(1+beta*a0),'required_slew_20kHz_1Vpk_V_per_us':2*np.pi*2e4/1e6}}
(REC/'calculations.json').write_text(json.dumps(vals,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(vals,ensure_ascii=True,indent=2))
