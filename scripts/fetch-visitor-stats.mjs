import { mkdir, writeFile, rename } from 'node:fs/promises';
import { resolve, dirname } from 'node:path';
import { pathToFileURL } from 'node:url';
import analytics from '../src/data/analytics.json' with { type: 'json' };

function count(value) {
  if (!Number.isSafeInteger(value) || value < 0) throw new Error('Invalid statistics count');
  return value;
}

export async function collectVisitorStats({ site, token, now = new Date(), fetcher = fetch }) {
  site = site.trim().replace(/\/$/, '');
  if (!/^https:\/\/[a-z0-9-]+\.goatcounter\.com$/.test(site)) throw new Error('Invalid GoatCounter site URL');
  if (!token) throw new Error('Missing GoatCounter API token');
  const end = new Date(now);
  end.setUTCMinutes(0, 0, 0);
  const start = new Date(end.getTime() - 30 * 86400000);
  async function request(path, extra = {}) {
    const url = new URL(`/api/v0/stats/${path}`, site);
    url.search = new URLSearchParams({ start: start.toISOString(), end: end.toISOString(), ...extra });
    const response = await fetcher(url, {
      headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
      signal: AbortSignal.timeout(20000), redirect: 'error',
    });
    if (!response.ok) {
      let reason = '';
      try {
        const body = await response.json();
        if (typeof body.error === 'string') reason = body.error.replaceAll(token, '[redacted]').slice(0, 240);
      } catch { /* Non-JSON failures are identified by their HTTP status. */ }
      throw new Error(`GoatCounter ${path} returned HTTP ${response.status}${reason ? `: ${reason}` : ''}`);
    }
    return response.json();
  }
  const total = await request('total');
  const visits = count(total.total) - count(total.total_events);
  if (visits < 0) throw new Error('Invalid event count');
  const countries = [];
  const names = new Intl.DisplayNames(['zh-CN'], { type: 'region' });
  for (let offset = 0; ; offset += 100) {
    if (offset > 1000) throw new Error('Unexpected number of locations');
    const page = await request('locations', { limit: '100', offset: String(offset) });
    if (!Array.isArray(page.stats) || typeof page.more !== 'boolean') throw new Error('Invalid locations response');
    for (const row of page.stats) {
      const visits = count(row.count);
      if (!visits) continue;
      const code = String(row.id || '').toUpperCase();
      const name = /^[A-Z]{2}$/.test(code) && !['XX', 'ZZ'].includes(code) ? names.of(code) : String(row.name || '未知地区');
      countries.push({ name, visits });
    }
    if (!page.more) break;
    if (!page.stats.length) throw new Error('Empty locations page has more results');
    await new Promise(resolve => setTimeout(resolve, 300));
  }
  countries.sort((a, b) => b.visits - a.visits || a.name.localeCompare(b.name));
  return { start: start.toISOString(), end: end.toISOString(), updatedAt: now.toISOString(), visits, countries };
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const site = process.env.PUBLIC_GOATCOUNTER_SITE || analytics.site;
  const token = process.env.GOATCOUNTER_API_TOKEN || '';
  if (!site || !token) {
    console.log('Visitor statistics inactive: configure site URL and API token to activate.');
  } else {
    const data = await collectVisitorStats({ site, token });
    const output = resolve('public/visitor-stats.json');
    await mkdir(dirname(output), { recursive: true });
    await writeFile(`${output}.tmp`, JSON.stringify(data) + '\n');
    await rename(`${output}.tmp`, output);
    console.log(`Updated visitor summary: ${data.visits} visits, ${data.countries.length} locations.`);
  }
}
