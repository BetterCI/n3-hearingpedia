import { readFile, readdir, writeFile } from 'node:fs/promises';
import assert from 'node:assert/strict';
import { parseFrontmatter } from '@astrojs/markdown-remark';
import { references } from '../src/data/references.ts';
import { knowledgeRelations, relationshipsFor } from '../src/data/relations.ts';

const folder = 'docs/research/carfac-2026-11-06';
const wiki = JSON.parse(await readFile('docs/research/wiki-evidence-map.json', 'utf8'));
const slugs = ['carfac-cochlear-model', 'auditory-computational-models'];
const files = new Set(await readdir('src/content/concepts'));
for (const slug of slugs) {
  const source = (await readFile(`src/content/concepts/${slug}.md`, 'utf8')).replaceAll('\r\n', '\n');
  const { frontmatter: data } = parseFrontmatter(source);
  const body = source.split('\n---\n').slice(1).join('\n---\n');
  const citations = [...body.matchAll(/\[(\d+)\]\(#ref-([^\s)]+)\)/g)];
  for (const caption of body.matchAll(/<figcaption>[\s\S]*?<\/figcaption>/g)) assert(!caption[0].includes('](#ref-') && !caption[0].includes('$'), 'Raw markdown in caption');
  for (const c of citations) assert.equal(data.references[Number(c[1]) - 1], c[2]);
  for (const c of body.matchAll(/href="#ref-([^"]+)">(\d+)<\/a>/g)) assert.equal(data.references[Number(c[2]) - 1], c[1]);
  for (const id of data.references) {
    assert(references[id], 'Missing reference: ' + id);
    assert(body.includes('#ref-' + id), 'Unused reference: ' + id);
  }
  const links = [...new Set([...body.matchAll(/\]\(\.\.\/([^/]+)\/\)/g)].map(m => m[1]))];
  for (const link of links) assert(files.has(link + '.md'), 'Missing target: ' + link);
  const record = { slug, knowledge_area: data.knowledge_area, kind: data.kind,
    chinese_characters: (body.match(/[\u3400-\u9fff]/g) || []).length,
    body_characters: body.length, sections: (body.match(/^## /gm) || []).length,
    subsections: (body.match(/^### /gm) || []).length,
    reference_ids: data.references, wiki_links: links, status: data.status, depth: data.depth };
  const i = wiki.entries.findIndex(e => e.slug === slug);
  if (process.argv.includes('--write')) {
    if (i < 0) wiki.entries.push(record); else wiki.entries[i] = { ...wiki.entries[i], ...record };
  } else {
    assert(i >= 0, 'Missing evidence record: ' + slug);
    for (const key of ['chinese_characters', 'sections', 'subsections', 'reference_ids', 'wiki_links']) assert.deepEqual(wiki.entries[i][key], record[key], key);
  }
  if (slug === 'carfac-cochlear-model') {
    assert.equal(data.depth, 'in-depth'); assert.equal(data.status, 'draft');
    assert.equal(data.reviewer, null); assert.equal(data.reviewed_at, null);
    assert(record.chinese_characters >= 5000);
    const imgs = [...body.matchAll(/<img src="([^"]+)"/g)];
    assert.equal(imgs.length, 4);
    for (const img of imgs) await readFile('public' + img[1].replace('/n3-hearingpedia', ''));
    assert(relationshipsFor(slug).length >= 10);
    await writeFile(folder + '/content-verification.json', JSON.stringify({ ...record, citations: citations.length, figures: imgs.length, relationships: relationshipsFor(slug).length }, null, 2) + '\n');
  }
}
if (process.argv.includes('--write')) {
  wiki.relations = knowledgeRelations.length;
  await writeFile('docs/research/wiki-evidence-map.json', JSON.stringify(wiki, null, 2) + '\n');
}
const computation = JSON.parse(await readFile(folder + '/figure-verification.json', 'utf8'));
assert(computation.all_outputs_finite);
assert(computation.preserved_state_max_absolute_error <= 1e-12);
assert(computation.reset_state_max_absolute_error > 0);
assert.equal(computation.upstream_commit, 'a9fba19ac76c6b8052d1d4a2973f91450fb4d1d8');
console.log('CARFAC: references, links, draft status, evidence records, four figures and computed state-continuity checks passed.');
