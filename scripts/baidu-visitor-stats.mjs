import { createHash, randomBytes, createCipheriv, createDecipheriv } from 'node:crypto';
import { readFile, mkdir, writeFile, rename } from 'node:fs/promises';
import { dirname } from 'node:path';

const origin = 'https://openapi.baidu.com';
const day = 86400000;
const fingerprint = value => createHash('sha256').update(value).digest('hex');

// OAuth state is cached only after authenticated encryption with the app secret.
export function encryptState(state, secret) {
  const iv = randomBytes(12);
  const cipher = createCipheriv('aes-256-gcm', createHash('sha256').update(secret).digest(), iv);
  const encrypted = Buffer.concat([cipher.update(JSON.stringify(state), 'utf8'), cipher.final()]);
  return Buffer.concat([iv, cipher.getAuthTag(), encrypted]);
}

export function decryptState(bytes, secret) {
  const decipher = createDecipheriv('aes-256-gcm', createHash('sha256').update(secret).digest(), bytes.subarray(0, 12));
  decipher.setAuthTag(bytes.subarray(12, 28));
  return JSON.parse(Buffer.concat([decipher.update(bytes.subarray(28)), decipher.final()]).toString('utf8'));
}

class BaiduError extends Error {
  constructor(message, code) { super(message); this.code = code; }
}

async function call(path, parameters, fetcher) {
  let response;
  try {
    response = await fetcher(new URL(path, origin), {
      method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams(parameters), redirect: 'error', signal: AbortSignal.timeout(20000),
    });
  } catch { throw new BaiduError('Baidu request failed or timed out'); }
  if (!response.ok) throw new BaiduError(`Baidu returned HTTP ${response.status}`);
  let data;
  try { data = await response.json(); } catch { throw new BaiduError('Baidu returned invalid JSON'); }
  // Never include server error text, request bodies, or URLs containing credentials.
  if (data.error_code || data.error) {
    const code = Number(data.error_code);
    throw new BaiduError(`Baidu API rejected the request${Number.isFinite(code) ? ` (code ${code})` : ''}`, code);
  }
  return data;
}

export async function createBaiduSession({ accessToken, refreshToken = '', apiKey = '', secretKey = '', statePath,
  now = new Date(), fetcher = fetch }) {
  if (!accessToken) throw new Error('Missing BAIDU_ACCESS_TOKEN');
  let state = { accessToken, refreshToken, initialRefreshHash: fingerprint(refreshToken) };
  if (statePath && secretKey && refreshToken) {
    try {
      const cached = decryptState(await readFile(statePath), secretKey);
      if (cached.initialRefreshHash === state.initialRefreshHash && typeof cached.accessToken === 'string'
          && cached.accessToken && typeof cached.refreshToken === 'string' && cached.refreshToken
          && Number.isFinite(cached.expiresAt)) state = cached;
    } catch (error) {
      if (error.code !== 'ENOENT') throw new Error('Cannot read encrypted Baidu OAuth cache; clear cache or reconfigure credentials');
    }
  }
  async function refresh() {
    if (!apiKey || !secretKey || !state.refreshToken) {
      throw new Error('Baidu access token expired; configure BAIDU_API_KEY, BAIDU_SECRET_KEY and BAIDU_REFRESH_TOKEN');
    }
    const result = await call('/oauth/2.0/token', {
      grant_type: 'refresh_token', refresh_token: state.refreshToken, client_id: apiKey, client_secret: secretKey,
    }, fetcher);
    if (typeof result.access_token !== 'string' || !result.access_token
        || typeof result.refresh_token !== 'string' || !result.refresh_token
        || !Number.isFinite(result.expires_in) || result.expires_in <= 0) throw new Error('Invalid Baidu OAuth response');
    state = { ...state, accessToken: result.access_token, refreshToken: result.refresh_token,
      expiresAt: now.getTime() + result.expires_in * 1000 };
    if (statePath) {
      await mkdir(dirname(statePath), { recursive: true });
      await writeFile(`${statePath}.tmp`, encryptState(state, secretKey), { mode: 0o600 });
      await rename(`${statePath}.tmp`, statePath);
    }
  }
  if (state.expiresAt && state.expiresAt <= now.getTime() + 3600000) await refresh();
  return async (path, parameters = {}) => {
    try { return await call(path, { ...parameters, access_token: state.accessToken }, fetcher); }
    catch (error) {
      if (![110, 111].includes(error.code)) throw error;
      await refresh();
      return call(path, { ...parameters, access_token: state.accessToken }, fetcher);
    }
  };
}

function count(value) {
  const number = typeof value === 'string' && /^\d+$/.test(value) ? Number(value) : value;
  if (!Number.isSafeInteger(number) || number < 0) throw new Error('Invalid Baidu statistics count');
  return number;
}

function metricIndex(result, metric) {
  const index = result?.fields?.indexOf(metric);
  if (!Number.isInteger(index) || index < 1) throw new Error(`Missing Baidu metric: ${metric}`);
  return index - 1; // The dimension occupies fields[0], but is separate from metric rows.
}

export async function collectBaiduVisitorStats({ request, siteId, domain, now = new Date() }) {
  if (!Number.isSafeInteger(siteId) || siteId <= 0) throw new Error('Invalid Baidu report site ID');
  const sites = await request('/rest/2.0/tongji/config/getSiteList');
  const site = sites.list?.find(item => Number(item.site_id) === siteId);
  if (!site || site.domain !== domain || Number(site.status) !== 0) throw new Error('Baidu site ID/domain does not match an active owned site');
  // Thirty complete Beijing calendar days, excluding today's partial totals.
  const today = new Date(now.getTime() + 8 * 3600000).toISOString().slice(0, 10);
  const exclusiveEnd = new Date(`${today}T00:00:00+08:00`);
  const start = new Date(exclusiveEnd.getTime() - 30 * day);
  const end = new Date(exclusiveEnd.getTime() - day);
  const reportDate = date => new Date(date.getTime() + 8 * 3600000).toISOString().slice(0, 10).replaceAll('-', '');
  const common = { site_id: String(siteId), start_date: reportDate(start), end_date: reportDate(end), max_results: '0' };
  const trend = (await request('/rest/2.0/tongji/report/getData', {
    ...common, method: 'trend/time/a', metrics: 'pv_count,visit_count', gran: 'day',
  })).result;
  // Read the report's period sum; never add daily UV counts.
  const visits = count(trend?.sum?.[0]?.[metricIndex(trend, 'visit_count')]);
  const pageviews = count(trend?.sum?.[0]?.[metricIndex(trend, 'pv_count')]);
  const world = (await request('/rest/2.0/tongji/report/getData', {
    ...common, method: 'visit/world/a', metrics: 'visit_count', order: 'visit_count,desc',
  })).result;
  const index = metricIndex(world, 'visit_count');
  const dimensions = world?.items?.[0];
  const values = world?.items?.[1];
  if (!Array.isArray(dimensions) || !Array.isArray(values) || dimensions.length !== values.length
      || count(world.total) !== dimensions.length) throw new Error('Incomplete Baidu country report');
  const names = new Map();
  for (let i = 0; i < dimensions.length; i++) {
    const label = dimensions[i]?.[0];
    const name = typeof label === 'string' ? label : label?.name;
    if (typeof name !== 'string' || !name.trim()) throw new Error('Invalid Baidu country name');
    const visits = count(values[i]?.[index]);
    if (visits > 0) names.set(name, count((names.get(name) || 0) + visits));
  }
  const countries = [...names].map(([name, visits]) => ({ name, visits }))
    .sort((a, b) => b.visits - a.visits || a.name.localeCompare(b.name));
  return { provider: 'baidu', start: start.toISOString(), end: end.toISOString(), updatedAt: now.toISOString(), visits, pageviews, countries };
}
