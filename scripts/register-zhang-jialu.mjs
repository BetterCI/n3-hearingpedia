// Update only this article's evidence record and export its actual source scopes.
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { zhangJialuReferences } from '../src/data/zhang-jialu-references.ts';
import { knowledgeRelations } from '../src/data/relations.ts';
const slug = 'zhang-jialu';
const source = (await readFile(`src/content/concepts/${slug}.md`, 'utf8')).replaceAll('\r\n', '\n');
const body = source.split(/\n---\n/).slice(1).join('\n---\n');
const record = {
  slug, knowledge_area: 'perception', kind: 'person',
  chinese_characters: (body.match(/[\u3400-\u9fff]/g) || []).length,
  body_characters: body.length,
  sections: (body.match(/^## /gm) || []).length,
  subsections: (body.match(/^### /gm) || []).length,
  reference_ids: JSON.parse(source.match(/^references: (.+)$/m)[1]),
  wiki_links: [...new Set([...body.matchAll(/\.\.\/([a-z0-9-]+)\//g)].map(m => m[1]))],
  status: 'draft', depth: 'in-depth',
};
const path = 'docs/research/wiki-evidence-map.json';
const map = JSON.parse(await readFile(path, 'utf8'));
const index = map.entries.findIndex(e => e.slug === slug);
if (index === -1) map.entries.push(record); else map.entries[index] = record;
map.date = '2026-10-25';
map.relations = knowledgeRelations.length;
await writeFile(path, JSON.stringify(map, null, 2) + '\n');
const out = `docs/research/${slug}-2026-10-25`;
await mkdir(out, { recursive: true });
await writeFile(`${out}/source-ledger.json`, JSON.stringify(Object.entries(zhangJialuReferences).map(([id, ref]) => ({id, ...ref, checked_at: '2026-10-25'})), null, 2) + '\n');
await writeFile(`${out}/entry-metrics.json`, JSON.stringify(record, null, 2) + '\n');
for (const [label, id] of [...body.matchAll(/\[(\d+)\]\(#ref-([^\s)]+)/g)].map(m => [m[1],m[2]])) {
  if (record.reference_ids[Number(label)-1] !== id) throw new Error(`Citation order mismatch: ${id}`);
}
if (!record.reference_ids.every(id => zhangJialuReferences[id])) throw new Error('Missing registered source');
console.log(JSON.stringify(record, null, 2));
