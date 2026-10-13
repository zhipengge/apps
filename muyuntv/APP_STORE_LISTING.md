# 牧云电视 (Muyun TV) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。
> **这份素材刻意没有「比免费播放器更强」「打开就有台」这类主张，理由见第 8 节。改文案之前先读那一节。**

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **牧云电视** | 电视直播、IPTV、万能播放器（通称易被占） |
| 名称（English 本地化） | **Muyun TV** | Live TV Player |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.MuyunTV` | 任何旧 ID |
| SKU | `muyuntv-20260828` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「牧云电视」，主类别已在工程里写成 `public.app-category.entertainment`。

备选店名（创建时报名被占再用）：

- 牧云直播播放器
- 牧云流播放
- MuyunLivePlayer

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

**店名、副标题、关键词里都不要出现「聚合」二字。** 仓库根目录 `竞争力审计.md:37` 把这一项写成
「电视直播聚合」，那是内部盘点用的品类速记，**不是可以搬进商店的定位**：`MuyunTV/AGENTS.md` 的硬约束写着
「**这是播放工具，不是内容源**」，一旦商店文案自称聚合平台，定位就从工具滑到了内容提供方。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
导入你自己的播放列表或直播地址即可播放。同一频道的多条线路合成一条，播不动自动换线；直播能往回拖 30 分钟。最多四路监控墙分屏。不内置任何频道。
```

**字符数：73 / 170**

### English

```
Import your list or URL. Lines for one channel merge into one entry and auto-switch on failure; live TV rewinds 30 minutes. Four feeds at once. No built-in channels.
```

**字符数：165 / 170**（离上限只剩 5，改写时留意）

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
牧云电视是一个直播流播放工具。把你自己的播放列表或直播地址加进来，就能在 iPhone 和 iPad 上播放。本应用不提供、不托管、也不内置任何电视节目，源由你选择。

【导入】
- 支持 M3U / M3U8，读取分组（#EXTGRP 与 group-title 都认）和台标
- 支持 JSON 的三种外壳，urls 多线路会自动展开
- 支持 TXT / CSV，逗号、制表符、竖线三种分隔都认
- UTF-8 BOM、UTF-16 与 CRLF 换行都能读
- 后缀说谎时按内容嗅探：从浏览器另存下来的文件常常是 .txt 甚至 .mp4
- 可从网址导入、从文件导入、手动添加单条，也可以导出 JSON 备份
- 默认合并导入并按地址去重，不覆盖你手工改过的名称；也可以选择覆盖全部

【同一频道合成一条】
- 同一个频道有好几个地址是常态，它们会折成一条内容，多地址作为可切换线路
- 所以你看到的列表长度是你想看的频道数，而不是你手上地址的条数
- 线路可以测速排序，播放失败时自动切到下一路，打开时默认用最快的那一路

【直播也能往回拖】
- 同一个源连续播放满 60 秒后，可以往回拖最多 30 分钟，点「直播」追上最新
- 切台时按源暂留，最多 3 路，切回去接着看
- 上限是硬的：30 分钟 / 400MB / 3 路，不是可以随手调大的展示参数

【播放】
- 播放 HLS 和常见 HTTP 视频流，支持画中画、AirPlay 与后台音频
- 全屏观看，可切换上一个 / 下一个频道
- 失败可重试，可选自动重连
- 可让屏幕保持常亮，也可设定时关闭

【监控墙】
- 把摄像头或其他源钉到监控墙，最多同时看 4 路
- 默认静音，长按某一格可以单独开声
- 绿 / 橙 / 红分别表示在线、重连中、离线，直播断掉时本机震动
- 不录像，不识别画面里的人，不把画面传到任何服务器
- 监控墙不缓存，也不支持画中画

【整理与外观】
- 按播放列表里的分组浏览，支持收藏、最近观看、搜索、编辑、删除
- 清空全部频道后不会自动填回示例
- 中文与 English，深色 / 浅色 / 跟随系统

【联网都用在哪儿】
- 只有五处：导入你给的地址、拉那份公开测试表、给你列表里的线路测速、播放你点的频道、加载列表里的台标
- 测速是自动的：列表一出现就发，最多同时 5 条，每条 6 秒超时，最多下 64 KB 就断开
- 很多公开源只提供 http，所以传输层放开了任意加载；对明文 http 的源，你和源站之间的流量是不加密的
- 没有账号，没有登录，没有属于开发者的服务器，没有广告，没有内购，没有任何分析或崩溃上报 SDK

【请注意】
本应用是播放工具，不是直播平台，也不内置频道。请只导入你有权使用的源。关于页提供免责声明和举报入口。

【系统要求】
需要 iOS 17.0 或更高版本。iPhone 与 iPad 都可以。
```

**字符数：1230 / 4000**

### English

```
Muyun TV is a live-stream player. Add your own playlist or stream URL and play it on iPhone and iPad. This app does not provide, host or bundle any TV channel; you choose the sources.

[Import]
- M3U / M3U8, reading groups (#EXTGRP and group-title both work) and logos
- JSON in its three common shells, with urls arrays expanded into multiple lines
- TXT / CSV with commas, tabs or pipes as separators
- UTF-8 BOM, UTF-16 and CRLF line endings all read correctly
- Content sniffing when the extension lies: files saved from a browser are often .txt or even .mp4
- Import from a URL, import from a file, add one source by hand, or export JSON as a backup
- Merge and de-duplicate by address by default, without overwriting names you edited; replace-all is optional

[One entry per channel]
- A channel having several addresses is normal; they fold into a single entry, with the addresses as switchable lines
- So the length of your list is the number of channels you want, not the number of addresses you have
- Lines can be sorted by measured speed, playback switches to the next line automatically when one fails, and the fastest is used by default

[Live TV you can rewind]
- After 60 seconds of continuous playback on one source you can drag back up to 30 minutes, and tap Live to catch up
- Switching channels keeps the cache per source, up to 3 lines, so switching back resumes where you were
- The caps are hard: 30 minutes, 400 MB, 3 lines, not a display setting to be raised on a whim

[Playback]
- Plays HLS and common HTTP video streams, with Picture in Picture, AirPlay and background audio
- Full screen, with previous and next channel
- Retry when a source fails, with optional auto reconnect
- Keep the screen awake, or set a sleep timer

[Monitor wall]
- Pin cameras or other feeds on a wall, up to four at once
- Muted by default; long-press one tile to unmute only that one
- Green, orange and red show live, reconnecting and offline, and the device vibrates when a live feed drops
- No recording, no detection of people in the video, no upload of the picture to any server
- The wall does not cache, and Picture in Picture is not available inside tiles

[Organising and appearance]
- Browse by playlist groups, with favourites, recents, search, edit and delete
- Clearing the whole list does not put samples back
- Chinese and English; dark, light or follow the system

[Where the network is used]
- Five places only: importing an address you supply, fetching the public test playlist, probing the lines in your list, playing the channel you tap, and loading logos in the list
- The probing is automatic: it starts as soon as the list appears, at most 5 at a time, a 6-second timeout each, disconnected after at most 64 KB
- Many public sources are http only, so the transport layer permits arbitrary loads; with a plain-http source, traffic between you and that source is not encrypted
- No account, no sign-in, no server of ours, no ads, no in-app purchases, and no analytics or crash-reporting SDK

[Please note]
This is a player, not a streaming service, and it bundles no channels. Import only sources you are allowed to use. The About card carries a disclaimer and a report path.

[Requirements]
iOS 17.0 or later. iPhone and iPad both supported.
```

**字符数：3271 / 4000**

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
导入直播源，分屏盯画面
```

**字符数：11 / 30**

### English

```
Play streams and camera walls
```

**字符数：29 / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
直播,播放器,播放列表,视频流,频道,收藏,导入,分组,hls,监控墙,摄像头,分屏
```

**字符数：42 / 100**

### English

```
live,player,playlist,stream,channel,hls,import,favorite,group,camera,monitor
```

**字符数：76 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/muyuntv/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/muyuntv/privacy.html` |
| 营销 URL | `https://zhipengge.github.io/apps/muyuntv/` |

技术支持是**版本级**字段（改它要跟新版本一起提审），隐私政策是 **App 级**（要有待发版本才能改）。
这两个 URL 一旦提审就不好改了，提审前先确认目录名。

营销 URL 这一条和其它几个 app 不同，**这里可以填**：`apps/muyuntv/` 下有 `index.html`
（本轮已确认存在，1287 字节，链到 privacy.html、support.html 与 public_channels.m3u），
不会像没有落地页的目录那样 404。

`apps/` 是独立仓库 `zhipengge/apps`，Pages 已经开着。

---

## 6. 类别、评级、隐私问卷

| 字段 | 建议 |
|---|---|
| 主要类别 | 娱乐 / Entertainment |
| 次要类别 | 照片与视频 / Photo & Video |
| 内购 | **无**。工程里 grep 不到一个 `StoreKit` 符号，也没有商品 ID |
| 年龄分级 | 按问卷如实填。App 内**没有任何网页浏览器或网页视图**（零 `WKWebView` / `SFSafariViewController`），所以问卷里问「不受限的网页访问」应填否；用户粘贴的只是流地址 |
| App 隐私 | **不收集数据**。须与本目录的 `privacy.html` 一致 |
| 出口合规 | **NO**（`INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO` 写在工程里，App 里没有任何加密代码） |

审核备注建议写清：本 App 不内置、不托管、不审核任何频道，用户必须自行导入播放列表或地址后才能播放；
一键导入的那份公开表只含播出方自己发布的流（央视网公开音频无画面、国际频道官方直播、厂商测试流）；
App 不申请任何权限，没有摄像头权限，监控墙只是把几个地址分屏播放，不录像、不上云。
关于页有免责声明和举报入口。

年龄分级这一点值得单独提醒：**App 本身没有任何不受控的内容来源**（无浏览器、无内置内容、无用户社区），
但**用户自己导入的流内容不在 App 的控制范围内**。按问卷如实作答即可，不要因为「用户可以粘任何地址」
就随手勾 17+；反过来也不要为了让分级好看而少答。

---

## 7. 截图

`TARGETED_DEVICE_FAMILY = "1,2"`，iPhone 与 iPad 两套都要，各 3-10 张。

### iPhone 6.9 寸 / 1320 x 2868

`apps/muyuntv/screenshots/iphone/` 下 4 个文件，本轮已核过尺寸，全部 **1320 x 2868**：

| 文件 | 内容 |
|---|---|
| `01-empty.png` | 导入你自己的直播源 |
| `02-channels.png` | 频道列表一目了然 |
| `03-browse.png` | 按分组浏览 |
| `04-settings.png` | 播放行为随你调 |

### iPad 13 寸 / 2064 x 2752

`apps/muyuntv/screenshots/ipad/` 下 3 个文件，本轮已核过尺寸，全部 **2064 x 2752**：

| 文件 | 内容 |
|---|---|
| `01-empty.png` | 导入你自己的直播源 |
| `02-channels.png` | 频道列表一目了然 |
| `03-browse.png` | 按分组浏览 |

**两套都齐了。** 这是本轮核查里唯一一个截图不缺的 app。

所有图都用真实界面截图加设备外框与标题，符合 Apple 对截图的真实性要求。

### 建议补拍的两张

现有 7 张覆盖了空状态、列表、分组、设置，**没有一张拍到这一作真正独有的东西**。建议加：

- `05-lines.png` 同一频道的多条线路切换：列表里只有一条，展开后是三条可选线路
- `06-timeshift.png` 时移：进度条拖回 20 分钟的位置，右下角是「直播」按钮

监控墙（4 路分屏）也值得一张，但那需要 4 个可用的源，是否拍由你定。

重新生成：

```bash
cd ../
python3 tools/compose_all.py muyuntv
```

---

## 8. 这份素材里，哪些卖点是被故意排除的

**这一节比前几节重要。改文案之前请先读完。**

### 先说结论：作者自己写了「这不是一个别人做不了的东西」

`MuyunTV/AGENTS.md` 的「差异化：这个 app 凭什么存在」一节，开头第一段逐字：

> 先说结论，免得被下面的清单误导：**这不是一个别人做不了的东西。** 免费播放器（VLC 之类）
> 播 HLS 的能力不比它差。它成立的前提是**用户已经有一份自己的源**——
> 如果是「打开就想有台看」，这个 app 不是他的选择，也不该假装是。

这一句是**这份素材的地基**。所以全篇没有出现过：

- 「比免费播放器更强」「比 VLC 好用」之类的比较级
- 「打开就有台看」「不用折腾就能看电视」
- 任何暗示 App 自带内容的说法；空列表是设计，素材里写的是设计，而不是「先给你几个台」

同一条约束在 `AGENTS.md` 的硬约束里还有一份：「**这是播放工具，不是内容源。**」
以及「一键导入的那份表**不得**塞未授权的国内电视台视频转播，也不得塞第三方 IPTV 聚合」
（`AppIdentifiers.publicPlaylistURL` 指向本仓库的 `public_channels.m3u`，逻辑测试里有 16 条断言守着）。

### 用掉的（每条都能在代码里指出位置）

| 卖点 | 代码依据 | 用在哪 |
|---|---|---|
| 同名源聚合为一条内容、多地址作线路 | `LineAggregator.normalizeName` | 推广文本、描述、FAQ |
| 测速排序、失败自动换线、默认用最快 | `LineSpeedManager`、`PlayerView` 的 `state == .failed && autoSwitchLine && hasMultipleLines` | 推广文本、描述、FAQ |
| 时移：满 60 秒武装、最多 30 分钟 / 400MB、切台暂留 3 路 | `TimeshiftLogic.swift`、`AppIdentifiers.monitorLimit` 同层的硬上限 | 推广文本、描述、FAQ |
| 导入层的宽容度（BOM / UTF-16 / CRLF / 三种 JSON 外壳 / 三种分隔 / 后缀说谎嗅探 / 非绝对地址整条丢弃） | `PlaylistParser.swift`、`PlaylistImporter.swift` | 描述、FAQ |
| 监控墙 4 路上限、默认静音、三色状态、断线震动、不缓存、子格无画中画 | `MonitorWallView.swift`、`AppIdentifiers.monitorLimit = 4` | 描述、FAQ |
| 画中画 / AirPlay / 后台音频 / 屏幕常亮 / 定时关闭 | `AVKit`、`UIBackgroundModes: audio`、`SleepTimerManager.swift` | 描述、FAQ |
| 四个导入入口 + JSON 导出 | `ImportSourcesView.swift`、`AppIdentifiers.channelsStorageKey` 周边 | 描述、FAQ |
| 中英双语界面、三种主题 | `LanguageManager.swift`、`ThemeManager.swift` | 描述、FAQ |
| 无账号 / 无内购 / 无广告 / 无第三方 SDK / 不申请任何权限 | 零 `StoreKit`、零 package 依赖、空的 frameworks 构建阶段、零 `*UsageDescription` | 全篇 |
| 联网只有五处、测速自动发起 | `PlaylistImporter` / `LineSpeedManager` / `HLSTimeshiftCache` 三处 `URLSession`、`StreamSession` 的 `AVURLAsset`、`ChannelRow` 的 `AsyncImage` | 描述、隐私政策、FAQ |

### 排除项一：免费播放器的比较——一个字都不写

作者原话已经说得很清楚（见上）。**素材里没有写过任何播放器的名字**，也没有写过「同类」。
`AGENTS.md` 里那句「用户不需要先判断这个 app 是不是在盗播，才敢装它」，
**没有以比较句的形式写进任何一段面向用户的文案**——它被改写成对自己的正面陈述：
不内置节目、不申请摄像头权限、不录像、不上云、列表只存本机。**说的是自己做了什么，不是别人做了什么。**

### 排除项二：第三条差异化——作者自己说它不亮

`AGENTS.md` 里导入宽容度这一条（第 3 条）末尾逐字：

> 这条不是差异化里最亮的一条，但它是「用户第一次导入能不能成功」的全部。

所以素材里的处理是：**照实列出支持哪些格式**（因为用户确实需要知道自己的文件能不能导入），
**但不写成「导入比其他播放器聪明」**，也不写「再也不怕格式不对」。

### 排除项三：把「聚合」当成定位——不写

见第 0 节。商店文案里没有「聚合」二字，主要类别也是娱乐而不是某个内容品类。

### 排除项四：源可用性——不承诺

一键导入的那份表是公开源，**随时可能失效或按地区受限**。素材里写的是「公开测试表」，
没有写「稳定可用」「长期维护」「几十个台随便挑」。FAQ 里明确写了这份表可能失效。

### 排除项五：测速的开销——写成事实，不写成优点

测速在列表渲染时就自动发起，这不是零成本的（消耗流量、对源站发出请求）。
素材的处理是**把它说清楚**：自动、最多 5 并发、6 秒超时、最多 64 KB、没有单独开关。
隐私政策和 FAQ 里都明确写了「它不需要你点」，并且提醒按流量计费时留意。
**这一条没有被包装成「智能加速」之类的卖点。**

---

## 9. 提审前必须先解决的三件事

1. **本地网络权限需要真机确认一次。** App 支持填 `http://192.168.x.x/...` 这类局域网地址，
   但工程里**没有 `NSLocalNetworkUsageDescription`**。静态读代码**判断不出**填了之后会不会弹窗、
   或者会不会被系统拦下。上架前在真机上用一条真实的局域网地址试一次。
   **在那之前，「不申请任何权限」这句话只对公网地址成立**，隐私政策里已经把这个边界写明了。
2. **English 商店本地化与界面语言要对齐。** 界面有中英两套（`LanguageManager.swift`），
   所以英文商店描述不会撞上中文界面——这一点比 SkyStrike 好办。但要确认
   **首次启动的自动选择逻辑**在英文区用户那里真的落到英文，别让人看到英文描述配中文界面。
3. **截图补两张独有功能**（同名源聚合、时移），见第 7 节。不是必填，但现有 7 张里
   一张都没拍到这台 app 真正独有的东西。
