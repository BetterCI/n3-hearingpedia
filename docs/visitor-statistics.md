# 免费访问统计接入

使用 GoatCounter 的免费托管服务。全站共用同一站点，页脚展示最近 30 天访问人次、来源国家 / 地区数量和前五个来源。仅统计发布在 `betterci.github.io/n3-hearingpedia/` 的网页，开发和预览不发送计数请求。

## 一次性启用

1. 已配置你的站点 `https://n3hearing.goatcounter.com`。在 GoatCounter 中将网站地址填写为 `https://betterci.github.io/n3-hearingpedia/`。确认收集国家 / 地区信息，建议关闭地区细分。
2. 在 GoatCounter 的用户菜单 → API 创建只拥有统计读取权限的 Token。
3. 在 GitHub 仓库 Settings → Secrets and variables → Actions → Secrets 中添加 `GOATCOUNTER_API_TOKEN`。不要将 Token 写进公开代码、聊天或网页。无需配置站点变量；如以后换站点，可在 Variables 设置 `GOATCOUNTER_SITE` 覆盖当前默认值。
4. 在 Actions → Verify and deploy Hearingpedia → Run workflow 运行一次。此后每 6 小时左右自动更新（GitHub 的调度可能延迟）。首次部署后开始采集访问数据。

未配置站点时不加载统计脚本，也不显示虚构数据。已配置但没有快照时先开始采集，页脚统计区在下一次成功更新后显示。请求失败时构建停止，已发布页面保留；不会用零覆盖真实数据。

## 统计口径

访问人次取自 GoatCounter `stats/total` 的 `total - total_events`。该值按统计服务的会话与页面规则去重，跨页面可重复计数，不是全站独立人数，也不等同于独立 IP 数。国家来源使用相同时间窗口的 `stats/locations`，读取全部分页再显示前五个，地区数字不伪装成精确人数。时间窗口为最近 30×24 小时，按 UTC 整点查询，网页日期采用北京时间。

网页仅公开聚合统计；API Token 留在 GitHub Secret 内，既不出现在构建文件中也不发给网页访客。自注册前的历史流量无法补回。使用 VPN、拦截统计脚本等会影响国家估计及计数。

接口依据：https://www.goatcounter.com/help/api 、https://www.goatcounter.com/api.html 。
