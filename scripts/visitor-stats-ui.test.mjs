import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { runInNewContext } from 'node:vm';
import ts from 'typescript';

const source = (await readFile(new URL('../src/scripts/visitor-stats.ts', import.meta.url), 'utf8'))
  .replace("import analytics from '../data/analytics.json';", 'const analytics = { baiduSiteId: "0213110796858a57e43a0bd3fc744126" };');
const compiled = ts.transpileModule(source, { compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.CommonJS } }).outputText;
const summary = (visits, provider) => ({ provider, visits, start: '2026-09-10T16:00:00Z', end: '2026-10-09T16:00:00Z',
  updatedAt: '2026-10-11T01:00:00Z', countries: [{ name: '中国', visits }] });

async function render(snapshot, hostname = 'betterci.github.io') {
  const scripts = [];
  const panel = { hidden: true };
  const sections = ['baidu', 'goatcounter'].map(provider => ({
    hidden: true, dataset: { statsSource: provider, statsUrl: '/visitor-stats.json', counterSite: 'https://n3hearing.goatcounter.com' },
    nodes: new Map(),
    querySelector(selector) {
      if (!this.nodes.has(selector)) this.nodes.set(selector, { textContent: '', children: [],
        append(item) { this.children.push(item); }, replaceChildren() { this.children = []; } });
      return this.nodes.get(selector);
    },
  }));
  let fetches = 0;
  const context = { exports: {}, window: {}, location: { hostname, pathname: '/n3-hearingpedia/' }, AbortSignal,
    fetch: async () => { fetches++; return { ok: true, json: async () => snapshot }; },
    document: {
      querySelector: selector => selector === '.visitor-stats' ? sections[0]
        : selector === '.visitor-stats-panel' ? panel : scripts.find(item => `#${item.id}` === selector),
      querySelectorAll: () => sections,
      createElement: () => ({ dataset: {}, textContent: '' }),
      head: { append: script => scripts.push(script) },
    },
  };
  runInNewContext(compiled, context);
  context.exports.initVisitorStats();
  await new Promise(resolve => setImmediate(resolve));
  return { context, sections, scripts, fetches, panel };
}

test('renders both providers with independent counts and loads each tracker only once', async () => {
  const { context, sections, scripts, fetches, panel } = await render({ sources: { baidu: summary(12, 'baidu'), goatcounter: summary(17) } });
  assert.equal(panel.hidden, false);
  assert.equal(fetches, 1);
  assert.equal(scripts.length, 2);
  assert.equal(sections[0].querySelector('[data-stats-visits]').textContent, '12');
  assert.equal(sections[1].querySelector('[data-stats-visits]').textContent, '17');
  assert.equal(sections[0].querySelector('[data-stats-visits-label]').textContent, '访问次数');
  assert.equal(sections[1].querySelector('[data-stats-visits-label]').textContent, '访问人次');
  assert(sections.every(section => !section.hidden));
  context.exports.initVisitorStats();
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(scripts.length, 2);
  assert.equal(sections[0].querySelector('ul').children.length, 1);
});

test('keeps legacy GoatCounter snapshots working and excludes local previews from both trackers', async () => {
  const { sections, scripts } = await render(summary(17), 'localhost');
  assert.equal(scripts.length, 0);
  assert.equal(sections[0].hidden, true);
  assert.equal(sections[1].hidden, false);
});

test('a missing provider remains hidden while the other provider displays its real data', async () => {
  const { sections } = await render({ sources: { baidu: summary(12, 'baidu') } });
  assert.equal(sections[0].hidden, false);
  assert.equal(sections[1].hidden, true);
});

test('the unified panel stays hidden when neither source has a snapshot', async () => {
  const { sections, panel } = await render({ sources: {} });
  assert.equal(panel.hidden, true);
  assert(sections.every(section => section.hidden));
});
