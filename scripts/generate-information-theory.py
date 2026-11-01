"""Original information-theory teaching calculations, figures and quantization audio."""
from pathlib import Path
import json
import wave
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT/'public/figures/information-theory'
AUDIO = ROOT/'public/audio/information-theory'
REC = ROOT/'docs/research/information-theory-2026-11-02'
PRE = ROOT/'artifacts/information-theory/figures'
for folder in (FIG, AUDIO, REC, PRE): folder.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei', 'font.size':12, 'svg.fonttype':'path',
 'svg.hashsalt':'information-theory-hearingpedia', 'axes.unicode_minus':False,
 'axes.spines.top':False, 'axes.spines.right':False})
B,G,R,M = '#22658c','#31755e','#b44e37','#61727d'

def H(p):
    p=np.asarray(p, dtype=float); p=p[p>0]
    return float(-np.sum(p*np.log2(p)))

def h(p): return H([p,1-p])

def measures(prior, channel):
    joint=np.asarray(prior)[:,None]*np.asarray(channel)
    px=joint.sum(axis=1); py=joint.sum(axis=0)
    hx=H(px); hy=H(py); hxy=H(joint.ravel())
    return {'H_X':hx,'H_Y':hy,'H_XY':hxy,'H_X_given_Y':hxy-hy,
            'I_XY':hx+hy-hxy,'accuracy':float(np.trace(joint))}

def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创信息论教学计算 · 非听者或器件实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.05,1,.93),w_pad=3)
    p=FIG/f'{name}.svg'; fig.savefig(p,metadata={'Date':None},facecolor='white')
    p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/f'{name}.png',dpi=105,facecolor='white'); plt.close(fig)

p=np.linspace(.001,.999,600)
fig,ax=plt.subplots(1,2,figsize=(14,6))
ax[0].plot(p,-np.log2(p),color=B);ax[0].scatter([.5,.125],[1,3],color=R)
ax[0].set(xlabel='事件概率 p',ylabel='自信息（bit）',title='（a）小概率事件的自信息更大',ylim=(0,8))
ax[1].plot(p,[h(v) for v in p],color=G);ax[1].scatter([.1,.5],[h(.1),1],color=R)
ax[1].set(xlabel='二值标签 X=1 的概率',ylabel='熵 H(X)（bit/次）',title='（b）平均不确定性在等概率时最大',ylim=(0,1.1))
fig.suptitle('自信息属于一次结果，熵属于整个分布',fontsize=18,fontweight='bold');save(fig,'surprisal-and-entropy')

conf=np.full((4,4),.1);np.fill_diagonal(conf,.7)
cm=measures(np.full(4,.25),conf)
fig,ax=plt.subplots(1,2,figsize=(14,6))
im=ax[0].imshow(conf,cmap='Blues',vmin=0,vmax=1)
for i in range(4):
    for j in range(4):ax[0].text(j,i,f'{conf[i,j]:.1f}',ha='center',va='center',color='white' if i==j else B)
ax[0].set(xticks=range(4),yticks=range(4),xticklabels=list('ABCD'),yticklabels=list('ABCD'),xlabel='报告标签 Y',ylabel='呈现标签 X',title='（a）每行是条件概率，不是联合概率')
ax[1].bar(['呈现前 H(X)','观察后 H(X|Y)','减少 I(X;Y)'],[cm['H_X'],cm['H_X_given_Y'],cm['I_XY']],color=[M,B,G])
ax[1].set(ylabel='bit/次',title='（b）四标签等概率；正确率 70%',ylim=(0,2.25))
for i,v in enumerate([cm['H_X'],cm['H_X_given_Y'],cm['I_XY']]):ax[1].text(i,v+.05,f'{v:.4f}',ha='center')
fig.suptitle('从完整混淆矩阵计算互信息',fontsize=18,fontweight='bold');save(fig,'confusion-and-information')

prior=np.array([.6,.2,.1,.1]);q=np.full(4,.25)
cross=float(-np.sum(prior*np.log2(q)));kl=cross-H(prior)
fig,ax=plt.subplots(1,2,figsize=(14,6))
w=.35;xx=np.arange(4)
ax[0].bar(xx-w/2,prior,w,label='真实分布 P',color=B);ax[0].bar(xx+w/2,q,w,label='假设分布 Q',color=G)
ax[0].set(xticks=xx,xticklabels=list('ABCD'),ylabel='概率',title='（a）把高频标签误当成等概率');ax[0].legend()
ax[1].bar(['H(P)','交叉熵 H(P,Q)'],[H(prior),cross],color=[B,M]);ax[1].set(ylabel='bit/符号',title='（b）期望对数损失增加 KL(P||Q)',ylim=(0,2.35))
ax[1].annotate(f'差值 {kl:.4f} bit',xy=(1,H(prior)),xytext=(.5,2.18),arrowprops={'arrowstyle':'->','color':R},ha='center',color=R)
fig.suptitle('分布失配的代价有方向',fontsize=18,fontweight='bold');save(fig,'divergence-and-cross-entropy')

eps=.2; binary=np.array([[1-eps,eps],[eps,1-eps]])
pis=np.linspace(.001,.999,300);mis=[measures([1-v,v],binary)['I_XY'] for v in pis]
second=np.array([[.9,.1],[.1,.9]]);cascade=binary@second
fig,ax=plt.subplots(1,2,figsize=(14,6))
mi_line=ax[0].plot(pis,mis,color=B,label='互信息（左轴）')[0]
ax[0].set(xlabel='有声先验 P(X=1)',ylabel='互信息（bit/次）',title='（a）相同条件反应与正确率，互信息仍会变化',ylim=(0,1))
accuracy_axis=ax[0].twinx();accuracy_line=accuracy_axis.axhline(.8,color=R,ls='--',label='正确率（右轴）')
accuracy_axis.set(ylabel='正确率（概率）',ylim=(0,1));ax[0].legend(handles=[mi_line,accuracy_line],fontsize=10)
ax[1].bar(['原观察 Y','再翻转后的 Z'],[1-h(.2),1-h(.26)],color=[B,G]);ax[1].set(ylabel='与原标签 X 的互信息（bit/次）',title='（b）两级无记忆翻转：0.2，再 0.1',ylim=(0,.34))
fig.suptitle('互信息取决于联合分布，串联处理受到条件约束',fontsize=18,fontweight='bold');save(fig,'prior-and-processing')

fig,ax=plt.subplots(1,2,figsize=(14,6))
n=np.arange(1,51);ax[0].plot(n,n,color=M,ls='--',label='独立等概率标签');ax[0].plot(n,1+(n-1)*h(.1),color=B,label='翻转概率 0.1 的平稳马尔可夫链')
ax[0].set(xlabel='序列长度 n',ylabel='联合熵 H(X1,…,Xn)（bit）',title='（a）单标签熵相同，序列熵不同');ax[0].legend(fontsize=10)
codes=['0','10','110','111'];lengths=[1,2,3,3]
ax[1].bar(np.arange(4),lengths,color=G);ax[1].set(xticks=range(4),xticklabels=[f'{a}\np={v:g}\n码字 {c}' for a,v,c in zip('ABCD',prior,codes)],ylabel='码长（bit）',title='（b）前缀码平均码长 1.6 bit/符号',ylim=(0,3.6))
fig.suptitle('利用统计结构压缩，与为抗错而增加冗余是不同任务',fontsize=18,fontweight='bold');save(fig,'sequence-and-prefix-code')

fig,ax=plt.subplots(1,2,figsize=(14,6))
ep=np.linspace(0,1,501);ax[0].plot(ep,[1-h(v) for v in ep],color=B);ax[0].set(xlabel='独立翻转概率 ε',ylabel='容量（bit/次使用）',title='（a）二元对称信道：完全翻转仍可逆',ylim=(0,1.05));ax[0].scatter([0,.5,1],[1,0,1],color=R)
db=np.linspace(-10,30,300);cap=3000*np.log2(1+10**(db/10))
ax[1].plot(db,cap/1000,color=G);ax[1].scatter([10],[3000*np.log2(11)/1000],color=R)
ax[1].set(xlabel='接收带内信噪比（dB）',ylabel='容量（kbit/s）',title='（b）带宽固定为 3000 Hz 的理想带限 AWGN')
fig.suptitle('容量是给定信道模型与约束下的极限',fontsize=18,fontweight='bold');save(fig,'channel-capacity')

fs=16000;t=np.arange(fs)/fs
x=np.sin(2*np.pi*220*t)+.35*np.sin(2*np.pi*440*t)+.2*np.sin(2*np.pi*880*t)
x=.65*x/np.max(np.abs(x));ramp=np.ones(fs);edge=np.sin(np.linspace(0,np.pi/2,160))**2;ramp[:160]=edge;ramp[-160:]=edge[::-1];x*=ramp
def quantize(x,b):
    m=2**(b-1);return np.clip(np.rint(x*m),-m,m-1)/m
quant={b:quantize(x,b) for b in [2,4,8]};mse={str(b):float(np.mean((v-x)**2)) for b,v in quant.items()}
for name,values in [('source',x),('quantized-2bit',quant[2]),('quantized-4bit',quant[4])]:
    pcm=np.rint(.85*values*32767).astype('<i2')
    with wave.open(str(AUDIO/f'{name}.wav'),'wb') as wav:
        wav.setnchannels(1);wav.setsampwidth(2);wav.setframerate(fs);wav.writeframes(pcm.tobytes())
fig,ax=plt.subplots(1,2,figsize=(14,6))
take=(t>=.04)&(t<.049);ax[0].plot(t[take]*1000,x[take],color=M,label='原始合成波形');ax[0].step(t[take]*1000,quant[2][take],where='mid',color=B,label='2 bit 量化')
ax[0].set(xlabel='时间（ms）',ylabel='归一化幅度',title='（a）固定量化器带来的样本误差');ax[0].legend(fontsize=10)
ds=np.geomspace(.005,1,300);ax[1].plot(ds,.5*np.log2(1/ds),color=G);ax[1].scatter([.25],[1],color=R)
ax[1].set(xscale='log',xlabel='归一化平均平方失真 D/σ²',ylabel='R(D)（bit/样本）',title='（b）另一个模型：独立高斯源的率失真函数')
fig.suptitle('量化实例与理论率失真曲线使用不同信源',fontsize=18,fontweight='bold');save(fig,'quantization-and-rate-distortion')

rng=np.random.default_rng(20261102);sizes=[40,200,1000];estimates=[]
for size in sizes:
    vals=[]
    for _ in range(400):
        counts=rng.multinomial(size,np.full(16,1/16)).reshape(4,4);joint=counts/size
        vals.append(H(joint.sum(axis=1))+H(joint.sum(axis=0))-H(joint.ravel()))
    estimates.append(np.array(vals))
fig,ax=plt.subplots(1,2,figsize=(14,6))
for vals,size,color in zip(estimates,sizes,[R,B,G]):ax[0].hist(vals,bins=28,density=True,histtype='step',label=f'N={size}',color=color)
ax[0].set(xlabel='插件互信息估计（bit/次）',ylabel='重复模拟的密度',title='（a）两组标签真实独立，真值为零');ax[0].legend()
means=[float(v.mean()) for v in estimates];ax[1].plot(sizes,means,'o-',color=B,label='400 次模拟均值');ax[1].plot(sizes,9/(2*np.array(sizes)*np.log(2)),'s--',color=R,label='固定满支持下的大样本近似')
ax[1].set(xscale='log',xlabel='每次模拟的样本量 N',ylabel='估计互信息的均值（bit/次）',title='（b）小样本近似并非精确校正');ax[1].legend(fontsize=10)
fig.suptitle('经验互信息为正，不能单凭这一点认定存在信息传递',fontsize=18,fontweight='bold');save(fig,'finite-sample-bias')

result={'entropy':{'binary_p01':h(.1),'binary_p02':h(.2),'biased_four':H(prior)},'confusion':cm,
 'mismatch':{'cross_entropy':cross,'KL_PQ':kl,'KL_QP':float(np.sum(q*np.log2(q/prior)))},
 'detection':{'prior_half':measures([.5,.5],binary),'prior_tenth':measures([.9,.1],binary),'cascade':measures([.5,.5],cascade)},
 'prefix':{'probabilities':prior.tolist(),'codewords':codes,'mean_length':float(np.dot(prior,lengths))},
 'markov':{'flip_probability':.1,'entropy_rate':h(.1),'H20':1+19*h(.1)},
 'capacity':{'BSC_eps01':1-h(.1),'bandwidth_Hz':3000,'snr_linear':10,'AWGN_bit_per_s':float(3000*np.log2(11))},
 'rate_distortion':{'D_over_variance':.25,'Gaussian_bit_per_sample':1.0},
 'audio':{'fs_Hz':fs,'samples':len(x),'ramp_samples':160,'common_gain':.85,'source_peak':float(np.max(np.abs(x))),'source_mean_square':float(np.mean(x*x)),'quantizer_mse':mse},
 'null_estimation':{'seed':20261102,'repetitions':400,'sizes':sizes,'means':means,'asymptotic_bias':[float(9/(2*s*np.log(2))) for s in sizes]}}
(REC/'calculations.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
