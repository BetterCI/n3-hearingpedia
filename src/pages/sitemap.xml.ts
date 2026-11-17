import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { domains } from '../data/domains';
import { url } from '../lib/paths';

export const prerender = true;

// Discover static content pages without executing their templates. Dynamic
// concept and domain routes are expanded from the same data as their pages.
const staticPaths = Object.keys(import.meta.glob('./**/*.astro', { query: '?raw', import: 'default' }))
  .filter(file => !file.includes('['))
  .map(file => file.replace(/^\.\//, '').replace(/\.astro$/, '').replace(/(^|\/)index$/, ''))
  .filter(path => !['404', 'search'].includes(path) && !path.startsWith('share/'));

function escapeXml(value: string): string {
  return value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;').replaceAll("'", '&apos;');
}

export const GET: APIRoute = async ({ site }) => {
  if (!site) throw new Error('A site URL is required to generate the sitemap.');
  const concepts = await getCollection('concepts');
  const entries: { path: string; lastmod?: string }[] = [
    ...staticPaths.map(path => ({ path })),
    ...domains.map(domain => ({ path: `domains/${domain.id}` })),
    ...concepts.map(({ data }) => ({ path: `concepts/${data.slug}`, lastmod: data.last_updated })),
  ];
  const seen = new Set<string>();
  const items = entries.map(({ path, lastmod }) => {
    const loc = new URL(url(path), site).href;
    if (seen.has(loc)) throw new Error(`Duplicate sitemap URL: ${loc}`);
    seen.add(loc);
    if (lastmod !== undefined) {
      const date = new Date(`${lastmod}T00:00:00Z`);
      if (!/^\d{4}-\d{2}-\d{2}$/.test(lastmod) || !Number.isFinite(date.getTime())
        || date.toISOString().slice(0, 10) !== lastmod) {
        throw new Error(`Invalid last_updated for ${path}: ${lastmod}`);
      }
    }
    // Only articles have an editorial update date. A rebuild must not make
    // unchanged content appear newly updated, so other pages omit lastmod.
    return { loc, xml: `  <url><loc>${escapeXml(loc)}</loc>${lastmod ? `<lastmod>${lastmod}</lastmod>` : ''}</url>` };
  }).sort((a, b) => a.loc.localeCompare(b.loc));

  const xml = `<?xml version="1.0" encoding="UTF-8"?>\n`
    + `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`
    + items.map(item => item.xml).join('\n') + '\n</urlset>\n';
  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
