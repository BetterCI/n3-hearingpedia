"""Reproducible teaching figures; all thresholds and response sequences are synthetic.
Run: python generate-figures.py. No audio output or clinical measurement is performed.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, FancyArrowPatch

OUT = Path(__file__).resolve().parent / 'figures'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':11,
    'axes.unicode_minus':False,'svg.fonttype':'path','savefig.facecolor':'white'})
RED, BLUE, GREEN, GRAY = '#ad3f43', '#28658b', '#347765', '#60666a'
F = np.array([250,500,1000,2000,4000,8000])
saved=[]

def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),bbox_inches='tight')
    fig.savefig(OUT/(name+'.png'),dpi=170,bbox_inches='tight')
    saved.append(name)
    plt.close(fig)

def audiogram(ax, ymax=100):
    ax.set_xscale('log',base=2)
    ax.set_xlim(220,9200); ax.set_ylim(ymax,-10)
    ax.set_xticks(F);ax.set_xticklabels([str(f) for f in F])
    ax.set_yticks(np.arange(-10,ymax+1,10))
    ax.set_xlabel('频率（Hz）');ax.set_ylabel('听力级（dB HL）')
    ax.grid(color='#dbe0e3',lw=.65)
    ax.tick_params(axis='x',labelsize=9)
    ax.spines[['top','right']].set_visible(False)

# 1. Ear-specific conventional symbols and an explicit no-response ceiling.
fig,(ax,symbols)=plt.subplots(1,2,figsize=(11.5,5.2),gridspec_kw={'width_ratios':[1.65,1]})
audiogram(ax,110)
right=np.array([15,20,25,35,50,65]);left=np.array([20,25,30,45,65,85])
ax.plot(F,right,'o-',c=RED,mfc='white',ms=8,lw=1.4,label='右耳气导，未掩蔽：O')
ax.plot(F,left,'x--',c=BLUE,ms=8,mew=1.6,lw=1.3,label='左耳气导，未掩蔽：X')
for f,r,l in zip(F[1:5],right[1:5]-5,left[1:5]-5):
    ax.text(f*.96,r,'[',ha='center',va='center',color=RED,fontsize=17)
    ax.text(f*1.04,l,']',ha='center',va='center',color=BLUE,fontsize=17)
ax.legend(loc='upper left',fontsize=10,frameon=False)
ax.set_title('A  听力图：听力级向下增大',pad=14)
symbols.set(xlim=(0,10),ylim=(0,10));symbols.axis('off');symbols.set_title('B  符号与无反应记录',pad=14)
for y,s1,s2,label in [(8.4,'O','X','气导，未掩蔽'),(7.2,'△','□','气导，掩蔽'),
                      (6.0,'<','>','骨导，未掩蔽'),(4.8,'[',']','骨导，掩蔽')]:
    symbols.text(.7,y,s1,color=RED,fontsize=17,ha='center',va='center')
    symbols.text(2,y,s2,color=BLUE,fontsize=17,ha='center',va='center')
    symbols.text(3.1,y,label,fontsize=10,va='center')
symbols.text(.7,9.35,'右耳',ha='center',fontsize=9,color=RED)
symbols.text(2,9.35,'左耳',ha='center',fontsize=9,color=BLUE)
symbols.text(.2,3.15,'独立记录示例：100 dB HL 无反应',fontsize=10,color=GRAY)
symbols.text(.7,2.2,'△',ha='center',va='center',color=RED,fontsize=18)
symbols.annotate('',xy=(.7,.8),xytext=(.7,2.05),arrowprops={'arrowstyle':'->','color':RED,'lw':1.3})
symbols.text(2,1.5,'箭头附于实际使用的符号\n听阈未在可用输出内确定',fontsize=10,color=GRAY,va='center')
fig.text(.12,.01,'方括号表示掩蔽骨导（右 [、左 ]）；图中骨导点横向错开仅为避免重叠。\n向下箭头表示在标示水平无反应，不代表该处已经测得听阈。所有数据为教学示例。',fontsize=9,color=GRAY)
fig.subplots_adjust(bottom=.23,wspace=.3)
save(fig,'01-audiogram-coordinates-and-symbols')

# 2. Probability threshold and the ascending-series decision rule are distinct.
fig,axs=plt.subplots(1,2,figsize=(11.5,4.6),gridspec_kw={'width_ratios':[1,1.45]})
level=np.linspace(10,50,300);prob=1/(1+np.exp(-(level-30)/3.5))
ax=axs[0];ax.plot(level,prob,c=BLUE,lw=2);ax.axhline(.5,c=GRAY,lw=.8,ls='--')
ax.axvline(30,c=GRAY,lw=.8,ls='--');ax.plot(30,.5,'o',c=BLUE)
ax.set(xlabel='呈现听力级（dB HL）',ylabel='报告听见的概率',ylim=(-.02,1.03),
       title='A  理想化的心理测量函数')
ax.text(31,.23,'50% 点为 30 dB HL',fontsize=9,color=BLUE);ax.grid(alpha=.15)
seq=np.array([50,40,30,20,25,30,20,25,30]);heard=seq>=30
ax=axs[1];trial=np.arange(1,len(seq)+1)
ax.plot(trial,seq,c=GRAY,lw=1)
ax.scatter(trial[heard],seq[heard],s=65,c=BLUE,zorder=3,label='有反应')
ax.scatter(trial[~heard],seq[~heard],s=65,c='white',edgecolor=BLUE,zorder=3,label='无反应')
ax.scatter([6,9],[30,30],s=145,facecolors='none',edgecolors=RED,lw=1.5,zorder=4)
ax.axhline(30,c=GRAY,ls='--',lw=.8)
ax.annotate('上升试次中两次\n在 30 dB HL 有反应',xy=(9,30),xytext=(6.6,46),
            fontsize=10,ha='center',arrowprops={'arrowstyle':'->','color':RED},color=RED)
ax.text(2,22,'熟悉后下降',ha='center',fontsize=9,color=GRAY)
ax.text(4.35,38,'无反应 +5 dB\n有反应 −10 dB',ha='center',fontsize=9,color=GRAY)
ax.set(xticks=trial,xlabel='刺激序号（时长与间隔未绘出）',ylabel='呈现听力级（dB HL）',
       ylim=(15,55),title='B  下降 10、上升 5 dB 的示例序列')
ax.legend(loc='upper left',fontsize=9,frameon=False)
fig.text(.09,.015,'示意数据：临床判定依据上升试次的重复反应；一次听见或一个转折点均不足以定义听阈。',fontsize=9,color=GRAY)
fig.subplots_adjust(wspace=.3,bottom=.21,top=.85)
save(fig,'02-threshold-probability-and-search')

# 3. All patterns use the same ear and masked symbols; no diagnostic cut-off zones.
fig,axs=plt.subplots(1,3,figsize=(12,4.8),sharey=True)
patterns=[('A  传导性模式',[40,40,45,40,45,40],[10,10,15,10,15]),
          ('B  感音神经性模式',[25,30,40,50,65,75],[25,30,40,50,65]),
          ('C  混合性模式',[55,60,65,70,80,85],[30,35,40,45,55])]
for ax,(title,ac,bc) in zip(axs,patterns):
    audiogram(ax);ax.set_title(title,fontsize=12)
    ax.plot(F,ac,'^-',c=RED,mfc='white',ms=7,lw=1.3)
    for f,h in zip(F[:5],bc):ax.text(f*.98,h,'[',fontsize=17,color=RED,ha='center',va='center')
    if title.startswith('A') or title.startswith('C'):
        ax.annotate('',xy=(1000,ac[2]),xytext=(1000,bc[2]),arrowprops={'arrowstyle':'<->','color':GRAY})
        ax.text(1250,(ac[2]+bc[2])/2,'气骨导差',fontsize=9,color=GRAY,va='center')
handles=[Line2D([],[],color=RED,marker='^',mfc='white',label='右耳掩蔽气导 △'),
         Line2D([],[],color=RED,marker='$[$',linestyle='none',ms=11,label='右耳掩蔽骨导 [')]
fig.legend(handles=handles,loc='lower center',bbox_to_anchor=(.5,.08),ncol=2,frameon=False,fontsize=10)
fig.text(.11,.015,'人工构造的阈值模式；骨导只绘至 4000 Hz。形状与气骨导差提供线索，不能单凭图形确定具体病因。',fontsize=9,color=GRAY)
fig.subplots_adjust(bottom=.26,wspace=.27,top=.86)
save(fig,'03-air-bone-patterns')

# 4. Schematic cross-hearing paths and an artificial masking plateau.
fig,axs=plt.subplots(1,2,figsize=(11.5,4.7),gridspec_kw={'width_ratios':[1.1,1]})
ax=axs[0];ax.set(xlim=(0,10),ylim=(0,6));ax.axis('off');ax.set_title('A  跨耳听见与对侧掩蔽',pad=16)
boxes=[(0,3.6,2.2,1,'测试耳耳机'),(3.4,3.6,2.5,1,'测试耳耳蜗'),
       (3.4,.8,2.5,1,'非测试耳耳蜗'),(7.2,.8,2.6,1,'非测试耳\n掩蔽耳机')]
for x,y,w,h,label in boxes:
    ax.add_patch(Rectangle((x,y),w,h,fill=False,ec=GRAY,lw=1.2));ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=10)
def arrow(ax,a,b,color=GRAY,style='-'):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=12,lw=1.2,color=color,linestyle=style))
arrow(ax,(2.2,4.1),(3.4,4.1),BLUE);ax.text(2.7,4.55,'气导路径',ha='center',fontsize=9,color=BLUE)
ax.plot([1.1,1.1,3.4],[3.6,1.3,1.3],c=RED,ls='--',lw=1.2);arrow(ax,(2.7,1.3),(3.4,1.3),RED,'--')
ax.text(.8,2.65,'颅骨传递\n可能跨耳听见',ha='left',fontsize=9,color=RED)
arrow(ax,(7.2,1.3),(5.9,1.3),GREEN);ax.text(6.55,2.0,'窄带噪声',ha='center',fontsize=9,color=GREEN)
ax.text(.15,.05,'骨振器的振动也可能激励两耳；放置侧不等于反应耳。',fontsize=9,color=GRAY)
ax=axs[1];mask=np.arange(20,81,5);threshold=np.array([20,25,30,35,40,40,40,40,40,45,50,55,60])
ax.plot(mask,threshold,'o-',c=BLUE,lw=1.5,ms=5)
ax.axvspan(40,60,color='#eef3f5',zorder=-1);ax.text(50,34,'平台',ha='center',color=BLUE)
ax.text(29,18,'掩蔽不足',ha='center',fontsize=10,color=GRAY)
ax.text(71,66,'过度掩蔽',ha='center',fontsize=10,color=GRAY)
ax.set(xlabel='非测试耳掩蔽水平（示意，dB EML）',ylabel='测试耳重新测得的听阈（dB HL）',
       title='B  掩蔽平台的概念示意',ylim=(10,72));ax.grid(alpha=.15)
fig.text(.075,.01,'教学曲线，不规定起始噪声、步长或平台合格范围；dB EML 与 dB HL 是不同的标度。',fontsize=9,color=GRAY)
fig.subplots_adjust(wspace=.32,bottom=.23,top=.85)
save(fig,'04-cross-hearing-and-masking')

# 5. Equal four-frequency average does not imply equal frequency-specific sensitivity.
fig,axs=plt.subplots(1,2,figsize=(11.5,4.6),gridspec_kw={'width_ratios':[1.5,1]})
flat=np.full(6,40);sloping=np.array([5,10,20,50,80,95]);idx=np.array([1,2,3,4])
assert np.mean(flat[idx])==np.mean(sloping[idx])==40
ax=axs[0];audiogram(ax)
ax.plot(F,flat,'o-',c=BLUE,mfc='white',lw=1.5,label='听者甲：较平坦')
ax.plot(F,sloping,'s--',c=GREEN,mfc='white',lw=1.5,label='听者乙：高频下降')
ax.legend(loc='upper left',frameon=False,fontsize=10);ax.set_title('A  两张不同的气导听力图')
ax=axs[1];selected=F[idx];diff=sloping[idx]-flat[idx]
ax.bar(np.arange(4),diff,color=[GREEN if d>=0 else BLUE for d in diff],width=.55)
ax.axhline(0,c=GRAY,lw=.8);ax.set(xticks=np.arange(4),xticklabels=[str(x) for x in selected],
       xlabel='参与平均的频率（Hz）',ylabel='乙减甲的听阈差（dB）',ylim=(-45,50),
       title='B  四频平均均为 40 dB HL')
for i,d in enumerate(diff):ax.text(i,d+(3 if d>=0 else -3),f'{d:+d}',ha='center',va='bottom' if d>=0 else 'top',fontsize=10)
ax.grid(axis='y',alpha=.15)
fig.text(.09,.015,'平均频率明确为 500、1000、2000、4000 Hz；教学数据不包含言语任务，不能据此计算或排序实际言语识别成绩。',fontsize=9,color=GRAY)
fig.subplots_adjust(wspace=.32,bottom=.21,top=.85)
save(fig,'05-equal-average-different-audiograms')

verification={'figures':saved,'source':'synthetic educational data','no_audio_output':True,
    'audiogram_axis':'log2 frequency; hearing level increases downward',
    'masked_pattern_symbols':{'right_air':'triangle','right_bone':'['},
    'ascending_positive_trials':[6,9],'ascending_threshold_dB_HL':30,
    'average_frequencies_Hz':F[idx].tolist(),'both_average_dB_HL':40,
    'figure_1_arrow':'separate no-response example, not an additional threshold'}
(OUT.parent/'figure-verification.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2),encoding='utf8')
print('Generated five SVG and PNG teaching figures.')
