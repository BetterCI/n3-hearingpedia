import test from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { basename, dirname, join, resolve } from 'node:path';
import { getConceptPublicationRanks, compareConceptPublication } from '../src/lib/concept-publication.ts';

const entry = (slug, order, date = '2026-10-09') => ({ data: { slug, order, last_updated: date } });
const ordered = (entries, ranks) => [...entries].sort((a, b) => compareConceptPublication(a, b, ranks)).map(e => e.data.slug);

test('same-day updates and an older draft follow publishing history, even with identical commit timestamps', () => {
  const root = mkdtempSync(join(tmpdir(), 'hearingpedia-publication-'));
  const git = (...args) => execFileSync('git', args, {
    cwd: root, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'],
    env: { ...process.env, GIT_AUTHOR_DATE: '2026-10-09T10:00:00+08:00', GIT_COMMITTER_DATE: '2026-10-09T10:00:00+08:00' },
  });
  const publish = (slug, content) => {
    writeFileSync(join(root, 'src/content/concepts', slug + '.md'), content);
    git('add', '.');
    git('commit', '-m', slug);
  };
  try {
    git('init', '--initial-branch=main');
    git('config', 'user.name', 'Publication test');
    git('config', 'user.email', 'publication-test@example.invalid');
    git('config', 'commit.gpgsign', 'false');
    mkdirSync(join(root, 'src/content/concepts'), { recursive: true });
    publish('old', 'original');
    git('switch', '-c', 'draft');
    publish('draft', 'written before the next main update');
    git('switch', 'main');
    publish('middle', 'published while draft is pending');
    git('merge', '--no-ff', 'draft', '-m', 'Publish the older draft');
    const entries = [entry('old', 1), entry('middle', 2), entry('draft', 3)];
    assert.deepEqual(ordered(entries, getConceptPublicationRanks(root)), ['draft', 'middle', 'old']);
    publish('old', 'new substantive update');
    assert.deepEqual(ordered(entries, getConceptPublicationRanks(root)), ['old', 'draft', 'middle']);
    writeFileSync(join(root, 'README.md'), 'unrelated site update');
    git('add', '.');
    git('commit', '-m', 'Update README');
    assert.deepEqual(ordered(entries, getConceptPublicationRanks(root)), ['old', 'draft', 'middle']);
  } finally {
    assert.equal(dirname(resolve(root)), resolve(tmpdir()));
    assert(basename(root).startsWith('hearingpedia-publication-'));
    rmSync(root, { recursive: true, force: true });
  }
});

test('entries published together and untracked preview entries have deterministic fallback order', () => {
  const ranks = new Map([['a', 0], ['b', 0]]);
  assert.deepEqual(ordered([entry('b', 2), entry('a', 1), entry('preview', 0)], ranks), ['a', 'b', 'preview']);
  assert.deepEqual(ordered([entry('older', 1, '2026-10-08'), entry('newer', 2)], new Map()), ['newer', 'older']);
});
