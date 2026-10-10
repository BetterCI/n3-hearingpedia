"""Original microphone teaching figures; analytic models, not device measurements."""
from pathlib import Path
import json, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/microphone';OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':11,'svg.fonttype':'path','axes.unicode_minus':False,'savefig.facecolor':'white'})
blue='#276985';orange='#bf7137';gray='#526873';green='#4b826e'
def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),bbox_inches='tight');fig.savefig(OUT/(name+'.png'),dpi=165,bbox_inches='tight');plt.close(fig)
def box(ax,x,y,w,h,text,color=blue):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',facecolor='#f2f7fa',edgecolor=color,lw=1.4));ax.text(x+w/2,y+h/2,text,ha='center',va='center',linespacing=1.7,color=color)
fig,ax=plt.subplots(figsize=(11,5.2));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.94,'声学入口与电读出是两个分类维度',ha='center',fontsize=17,color=blue)
box(ax,.03,.60,.26,.21,'声压型\n背侧经慢速通气均压\n声频变化主要从前侧进入')
box(ax,.03,.22,.26,.21,'声压梯度成分\n前、后声路都传入声频\n有效驱动由两侧差压形成')
box(ax,.39,.42,.20,.21,'机械响应\n振膜位移／速度\n受质量、刚度、阻尼影响')
box(ax,.72,.59,.24,.23,'电读出\n动圈：运动感应电压\n电容：间隙改变电容量')
box(ax,.72,.22,.24,.21,'其他读出／制作方式\n压电：应变产生电荷\nMEMS：微结构制作平台')
for x1,y1,x2,y2 in [(.30,.70,.38,.56),(.30,.32,.38,.47),(.60,.56,.71,.70),(.60,.47,.71,.32)]:
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'->','color':gray,'lw':1.5})
ax.text(.5,.08,'通气孔 ≠ 用于定向的后声孔；概念连接图，不表示具体器件的几何布局',ha='center',fontsize=11,color=gray)
save(fig,'sensing-ports')
theta=np.linspace(0,2*np.pi,1441)
fig=plt.figure(figsize=(11,6.8),layout='constrained')
patterns=[(1,'全向：a = 1'),(.5,'心形：a = 0.5'),(0,'八字形：a = 0'),(.25,'窄心形：a = 0.25')]
checks={}
for i,(a,name) in enumerate(patterns):
    ax=fig.add_subplot(2,2,i+1,projection='polar');d=a+(1-a)*np.cos(theta)
    ax.plot(theta,np.abs(d),color=blue,lw=2);ax.set_theta_zero_location('N');ax.set_theta_direction(-1)
    ax.set_ylim(0,1.05);ax.set_rticks([.5,1]);ax.grid(alpha=.25)
    q=1/(a*a+(1-a)**2/3);di=10*np.log10(q);ax.set_title(f'（{chr(97+i)}）'+name+f'；DI = {di:.2f} dB',pad=18,fontsize=12,color=blue)
    if a<.5:ax.plot(theta,np.where(d<0,abs(d),np.nan),color=orange,ls='--',lw=2)
    avg=np.trapz((a+(1-a)*np.cos(np.linspace(0,np.pi,20001)))**2*np.sin(np.linspace(0,np.pi,20001)),np.linspace(0,np.pi,20001))/2
    assert np.isclose(avg,1/q,atol=1e-8)
    checks[name]={'Q':q,'DI_dB':di,'sphere_power_average':float(avg)}
fig.suptitle('理想一阶轴对称响应：径向为线性幅值，前方均归一化为 1\n橙色虚线为相对前方反相的后瓣；DI 按整个球面计算',fontsize=14,color=blue)
save(fig,'polar-patterns')
f=np.geomspace(50,5000,800);c=343.;k=2*np.pi*f/c
fig,ax=plt.subplots(figsize=(10,4.9),layout='constrained')
for r,color,style in [(.05,orange,'-'),(.2,blue,'--'),(1,green,':')]:
    lift=10*np.log10(1+1/(k*r)**2);ax.semilogx(f,lift,color=color,ls=style,label=f'r = {100*r:g} cm',lw=2)
ax.set(xlim=(50,5000),ylim=(0,28),xlabel='频率（Hz）',ylabel='相对相同局部声压的远场响应增量（dB）',title='理想点声源 · 轴向纯梯度接收 · 已补偿远场频率因子')
ax.grid(which='both',alpha=.2);ax.legend(loc='upper center');ax.text(.97,.96,'端口间距远小于 r 和波长\n不含声压本身的 1/r 增长\n不是心形产品的响应曲线',transform=ax.transAxes,ha='right',va='top',color=gray,fontsize=10)
save(fig,'proximity')
levels=np.linspace(30,115,400);p=20e-6*10**(levels/20);s=.01;fullscale=.5
fig,axes=plt.subplots(1,2,figsize=(11,4.9),layout='constrained')
for gain,color,style in [(20,orange,'-'),(5,blue,'--')]:
    v=gain*s*p;clip=20*np.log10(fullscale/(gain*s)/20e-6)
    axes[0].semilogy(levels,v,color=color,ls=style,label=f'模拟增益 G = {gain}（上限 {clip:.2f} dB SPL）',lw=2)
    axes[0].axvline(clip,color=color,alpha=.4,ls=':')
axes[0].axhline(fullscale,color=gray,ls='--');axes[0].text(32,.63,'ADC 正弦满量程：0.5 Vrms',color=gray,fontsize=10)
axes[0].set(xlim=(30,115),ylim=(1e-5,8),xlabel='输入 1 kHz 正弦声压级（dB SPL）',ylabel='ADC 输入电压（Vrms）');axes[0].grid(which='both',alpha=.2);axes[0].legend(loc='lower right',fontsize=8)
rho=np.linspace(0,1,201);benefit=10*np.log10(2/(1+rho));axes[1].plot(rho,benefit,color=blue,lw=2)
axes[1].set(xlabel='两路噪声相关系数 ρ',ylabel='平均后相对单路的 SNR 增益（dB）',xlim=(0,1),ylim=(0,3.4));axes[1].grid(alpha=.2)
axes[1].text(.97,.95,'同一对齐信号、等噪声方差\n等权平均；不含方向性滤波\nρ = 0：3.01 dB；ρ = 1：0 dB',transform=axes[1].transAxes,ha='right',va='top',color=gray,fontsize=10)
fig.suptitle('两种独立的限制：（a）增益与削顶；（b）噪声相关性与融合\n教学设定，未拟合任何产品或论文原型',fontsize=14,color=blue)
save(fig,'gain-and-noise')
manifest={'origin':'Original conceptual and analytic teaching figures; no product measurements or copied paper curves','figures':['sensing-ports.svg','polar-patterns.svg','proximity.svg','gain-and-noise.svg'],'directivity':{'model':'D(theta)=a+(1-a)cos(theta); signed response; spherical averaging; on-axis normalization','checks':checks},'proximity':{'model':'sqrt(1+1/(kr)^2)','c_m_per_s':c,'distances_m':[.05,.2,1],'assumptions':['on-axis point source, pure gradient, negligible port spacing compared with r and wavelength','far-field gradient frequency factor compensated','equal local pressure comparison; excludes geometric 1/r pressure increase; no microphone compensation network']},'gain_example':{'sensitivity_V_per_Pa':s,'ADC_fullscale_sine_Vrms':fullscale,'ADC_fullscale_peak_V':float(fullscale*np.sqrt(2)),'gains':[20,5],'clips_dBSPL':[float(20*np.log10(fullscale/(g*s)/20e-6)) for g in [20,5]],'assumptions':['frequency-independent teaching sensitivity at 1 kHz, linear microphone and preamp until ADC clipping','no specified real microphone AOP; peak limits for non-sinusoidal signals differ']},'noise_average':{'model':'10log10(2/(1+rho))','assumptions':['equal noise variances, same signal gain and phase, stationary additive noise; rho in [0,1]'],'uncorrelated_gain_dB':float(10*np.log10(2))}}
assert np.isclose(checks['心形：a = 0.5']['Q'],3)
assert np.isclose(manifest['gain_example']['clips_dBSPL'][0],101.93820026)
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Generated 4 original figures; angular integration and analytic conversions passed.')
