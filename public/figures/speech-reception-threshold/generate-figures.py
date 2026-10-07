"""Original SRT teaching figures. All curves, observations and listeners are synthetic.
Run with Python, NumPy and Matplotlib. No audio is generated or played.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent / 'figures'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':11,
                     'axes.unicode_minus':False,'svg.fonttype':'path'})
BLUE, RED, GREEN, GRAY = '#28658b', '#ad3f43', '#347765', '#60666a'
records = {}

def sigmoid(x, theta, scale, gamma=0, lapse=0):
    return gamma+(1-gamma-lapse)/(1+np.exp(-(x-theta)/scale))

def clean(ax):
    ax.spines[['top','right']].set_visible(False)
    ax.grid(color='#dce2e5',lw=.6,alpha=.7)

def save(fig, name):
    fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',facecolor='white')
    fig.savefig(OUT/(name+'.png'),dpi=170,bbox_inches='tight',facecolor='white')
    plt.close(fig)

# 1. Detection is not recognition; a low maximum may prevent a 50% threshold.
fig,axs=plt.subplots(1,2,figsize=(11.7,4.6))
level=np.linspace(0,70,400)
ax=axs[0]
ax.plot(level,sigmoid(level,18,3.7)*100,c=GREEN,lw=2,label='报告有声音：检测任务')
ax.plot(level,sigmoid(level,28,4.2)*100,c=BLUE,lw=2,label='辨认内容：识别任务')
ax.axhline(50,c=GRAY,ls='--',lw=.9)
for threshold,c in [(18,GREEN),(28,BLUE)]:
    ax.vlines(threshold,0,50,color=c,ls=':',lw=1.1)
    ax.plot(threshold,50,'o',c=c)
ax.text(16,7,'检测阈\n18',ha='right',fontsize=10,color=GREEN)
ax.text(30,7,'接收阈\n28',ha='left',fontsize=10,color=BLUE)
ax.legend(frameon=False,fontsize=10,loc='lower right')
ax.set(xlim=(0,70),ylim=(0,105),xlabel='呈现听力级（dB HL）',ylabel='反应比例（%）',title='A  任务不同，阈值不同')
ax=axs[1];upper=.4
ax.plot(level,upper*sigmoid(level,28,4.2)*100,c=RED,lw=2,label='识别曲线：上限低于 50%')
ax.axhline(50,c=GRAY,ls='--',lw=.9);ax.axhline(20,c=RED,ls=':',lw=.9)
ax.plot(28,20,'o',c=RED)
ax.text(34,23,'20% 是本图上限的一半\n不等于 50% 接收阈',fontsize=10,color=RED)
ax.text(8,54,'曲线未达到 50%，此目标阈值不能确定',fontsize=10,color=GRAY)
ax.set(xlim=(0,70),ylim=(0,105),xlabel='呈现听力级（dB HL）',ylabel='识别正确率（%）',title='B  不把半最高分改称为 50% 接收阈')
for ax in axs:clean(ax)
fig.text(.08,.005,'所有参数为教学构造；检测阈与接收阈的差值不是固定常数。右图不描述增加声级的临床建议。',fontsize=9,color=GRAY)
fig.subplots_adjust(bottom=.2,wspace=.25)
save(fig,'01-detection-recognition-and-ceiling')
records['figure1']={'detection50_HL':18,'recognition50_HL':28,'limited_maximum':.4,'half_maximum':.2}

# 2. Threshold differences do not imply a constant change in percentage score.
fig,axs=plt.subplots(1,2,figsize=(11.7,4.6))
x=np.linspace(-15,6,450);theta=-6
ax=axs[0]
for scale,label,c in [(1,'曲线甲：较陡',BLUE),(2.8,'曲线乙：较缓',GREEN)]:
    ax.plot(x,sigmoid(x,theta,scale)*100,label=label,c=c,lw=2)
ax.axhline(50,c=GRAY,ls='--',lw=.9);ax.axvline(theta,c=GRAY,ls=':',lw=.9)
ax.text(-14,68,'同为 −6 dB SNR\n高正确率区间表现不同',fontsize=9)
ax.legend(frameon=False,loc='lower right',fontsize=10)
ax.set(xlim=(-15,6),ylim=(0,105),xlabel='信噪比（dB SNR）',ylabel='识别正确率（%）',title='A  相同接收阈，不同曲线斜率')
gamma,lapse,scale=.1,.05,1.8
q=(.5-gamma)/(1-gamma-lapse)
x50=theta+scale*np.log(q/(1-q))
ax=axs[1];ax.plot(x,sigmoid(x,theta,scale,gamma,lapse)*100,c=BLUE,lw=2)
ax.axhline(50,c=GRAY,ls='--',lw=.9);ax.axhline(gamma*100,c=GREEN,ls=':',lw=.9);ax.axhline((1-lapse)*100,c=RED,ls=':',lw=.9)
ax.vlines(x50,0,50,color=BLUE,ls=':',lw=1);ax.plot(x50,50,'o',c=BLUE)
ax.text(-14,15,'下渐近线 10%',fontsize=10,color=GREEN)
ax.text(-14,87,'上渐近线 95%',fontsize=10,color=RED)
ax.text(-3.5,38,f'原始 50% 点 ≈ {x50:.2f}\n曲线位置参数为 −6',fontsize=10,color=BLUE)
ax.set(xlim=(-15,6),ylim=(0,105),xlabel='信噪比（dB SNR）',ylabel='识别正确率（%）',title='B  猜测与失误改变参数的解释')
for ax in axs:clean(ax)
fig.text(.08,.005,'教学函数，不是任何测试的常模。右图 10% 下渐近线为假设值，不由某种实际材料的选项数推出。',fontsize=9,color=GRAY)
fig.subplots_adjust(bottom=.2,wspace=.25)
save(fig,'02-threshold-slope-and-asymptotes')
records['figure2']={'theta':theta,'gamma':gamma,'lapse':lapse,'scale':scale,'raw50_SNR':float(x50)}

# 3. Deterministic replay of recorded decisions, not an estimate from simulated listeners.
correct=np.array([1,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,0,1,0,1,1,0,0,1],dtype=bool)
levels=[0.]
for response in correct[:-1]:levels.append(levels[-1]+(-2 if response else 2))
levels=np.array(levels);trials=np.arange(1,len(levels)+1)
formal_mean=float(levels[4:].mean())
fig,axs=plt.subplots(1,2,figsize=(12,4.6),gridspec_kw={'width_ratios':[1.65,1]})
ax=axs[0];ax.plot(trials,levels,c=GRAY,lw=1)
ax.scatter(trials[correct],levels[correct],s=45,c=BLUE,zorder=3,label='正确：下一次降低信噪比')
ax.scatter(trials[~correct],levels[~correct],s=45,facecolors='white',edgecolors=BLUE,zorder=3,label='错误：下一次提高信噪比')
ax.axvspan(.5,4.5,color='#eaf0f4',label='示例中排除的起始试次')
ax.hlines(formal_mean,4.5,24.5,color=RED,lw=1.2,ls='--')
ax.text(15,-1.0,f'后 20 次平均 = {formal_mean:.1f} dB SNR',color=RED,ha='center',fontsize=10)
ax.set(xlim=(.5,24.5),ylim=(-10,1.5),xlabel='刺激序号',ylabel='信噪比（dB SNR）',title='A  单次正确下降、单次错误上升的示例')
ax.legend(frameon=False,fontsize=9,loc='lower left');clean(ax)
ax=axs[1]
locations=np.array([0,1]);speech=np.array([57,60]);noise=np.array([65,65])
ax.bar(locations-.16,speech,width=.3,color=BLUE,label='言语')
ax.bar(locations+.16,noise,width=.3,color=GRAY,label='噪声')
for i,s,n in zip(locations,speech,noise):
    ax.text(i-.16,s+1,str(s),ha='center',fontsize=10)
    ax.text(i+.16,n+1,str(n),ha='center',fontsize=10)
    ax.text(i,24,f'{s} − {n}\n= {s-n} dB SNR',ha='center',fontsize=9,color=RED,
            bbox={'facecolor':'white','edgecolor':'#dce2e5','boxstyle':'square,pad=.4'})
ax.set(xticks=locations,xticklabels=['条件甲','条件乙'],ylim=(0,82),ylabel='相同参考条件下的声压级（dB SPL）',title='B  负信噪比的量值含义')
ax.legend(frameon=False,fontsize=9,loc='upper right');clean(ax)
fig.text(.08,.005,'左图反应人工指定，步长为 2 dB，只演示规则与计算；不是任何临床测试的正式流程。右图数值与左图无配对关系。',fontsize=9,color=GRAY)
fig.subplots_adjust(bottom=.2,wspace=.27)
save(fig,'03-adaptive-search-and-snr')
records['figure3']={'levels_SNR':levels.tolist(),'correct':correct.astype(int).tolist(),'mean_last20_SNR':formal_mean,'step_dB':2,'SPL_examples':[[57,65,-8],[60,65,-5]]}

# 4. In a deliberately independent-word toy model, scoring changes the 50% criterion.
fig,axs=plt.subplots(1,2,figsize=(11.7,4.6));x=np.linspace(-15,6,450)
word=sigmoid(x,-6,1.8);whole=word**5
p_for_whole=.5**.2
snr_whole=-6+1.8*np.log(p_for_whole/(1-p_for_whole))
ax=axs[0];ax.plot(x,word*100,c=BLUE,lw=2,label='逐关键词正确率')
ax.plot(x,whole*100,c=RED,lw=2,label='五关键词全部正确的句子比例')
ax.axhline(50,c=GRAY,ls='--',lw=.9)
ax.plot([-6,snr_whole],[50,50],'o',c=GRAY)
ax.set(xlim=(-15,6),ylim=(0,105),xlabel='信噪比（dB SNR）',ylabel='按相应单位计分的正确率（%）',title='A  同一底层假设，不同评分得到不同阈值')
ax.legend(frameon=False,fontsize=9,loc='upper left');clean(ax)
ax=axs[1];p=np.linspace(0,1,301)
ax.plot(p*100,p**5*100,c=RED,lw=2)
ax.plot([50,p_for_whole*100],[100*.5**5,50],'o',c=RED)
ax.annotate('逐词 50% → 整句约 3.1%',xy=(50,100*.5**5),xytext=(5,24),fontsize=10,arrowprops={'arrowstyle':'->','color':GRAY})
ax.annotate('整句 50% → 逐词约 87.1%',xy=(p_for_whole*100,50),xytext=(5,64),fontsize=10,arrowprops={'arrowstyle':'->','color':GRAY})
ax.set(xlim=(0,100),ylim=(0,105),xlabel='单个关键词的正确概率（%）',ylabel='五个关键词全部正确的概率（%）',title='B  独立、等概率假设下的数学关系')
clean(ax)
fig.text(.08,.005,'仅为数学示意：假设五个关键词等难且相互独立，整句正确概率为 p⁵。真实句子受语境及相关性影响，不能按此换算。',fontsize=9,color=GRAY)
fig.subplots_adjust(bottom=.2,wspace=.25)
save(fig,'04-word-versus-sentence-scoring')
records['figure4']={'assumed_independent_keywords':5,'whole_at_word50':.5**5,'word_at_whole50':p_for_whole,'word50_SNR':-6,'whole50_SNR':float(snr_whole)}

# 5. Pairwise differences and group means answer different questions.
a=np.array([-4,-6,-3,-7,-5,-2,-8,-4]);benefit=np.array([3,2,-1,4,1,0,2,5]);b=a-benefit
fig,axs=plt.subplots(1,2,figsize=(11.7,4.9));y=np.arange(1,9)
ax=axs[0]
for i,ai,bi in zip(y,a,b):ax.plot([ai,bi],[i,i],c='#bac4ca',lw=1.5)
ax.scatter(a,y,c=BLUE,s=45,label='条件 A');ax.scatter(b,y,c=GREEN,s=45,marker='s',label='条件 B')
ax.set(yticks=y,yticklabels=[f'听者 {i}' for i in y],ylim=(8.7,.3),xlim=(-13,.5),xlabel='同一测试的 SRT（dB SNR）',title='A  保留每位听者的配对结果')
ax.legend(frameon=False,loc='upper left',fontsize=10);clean(ax)
ax=axs[1]
for i,d in zip(y,benefit):ax.plot([0,d],[i,i],c=GREEN if d>=0 else RED,lw=1.5)
ax.scatter(benefit,y,c=[GREEN if d>=0 else RED for d in benefit],s=45)
ax.axvline(0,c=GRAY,lw=.9);ax.axvline(benefit.mean(),c=BLUE,ls='--',lw=1)
ax.text(2.25,8.4,f'组平均改善 {benefit.mean():.1f} dB',fontsize=10,color=BLUE)
ax.set(yticks=y,yticklabels=[],ylim=(8.7,.3),xlim=(-2,6),xlabel='改善 = SRT_A − SRT_B（dB）',title='B  平均改善不等于所有人均改善')
clean(ax)
fig.text(.08,.005,'人工构造的八组配对值；未提供复测或置信区间，不代表统计显著、临床获益或真实设备效能。',fontsize=9,color=GRAY)
fig.subplots_adjust(bottom=.2,wspace=.25)
save(fig,'05-paired-srt-differences')
records['figure5']={'A_SNR':a.tolist(),'B_SNR':b.tolist(),'benefit_dB':benefit.tolist(),'mean_benefit_dB':float(benefit.mean())}
(OUT.parent/'figure-verification.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf8')
print('Generated 5 SVG and 5 PNG teaching figures.')
