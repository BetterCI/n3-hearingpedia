"""Four original analytic teaching figures. No recorded speech or clinical data.
Run: python demo.py (Python 3.11, NumPy, Matplotlib, Chinese font).
"""
from pathlib import Path
import json,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
HERE=Path(__file__).resolve().parent
OUT=HERE.parents[1]/'figures'/'speech-enhancement-and-noise-reduction'
OUT.mkdir(parents=True,exist_ok=True)
fonts={f.name for f in font_manager.fontManager.ttflist}
font=next((x for x in ['Microsoft YaHei','Noto Sans CJK SC','SimHei'] if x in fonts),None)
if not font:raise RuntimeError('A Chinese font is required')
plt.rcParams.update({'font.family':[font,'DejaVu Sans'],'font.size':16,'axes.titlesize':19,'axes.labelsize':16,'xtick.labelsize':13,'ytick.labelsize':13,'legend.fontsize':14,'svg.fonttype':'none','svg.hashsalt':'hearingpedia-se-20261106','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B='#2769a0';O='#ba6024';G='#287c68';K='#26384b';GRAY='#667586'
def save(fig,name,note):
    fig.text(.07,.035,note,fontsize=13,color=GRAY)
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None,'Creator':'Hearingpedia original analytic demonstration'})
    p=OUT/(name+'.svg');s=p.read_text(encoding='utf-8')
    s=re.sub(r'width="[\d.]+pt" height="[\d.]+pt"','width="1400" height="700"',s,count=1)
    p.write_text('\n'.join(l.rstrip() for l in s.splitlines())+'\n',encoding='utf-8')
    fig.savefig(OUT/(name+'.png'),dpi=100);plt.close(fig)
def one(title):
    fig,ax=plt.subplots(figsize=(14,7),dpi=100)
    fig.subplots_adjust(left=.10,right=.94,bottom=.19,top=.82)
    fig.suptitle(title,x=.07,y=.95,ha='left',fontsize=25,fontweight='bold',color=K)
    return fig,ax

db=np.linspace(-20,20,401);xi=10**(db/10);w=xi/(1+xi);irm=np.sqrt(w)
fig,ax=one('同一个功率比，可以定义不同的幅度增益')
ax.plot(db,w,color=B,lw=3,label='维纳增益 ξ / (1 + ξ)')
ax.plot(db,irm,color=O,lw=3,label='本文 IRM 定义 √[ξ / (1 + ξ)]')
ax.scatter([0,0],[.5,np.sqrt(.5)],color=[B,O],s=65,zorder=3)
ax.annotate('0 dB：0.500',xy=(0,.5),xytext=(5,.43),color=B)
ax.annotate('0 dB：0.707',xy=(0,np.sqrt(.5)),xytext=(-16,.78),color=O)
ax.axvline(0,color=GRAY,lw=1,ls=':');ax.set(xlabel='先验信噪比 10 log₁₀ ξ（dB）',ylabel='乘在复数谱上的实数幅度增益',ylim=(0,1.05),xlim=(-20,20));ax.legend(loc='lower right');ax.grid(alpha=.18)
save(fig,'gain-definitions','原创解析曲线；功率按共同尺度归一化。IRM 的命名并不固定，使用时必须给出公式。')

g=np.linspace(0,1,401);dist=(1-g)**2;noise=g*g;total=dist+noise
fig,ax=one('压低残余噪声，也会压低同一频点的语音')
ax.plot(g,noise,color=G,lw=3,label=r'残余噪声功率 $g^2P_v$')
ax.plot(g,dist,color=O,lw=3,label='语音失真功率 (1−g)²Pₛ')
ax.plot(g,total,color=B,lw=3,label='总均方误差：两项之和')
ax.scatter([.5],[.5],color=B,s=75,zorder=3);ax.annotate('最小值：g = 0.5，MSE = 0.5',(.5,.5),(.48,.76),arrowprops={'arrowstyle':'->','color':B},color=B)
ax.set(xlabel='固定实数幅度增益 g',ylabel='归一化功率／均方误差',xlim=(0,1),ylim=(0,1.08));ax.legend(loc='upper center',ncol=1);ax.grid(alpha=.18)
save(fig,'distortion-tradeoff',r'教学条件：零均值且不相关的 S 与 V，$P_s = P_v = 1$。固定 g > 0 时，该频点输出 SNR 仍为 0 dB。')

fig,axes=plt.subplots(1,2,figsize=(14,7),dpi=100)
fig.subplots_adjust(left=.08,right=.96,bottom=.22,top=.77,wspace=.32)
fig.suptitle('复数相加，不等于幅度相加',x=.07,y=.95,ha='left',fontsize=25,fontweight='bold',color=K)
cases=[(1+0j,-.8+0j,'反相抵消：X = 0.2，理想比值 S/X = 5'),(1+0j,1j,'相位偏移：X = 1+j，S/X = 0.5−0.5j')]
for ax,(s,n,title) in zip(axes,cases):
    x=s+n
    for z,color,label,offset in [(s,B,'S',(0,-22)),(n,O,'V',(5,8)),(x,G,'X',(8,8))]:
        ax.annotate('',(z.real,z.imag),(0,0),arrowprops={'arrowstyle':'->','color':color,'lw':3})
        ax.annotate(label,(z.real,z.imag),xytext=offset,textcoords='offset points',color=color,fontweight='bold')
    ax.set(xlim=(-1.05,1.35),ylim=(-.45,1.35),xlabel='实部（归一化幅度）',ylabel='虚部（归一化幅度）',title=title);ax.set_aspect('equal');ax.axhline(0,color=GRAY,lw=.6);ax.axvline(0,color=GRAY,lw=.6);ax.grid(alpha=.15)
save(fig,'complex-mixture','原创单频点算例，不是语音实验；0–1 实数掩蔽不能完成上述全部恢复，X = 0 时比值不定义。')

freqs=[1000,3000];angles=np.linspace(-90,90,721);pos=np.arange(4)*.025;c=343
def steer(f,angle):return np.exp(-2j*np.pi*f*pos*np.sin(np.deg2rad(angle))/c)
checks=[]
fig,axes=plt.subplots(1,2,figsize=(14,7),dpi=100)
fig.subplots_adjust(left=.08,right=.96,bottom=.20,top=.78,wspace=.22)
fig.suptitle('阵列利用方向差异：理想 MVDR 与延时求和',x=.07,y=.95,ha='left',fontsize=25,fontweight='bold',color=K)
for f,ax in zip(freqs,axes):
    d=steer(f,0);v=steer(f,50);rn=10*np.outer(v,v.conj())+np.eye(4)
    q=np.linalg.solve(rn,d);weight=q/(d.conj()@q);ds=d/4
    a=np.array([steer(f,t) for t in angles]).T
    for ww,label,color in [(weight,'MVDR',B),(ds,'延时求和',O)]:
        resp=20*np.log10(np.maximum(np.abs(ww.conj()@a),1e-3));ax.plot(angles,resp,color=color,lw=2.5,label=label)
    ax.axvline(0,color=G,ls=':',label='目标 0°');ax.axvline(50,color=GRAY,ls=':',label='干扰 50°');ax.set(title=f'{f/1000:g} kHz',xlabel='相对阵列正前方的角度（°）',ylabel='幅度响应（dB）',ylim=(-60,6),xlim=(-90,90));ax.grid(alpha=.18);ax.legend(fontsize=12,loc='lower left')
    checks.append({'frequency_hz':f,'distortionless_error':float(abs(weight.conj()@d-1)),'mvdr_noise_power':float(np.real(weight.conj()@rn@weight)),'delay_sum_noise_power':float(np.real(ds.conj()@rn@ds))})
    assert abs(weight.conj()@d-1)<1e-12
    assert checks[-1]['mvdr_noise_power']<=checks[-1]['delay_sum_noise_power']+1e-12
save(fig,'mvdr-directivity',r'原创自由场模型：4 个全向传感器，间距 2.5 cm；$R_v = 10 aa^H + I$，声速 343 m/s；只画前半平面。')
assert abs(w[200]-.5)<1e-12 and abs(irm[200]-np.sqrt(.5))<1e-12
assert np.argmin(total)==200
for s,n,_ in cases:assert abs((s/(s+n))*(s+n)-s)<1e-12
validation={'date':'2026-11-06','model':'analytic teaching examples, not clinical or speech benchmark data','wiener_at_zero_db':float(w[200]),'irm_at_zero_db':float(irm[200]),'mse_optimum_gain':float(g[np.argmin(total)]),'mse_minimum':float(total.min()),'complex_ratio_case_1':5,'complex_ratio_case_2_real':.5,'complex_ratio_case_2_imag':-.5,'mvdr':checks,'checks_passed':True}
(HERE/'validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(validation,ensure_ascii=False,indent=2))
