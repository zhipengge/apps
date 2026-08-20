# 即刻 (JiKe) — 隐私政策 / Privacy Policy

**最后更新 / Last updated: 2026-08-20**

---

## 中文

### 总览

**即刻不收集、不上传、不分享你的任何数据。** 配置、标签会话与终端输出全部只在你这台 Mac 本地处理和保存。本 App 没有后端服务器，没有云同步，不内嵌任何第三方分析、追踪或广告 SDK。

你主动「在网页搜索」或打开链接时，系统会用默认浏览器访问对应网站。这是系统打开行为，不是即刻自己的联网代码。

### 我们处理什么、在哪处理

| 数据 | 用途 | 处理/存储位置 |
|---|---|---|
| 外观与行为配置 | 记住热键、配色、窗口大小、自定义命令等 | 本机偏好设置（`~/Library/Preferences/com.gezhipeng0201.JiKe.plist`） |
| 标签快照（标题、工作目录、分屏结构） | 下次启动恢复标签 | 同上偏好设置中的独立 key |
| 伪终端里的命令与输出 | 运行你的登录 Shell | **仅内存 / 本机 PTY**；你另存为文件时才写入你指定的路径 |
| 你选中的文本 | 拷贝、Quick Open、在网页搜索 | 仅内存；拷贝进入本机剪贴板；搜索交给系统浏览器 |

### 我们 *不* 做的事

- 不向任何远端服务器上传终端内容或配置
- 不接入广告网络
- 不接入分析平台（无 Google Analytics / Firebase / Mixpanel / Sentry / 自建埋点）
- 不读取通讯录、位置、麦克风、摄像头
- 不要求登录账号
- 不申请「完全磁盘访问」

### 文件与终端访问

即刻**不启用 App 沙盒**，以便登录 Shell 能像系统「终端」一样读写你的项目文件。权限边界就是你在这个终端里自己敲的命令。App 不会在后台扫描磁盘。

### 数据删除

从「应用程序」删除 App，并删除 `~/Library/Preferences/com.gezhipeng0201.JiKe.plist`，即无任何残留。

### 联系方式

请通过本项目仓库的 Issue 提交。

---

## English

### Summary

**JiKe collects no data, transmits nothing to remote services, and shares nothing with third parties.** Settings, tab sessions, and terminal output stay on your Mac. There is no backend, no cloud sync, and no analytics, tracking, or advertising SDK.

If you choose "Search the web" or open a link, macOS opens your default browser. That is a system hand-off, not in-app networking.

### What we process and where

| Data | Purpose | Where |
|---|---|---|
| Appearance and behavior settings | Remember hotkey, palette, window size, custom commands | Local preferences (`~/Library/Preferences/com.gezhipeng0201.JiKe.plist`) |
| Tab snapshots (title, cwd, split tree) | Restore tabs on next launch | A separate key in the same preferences file |
| Commands and output inside the PTY | Run your login shell | **In-memory / local PTY**; written to disk only if you export |
| Selected text | Copy, Quick Open, web search | In-memory; copy goes to the local clipboard; search opens the system browser |

### What we do *not* do

- No upload of terminal contents or settings
- No ad networks
- No analytics platforms
- No Contacts, Location, Microphone, or Camera
- No account sign-up
- No Full Disk Access prompt

### File and terminal access

JiKe is **not App Sandboxed**, so your login shell can read and write project files the same way Terminal and iTerm do. The App does not scan the disk in the background.

### Deleting data

Remove the app from Applications and delete `~/Library/Preferences/com.gezhipeng0201.JiKe.plist`.

### Contact

Open an Issue in the project repository.
