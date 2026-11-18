# 牧云音乐 · 隐私政策

最后更新：2026-11-18　适用版本：1.0 及以后

**一句话：这个 App 不收集任何数据。**
没有账号，没有统计，没有广告，没有第三方 SDK。只有两件事会请求系统授权，
且都由你主动触发：扫码填写家庭影音服务器地址时使用相机；连接你填写的
局域网服务器时使用本地网络。你的音乐、歌词、收藏和设置都只在这台手机上。

---

## 我们收集什么

**什么都不收集。** 这里的「收集」指把数据交给开发者或第三方 SDK 读取。
App 没有向开发者服务器发送数据的代码路径，也没有集成任何统计、广告或
崩溃上报 SDK。我们没有服务器，也没有可以接收你数据的地方。

App 有三类网络流量，性质都是**你主动让它去取一个文件/发一个请求**：

1. **你粘贴的直连地址。** 你粘贴一个音频 URL，App 用系统网络栈向那个地址
   发起普通的 HTTP(S) 文件请求。请求里不带账号、设备标识或任何个人信息，
   服务端能看到的只是一个常规资源访问（和你在浏览器地址栏输入一个 mp3
   链接没有区别）。
2. **Wi-Fi 传歌（默认关闭）。** 只有你在设置里手动开启后，App 才在本机
   固定端口开启一个上传页面，供**同一局域网**里的电脑或其他手机把文件
   传进这台手机。它纯被动监听、不广播（不用 Bonjour）、不连外网；
   关掉开关即彻底停掉。
3. **你填写的家庭影音服务器（可选）。** 你在设置里填入**你自己的**服务器
   地址（也可以扫该服务器首页的二维码）后，App 才会在你点「测试连接 /
   搜索 / 播放 / 下载 / 分享」时，把搜索词、请求的媒体 URL，或你选择分享的
   音频文件发到**那台服务器**。请求不携带账号、设备标识或任何个人信息。
   服务器是你自己的设备，不是我们的；开发者收不到这些内容。地址留空时
   整块服务器 UI 隐藏，App 不发出任何相关请求。

除这三类外，App 没有任何外部请求。飞行模式下除直连地址/自填服务器外
全部功能可用。

## 你的数据存在哪里

全部在这台手机的 App 沙盒里，分三块：

- **音频文件**：导入的音乐在沙盒的 `Documents/` 下，按文件夹结构存放
  （直连导入的流不落盘，只在播放时缓存）。
- **曲库与偏好**：`UserDefaults`，键名前缀 `muyunmusic.`
  （曲库索引、收藏、歌单、队列位置、最近播放、搜索历史、外观/排序等设置、
  每首歌的歌词偏移、Wi-Fi 传歌开关）。
- **封面缓存**：沙盒 `Application Support` 下的 Covers/ 与 Lyrics/。

另有极小一块 App Group 容器（`group.com.gezhipeng0201.MuYunMusic`），
只用作**分享扩展 → 主 App** 的文件中转箱：你在微信里分享一首歌给本 App 时，
系统先把文件放进这块共享区，主 App 处理完即清空。它和 App 在同一台手机上。

其他 App 读不到这些数据；除你主动使用上述三类网络外，它们也不会离开这台设备。

## 权限

**相机（可选）**：只有你在「设置 → 家庭影音配置」点「扫码」时才请求。
相机画面只用于在本机识别二维码里的服务器地址，**不拍照、不保存、不上传**；
识别完成即结束，App 不保留任何画面。

**本地网络（可选）**：只有你填写/扫码得到一个局域网服务器地址，并让 App
去测试、搜索、播放、下载或分享时才请求。App 不扫描、不发现、不枚举网络中
的设备（没有 Bonjour/mDNS）；拒绝后本地播放、导入、歌词等功能不受影响，
只是服务器相关功能不可用。Wi-Fi 传歌也是同一局域网内的本机监听。

**其他权限一个都不申请**：相册、麦克风、通讯录、位置、通知、追踪（ATT）
都不申请。（后台播放音频是后台模式声明，不是需要弹窗同意的权限。）
分享走系统分享面板，去哪由你决定，App 不接触内容去向。

## 内容边界（顺便说清楚）

除随包一首所有者提供的《冬日之光》外，本 App 是播放工具：不内置、不提供、不抓取、不推荐任何第三方曲库或歌单，
界面里没有「发现」「推荐」入口。其余内容只能来自你自己的文件、你粘贴的
地址，或你自己填写的家庭影音服务器。你播放什么内容，由你自己负责。

## 删除数据

在曲库里删除歌曲/清空曲库即刻生效；卸载 App，沙盒连同所有数据一起删除。
我们这边没有任何副本——没有可以存副本的地方。你自建服务器上的分享文件
由那台服务器管理，删除方式取决于你自己的服务器。

## 儿童

App 不针对儿童设计，也不收集任何人的数据（包括儿童）。

## 政策变更

有改动会更新本页顶部日期。「不收集数据」这一点，我们无意改变。

## 联系

gezhipeng0201@gmail.com

---

## Privacy Policy (English)

**In one sentence: this app collects nothing.** No account, no analytics,
no ads, no third-party SDKs. Only two optional system permissions are ever
requested, both from your own action: Camera, when you scan a QR code to fill
in your family media server address; Local Network, when you connect to a
server you entered on your own LAN. Your music, lyrics, favorites and settings
live only on this device.

**What we collect:** nothing. "Collect" here means data made available to the
developer or a third-party SDK. There is no code path that sends data to a
developer-controlled server, and no analytics, advertising or crash SDK is
bundled. We operate no server and have nowhere to receive your data.

There are three kinds of network traffic, all initiated by you:

1. **A direct audio URL you paste.** The app makes a plain HTTP(S) file request
   to that address — carrying no account, device identifier or personal
   information.
2. **Wi-Fi transfer (off by default).** When you enable it, the app listens
   passively on a fixed local port for uploads from devices on your own LAN;
   no Bonjour, no discovery, no internet. Turning it off stops it completely.
3. **Your own family media server (optional).** After you enter the address of
   **your own** server (or scan its QR code), the app sends the search keyword,
   the requested media URL, or the audio file you choose to share to **that
   server** only when you tap test/search/play/download/share. Requests carry no
   account, device identifier or personal information. The server is yours, not
   ours; the developer receives nothing. Leaving the field empty hides all
   server UI and makes no related request.

**Where your data lives:** entirely inside the app sandbox on your device —
imported audio files under `Documents/`, library index, favorites, playlists,
queue, recent plays, search history, settings and per-song lyric offsets in
`UserDefaults` (key prefix `muyunmusic.`), and an artwork/lyrics cache. A tiny
App Group container is used only to relay files from the share extension to the
main app; it is emptied once handled.

**Permissions:** Camera (optional) is used only to decode a server QR code
on-device; frames are never saved or uploaded. Local Network (optional) is used
only to reach a server you entered on your LAN; the app does not scan or
discover devices, and denying it does not affect local playback. The app
requests no Photos, Microphone, Contacts, Location, Notifications or Tracking
access.

**Content:** the app ships no catalog and aggregates nothing; everything it
plays comes from files you import, addresses you paste, or your own server.

**Deleting data:** delete the app and everything goes with the sandbox. We hold
no copy, because there is nowhere for us to hold one. Files you shared to your
own server are managed by that server.

**Children:** the app is not directed to children and collects no one's data.

**Contact:** gezhipeng0201@gmail.com
