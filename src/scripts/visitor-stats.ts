import analytics from '../data/analytics.json';

type VisitorStats = {
  provider?: 'baidu';
  start: string; end: string; updatedAt: string; visits: number;
  countries: { name: string; visits: number }[];
};
type VisitorSnapshot = VisitorStats & { sources?: { baidu?: VisitorStats; goatcounter?: VisitorStats } };

export function initVisitorStats() {
  // Only production project visits enter the analytics account.
  if (location.hostname === 'betterci.github.io'
      && location.pathname.startsWith('/n3-hearingpedia/')
      && /^[a-f0-9]{32}$/.test(analytics.baiduSiteId)
      && !document.querySelector('#hearingpedia-baidu-tracker')) {
    const trackingWindow = window as Window & { _hmt?: unknown[][] };
    trackingWindow._hmt = trackingWindow._hmt || [];
    const tracker = document.createElement('script');
    tracker.id = 'hearingpedia-baidu-tracker';
    tracker.async = true;
    tracker.src = `https://hm.baidu.com/hm.js?${analytics.baiduSiteId}`;
    document.head.append(tracker);
  }

  const section = document.querySelector<HTMLElement>('.visitor-stats');
  if (!section) return;
  const site = section.dataset.counterSite!;
  // Count only the published site; previews and local development remain excluded.
  if (site && location.hostname === 'betterci.github.io' && location.pathname.startsWith('/n3-hearingpedia/')
      && !document.querySelector('#hearingpedia-goatcounter-tracker')) {
    const script = document.createElement('script');
    script.async = true;
    script.id = 'hearingpedia-goatcounter-tracker';
    script.dataset.goatcounter = `${site}/count`;
    script.src = 'https://gc.zgo.at/count.js';
    document.head.append(script);
  }

  if (!section.dataset.statsUrl) return;
  void fetch(section.dataset.statsUrl, { signal: AbortSignal.timeout(8000) })
    .then(async response => {
      if (!response.ok) throw new Error('Statistics unavailable');
      return response.json() as Promise<VisitorSnapshot>;
    }).then(snapshot => {
      document.querySelectorAll<HTMLElement>('.visitor-stats').forEach(section => {
        const provider = section.dataset.statsSource as 'baidu' | 'goatcounter';
        const data = snapshot.sources ? snapshot.sources[provider]
          : (snapshot.provider || 'goatcounter') === provider ? snapshot : undefined;
        if (!data) return;
        const dateValid = (value: string) => typeof value === 'string' && Number.isFinite(Date.parse(value));
        if (!dateValid(data.start) || !dateValid(data.end) || !dateValid(data.updatedAt)
            || !Number.isSafeInteger(data.visits) || data.visits < 0 || !Array.isArray(data.countries)
            || data.countries.some(item => typeof item.name !== 'string' || !Number.isSafeInteger(item.visits) || item.visits < 0)) return;
        const format = new Intl.NumberFormat('zh-CN');
        const date = new Intl.DateTimeFormat('zh-CN', { timeZone: 'Asia/Shanghai', month: 'numeric', day: 'numeric' });
        const set = (selector: string, value: string) => { section.querySelector<HTMLElement>(selector)!.textContent = value; };
        set('[data-stats-period]', `${data.provider === 'baidu' ? '近 30 个完整自然日' : '近 30 天'} · ${date.format(new Date(data.start))}—${date.format(new Date(data.end))}`);
        set('[data-stats-visits-label]', data.provider === 'baidu' ? '访问次数' : '访问人次');
        set('[data-stats-source-note]', data.provider === 'baidu'
          ? '数据来源：百度统计。访问次数不等于独立访客人数；国家 / 地区为网络地址估计。'
          : '按 GoatCounter 口径统计访问人次，跨页面可重复计数；国家 / 地区为网络地址估计。');
        set('[data-stats-visits]', format.format(data.visits));
        set('[data-stats-countries]', format.format(data.countries.length));
        const list = section.querySelector<HTMLUListElement>('ul')!;
        list.replaceChildren();
        data.countries.slice(0, 5).forEach(country => {
          const item = document.createElement('li');
          item.textContent = `${country.name} ${format.format(country.visits)}`;
          list.append(item);
        });
        set('[data-stats-updated]', ` 更新于 ${date.format(new Date(data.updatedAt))}。`);
        section.hidden = false;
      });
    }).catch(() => { /* Keep the footer compact until a real snapshot is available. */ });
}
