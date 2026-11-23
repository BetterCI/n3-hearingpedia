"""Original system and arithmetic teaching figures, not product data."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch

OUT=Path(__file__).resolve().parent
font=FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':font.get_name(),'font.size':14,
                     'axes.unicode_minus':False,'svg.fonttype':'path'})
BLUE,ORANGE,GREEN='#286896','#bf6829','#337d70'

def save(fig,name):
    fig.savefig(OUT/(name+'.svg'));fig.savefig(OUT/(name+'.png'),dpi=96)
    p=OUT/(name+'.svg');p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)

fig,axes=plt.subplots(2,1,figsize=(11.5,9),dpi=96)
fig.suptitle('日常运行的系统边界：体外 → 体内',fontsize=22,y=.975)
fig.subplots_adjust(left=.035,right=.98,bottom=.05,top=.90,hspace=.22)
def box(ax,x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.018',facecolor=color,edgecolor='white'))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',color='white',fontsize=14)
def arrow(ax,p,q,dashed=False):
    ax.annotate('',q,p,arrowprops={'arrowstyle':'->','color':'#555555','lw':1.6,'linestyle':'--' if dashed else '-'})
for ax in axes:
    ax.set(xlim=(0,11),ylim=(0,4));ax.axis('off')
a,b=axes
a.set_title('（a）常规模式：外部拾音、处理和供能',loc='left',fontsize=17)
a.axvspan(5.1,11,color='#e9f2f5',zorder=-1);a.plot([5.1,5.1],[0,4],'--',color='#888888')
a.text(2.5,3.65,'体外',ha='center');a.text(8,3.65,'体内',ha='center')
box(a,.25,2.0,1.7,.9,'麦克风',BLUE);box(a,2.5,2.,2,.9,'声音处理器',BLUE)
box(a,5.7,2.,2.1,.9,'接收／刺激器',GREEN);box(a,8.5,2.,2.1,.9,'耳蜗内电极',GREEN)
arrow(a,(1.95,2.45),(2.5,2.45));arrow(a,(4.5,2.45),(5.7,2.45));arrow(a,(7.8,2.45),(8.5,2.45))
box(a,2.5,.35,2,.8,'外部电源',ORANGE);arrow(a,(3.5,1.15),(3.5,2),True)
a.text(5.1,1.35,'跨皮肤\n信息与能量',ha='center',fontsize=12)
b.set_title('（b）全植入模式：体内信号链独立运行',loc='left',fontsize=17)
b.axvspan(2.5,11,color='#e9f2f5',zorder=-1);b.plot([2.5,2.5],[0,4],'--',color='#888888')
b.text(1.2,3.65,'体外',ha='center');b.text(6.9,3.65,'体内',ha='center')
box(b,.12,.35,2,.85,'外部充电器',ORANGE)
box(b,3.,2.,1.9,.9,'植入传感器',GREEN);box(b,5.5,2.,2,.9,'处理／刺激器',GREEN);box(b,8.3,2.,2.3,.9,'耳蜗内电极',GREEN)
b.text(1.2,2.45,'外界声音',ha='center');arrow(b,(2.05,2.45),(3,2.45))
arrow(b,(4.9,2.45),(5.5,2.45));arrow(b,(7.5,2.45),(8.3,2.45))
box(b,5.5,.35,2,.85,'植入电源',ORANGE)
arrow(b,(2.12,.77),(5.5,.77),True);arrow(b,(6.5,1.2),(6.5,2),True)
b.text(3.65,1.05,'经皮供能',ha='center',fontsize=12)
save(fig,'01-system-boundary')

def panels(title):
    fig,axes=plt.subplots(2,1,figsize=(11.5,9),dpi=96)
    fig.suptitle(title,fontsize=22,y=.975)
    fig.subplots_adjust(left=.13,right=.95,bottom=.12,top=.90,hspace=.52)
    for ax in axes:
        ax.spines[['top','right']].set_visible(False);ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
    return fig,axes
fig,(a,b)=panels('后级均衡恢复幅度，但不恢复输入信噪比')
pos=np.arange(3);target=np.array([1.,.25,1.]);noise=np.array([.1,.1,.4])
a.bar(pos-.18,target,.36,color=BLUE,label='目标幅度');a.bar(pos+.18,noise,.36,color=ORANGE,hatch='//',label='自噪声幅度')
labels=['对照通路','衰减通路','衰减后 ×4 均衡']
a.set_xticks(pos,labels);a.set(ylim=(0,1.3),ylabel='输出幅度（任意单位）');a.legend(fontsize=12)
a.set_title('（a）噪声在传感器输出端引入',loc='left')
snr=20*np.log10(target/noise);b.bar(pos,snr,width=.5,color=[GREEN,ORANGE,ORANGE])
b.set_xticks(pos,labels);b.set(ylim=(0,25),ylabel='信噪比（dB）');b.set_title('（b）均衡前后比值不变',loc='left')
for xx,yy in zip(pos,snr):b.text(xx,yy+.7,f'{yy:.2f} dB',ha='center')
save(fig,'02-input-noise')

fig,(a,b)=panels('能量预算：续航、运行与充电的关系')
power=np.linspace(2,10,100);duration=120/power
a.plot(power,duration,color=BLUE,lw=2);a.scatter([5,8],[24,15],color=ORANGE,s=60)
a.annotate('5 mW → 24 h',(5,24),xytext=(5.4,40),arrowprops={'arrowstyle':'->'})
a.annotate('8 mW → 15 h',(8,15),xytext=(7.2,30),arrowprops={'arrowstyle':'->'})
a.set(xlabel='平均运行功率（mW）',ylabel='理想续航（h）',ylim=(0,65))
a.set_title('（a）固定可用能量 120 mWh',loc='left')
eta=np.array([.3,.5,.7]);net=eta*100-5;hours=120/net
b.bar(eta*100,net,width=10,color=GREEN)
b.set(xlabel='有效传输效率（%）',ylabel='净补能功率（mW）',ylim=(0,90));b.set_xticks(eta*100)
b.set_title('（b）外部 100 mW，运行负载 5 mW',loc='left')
for xx,yy,hh in zip(eta*100,net,hours):b.text(xx,yy+2,f'{yy:g} mW\n补能约 {hh:.2f} h',ha='center',fontsize=13)
save(fig,'03-power-budget')
assert np.allclose(snr,[20,7.9588001734,7.9588001734])
assert np.isclose(120/5,24) and np.isclose(120/8,15)
assert np.allclose(net,[25,45,65])
validation={'data_type':'synthetic teaching examples; no product specifications',
 'input_target':target.tolist(),'output_noise':noise.tolist(),'snr_db':snr.tolist(),
 'energy_mwh':120,'runtime_h_at_5_8_mw':[24,15], 'net_charge_mw':net.tolist(),
 'ideal_charge_h':hours.tolist(),'figure_pixels':[1104,864],'assertions':'passed'}
(OUT/'validation.json').write_text(json.dumps(validation,indent=2)+'\n',encoding='utf-8')
print(json.dumps(validation))
