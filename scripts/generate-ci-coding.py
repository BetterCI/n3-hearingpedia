"""Generate original, code-derived teaching figures for the CI coding entry."""
from pathlib import Path
import importlib.util
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/figures/ci-coding'
OUT.mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location('encoder', ROOT / 'public/code/ci-coding/teaching_encoder.py')
enc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(enc)
t, x, bands, env, edges, cis, ace = enc.demo()
print(enc.verify(cis, ace))
plt.rcParams.update({'font.family': 'Microsoft YaHei', 'font.size': 11,
                     'svg.fonttype': 'path', 'svg.hashsalt': 'ci-coding',
                     'axes.unicode_minus': False, 'axes.spines.top': False,
                     'axes.spines.right': False})
PURPLE, GREEN, ORANGE = '#7454a2', '#227d83', '#be6536'


def save(fig, name):
    fig.savefig(OUT / (name + '.svg'), facecolor='white', metadata={'Date': None})
    svg = OUT / (name + '.svg')
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines()) + '\n', encoding='utf-8')
    fig.savefig(OUT / (name + '.png'), facecolor='white', dpi=145)
    plt.close(fig)


fig, ax = plt.subplots(figsize=(12, 7), layout='constrained')
ax.set(xlim=(0, 12), ylim=(0, 7)); ax.axis('off')
def box(x, y, w, h, text, color=PURPLE):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=.10',
                               facecolor='#f6f3fa', edgecolor=color, linewidth=1.4))
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=11)
def arrow(a, b):
    ax.annotate('', xy=b, xytext=a, arrowprops={'arrowstyle':'->', 'color':'#5a5363', 'lw':1.5})
box(.2, 5.75, 2, .8, '声音 x[n]\n前端增益／降噪')
box(3, 5.75, 2.4, .8, '分频 y_i[n]\n滤波器组或 FFT')
box(6.2, 5.75, 2.3, .8, '包络 a_i[n]\n整流低通／幅度估计')
box(9.3, 5.75, 2.3, .8, '通道增益 w_i\n可影响选峰结果')
for a,b in [((2.2,6.15),(3,6.15)),((5.4,6.15),(6.2,6.15)),((8.5,6.15),(9.3,6.15))]: arrow(a,b)
arrow((10.45,5.75),(10.45,5.5))
ax.plot([1.55,10.45],[5.5,5.5],color='#5a5363')
for xx in (1.55,4.45,7.35,10.35): arrow((xx,5.5),(xx,4.5))
box(.4, 3.45, 2.3, 1.05, 'CIS／HDCIS 家族\n固定启用通道\n周期性交错脉冲')
box(3.3, 3.45, 2.3, 1.05, 'ACE 家族\n先按增益后特征选峰\n再映射、交错发放')
box(6.2, 3.45, 2.3, 1.05, 'FSP／FS4 家族\n低频零交叉 → CSSS\n其余采用包络时序', GREEN)
box(9.1, 3.45, 2.5, 1.05, 'Fidelity120 家族\n频谱位置 → 电流权重\n相邻电极联合刺激', ORANGE)
for xx in (1.55,4.45,7.35,10.35): arrow((xx,3.45),(xx,2.35))
ax.plot([1.55,10.35],[2.35,2.35],color='#5a5363')
box(3.5,.85,5,1.05,'个体电映射与调度 → 事件 (e, t, I, τ)\n电荷平衡波形 → 电极—神经接口')
arrow((6,2.35),(6,1.9))
ax.text(.3,6.85,'上行展示公共操作；下行突出策略差异，实际模块顺序随实现而变。',color='#6b6278')
ax.text(.3,.55,'FSP／FS4 的零交叉取自分频波形；Fidelity120 的权重取自频谱位置，均需旁路信息。',fontsize=10)
ax.text(.3,.25,'原理流程图；不是某一型号的软件框图。ACE 的 maxima 选择须先于个体电映射。',fontsize=10,color='#6b6278')
save(fig, '01-workflow')

fig, axs = plt.subplots(1,2,figsize=(12,5.5),layout='constrained')
ax=axs[0]
theta=np.linspace(0,3.3*np.pi,600); r=2.9-.22*theta
xx,yy=r*np.cos(theta),r*np.sin(theta)
ax.plot(xx,yy,lw=32,color='#ece7f4',solid_capstyle='round')
ax.plot(xx,yy,lw=2,color=PURPLE)
idx=np.linspace(15,530,8).astype(int)
ax.scatter(xx[idx],yy[idx],s=110,c=np.arange(8),cmap='viridis',zorder=3,edgecolors='white')
for j,k in enumerate(idx): ax.text(xx[k]+.13,yy[k]+.16,f'E{8-j}',fontsize=10)
ax.annotate('基底端：较高频\n阵列入口',xy=(xx[0],yy[0]),xytext=(.7,-2.5),arrowprops={'arrowstyle':'->'})
ax.annotate('顶端方向：较低频',xy=(xx[idx[-1]],yy[idx[-1]]),xytext=(-3,2.7),arrowprops={'arrowstyle':'->'})
ax.set(xlim=(-3.5,3.5),ylim=(-3.2,3.2),title='（a）耳蜗内阵列：示意位置，不按比例'); ax.set_aspect('equal'); ax.axis('off')
ax=axs[1]
for j in range(8):
    ax.scatter(j,1,s=280,color=plt.cm.viridis((7-j)/7),edgecolor='white')
    ax.text(j,.65,f'E{j+1}',ha='center')
ax.plot([0,7],[1,1],color='#b2a9bd',zorder=0)
ax.annotate('低频／顶端方向',xy=(0,1.4),xytext=(2,1.4),arrowprops={'arrowstyle':'->'},va='center')
ax.annotate('高频／基底端',xy=(7,1.4),xytext=(4.3,1.4),arrowprops={'arrowstyle':'->'},va='center')
ax.text(3.5,.1,'本词条统一用 E1 → E8 表示低频到高频\n不同厂商的真实电极编号方向可能相反',ha='center',va='center')
ax.annotate('耳蜗外回流电极\n（单极模式示意）',xy=(6,-.9),xytext=(2,-.9),arrowprops={'arrowstyle':'->'},va='center')
ax.scatter(6,-.9,s=180,marker='s',color='#99909f')
ax.set(xlim=(-.5,7.5),ylim=(-1.5,2),title='（b）展开阵列：分析频带 → 刺激配置');ax.axis('off')
fig.suptitle('电极接触点 ≠ 分析频带 ≠ 独立神经通道',fontsize=16,color=PURPLE)
save(fig,'02-electrode-array')

fig, axs=plt.subplots(3,1,figsize=(12,8),layout='constrained')
mask=(t>=.04)&(t<.052)
im=axs[0].imshow(enc.compress(env)[:,mask],aspect='auto',origin='lower',
                  extent=[40,52,.5,8.5],vmin=0,vmax=1,cmap='viridis')
axs[0].set(title='（a）同一输入的包络映射热图：连续特征，不是脉冲',ylabel='教学通道')
for ax,events,title in [(axs[1],cis,'（b）CIS 原理模型：每周期 8 个候选事件'),(axs[2],ace,'（c）ACE 原理模型：每周期从 8 个通道选 4 个')]:
    ev=events[(events[:,0]>=.04)&(events[:,0]<.052)]
    ax.scatter(ev[:,0]*1000,ev[:,1]+1,c=ev[:,2],cmap='viridis',vmin=0,vmax=1,marker='|',s=200,linewidths=2.5)
    ax.set(xlim=(40,52),ylim=(.5,8.5),yticks=range(1,9),ylabel='教学电极',title=title)
    ax.grid(alpha=.15)
axs[2].set_xlabel('时间（ms）；短竖线为一个双相事件起点，未按相宽展开')
fig.colorbar(im,ax=axs,label='相对幅度（无量纲；非 µA）',shrink=.75,pad=.02)
save(fig,'03-electrodograms')

fig,axs=plt.subplots(2,2,figsize=(12,7),layout='constrained')
tt=np.arange(0,.012,1/enc.FS); y=np.sin(2*np.pi*300*tt)
cross=enc.upward_crossings(y)
axs[0,0].plot(tt*1000,y,color=GREEN);axs[0,0].scatter(cross*1000,np.zeros(len(cross)),color=ORANGE,zorder=4)
axs[0,0].set(title='（a）低频分频波形：上行零交叉作为时序线索',ylabel='相对幅度',xlabel='时间（ms）')
axs[1,0].eventplot([np.arange(0,.012,1/800)*1000,cross*1000],lineoffsets=[1,0],colors=[PURPLE,GREEN],linelengths=.5)
axs[1,0].set(yticks=[0,1],yticklabels=['零交叉事件','固定速率'],ylim=(-.6,1.6),xlabel='时间（ms）',title='（b）单通道时刻对比：非完整 CSSS 序列')
for alpha,color in [(0,PURPLE),(.5,GREEN),(1,ORANGE)]:
    pair=enc.steering(1,alpha)
    axs[0,1].plot([0,1],pair,'o-',label=f'α={alpha:g}',color=color)
axs[0,1].set(xticks=[0,1],xticklabels=['相邻电极 E_i','相邻电极 E_(i+1)'],ylim=(-.1,1.15),ylabel='电流份额',title='（c）电流导向：两电极同时分担总幅度')
axs[0,1].legend(fontsize=10)
us=np.arange(0,100,.25)
axs[1,1].plot(us,enc.biphasic(us*1e-6,10e-6,.8),color=PURPLE)
axs[1,1].set(xlabel='相对时间（µs）',ylabel='有符号相对幅度',ylim=(-1,1),title='（d）等面积双相：25 µs／相，间隔 8 µs')
for ax in axs.flat: ax.grid(alpha=.15)
save(fig,'04-timing-steering')
