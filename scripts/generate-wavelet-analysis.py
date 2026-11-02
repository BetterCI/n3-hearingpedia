"""Original vector teaching figures, with reproducible synthetic inputs."""
from pathlib import Path
import importlib.util,sys,json
sys.dont_write_bytecode=True
import numpy as np,pywt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyBboxPatch
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('wa',ROOT/'public/code/wavelet-analysis/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures/wavelet-analysis';PRE=ROOT/'artifacts/wavelet-analysis/figures';REC=ROOT/'docs/research/wavelet-analysis-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'wavelet-analysis-course','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创小波教学图 · 指定数学模型或模拟，非声音/神经/听者实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2)
    path=FIG/(name+'.svg');fig.savefig(path,metadata={'Date':None},facecolor='white')
    path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
def scalogram(ax,t,f,w):
    p=abs(w)**2;db=10*np.log10(np.maximum(p/p.max(),1e-6))
    im=ax.pcolormesh(t,f,db,shading='auto',cmap='magma',vmin=-40,vmax=0,rasterized=True);ax.set_yscale('log');ax.set(xlabel='时间 / s',ylabel='约定等效频率 / Hz',yticks=[20,40,80,160]);ax.set_yticklabels(['20','40','80','160']);return im
# 1 Mother functions, all explicitly defined in the article.
u=np.linspace(-4,4,1601);fig,axes=plt.subplots(1,3,figsize=(14,5.5))
haar=np.where((u>=0)&(u<.5),1,np.where((u>=.5)&(u<1),-1,0));mex=2/(np.sqrt(3)*np.pi**.25)*(1-u*u)*np.exp(-u*u/2)
axes[0].plot(u,haar,color=B,lw=2);axes[0].set_title('Haar：局部差分、阶跃形状');axes[1].plot(u,mex,color=G,lw=2);axes[1].set_title('Mexican hat：曲率式正负瓣')
axes[2].plot(u,m.morlet(u).real,color=P,label='实部');axes[2].plot(u,m.morlet(u).imag,color=R,label='虚部',alpha=.8);axes[2].set_title('修正Morlet：局部复振荡');axes[2].legend()
for ax in axes:ax.axhline(0,color=M,lw=.7);ax.set(xlabel='无量纲变量 u',ylabel='母小波值')
fig.suptitle('母小波不是唯一的一种波形：形状决定分析偏好',fontsize=18,fontweight='bold');save(fig,'mother-wavelets')
# 2 Dilation and time-frequency schematic; tile areas are conventional.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));t=np.linspace(-3,3,2001)
for a,col in [(.25,B),(.5,G),(1,P)]:axes[0].plot(t,m.morlet(t/a).real/np.sqrt(a),color=col,label=f'a={a:g}')
axes[0].set(xlabel='时间（指定单位）',ylabel='实部 / √a',title='（a）尺度增大：更宽、更慢、峰值降低');axes[0].legend()
ax=axes[1]
for y,width,n,col in [(0,.5,8,B),(1,1,4,G),(2,2,2,P)]:
    for k in range(n):ax.add_patch(Rectangle((k*width,y),width,.8,fc=col+'18',ec=col,lw=1.5))
ax.set(xlim=(0,4),ylim=(-.1,3),yticks=[.4,1.4,2.4],yticklabels=['小尺度 / 高频','中尺度','大尺度 / 低频'],xlabel='时间（示意，不是采样网格）',title='（b）时间宽度与频率宽度随尺度相反变化');ax.invert_yaxis()
fig.suptitle('多尺度观察：用局部变化的尺子，而不是任意增加分辨率',fontsize=18,fontweight='bold');save(fig,'scale-localization')
# 3 Physical CWT with chosen COI convention.
t,x,f,a,w=m.sound_example();fig,axes=plt.subplots(2,1,figsize=(14,7.5),gridspec_kw={'height_ratios':[1,2]});axes[0].plot(t,x,color=B,lw=1);axes[0].set(xlabel='时间 / s',ylabel='指定幅值',title='（a）20→120 Hz扫频，叠加1.3 s处100 Hz短脉冲包络振荡')
im=scalogram(axes[1],t,f,w);coi=np.sqrt(2)*a;axes[1].fill_betweenx(f,0,coi,color='white',alpha=.45);axes[1].fill_betweenx(f,t[-1]-coi,t[-1],color='white',alpha=.45);axes[1].set_title('（b）L²归一化系数功率 / 全图最大值；淡色为所选边界影响区');fig.colorbar(im,ax=axes[1],label='相对系数功率 / dB')
fig.suptitle('局部振荡的时间与尺度：颜色不是校准功率谱密度',fontsize=18,fontweight='bold');save(fig,'sound-cwt')
# 4 Haar exact vector and matrix.
v=np.array([4,6,10,12,8,8,2,2]);U=m.haar_matrix(8);c=U@v;fig,axes=plt.subplots(1,2,figsize=(14,5.5));im=axes[0].imshow(U,cmap='RdBu_r',vmin=-.71,vmax=.71);axes[0].set(xticks=range(8),yticks=range(8),yticklabels=['A₃','D₃','D₂[0]','D₂[1]','D₁[0]','D₁[1]','D₁[2]','D₁[3]'],xlabel='输入位置',title='（a）正交分析矩阵 U，每行一个局部模板');fig.colorbar(im,ax=axes[0],label='模板权重')
axes[1].bar(np.arange(8),c,color=[B,P,G,G,R,R,R,R]);axes[1].axhline(0,color=M,lw=.7);axes[1].set(xticks=range(8),xticklabels=['A₃','D₃','D₂₀','D₂₁','D₁₀','D₁₁','D₁₂','D₁₃'],ylabel='系数',title='（b）x=[4,6,10,12,8,8,2,2]，两侧能量均为432')
fig.suptitle('Haar变换：保留归一化的平均与差，而不是丢弃细节',fontsize=18,fontweight='bold');save(fig,'haar-decomposition')
# 5 Actual circular two-channel branch outputs.
n=np.arange(128);v=np.cos(2*np.pi*8*n/128)+.6*np.cos(2*np.pi*48*n/128);parts=m.filter_bank(v);fig,axes=plt.subplots(1,2,figsize=(14,5.5))
for y,col,label in [(parts[0],B,'低通支路合成'),(parts[1],R,'高通支路合成')]:axes[0].plot(n[:36],y[:36],color=col,label=label)
axes[0].set(xlabel='样本位置',ylabel='指定幅值',title='（a）单支路不是无混叠的原信号');axes[0].legend()
axes[1].plot(n[:36],np.roll(v,1)[:36],color=M,lw=3,label='原输入延迟1点');axes[1].plot(n[:36],sum(parts)[:36],color=G,ls='--',label='两支路复原之和');axes[1].set(xlabel='样本位置',ylabel='指定幅值',title=f'（b）总重建最大误差 {np.max(abs(sum(parts)-np.roll(v,1))):.1e}');axes[1].legend()
fig.suptitle('完全重建依赖分析与合成配对，以及正确的抽取相位',fontsize=18,fontweight='bold');save(fig,'filterbank-reconstruction')
# 6 Boundary and threshold shift equivariance, only circular convention.
v,out=m.boundary_example();sh=m.shift_example();fig,axes=plt.subplots(1,2,figsize=(14,5.5));axes[0].plot(v,color=M,ls=':',label='原始斜坡')
for (name,y),col in zip(out.items(),[B,G,P]):axes[0].plot(y,color=col,label=name)
axes[0].set(xlabel='样本位置',ylabel='近似支路重建',title='（a）db4三级，仅保留A₃；端点假设改变结果');axes[0].legend(fontsize=10)
for name,col in [('dwt',R),('swt',G)]:axes[1].plot(sh[name]-sh[name+'_shift'],color=col,label=name.upper())
axes[1].set(xlabel='样本位置',ylabel='原处理 − 移位处理后移回',title='（b）循环移位1点；Haar三级、固定软阈值0.2');axes[1].legend()
fig.suptitle('有限记录必须说明边界；降采样后的阈值处理可能依赖对齐',fontsize=18,fontweight='bold');save(fig,'boundary-shift')
# 7 Denoising, known clean is for teaching evaluation only.
d=m.denoising_example();fig,axes=plt.subplots(1,2,figsize=(14,5.5));axes[0].plot(d['t'],d['noisy'],color=M,alpha=.45,lw=.7,label='带噪输入');axes[0].plot(d['t'],d['clean'],color='black',lw=1.5,label='已知教学真值');axes[0].plot(d['t'],d['soft'],color=G,lw=1.3,label='软阈值重建');axes[0].set(xlabel='时间 / s',ylabel='指定幅值',title='（a）单次指定高斯噪声；db4、四级、periodization');axes[0].legend(fontsize=9)
q=np.linspace(-1.5,1.5,601);axes[1].plot(q,q,color=M,ls=':',label='不改系数');axes[1].plot(q,pywt.threshold(q,d['threshold'],'soft'),color=G,label='软阈值');axes[1].plot(q,pywt.threshold(q,d['threshold'],'hard'),color=R,label='硬阈值');axes[1].set(xlabel='原细节系数',ylabel='修改后系数',title=f'（b）估计σ={d["sigma"]:.4f}，通用阈值λ={d["threshold"]:.4f}');axes[1].legend()
fig.suptitle('去噪改变系数：噪声减少与信号偏差需要共同评价',fontsize=18,fontweight='bold');save(fig,'threshold-denoising')
# 8 Frequency ordered packets.
paths,e=m.packet_example();fig,axes=plt.subplots(1,2,figsize=(14,5.5))
for i,path in enumerate(paths):axes[0].add_patch(Rectangle((64*i,0),64,1,fc=([B,G,P,R][i%4])+'20',ec=M));axes[0].text(64*i+32,.5,path,ha='center',va='center',fontsize=13)
axes[0].axvline(160,color=R,lw=2);axes[0].set(xlim=(0,512),ylim=(-.05,1.3),yticks=[],xlabel='名义频带 / Hz，fs=1024',title='（a）三级频率顺序，不是节点名字母顺序')
axes[1].bar(paths,e/e.sum(),color=[B,G,P,R,B,G,P,R]);axes[1].set(xlabel='频率顺序节点',ylabel='正交系数能量比例',title='（b）160 Hz纯音：Haar滤波器并非理想带通')
fig.suptitle('小波包同时分解两支：频带顺序与实际响应都要检查',fontsize=18,fontweight='bold');save(fig,'wavelet-packets')
# 9 Vanishing moments and biorthogonal energy comparison.
_,moment=m.moment_example();fig,axes=plt.subplots(1,2,figsize=(14,5.5))
for name,col in [('haar',B),('db4',G)]:axes[0].semilogy(np.arange(8,120),np.maximum(abs(moment[name][8:120]),1e-18),color=col,label=name)
axes[0].set(xlabel='一级细节系数位置（去掉边界）',ylabel='|细节系数|，对数轴',title='（a）三次多项式内部：db4四个消失矩');axes[0].legend()
rng=np.random.default_rng(21);v=rng.normal(size=256);ratios=[]
for name in ['db4','bior4.4']:
    cs=pywt.wavedec(v,name,mode='periodization',level=3);ratios.append(sum(c@c for c in cs)/(v@v))
axes[1].bar(['正交 db4','双正交 bior4.4'],ratios,color=[G,P]);axes[1].axhline(1,color=M,ls=':');axes[1].set(ylabel='系数平方和 / 输入平方和',ylim=(0,1.35),title='（b）都可重建；普通系数平方和未必相同')
for i,r in enumerate(ratios):axes[1].text(i,r+.035,f'{r:.6f}',ha='center')
fig.suptitle('消失矩、正交性、对称性与可重建性是不同属性',fontsize=18,fontweight='bold');save(fig,'moments-biorthogonal')
# 10 Noise can create bright regions; toy independent multiple-testing probability.
t=np.arange(2048)/1024;v=np.random.default_rng(812).normal(size=len(t));w=m.cwt_physical(v,1/1024,a);fig,axes=plt.subplots(1,2,figsize=(14,5.5));im=scalogram(axes[0],t,f,w);axes[0].set_title('（a）输入只有独立高斯噪声，也有局部亮纹');fig.colorbar(im,ax=axes[0],label='相对系数功率 / dB')
q=np.arange(1,101);axes[1].plot(q,1-.95**q,color=R,lw=2);axes[1].set(xlabel='假设相互独立的检验次数 m',ylabel='至少一次假阳性的概率',ylim=(0,1.04),title='（b）每次α=0.05；不是小波像素的有效自由度');axes[1].axhline(.05,color=M,ls=':')
fig.suptitle('看到图形不等于发现结构：背景模型与重复检验不可省略',fontsize=18,fontweight='bold');save(fig,'noise-inference')
# Course sketch, original native SVG lines.
fig,ax=plt.subplots(figsize=(6.4,3.6));ax.axis('off');ax.set(xlim=(-3.5,3.5),ylim=(-.5,3.4))
for i,(a,col) in enumerate([(.18,B),(.4,G),(.9,P)]):
    t=np.linspace(-3,3,800);ax.plot(t,2.8-i*1.1+.35*m.morlet(t/a).real/np.sqrt(a),color=col,lw=2)
ax.annotate('',xy=(3.12,.25),xytext=(3.12,3.05),arrowprops=dict(arrowstyle='->',color=M,lw=1.7));ax.text(3.25,1.65,'尺度',rotation=90,ha='center',va='center',color=M)
ax.text(-3.1,3.15,'小波分析',fontsize=18,fontweight='bold',color=B);fig.tight_layout();path=ROOT/'public/figures/foundation-courses/wavelet-analysis.svg';fig.savefig(path,metadata={'Date':None},transparent=True);plt.close(fig)
(REC/'calculations.json').write_text(json.dumps(m.summary(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(m.summary(),ensure_ascii=False))
