"""Original functional and arithmetic teaching figures, not paper data or a codec reproduction."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/james-l-flanagan'
R=ROOT/'docs/research/james-l-flanagan-2026-10-10'
for p in [OUT,R]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':13,'svg.fonttype':'path'})
BLUE,ORANGE,GREEN,GRAY='#276582','#af6435','#39846b','#526472'
records=[]

def save(fig,name,parameters):
    for ext in ['svg','png']:
        p=OUT/(name+'.'+ext);fig.savefig(p,dpi=100,facecolor='white')
        if ext=='svg':p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)
    records.append({'name':name,'width':1280,'height':650,'parameters':parameters,'nature':'original functional or exact arithmetic teaching figure; not measured data'})

def canvas(title,subtitle):
    fig,ax=plt.subplots(figsize=(12.8,6.5));fig.subplots_adjust(0,0,1,1)
    ax.set(xlim=(0,1280),ylim=(0,650));ax.axis('off')
    ax.text(640,610,title,ha='center',fontsize=23,fontweight='bold')
    ax.text(640,562,subtitle,ha='center',fontsize=14,color=GRAY)
    return fig,ax

def box(ax,x,y,w,h,t,color=BLUE,size=14):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',facecolor='#f3f7fa',edgecolor=color,lw=1.6))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=size,color=color)

def arrow(ax,a,b,col=GRAY):ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.8,'color':col})

fig,ax=canvas('发声模型：分开描述与相互作用','近似线性表示便于分析；动力学模型进一步研究声源与声道耦合')
ax.text(55,495,'（a）近似稳定浊音：声源、声道和辐射',fontsize=17,color=BLUE)
top=[(55,200,'声门声源 G(f)\n重复周期与基频'),(350,230,'声道响应 H(f)\n共振峰与谱包络'),(675,205,'口端辐射 R(f)\n向外传播'),(975,250,'输出声音 S(f)\n近似频谱乘积')]
for x,w,t in top:box(ax,x,380,w,95,t)
for a,b in [(255,350),(580,675),(880,975)]:arrow(ax,(a+5,427),(b-8,427))
ax.text(55,290,'（b）双质量模型：状态、气流与声道反馈',fontsize=17,color=GREEN)
lower=[(55,205,'声门下压力\n驱动条件'),(350,340,'两个耦合振动状态\n与声门流相互作用'),(785,190,'声道模型\n传播与共振'),(1050,175,'口端声压\n计算输出')]
for x,w,t in lower:box(ax,x,155,w,100,t,GREEN)
for a,b in [(260,350),(690,785),(975,1050)]:arrow(ax,(a+5,205),(b-8,205),GREEN)
ax.plot([880,880,520],[155,105,105],color=GREEN,lw=1.8)
arrow(ax,(520,105),(520,150),GREEN)
ax.text(710,70,'声道压力反馈影响声源',ha='center',color=GREEN,fontsize=14)
ax.text(640,25,'功能归纳；不是解剖图，也没有实现原模型的流动、碰撞与差分方程',ha='center',fontsize=12,color=GRAY)
save(fig,'voice-framework',{'linear_approximation':'S(f) ≈ G(f) H(f) R(f)','dynamic_model':'coupled vibration and flow, tract feedback','not_anatomy':True,'not_model_simulation':True})

Fmin,Fmax=800.,2400.
def quantize(f,b):
    step=(Fmax-Fmin)/2**b
    return Fmin+(np.clip(np.floor((f-Fmin)/step),0,2**b-1)+.5)*step
f=np.linspace(Fmin,Fmax,12801)
fig=plt.figure(figsize=(12.8,6.5));fig.suptitle('共振峰参数：量化位数与频率误差',y=.96,fontsize=23,fontweight='bold')
fig.text(.5,.87,'范围800–2400 Hz；等宽区间、中点重建、没有范围外过载',ha='center',fontsize=14,color=GRAY)
a=fig.add_axes([.085,.19,.37,.58]);a.plot(f,f,'--',color=GRAY,lw=1,label='理想值')
bax=fig.add_axes([.585,.19,.37,.58])
for bits,col,style in [(4,ORANGE,'-'),(6,BLUE,'--')]:
    q=quantize(f,bits);a.plot(f,q,style,lw=1.7,color=col,label=f'{bits}位：{2**bits}个区间')
    bax.plot(f,q-f,style,lw=1.1,color=col,label=f'{bits}位误差')
    bound=(Fmax-Fmin)/(2**bits)/2
    assert np.max(np.abs(q-f))<=bound+1e-9
    bax.axhline(bound,color=col,ls=':',lw=1);bax.axhline(-bound,color=col,ls=':',lw=1)
for ax in [a,bax]:
    ax.set(xlim=(800,2400),xticks=[800,1200,1600,2000,2400],xlabel='输入F2（Hz）');ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15);ax.legend(fontsize=11)
a.set(ylim=(750,2450),ylabel='重建F2（Hz）',title='（a）重建值阶梯')
bax.set(ylim=(-62,62),yticks=[-50,-25,0,25,50],ylabel='重建减输入（Hz）',title='（b）误差与上界')
fig.text(.5,.045,'4位：步长100 Hz、上界50 Hz；6位：步长25 Hz、上界12.5 Hz；图中没有听觉阈值',ha='center',fontsize=12,color=GRAY)
save(fig,'formant-quantization',{'F2_range_Hz':[800,2400],'bits':[4,6],'reconstruction':'midpoint','boundary_rule':'lower inclusive, upper endpoint clipped to last cell','max_abs_error_Hz':[50,12.5],'not_perceptual_thresholds':True})

fs,N,k,Ha,Hs,truef=16000,1024,28,256,512,450.
fk=k*fs/N;expected=2*np.pi*k*Ha/N
residual=(2*np.pi*truef*Ha/fs-expected+np.pi)%(2*np.pi)-np.pi
estimate=fk+fs*residual/(2*np.pi*Ha)
assert np.isclose(fk,437.5) and np.isclose(residual,.4*np.pi) and np.isclose(estimate,450)
fig=plt.figure(figsize=(12.8,6.5));fig.suptitle('延长声音：保持时长以外的什么？',y=.96,fontsize=23,fontweight='bold')
fig.text(.5,.86,'450 Hz输入；437.5 Hz频点；16 ms分析步长 → 残差0.4π rad → 估计450 Hz',ha='center',fontsize=13,color=GRAY)
for y,duration,freq,label,col in [(.61,20,450,'原始：20 ms\n450 Hz',BLUE),(.385,40,225,'直接半速：40 ms\n225 Hz',ORANGE),(.16,40,450,'理想目标：40 ms\n450 Hz',GREEN)]:
    ax=fig.add_axes([.075,y,.73,.16]);t=np.arange(int(duration*fs/1000)+1)/fs
    ax.plot(t*1000,np.sin(2*np.pi*freq*t),color=col,lw=1.4)
    ax.set(xlim=(0,40),ylim=(-1.3,1.3),xticks=[0,10,20,30,40],yticks=[-1,0,1],ylabel='幅度（a.u.）');ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.12)
    if y==.16:ax.set_xlabel('时间（ms）')
    if duration==20:ax.axvspan(20,40,color='#f3f5f7');ax.text(30,.6,'无输入',ha='center',fontsize=12,color=GRAY)
    fig.text(.84,y+.08,label,color=col,va='center',fontsize=14)
fig.text(.5,.025,'解析正弦教学图；第三行是频率保持的目标，没有运行完整相位声码器',ha='center',fontsize=12,color=GRAY)
save(fig,'phase-time-scaling',{'sampling_rate_Hz':fs,'FFT_length':N,'bin_index':k,'bin_center_Hz':fk,'analysis_hop_samples':Ha,'synthesis_hop_samples':Hs,'input_frequency_Hz':truef,'phase_residual_rad':float(residual),'estimate_Hz':float(estimate),'waveforms':'analytic sinusoids only','not_full_phase_vocoder':True})

fig,ax=canvas('差分编码：两端必须拥有相同的重建历史','发送的是量化索引；预测与步长更新依靠双方可获得的信息')
ax.text(40,502,'编码端',fontsize=18,color=BLUE,fontweight='bold')
box(ax,40,345,130,95,'输入 x[n]')
box(ax,230,345,150,95,'减预测\n得到残差')
box(ax,435,345,205,95,'量化\n索引 / 量化残差')
box(ax,715,345,210,95,'本地重建\n预测 + 残差')
box(ax,1010,345,220,95,'重建与量化信息\n更新预测 / 步长',size=13)
for a,b in [(170,230),(380,435),(640,715),(925,1010)]:arrow(ax,(a+5,392),(b-8,392))
ax.text(620,286,'相同量化索引经信道送达',ha='center',fontsize=13,color=GRAY)
arrow(ax,(538,345),(538,241),GRAY)
ax.text(40,197,'接收端',fontsize=18,color=GREEN,fontweight='bold')
box(ax,435,105,205,95,'索引解码\n得到量化残差',GREEN)
box(ax,715,105,210,95,'接收端重建\n预测 + 残差',GREEN)
box(ax,1010,105,220,95,'相同状态更新\n预测器 / 步长',GREEN)
for a,b in [(640,715),(925,1010)]:arrow(ax,(a+5,153),(b-8,153),GREEN)
arrow(ax,(538,241),(538,205),GREEN)
# Feedback paths are routed away from the transport link and labels.
ax.plot([1120,1120,305,305],[440,475,475,443],color=BLUE,lw=1.7)
arrow(ax,(305,443),(305,439),BLUE)
for x in [538,820]:arrow(ax,(x,475),(x,440),BLUE)
ax.text(710,486,'预测反馈到相减与重建；步长反馈到量化器',ha='center',fontsize=12,color=BLUE)
ax.plot([1120,1120,538],[105,65,65],color=GREEN,lw=1.7)
for x in [538,820]:arrow(ax,(x,65),(x,105),GREEN)
ax.text(847,37,'步长反馈到解码；预测反馈到重建',ha='center',fontsize=12,color=GREEN)
ax.text(215,80,'一致性条件：相同初始状态\n相同运算与更新规则、无误码',ha='center',fontsize=12,color=GRAY)
save(fig,'adpcm-loop',{'functional_overview_only':True,'not_G726_implementation':True,'synchronization':['same initialization','same reconstructed history','same arithmetic and adaptation','error-free indices'],'arithmetic_example':{'input':.70,'prediction':.60,'quantized_residual':.09,'reconstruction':.69,'error':.01}})

tau=.04*np.sin(np.pi/6)/343
assert np.isclose(tau*1e6,58.3090379009) and np.isclose(tau*16000,.9329446064)
(R/'figure-parameters.json').write_text(json.dumps({'figures':records,'other_body_arithmetic':{'array_delay_us':tau*1e6,'array_delay_samples_16k':tau*16000,'raw_bitrate_8k_8bits':64000,'raw_bitrate_8k_4bits':32000}},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Generated and arithmetically checked four original SVG/PNG figures.')
