"""Rebuild the three original teaching SVGs; uses no historical experimental data."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/figures/zhang-jialu'
OUT.mkdir(parents=True, exist_ok=True)
BLUE, ORANGE, INK = '#296b91', '#b76523', '#243648'

def text(x, y, value, size=26, fill=INK, anchor='start', weight='400'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{escape(value)}</text>'

def rect(x, y, w, h, fill='#f1f6f9', stroke='#b7c9d4'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'

def arrow(x1, y1, x2, y2):
    return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#6c8291" stroke-width="3" fill="none" marker-end="url(#arrow)"/>'

def save(name, height, title, description, elements):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="{height}" viewBox="0 0 1280 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6" fill="#6c8291"/></marker></defs>
<rect width="1280" height="{height}" fill="white"/>
<g font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif">{''.join(elements)}</g></svg>'''
    (OUT / name).write_text(svg + '\n', encoding='utf-8')

items = [text(50, 58, '从物理信号到听者反应', 34, weight='600'), text(50, 100, '三个对象分别描述，再建立可以检验的联系', 25, '#526778')]
for x, title, a, b, foot in [
    (50, '声学信号', '频谱 · 时长 · 周期变化', '刺激与传输条件', '测量声音保留了什么'),
    (460, '语言结构', '声母 · 韵母 · 声调', '合法组合与候选类别', '说明计分单位和约束'),
    (870, '听者反应', '正确 · 混淆 · 自然度', '任务、选项与个体条件', '观察听者实际报告什么'),
]:
    items += [rect(x, 146, 360, 200), text(x+180, 193, title, 30, BLUE, 'middle', '600'), text(x+180, 241, a, 24, anchor='middle'), text(x+180, 282, b, 24, anchor='middle'), text(x+180, 324, foot, 22, '#526778', 'middle'), arrow(x+180, 353, x+180, 405)]
items += [rect(50, 413, 1180, 95, '#f8f5ef', '#d7c7b5'), text(640, 454, '清晰度的统计关系  →  混淆与知觉空间  →  语音系统评价', 29, anchor='middle', weight='600'), text(640, 490, '分析用途可以互补，结论需回到原来的材料与任务检验', 24, '#526778', 'middle'), text(50, 565, '原创教学框图｜不表示神经通路或一套同名历史模型', 23, '#526778')]
save('research-framework.svg', 600, '信号、语言结构与听者反应', '由代表论文整理的研究框架，非神经通路图。', items)

matrix_a = [[80,20,0,0],[20,80,0,0],[0,0,80,20],[0,0,20,80]]
matrix_b = [[80,0,20,0],[0,80,0,20],[20,0,80,0],[0,20,0,80]]
assert all(sum(row) == 100 for matrix in [matrix_a, matrix_b] for row in matrix)
assert all(sum(matrix[i][i] for i in range(4)) / sum(map(sum, matrix)) == .8 for matrix in [matrix_a, matrix_b])
items = [text(50, 58, '正确率相同，错误去向不同', 34, weight='600'), text(50, 100, '行＝刺激，列＝反应；每类100次，数字为次数（也等于行百分比）', 25, '#526778')]
for x, name, matrix, explanation in [(140, '(a) 条件A：送气类别混淆', matrix_a, 'b ↔ p；d ↔ t'), (760, '(b) 条件B：发音部位混淆', matrix_b, 'b ↔ d；p ↔ t')]:
    items += [text(x+148, 152, name, 27, anchor='middle', weight='600'), text(x+148, 192, '反应', 23, '#526778', 'middle')]
    for i, label in enumerate(['b','p','d','t']):
        items += [text(x+i*78+37, 227, label, 27, anchor='middle'), text(x-25, 279+i*72, label, 27, anchor='middle')]
        for j, value in enumerate(matrix[i]):
            fill = '#dcecf5' if i == j else '#f7dfc7' if value else '#f7f8fa'
            color = BLUE if i == j else ORANGE if value else '#7b8b96'
            items += [rect(x+j*78, 244+i*72, 74, 68, fill, '#d4dde3'), text(x+j*78+37, 287+i*72, str(value), 27, color, 'middle', '600')]
    items += [text(x+148, 574, '320 / 400 ＝ 80%', 28, BLUE, 'middle', '600'), text(x+148, 614, explanation, 24, ORANGE, 'middle')]
items += [text(30, 393, '刺激', 22, '#526778'), text(650, 393, '刺激', 22, '#526778'), text(50, 649, '本站人为构造数据｜拼音符号只作类别标签，非历史实验结果', 22, '#526778')]
save('confusion-example.svg', 660, '两张正确率均为80%的混淆矩阵', 'A混淆送气类别，B混淆发音部位。每行100次，全部为教学设定。', items)

items = [text(50, 58, '合成语音：测量表现，也定位问题', 34, weight='600'), text(50, 100, '控制材料、重放和听者条件，分别记录三个评价结果', 25, '#526778'), rect(50, 165, 310, 200), text(205, 223, '规定测试条件', 29, BLUE, 'middle', '600'), text(205, 272, '同一组语音材料', 25, anchor='middle'), text(205, 315, '系统与自然语音对照', 24, anchor='middle')]
for y, title, sub in [(140, '听写与正确率', '记录辨认出的语言单位'), (253, '自然度评分', '明确量表刻度与文字锚点'), (366, '混淆与层次比较', '保留错误去向，形成诊断假设')]:
    items += [arrow(370, 265, 465, y+40), rect(480, y, 750, 90), text(505, y+36, title, 28, BLUE, weight='600'), text(505, y+72, sub, 24)]
items += [text(50, 508, '原创教学功能图｜不同结果分别解释；诊断假设还需后续实验检验', 24, '#526778')]
save('evaluation-chain.svg', 540, '合成语音评价的三个互补结果', '从受控语音输入分别测量辨认、自然度和混淆，不合成为通用总分。', items)

manifest = {'data_type': 'original teaching diagrams; no historical or participant data', 'matrices': {'A': matrix_a, 'B': matrix_b, 'rows': 'stimulus', 'columns': 'response', 'labels': ['b','p','d','t'], 'trials_per_row': 100, 'accuracy_each': .8}, 'probability_example': {'P_I': .8, 'P_F': .8, 'joint_bounds': [.6,.8], 'independent_joint': .64, 'P_F_given_I': .9, 'joint': .72, 'P_F_given_not_I': .4}, 'files': ['research-framework.svg','confusion-example.svg','evaluation-chain.svg']}
assert abs(.8*.9 + .2*.4 - .8) < 1e-12
assert abs(.8*.9-.72) < 1e-12
(OUT / 'figure-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print('Generated 3 SVGs; both matrices have accuracy 80%; probability example checked.')
