from pathlib import Path
import json,shutil,hashlib,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).parent
plt.rcParams.update({'font.family':'Microsoft YaHei','svg.fonttype':'path','font.size':10,'axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B='#285f83';O='#b9613b';T='#347b70';G='#65727b'
def save(fig,name):
 fig.savefig(ROOT/(name+'.svg'),bbox_inches='tight');fig.savefig(ROOT/(name+'.png'),bbox_inches='tight',dpi=160);plt.close(fig)
 p=ROOT/(name+'.svg');p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
shutil.copy2(ROOT.parent/'outer-hair-cell/01-zha-corti.png',ROOT/'01-zha-corti.png')
# 两个分开的数学环节：门控工作区间与线性单极点滤波。
fig,axs=plt.subplots(1,2,figsize=(10,4.2),layout='constrained');x=np.linspace(-1,1,501);p=1/(1+np.exp(-x/.18));axs[0].plot(x,p,color=B,lw=2);axs[0].axhline(.5,color=G,ls=':',lw=.8);axs[0].set(xlabel='归一化毛束位移（无量纲）',ylabel='示意开放概率',ylim=(0,1),xlim=(-1,1));axs[0].text(-.92,.86,'参数为教学设定',fontsize=9)
f=np.geomspace(30,30000,601)
for fc,color in [(300,B),(1000,O),(3000,T)]:axs[1].semilogx(f,-10*np.log10(1+(f/fc)**2),color=color,lw=1.8,label=f'示意截止频率 {fc} Hz')
axs[1].set(xlabel='输入变化频率（Hz）',ylabel='线性滤波幅度级（dB）',ylim=(-45,1),xlim=(30,30000));axs[1].legend(fontsize=8);save(fig,'03-gating-filter')
# 有限资源适应：初始值为基线稳态，不声称为神经放电模型。
dt=.0001;t=np.arange(0,1+dt/2,dt);u=np.where((t>=.2)&(t<.6),20.,1.);tau=.1;R=np.empty_like(t);R[0]=1/(1+tau*u[0])
for i in range(len(t)-1):R[i+1]=R[i]+dt*((1-R[i])/tau-u[i]*R[i])
q=u*R
fig,axs=plt.subplots(3,1,figsize=(9,6.4),layout='constrained',sharex=True)
for ax,y,color,label in zip(axs,[u,R,q],[G,B,O],['释放驱动（1/s）','可用资源比例','示意释放通量（1/s）']):ax.plot(t,y,color=color,lw=1.5);ax.axvspan(.2,.6,color='#dce8ec',alpha=.55);ax.set_ylabel(label);ax.set_xlim(0,1)
axs[1].set_ylim(0,1);axs[2].set_xlabel('时间（s）');save(fig,'04-release-adaptation')
# 输出单元阈值异质性：全为数学参数，不等同自发率亚型。
levels=np.linspace(-10,110,1001);curves=np.array([1/(1+np.exp(-(levels-half)/7)) for half in [20,50,80]]);mean=curves.mean(axis=0)
fig,axs=plt.subplots(1,2,figsize=(10,4.3),layout='constrained')
for i,(half,color) in enumerate(zip([20,50,80],[B,O,T])):axs[0].plot(levels,curves[i],color=color,lw=1.7,label=f'示意半激活点 {half} dB')
axs[0].set(xlabel='相对于任意参考的输入水平（dB）',ylabel='单元归一化输出',ylim=(0,1));axs[0].legend(fontsize=8)
axs[1].plot(levels,mean,color=B,lw=2,label='三个单元等权平均');axs[1].set(xlabel='相对于任意参考的输入水平（dB）',ylabel='群体归一化输出',ylim=(0,1));ax2=axs[1].twinx();ax2.plot(levels,np.gradient(mean,levels),color=O,lw=1.3,ls='--',label='对输入的变化率');ax2.set_ylabel('群体输出变化率（每 dB）',color=O);ax2.set_ylim(0,.025);axs[1].legend(fontsize=8,loc='upper left');ax2.legend(fontsize=8,loc='lower right');save(fig,'05-population-range')
assert np.all((R>=0)&(R<=1)) and np.all((curves>=0)&(curves<=1))
report=dict(originalMathematicalFigures=3,publishedSourceFigures=2,data='数学教学参数；未拟合人体或动物细胞',gatingSlope=.18,exampleCutoffHz=[300,1000,3000],resourceTauSeconds=tau,drivePerSecond=[1,20],driveIntervalSeconds=[.2,.6],initialResource=float(R[0]),activeSteadyResource=1/(1+tau*20),unitHalfActivationDb=[20,50,80],probabilitiesAndResourceWithinZeroOne=True,modelsRun='仅原创教学模型；未运行所链接第三方生理模型')
(ROOT/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(report,ensure_ascii=False))
