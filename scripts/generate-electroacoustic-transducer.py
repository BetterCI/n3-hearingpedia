"""Original conceptual diagrams and analytic examples; no measured product data."""
from pathlib import Path
import json, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/electroacoustic-transducer';OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':11,'svg.fonttype':'path','axes.unicode_minus':False,'savefig.facecolor':'white'})
blue='#276985';orange='#bf7137';gray='#526873'
def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),bbox_inches='tight');fig.savefig(OUT/(name+'.png'),dpi=165,bbox_inches='tight');plt.close(fig)
def box(ax,x,y,w,h,text,color=blue):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',facecolor='#f2f7fa',edgecolor=color,lw=1.5));ax.text(x+w/2,y+h/2,text,ha='center',va='center',linespacing=1.7,color=color)
fig,ax=plt.subplots(figsize=(11,4.8));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
box(ax,.025,.43,.245,.33,'电域\n电压 V · 电流 I\n电阻抗 V/I（Ω）')
box(ax,.375,.43,.245,.33,'机械域\n力 F · 速度 v\n机械阻抗 F/v（N·s/m）')
box(ax,.725,.43,.245,.33,'声域\n声压 p · 体积速度 U\n声阻抗 p/U（Pa·s/m³）')
for x1,x2,label in [(.275,.365,'耦合机制'),(.625,.715,'有效面积')]:
    ax.annotate('',xy=(x2,.6),xytext=(x1,.6),arrowprops={'arrowstyle':'<->','color':gray,'lw':1.5});ax.text((x1+x2)/2,.81,label,ha='center',color=gray)
ax.text(.5,.94,'端口量与耦合：每个比值都有自己的单位',ha='center',fontsize=17,color=blue)
ax.text(.5,.27,'动圈输出示例：F = Bl I；反电动势 e = Bl v；U = Sd v',ha='center',fontsize=13)
ax.text(.5,.13,'麦克风读出可需要偏置与供电；双向箭头表示域间耦合，不保证整机可逆',ha='center',color=gray,fontsize=11)
save(fig,'domains')
P={'Re_ohm':16.,'Le_H':.0001,'Bl_N_per_A':1.2,'m_kg':.002,'Rm_Ns_per_m':.2,'K_N_per_m':400.,'Sd_m2':.0001,'c_m_per_s':343.,'rho_kg_per_m3':1.2,'cavity_m3':2e-6,'drive_Vrms':.1}
f=np.geomspace(20,1000,4000);w=2*np.pi*f
Kair=P['rho_kg_per_m3']*P['c_m_per_s']**2*P['Sd_m2']**2/P['cavity_m3']
fig,axes=plt.subplots(1,2,figsize=(11,4.8),layout='constrained');checks={}
for extra,color,label in [(0,blue,'未加腔体弹性负载'),(Kair,orange,'密闭后腔：2 cm³')]:
    zm=P['Rm_Ns_per_m']+1j*(w*P['m_kg']-(P['K_N_per_m']+extra)/w)
    ze=P['Re_ohm']+1j*w*P['Le_H'];zin=ze+P['Bl_N_per_A']**2/zm
    v=P['Bl_N_per_A']*P['drive_Vrms']/(ze*zm+P['Bl_N_per_A']**2);i=P['drive_Vrms']/zin;x=v/(1j*w)
    assert np.allclose(P['drive_Vrms'],ze*i+P['Bl_N_per_A']*v)
    assert np.allclose(zm*v,P['Bl_N_per_A']*i)
    assert np.all(zin.real>=P['Re_ohm'])
    f0=np.sqrt((P['K_N_per_m']+extra)/P['m_kg'])/(2*np.pi)
    checks[label]={'undamped_mechanical_f0_Hz':float(f0),'max_equation_residual_V':float(np.max(abs(P['drive_Vrms']-ze*i-P['Bl_N_per_A']*v)))}
    axes[0].semilogx(f,abs(zin),color=color,label=label);axes[1].loglog(f,abs(x)*1e6,color=color)
    axes[0].axvline(f0,color=color,alpha=.3,ls='--');axes[0].text(f0,26,f'{f0:.1f} Hz',rotation=90,va='top',ha='right',color=color,fontsize=9)
axes[0].set(ylabel='输入阻抗幅值 |Zin|（Ω）',ylim=(15,28));axes[1].set(ylabel='位移有效值 |x|（μm）')
for ax in axes:ax.set(xlabel='频率（Hz）',xlim=(20,1000));ax.grid(True,which='both',alpha=.17)
axes[0].legend(loc='lower left',fontsize=9)
fig.suptitle('同一线性动圈模型、同一驱动电压：仅改变后腔弹性',fontsize=16,color=blue)
save(fig,'load-model')
levels=np.linspace(30,110,500);pa=20e-6*10**(levels/20);mv=20*pa
fig,ax=plt.subplots(figsize=(9,4.9),layout='constrained');ax.semilogy(levels,mv,color=blue,lw=2)
for L,p in [(60,.02),(20*np.log10(1/20e-6),1.)]:
    output=20*p;ax.plot(L,output,'o',color=orange);ax.annotate(f'{L:.2f} dB SPL\n{p:g} Pa → {output:g} mV',xy=(L,output),xytext=(-110,26),textcoords='offset points',color=gray,fontsize=11,arrowprops={'arrowstyle':'-','color':gray})
ax.set(xlabel='声压级（dB SPL，参考 20 μPa，有效值）',ylabel='模拟输出电压（mV，有效值）',xlim=(30,110),ylim=(.008,200),title='教学麦克风：20 mV/Pa，1 kHz；假定线性、忽略自噪声和削顶')
ax.grid(True,which='both',alpha=.2);save(fig,'sensitivity')
fig,ax=plt.subplots(figsize=(11,5.4));ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
ax.text(.5,.94,'测量终点取决于负载与问题',ha='center',fontsize=17,color=blue)
for y,source,load,output in [(.68,'扬声器\n给定端电压','自由场／指定距离\n测量麦克风','声压响应、指向性\n以测量位置为条件'),(.41,'入耳式耳机／受话器\n给定端电压','耳模拟器／规定连接\n控制密封与插入','模拟器内声压\n不等于每个人的鼓膜响应'),(.14,'骨导振子\n给定端电压','机械耦合器\n规定接触与加载','振动力等机械量\n不以空气声压替代')]:
    box(ax,.02,y,.25,.18,source);box(ax,.375,y,.27,.18,load);box(ax,.735,y,.245,.18,output,orange)
    for a,b in [(.28,.36),(.65,.72)]:ax.annotate('',xy=(b,y+.09),xytext=(a,y+.09),arrowprops={'arrowstyle':'->','color':gray,'lw':1.5})
save(fig,'measurement-loads')
manifest={'origin':'Original diagrams and analytic teaching examples; no product measurements','parameters':P,'assumptions':['linear steady-state phasors; all amplitudes rms','constant inductance; piston motion; negligible radiation load in both comparisons','sealed cavity pressure uniform, adiabatic compliance only; leakage, tube resonances and thermoviscous losses omitted','mechanical f0 is undamped natural frequency, not generally the constant-voltage displacement maximum'],'added_cavity_stiffness_N_per_m':Kair,'checks':checks,'sensitivity_check':{'20mV_per_Pa_dB_re_1V_per_Pa':float(20*np.log10(.02)),'one_Pa_dBSPL':float(20*np.log10(1/20e-6))},'figures':['domains.svg','load-model.svg','sensitivity.svg','measurement-loads.svg']}
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert np.isclose(Kair,705.894)
assert np.isclose(mv[0],20*20e-6*10**(30/20))
print(json.dumps(manifest['checks'],ensure_ascii=False))

