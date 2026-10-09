"""Original teaching figures and four additive-synthesis sounds; no participant data.

Run with Python + numpy, scipy, matplotlib, soundfile. All parameters are below.
The MDS distances are stipulated Euclidean distances, not human ratings.
"""
from pathlib import Path
import json, hashlib
import numpy as np
from scipy.spatial.distance import pdist, squareform
import soundfile as sf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/timbre-perception'
AUDIO=ROOT/'public/audio/timbre-perception'
OUT.mkdir(parents=True,exist_ok=True);AUDIO.mkdir(parents=True,exist_ok=True)
font=Path('C:/Windows/Fonts/msyh.ttc')
if font.exists():
    font_manager.fontManager.addfont(str(font))
    family=font_manager.FontProperties(fname=str(font)).get_name()
else:family='Noto Sans CJK SC'
plt.rcParams.update({'font.family':family,'font.size':23,'svg.fonttype':'path',
 'svg.hashsalt':'hearingpedia-timbre-20261009','axes.unicode_minus':False,
 'axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})
BLUE,ORANGE,GREY='#1865a2','#b85a16','#576779'
sizes={}
def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None,'Creator':'Hearingpedia original teaching figure'})
    svg=OUT/(name+'.svg')
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
    fig.savefig(OUT/(name+'.png'),dpi=100)
    sizes[name]={'svg_viewbox':[round(v*72) for v in fig.get_size_inches()],
                 'png_pixels':[round(v*100) for v in fig.get_size_inches()]}
    plt.close(fig)

FS,F0,DURATION,RELEASE,RMS=48000,200,1.2,.15,.06
n=np.arange(1,7);freq=F0*n
weights={'A':np.array([1,.8,.6,.4,.2,.1]),'B':np.array([1,.2,.1,.05,.02,.01])}
centroid=lambda a:float(freq@a/np.sum(a))
centroids={k:centroid(a) for k,a in weights.items()}
C=np.array([1,.5,0,.5,0,0]);D=np.array([.5,1,.5,0,0,0])
assert centroid(C)==centroid(D)==400
fig,axs=plt.subplots(1,2,figsize=(20,10))
fig.subplots_adjust(left=.075,right=.98,bottom=.2,top=.83,wspace=.3)
for ax,pairs,title in [(axs[0],[('A',weights['A']),('B',weights['B'])],'（a）同一基频，频谱分布不同'),(axs[1],[('C',C),('D',D)],'（b）同一重心，谐波结构仍不同')]:
    for index,(label,a) in enumerate(pairs):
        color=BLUE if index==0 else ORANGE
        ax.bar(freq+(-24 if index==0 else 24),a,width=42,color=color,
               hatch='' if index==0 else '//',label=f'{label}：重心 {centroid(a):.1f} Hz')
    ax.set(xlabel='谐波频率 / Hz',ylabel='相对振幅系数',xticks=freq,ylim=(0,1.3))
    ax.set_title(title,pad=20,fontsize=26);ax.legend(fontsize=19,loc='upper right')
fig.text(.5,.075,'教学设定：基频 200 Hz；重心采用振幅权重；柱的横向偏移仅为避免遮挡',ha='center',color=GREY,fontsize=21)
save(fig,'01-spectral-cues')

t=np.arange(round(FS*DURATION))/FS
def envelope(attack):
    e=np.ones_like(t)
    onset=t<attack;e[onset]=.5*(1-np.cos(np.pi*t[onset]/attack))
    offset=t>DURATION-RELEASE;e[offset]=.5*(1+np.cos(np.pi*(t[offset]-(DURATION-RELEASE))/RELEASE))
    return e
audio=[]
for key,a in weights.items():
    carrier=np.sum(a[:,None]*np.sin(2*np.pi*freq[:,None]*t),axis=0)
    for label,attack in [('fast',.02),('slow',.2)]:
        x=envelope(attack)*carrier
        x*=RMS/np.sqrt(np.mean(x*x))
        path=AUDIO/(key.lower()+'-'+label+'.wav')
        sf.write(path,x,FS,subtype='PCM_24')
        read,sr=sf.read(path);rms=float(np.sqrt(np.mean(read*read)))
        assert sr==FS and len(read)==57600 and np.max(np.abs(read))<1
        assert abs(rms-RMS)<1e-7
        spectrum=np.abs(np.fft.rfft(read[int(.4*FS):int(.8*FS)]))
        bins=np.fft.rfftfreq(int(.4*FS),1/FS)
        harm_amp=np.array([spectrum[np.argmin(abs(bins-f))] for f in freq])
        measured=centroid(harm_amp)
        assert abs(measured-centroids[key])<.002
        audio.append({'file':str(path.relative_to(ROOT)).replace('\\','/'),
          'fs_hz':sr,'duration_s':len(read)/sr,'attack_s':attack,'release_s':RELEASE,
          'fundamental_hz':F0,'harmonic_amplitudes':a.tolist(),
          'whole_event_rms':rms,'peak':float(np.max(np.abs(read))),
          'steady_harmonic_amplitude_centroid_hz':measured,
          'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
fig,axs=plt.subplots(1,2,figsize=(20,10));fig.subplots_adjust(left=.075,right=.96,bottom=.21,top=.82,wspace=.25)
for attack,label,color,ls in [(.02,'快起音：20 ms',BLUE,'-'),(.2,'慢起音：200 ms',ORANGE,'--')]:
    axs[0].plot(t*1000,envelope(attack),label=label,color=color,ls=ls,lw=3)
axs[0].set(xlim=(0,350),ylim=(-.02,1.1),xlabel='起始后的时间 / ms',ylabel='归一化包络（峰值 = 1）')
axs[0].set_title('（a）固定频谱，改变起音',fontsize=26,pad=20);axs[0].legend(fontsize=20,loc='lower right')
for row,(label,attack) in enumerate([('快起音',.02),('慢起音',.2)]):
    for col,key in enumerate(['A','B']):
        x,y=col*1.1,row*1.1
        axs[1].add_patch(FancyBboxPatch((x,y),1,.9,boxstyle='round,pad=.02',facecolor='#f3f7fb',edgecolor=BLUE if key=='A' else ORANGE,lw=2))
        axs[1].text(x+.5,y+.57,f'频谱 {key} · {label}',ha='center',fontsize=22)
        axs[1].text(x+.5,y+.23,f'{centroids[key]:.1f} Hz · {round(attack*1000)} ms',ha='center',fontsize=21,color=GREY)
axs[1].set(xlim=(-.1,2.2),ylim=(-.15,2.15));axs[1].axis('off')
axs[1].set_title('（b）两项声学操作，四个试听条件',fontsize=26,pad=20)
fig.text(.5,.075,'音频：1.2 s、6 条谐波、全事件 RMS = 0.06；等 RMS 不等于等响，图（a）显示归一化形状',ha='center',fontsize=20,color=GREY)
save(fig,'02-attack-and-stimuli')

coords=np.array([[0,0],[1,0],[0,1],[1,1]],float)
dist=squareform(pdist(coords));J=np.eye(4)-np.ones((4,4))/4
gram=-.5*J@(dist**2)@J
values,vectors=np.linalg.eigh(gram);order=np.argsort(values)[::-1]
values=values[order];vectors=vectors[:,order]
recovered=vectors[:,:2]*np.sqrt(np.maximum(values[:2],0))
error=float(np.max(abs(squareform(pdist(recovered))-dist)))
assert error<1e-12
fig,axs=plt.subplots(1,2,figsize=(20,10));fig.subplots_adjust(left=.055,right=.97,bottom=.22,top=.82,wspace=.3)
axs[0].imshow(dist,cmap='Blues',vmin=0,vmax=np.sqrt(2))
labels=['P','Q','R','S'];axs[0].set(xticks=np.arange(4),yticks=np.arange(4),xticklabels=labels,yticklabels=labels)
for i in range(4):
    for j in range(4):axs[0].text(j,i,'0' if i==j else ('√2' if dist[i,j]>1.1 else '1'),ha='center',va='center',color='white' if dist[i,j]>1.1 else '#172d40',fontsize=28)
axs[0].set_title('（a）预先设定的距离矩阵',fontsize=27,pad=22)
# Rotation of recovered coordinates is permitted; display the equivalent centered square.
display=coords-.5
for i,j in [(0,1),(0,2),(1,3),(2,3),(0,3)]:
    axs[1].plot(display[[i,j],0],display[[i,j],1],ls='--' if (i,j)==(0,3) else '-',color=GREY,lw=2)
axs[1].scatter(display[:,0],display[:,1],s=190,color=BLUE)
for lab,(x,y) in zip(labels,display):axs[1].text(x+.06,y+.06,lab,fontsize=28)
axs[1].text(0,-.65,'边长 1；对角线 √2',ha='center',fontsize=23)
axs[1].set(xlim=(-.9,.9),ylim=(-.9,.9),xlabel='显示坐标 1（无量纲）',ylabel='显示坐标 2（无量纲）')
axs[1].set_aspect('equal');axs[1].set_title('（b）经典 MDS 恢复等价的正方形',fontsize=26,pad=22)
fig.text(.5,.075,'纯数学教学例：P、Q、R、S 不是四段试听音频；距离不是听者评分；方向可旋转或镜像',ha='center',color=GREY,fontsize=21)
save(fig,'03-mds-example')

fig,ax=plt.subplots(figsize=(20,10));fig.subplots_adjust(left=.02,right=.98,bottom=.03,top=.98)
ax.set(xlim=(0,20),ylim=(0,10));ax.axis('off')
def box(x,y,w,h,title,body,color=BLUE):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',facecolor='#f3f7fb' if color==BLUE else '#fff6ec',edgecolor=color,lw=2))
    ax.text(x+w/2,y+h-.6,title,ha='center',va='center',fontsize=29,weight='bold')
    ax.text(x+w/2,y+(h-.85)/2,body,ha='center',va='center',fontsize=25,linespacing=1.7)
box(.6,5.25,5.5,3.5,'声学输入','频谱、起音与动态\n录音、空间、声级条件')
box(7.2,5.25,5.5,3.5,'听觉加工与模型','外周频率与时域表征\n中枢整合及选择性')
box(13.8,5.25,5.5,3.5,'独立测量的行为','相异性、辨别、匹配\n声源命名与偏好')
for x in [6.25,12.85]:ax.annotate('',(x+.8,7),(x,7),arrowprops={'arrowstyle':'->','lw':2,'color':GREY})
box(3,1.1,14,2.8,'连接三类证据时需要检验','输入操作是否改变感知？模型能否预测未见刺激？\n神经活动能否解释任务结果与个体差异？',ORANGE)
ax.text(10,9.5,'音色研究中的三类证据',ha='center',weight='bold',fontsize=33)
ax.text(10,.35,'原创概念图；没有解剖定位、神经效应量或患者改善比例',ha='center',color=GREY,fontsize=23)
save(fig,'04-evidence-levels')

record={'nature':'original teaching synthesis and mathematical example; no human data',
 'fundamental_hz':F0,'amplitude_weighted_centroids_hz':centroids,
 'same_centroid_counterexample':{'C':C.tolist(),'D':D.tolist(),'centroid_hz':400},
 'mds':{'labels':labels,'stipulated_coordinates':coords.tolist(),'distances':dist.tolist(),
        'eigenvalues':values.tolist(),'max_distance_reconstruction_error':error},
 'figures':sizes,'audio':audio,
 'limitations':['RMS matching does not establish equal loudness or equal perceived duration',
 'Same physical F0 does not prove identical perceived pitch',
 'MDS distances are stipulated and unrelated to synthesized sound judgments']}
(OUT/'verification.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'centroids_hz':centroids,'audio_files':len(audio),'figures':len(sizes),'mds_error':error},ensure_ascii=False))
