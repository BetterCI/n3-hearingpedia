"""Original teaching diagrams; ISO 226:2023 calculation; no listener data."""
from pathlib import Path
import csv,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/harvey-fletcher'
RESEARCH=ROOT/'docs/research/harvey-fletcher-2026-10-10'
OUT.mkdir(parents=True,exist_ok=True);RESEARCH.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':13,'svg.fonttype':'path'})
BLUE,ORANGE,GREEN,GRAY='#276582','#ad683c','#477e63','#526472'
def save(fig,name):
    for ext in ['svg','png']:
        p=OUT/(name+'.'+ext);fig.savefig(p,dpi=100,facecolor='white')
        if ext=='svg':p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)
def box(ax,x,y,w,h,title,detail,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.008,rounding_size=.015',edgecolor=color,facecolor='#f6f9fb',lw=1.5))
    ax.text(x+w/2,y+h*.67,title,ha='center',va='center',color=color,fontsize=16,fontweight='bold')
    ax.text(x+w/2,y+h*.29,detail,ha='center',va='center',fontsize=13,color=GRAY)
fig,ax=plt.subplots(figsize=(12.8,6.5));fig.subplots_adjust(left=.035,right=.965,top=.80,bottom=.13)
fig.suptitle('听见、多响与听懂，需要不同任务',fontsize=23,fontweight='bold',y=.95)
ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
rows=[('纯音与背景','频率、声级、噪声','检测声音','是否出现？','检测阈值','规定参考下的声级',BLUE),('参考声与测试声','参考固定、测试可调','等响匹配','感觉一样响吗？','匹配声级','等响关系与响度级',ORANGE),('经处理的语音','材料、声级、噪声','识别语音','重复音节、词或句子','识别成绩','明确计分单位的正确率',GREEN)]
for y,row in zip([.70,.38,.06],rows):
    for x,title,detail in zip([.02,.365,.71],row[:6:2],row[1:6:2]):box(ax,x,y,.265,.23,title,detail,row[6])
    for a,b in [(.292,.352),(.637,.697)]:ax.annotate('',xy=(b,y+.115),xytext=(a,y+.115),arrowprops={'arrowstyle':'->','lw':1.8,'color':GRAY})
fig.text(.5,.855,'共同前提：物理校准、明确听者条件、固定任务与反应规则',ha='center',fontsize=14,color=GRAY)
fig.text(.5,.045,'原创功能框图；不表示神经结构，三种输出不直接互换',ha='center',fontsize=12,color=GRAY)
save(fig,'measurement-tasks')

# Parameters independently retained from the repository's previously verified ISO table record.
freq=np.array([20,25,31.5,40,50,63,80,100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150,4000,5000,6300,8000,10000,12500])
alpha=np.array([.635,.602,.569,.537,.509,.482,.456,.433,.412,.391,.373,.357,.343,.330,.320,.311,.303,.300,.295,.292,.290,.290,.289,.289,.289,.293,.303,.323,.354])
lu=np.array([-31.5,-27.2,-23.1,-19.3,-16.1,-13.1,-10.4,-8.2,-6.3,-4.6,-3.2,-2.1,-1.2,-.5,0,.4,.5,0,-2.7,-4.2,-1.2,1.4,2.3,1,-2.3,-7.2,-11.2,-10.9,-3.5])
threshold=np.array([78.1,68.7,59.5,51.1,44,37.5,31.5,26.5,22.1,17.9,14.4,11.4,8.6,6.2,4.4,3,2.2,2.4,3.5,1.7,-1.3,-4.2,-6,-5.4,-1.5,6,12.6,13.9,12.3])
def lp(phon):return 10/alpha*np.log10((4e-10)**(.3-alpha)*(10**(.03*phon)-10**.072)+10**(alpha*(threshold+lu)/10))-lu
levels=[20,40,60,80];curves=np.array([lp(p) for p in levels])
assert np.allclose(curves[:,17],levels,atol=.02)
assert np.all(np.diff(curves,axis=0)>0)
assert np.allclose(lp(2.4),threshold)
prior=ROOT/'public/figures/core-eight/additions/iso226-2023-calculated.csv'
if prior.exists():
    old=list(csv.DictReader(prior.open(encoding='utf-8')))
    for i,p in enumerate(levels):assert np.allclose(curves[i],[float(row[f'{p}_phon_dBSPL']) for row in old])
with (OUT/'equal-loudness-data.csv').open('w',encoding='utf-8',newline='') as f:
    wr=csv.writer(f);wr.writerow(['frequency_Hz','alpha_f','L_U_dB','T_f_dB']+[f'{p}_phon_dBSPL' for p in levels])
    for j in range(len(freq)):wr.writerow([freq[j],alpha[j],lu[j],threshold[j]]+list(curves[:,j]))
fig,ax=plt.subplots(figsize=(12.8,6.5));fig.subplots_adjust(left=.085,right=.96,top=.79,bottom=.19)
fig.suptitle('等响曲线：现代 ISO 226:2023 计算示例',fontsize=22,fontweight='bold',y=.95)
for p,ys,c,style in zip(levels,curves,[BLUE,ORANGE,GREEN,GRAY],['-','--','-.',':']):ax.semilogx(freq,ys,color=c,lw=2.5,linestyle=style,marker='o',ms=3,label=f'{p} phon')
ax.set(xlim=(20,12500),ylim=(0,130),xlabel='频率 / Hz',ylabel='声压级 / dB SPL')
ax.set_xticks([20,50,100,200,500,1000,2000,5000,10000]);ax.set_xticklabels(['20','50','100','200','500','1k','2k','5k','10k'])
ax.grid(alpha=.2);ax.axvline(1000,color=GRAY,lw=1,alpha=.4);ax.legend(ncol=4,loc='upper right',frameon=False)
fig.text(.5,.855,'正常听力年轻人 · 自由场正面入射 · 双耳 · 纯音',ha='center',fontsize=14,color=GRAY)
fig.text(.5,.047,'标准公式计算；不是1933年历史数据，也不是耳机均衡或个人增益处方',ha='center',fontsize=12,color=GRAY)
save(fig,'equal-loudness')

B=np.geomspace(20,2000,401);W=200.
spectral=np.minimum(B,W)/W;total=np.minimum(B,W)/B
assert np.isclose(np.minimum(100,W)/W,.5) and np.isclose(np.minimum(400,W)/400,.5)
assert np.all((total>0)&(total<=1)) and np.all((spectral>0)&(spectral<=1))
fig,axs=plt.subplots(1,2,figsize=(12.8,6.5));fig.subplots_adjust(left=.07,right=.965,top=.76,bottom=.25,wspace=.30)
fig.suptitle('噪声带宽实验：固定谱密度 ≠ 固定总功率',fontsize=22,fontweight='bold',y=.95)
axs[0].plot([600,900,900,1100,1100,1400],[0,0,1,1,0,0],color=BLUE,lw=2.7)
axs[0].fill_between([900,1100],[1,1],color=BLUE,alpha=.1)
axs[0].set(title='（a）理想矩形通带',xlabel='频率 / Hz',ylabel='功率增益（无量纲）',xlim=(600,1400),ylim=(-.04,1.3))
axs[0].annotate('',xy=(1100,1.15),xytext=(900,1.15),arrowprops={'arrowstyle':'<->','color':GRAY})
axs[0].text(1000,1.22,'W = 200 Hz',ha='center',fontsize=13,color=GRAY)
axs[1].semilogx(B,10*np.log10(spectral),color=BLUE,lw=2.5,label='固定噪声谱密度')
axs[1].semilogx(B,10*np.log10(total),color=ORANGE,lw=2.5,ls='--',label='固定噪声总功率')
axs[1].axvline(W,color=GRAY,ls=':',lw=1.4)
axs[1].set(title='（b）进入通带的噪声功率',xlabel='噪声带宽 B / Hz',ylabel='归一化功率 / dB',ylim=(-11,1))
axs[1].set_xticks([20,50,100,200,500,1000,2000]);axs[1].set_xticklabels(['20','50','100','200','500','1k','2k'])
axs[1].legend(loc='lower left',frameon=False,fontsize=12)
for ax in axs:ax.grid(alpha=.2)
fig.text(.5,.855,'两种条件在 B = W 时具有相同通带内功率，以此归一化为 0 dB',ha='center',fontsize=14,color=GRAY)
fig.text(.5,.08,'原创解析教学图；矩形通带、同中心噪声；没有听者数据与检测阈预测',ha='center',fontsize=12,color=GRAY)
save(fig,'masking-bandwidth')

weights=np.array([.10,.20,.30,.25,.15]);inputs=np.array([[.9,.8,.4,.3,.2],[.5,.8,.8,.3,.2],[.5,.8,.4,.3,.6]])
scores=inputs@weights;assert np.isclose(weights.sum(),1) and np.allclose(inputs.mean(axis=1),.52) and np.allclose(scores,[.475,.555,.495])
fig,axs=plt.subplots(1,2,figsize=(12.8,6.5));fig.subplots_adjust(left=.07,right=.96,top=.77,bottom=.25,wspace=.30)
fig.suptitle('平均可利用程度相同，加权结果仍可不同',fontsize=22,fontweight='bold',y=.95)
colors=[BLUE,ORANGE,GREEN];labels=['基线','变更 A','变更 B'];hatches=['','//','..'];x=np.arange(5)
for j,(row,c,label,hatch) in enumerate(zip(inputs,colors,labels,hatches)):axs[0].bar(x+(j-1)*.24,row,width=.23,color=c,label=label,hatch=hatch,edgecolor='white')
axs[0].set(title='（a）五个抽象频带',ylabel='可利用程度（无量纲）',ylim=(0,1.08))
axs[0].set_xticks(x);axs[0].set_xticklabels([f'频带 {i+1}\nw={w:.2f}' for i,w in enumerate(weights)],fontsize=11)
axs[0].legend(loc='upper right',frameon=False,ncol=3,fontsize=11)
bars=axs[1].bar(labels,scores,color=colors,width=.55)
for bar,hatch,s in zip(bars,hatches,scores):bar.set_hatch(hatch);axs[1].text(bar.get_x()+bar.get_width()/2,s+.018,f'{s:.3f}',ha='center',fontsize=15)
axs[1].axhline(.52,color=GRAY,linestyle=':',lw=1.5,label='未加权平均均为0.52')
axs[1].set(title='（b）加权教学指数',ylabel='A_demo（无量纲）',ylim=(0,.7))
axs[1].legend(loc='upper right',frameon=False,fontsize=11)
for ax in axs:ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
fig.text(.5,.855,'权重和输入由教学目的选择；移到不同权重的频带，贡献不同',ha='center',fontsize=14,color=GRAY)
fig.text(.5,.075,'原创教学计算；不是正式 AI / SII，不对应真实频段或识别正确率',ha='center',fontsize=12,color=GRAY)
save(fig,'band-weighting')
manifest={'date':'2026-10-10','script':'scripts/generate-fletcher.py','listener_data':False,'figures':['measurement-tasks','equal-loudness','masking-bandwidth','band-weighting'],'iso_calculation':{'source':'ISO 226:2023; repository previously verified table record; checked against retained CSV when present','phon_levels':levels,'one_kHz_dBSPL':curves[:,17].tolist(),'parameter_rows':29,'not_1933_data':True},'masking_demo':{'center_Hz':1000,'rectangular_width_Hz':200,'noise_bandwidth_Hz':[20,2000],'normalization':'same admitted power at B=W','not_detection_thresholds':True},'weighted_demo':{'weights':weights.tolist(),'inputs':inputs.tolist(),'scores':scores.tolist(),'means':inputs.mean(axis=1).tolist(),'not_standard_SII':True},'assertions':'passed'}
(RESEARCH/'figure-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':4,'assertions':'passed','scores':scores.tolist()}))
