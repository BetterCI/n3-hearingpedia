"""Original analytic teaching figures; no recorded neuronal or listener data."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/lloyd-jeffress'
RESEARCH=ROOT/'docs/research/lloyd-jeffress-2026-10-10'
for p in [OUT,RESEARCH]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':13,'svg.fonttype':'path'})
BLUE,ORANGE,GREEN,GRAY='#276582','#af6435','#39846b','#526472'
records=[]

def save(fig,name,params):
    for ext in ['svg','png']:
        p=OUT/(name+'.'+ext);fig.savefig(p,dpi=100,facecolor='white')
        if ext=='svg':p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)
    records.append({'name':name,'width':1280,'height':650,'parameters':params,'nature':'original analytic teaching figure; not measured data or fitted neuronal model'})

def pair(title,subtitle):
    fig,axs=plt.subplots(1,2,figsize=(12.8,6.5))
    fig.subplots_adjust(left=.085,right=.97,bottom=.20,top=.73,wspace=.30)
    fig.suptitle(title,fontsize=23,fontweight='bold',y=.96)
    fig.text(.5,.86,subtitle,ha='center',fontsize=14,color=GRAY)
    for ax in axs:
        ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.16)
    return fig,axs

fig,ax=plt.subplots(figsize=(12.8,6.5));ax.set(xlim=(0,1280),ylim=(0,650));ax.axis('off')
ax.text(640,612,'时间差怎样变成可读出的活动？',ha='center',fontsize=23,fontweight='bold')
ax.text(640,560,'功能框架：延迟、符合检测与编码，需要不同证据',ha='center',fontsize=15,color=GRAY)
def box(x,y,w,h,text,color=BLUE,size=15):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=12',facecolor='#f3f7fa',edgecolor=color,lw=1.7))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,color=color)
def arrow(x1,y1,x2,y2,color=GRAY):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'->','color':color,'lw':2})
box(30,380,180,85,'左耳时序输入',BLUE);box(30,255,180,85,'右耳时序输入',ORANGE)
box(295,370,215,105,'左侧内部延迟\ndL1、dL2、…',BLUE)
box(295,245,215,105,'右侧内部延迟\ndR1、dR2、…',ORANGE)
arrow(210,422,290,422,BLUE);arrow(210,297,290,297,ORANGE)
box(620,295,245,125,'符合检测阵列\n输入接近同时到达\n→ 较强反应',GREEN)
arrow(510,422,614,385,BLUE);arrow(510,297,614,335,ORANGE)
box(970,295,275,125,'输出读出\n经典：哪个单元最活跃\n后续：比较群体活动',BLUE,14)
arrow(865,358,965,358)
for x,w,t in [(275,260,'延迟证据\n路径与传导时序'),(595,295,'检测证据\n单耳输入与双耳输出'),(950,300,'编码证据\n调谐排列与行为预测')]:box(x,100,w,100,t,GRAY,14)
ax.text(640,40,'框与箭头表示计算关系；没有指定真实轴突形态、脑区或解剖比例',ha='center',fontsize=12,color=GRAY)
fig.subplots_adjust(0,0,1,1)
save(fig,'computational-framework',{'boxes':'functional input-delay-coincidence-readout; no anatomy'})

dl=np.arange(7)*100;dr=600-dl;D=dl-dr;tau=200
arrl=dl;arrr=tau+dr;response=np.exp(-.5*((D-tau)/80)**2)
assert (D==tau).sum()==1 and arrl[4]==arrr[4]==400
fig,axs=pair('内部延迟补偿外部时间差','左耳0 µs、右耳200 µs；七个单元使用不同补偿差值')
ax=axs[0];ax.plot(D,arrl,'o-',color=BLUE,label='左输入到达');ax.plot(D,arrr,'s-',color=ORANGE,label='右输入到达')
ax.scatter([200],[400],s=190,facecolors='none',edgecolors=GREEN,lw=2.5,zorder=4)
ax.annotate('单元5：两侧均为400 µs',xy=(200,400),xytext=(-570,85),arrowprops={'arrowstyle':'->','color':GREEN},color=GREEN,fontsize=12)
ax.set(xlim=(-650,650),ylim=(-30,850),xticks=D,xlabel='内部差值 D = dL − dR（µs）',ylabel='到达单元的时刻（µs）',title='（a）比较到达时刻');ax.legend(loc='upper left',fontsize=11)
ax=axs[1];ax.plot(D,response,'o-',color=GREEN);ax.axvline(200,color=GRAY,ls='--',lw=1)
ax.set(xlim=(-650,650),ylim=(-.05,1.15),xticks=D,xlabel='内部差值 D（µs）',ylabel='归一化教学响应',title='（b）时间匹配的示例输出')
ax.text(-580,.84,'响应 = exp[−(D − 200)² / (2 × 80²)]',fontsize=11,color=GRAY)
fig.text(.5,.055,'内部延迟与80 µs宽度均为教学设定；线辅助阅读，不是实测放电率或听觉阈值',ha='center',fontsize=12,color=GRAY)
save(fig,'delay-compensation',{'external_arrival_us':[0,200],'left_delay_us':dl.tolist(),'right_delay_us':dr.tolist(),'internal_difference_us':D.tolist(),'gaussian_sigma_us':80,'response':response.tolist()})

d=np.linspace(-4500,4500,4501)
fig,axs=pair('周期性输入会产生多个匹配峰','两例的匹配中心均为200 µs；宽扫描范围用来展示歧义')
for ax in axs:
    ax.set(xlim=(-4500,4500),ylim=(-1.12,1.28),xticks=[-4000,-2000,0,2000,4000],xlabel='补偿量 D（µs）',ylabel='归一化相关')
    ax.axvline(200,color=GRAY,ls='--',lw=1)
axs[0].plot(d,np.cos(2*np.pi*500*(d-200)*1e-6),color=BLUE,lw=2)
axs[0].set_title('（a）500 Hz纯音的解析相关')
peaks=np.array([-3800,-1800,200,2200,4200]);axs[0].scatter(peaks,np.ones(5),s=30,color=BLUE)
axs[0].annotate('',xy=(2200,1.15),xytext=(200,1.15),arrowprops={'arrowstyle':'<->','color':BLUE})
axs[0].text(1200,.84,'峰间隔2000 µs',ha='center',fontsize=11,color=BLUE)
axs[1].plot(d,np.exp(-.5*((d-200)/120)**2),color=GREEN,lw=2);axs[1].set_title('（b）非周期高斯相关核示例')
axs[1].text(-3700,.75,'仅作解析教学类比\n宽度参数120 µs',fontsize=12,color=GRAY)
fig.text(.5,.055,'高斯核不是随机白噪声的实测相关；两图均未运行听觉模型或采用神经数据',ha='center',fontsize=12,color=GRAY)
save(fig,'correlation-ambiguity',{'delay_range_us':[-4500,4500],'true_delay_us':200,'tone_hz':500,'period_us':2000,'analytic_gaussian_sigma_us':120})

tauvals=np.linspace(-600,600,1201)
fig,axs=pair('位置编码与群体读出：比较不同的活动关系','同样对ITD敏感，不必使用同一种输出解释')
for ax in axs:ax.set(xlim=(-620,620),ylim=(-.04,1.1),xticks=[-600,-400,-200,0,200,400,600],xlabel='输入ITD τ（µs；正值为左耳先到）',ylabel='归一化教学响应')
colors=['#aac4cf','#83acbd','#5f91a9',BLUE,'#bc916a',ORANGE,'#855534']
for c,col in zip(np.arange(-600,601,200),colors):axs[0].plot(tauvals,np.exp(-.5*((tauvals-c)/120)**2),color=col,lw=1.8)
axs[0].set_title('（a）不同单元具有不同峰值ITD')
a=1/(1+np.exp(-tauvals/180));axs[1].plot(tauvals,a,color=BLUE,lw=2,label='通道A');axs[1].plot(tauvals,1-a,color=ORANGE,lw=2,label='通道B');axs[1].legend(fontsize=12,loc='upper left');axs[1].set_title('（b）两通道活动相反变化')
fig.text(.5,.055,'高斯宽度120 µs、logistic尺度180 µs均为教学设定；A/B不指定脑半球，未拟合行为',ha='center',fontsize=12,color=GRAY)
save(fig,'readout-strategies',{'place_centers_us':list(range(-600,601,200)),'place_sigma_us':120,'opponent_scale_us':180,'input_itd_us':[-600,600],'channels':'A,B not assigned to hemispheres'})
(RESEARCH/'figure-parameters.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':len(records),'outputs':str(OUT)}))
