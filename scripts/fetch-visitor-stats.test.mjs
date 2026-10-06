import test from 'node:test';
import assert from 'node:assert/strict';
import { collectVisitorStats } from './fetch-visitor-stats.mjs';

const options = { site: 'https://example.goatcounter.com/', token: 'test-only-secret', now: new Date('2026-10-06T03:25:00Z') };
test('collects all country pages and exports only aggregates', async () => {
  const requests = [];
  const summary = await collectVisitorStats({ ...options, fetcher: async (url, init) => {
    requests.push(url);
    assert.equal(init.headers.Authorization, `Bearer ${options.token}`);
    assert.equal(init.redirect, 'error');
    assert.equal(url.searchParams.get('start'), '2026-09-06T03:00:00.000Z');
    assert.equal(url.searchParams.get('end'), '2026-10-06T03:00:00.000Z');
    const data = url.pathname.endsWith('/total') ? { total: 12, total_events: 2 }
      : url.searchParams.get('offset') === '0' ? { stats: [{ id: 'CN', name: 'China', count: 8 }], more: true }
      : { stats: [{ id: 'US', name: 'United States', count: 2 }], more: false };
    return { ok: true, json: async () => data };
  } });
  assert.equal(requests.length, 3);
  assert.equal(summary.visits, 10);
  assert.deepEqual(summary.countries, [{ name: '中国', visits: 8 }, { name: '美国', visits: 2 }]);
  assert(!JSON.stringify(summary).includes(options.token));
});
test('rejects invalid counts and failed requests instead of publishing zero', async () => {
  await assert.rejects(collectVisitorStats({ ...options, fetcher: async () => ({ ok: false, status: 401 }) }), /HTTP 401/);
  await assert.rejects(collectVisitorStats({ ...options, fetcher: async () => ({ ok: true, json: async () => ({ total: -1, total_events: 0 }) }) }), /Invalid statistics count/);
});
test('rejects untrusted endpoints before transmitting token', async () => {
  let called = false;
  await assert.rejects(collectVisitorStats({ ...options, site: 'https://example.goatcounter.com.attacker.test', fetcher: async () => { called = true; } }), /Invalid GoatCounter site URL/);
  assert.equal(called, false);
});
test('reports API errors while redacting the configured secret', async () => {
  await assert.rejects(collectVisitorStats({ ...options, fetcher: async () => ({
    ok: false, status: 404, json: async () => ({ error: `Rejected ${options.token}` }),
  }) }), error => {
    assert.match(error.message, /HTTP 404: Rejected \[redacted\]/);
    assert(!error.message.includes(options.token));
    return true;
  });
});
