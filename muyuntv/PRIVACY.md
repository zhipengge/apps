# 牧云电视 (Muyun TV) — 隐私政策 / Privacy Policy

**最后更新 / Last updated: 2026-08-29**

---

## 中文

### 总览

**牧云电视不收集、不上传、不把你的频道列表发到任何自有服务器。** 频道名称、地址、分组、收藏和语言/主题偏好全部只在这台 iPhone 或 iPad 本地保存。本 App 没有账号系统，没有后端，不内嵌广告、分析或追踪 SDK。

本应用是播放工具，不提供、不托管任何第三方电视或视频内容。你导入或输入的直播源由你自己选择。

### 我们处理什么、在哪处理

| 数据 | 用途 | 处理/存储位置 |
|---|---|---|
| 频道名称、地址、分组、台标地址 | 列表、搜索、播放 | 本机 UserDefaults |
| 收藏的频道地址 | 收藏分组 | 同上 |
| 上次播放、最近观看地址 | 继续播放、最近分组 | 同上 |
| 监控墙钉选（最多 4 路） | 分屏同时看你钉的源 | 同上 |
| 播放时长统计 | 设置里查看今日/累计 | 同上 |
| 常亮、重连、静音、铺满、低延迟、时移回放 | 播放偏好 | 同上 |
| 时移临时分片 | 同一源看满约 1 分钟后，把刚才的画面暂存在本机，供拖回重看 | 系统临时目录；退出播放即删除。不上云。监控墙不缓存 |
| 语言、主题 | 界面 | 同上 |
| 你主动导出的 JSON 播放列表 | 备份或换机 | 经系统分享面板送到你选择的位置；App 不上传 |
| 你导入的播放列表文件或网址 | 解析出频道 | 文件只读一次；网址请求只发往你粘贴的那个地址 |
| 一键导入的公开列表 | 测试播放、播出方公开的国际频道，以及央视网公开音频 | 向 GitHub raw 上的 public_channels.m3u 发一次 GET，在本机解析 |

### 我们不做的事

- 不把频道列表上传到开发者服务器
- 不接入广告网络或分析平台
- 不读取通讯录、位置、麦克风、摄像头、相册
- 不录像、不识别人脸、不把监控墙画面传到任何服务器
- 不要求登录账号
- 不追踪你
- 不内置电视节目列表

### 网络通信

联网只发生在你主动操作时：

1. **导入播放列表网址**：向你粘贴的 http 或 https 地址发请求，下载文本并在本机解析。
2. **一键导入**：向 `raw.githubusercontent.com/zhipengge/apps/main/muyuntv/public_channels.m3u` 发一次 GET，下载公开列表并在本机解析。该文件含厂商测试流、播出方自己公开的国际频道视频 HLS，以及央视网 VDN 自己公开的音频 HLS。不是盗链 IPTV，本仓库不托管音视频。
3. **播放直播源**：向该频道的流媒体地址请求音视频数据。许多直播源使用明文 HTTP，因此 App 允许非 HTTPS 连接。请求发往源站，不经过开发者服务器。开启时移后，可能向同一地址再拉媒体分片做本机回放缓存。
4. **加载台标**：若播放列表里带有台标网址，列表会向该地址请求图片。

打开关于页里的隐私政策或支持页链接时，由系统浏览器访问 GitHub Pages，不经过 App 自己的接口。

### 数据删除

- 在列表左滑可删除单个频道；设置里可清空全部频道。清空后不会自动填回。
- 退出全屏播放时，时移临时分片会从本机删除。
- 从主屏幕删除 App，本机容器内的频道数据一并消失。换机前请先导出播放列表。

### 联系方式

如对本政策有疑问，请通过支持页反馈。

---

## English

### Summary

**Muyun TV does not collect, upload, or send your channel list to any server we operate.** Channel names, URLs, groups, favorites, and language/theme preferences stay on this iPhone or iPad. There is no account, no backend, and no ads, analytics, or tracking SDK.

This app is a playback tool. It does not provide or host third-party TV or video. Streams you import or type are chosen by you.

### What we process and where

| Data | Purpose | Where |
|---|---|---|
| Channel name, URL, group, logo URL | List, search, playback | On-device UserDefaults |
| Favorite channel URLs | Favorites group | Same |
| Last played and recent URLs | Resume and Recents | Same |
| Monitor wall pins (up to 4) | Multi-view of feeds you pin | Same |
| Playback duration stats | Today / total in Settings | Same |
| Keep-awake, reconnect, mute, fill, low latency, timeshift | Playback preferences | Same |
| Timeshift media segments | After about a minute on the same source, rewind what you just watched | On-device temp files; deleted when you leave the player. Not uploaded. The monitor wall does not cache |
| Language and theme | UI | Same |
| JSON playlist you export | Backup or move devices | System share sheet; the app does not upload it |
| Playlist file or URL you import | Parse channels | File is read once; the HTTP request goes only to the URL you pasted |
| Public playlist from Quick Import | Verify playback, official international channels, and official CCTV audio | One GET to public_channels.m3u on GitHub raw, parsed on device |

### What we do not do

- No upload of your channel list to developer servers
- No ads or analytics
- No contacts, location, microphone, camera, or photos access
- No recording, face detection, or upload of monitor-wall video
- No account
- No tracking
- No built-in TV program list

### Network

Network use happens only when you act:

1. **Import playlist URL**: request the http or https address you paste, then parse on device.
2. **Quick import**: one GET to `raw.githubusercontent.com/zhipengge/apps/main/muyuntv/public_channels.m3u` for a public list, parsed on device. It includes vendor test streams, official international video HLS, and official CCTV audio HLS from CNTV VDN. Not pirate IPTV; this repo does not host audio or video.
3. **Play a stream**: request audio/video from that channel URL. Many live sources use plain HTTP, so the app allows non-HTTPS connections. Traffic goes to the source, not through our servers. With timeshift on, the app may also fetch media segments from that same URL for a local replay cache.
4. **Logos**: if a playlist includes a logo URL, the list may fetch that image.

Privacy and support links in About open in the system browser to GitHub Pages.

### Deletion

- Swipe to delete one channel; Settings can clear all. A cleared list is not filled back in.
- Timeshift temp files are deleted when you leave the player.
- Deleting the app removes the sandbox data. Export a playlist before switching phones.

### Contact

Use the support page if you have questions about this policy.
