import assert from 'node:assert/strict';
import { readFile, readdir } from 'node:fs/promises';
import { join, relative, resolve, sep } from 'node:path';
import { parseFrontmatter } from '@astrojs/markdown-remark';

const decodeXml = value => value.replaceAll('&quot;', '"').replaceAll('&apos;', "'")
  .replaceAll('&lt;', '<').replaceAll('&gt;', '>').replaceAll('&amp;', '&');

export async function verifySitemap() {
  const root = resolve('dist');
  const base = (process.env.BASE_PATH || '/n3-hearingpedia').replace(/\/$/, '');
  const site = new URL(process.env.SITE_URL || 'https://betterci.github.io');
  const prefix = new URL(`${base}/`, site).href;
  const xml = await readFile(join(root, 'sitemap.xml'), 'utf8');
  assert(xml.startsWith('<?xml version="1.0" encoding="UTF-8"?>'), 'Missing XML declaration');
  assert(xml.includes('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'), 'Invalid sitemap namespace');
  assert(xml.trimEnd().endsWith('</urlset>'), 'Unclosed sitemap');
  const records = [...xml.matchAll(/<url><loc>([^<]+)<\/loc>(?:<lastmod>([^<]+)<\/lastmod>)?<\/url>/g)];
  assert(records.length > 0 && records.length <= 50000, 'Invalid sitemap URL count');
  assert.equal(records.length, (xml.match(/<url>/g) || []).length, 'Malformed sitemap record');
  const entries = new Map(records.map(([, loc, lastmod]) => [decodeXml(loc), lastmod]));
  assert.equal(entries.size, records.length, 'Duplicate sitemap URLs');

  async function walk(folder) {
    const children = await readdir(folder, { withFileTypes: true });
    return (await Promise.all(children.map(child => child.isDirectory()
      ? walk(join(folder, child.name)) : join(folder, child.name)))).flat();
  }

  // Compare with the actual rendered canonical pages, not the sitemap generator's
  // route list: this catches missing pages, redirects and accidental noindex URLs.
  const expected = new Set();
  for (const file of (await walk(root)).filter(file => file.endsWith('.html'))) {
    const page = await readFile(file, 'utf8');
    const canonical = page.match(/<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"[^>]*>/)?.[1];
    if (!canonical) continue; // Standalone downloads and demos are not site pages.
    const path = relative(root, file).split(sep).join('/');
    if (path === '404.html' || path.startsWith('404/') || path.startsWith('search/') || path.startsWith('share/')) continue;
    if (/<meta\b[^>]*http-equiv=["']refresh["']/i.test(page)) continue;
    if (/<meta\b[^>]*name=["'](?:robots|googlebot)["'][^>]*content=["'][^"']*\b(?:noindex|none)\b/i.test(page)) continue;
    const loc = decodeXml(canonical);
    const physicalUrl = new URL(`${base}/${path.replace(/index\.html$/, '')}`, site).href;
    assert.equal(loc, physicalUrl, `Canonical must match the built page: ${path}`);
    assert(!expected.has(loc), `Duplicate canonical page: ${loc}`);
    expected.add(loc);
    assert(page.includes(`rel="sitemap" type="application/xml" href="${base}/sitemap.xml"`), `Missing sitemap discovery link: ${path}`);
  }
  assert.deepEqual(new Set(entries.keys()), expected, 'Sitemap must contain exactly the canonical content pages');

  const dates = new Map();
  for (const file of (await readdir('src/content/concepts')).filter(file => file.endsWith('.md'))) {
    const { frontmatter } = parseFrontmatter(await readFile(join('src/content/concepts', file), 'utf8'));
    const loc = new URL(`${base}/concepts/${frontmatter.slug}/`, site).href;
    assert(entries.has(loc), `Concept missing from sitemap: ${frontmatter.slug}`);
    dates.set(loc, frontmatter.last_updated);
  }
  for (const [loc, lastmod] of entries) {
    const parsed = new URL(loc);
    assert(loc.startsWith(prefix) && !parsed.search && !parsed.hash && loc.endsWith('/'), `Invalid sitemap URL: ${loc}`);
    assert.equal(lastmod, dates.get(loc), `Sitemap date differs from editorial last_updated: ${loc}`);
  }
  return { sitemapUrls: entries.size, sitemapConcepts: dates.size };
}
