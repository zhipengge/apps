# 牧云电视 (Muyun TV) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带 `://` 的字面量。

---

## 0️⃣ 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **牧云电视** | 电视直播、IPTV、万能播放器（通称易被占） |
| 名称（English 本地化） | **Muyun TV** | Live TV Player |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.MuyunTV` | 任何旧 ID |
| SKU | `muyuntv-20260828` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「牧云电视」。

备选店名（创建时报名被占再用）：

- 牧云直播播放器
- 牧云流播放
- MuyunLivePlayer

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

---

## 1️⃣ 推广文本 (Promotional Text)

> **上限 170 字符**

### 简体中文

```
导入你自己的播放列表或直播地址即可播放。最多四路监控墙分屏，断线重连、常亮、定时关闭。不内置电视节目，源由你自己负责。
```

**字符数：59 / 170**

### English

```
Import your list or a stream URL. Pin up to four camera feeds on a wall. Reconnect, keep-awake, sleep timer. No built-in TV. You choose sources.
```

**字符数：144 / 170**

---

## 2️⃣ 描述 (Description)

> **上限 4000 字符**。修改需提交新版本审核。

### 简体中文

```
牧云电视是直播流播放工具。把你自己的播放列表或直播地址加进来，即可在 iPhone 和 iPad 上播放。本应用不提供、不托管任何电视节目或第三方视频。源由你选择，合法性由你负责。

【导入直播源】
- 支持 M3U / M3U8 播放列表，读取分组和台标
- 支持 JSON 和 TXT（名称与地址，一行一条）
- 可从网址下载播放列表，也可从文件导入
- 可手动添加单条直播源
- 默认为合并导入，按地址去重；也可选择覆盖现有列表
- 可导出 JSON，方便备份或换机

【播放】
- 使用系统播放器播放 HLS 和常见 HTTP 视频流
- 全屏观看，可切换上一个 / 下一个频道
- 支持画中画和 AirPlay
- 加载失败时可重试，断线可自动重连
- 播放时可保持屏幕常亮，可定时关闭

【监控墙】
- 把摄像头或其他源钉到监控墙，最多同时看 4 路
- 默认静音，长按格子可单独开声
- 绿 / 橙 / 红表示在线、重连、离线；离线时本机震动
- 不录像、不识别人、不把画面传到服务器

【整理】
- 按播放列表里的分组浏览
- 收藏、最近观看、搜索、编辑、删除
- 清空全部频道后不会自动填回

【语言与外观】
- 中文和 English
- 深色、浅色、跟随系统

【请注意】
本应用是工具，不是直播平台，也不内置频道。请只导入你有权使用的源。关于页提供免责声明和举报入口。
```

**字符数：约 620 / 4000**

### English

```
Muyun TV is a live-stream player. Add your own playlist or stream URL and play it on iPhone and iPad. This app does not provide or host TV programs or third-party video. You choose the sources and are responsible for them.

[Import]
- M3U / M3U8 playlists, including groups and logos
- JSON and TXT (name and URL per line)
- Import from a playlist URL or from a file
- Add a single source by hand
- Merge by default and skip duplicate URLs; optional replace
- Export JSON for backup

[Playback]
- System player for HLS and common HTTP video streams
- Full screen, previous / next channel
- Picture in Picture and AirPlay
- Retry when a source fails; optional auto reconnect
- Keep the screen awake; optional sleep timer

[Monitor wall]
- Pin camera or other feeds, up to four at once
- Muted by default; unmute one tile from the menu
- Green, orange, and red show live, reconnecting, and offline; the device vibrates when a live feed drops
- No recording, no face detection, no upload of the video

[Organize]
- Browse by playlist groups
- Favorites, recents, search, edit, delete
- Clearing the list does not restore samples

[Language and theme]
- Chinese and English
- Dark, light, or follow the system

[Please note]
This is a tool, not a streaming service, and it ships with no channels. Import only sources you are allowed to use. About includes a disclaimer and a report path.
```

**字符数：约 980 / 4000**

---

## 3️⃣ 副标题 (Subtitle)

> **上限 30 字符**。不要写 Apple 产品名。

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

## 4️⃣ 关键词 (Keywords)

> **上限 100 字符**（含逗号）。不要重复 App 名，不要写竞品名。

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

## 5️⃣ URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/muyuntv/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/muyuntv/privacy.html` |
| 营销 URL | `https://zhipengge.github.io/apps/muyuntv/` |

---

## 6️⃣ 类别、评级、隐私问卷

| 字段 | 建议 |
|---|---|
| 主要类别 | 娱乐 / Entertainment |
| 次要类别 | 照片与视频 / Photo & Video |
| 年龄分级 | 按问卷如实填。用户可粘贴任意流地址，若勾选 Unrestricted Web Access 则为 17+ |
| App 隐私 | **不收集数据**。须与 `PRIVACY.md` 一致 |
| 出口合规 | NO（见 `EXPORT_COMPLIANCE.md`） |

审核备注建议写清：本 App 不内置频道；用户需自行导入播放列表后才能播放；关于页有免责声明。

---

## 7️⃣ 截图

iPhone 6.7 寸和 iPad 12.9 寸各 3-10 张真实界面。至少包含：空状态导入引导、频道列表、播放页、监控墙分屏、导入页、设置/关于（免责声明可见）。
