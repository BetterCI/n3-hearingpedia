# 网站访问统计：百度统计与 GoatCounter

两套服务同时采集发布在 `betterci.github.io/n3-hearingpedia/` 的访问。开发和预览不发送计数请求。页脚用一个“世界各地的读者”统计区域，桌面并列、手机上下排列百度统计和 GoatCounter 的访问总量、国家 / 地区及前五个来源。各自标注来源和时间范围，两套数字不相加。

## 百度统计的一次性配置

访问采集标识为 `0213110796858a57e43a0bd3fc744126`；报告接口的数字站点 ID 为 `23586320`，域名为 `betterci.github.io`。两种标识各有用途，保存在 `src/data/analytics.json`。每次读取报告前会核对站点 ID、域名和启用状态。报告覆盖该百度统计站点；若以后用同一采集标识统计其他 GitHub Pages 项目，这些流量也会进入该报告。

按[百度账号授权说明](https://tongji.baidu.com/api/manual/Chapter2/openapi.html)完成授权后，在[仓库 Actions Secrets](https://github.com/BetterCI/n3-hearingpedia/settings/secrets/actions)添加：

| Secret 名称 | 对应值 |
| --- | --- |
| `BAIDU_ACCESS_TOKEN` | 第 4 步返回的 `access_token` |
| `BAIDU_REFRESH_TOKEN` | 同次返回的 `refresh_token` |
| `BAIDU_API_KEY` | 数据导出服务的 API Key |
| `BAIDU_SECRET_KEY` | 数据导出服务的 Secret Key |

不要把凭证写入代码、聊天、网页或构建产物。站点 ID 无需添加为 Secret。

访问令牌过期时，脚本用刷新令牌取得新令牌。新的访问和刷新令牌以 AES-256-GCM 加密，密钥由应用 Secret Key 派生，保存到 `.cache/baidu-oauth.enc`。GitHub Actions 在每次运行前恢复加密缓存，在读取步骤后保存缓存，即使报告读取失败也会保存已续期的令牌。网页只获取公开的聚合统计 JSON。

缓存不是永久凭证存储。若缓存被删除、被 GitHub 淘汰，且最初配置的刷新令牌已失效，需要重新授权、更新两个 Token Secrets。更换应用 Secret Key 时应删除旧的 `baidu-oauth-v1-` 缓存；单独重新授权时，脚本会按初始刷新令牌的指纹自动忽略旧状态。

## 自动更新与失败处理

接入代码合入 `main` 且 Secrets 配好后，在 Actions → Verify and deploy Hearingpedia → Run workflow 运行一次。此后约每 6 小时更新，GitHub 调度可能延迟。运行日志分别显示两个数据源的访问次数和地域数量。

没有配置 API Token 的服务仍可采集访问，但不生成该服务的公开数据。成功获取的服务分别写入 `public/visitor-stats.json` 的 `sources.baidu` 和 `sources.goatcounter`，并显示在各自页脚区域。

单套服务失败会产生 Actions 警告，该服务的页脚统计在本次发布中隐藏，另一套服务仍可更新；不会用零替代失败数据。所有已配置服务都失败时，构建停止，已发布页面保留。PR 构建不读取凭证、获取报告或恢复 OAuth 缓存。

## 百度统计的口径

最近 30 个完整北京时间自然日，不含当天。使用 `trend/time/a` 报告总计中的 `visit_count`（访问次数），同时保留 `pv_count`（浏览量）。不把每日 UV 相加当作整个时段的独立访客数。国家 / 地区使用相同时间范围的 `visit/world/a`，校验返回条目完整后显示前五个。

两套服务的日期范围、会话规则和脚本拦截情况可能不同，因此数字通常不会一致。国家 / 地区依赖网络地址估计，VPN 等也会影响结果。

接口依据：[百度报告接口](https://tongji.baidu.com/api/manual/Chapter1/getData.html)、[国家报告](https://tongji.baidu.com/api/manual/Chapter1/visit_world_a.html)。

## 保留 GoatCounter

继续使用 GoatCounter 的免费托管服务。全站共用同一站点，页脚展示最近 30 天访问人次、来源国家 / 地区数量和前五个来源。保留已有 `GOATCOUNTER_API_TOKEN`，百度凭证不会替代或删除 GoatCounter 凭证。

## 一次性启用

1. 已配置你的站点 `https://n3hearing.goatcounter.com`。在 GoatCounter 中将网站地址填写为 `https://betterci.github.io/n3-hearingpedia/`。确认收集国家 / 地区信息，建议关闭地区细分。
2. 在 GoatCounter 的用户菜单 → API 创建只拥有统计读取权限的 Token。
3. 在 GitHub 仓库 Settings → Secrets and variables → Actions → Secrets 中添加 `GOATCOUNTER_API_TOKEN`。不要将 Token 写进公开代码、聊天或网页。无需配置站点变量；如以后换站点，可在 Variables 设置 `GOATCOUNTER_SITE` 覆盖当前默认值。
4. 在 Actions → Verify and deploy Hearingpedia → Run workflow 运行一次。此后每 6 小时左右自动更新（GitHub 的调度可能延迟）。首次部署后开始采集访问数据。

已配置但没有快照时先开始采集，页脚统计区在下一次成功更新后显示。失败处理遵循前述双数据源规则。

## 统计口径

访问人次取自 GoatCounter `stats/total` 的 `total - total_events`。该值按统计服务的会话与页面规则去重，跨页面可重复计数，不是全站独立人数，也不等同于独立 IP 数。国家来源使用相同时间窗口的 `stats/locations`，读取全部分页再显示前五个，地区数字不伪装成精确人数。时间窗口为最近 30×24 小时，按 UTC 整点查询，网页日期采用北京时间。

网页仅公开聚合统计；API Token 留在 GitHub Secret 内，既不出现在构建文件中也不发给网页访客。自注册前的历史流量无法补回。使用 VPN、拦截统计脚本等会影响国家估计及计数。

接口依据：https://www.goatcounter.com/help/api 、https://www.goatcounter.com/api.html 。
