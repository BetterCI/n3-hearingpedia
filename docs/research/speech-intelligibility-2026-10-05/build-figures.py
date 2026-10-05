"""Original, reproducible teaching figures; no empirical listener measurements."""
from pathlib import Path
import json
import numpy as np
from scipy import signal, ndimage
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import patches, font_manager
from PIL import Image, ImageOps, ImageDraw

OUT = Path(__file__).resolve().parent
font_manager.fontManager.addfont('C:/Windows/Fonts/msyh.ttc')
FONT = font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttc').get_name()
plt.rcParams.update({
    'font.family': [FONT, 'DejaVu Sans'], 'font.size': 12,
    'axes.titlesize': 13, 'axes.labelsize': 12, 'xtick.labelsize': 11,
    'ytick.labelsize': 11, 'legend.fontsize': 10.5, 'svg.fonttype': 'none',
    'axes.spines.top': False, 'axes.spines.right': False,
    'axes.linewidth': .8, 'axes.edgecolor': '#555555',
    'text.color': '#222222', 'axes.labelcolor': '#222222',
    'xtick.color': '#333333', 'ytick.color': '#333333',
    'figure.facecolor': 'white', 'axes.facecolor': 'white',
    'savefig.facecolor': 'white', 'axes.unicode_minus': False,
})
C = dict(blue='#0072b2', orange='#d55e00', green='#00846b', grey='#777777', ink='#222222')
manifest = []

def save(fig, name, title, description):
    fig.savefig(OUT / f'{name}.svg', metadata={'Date': None, 'Title': title, 'Description': description})
    fig.savefig(OUT / f'{name}.png', dpi=180)
    width, height = fig.get_size_inches() * 72
    manifest.append(dict(name=name, title=title, width=float(width), height=float(height)))
    plt.close(fig)

def title(ax, letter, text):
    ax.set_title(f'({letter}) {text}', loc='left', pad=12)

def arrow(ax, points, color, dashed=False, lw=1.6):
    for i, (a, b) in enumerate(zip(points[:-1], points[1:])):
        ax.annotate('', xy=b, xytext=a, arrowprops=dict(
            arrowstyle='->' if i == len(points)-2 else '-', color=color, lw=lw,
            linestyle='--' if dashed else '-', shrinkA=0, shrinkB=0))

def person(ax, x, y, color, label):
    ax.add_patch(patches.Circle((x, y+.07), .043, facecolor='white', edgecolor=color, lw=1.5))
    ax.add_patch(patches.Arc((x, y-.005), .13, .10, theta1=0, theta2=180, color=color, lw=1.5))
    ax.plot([x-.065, x-.065], [y-.005, y-.07], color=color, lw=1.5)
    ax.plot([x+.065, x+.065], [y-.005, y-.07], color=color, lw=1.5)
    ax.text(x, y-.12, label, ha='center', va='top', fontsize=11)

fig, axes = plt.subplots(1, 3, figsize=(12, 3.65), layout='constrained')
for ax in axes:
    ax.set(xlim=(0, 1), ylim=(0, 1)); ax.set_aspect('equal'); ax.axis('off')
title(axes[0], 'a', '安静对话')
person(axes[0], .18, .56, C['blue'], '目标说话人')
person(axes[0], .80, .56, C['ink'], '听者')
arrow(axes[0], [(.28, .61), (.70, .61)], C['blue'])
axes[0].text(.49, .67, '目标言语', ha='center', fontsize=11, color=C['blue'])
title(axes[1], 'b', '多人交谈')
person(axes[1], .16, .69, C['blue'], '目标')
person(axes[1], .15, .30, C['orange'], '干扰说话人')
person(axes[1], .46, .25, C['orange'], '干扰')
person(axes[1], .82, .58, C['ink'], '听者')
arrow(axes[1], [(.25, .74), (.71, .64)], C['blue'])
arrow(axes[1], [(.24, .34), (.72, .59)], C['orange'])
arrow(axes[1], [(.54, .30), (.74, .55)], C['orange'])
title(axes[2], 'c', '混响房间')
axes[2].plot([.03, .03, .97, .97], [.18, .87, .87, .18], color='#aaaaaa', lw=1.2)
person(axes[2], .18, .50, C['blue'], '目标说话人')
person(axes[2], .81, .50, C['ink'], '听者')
arrow(axes[2], [(.28, .55), (.71, .55)], C['blue'])
arrow(axes[2], [(.25, .62), (.49, .86), (.75, .61)], C['grey'], True)
arrow(axes[2], [(.25, .56), (.96, .74), (.76, .57)], C['grey'], True)
axes[2].text(.51, .66, '反射声', ha='center', fontsize=11, color=C['grey'])
axes[2].text(.51, .47, '直达声', ha='center', fontsize=11, color=C['blue'])
save(fig, '01-listening-scenes', '不同环境中的言语聆听', 'Original qualitative scene schematic, not a comparison of measured intelligibility.')

FS = 16000
t = np.arange(round(.90*FS))/FS

def synthetic(f0, shift=0., gain=1.):
    """Three nonlexical vowel-like harmonic segments, with raised-sine envelopes."""
    result = np.zeros_like(t)
    sections = [(0.03, .24, (500, 1500, 2500)), (.30, .53, (350, 2200, 2800)), (.59, .83, (700, 1100, 2450))]
    for begin, end, centres in sections:
        mask = (t >= begin) & (t < end)
        tau = t[mask]-begin
        env = np.sin(np.pi*tau/(end-begin))**1.3
        frequencies = np.arange(1, 31)*f0
        centres = np.asarray(centres) + shift
        normalised_offset = (frequencies[:, None]-centres)/np.array([90, 150, 220])
        amplitudes = (.02+np.exp(-.5*normalised_offset**2).sum(axis=1))/np.arange(1, 31)**.35
        carrier = (amplitudes[:, None]*np.sin(2*np.pi*frequencies[:, None]*tau)).sum(axis=0)
        carrier /= np.sqrt(np.mean(carrier**2))
        result[mask] = gain*env*carrier
    return result

x = synthetic(130.)
x /= np.sqrt(np.mean(x*x))
# Match whole-record RMS first, then apply one common peak-normalization factor.
# Independent peak normalization would change the comparison's 0 dB SNR.
rng = np.random.default_rng(20261005)
freq, power = signal.welch(x, FS, nperseg=512)
smoothed = ndimage.gaussian_filter1d(power, 2.0)
fft_freq = np.fft.rfftfreq(len(t), 1/FS)
shaping = np.sqrt(np.interp(fft_freq, freq, smoothed))
noise = np.fft.irfft(np.fft.rfft(rng.normal(size=len(t)))*shaping, n=len(t))
noise /= np.sqrt(np.mean(noise**2))
modulator = .08+.92*(.5+.5*np.cos(2*np.pi*4*t))**2
fluctuating = noise*modulator; fluctuating /= np.sqrt(np.mean(fluctuating**2))
competitor = np.roll(synthetic(205., shift=130.), round(.085*FS))
competitor /= np.sqrt(np.mean(competitor**2))
common_peak = max(np.abs(a).max() for a in [x, noise, fluctuating, competitor])
x /= common_peak
backgrounds = [a/common_peak for a in [noise, fluctuating, competitor]]
reference_rms = float(np.sqrt(np.mean(x*x)))
from scipy.io import wavfile
wavfile.write(OUT/'synthetic-teaching-signal.wav', FS, x.astype(np.float32))
bands = [(250, 550), (1200, 1800), (2400, 3200)]
band_signals, envelopes = [], []
for lo, hi in bands:
    band = signal.sosfiltfilt(signal.butter(4, [lo, hi], btype='bandpass', fs=FS, output='sos'), x)
    envelope = np.abs(signal.hilbert(band))
    envelope = signal.sosfiltfilt(signal.butter(3, 20, fs=FS, output='sos'), envelope)
    band_signals.append(band); envelopes.append(np.maximum(envelope, 0))
f, ts, spec = signal.spectrogram(x, FS, window='hann', nperseg=512, noverlap=448, mode='magnitude')
db = 20*np.log10(np.maximum(spec, 1e-10)/spec.max())
waveform_limit = 1.0
envelope_limit = float(max(env.max() for env in envelopes)*1.6)
fig, axes = plt.subplots(2, 2, figsize=(12, 8.0), layout='constrained')
ax = axes[0,0]; title(ax, 'a', '合成教学信号的波形')
ax.plot(t, x, color=C['blue'], lw=.65); ax.set(xlim=(0, .9), xlabel='时间（秒）', ylabel='相对幅度', ylim=(-waveform_limit, waveform_limit), yticks=[-1, -.5, 0, .5, 1])
ax = axes[0,1]; title(ax, 'b', '同一信号的声谱图')
visible_frequencies = f <= 4000
im = ax.pcolormesh(ts, f[visible_frequencies]/1000, db[visible_frequencies], cmap='cividis', vmin=-55, vmax=0, shading='auto', rasterized=True)
ax.set(xlim=(0, .9), ylim=(0, 4), xlabel='时间（秒）', ylabel='频率（千赫）')
cb = fig.colorbar(im, ax=ax, shrink=.92, pad=.025); cb.set_label('相对幅度（dB）')
ax = axes[1,0]; title(ax, 'c', '不同频带的时域包络')
for env, (lo, hi), color in zip(envelopes, bands, [C['blue'], C['orange'], C['green']]):
    ax.plot(t, env, color=color, lw=1.8, label=f'{lo}—{hi} Hz')
ax.set(xlim=(0, .9), xlabel='时间（秒）', ylabel='相对幅度', ylim=(0, envelope_limit)); ax.legend(frameon=False, loc='upper right')
ax = axes[1,1]; title(ax, 'd', '带内振荡与包络')
mask = (t >= .105) & (t <= .145)
band = band_signals[0]; raw_env = np.abs(signal.hilbert(band))
ax.plot(t[mask]*1000, band[mask], lw=1.2, color=C['blue'], label='带内波形')
ax.plot(t[mask]*1000, raw_env[mask], color=C['orange'], lw=1.8, label='解析信号幅度')
ax.plot(t[mask]*1000, -raw_env[mask], color=C['orange'], lw=1.1, linestyle='--')
detail_peak = float(max(np.abs(band[mask]).max(), raw_env[mask].max()))
ax.set(xlabel='时间（毫秒）', ylabel='相对幅度', ylim=(-1.15*detail_peak, 1.7*detail_peak)); ax.legend(frameon=False, loc='upper left')
save(fig, '02-acoustic-cues', '合成信号的频谱与时域线索', 'Computed from one synthetic nonlexical vowel-like signal. Not a human recording or a neural measurement.')

background_limit = 1.0
def short_level(y):
    rms = np.sqrt(np.maximum(ndimage.uniform_filter1d(y*y, size=round(.020*FS), mode='constant'), 1e-8))
    return 20*np.log10(rms/reference_rms)

fig, axes = plt.subplots(2, 3, figsize=(12, 6.4), layout='constrained', sharex=True, sharey='row')
for i, (bg, label) in enumerate(zip(backgrounds, ['稳态有色噪声', '起伏噪声', '类言语干扰'])):
    ax = axes[0,i]; title(ax, 'abc'[i], label)
    ax.plot(t, bg, color=C['orange'], lw=.65); ax.set(xlim=(0, .9), ylim=(-background_limit, background_limit), yticks=[-1, -.5, 0, .5, 1])
    ax = axes[1,i]
    ax.plot(t, short_level(bg), color=C['orange'], lw=1.6, label='背景')
    ax.plot(t, short_level(x), color=C['blue'], lw=1.4, linestyle='--', label='共同目标')
    ax.axhline(0, color='#bbbbbb', lw=.8, linestyle=':')
    ax.set(xlim=(0, .9), ylim=(-40, 12), xlabel='时间（秒）')
    ax.legend(frameon=False, loc='lower left')
axes[0,0].set_ylabel('背景相对幅度')
axes[1,0].set_ylabel('短时相对级（dB）')
save(fig, '03-background-conditions', '相同总体信噪比下的背景时间结构', 'Common peak normalization keeps all waveforms within [-1, 1], preserving equal whole-record RMS and 0 dB SNR. Not measured masking or intelligibility data.')

def psychometric(snr, alpha, beta, gamma=0., lapse=0.):
    return gamma+(1-gamma-lapse)/(1+np.exp(-(snr-alpha)/beta))
snr = np.linspace(-12, 4, 700)
fig, axes = plt.subplots(2, 2, figsize=(12, 8), layout='constrained')
for ax in axes.flat:
    ax.set(xlim=(-12, 4), ylim=(0, 103), xlabel='信噪比（dB）', ylabel='正确率（%）', yticks=[0,25,50,75,100])
    ax.grid(axis='y', color='#e4e4e4', lw=.65)
ax = axes[0,0]; title(ax, 'a', '阈值移动')
for alpha, color, label in [(-6, C['blue'], '条件甲：阈值 -6 dB'), (-3, C['orange'], '条件乙：阈值 -3 dB')]:
    ax.plot(snr, 100*psychometric(snr, alpha, 1.2), color=color, lw=2, label=label)
    ax.plot([alpha, alpha], [0, 50], color=color, lw=1, linestyle='--')
ax.axhline(50, color=C['grey'], lw=1, linestyle='--'); ax.legend(frameon=False, loc='upper left')
ax = axes[0,1]; title(ax, 'b', '相同阈值，不同斜率')
for beta, color, label in [(.8, C['blue'], '尺度 0.8 dB'), (1.8, C['orange'], '尺度 1.8 dB')]:
    ax.plot(snr, 100*psychometric(snr, -4, beta), color=color, lw=2, label=label)
ax.plot([-4], [50], 'o', color=C['ink'], ms=4); ax.axhline(50, color=C['grey'], lw=1, linestyle='--')
ax.legend(frameon=False, loc='upper left')
ax = axes[1,0]; title(ax, 'c', '机会水平与上限')
ax.plot(snr, 100*psychometric(snr, -4, 1.2, .10, .02), color=C['blue'], lw=2)
for value, ls in [(10, ':'), (50, '--'), (98, ':')]: ax.axhline(value, color=C['grey'], lw=.9, linestyle=ls)
ax.plot([-4], [54], 'o', color=C['ink'], ms=4)
ax.annotate('曲线中点：54%', xy=(-4,54), xytext=(-10.8,70), fontsize=11, arrowprops=dict(arrowstyle='->', lw=1, color=C['ink']))
ax.text(-11.2, 13, '下限：10%', fontsize=10.5); ax.text(-11.2, 90, '上限：98%', fontsize=10.5)
ax.text(.1, 52, '50%目标', fontsize=10, color=C['grey'])
ax = axes[1,1]; title(ax, 'd', '地板与天花板效应')
ax.axvspan(-12, -9, color='#ededed'); ax.axvspan(0, 4, color='#ededed')
for alpha, color, label in [(-5, C['blue'], '条件甲'), (-3, C['orange'], '条件乙')]:
    ax.plot(snr, 100*psychometric(snr, alpha, .8), color=color, lw=2, label=label)
ax.text(-10.5, 25, '地板区', fontsize=11, ha='center'); ax.text(2, 78, '天花板区', fontsize=11, ha='center')
ax.legend(frameon=False, loc='upper left', bbox_to_anchor=(.25,.98))
save(fig, '04-psychometric-functions', '正确率、阈值、斜率与上下限', 'Four idealized logistic examples with explicitly specified parameters, not normative data.')

correct_a = np.ones((10,5), dtype=bool); correct_a[8:] = False
correct_b = np.ones((10,5), dtype=bool)
for row in range(10): correct_b[row, row%5] = False
fig, axes = plt.subplots(1,2, figsize=(11,6.6), layout='constrained')
for ax, answers, letter, heading in zip(axes, [correct_a, correct_b], 'ab', ['错误集中于少数句子', '每句均有一个漏词']):
    title(ax, letter, heading)
    for row in range(10):
        for col in range(5):
            ax.scatter(col, row, s=95, marker='o' if answers[row,col] else 'x', color=C['green'] if answers[row,col] else C['orange'], linewidth=1.8)
    ax.set(xlim=(-.7,4.7), ylim=(12,-.7), xticks=range(5), xticklabels=[f'词{i}' for i in range(1,6)], yticks=range(10), yticklabels=[f'句{i}' for i in range(1,11)])
    ax.tick_params(length=0); ax.xaxis.tick_top()
    for spine in ax.spines.values(): spine.set_visible(False)
    words = int(answers.sum()); sentences = int(answers.all(axis=1).sum())
    ax.text(2,10.6,f'词正确率：{words}/50 = {words/50:.0%}',ha='center',fontsize=12.5)
    ax.text(2,11.4,f'整句正确率：{sentences}/10 = {sentences/10:.0%}',ha='center',fontsize=12.5)
save(fig, '05-scoring-units', '相同词正确率与不同整句正确率', 'Two constructed answer patterns; circles are correct and crosses incorrect. Both score 80% words; complete sentences score 80% and 0%. Not listener data.')

checks = dict(
    samplingRateHz=FS, durationSeconds=len(t)/FS, fundamentalFrequencyHz=130,
    envelopeBandsHz=bands, envelopeLowpassHz=20, rmsWindowMilliseconds=20,
    waveformPeak=float(np.abs(x).max()), waveformPlotLimit=waveform_limit,
    backgroundPeaks=[float(np.abs(bg).max()) for bg in backgrounds], backgroundPlotLimit=background_limit,
    commonPeakNormalizationFactor=float(common_peak), commonRms=reference_rms,
    backgroundSnrDb=[float(20*np.log10(np.sqrt(np.mean(x*x))/np.sqrt(np.mean(bg*bg)))) for bg in backgrounds],
    psychometricMidpointPercent=100*psychometric(-4, -4, 1.2, .1, .02),
    wordCorrectPercent=[float(100*a.mean()) for a in [correct_a,correct_b]],
    sentenceCorrectPercent=[float(100*a.all(axis=1).mean()) for a in [correct_a,correct_b]],
    finiteSignals=bool(all(np.isfinite(a).all() for a in [x,*backgrounds,*envelopes])),
    files=manifest, style='White background, Chinese labels, lettered panels; captions and evidence in article.'
)
assert max(abs(v) for v in checks['backgroundSnrDb']) < 1e-10
assert checks['psychometricMidpointPercent'] == 54
assert checks['wordCorrectPercent'] == [80,80] and checks['sentenceCorrectPercent'] == [80,0]
assert checks['finiteSignals']
assert checks['waveformPeak'] < waveform_limit
assert max(checks['backgroundPeaks']) <= background_limit
(OUT/'figure-verification.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2)+'\n', encoding='utf8')

thumbs = []
for record in manifest:
    image = Image.open(OUT/(record['name']+'.png')).convert('RGB')
    image.thumbnail((1100,760))
    tile = Image.new('RGB', (1140, image.height+54), 'white')
    tile.paste(image, ((1140-image.width)//2,42)); ImageDraw.Draw(tile).text((20,10), record['name'], fill='#222222')
    thumbs.append(tile)
sheet = Image.new('RGB',(1140,sum(i.height for i in thumbs)+30*(len(thumbs)-1)),'#eeeeee')
y=0
for tile in thumbs: sheet.paste(tile,(0,y)); y+=tile.height+30
sheet.save(OUT/'figure-overview.png')
print(json.dumps(checks, ensure_ascii=False))
