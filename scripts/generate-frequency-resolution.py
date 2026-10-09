"""Four original, deterministic teaching figures; no participant or device data.

Python + numpy + matplotlib. Log-frequency Gaussian smoothing is a stipulated
power-density model, not a fitted auditory filter or a real implant processor.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/frequency-resolution';OUT.mkdir(parents=True,exist_ok=True)
font=Path('C:/Windows/Fonts/msyh.ttc')
if font.exists():
    font_manager.fontManager.addfont(str(font));family=font_manager.FontProperties(fname=str(font)).get_name()
else:family='Noto Sans CJK SC'
plt.rcParams.update({'font.family':family,'font.size':21,'svg.fonttype':'path','svg.hashsalt':'hearingpedia-frequency-20261009','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})
B,O,G='#1865a2','#b85a16','#526375';sizes={}
def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None,'Creator':'Hearingpedia original teaching figure'})
    path=OUT/(name+'.svg');path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
    fig.savefig(OUT/(name+'.png'),dpi=100)
    sizes[name]={'png_pixels':[round(v*100) for v in fig.get_size_inches()]}
    plt.close(fig)

fig,axs=plt.subplots(1,3,figsize=(21,9))
fig.subplots_adjust(left=.06,right=.98,top=.79,bottom=.29,wspace=.38)
axs[0].bar([1,2],[1000,1020],color=[B,O],width=.55)
axs[0].set(xticks=[1,2],xticklabels=['第一声','第二声'],ylim=(900,1080),ylabel='纯音频率 / Hz')
axs[0].set_title('（a）先后纯音辨别',pad=18,fontsize=24)
axs[0].text(.5,-.32,'指标：频率差别阈\n变化：Δf；任务：哪声更高？',transform=axs[0].transAxes,ha='center',fontsize=20)
f=np.linspace(600,1400,1001)
for sigma,c,label in [(70,B,'较窄（教学）'),(170,O,'较宽（教学）')]:
    axs[1].plot(f,np.exp(-.5*((f-1000)/sigma)**2),c=c,lw=3,label=label)
axs[1].set(xlabel='频率 / Hz',ylabel='归一化功率权重',ylim=(0,1.25),xticks=[600,1000,1400])
axs[1].legend(fontsize=16,loc='upper right');axs[1].set_title('（b）频率选择性',pad=18,fontsize=24)
axs[1].text(.5,-.32,'指标：拟合滤波器带宽\n输入：目标音与不同位置的噪声',transform=axs[1].transAxes,ha='center',fontsize=20)
x=np.linspace(0,2,1001)
axs[2].plot(2**x,1+.65*np.cos(2*np.pi*x),c=B,lw=3,label='峰谷频谱')
axs[2].plot(2**x,1+.65*np.cos(2*np.pi*x+np.pi),c=O,lw=3,ls='--',label='峰谷反转')
axs[2].set(xlabel='相对频率 f/f0',ylabel='相对功率谱密度',xticks=[1,2,4],ylim=(0,2.15))
axs[2].set_xscale('log',base=2);axs[2].legend(fontsize=16,loc='upper right')
axs[2].set_title('（c）频谱形状辨别',pad=18,fontsize=24)
axs[2].text(.5,-.32,'指标：可辨纹波密度等\n任务：峰谷位置变化是否可辨？',transform=axs[2].transAxes,ha='center',fontsize=20)
fig.text(.5,.92,'不同任务测不同对象，不能汇成一个通用“最小频差”',ha='center',fontsize=27)
fig.text(.5,.075,'三幅均为教学设定；（a）的 20 Hz 差值不是人耳阈值；（b）不代表具体听者',ha='center',fontsize=20,color=G)
save(fig,'01-three-constructs')

# Exact Fourier-domain convolution on a four-octave periodic grid.
length=4.;N=4096;x=np.arange(N)*length/N
freq=250*2**x;sigmas=[.06,.18];rates=[1,4];verification=[]
fig,axs=plt.subplots(2,2,figsize=(20,12))
fig.subplots_adjust(left=.075,right=.98,bottom=.15,top=.87,wspace=.25,hspace=.4)
for col,r in enumerate(rates):
    p=1+.8*np.cos(2*np.pi*r*x)
    for row,sigma in enumerate(sigmas):
        transfer=np.exp(-2*np.pi**2*sigma**2*np.fft.fftfreq(N,d=length/N)**2)
        output=np.fft.ifft(np.fft.fft(p)*transfer).real
        factor=float(np.exp(-2*np.pi**2*sigma**2*r*r));m=.8*factor
        observed=float((output.max()-output.min())/(output.max()+output.min()))
        assert abs(observed-m)<1e-12
        verification.append({'rpo':r,'sigma_octave':sigma,'contrast_retention':factor,'output_modulation':observed,'analytic_error':abs(observed-m)})
        ax=axs[row,col];ax.plot(freq,p,color=G,lw=1.7,alpha=.5,ls='--',label='输入：m=0.8')
        ax.plot(freq,output,color=B if row==0 else O,lw=3,label=f'平滑输出：m={m:.4g}')
        ax.set_xscale('log',base=2);ax.set(xticks=[250,500,1000,2000,4000],xticklabels=['250','500','1000','2000','4000'],ylim=(0,2.35),ylabel='相对功率密度')
        if row==1:ax.set_xlabel('频率 / Hz（对数坐标）')
        ax.legend(fontsize=18,loc='upper right')
        ax.set_title(f'（{"abcd"[row*2+col]}）r={r} RPO；σ={sigma:.2f} 八度',fontsize=25,pad=12)
fig.text(.5,.95,'同一频谱，对数频率平滑越强，密集峰谷越难保留',ha='center',fontsize=27)
fig.text(.5,.055,'高斯功率平滑教学模型；四八度周期边界；σ 不是 ERB，输出不代表行为阈值',ha='center',fontsize=21,color=G)
save(fig,'02-spectral-smoothing')

fig,ax=plt.subplots(figsize=(20,10));ax.set_axis_off();ax.set(xlim=(0,20),ylim=(0,10))
def box(x,y,w,h,title,detail,color=B):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.15,rounding_size=.15',facecolor='#f3f7fa',edgecolor=color,lw=2))
    ax.text(x+w/2,y+h*.72,title,ha='center',va='center',fontsize=24,color=color)
    ax.text(x+w/2,y+h*.32,detail,ha='center',va='center',fontsize=20,linespacing=1.55)
def arrow(x1,y1,x2,y2):ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'->','color':G,'lw':2})
ax.text(10,9.45,'纯音频率辨别：从一次判断到一个有条件的阈值',ha='center',fontsize=28)
box(.6,6,5.1,2.25,'① 两个时段','1000 Hz 与 1000+Δf Hz\n顺序随机；时长与包络一致')
box(7.1,6,5.1,2.25,'② 明确任务','选择音高更高的时段\n记录正确／错误')
box(13.6,6,5.1,2.25,'③ 改变频差','按规定程序调节 Δf\n容易时缩小，困难时增大')
arrow(5.9,7.1,6.8,7.1);arrow(12.4,7.1,13.3,7.1)
box(4,2.3,11.6,2.3,'④ 阈值与可靠性','报告判据、重复测量与不确定性\n同时记录频率、声级、呈现耳、可听度与训练',O)
arrow(16.1,5.8,16.1,3.5);arrow(16.1,3.5,15.65,3.5)
ax.text(10,.65,'“更高”与“不同”不是同一任务；上述流程没有测得任何真人阈值',ha='center',fontsize=22,color=G)
fig.subplots_adjust(left=.01,right=.99,bottom=.02,top=.98)
save(fig,'03-measurement-chain')

x=np.linspace(0,2,1601);sample=np.arange(0,2.01,.25)
a=1+.8*np.cos(2*np.pi*x);b=1+.8*np.cos(2*np.pi*3*x)
sa=1+.8*np.cos(2*np.pi*sample);sb=1+.8*np.cos(2*np.pi*3*sample)
alias_error=float(np.max(abs(sa-sb)));assert alias_error<1e-12
fig,axs=plt.subplots(2,1,figsize=(20,11))
fig.subplots_adjust(left=.075,right=.98,bottom=.16,top=.88,hspace=.39)
axs[0].plot(x,a,c=B,lw=3,label='1 RPO')
axs[0].plot(x,b,c=O,lw=2.6,ls='--',label='3 RPO')
axs[0].scatter(sample,sa,c='black',s=50,zorder=5,label='每八度 4 个等间距采样点')
axs[0].set(ylabel='相对功率密度',ylim=(0,2.6));axs[0].legend(fontsize=19,ncol=3,loc='upper right')
axs[0].set_title('（a）连续输入不同，采样点上的值却相同',pad=12,fontsize=25)
axs[1].plot(sample,sa,c=B,lw=3,marker='o',ms=9,label='1 RPO 的采样序列')
axs[1].plot(sample,sb,c=O,lw=2,ls='--',marker='x',ms=11,label='3 RPO 的采样序列')
axs[1].set(xlabel='对数频率 x / 八度（相对起点）',ylabel='采样值',ylim=(0,2.6))
axs[1].legend(fontsize=19,ncol=2,loc='upper right');axs[1].set_title('（b）相同采样输出，无法唯一还原纹波密度',pad=12,fontsize=25)
for ax in axs:ax.set(xticks=np.arange(0,2.01,.25),xlim=(0,2))
fig.text(.5,.95,'频谱采样混叠：成功辨别不一定意味着分辨了原始峰谷',ha='center',fontsize=27)
fig.text(.5,.045,'仅演示理想点采样：实际处理器还包括频带积分、压缩、选择与电刺激，不使用此图定义设备上限',ha='center',fontsize=19,color=G)
save(fig,'04-spectral-aliasing')
report={'model':'stipulated log-frequency Gaussian power-density smoothing; no human or device data','smoothing':verification,'aliasing':{'samples_per_octave':4,'input_rpo':[1,3],'maximum_sample_difference':alias_error},'figures':sizes}
(OUT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
