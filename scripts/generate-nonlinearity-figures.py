from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json
root=Path(__file__).resolve().parents[1];out=root/'public/figures/nonlinearity-and-distortion';out.mkdir(parents=True,exist_ok=True)
x=np.linspace(-2,2,1001)
fig,ax=plt.subplots(figsize=(9,4));ax.plot(x,x,label='Linear');ax.plot(x,np.tanh(x),label='Soft saturation');ax.plot(x,np.clip(x,-1,1),label='Hard clipping');ax.set(xlabel='Input (normalized)',ylabel='Output (normalized)');ax.legend();ax.grid(alpha=.2);fig.tight_layout();fig.savefig(out/'curves.svg');fig.savefig(out/'curves.png',dpi=160);plt.close(fig)
fs=48000;t=np.arange(fs)/fs
amp=lambda z:2*abs(np.fft.rfft(z))/len(z)
x=.5*np.cos(2*np.pi*1000*t);v=amp(x-.2*x**3)
x2=.25*(np.cos(2*np.pi*1000*t)+np.cos(2*np.pi*1300*t));v2=amp(x2-.2*x2**3)
assert np.isclose(v[1000],.48125,atol=1e-12)
assert np.isclose(v[3000],.00625,atol=1e-12)
assert np.isclose(v2[700],.00234375,atol=1e-12)
assert np.isclose(v2[1600],.00234375,atol=1e-12)
fig,axs=plt.subplots(1,2,figsize=(11,4))
for ax,vv,title in zip(axs,[v,v2],['Single tone','Two tones']):
 ix=np.flatnonzero(vv>1e-8);ax.stem(ix,vv[ix]);ax.set(xlim=(0,4200),xlabel='Frequency (Hz)',ylabel='Peak amplitude',title=title);ax.grid(alpha=.2)
fig.tight_layout();fig.savefig(out/'spectra.svg');fig.savefig(out/'spectra.png',dpi=160)
result={'fs':fs,'samples':fs,'fundamental':float(v[1000]),'third_harmonic':float(v[3000]),'THD_percent':float(100*v[3000]/v[1000]),'THD_dB':float(20*np.log10(v[3000]/v[1000])),'IMD_700':float(v2[700]),'IMD_1600':float(v2[1600]),'assertions':'passed'}
(root/'docs/research/nonlinearity-and-distortion-2026-11-23/numerical-validation.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(result)
