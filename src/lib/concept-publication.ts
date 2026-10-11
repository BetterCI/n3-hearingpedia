import { execFileSync } from 'node:child_process';

interface PublicationEntry {
  data: { slug: string; last_updated: string; order: number };
}

// First-parent history records when content enters the publishing branch,
// including merges of drafts whose original commits were written earlier.
export function getConceptPublicationUpdates(root = process.cwd()): Map<string, { rank: number; date: string }> {
  let history: string;
  try {
    history = execFileSync('git', [
      'log', '--first-parent', '--format=commit:%H:%ct', '--name-only',
      '--', 'src/content/concepts',
    ], { cwd: root, encoding: 'utf8', maxBuffer: 8 * 1024 * 1024, stdio: ['ignore','pipe','pipe'] });
  } catch (error) {
    const failure = error as { code?: string; stderr?: Buffer };
    // Source archives lack Git history; the comparator falls back to dates/order.
    if (failure.code === 'ENOENT' || /not a git repository/i.test(failure.stderr?.toString() || '')) return new Map();
    throw error;
  }
  const updates = new Map<string, { rank: number; date: string }>();
  const dateFormat = new Intl.DateTimeFormat('en', { timeZone: 'Asia/Shanghai', year: 'numeric', month: '2-digit', day: '2-digit' });
  let rank = -1;
  let date = '';
  for (const line of history.split(/\r?\n/)) {
    const commit = line.match(/^commit:[a-f0-9]+:(\d+)$/);
    if (commit) {
      rank++;
      const parts = dateFormat.formatToParts(new Date(Number(commit[1])*1000));
      date = ['year','month','day'].map(type=>parts.find(part=>part.type===type)!.value).join('-');
      continue;
    }
    const match = line.match(/^src\/content\/concepts\/([^/]+)\.md$/);
    if (match && !updates.has(match[1])) updates.set(match[1], { rank, date });
  }
  return updates;
}

export function getConceptPublicationRanks(root = process.cwd()): Map<string, number> {
  return new Map([...getConceptPublicationUpdates(root)].map(([slug,update])=>[slug,update.rank]));
}

export function compareConceptPublication(
  a: PublicationEntry, b: PublicationEntry, ranks: ReadonlyMap<string, number>,
): number {
  const publicationOrder = (ranks.get(a.data.slug) ?? Number.MAX_SAFE_INTEGER)
    - (ranks.get(b.data.slug) ?? Number.MAX_SAFE_INTEGER);
  return publicationOrder
    || b.data.last_updated.localeCompare(a.data.last_updated)
    || a.data.order - b.data.order;
}
