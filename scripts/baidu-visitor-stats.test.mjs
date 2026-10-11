import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, readFile, rm } from 'node:fs/promises';
import { join } from 'node:path';
import { tmpdir } from 'node:os';
import { collectBaiduVisitorStats, createBaiduSession, encryptState, decryptState } from './baidu-visitor-stats.mjs';
import { collectSummaries } from './fetch-visitor-stats.mjs';

const now = new Date('2026-10-10T17:30:00Z'); // October 11 in Beijing.
const options = { siteId: 23586320, domain: 'betterci.github.io', now };
const fixture = (path, parameters) => path.endsWith('getSiteList')
  ? { list: [{ site_id: 23586320, domain: options.domain, status: 0 }] }
  : parameters.method === 'trend/time/a'
    ? { result: { fields: ['simple_date_title', 'pv_count', 'visit_count'], sum: [[18, '12']], items: [] } }
    : { result: { fields: ['visit_world_title', 'visit_count'], total: 2,
      items: [[[ { name: '中国' } ], [ { name: '美国' } ]], [[9], ['3']]] } };

test('uses complete Beijing days, report totals and country report without exposing tokens', async () => {
  const calls = [];
  const data = await collectBaiduVisitorStats({ ...options, request: async (path, parameters) => {
    calls.push({ path, parameters }); return fixture(path, parameters);
  } });
  assert.equal(data.visits, 12);
  assert.equal(data.pageviews, 18);
  assert.equal(data.start, '2026-09-10T16:00:00.000Z');
  assert.equal(data.end, '2026-10-09T16:00:00.000Z');
  for (const { parameters } of calls.slice(1)) {
    assert.equal(parameters.start_date, '20260911');
    assert.equal(parameters.end_date, '20261010');
    assert.equal(parameters.max_results, '0');
    assert.equal(parameters.site_id, '23586320');
  }
  assert.deepEqual(data.countries, [{ name: '中国', visits: 9 }, { name: '美国', visits: 3 }]);
  assert.equal(data.provider, 'baidu');
});

test('rejects mismatched sites, incomplete country reports and placeholder totals', async () => {
  await assert.rejects(collectBaiduVisitorStats({ ...options, domain: 'other.test', request: fixture }), /does not match/);
  await assert.rejects(collectBaiduVisitorStats({ ...options, request: (path, parameters) => {
    const data = fixture(path, parameters);
    if (parameters?.method === 'visit/world/a') data.result.total = 3;
    return data;
  } }), /Incomplete/);
  await assert.rejects(collectBaiduVisitorStats({ ...options, request: (path, parameters) => {
    const data = fixture(path, parameters);
    if (parameters?.method === 'trend/time/a') data.result.sum[0][1] = '--';
    return data;
  } }), /Invalid Baidu statistics count/);
});

test('OAuth state requires the app secret and detects tampering', () => {
  const state = { accessToken: 'private-access', refreshToken: 'private-refresh' };
  const encoded = encryptState(state, 'private-app-secret');
  assert(!encoded.includes(Buffer.from(state.accessToken)));
  assert.deepEqual(decryptState(encoded, 'private-app-secret'), state);
  assert.throws(() => decryptState(encoded, 'incorrect-secret'));
  encoded[encoded.length - 1] ^= 1;
  assert.throws(() => decryptState(encoded, 'private-app-secret'));
});

test('refreshes an expired token, persists the rotated refresh token, and reuses it next run', async t => {
  const directory = await mkdtemp(join(tmpdir(), 'hearingpedia-baidu-'));
  t.after(() => rm(directory, { recursive: true, force: true }));
  const statePath = join(directory, 'oauth.enc');
  const credentials = { accessToken: 'initial-access', refreshToken: 'initial-refresh', apiKey: 'app-key', secretKey: 'app-secret', now, statePath };
  const calls = [];
  const request = await createBaiduSession({ ...credentials, fetcher: async (url, init) => {
    assert.equal(url.origin, 'https://openapi.baidu.com');
    assert.equal(init.redirect, 'error');
    calls.push({ path: url.pathname, body: init.body });
    const data = url.pathname.endsWith('/token')
      ? { access_token: 'fresh-access', refresh_token: 'rotated-refresh', expires_in: 2592000 }
      : init.body.get('access_token') === 'initial-access' ? { error_code: 111 } : { list: [] };
    return { ok: true, json: async () => data };
  } });
  await request('/rest/2.0/tongji/config/getSiteList');
  assert.equal(calls.length, 3);
  assert.equal(calls[1].body.get('refresh_token'), 'initial-refresh');
  const cached = decryptState(await readFile(statePath), credentials.secretKey);
  assert.equal(cached.refreshToken, 'rotated-refresh');
  const requestAgain = await createBaiduSession({ ...credentials, fetcher: async (_url, init) => {
    assert.equal(init.body.get('access_token'), 'fresh-access');
    return { ok: true, json: async () => ({ list: [] }) };
  } });
  await requestAgain('/rest/2.0/tongji/config/getSiteList');
  const requestLater = await createBaiduSession({ ...credentials, now: new Date(now.getTime() + 31 * 86400000), fetcher: async (url, init) => {
    assert(url.pathname.endsWith('/token'));
    assert.equal(init.body.get('refresh_token'), 'rotated-refresh');
    return { ok: true, json: async () => ({ access_token: 'later-access', refresh_token: 'later-refresh', expires_in: 2592000 }) };
  } });
  assert.equal(typeof requestLater, 'function');
});

test('Baidu failures never print error text containing credentials', async () => {
  const request = await createBaiduSession({ accessToken: 'private-access', fetcher: async () => ({
    ok: true, json: async () => ({ error_code: 6, error_msg: 'private-access denied' }),
  }) });
  await assert.rejects(request('/rest/2.0/tongji/config/getSiteList'), error => {
    assert.match(error.message, /code 6/);
    assert(!error.message.includes('private-access'));
    return true;
  });
});

test('keeps both providers separate and lets either provider survive the other failing', async () => {
  const baidu = { provider: 'baidu', visits: 10 };
  const goat = { visits: 17 };
  const both = await collectSummaries([['baidu', async () => baidu], ['goatcounter', async () => goat]]);
  assert.equal(both.sources.baidu.visits, 10);
  assert.equal(both.sources.goatcounter.visits, 17);
  for (const [failed, live] of [['baidu', 'goatcounter'], ['goatcounter', 'baidu']]) {
    const data = await collectSummaries([[failed, async () => { throw new Error('offline'); }], [live, async () => ({ visits: 7 })]], () => {});
    assert.equal(data.sources[live].visits, 7);
    assert.equal(data.sources[failed], undefined);
  }
  await assert.rejects(collectSummaries([['baidu', async () => { throw new Error('offline'); }]], () => {}), /All configured/);
});
