"""Copy only this draft's owned files and narrow registry additions to the shared checkout."""
from pathlib import Path
import shutil, json, sys
ROOT=Path(__file__).resolve().parents[1]
TARGET=Path('C:/AI_Lab/n³ Hearingpedia')
SLUG='electroacoustic-transducer'
if ROOT.resolve()==TARGET.resolve():
    print('Already in the shared checkout; synchronization is unnecessary.')
    sys.exit(0)
for rel in [f'src/content/concepts/{SLUG}.md',f'src/data/{SLUG}-references.ts',f'scripts/research-{SLUG}.py',f'scripts/generate-{SLUG}.py',f'scripts/fetch-{SLUG}-photos.py',f'scripts/register-{SLUG}.py',f'scripts/screen-{SLUG}.py',f'scripts/render-{SLUG}-draft.mjs',f'scripts/sync-{SLUG}.py',f'docs/drafts/{SLUG}-preview.html',f'docs/drafts/{SLUG}-review-2026-10-10.md']:
    src=ROOT/rel;dest=TARGET/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
for rel in [f'public/figures/{SLUG}',f'docs/research/{SLUG}-2026-10-10',f'docs/drafts/assets/{SLUG}']:
    shutil.copytree(ROOT/rel,TARGET/rel,dirs_exist_ok=True)
# Preserve all other user edits. Never replace a shared file with the isolated version.
p=TARGET/'src/data/references.ts';s=p.read_text(encoding='utf-8')
imp="import { electroacousticTransducerReferences } from './electroacoustic-transducer-references.ts';\n"
if imp.strip() not in s:s=imp+s
if '  ...electroacousticTransducerReferences,' not in s:s=s.replace('export const references: Record<string, Reference> = {','export const references: Record<string, Reference> = {\n  ...electroacousticTransducerReferences,',1)
p.write_text(s,encoding='utf-8')
p=TARGET/'src/data/relations.ts';s=p.read_text(encoding='utf-8')
edges=[line for line in (ROOT/'src/data/relations.ts').read_text(encoding='utf-8').splitlines() if "link('electroacoustic-transducer'," in line]
assert len(edges)==10
if "link('electroacoustic-transducer'," not in s:s=s.replace('export const knowledgeRelations: KnowledgeRelation[] = [','export const knowledgeRelations: KnowledgeRelation[] = [\n'+'\n'.join(edges),1)
p.write_text(s,encoding='utf-8')
p=TARGET/'src/data/paths.ts';s=p.read_text(encoding='utf-8')
row=next(line for line in (ROOT/'src/data/paths.ts').read_text(encoding='utf-8').splitlines() if "id:'electroacoustic-transducer'" in line)
if "id:'electroacoustic-transducer'" not in s:s=s.replace('export const learningPaths = [','export const learningPaths = [\n'+row,1)
p.write_text(s,encoding='utf-8')
print('Copied owned draft files; preserved unrelated shared checkout edits.')
