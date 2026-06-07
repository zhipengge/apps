# Open Terminal — 隐私政策 / Privacy Policy

**最后更新 / Last updated: 2026-06-07**

---

## 中文

### 总览

**Open Terminal 不收集、不上传、不分享你的任何数据。** 所有服务器配置、密码、命令历史、日志、偏好设置全部仅保存在你这台设备本地。本 App 没有后端服务器,没有云同步,不内嵌任何第三方分析、追踪或广告 SDK。

### 我们存什么、存在哪

| 数据 | 用途 | 存储位置 |
|---|---|---|
| 服务器配置(名称/主机/端口/用户名/标签/备注) | 列表显示与建立 SSH 连接 | 设备本地 `UserDefaults` |
| SSH 密码 | 你连接服务器时使用 | 设备本地 **Keychain**(系统加密,仅本 App 可读) |
| 终端会话输出 | 当前连接期间显示 | **仅内存**,断开连接后立即清空,不持久化 |
| 命令输入历史 | 输入框 ↑/↓ 翻历史 | **仅内存**,会话级,断开即丢 |
| 自定义命令(命令面板) | 一键发送常用命令 | 设备本地 `UserDefaults` |
| 连接日志(成功/失败/断开时间) | 你查看连接情况 | 设备本地 `UserDefaults`,可在设置里随时清空 |
| 偏好设置(主题/字体/字号/触感/保活/超时等) | 你的个性化 | 设备本地 `UserDefaults` |

### 我们 *不* 做的事

- ❌ 不向任何远端服务器上传你的数据
- ❌ 不接入广告网络
- ❌ 不接入分析平台(无 Google Analytics / Firebase / Mixpanel / 友盟 / 神策 / TalkingData / Sentry / 自建埋点 …)
- ❌ 不读取你的通讯录、相册、位置、麦克风、摄像头
- ❌ 不要求登录账号,不绑定手机号/邮箱
- ❌ 不在后台静默上传任何信息

### 网络通信

本 App 仅在以下情况发起网络连接,且**完全是你主动触发的**:

1. **SSH 连接** — 你点击服务器卡片连接时,App 通过 SSH 协议(基于 [Citadel](https://github.com/orlandos-nl/citadel) + [SwiftNIO SSH](https://github.com/apple/swift-nio-ssh))直接连到**你**配置的目标主机。连接细节(主机地址、端口、协议数据)仅在你的设备与目标服务器之间传输,Open Terminal 的开发者无法看到。
2. **TCP 探测** — 你在服务器列表点 "刷新"、或在编辑页点 "测试 TCP 连接" 时,App 用 `Network.framework` 向目标主机做一次 TCP 三次握手,不发送任何 SSH 凭证。

除上述两种你主动触发的连接外,**App 不与任何其他服务器通信**。

### 数据导出与备份

设置 → 数据 → "导出备份" 会生成 JSON,**仅包含**服务器列表(名称/主机/端口/用户名/标签/备注)和偏好设置。**不包含密码**,Keychain 不会被导出。生成后由你自己选择如何分享(系统标准分享面板,完全由你决定走向)。

### 数据删除

- **单条删除**:在服务器列表卡片 "⋯" 菜单或编辑页底部点删除,服务器配置 + Keychain 中的密码会被**同步永久删除**。
- **全部清除**:从 iOS 主屏幕长按图标 → 删除 App。删除后系统会一并清除沙盒(包括 `UserDefaults`、Keychain 项),无任何残留。

### 联系方式

如对本政策有疑问,请通过 App Store 联系页或本项目仓库的 Issue 提交。

---

## English

### Summary

**Open Terminal collects no data, transmits nothing to remote services, and shares nothing with third parties.** All server profiles, passwords, command history, logs, and preferences are stored exclusively on your own device. There is no backend server, no cloud sync, and no embedded analytics, tracking, or advertising SDK of any kind.

### What we store and where

| Data | Purpose | Where |
|---|---|---|
| Server profiles (name, host, port, username, tags, notes) | Display & SSH connection | Device-local `UserDefaults` |
| SSH passwords | Authentication when you connect | Device **Keychain** (system-encrypted, only this app can read) |
| Terminal session output | Displayed during the live session | **In-memory only** — wiped on disconnect, never persisted |
| Command input history | Up/Down arrow recall | **In-memory only** — session-scoped, gone on disconnect |
| Saved commands (command palette) | One-tap send of frequently used commands | Device-local `UserDefaults` |
| Connection log (success/failure/disconnect timestamps) | Your own troubleshooting | Device-local `UserDefaults` — clear anytime in Settings |
| Preferences (theme, font, size, haptics, keep-alive, timeout, …) | Personalization | Device-local `UserDefaults` |

### What we *do not* do

- ❌ No upload of any data to any remote server
- ❌ No ad networks
- ❌ No analytics platforms (no Google Analytics / Firebase / Mixpanel / Sentry / custom telemetry)
- ❌ No access to Contacts, Photos, Location, Microphone, or Camera
- ❌ No account sign-up, no phone number, no email
- ❌ No background silent uploads

### Network traffic

The app initiates network traffic only in the following cases, **all explicitly triggered by you**:

1. **SSH connection** — When you tap a server to connect, the app dials the host you configured over SSH (powered by [Citadel](https://github.com/orlandos-nl/citadel) on top of [SwiftNIO SSH](https://github.com/apple/swift-nio-ssh)). Connection details (host address, port, SSH protocol bytes) travel directly between your device and your server. The Open Terminal author cannot see any of it.
2. **TCP probe** — When you tap "Refresh" on the server list or "Test TCP" on the edit screen, the app performs a single TCP handshake via `Network.framework`. No SSH credentials are sent.

Outside of those two user-initiated paths, **the app talks to no other servers**.

### Export & backup

Settings → Data → "Export backup" produces a JSON file containing **only** your server list metadata (name, host, port, username, tags, notes) and preferences. **Passwords are never exported**; the Keychain is untouched. What you do with the exported JSON (system share sheet) is entirely your choice.

### Data deletion

- **Per-server delete**: Tap the "⋯" menu on a server card or "Delete" on the edit screen. The profile **and** its Keychain password entry are removed permanently and atomically.
- **Complete wipe**: Long-press the app icon on the Home Screen → Delete App. iOS clears the entire app container (including `UserDefaults` and Keychain items), leaving no residue.

### Contact

For questions about this policy, please use the App Store support page or open an issue on the project repository.

---

## 技术声明 / Technical statement

For App Store reviewers and security-conscious users:

- **Source**: Built from public, auditable source. SSH transport uses Apple SwiftNIO SSH (Apache 2.0) via Citadel (MIT).
- **Permissions declared in Info.plist**: only standard `NSAppTransportSecurity` defaults — no special hardware/location/contacts entitlements.
- **Keychain access group**: `com.openterminal.ssh` — entries are protected with `kSecAttrAccessibleAfterFirstUnlock`, never synced to iCloud Keychain by default.
- **No third-party SDK at runtime**: dependency graph is limited to Apple SwiftNIO / Swift Crypto / Swift ASN.1 / Swift Atomics / Swift Collections / Swift Log / Swift System / BigInt / Citadel — all open-source libraries, none with telemetry.
