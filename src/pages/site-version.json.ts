import { execFileSync } from 'node:child_process';
import { getCollection } from 'astro:content';
import type { APIRoute } from 'astro';
import packageInfo from '../../package.json';
import { summarizeSite } from '../lib/site-statistics';

export const prerender = true;

export const GET: APIRoute = async () => {
  let sourceCommit: string | null = null;
  let workingTreeDirty: boolean | null = null;
  try {
    sourceCommit = execFileSync('git', ['rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();
    workingTreeDirty = execFileSync('git', ['status', '--porcelain'], { encoding: 'utf8' }).trim().length > 0;
  } catch {
    // Source archives can still build without a Git checkout.
  }
  const ciCommit = process.env.GITHUB_SHA;
  if (ciCommit && /^[a-f0-9]{40}$/.test(ciCommit)) {
    if (sourceCommit && sourceCommit !== ciCommit) throw new Error('CI commit differs from checked-out source');
    sourceCommit = ciCommit;
  }
  return new Response(JSON.stringify({
    version: packageInfo.version,
    sourceCommit,
    workingTreeDirty,
    builtAt: new Date().toISOString(),
    statistics: summarizeSite(await getCollection('concepts')),
  }, null, 2), { headers: { 'Content-Type': 'application/json; charset=utf-8' } });
};
