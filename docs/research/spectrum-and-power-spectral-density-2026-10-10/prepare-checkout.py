"""Integrate only this draft into the existing isolated publication checkout."""
from pathlib import Path
import shutil
import sys
sys.stdout.reconfigure(encoding='utf-8')
root=Path(__file__).resolve().parents[3]
dst=Path('C:/Users/mengq/.codex/worktrees/sound-waves-release/n³ Hearingpedia')
slug='spectrum-and-power-spectral-density'
for name in [f'src/content/concepts/{slug}.md','src/data/spectrum-psd-references.ts',
             'scripts/generate-spectrum-psd.py','scripts/render-spectrum-psd-draft.mjs']:
    shutil.copyfile(root/name,dst/name)
shutil.copytree(root/f'public/figures/{slug}',dst/f'public/figures/{slug}',dirs_exist_ok=True)
p=dst/'src/data/references.ts';s=p.read_text(encoding='utf-8')
if 'spectrumPsdReferences' not in s:
    s="import { spectrumPsdReferences } from './spectrum-psd-references.ts';\n"+s
    s=s.replace('export const references: Record<string, Reference> = {','export const references: Record<string, Reference> = {\n  ...spectrumPsdReferences,')
    p.write_text(s,encoding='utf-8')
p=dst/'src/data/relations.ts';s=p.read_text(encoding='utf-8')
if slug not in s:
    own=[line for line in (root/'src/data/relations.ts').read_text(encoding='utf-8').splitlines() if 'link(' in line and slug in line]
    assert len(own)==6
    s=s.replace('export const knowledgeRelations: KnowledgeRelation[] = [','export const knowledgeRelations: KnowledgeRelation[] = [\n'+'\n'.join(own))
    p.write_text(s,encoding='utf-8')
p=dst/'src/data/paths.ts';s=p.read_text(encoding='utf-8')
if slug not in s:
    anchor="'pure-and-complex-tones',"
    assert anchor in s
    s=s.replace(anchor,anchor+"'"+slug+"',",1)
    p.write_text(s,encoding='utf-8')
shutil.copytree(Path(__file__).resolve().parent,dst/'docs/research'/Path(__file__).resolve().parent.name,dirs_exist_ok=True)
print('Draft integrated without copying unrelated source changes.')
