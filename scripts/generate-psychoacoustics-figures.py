"""Original teaching figures; no participant data or device recommendations.

Run from any directory with Python, NumPy, SciPy and Matplotlib installed.
Chinese labels use Microsoft YaHei on Windows, Noto Sans CJK SC otherwise.
SVG text is outlined to preserve labels when displayed on other systems.
"""
from pathlib import Path
import json
import numpy as np
from scipy.special import expit, logit
from scipy.stats import norm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/figures/psychoacoustics'
OUT.mkdir(parents=True, exist_ok=True)
FONT = Path('C:/Windows/Fonts/msyh.ttc')
if FONT.exists():
    font_manager.fontManager.addfont(str(FONT))
    family = font_manager.FontProperties(fname=str(FONT)).get_name()
else:
    family = 'Noto Sans CJK SC'
plt.rcParams.update({'font.family':family, 'font.size':20, 'axes.titlesize':24,
    'axes.labelsize':22, 'legend.fontsize':18, 'svg.fonttype':'path',
    'axes.unicode_minus':False, 'axes.spines.top':False, 'axes.spines.right':False,
    'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
BLUE, ORANGE, GREY = '#1865a2','#b85a16','#576779'
sizes = {}
def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None,'Creator':'Hearingpedia original teaching figure'})
    fig.savefig(OUT/(name+'.png'),dpi=100)
    sizes[name] = {'svg_viewbox':[round(v*72) for v in fig.get_size_inches()],
                   'png_pixels':[round(v*100) for v in fig.get_size_inches()]}
    plt.close(fig)

# 1. Levels of evidence, arranged rather than asserting anatomical identity.
fig,ax=plt.subplots(figsize=(20,10)); fig.subplots_adjust(left=.02,right=.98,top=.98,bottom=.04)
ax.set(xlim=(0,20),ylim=(0,10)); ax.axis('off')
boxes=[(.5,6.3,'刺激与呈现','频谱、声级、时长\n校准、耳机、环境'),(7.1,6.3,'听者与内部加工','可听度、注意、记忆\n内部噪声与决策'),(13.7,6.3,'任务与行为','检测、辨别、匹配\n选择、评分与反应时间')]
for x,y,title,body in boxes:
    ax.add_patch(FancyBboxPatch((x,y),5.7,2.8,boxstyle='round,pad=.12',facecolor='#f2f6fa',edgecolor=BLUE,linewidth=2))
    ax.text(x+2.85,y+2.1,title,ha='center',weight='bold',fontsize=27)
    ax.text(x+2.85,y+.95,body,ha='center',va='center',fontsize=24,linespacing=1.7)
for x in [6.3,12.9]: ax.annotate('',(x+.7,7.7),(x,7.7),arrowprops={'arrowstyle':'->','lw':2.5,'color':GREY})
ax.add_patch(FancyBboxPatch((2.6,2.25),14.8,2.55,boxstyle='round,pad=.12',facecolor='#fff6eb',edgecolor=ORANGE,linewidth=2))
ax.text(10,4.05,'统计估计与模型比较',ha='center',fontsize=27,weight='bold')
ax.text(10,3.05,'阈值、斜率、敏感性、偏向与不确定性',ha='center',fontsize=24)
ax.annotate('',(16.1,4.9),(16.1,6.1),arrowprops={'arrowstyle':'->','lw':2.5,'color':GREY})
ax.text(10,1.1,'行为结果约束机制解释；定位神经环节还需要独立证据',ha='center',fontsize=24,color=GREY)
save(fig,'01-measurement-chain')

# 2. Logistic psychometric functions. x is dB above a teaching reference.
gamma, lapse, alpha = .5,.02,0.
def pcorrect(x,beta=2): return gamma+(1-gamma-lapse)*expit((np.asarray(x)-alpha)/beta)
x=np.linspace(-12,12,400)
fig,ax=plt.subplots(figsize=(20,10)); fig.subplots_adjust(left=.12,right=.95,bottom=.18,top=.88)
for beta,style,color in [(2,'-',BLUE),(4,'--',ORANGE)]:
    ax.plot(x,pcorrect(x,beta),style,color=color,lw=4,label=f'位置 α = 0 dB，尺度 β = {beta} dB')
for y,label in [(.5,'机会水平 0.50'),(.74,'函数中点 0.74'),(.98,'上渐近线 0.98')]:
    ax.axhline(y,color=GREY,ls=':',lw=1.5);ax.text(-11.7,y+.008,label,color=GREY,fontsize=18)
ax.plot(0,.74,'o',color=BLUE,ms=11)
ax.set(xlabel='相对参考声级 x（dB，教学设定）',ylabel='二选一任务的正确率',ylim=(.47,1.04),xlim=(-12,12))
ax.legend(loc='lower right'); ax.grid(alpha=.13)
save(fig,'02-psychometric-function')

# 3. SDT: equal-variance Gaussian distributions and ROC.
fig,axes=plt.subplots(1,2,figsize=(20,10));fig.subplots_adjust(left=.075,right=.97,bottom=.18,top=.89,wspace=.3)
z=np.linspace(-3.5,5,500); ax=axes[0]
ax.plot(z,norm.pdf(z),color=BLUE,lw=3,label='无目标 N(0, 1)')
ax.plot(z,norm.pdf(z-1.5),'--',color=ORANGE,lw=3,label='有目标 N(1.5, 1)')
for c,style in [(.2,':'),(1.2,'-.')]:ax.axvline(c,color=GREY,lw=2,ls=style,label=f'判据 k = {c}')
ax.set(xlabel='内部证据（标准差单位）',ylabel='概率密度',title='（a）敏感性相同，判据不同',ylim=(0,.56))
ax.legend(loc='upper right',fontsize=17)
criteria=np.linspace(-5,7,500); ax=axes[1]
ax.plot(norm.sf(criteria),norm.sf(criteria-1.5),color=BLUE,lw=3,label="同一敏感性 d′ = 1.5")
ax.plot([0,1],[0,1],':',color=GREY,label="d′ = 0 的参照")
sdt=[]
for k,marker,color in [(.2,'o',BLUE),(1.2,'s',ORANGE)]:
    h,f=norm.sf(k-1.5),norm.sf(k)
    ax.plot(f,h,marker,color=color,ms=12)
    ax.annotate(f'k = {k}\nH = {h:.3f}\nF = {f:.3f}',(f,h),xytext=(18,-60 if k==.2 else -15),textcoords='offset points',fontsize=18)
    dp=norm.ppf(h)-norm.ppf(f); assert np.isclose(dp,1.5)
    sdt.append({'criterion':k,'hit':h,'false_alarm':f,'d_prime':dp})
ax.set(xlabel='虚报率 F',ylabel='命中率 H',title='（b）接收者操作特征曲线（ROC）',xlim=(0,1),ylim=(0,1.03));ax.legend(loc='lower right',fontsize=17)
save(fig,'03-sensitivity-and-bias')

# 4. Distinguish response-independent sampling from a response-adaptive track.
rng=np.random.default_rng(20261009)
levels=np.arange(-6,7,2); constant=rng.permutation(np.repeat(levels,8))
level=8.; run=0; adaptive=[];responses=[];moves=[]
for trial in range(56):
    adaptive.append(level); correct=bool(rng.random()<pcorrect(level));responses.append(correct)
    if correct:
        run+=1
        move=-1 if run==2 else 0
        if run==2:run=0
    else:run=0;move=1
    moves.append(move);level+=move
target=2**(-.5);target_x=2*logit((target-gamma)/(1-gamma-lapse))
fig,axes=plt.subplots(2,1,figsize=(20,12));fig.subplots_adjust(left=.11,right=.96,bottom=.13,top=.93,hspace=.5)
axes[0].plot(np.arange(1,57),constant,'o-',color=BLUE,ms=6,lw=1.3)
axes[0].set(title='（a）恒定刺激：预先选定水平，再随机排序',ylabel='相对声级（dB）',ylim=(-8,10))
axes[1].plot(np.arange(1,57),adaptive,color=GREY,lw=2,drawstyle='steps-post')
r=np.asarray(responses);t=np.arange(1,57);a=np.asarray(adaptive)
axes[1].scatter(t[r],a[r],color=BLUE,s=45,marker='o',label='答对')
axes[1].scatter(t[~r],a[~r],color=ORANGE,s=65,marker='x',label='答错')
axes[1].axhline(target_x,color=ORANGE,ls='--',lw=2,label=f'模型中 70.71% 的位置：{target_x:.2f} dB')
axes[1].set(title='（b）二降一升：连续两次答对降 1 dB，答错升 1 dB',xlabel='试次',ylabel='相对声级（dB）',ylim=(-8,10));axes[1].legend(loc='upper right',fontsize=17)
for ax in axes:ax.set_xlim(0,57);ax.grid(alpha=.15)
save(fig,'04-sampling-procedures')

# 5. Wilson intervals refer to trial outcomes at a fixed level, not listeners.
def wilson(k,n,z=norm.ppf(.975)):
    p=k/n;center=(p+z*z/(2*n))/(1+z*z/n)
    half=z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/(1+z*z/n)
    return center-half,center+half
fig,ax=plt.subplots(figsize=(20,10));fig.subplots_adjust(left=.13,right=.94,bottom=.2,top=.9)
intervals=[]
for i,(k,n,color,marker) in enumerate([(16,20,BLUE,'o'),(80,100,ORANGE,'s')]):
    lo,hi=wilson(k,n);p=k/n
    ax.errorbar(i,p,yerr=[[p-lo],[hi-p]],fmt=marker,color=color,capsize=16,ms=15,lw=4)
    ax.text(i+.12,p+.025,f'{k}/{n} = 0.80',ha='left',fontsize=25)
    ax.text(i,lo-.065,f'95% Wilson 区间\n[{lo:.3f}, {hi:.3f}]',ha='center',fontsize=22)
    intervals.append({'correct':k,'trials':n,'estimate':p,'lower':lo,'upper':hi})
ax.set(xticks=[0,1],xticklabels=['20 个独立试次','100 个独立试次'],ylabel='同一刺激水平下的正确率',ylim=(.45,1.0),xlim=(-.7,1.7))
ax.axhline(.8,color=GREY,ls=':',lw=1.5);ax.grid(axis='y',alpha=.15)
save(fig,'05-trial-uncertainty')

record={'nature':'Original teaching calculations; no empirical participant data.',
    'gamma':gamma,'lambda':lapse,'alpha_db':alpha,'beta_db':[2,4],
    'midpoint_probability':gamma+(1-gamma-lapse)/2,
    'threshold_75_percent_db':2*logit((.75-gamma)/(1-gamma-lapse)),
    'two_down_one_up_target':target,'two_down_one_up_model_position_db':target_x,
    'random_seed':20261009,'initial_level_db':8,'step_db':1,'trials':56,
    'sdt':sdt,'wilson_intervals':intervals,'figures':sizes}
record_path=ROOT/'docs/research/psychoacoustics-2026-10-09/figure-calculations.json'
record_path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(record,ensure_ascii=False,indent=2))
