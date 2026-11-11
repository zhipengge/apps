# 牧云音乐 · 隐私政策

最后更新：2026-11-11　适用版本：1.0 及以后

**一句话：这个 App 不收集任何数据。**
没有账号，没有统计，没有广告，没有第三方 SDK，不申请任何系统权限。
你的音乐、歌词、收藏和设置都只在这台手机上。

---

## 我们收集什么

**什么都不收集。** App 没有向任何服务器发送数据的代码路径，也没有集成任何
统计、广告或崩溃上报 SDK。所谓「收集」指把数据传离你的设备——本 App 没有
把任何数据「交给我们」的路径：我们没有服务器。

App 有两处会发生网络流量，性质都是**你让它去取一个文件**，而不是它上报什么：

1. **你粘贴的直连地址。** 你粘贴一个音频 URL，App 用系统网络栈向那个地址
   发起普通的 HTTP(S) 文件请求。请求里不带账号、设备标识或任何个人信息，
   服务端能看到的只是一个常规资源访问（和你在浏览器地址栏输入一个 mp3
   链接没有区别）。
2. **Wi-Fi 传歌（默认关闭）。** 只有你在设置里手动开启后，App 才在本机
   固定端口开启一个上传页面，供**同一局域网**里的电脑或其他手机把文件
   传进这台手机。它纯被动监听、不广播（不用 Bonjour）、不连外网；
   关掉开关即彻底停掉。

除这两处外，App 没有任何外部请求。飞行模式下除直连地址外全部功能可用。

## 你的数据存在哪里

全部在这台手机的 App 沙盒里，分三块：

- **音频文件**：导入的音乐在沙盒的 `Documents/MuYunMusic/` 下，
  按文件夹结构存放（直连导入的流不落盘，只在播放时缓存）。
- **曲库与偏好**：`UserDefaults`，键名前缀 `muyunmusic.`
  （曲库索引、收藏、歌单、队列位置、最近添加、外观/排序等设置、
  每首歌的歌词偏移、Wi-Fi 传歌开关）。
- **封面缓存**：沙盒 `Application Support/Covers`。

另有极小一块 App Group 容器（`group.com.gezhipeng0201.MuYunMusic`），
只用作**分享扩展 → 主 App** 的文件中转箱：你在微信里分享一首歌给本 App 时，
系统先把文件放进这块共享区，主 App 处理完即清空。它和 App 在同一台手机上。

其他 App 读不到这些数据，它们也不会离开这台设备。

## 权限：一个都不申请

相册、相机、麦克风、通讯录、位置、通知、追踪（ATT）、本地网络——
全部不申请。（后台播放音频是后台模式声明，不是需要弹窗同意的权限。）
分享走系统分享面板，去哪由你决定，App 不接触内容去向。

## 内容边界（顺便说清楚）

本 App 是播放工具：不内置、不提供、不抓取、不推荐任何曲库或歌单，
界面里没有「发现」「推荐」入口。所有内容只能来自你自己的文件和你自己
粘贴的地址。你播放什么内容，由你自己负责。

## 删除数据

在曲库里删除歌曲/清空曲库即刻生效；卸载 App，沙盒连同所有数据一起删除。
我们这边没有任何副本——没有可以存副本的地方。

## 儿童

App 不针对儿童设计，也不收集任何人的数据（包括儿童）。

## 政策变更

有改动会更新本页顶部日期。「不收集数据」这一点，我们无意改变。

## 联系

gezhipeng0201@gmail.com

---

## Privacy Policy (English)

**In one sentence: this app collects nothing.** No account, no analytics,
no ads, no third-party SDKs, and it asks for no system permissions. Your
music, lyrics, favorites and settings live only on this iPhone.

**What we collect:** nothing. There is no code path that sends data to any
developer-controlled server, and no analytics, advertising or crash SDK is
bundled. The only network traffic comes from actions you take yourself:
(a) when you paste a direct audio URL, the app makes a plain HTTP(S) file
request to that address — carrying no account, device identifier or
personal information; and (b) the optional Wi-Fi transfer page, which is
off by default, listens passively on a fixed local port for uploads from
devices on your own LAN only, never reaching the internet.

**Where your data lives:** entirely inside the app sandbox on your device —
imported audio files under `Documents/MuYunMusic/`, library index, favorites,
playlists, queue, settings and per-song lyric offsets in `UserDefaults`
(key prefix `muyunmusic.`), and an artwork cache. A tiny App Group container
is used only to relay files from the share extension to the main app.

**Permissions:** none. The app requests no Photos, Camera, Microphone,
Contacts, Location, Notifications, Tracking, or Local Network access.

**Content:** the app ships no catalog and aggregates nothing; everything it
plays comes from files you import or addresses you paste.

**Deleting data:** uninstall the app and everything goes with the sandbox.
Contact: gezhipeng0201@gmail.com
