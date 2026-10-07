from pathlib import Path
import numpy as np,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
ROOT=Path(__file__).parent
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.unicode_minus':False,'svg.fonttype':'path','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':150})
C=['#276a8c','#b75c3c','#59785b'];reports={}
def save(fig,name):
 fig.savefig(ROOT/(name+'.svg'),bbox_inches='tight');fig.savefig(ROOT/(name+'.png'),bbox_inches='tight');plt.close(fig)
def clean(ax):ax.grid(alpha=.17);ax.set_axisbelow(True)

fig,ax=plt.subplots(figsize=(10,5.3));ax.set(xlim=(0,10),ylim=(0,5.3));ax.axis('off')
def box(x,y,w,h,label):
 ax.add_patch(Rectangle((x,y),w,h,facecolor='white',edgecolor='#697b86',lw=1));ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=10)
def arrow(xy,xytext):ax.annotate('',xy=xy,xytext=xytext,arrowprops={'arrowstyle':'->','color':'#506471','lw':1.3})
for x,label in [(0,'数字刺激\n幅度、频率、时长'),(2.6,'播放链\n软件、接口、增益'),(5.2,'换能器\n指定耳机与配置'),(7.8,'声学负载\n耦合器／耳模拟器')]:box(x,3.5,2.2,1,label)
for x in [2.2,4.8,7.4]:arrow((x+.4,4),(x,4))
box(0,1.2,2.2,1,'参考仪器\n校准及溯源信息');box(3.1,1.2,2.4,1,'测量链\n麦克风、分析与修正');box(6.5,1.2,3.5,1,'指定条件下的物理输出\n测量值与不确定度')
arrow((3.1,1.7),(2.2,1.7));arrow((6.5,1.7),(5.5,1.7));arrow((4.3,2.2),(8.9,3.5))
ax.text(6.1,2.9,'声压测量',ha='center',fontsize=10)
ax.text(5,.55,'物理输出与适用参考零点的对应 → 听力级；骨导需采用机械测量负载',ha='center',fontsize=11)
ax.text(0,4.9,'测听输出路径',fontsize=12);ax.text(0,2.65,'测量与参考路径',fontsize=12)
save(fig,'01-calibration-chain')
reports['chain']={'schematic':True,'air_conduction_load_only':True}

freq=np.array([250,500,1000,2000,4000,8000]);rA=np.array([20,14,10,12,18,24]);rB=np.array([32,28,25,22,29,35])
fig,axs=plt.subplots(1,2,figsize=(10,4.7),layout='constrained')
for ax,add,title in zip(axs,[0,40],['A  假设参考零点（0 dB HL）','B  假设 40 dB HL 的目标输出']):
 ax.plot(freq,rA+add,'o-',color=C[0],label='假设配置 A');ax.plot(freq,rB+add,'s--',color=C[1],label='假设配置 B');ax.set_xscale('log',base=2);ax.set_xticks(freq,labels=freq);ax.set(xlabel='频率 / Hz',ylabel='耦合器声压级 / dB SPL',ylim=(0,82),title=title);clean(ax);ax.legend(fontsize=9)
fig.suptitle('全部参考数值为教学设定，不代表任何实际耳机',fontsize=12);save(fig,'02-hl-spl-reference')
assert np.array_equal((rA+40)-rA,np.full(6,40))
reports['reference']={'hypothetical_not_standard_values':True,'frequency_hz':freq.tolist(),'reference_A_db_spl':rA.tolist(),'reference_B_db_spl':rB.tolist(),'target_db_hl':40}

gain=np.linspace(-30,30,301);linear=60+gain;comp=np.where(gain<=10,60+gain,70+.4*(gain-10))
t=np.arange(0,.004,1/48000);a=.1*np.sin(2*np.pi*1000*t);b=.05*np.sin(2*np.pi*1000*t)
fig,axs=plt.subplots(1,2,figsize=(10,4.7),layout='constrained')
axs[0].plot(gain,linear,color=C[0],label='线性模型：斜率 1');axs[0].plot(gain,comp,'--',color=C[1],label='压缩模型：高段斜率 0.4');axs[0].axvline(10,color='#9aa4aa',ls=':',lw=1);axs[0].set(xlabel='相对参考驱动的数字增益 / dB',ylabel='假设输出声压级 / dB SPL',title='A  假设输出关系',ylim=(25,95));axs[0].legend(fontsize=9);clean(axs[0])
axs[1].plot(t*1000,a,color=C[0],label='峰值幅度 0.10');axs[1].plot(t*1000,b,'--',color=C[1],label='峰值幅度 0.05');axs[1].set(xlabel='时间 / ms',ylabel='数字相对幅度',ylim=(-1,1),xlim=(0,4),title='B  1 kHz 正弦（未削波）');axs[1].legend(fontsize=9);clean(axs[1]);save(fig,'03-digital-output')
reports['gain']={'synthetic':True,'reference_output_db_spl':60,'compression_knee_gain_db':10,'compression_slope':.4,'halving_db':float(20*np.log10(.5)),'target_amplitude_for_50_db_spl':float(.1*10**(-10/20)),'waveform_peak':[float(np.max(a)),float(np.max(b))],'axis_limits':[-1,1]}
assert np.max(np.abs(a))<=1

x=np.linspace(-.3,.3,601);y=np.linspace(-.25,.25,251);f=1000;c=343;r=.55;k=2*np.pi*f/c
# P=e^(ikx)+r e^(-ikx); reference x=0; RMS factors cancel in relative level.
profile=20*np.log10(np.abs(np.exp(1j*k*x)+r*np.exp(-1j*k*x))/(1+r));field=np.tile(profile,(len(y),1))
fig,axs=plt.subplots(1,2,figsize=(10,4.7),layout='constrained')
im=axs[0].imshow(field,origin='lower',extent=[-.3,.3,-.25,.25],aspect='equal',cmap='viridis',vmin=-11,vmax=0);axs[0].plot(0,0,'wo',mec='black',ms=7);axs[0].text(.018,.015,'参考点',color='white',fontsize=10);axs[0].set(xlabel='轴向位置 x / m',ylabel='横向位置 y / m',title='A  一个轴向干涉成分');fig.colorbar(im,ax=axs[0],label='相对参考点的声压级 / dB',shrink=.82)
axs[1].plot(x,profile,color=C[0]);axs[1].plot(0,0,'o',color=C[1]);axs[1].set(xlabel='轴向位置 x / m',ylabel='相对参考点的声压级 / dB',ylim=(-12,1),title='B  通过参考点的截面');clean(axs[1]);fig.suptitle('简化模型：1 kHz 平面波＋反向反射波，反射幅度比 0.55',fontsize=12);save(fig,'04-sound-field')
reports['field']={'idealized_not_room_measurement':True,'frequency_hz':1000,'sound_speed_m_s':343,'reflection_amplitude_ratio':.55,'reference_x_m':0,'relative_min_db':float(profile.min()),'relative_max_db':float(profile.max()),'no_tolerance_claim':True}

vals=np.array([[-.3,.1,.2,-.2,.1],[2.7,3.1,3.2,2.8,3.1],[-2.4,1.5,2.2,-1.8,.5]])
u=np.array([.3,.4,.6,.2]);uc=float(np.sqrt(np.sum(u*u)))
fig,axs=plt.subplots(1,2,figsize=(10,4.8),layout='constrained')
for i in range(3):axs[0].scatter(np.full(5,i)+np.linspace(-.12,.12,5),vals[i],color=C[i],s=32);axs[0].plot([i-.2,i+.2],[vals[i].mean()]*2,color=C[i],lw=2)
axs[0].axhline(0,color='#6b747a',ls='--',lw=1);axs[0].set(xticks=[0,1,2],xticklabels=['A  小幅散布','B  整体偏高','C  装夹变化'],ylabel='相对假设参考的输出偏差 / dB',ylim=(-3.4,4.2),title='A  三种假设重复测量');clean(axs[0]);axs[0].tick_params(axis='x',labelsize=9)
axs[1].barh(['参考校准','读数处理','装夹','短期重复'],u,color=[C[0],C[0],C[1],C[2]]);axs[1].invert_yaxis();axs[1].set(xlabel='假设标准不确定度 / dB',xlim=(0,.8),title='B  独立加性模型的教学预算');
for i,v in enumerate(u):axs[1].text(v+.015,i,f'{v:.1f}',va='center')
axs[1].text(.02,.04,f'合成值 = {uc:.2f} dB；覆盖因子 2：{2*uc:.2f} dB',transform=axs[1].transAxes,fontsize=10);axs[1].set_ylim(4.15,-.65);clean(axs[1]);save(fig,'05-uncertainty')
reports['uncertainty']={'illustrative':True,'repeated_bias_db':vals.tolist(),'independent_standard_components_db':u.tolist(),'combined_db':uc,'coverage_factor':2,'expanded_db':2*uc,'not_threshold_uncertainty':True}
(ROOT/'figure-verification.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'figures':5,'combined_uncertainty_db':uc,'amplitude_halving_db':20*np.log10(.5)},ensure_ascii=False))
