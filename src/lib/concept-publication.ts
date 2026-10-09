import { execFileSync } from 'node:child_process';

interface PublicationEntry {
  data: { slug: string; last_updated: string; order: number };
}

// First-parent history records when content enters the publishing branch,
// including merges of drafts whose original commits were written earlier.
export function getConceptPublicationRanks(root = process.cwd()): Map<string, number> {
  const history = execFileSync('git', [
    'log', '--first-parent', '--format=commit:%H', '--name-only',
    '--', 'src/content/concepts',
  ], { cwd: root, encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 });
  const ranks = new Map<string, number>();
  let rank = -1;
  for (const line of history.split(/\r?\n/)) {
    if (line.startsWith('commit:')) {
      rank++;
      continue;
    }
    const match = line.match(/^src\/content\/concepts\/([^/]+)\.md$/);
    if (match && !ranks.has(match[1])) ranks.set(match[1], rank);
  }
  return ranks;
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
