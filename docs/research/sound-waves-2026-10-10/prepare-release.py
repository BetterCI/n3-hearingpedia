"""Copy only this entry and merge its navigation into a clean origin/main checkout."""
from pathlib import Path
import json
import re
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[3]
DEST = Path(sys.argv[1]).resolve()
slug = 'sound-waves-and-propagation'
entry = ROOT / f'src/content/concepts/{slug}.md'
text = entry.read_text(encoding='utf-8')
# These two entries exist locally but have not been published. Keep the explanations.
for target in ['sound-pressure-level', 'interaural-level-difference']:
    text = re.sub(r'\[([^\]]+)\]\(\.\./' + target + r'/\)', r'\1', text)
entry.write_text(text, encoding='utf-8')
relations = ROOT / 'src/data/relations.ts'
s = relations.read_text(encoding='utf-8')
s = s.replace("link('sound-pressure-level','sound-waves-and-propagation','describes','声压级描述给定位置与时窗内的声压幅度标度。',3)", "link('sound-waves-and-propagation','loudness','related','声压的物理标度与听者的响度感知需要区分。',2)")
s = s.replace("link('sound-waves-and-propagation','interaural-level-difference','mechanism','头部附近的绕射与声影使两耳声级差依赖频率和方向。',3)", "link('sound-waves-and-propagation','spatial-hearing','mechanism','传播路径与头部附近绕射共同影响空间听觉输入。',3)")
relations.write_text(s, encoding='utf-8')

for relative in [f'src/content/concepts/{slug}.md', 'src/data/sound-waves-references.ts', 'scripts/generate-sound-waves.py', 'scripts/render-sound-waves-draft.mjs']:
    dst = DEST / relative
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / relative, dst)
for relative in [f'public/figures/{slug}', 'docs/research/sound-waves-2026-10-10']:
    shutil.copytree(ROOT / relative, DEST / relative, dirs_exist_ok=True)

p = DEST / 'src/data/references.ts'
s = p.read_text(encoding='utf-8')
assert 'soundWavesReferences' not in s
s = "import { soundWavesReferences } from './sound-waves-references.ts';\n" + s
s = s.replace('export const references: Record<string, Reference> = {', 'export const references: Record<string, Reference> = {\n  ...soundWavesReferences,')
p.write_text(s, encoding='utf-8')
p = DEST / 'src/data/relations.ts'
s = p.read_text(encoding='utf-8')
edges = '\n'.join(line for line in relations.read_text(encoding='utf-8').splitlines() if "link(" in line and slug in line)
assert len(edges.splitlines()) == 6
s = s.replace('export const knowledgeRelations: KnowledgeRelation[] = [', 'export const knowledgeRelations: KnowledgeRelation[] = [\n' + edges)
p.write_text(s, encoding='utf-8')
p = DEST / 'src/data/paths.ts'
s = p.read_text(encoding='utf-8')
s = s.replace("slugs:['fundamental-frequency','harmonicity'", "slugs:['sound-waves-and-propagation','fundamental-frequency','harmonicity'", 1)
s = s.replace("description:'区分基频、谐波、共振峰、动态范围与时域表征，理解相同声音的不同表示。'", "description:'从声波传播进入基频、谐波、共振峰、动态范围与时域表征，理解相同声音的不同表示。'", 1)
assert slug in s
p.write_text(s, encoding='utf-8')
print(json.dumps({'destination': str(DEST), 'article_copied': slug, 'merged_relations': 6, 'unpublished_links_removed': 2}, ensure_ascii=False))
