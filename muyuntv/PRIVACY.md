# 牧云电视 (Muyun TV) — 隐私政策 / Privacy Policy

**最后更新 / Last updated: 2026-10-12**

> 本文件是 `privacy.html` 的 Markdown 存底，内容以 `privacy.html` 为准。App Store Connect 里填的是 HTML 那一份。

---

## 中文

### 总览

**牧云电视不收集你的数据，也没有任何属于我们的服务器。但它确实会联网**——联网是它的全部用途。

它保护隐私的方式不是「不联网」，而是两件事：**所有请求都发往你自己选的地址**，以及**发出去的东西里没有一样能指认到你**。没有账号，没有登录，没有后端，没有广告、分析或崩溃上报 SDK，工程里零第三方依赖。

这个 App 是播放工具，不提供、不托管、不审核任何电视节目。源由你选择。

### 联网发生在哪五处

| 场景 | 什么时候发 | 发往哪里 |
|---|---|---|
| 导入播放列表 | 你粘贴网址并点「导入」 | 你粘贴的那个地址 |
| 一键导入 | 你点「一键导入源」 | 本仓库 GitHub raw 上的 `public_channels.m3u` |
| **线路测速** | **自动，列表一出现就发** | **你列表里每条线路的地址** |
| 播放 | 你点一个频道 | 该频道的流地址（时移开启时会持续拉分片） |
| 加载台标 | 自动，列表渲染到该行时 | 播放列表里带的台标地址 |

写死的网址一共只有五个：一键导入那份公开表、演示频道用的 Apple 公开测试流、导入框里的示例占位符，以及关于页的两个链接（后两个交给系统浏览器打开，App 自己不请求）。除此之外所有地址都来自你自己导入的列表。

### 主动测速这一条要单独说

**它不需要你点。** 列表一出现，App 就会对你列表里的每条线路各发一次探测，用来排序、决定打开时走哪一路。

边界是明确的：最多同时 5 条、每条 6 秒超时、**最多下 64 KB 就主动断开**，并刻意绕开本机缓存以测真实速度。结果只写在本机。可以关掉「按测速排序」「失败自动换线」「打开时用最快线路」，但**探测本身目前没有单独的开关**。

### 伪装成 Safari 的 User-Agent

拉取播放列表时，请求头里的 User-Agent 是写死的：

```
Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1
```

这么做是因为不少源站对「不像浏览器」的请求直接拒绝。它**不携带你的设备型号、系统版本或任何标识**，每次请求都是同一个固定字符串。

### 明文 HTTP

传输层放开了任意加载（`NSAllowsArbitraryLoads = true`），因为很多公开直播源只提供 http，关掉等于让用户的列表大半播不了。

**后果是：对接明文 http 的源时，你和那台源站之间的流量不加密**，同一网络下的第三方可以看到你请求了哪个地址。想避免就只导入 https 的地址。

### 本机存了什么

19 个键，全在这台设备的沙盒里，不上传、不同步：

- 频道列表、收藏、最近观看、监控墙钉选
- 播放偏好（常亮、自动重连、默认静音、铺满画面、低延迟、时移开关、切台保留时移）、界面语言与主题
- 测速结果、播放时长统计

### Cookie、缓存与时移临时文件

- **Cookie 不做清理**：如果源站下发了 Cookie，它会留在这个 App 的容器里直到你删除 App。
- **URLCache 会写盘**：台标图片和播放列表响应体会进入系统的 URLCache，占用是有上限的，但不提供「清除缓存」按钮。
- **时移临时文件**：同一源连续播放满 60 秒后开始暂存分片，最多 30 分钟 / 400 MB / 3 路，离开播放页即删。**强制退出 App 可能留下没有清掉的临时目录**，它们会一直占用空间直到系统回收或你删除 App。

### 权限

**App 不申请任何权限**：没有摄像头、麦克风、相册、通讯录、位置、通知。`Info.plist` 里一个 `*UsageDescription` 都没有。监控墙只是把几个地址分屏播放，不调用摄像头。

关于局域网地址（`http://192.168.x.x/...`）有一条**目前无法静态确认**：iOS 14 之后访问本地网络有独立权限，而本 App 没有声明本地网络用途描述。填了之后会不会弹窗或被系统拦下，需要真机验证。

### 播放行为

- 退到后台时音频继续播放（`UIBackgroundModes: audio`）。
- AirPlay 投屏时，流的地址会交给接收设备，由那台设备去拉流。
- 截图抓的是当前暂停帧，交给系统分享面板，不写相册、不需要相册权限。
- 导出播放列表生成 JSON，同样经系统分享面板发出，发到哪由你决定。

### 我们不做的事

- 不把频道列表上传到开发者服务器
- 不接入广告网络、分析平台或崩溃上报
- 不读取通讯录、位置、麦克风、摄像头、相册
- 不录像、不识别画面里的人、不把监控墙画面传到任何服务器
- 不要求登录账号，不追踪你
- 不内置电视节目列表

### 数据删除

- 列表里左滑删除单个频道；设置里可清空全部，清空后不会自动填回示例。
- 离开播放页即删除时移临时分片（强制退出可能残留，见上）。
- 从主屏幕删除 App，容器内全部数据一并消失，找不回来。**换机前先导出播放列表。**

### 内容与举报

App 不携带任何内容。一键导入那份表只含播出方自己公开发布的流（央视网公开音频，无画面；国际频道官方直播；厂商测试流），可能随时失效或按地区受限。关于页提供免责声明与举报入口，也可以发邮件到 gezhipeng0201@163.com。

---

## English

### Summary

**Muyun TV collects no data from you, and there is no server of ours anywhere. It does use the network**: that is what it is for.

It protects your privacy not by staying offline, but by two things: **every request goes to an address you chose**, and **nothing it sends can be tied to you**. No account, no sign-in, no backend, no ads, analytics or crash-reporting SDK, and zero third-party dependencies.

This app is a player. It does not provide, host or review any TV channel. You choose the sources.

### The five places the network is used

| What | When it fires | Where it goes |
|---|---|---|
| Import a playlist | You paste a URL and tap Import | The address you pasted |
| Quick Import | You tap Quick Import | `public_channels.m3u` on GitHub raw |
| **Line speed test** | **Automatically, as soon as the list appears** | **Every line address in your list** |
| Playback | You tap a channel | That channel's stream URL, and its segments while timeshift is on |
| Logos | Automatically, when the row is rendered | Logo URLs in your playlist |

Exactly five URLs are hard-coded: the public playlist, the Apple test stream used by the demo channel, the example placeholder in the import field, and the two About links, which are handed to the system browser rather than fetched here. Every other address comes from the list you imported.

### The speed test, on its own

**It does not wait for a tap.** As soon as the list appears, the app sends one probe to every line in your list, to sort them and to decide which to open with.

The limits are explicit: at most 5 at a time, a 6-second timeout each, **at most 64 KB before disconnecting**, deliberately bypassing the local cache so the measurement is real. Results stay on the device. Sort-by-speed, auto-switch-on-failure and prefer-fastest can be turned off, but **probing itself has no separate switch at present**.

### A Safari User-Agent

When fetching playlists the request carries this fixed User-Agent:

```
Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1
```

Many sources reject requests that do not look like a browser. It carries **no device model, OS version or identifier**, and it is the same string on every request.

### Plain HTTP

The transport layer permits arbitrary loads (`NSAllowsArbitraryLoads = true`) because many public live sources are http only, and disabling it would stop a large share of users' lists from playing.

**The consequence: with a plain-http source, traffic between you and that source is not encrypted**, and a third party on the same network can see which address you requested. Import https addresses only if you want to avoid that.

### Stored on this device

Nineteen keys, all inside this device's sandbox, never uploaded and never synced:

- Channel list, favourites, recents, monitor-wall pins
- Playback preferences (keep awake, auto reconnect, start muted, fill screen, low latency, timeshift, keep timeshift on switch), interface language and theme
- Speed results and playback duration records

### Cookies, caches and timeshift temp files

- **Cookies are not cleared**: if a source sets one, it stays in this app's container until you delete the app.
- **URLCache writes to disk**: logo images and playlist responses go into the system URLCache. It is bounded, but there is no Clear Cache button.
- **Timeshift temp files**: after 60 seconds of continuous playback on one source the app starts storing segments, up to 30 minutes, 400 MB and 3 lines, deleted when you leave the player. **A force-quit can leave those directories behind**, taking up space until the system reclaims them or you delete the app.

### Permissions

**The app requests no permissions at all**: no camera, microphone, photos, contacts, location or notifications. `Info.plist` declares no usage description of any kind. The monitor wall plays several addresses side by side and never touches the camera.

One open question about LAN addresses (`http://192.168.x.x/...`): local network access has had its own permission since iOS 14, and this app declares no local network usage description. Whether entering one triggers a prompt or is blocked **cannot be determined statically** and needs a real-device test.

### Playback behaviour

- Audio continues when the app goes to the background (`UIBackgroundModes: audio`).
- With AirPlay the stream address is handed to the receiving device, which fetches it.
- Screenshots capture the paused frame and hand it to the system share sheet; they are not written to the photo library and need no photo permission.
- Exporting the playlist produces JSON, also handed to the system share sheet, going wherever you send it.

### What we do not do

- No uploading your channel list to a developer server
- No ad networks, analytics or crash reporting
- No contacts, location, microphone, camera or photos access
- No recording, no detection of people in the video, no upload of monitor-wall video
- No account, no sign-in, no tracking
- No built-in TV channel list

### Deletion

- Swipe to delete one channel; Settings can clear the whole list, and a cleared list is not filled back in.
- Timeshift temp files are deleted when you leave the player (a force-quit may leave some behind; see above).
- Deleting the app removes everything in its container, unrecoverably. **Export your playlist before switching phones.**

### Content and reporting

The app ships with no content. The Quick Import list contains only streams published by the broadcasters themselves (official CCTV audio, with no picture; official international channels; vendor test streams), and it can break or become region-restricted at any time. The About card carries a disclaimer and a report path, or write to gezhipeng0201@163.com.
