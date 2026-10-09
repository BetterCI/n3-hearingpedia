"""Reproducible original teaching figures. No participant recordings or outcomes."""
from pathlib import Path
import json, re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'public/figures/phonetics'
RECORD = ROOT/'docs/research/phonetics-2026-10-09'
OUT.mkdir(parents=True, exist_ok=True); RECORD.mkdir(parents=True, exist_ok=True)
FONT = FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':FONT.get_name(),'font.size':23,'axes.unicode_minus':False,
    'svg.fonttype':'path','svg.hashsalt':'phonetics-2026-10-09','figure.facecolor':'white',
    'savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
BLUE='#24678d'; GREEN='#39775a'; ORANGE='#b3652d'; INK='#263944'; GRAY='#65747d'; PALE='#eaf2f6'
manifest=[]

def canvas(height=840):
    fig=plt.figure(figsize=(1200/72,height/72)); ax=fig.add_axes([.02,.025,.96,.95])
    ax.set_xlim(0,12); ax.set_ylim(0,height/100); ax.axis('off'); return fig,ax

def box(ax,x,y,text,w=3.3,h=1.3,color=BLUE,size=25):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.06',
        lw=2,facecolor=PALE,edgecolor=color))
    ax.text(x,y,text,ha='center',va='center',fontsize=size,color=INK)

def arrow(ax,a,b,color=BLUE):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=24,lw=2.4,color=color))

def save(fig,name,description,parameters):
    for ext in ('svg','png'):
        path=OUT/(name+'.'+ext)
        fig.savefig(path,dpi=90,metadata={'Date':None} if ext=='svg' else None)
        if ext=='svg':path.write_text('\n'.join(x.rstrip() for x in path.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
    svg=(OUT/(name+'.svg')).read_text(encoding='utf8')
    manifest.append({'name':name,'files':[name+'.svg',name+'.png'],
        'svg_viewbox':[float(x) for x in re.search(r'viewBox="([^"]+)"',svg).group(1).split()],
        'description':description,'parameters':parameters,'empirical_data':False,
        'generator':'scripts/generate-phonetics.py','attribution':'n³ Hearingpedia；AI 辅助编写与绘图',
        'copyright':'原创教学图；未转载论文图形或参与者数据',
        'usage':'本站展示与教学计算复现；对外开放许可证尚待维护者确定'})
    plt.close(fig)

fig,ax=canvas()
ax.text(.2,7.8,'语音学：连接发音、声学信号与感知',fontsize=31,weight='bold',color=INK)
for x,title,measure in [(2,'发音动作\n气流、声带、声道','器官记录\n位置、接触、轮廓'),
                        (6,'声学信号\n周期、频谱、时序','信号分析\nHz、ms、谱量'),
                        (10,'感知判断\n类别、词与线索','行为任务\n比例、阈值、反应时')]:
    box(ax,x,6.15,title)
    ax.text(x,3.75,measure,ha='center',va='center',fontsize=25,color=INK)
    arrow(ax,(x,5.43),(x,4.45),GREEN)
arrow(ax,(3.75,6.15),(4.25,6.15));arrow(ax,(7.75,6.15),(8.25,6.15))
ax.plot([10,10,2,2],[2.7,2.25,2.25,2.7],color=ORANGE,lw=2)
arrow(ax,(2,2.7),(2,3.05),ORANGE)
ax.text(6,1.65,'说话人也可听到自身语音，获得反馈',ha='center',fontsize=26,color=ORANGE)
ax.text(6,.65,'语言经验与语境影响产生和理解；箭头不表示独立神经模块',ha='center',fontsize=24,color=GRAY)
save(fig,'01-production-signal-perception','三种研究入口和简化自身语音反馈；非解剖图。',{'data':None})

FS=16000; F0=125; duration=1.; centers=[500,1500,2500]; bandwidths=[80,120,180]
r=np.exp(-np.pi*np.array(bandwidths)/FS); omega=2*np.pi*np.array(centers)/FS
def response(f):
    z=np.exp(-2j*np.pi*np.asarray(f)/FS)
    return np.prod(1/(1-2*r[:,None]*np.cos(omega[:,None])*z+r[:,None]**2*z**2),axis=0)
f=np.linspace(0,4000,4097); H=response(f)
harmonics=np.arange(1,int((FS/2-1)//F0)+1); fh=harmonics*F0
source=1/harmonics; filtered=source*response(fh)
t=np.arange(int(FS*duration))/FS
x=np.imag(np.exp(2j*np.pi*t[:,None]*fh)*filtered).sum(axis=1)
x/=np.max(np.abs(x))
assert FS/F0==128
assert np.allclose(x[:-128],x[128:],atol=2e-12)
def db(a):return 20*np.log10(np.maximum(np.abs(a)/np.max(np.abs(a)),1e-6))

fig=plt.figure(figsize=(1200/72,1000/72))
fig.text(.065,.95,'声源 × 声道滤波器 → 输出幅度谱',fontsize=31,weight='bold',color=INK)
for i,(title,color) in enumerate([('（a）周期声源：谐波间距 125 Hz',BLUE),
                                 ('（b）三个离散共振器：设计频率与带宽',GREEN),
                                 ('（c）输出：谐波受滤波器加权',ORANGE)]):
    ax=fig.add_axes([.12,.70-i*.27,.82,.17])
    if i==1:
        ax.plot(f,db(H),color=color,lw=2.4)
        for freq,bw in zip(centers,bandwidths):
            ax.axvline(freq,color=GRAY,lw=1,ls='--');ax.text(freq,-47,f'{freq}\n({bw})',ha='center',fontsize=19,color=INK)
    else:
        y=db(source if i==0 else filtered)
        ax.vlines(fh,-60,y,color=color,lw=1.8)
    ax.set_xlim(0,4000);ax.set_ylim(-60,4);ax.set_yticks([-60,-30,0]);ax.set_title(title,loc='left',fontsize=25,pad=13)
    ax.set_ylabel('相对幅度（dB）',fontsize=21)
    if i==2:ax.set_xlabel('频率（Hz）',fontsize=23)
    else:ax.set_xticklabels([])
fig.text(.5,.042,'每个面板以自身最大幅度为 0 dB；非声压级，非真实元音录音',ha='center',fontsize=22,color=GRAY)
save(fig,'02-source-filter','独立源滤波教学模型；各面板自身幅度归一化。',{
    'sample_rate_Hz':FS,'F0_Hz':F0,'harmonics':len(harmonics),'source_amplitude':'1/k',
    'resonator_centers_Hz':centers,'bandwidth_parameters_Hz':bandwidths,
    'pole_radius':'exp(-pi*bandwidth/fs)','transfer':'product of 1/(1-2*r*cos(2*pi*center/fs)*z^-1+r^2*z^-2)',
    'output':'steady-state harmonic synthesis using complex transfer; peak normalized',
    'plot_limit_Hz':4000,'panel_reference':'each panel own maximum amplitude'})

def stft(N):
    w=.5-.5*np.cos(2*np.pi*np.arange(N)/N)
    # All windows lie in the interior of a stationary 1-second signal.
    mid=np.arange(int(.4*FS),int(.6*FS)+1,16)
    frames=np.stack([x[c-N//2:c+N//2]*w for c in mid])
    amp=np.abs(np.fft.rfft(frames,n=4096,axis=1))/w.sum()
    enbw=FS*np.sum(w*w)/w.sum()**2
    return mid/FS-.4,amp,enbw
ts,A,b1=stft(80);_,B,b2=stft(640)
assert np.isclose(b1,300) and np.isclose(b2,37.5)
freq=np.fft.rfftfreq(4096,1/FS); keep=freq<=4000
shared=max(A[:,keep].max(),B[:,keep].max())
fig=plt.figure(figsize=(1200/72,1100/72))
fig.text(.065,.95,'相同信号，不同窗长：频率网格不能代替分析带宽',fontsize=29,weight='bold',color=INK)
ax=fig.add_axes([.12,.74,.72,.13]);sel=t<.024
ax.plot(t[sel]*1000,x[sel],lw=1.8,color=BLUE);ax.set_xlim(0,24);ax.set_ylim(-1.1,1.1)
ax.set_ylabel('归一化幅度',fontsize=21);ax.set_xlabel('时间（ms）',fontsize=22)
ax.set_title('（a）周期 8 ms；一个周期有 128 个样本',loc='left',fontsize=25,pad=11)
for i,(amp,N,enbw) in enumerate([(A,80,b1),(B,640,b2)]):
    ax=fig.add_axes([.12,.44-i*.29,.72,.17])
    val=20*np.log10(np.maximum(amp[:,keep]/shared,1e-8))
    pcm=ax.pcolormesh(ts*1000,freq[keep],val.T,shading='auto',cmap='viridis',vmin=-65,vmax=0,rasterized=True)
    ax.set_ylim(0,4000);ax.set_xlim(0,200);ax.set_ylabel('频率（Hz）',fontsize=21)
    ax.set_title(f'{"（b）" if i==0 else "（c）"}Hann 窗 {N/FS*1000:g} ms；等效噪声带宽 {enbw:g} Hz',loc='left',fontsize=24,pad=12)
    if i==1:ax.set_xlabel('局部时间（ms）',fontsize=22)
    else:ax.set_xticklabels([])
cax=fig.add_axes([.88,.17,.022,.42]);cb=fig.colorbar(pcm,cax=cax);cb.set_label('共用参考值的相对功率（dB）',fontsize=21,labelpad=12)
fig.text(.5,.049,'两图均使用 1 ms 帧移、4096 点 FFT；网格间距均为 3.90625 Hz',ha='center',fontsize=22,color=GRAY)
save(fig,'03-window-length','同一平稳信号的波形及两种周期Hann窗语谱图；共享颜色参考。',{
    'input':'same steady-state signal as figure 2','sample_rate_Hz':FS,'F0_Hz':F0,'period_samples':128,
    'window':'periodic Hann: .5-.5*cos(2*pi*n/N)','window_samples':[80,640],'window_ms':[5,40],
    'ENBW_Hz':[b1,b2],'ENBW_definition':'fs*sum(w^2)/sum(w)^2; not two-tone threshold or Gaussian -3 dB bandwidth',
    'frame_hop_samples':16,'frame_hop_ms':1,'FFT_points':4096,'frequency_grid_Hz':FS/4096,
    'normalization':'FFT amplitude divided by sum(window); shared maximum over both panels within 0-4000 Hz',
    'color_dB_range':[-65,0],'signal_section_seconds':[.4,.6],'display_time_ms':[0,200],
    'boundary_handling':'interior complete windows; no padding signal ends with silence; FFT zero padding only'})

fig,ax=canvas()
ax.text(.2,7.8,'起声时间：先规定事件，再计算差值',fontsize=31,weight='bold',color=INK)
start=2.25;end=11.15;scale=(end-start)/250;release=100
for y,onset in [(6.25,70),(4.55,120),(2.85,160)]:
    vot=onset-release; ax.text(.1,y,f'VOT = {vot:+d} ms',fontsize=25,va='center',color=INK)
    ax.plot([start,end],[y,y],color='#c7d0d6',lw=4)
    ax.plot([start+onset*scale,end],[y,y],color=BLUE,lw=14,solid_capstyle='butt')
    a=start+onset*scale;b=start+release*scale
    ax.plot([a,a],[y-.2,y+.26],color=BLUE,lw=2);ax.plot([b,b],[y-.3,y+.45],color=ORANGE,lw=2)
    ax.text(a,y-.55,f'起声 {onset} ms',ha='center',color=BLUE,fontsize=21)
    ax.annotate('',xy=(a,y+.62),xytext=(b,y+.62),arrowprops={'arrowstyle':'<->','color':GREEN,'lw':2})
ax.text(start+release*scale,7.15,'共同释放：100 ms',ha='center',color=ORANGE,fontsize=25)
for ms in [0,50,100,150,200,250]:
    xx=start+ms*scale;ax.text(xx,1.7,str(ms),ha='center',fontsize=21,color=GRAY)
ax.text(6.8,1.15,'共同时间基准（ms）',ha='center',fontsize=23,color=GRAY)
ax.text(6,.45,'蓝条：指定的连续周期振动；非录音波形，非跨语言分类阈值',ha='center',fontsize=24,color=GRAY)
save(fig,'04-vot-timing','事件时间条；假定起声后连续周期振动；数值不对应特定语言类别。',
    {'release_ms':100,'voicing_onsets_ms':[70,120,160],'VOT_ms':[-30,20,60],
     'assumption':'voicing continuous from designated onset; no interruption or multiple releases','data':None})

(OUT/'parameters.json').write_text(json.dumps({'date':'2026-10-09','figures':manifest},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(RECORD/'figure-verification.json').write_text(json.dumps({'date':'2026-10-09','passed':True,
    'assertions':['steady-state period is 128 samples at 125 Hz / 16 kHz','periodic Hann ENBW is 300 / 37.5 Hz',
                  'FFT grid is 3.90625 Hz in both panels','VOT differences are -30 / 20 / 60 ms'],
    'figures':manifest},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Generated 4 original figures, SVG + PNG, with reproducible parameters and numerical checks.')
