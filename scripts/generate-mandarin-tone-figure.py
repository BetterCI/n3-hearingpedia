"""Draw illustrative citation-tone F0 contours, not recorded speech or normative data.

Run from the repository root. Dependencies: scripts/figures-requirements.txt.
The committed SVG embeds glyph paths so Chinese and tone marks render consistently.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_candidates = [
    Path('C:/Windows/Fonts/msyh.ttc'),
    Path('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'),
]
font_path = next((p for p in font_candidates if p.exists()), None)
if font_path is None:
    raise RuntimeError('Install a CJK font or add its path to font_candidates.')
font_manager.fontManager.addfont(str(font_path))
font_name = font_manager.FontProperties(fname=str(font_path)).get_name()
plt.rcParams.update({
    'font.family': [font_name, 'DejaVu Sans'], 'font.size': 11,
    'svg.fonttype': 'path', 'axes.spines.top': False, 'axes.spines.right': False,
    'axes.labelcolor': '#526579', 'text.color': '#253a51',
    'axes.edgecolor': '#c4cfdc', 'xtick.color': '#526579', 'ytick.color': '#526579',
})
u = np.linspace(0, 1, 301)
smooth = 3*u*u - 2*u*u*u
turn = .43
fall = np.clip(u/turn, 0, 1)
rise = np.clip((u-turn)/(1-turn), 0, 1)
tones = [
    ('妈', 'mā', '第一声 · 阴平 · 高平', '#237ca7', np.full_like(u, 225.)),
    ('麻', 'má', '第二声 · 阳平 · 上升', '#39896e', 155 + 70*smooth),
    ('马', 'mǎ', '第三声 · 上声 · 降升', '#9362a5', 155 - 45*np.sin(fall*np.pi/2) + 85*rise*rise),
    ('骂', 'mà', '第四声 · 去声 · 下降', '#c8783f', 235 - 120*smooth),
]
fig, axes = plt.subplots(2, 2, figsize=(9.0, 7.2))
fig.patch.set_facecolor('#f7f9fc')
fig.suptitle('普通话汉语声调：妈 · 麻 · 马 · 骂', fontsize=21, fontweight='bold', y=.976)
fig.text(.5, .916, '相同音节 ma，不同声调：文字、拼音与基频轮廓', ha='center', fontsize=12, color='#667b90')
for ax, (hanzi, pinyin, name, color, f0) in zip(axes.flat, tones):
    ax.set_facecolor('#ffffff')
    ax.text(.02, 1.20, hanzi, transform=ax.transAxes, fontsize=33, fontweight='bold', color=color)
    ax.text(.21, 1.24, pinyin, transform=ax.transAxes, fontsize=22, color=color)
    ax.text(.21, 1.08, name, transform=ax.transAxes, fontsize=11, color='#526579')
    ax.plot(u, f0, color=color, lw=3.3, solid_capstyle='round')
    ax.scatter([u[0], u[-1]], [f0[0], f0[-1]], color=color, s=24, zorder=3)
    ax.set(xlim=(-.04, 1.04), ylim=(95, 250), xlabel='音节归一化时间', ylabel='基频 F₀（Hz）')
    ax.set_xticks([0, .5, 1], ['0', '0.5', '1'])
    ax.set_yticks([100, 150, 200, 250])
    ax.grid(color='#e8edf3', lw=.8)
    ax.set_axisbelow(True)
fig.subplots_adjust(left=.09, right=.965, bottom=.135, top=.775, hspace=1.05, wspace=.30)
fig.text(.5, .052, '教学示意，非实测或统一标准值；四图采用相同坐标尺度。', ha='center', fontsize=11, color='#526579')
fig.text(.5, .023, '第三声绘为孤立音节的完整降升示意；自然语流可呈低降、变调或其他语境变体。', ha='center', fontsize=10, color='#667b90')
out = Path('public/figures/mandarin-four-tones.svg')
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, metadata={'Date': None, 'Description': 'Original idealized illustration; not empirical speech, normative F0 values, or a reproduction of a paper figure.'})
# Add a readable description in addition to the embedded glyph paths.
svg = out.read_text(encoding='utf8')
pos = svg.index('>', svg.index('<svg')) + 1
svg = svg[:pos] + '\n<title>普通话汉语声调：妈 mā、麻 má、马 mǎ、骂 mà 的基频曲线示意</title>\n<desc>四个音节归一化时间与基频 Hz 曲线面板，分别为高平、上升、降升和下降。曲线仅供教学，不是实测或统一标准值；第三声在自然语流中可不同。</desc>' + svg[pos:]
out.write_text(svg, encoding='utf8')
preview = Path('artifacts/figure-preview/mandarin-four-tones.png')
preview.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(preview, dpi=160)
plt.close(fig)
print(out)
print(preview)
