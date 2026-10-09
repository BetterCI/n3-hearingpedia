"""Generate original teaching figures for the five Mandarin phonetics articles.

Purpose: show syllable roles, articulator pairings, airflow conditions and source timing.
Inputs: constants are teaching choices; HEARINGPEDIA_FIGURE_FONT optionally selects a CJK font.
Outputs: one editable SVG and one PNG per article, plus a JSON provenance record.
Side effects: writes only public/figures/<article>/ and the scoped research directory.
Dependencies: NumPy, Matplotlib, Pillow and a CJK font (Windows Microsoft YaHei by default).
Boundary/errors: missing dependencies/fonts fail explicitly; no original papers are copied.
Usage: python scripts/generate-mandarin-phonetics-figures.py
Update history: 2026-10-09, initial contributor-guide figure set.
Copyright: Huali Zhou, zhouhuali224@gmail.com
School of Electronics and Information Engineering, Heyuan Polytechnic, Heyuan, Guangdong, China.
"""

from pathlib import Path
from PIL import Image
import json
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = REPO_ROOT / "public" / "figures"
RESEARCH_ROOT = REPO_ROOT / "docs" / "research" / "mandarin-phonetics-guide-2026-10-09"
FONT_FILE = Path(os.environ.get("HEARINGPEDIA_FIGURE_FONT", "C:/Windows/Fonts/msyh.ttc"))
BLUE = "#176b92"
PURPLE = "#744e9e"
INK = "#203040"
GRAY = "#7c8792"
BORDER = "#c6cfd8"
LIGHT = "#f2f6f9"
SAMPLE_RATE_HZ = 8000
PERIODIC_FREQUENCY_HZ = 150
RANDOM_SEED = 20261009
RELEASE_TIME_MS = 0
TEACHING_VOT_MS = (12, 60)


def configureStyle():
    """Configure readable Chinese/vector output with a small, consistent palette.

    Inputs: FONT_FILE and module constants. Output: none.
    Side effects: registers a local font and updates Matplotlib rendering defaults.
    Missing font raises FileNotFoundError. Usage: call once before making figures.
    """
    if not FONT_FILE.is_file():
        raise FileNotFoundError(f"Chinese font missing: {FONT_FILE}")
    font_manager.fontManager.addfont(str(FONT_FILE))
    plt.rcParams.update({
        "font.family": [font_manager.FontProperties(fname=str(FONT_FILE)).get_name(), "DejaVu Sans"],
        "svg.fonttype": "none", "axes.unicode_minus": False,
        "figure.facecolor": "white", "savefig.facecolor": "white",
        "text.color": INK, "axes.labelcolor": INK, "xtick.color": INK,
        "ytick.color": INK, "axes.spines.top": False, "axes.spines.right": False,
    })


def makeCanvas(height, title, subtitle):
    """Create a white teaching-diagram canvas with 1200 horizontal SVG units.

    Inputs: positive height, title and subtitle strings. Output: (figure, axes).
    Side effects: creates Matplotlib artists; no files are written.
    Invalid dimensions follow Matplotlib errors. Usage: makeCanvas(1000, title, note).
    """
    figure = plt.figure(figsize=(1200 / 72, height / 72), dpi=72)
    axes = figure.add_axes([0, 0, 1, 1])
    axes.set_xlim(0, 1200)
    axes.set_ylim(height, 0)
    axes.axis("off")
    axes.text(55, 62, title, fontsize=42, weight="bold", va="center")
    axes.text(55, 118, subtitle, fontsize=27, color=GRAY, va="center")
    return figure, axes


def addBox(axes, x, y, width, height, label, detail="", color=BLUE):
    """Add one labeled rectangle representing a category, condition or process.

    Inputs: axes, rectangle coordinates, label/detail and accent color. Output: none.
    Side effects: adds a box and text artists; geometry is not an anatomical measure.
    Inputs are internal fixed layout values. Usage: addBox(ax, 100, 200, 300, 100, name).
    """
    axes.add_patch(FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0,rounding_size=13",
                                edgecolor=color, facecolor=LIGHT, linewidth=2.2))
    if detail:
        axes.text(x + width / 2, y + height * .36, label, ha="center", va="center",
                  fontsize=36, weight="bold", color=color)
        axes.text(x + width / 2, y + height * .72, detail, ha="center", va="center", fontsize=30)
    else:
        axes.text(x + width / 2, y + height / 2, label, ha="center", va="center", fontsize=35)


def addArrow(axes, start, end, color=INK):
    """Connect two diagram elements without encoding measured magnitude.

    Inputs: axes, coordinate pairs and color. Output: none.
    Side effects: adds an arrow artist. Internal coordinates must be finite.
    Usage: addArrow(ax, (450, 300), (580, 300)).
    """
    axes.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=27,
                                  linewidth=2.7, color=color, shrinkA=6, shrinkB=6))


def makeSyllableFigure():
    """Illustrate syllable positions and spelling with three Mandarin examples.

    Inputs: none. Output: Matplotlib figure; no numerical speech data are used.
    Side effects: creates artists. Boxes encode roles, never durations or distances.
    Usage: exportFigure(makeSyllableFigure(), 'mandarin-consonants', 'consonant-system').
    """
    figure, axes = makeCanvas(1100, "音节位置与拼音记写", "声母是位置概念；字母、辅音和音节成分不能直接等同")
    examples = [("（a）妈 mā", "第一声", "声母 m", "双唇鼻音", "韵母 a", "主要元音"),
                ("（b）衣 yī", "第一声", "零声母", "无常规辅音声母", "韵母 i", "y 参与拼写")]
    for index, example in enumerate(examples):
        label, tone, initial, initialNote, rhyme, rhymeNote = example
        top = 210 + index * 290
        axes.text(65, top + 72, label, fontsize=35, weight="bold", va="center")
        axes.text(715, top - 30, f"声调：{tone}（依附音节）", fontsize=32, ha="center")
        addBox(axes, 300, top + 25, 370, 125, initial, initialNote)
        addBox(axes, 715, top + 25, 415, 125, rhyme, rhymeNote, PURPLE)
        axes.plot([310, 1120], [top - 4, top - 4], color=GRAY, linewidth=2)
    top = 790
    axes.text(65, top + 75, "（c）昂 áng", fontsize=35, weight="bold", va="center")
    axes.text(715, top - 30, "声调：第二声（依附音节）", fontsize=32, ha="center")
    addBox(axes, 300, top + 25, 265, 125, "零声母")
    addBox(axes, 590, top + 25, 250, 125, "a", "主要元音", PURPLE)
    addBox(axes, 870, top + 25, 260, 125, "ng", "鼻音韵尾", PURPLE)
    axes.plot([310, 1120], [top - 4, top - 4], color=GRAY, linewidth=2)
    axes.text(65, 1020, "韵尾 ng 不列入 21 个常规声母；图中框宽不表示真实发音时长。", fontsize=28)
    return figure


def makePlaceFigure():
    """Show seven traditional place categories as articulator/target pairings.

    Inputs: none. Output: original relation diagram, not a midsagittal anatomy drawing.
    Side effects: creates artists. Rows/columns do not represent measured distances.
    Usage: exportFigure(makePlaceFigure(), 'consonant-place-of-articulation', 'articulator-pairs').
    """
    figure, axes = makeCanvas(1380, "主动器官与被动目标的配对", "部位索引：从口腔前部向后部整理；不是按比例的口腔剖面")
    axes.text(285, 190, "主要主动器官", fontsize=34, ha="center", weight="bold")
    axes.text(700, 190, "接近或接触的目标", fontsize=34, ha="center", weight="bold")
    axes.text(1050, 190, "拼音例项", fontsize=30, ha="center", weight="bold")
    rows = [("下唇", "上唇", "双唇", "b、p、m"),
            ("下唇", "上门齿", "唇齿", "f"),
            ("舌尖或舌端", "齿龈附近", "舌尖中", "d、t、n、l"),
            ("舌尖或舌叶", "上齿 / 齿龈前部", "舌尖前", "z、c、s"),
            ("舌前部", "齿龈后区域", "舌尖后", "zh、ch、sh、r"),
            ("舌面前部", "龈腭 / 前部硬腭", "舌面前", "j、q、x"),
            ("舌背后部", "软腭附近", "舌根", "g、k、h")]
    for index, (active, passive, place, examples) in enumerate(rows):
        y = 250 + index * 140
        addBox(axes, 100, y, 350, 98, active)
        addArrow(axes, (465, y + 48), (535, y + 48))
        addBox(axes, 550, y, 350, 98, passive, color=PURPLE)
        axes.text(1050, y + 31, place, fontsize=30, ha="center", weight="bold")
        axes.text(1050, y + 75, examples, fontsize=28, ha="center")
    axes.text(65, 1285, "双唇可共同接近；同一部位仍可有闭塞、摩擦、鼻腔或舌侧通气。", fontsize=28)
    axes.text(65, 1335, "箭头只表示器官配对；实际舌形与接触区域可随说话人、元音改变。", fontsize=27, color=GRAY)
    return figure


def makeMannerFigure():
    """Compare closure/release and oral, nasal, lateral airflow conditions.

    Inputs: none. Output: five-row schematic process/condition diagram.
    Side effects: creates artists; arrows are explanatory links, not flow-rate data.
    Usage: exportFigure(makeMannerFigure(), 'consonant-manner-of-articulation', 'airflow-manners').
    """
    figure, axes = makeCanvas(1210, "阻塞、释放与气流通路", "（a）（b）看闭塞怎样释放；（c）看狭窄；（d）（e）看通气路线")
    rows = [("（a）塞音", "完全闭塞", "随后释放", "鼻腔通常关闭"),
            ("（b）塞擦音", "完全闭塞", "窄通道摩擦释放", "闭塞与摩擦紧密相连"),
            ("（c）擦音", "保持狭窄", "持续口腔摩擦", "不要求起始完全闭塞"),
            ("（d）鼻音", "口腔闭塞", "鼻腔通路开放", "软腭下降，气流经鼻腔"),
            ("（e）边音", "口腔中央阻碍", "舌侧通路保留", "l 主要经口腔侧向通气")]
    for index, (label, state, outcome, note) in enumerate(rows):
        y = 225 + index * 165
        axes.text(65, y + 42, label, fontsize=33, weight="bold", va="center")
        addBox(axes, 340, y, 300, 94, state)
        addArrow(axes, (655, y + 47), (715, y + 47))
        addBox(axes, 730, y, 390, 94, outcome, color=PURPLE)
        axes.text(730, y + 132, note, fontsize=29)
    axes.text(65, 1085, "箭头表示过程或通气条件的联系，不表示解剖位置、流速或持续时间。", fontsize=27, color=GRAY)
    axes.text(65, 1150, "（d）（e）是同时成立的通气条件，并非先后动作。", fontsize=28, color=GRAY)
    return figure


def makeAspirationFigure():
    """Generate two synthetic release-to-periodicity timing examples.

    Inputs: fixed 8 kHz sampling, 150 Hz periodicity, seed and 12/60 ms delays.
    Output: figure and parameter dictionary. Side effects: creates artists only.
    Waveforms are toy signals, not recordings, language norms or classifiers.
    Usage: exportFigure(makeAspirationFigure()[0], 'aspiration', 'aspiration-timing').
    """
    timeMs = np.arange(-20, 100, 1000 / SAMPLE_RATE_HZ)
    randomGenerator = np.random.default_rng(RANDOM_SEED)
    noise = randomGenerator.normal(0, .16, timeMs.size)
    waveforms = []
    for delayMs in TEACHING_VOT_MS:
        waveform = np.zeros_like(timeMs)
        noiseMask = (timeMs >= 0) & (timeMs < delayMs)
        periodicMask = timeMs >= delayMs
        waveform[noiseMask] = noise[noiseMask]
        waveform[periodicMask] = .68 * np.sin(2 * np.pi * PERIODIC_FREQUENCY_HZ * (timeMs[periodicMask] - delayMs) / 1000)
        waveform += np.where(timeMs >= 0, .9 * np.exp(-(timeMs / .35) ** 2), 0)
        waveforms.append(waveform)
    commonScale = max(np.max(np.abs(w)) for w in waveforms)
    figure, axes = plt.subplots(2, 1, figsize=(1200 / 72, 1000 / 72), sharex=True)
    figure.subplots_adjust(left=.13, right=.96, bottom=.13, top=.78, hspace=.8)
    figure.suptitle("释放与周期振动开始的相对时序", fontsize=39, y=.97, weight="bold")
    figure.text(.05, .9, "教学合成信号：12 / 60 ms 与 150 Hz 为选参，非实测或普通话常模", fontsize=25, color=GRAY)
    labels = ["（a）不送气时序的教学例子", "（b）送气时序的教学例子"]
    for index, (axesItem, delayMs, waveform) in enumerate(zip(axes, TEACHING_VOT_MS, waveforms)):
        axesItem.plot(timeMs, waveform / commonScale, color=INK, linewidth=1.5)
        axesItem.axvspan(0, delayMs, color=BLUE, alpha=.12)
        axesItem.axvline(0, color=INK, linestyle=":", linewidth=2.3)
        axesItem.axvline(delayMs, color=PURPLE, linestyle="--", linewidth=2.3)
        axesItem.set_title(labels[index], fontsize=31, loc="left", pad=64)
        axesItem.text(.02, 1.05, f"释放 0 ms → 周期开始 {delayMs} ms", transform=axesItem.transAxes, fontsize=26)
        axesItem.set_ylim(-1.13, 1.13)
        axesItem.set_ylabel("相对幅度\n（无量纲）", fontsize=29)
        axesItem.set_yticks([-1, 0, 1])
        axesItem.tick_params(labelsize=25)
        axesItem.spines["left"].set_color(BORDER)
        axesItem.spines["bottom"].set_color(BORDER)
    axes[-1].set_xlabel("时间（ms）；0 表示闭塞释放", fontsize=29, labelpad=18)
    axes[-1].set_xticks([-20, 0, 20, 40, 60, 80, 100])
    parameters = {"sample_rate_hz": SAMPLE_RATE_HZ, "periodic_frequency_hz": PERIODIC_FREQUENCY_HZ,
                  "seed": RANDOM_SEED, "release_ms": RELEASE_TIME_MS, "periodicity_onset_ms": list(TEACHING_VOT_MS),
                  "time_window_ms": [-20, 100], "normalization": "common peak magnitude across both examples",
                  "noise_standard_deviation": .16, "periodic_amplitude_before_normalization": .68,
                  "release_pulse_amplitude": .9, "release_pulse_width_ms": .35}
    return figure, parameters


def makeVoicingFigure():
    """Generate periodic, noise and mixed toy source components on shared scales.

    Inputs: fixed 8 kHz sampling, 150 Hz periodicity and deterministic seed.
    Output: figure and parameter dictionary. Side effects: creates artists only.
    Periodicity is a possible cue, not a sufficient definition of all voiced consonants.
    Usage: exportFigure(makeVoicingFigure()[0], 'voicing', 'voicing-patterns').
    """
    timeMs = np.arange(0, 40, 1000 / SAMPLE_RATE_HZ)
    randomGenerator = np.random.default_rng(RANDOM_SEED + 1)
    periodic = .65 * np.sin(2 * np.pi * PERIODIC_FREQUENCY_HZ * timeMs / 1000)
    noise = randomGenerator.normal(0, .25, timeMs.size)
    mixed = periodic + .55 * noise
    commonScale = max(np.max(np.abs(w)) for w in [periodic, noise, mixed])
    figure, axes = plt.subplots(3, 1, figsize=(1200 / 72, 1120 / 72), sharex=True)
    figure.subplots_adjust(left=.13, right=.96, bottom=.12, top=.82, hspace=.76)
    figure.suptitle("周期振动、噪声与两者混合", fontsize=41, y=.97, weight="bold")
    figure.text(.05, .915, "合成信号示例：周期源选用 150 Hz；波形并非任何真实辅音的录音", fontsize=26, color=GRAY)
    labels = ["（a）周期分量", "（b）非周期噪声分量", "（c）周期与噪声的混合"]
    for axesItem, waveform, label in zip(axes, [periodic, noise, mixed], labels):
        axesItem.plot(timeMs, waveform / commonScale, color=INK, linewidth=1.6)
        axesItem.set_title(label, fontsize=31, loc="left", pad=15)
        axesItem.set_ylim(-1.15, 1.15)
        axesItem.set_ylabel("相对幅度\n（无量纲）", fontsize=28)
        axesItem.set_yticks([-1, 0, 1])
        axesItem.tick_params(labelsize=25)
        axesItem.spines["left"].set_color(BORDER)
        axesItem.spines["bottom"].set_color(BORDER)
    axes[-1].set_xlabel("时间（ms）", fontsize=30, labelpad=20)
    axes[-1].set_xticks([0, 10, 20, 30, 40])
    return figure, {"sample_rate_hz": SAMPLE_RATE_HZ, "periodic_frequency_hz": PERIODIC_FREQUENCY_HZ,
                    "seed": RANDOM_SEED + 1, "time_window_ms": [0, 40], "noise_standard_deviation": .25,
                    "periodic_amplitude_before_normalization": .65, "mixed_noise_weight": .55,
                    "normalization": "common peak magnitude across all three examples"}


def exportFigure(figure, slug, name):
    """Save an editable SVG and matching PNG, then close the figure.

    Inputs: figure, canonical article slug and descriptive basename. Output: path record.
    Side effects: creates the scoped public directory and writes two original images.
    Export errors propagate; paths are fixed by main. Usage: exportFigure(fig, slug, name).
    """
    folder = OUTPUT_ROOT / slug
    folder.mkdir(parents=True, exist_ok=True)
    svgPath = folder / f"{name}.svg"
    pngPath = folder / f"{name}.png"
    figure.savefig(svgPath, format="svg", metadata={"Creator": "n³ Hearingpedia; AI-assisted original teaching figure"})
    svgText = svgPath.read_text(encoding="utf-8")
    svgPath.write_text("\n".join(line.rstrip() for line in svgText.splitlines()) + "\n", encoding="utf-8")
    figure.savefig(pngPath, format="png", dpi=72)
    plt.close(figure)
    with Image.open(pngPath) as preview:
        pngDimensions = list(preview.size)
    return {"slug": slug, "svg": svgPath.relative_to(REPO_ROOT).as_posix(),
            "png": pngPath.relative_to(REPO_ROOT).as_posix(), "png_dimensions": pngDimensions}


def main():
    """Generate all five figure pairs and their truthful provenance manifest.

    Inputs: script constants and verified conceptual sources. Output: printed path JSON.
    Side effects: saves images and a research manifest; no external downloads or git actions.
    Raises dependency, font or export errors. Usage: execute this script from the repository.
    """
    configureStyle()
    records = [
        exportFigure(makeSyllableFigure(), "mandarin-consonants", "consonant-system"),
        exportFigure(makePlaceFigure(), "consonant-place-of-articulation", "articulator-pairs"),
        exportFigure(makeMannerFigure(), "consonant-manner-of-articulation", "airflow-manners"),
    ]
    aspirationFigure, aspirationParameters = makeAspirationFigure()
    records.append(exportFigure(aspirationFigure, "aspiration", "aspiration-timing"))
    voicingFigure, voicingParameters = makeVoicingFigure()
    records.append(exportFigure(voicingFigure, "voicing", "voicing-patterns"))
    sourceMap = {
        "mandarin-consonants": ["hanyu-pinyin-scheme", "lee-zee-standard-chinese-2003"],
        "consonant-place-of-articulation": ["essentials-consonant-place-phonation", "lee-zee-standard-chinese-2003"],
        "consonant-manner-of-articulation": ["essentials-consonant-manner", "lee-zee-standard-chinese-2003"],
        "aspiration": ["essentials-vot-phonemes", "lee-zee-standard-chinese-2003"],
        "voicing": ["essentials-consonant-place-phonation", "essentials-consonant-manner"],
    }
    for record in records:
        record.update({"nature": "original educational diagram or synthetic signal; not empirical data",
                       "creator": "n³ Hearingpedia, AI-assisted code and editorial verification",
                       "principle_sources": sourceMap[record["slug"]], "original_source_figure": None,
                       "reproduction": "No third-party figure copied or traced",
                       "usage": "Created for display, editing and publication in this repository; no separate external reuse license assigned",
                       "generator": "scripts/generate-mandarin-phonetics-figures.py"})
    RESEARCH_ROOT.mkdir(parents=True, exist_ok=True)
    manifest = {"date": "2026-10-09", "figures": records,
                "parameters": {"aspiration": aspirationParameters, "voicing": voicingParameters},
                "limits": "Diagrams omit individual anatomy and coarticulation; toy waves do not establish norms or perceptual boundaries."}
    (RESEARCH_ROOT / "figure-sources.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"generated": len(records), "records": records}, ensure_ascii=False))


if __name__ == "__main__":
    main()
