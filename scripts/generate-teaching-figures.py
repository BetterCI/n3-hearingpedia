"""Generate idealized teaching plots; none are empirical measurements.

Optional dependencies: scripts/figures-requirements.txt.
Run from the repository root. SVG files are committed and require no Python at build time.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path('public/figures')
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.labelcolor': '#293c52', 'text.color': '#293c52',
                     'axes.edgecolor': '#b0bbca', 'grid.color': '#dfe5ed',
                     'svg.fonttype': 'none'})
COLORS = ['#2375a2', '#d78738', '#557f69']

def save(fig, name):
    fig.tight_layout(pad=1.5)
    fig.savefig(OUT / (name + '.svg'), metadata={'Date': None, 'Description': 'Idealized teaching illustration, not empirical data.'})
    Path('artifacts/figure-preview').mkdir(parents=True, exist_ok=True)
    fig.savefig(Path('artifacts/figure-preview') / (name + '.png'), dpi=140)
    plt.close(fig)

fig, ax = plt.subplots(figsize=(7.2, 3.2))
x = np.linspace(0, 1, 400)
ax.semilogy(x, 165.4*(10**(2.1*x)-0.88), color=COLORS[0], lw=2.3)
ax.set(xlabel='Normalized position: apex (0) to base (1)', ylabel='Frequency (Hz)',
       title='Greenwood mapping: coordinate convention matters')
ax.grid(alpha=.6)
save(fig, 'frequency-place')

fig, axes = plt.subplots(1, 2, figsize=(7.8, 3.1))
f = np.linspace(400, 1600, 800)
for p, color in [(20, COLORS[0]), (40, COLORS[1])]:
    g = np.abs(f-1000)/1000
    w = (1+p*g)*np.exp(-p*g)
    axes[0].plot(f, 10*np.log10(w), color=color, label=f'p = {p}')
axes[0].set(xlabel='Frequency (Hz)', ylabel='Power weight (dB)', ylim=(-55, 2), title='Symmetric roex examples')
axes[0].legend(frameon=False)
fc = np.linspace(100, 8000, 400)
axes[1].plot(fc, 24.7*(4.37*fc/1000+1), color=COLORS[0])
axes[1].set(xlabel='Center frequency (Hz)', ylabel='ERB (Hz)', title='Common ERB-N approximation')
for ax in axes: ax.grid(alpha=.45)
save(fig, 'auditory-filter')

fig, axes = plt.subplots(2, 1, figsize=(7.2, 3.6), sharex=True)
t = np.linspace(0, .1, 5000)
m = .7
env = 1+m*np.cos(2*np.pi*20*t)
carrier = np.cos(2*np.pi*400*t)
axes[0].plot(t*1000, env*carrier, color=COLORS[0], lw=.8, label='AM waveform')
axes[0].plot(t*1000, env, color=COLORS[1], lw=2, label='Envelope')
axes[0].plot(t*1000, -env, color=COLORS[1], lw=1)
axes[0].set(ylabel='Amplitude', title='Envelope and rapid oscillation: an ideal AM signal')
axes[0].legend(frameon=False, loc='upper right')
axes[1].plot(t*1000, carrier, color=COLORS[2], lw=.8)
axes[1].set(xlabel='Time (ms)', ylabel='Normalized carrier', xlim=(0, 100))
save(fig, 'envelope-tfs')

fig, axes = plt.subplots(1, 2, figsize=(7.8, 3.2))
t = np.linspace(-.006, .006, 500)
df = np.linspace(-1200, 1200, 500)
for sigma, color in [(.0008, COLORS[0]), (.002, COLORS[1])]:
    axes[0].plot(t*1000, np.exp(-t*t/(2*sigma*sigma)), color=color, label=f'sigma_t = {sigma*1000:g} ms')
    axes[1].plot(df, np.exp(-2*np.pi**2*sigma*sigma*df*df), color=color)
axes[0].set(xlabel='Time relative to event center (ms)', ylabel='Normalized amplitude', title='Gaussian time envelope')
axes[0].legend(frameon=False, fontsize=9)
axes[1].set(xlabel='Frequency offset (Hz)', ylabel='Normalized Fourier amplitude', title='Shorter time, broader spectrum')
for ax in axes: ax.grid(alpha=.45)
save(fig, 'gaussian-width')

fig, ax = plt.subplots(figsize=(7.2, 3.2))
snr = np.linspace(-12, 4, 500)
for slope, color in [(.8, COLORS[0]), (1.8, COLORS[1])]:
    ax.plot(snr, .1+.88/(1+np.exp(-(snr+4)/slope)), color=color,
            label=f'Logistic scale = {slope:g} dB')
ax.axhline(.5, ls='--', color='#7e8999', lw=1, label='50% target')
ax.set(xlabel='SNR (dB)', ylabel='Probability correct', ylim=(0, 1.03),
       title='Same task, different psychometric slopes (idealized)')
ax.legend(frameon=False, fontsize=9)
ax.grid(alpha=.4)
save(fig, 'psychometric-function')

fig, axes = plt.subplots(2, 1, figsize=(7.2, 3.5), sharex=True)
t = np.linspace(0, .004, 800)
left = np.cos(2*np.pi*1000*t)
for ax, sign, title in [(axes[0], 1, 'Same-phase target: S0'), (axes[1], -1, 'Antiphasic target: S-pi')]:
    ax.plot(t*1000, left, color=COLORS[0], lw=2, label='Left')
    ax.plot(t*1000, sign*left, color=COLORS[1], lw=1.4, ls='--', label='Right')
    ax.set(ylabel='Amplitude', title=title, ylim=(-1.3, 1.3))
    ax.legend(frameon=False, fontsize=9, loc='upper right')
axes[1].set(xlabel='Time (ms)', xlim=(0, 4))
save(fig, 'binaural-phase')
