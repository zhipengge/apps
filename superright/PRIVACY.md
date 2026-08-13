# 右键大师 (SuperRight) — 隐私政策 / Privacy Policy

**最后更新 / Last updated: 2026-08-11**

---

## 中文

### 总览

**右键大师不收集、不上传、不分享你的任何数据。** 你的文件、菜单配置、文件模板与文件夹授权信息全部只在你这台 Mac 本地处理和保存。本 App 没有后端服务器，没有云同步，不内嵌任何第三方分析、追踪或广告 SDK，**不发起任何网络请求**——右键菜单、新建文件、拷贝路径、打开终端等所有功能均在你的设备上完成，断网状态下完全可用。

### 我们处理什么、在哪处理

| 数据 | 用途 | 处理/存储位置 |
|---|---|---|
| 菜单配置与文件模板 | 决定右键菜单显示哪些功能与模板 | 本机 App Group 沙盒容器（`~/Library/Group Containers/...`）内的偏好设置 |
| 文件夹授权书签 | 记住你已授权"新建文件"的文件夹，避免重复弹窗 | 本机 App Group 沙盒容器，系统安全书签（Security-Scoped Bookmark），仅本机有效 |
| 你右键操作的文件/文件夹路径 | 执行你触发的动作（新建文件、拷贝路径、打开终端） | **仅内存**，动作完成即释放；拷贝的路径仅进入你本机的剪贴板 |
| 新建的文件 | 按模板在你指定的文件夹创建 | 直接写入你右键的文件夹，App 不留存副本 |

### 我们 *不* 做的事

- ❌ 不发起任何网络请求（App 中没有任何联网代码）
- ❌ 不向任何远端服务器上传你的文件或任何数据
- ❌ 不接入广告网络
- ❌ 不接入分析平台（无 Google Analytics / Firebase / Mixpanel / 友盟 / 神策 / Sentry / 自建埋点 …）
- ❌ 不扫描你的磁盘，不读取未经你授权的任何文件夹
- ❌ 不读取你的通讯录、位置、麦克风、摄像头
- ❌ 不要求登录账号，不绑定手机号/邮箱
- ❌ 不申请"完全磁盘访问"权限

### 网络通信

**本 App 不与任何服务器通信。** 没有更新检查、没有遥测、没有模型或资源下载。你可以在完全断网的环境下使用全部功能。

### 文件访问

右键大师运行在 macOS App Sandbox 中：

- **访达扩展**只在你主动点击菜单项时才操作对应的文件或文件夹；
- 首次在某个文件夹"新建文件"时，系统会弹出标准授权面板（NSOpenPanel）请求你确认，确认后系统生成安全书签保存在本机，该文件夹此后不再询问；
- App 无法访问你未授权的任何位置，也不会扫描或读取磁盘上的其他内容。

### 数据删除

- **撤销文件夹授权**：主 App「权限管理」页面可查看全部已授权文件夹，支持单个撤销或全部撤销；也可直接删除 App Group 容器目录（`~/Library/Group Containers` 下以 `7252W54VUU.com.gezhipeng0201.SuperRight` 命名的文件夹）。
- **全部清除**：从"应用程序"文件夹删除 App，并移除上述容器目录，即无任何残留。

### 联系方式

如对本政策有疑问，请通过 App Store 联系页或本项目仓库的 Issue 提交。

---

## English

### Summary

**SuperRight collects no data, transmits nothing to remote services, and shares nothing with third parties.** Your files, menu settings, file templates, and folder authorizations are processed and stored exclusively on your own Mac. There is no backend server, no cloud sync, no embedded analytics, tracking, or advertising SDK — and **the app makes zero network requests**. Every feature (context menu, new file, copy path, open in terminal) runs entirely on your device and works fully offline.

### What we process and where

| Data | Purpose | Where |
|---|---|---|
| Menu settings & file templates | Decide which actions and templates appear in the context menu | Preferences inside the local App Group sandbox container (`~/Library/Group Containers/...`) |
| Folder authorization bookmarks | Remember folders you've authorized for "New File" so you aren't asked twice | Local App Group container, as system Security-Scoped Bookmarks; valid only on this Mac |
| Paths of items you right-click | Perform the action you trigger (new file, copy path, open in terminal) | **In-memory only**, released when the action completes; copied paths go only to your local clipboard |
| Files you create | Created from a template in the folder you chose | Written directly into that folder; the app keeps no copy |

### What we do *not* do

- ❌ No network requests of any kind (there is no networking code in the app)
- ❌ No upload of your files or any data to any remote server
- ❌ No ad networks
- ❌ No analytics platforms (no Google Analytics / Firebase / Mixpanel / Sentry / custom telemetry)
- ❌ No disk scanning; no access to folders you haven't authorized
- ❌ No access to Contacts, Location, Microphone, or Camera
- ❌ No account sign-up, no phone number, no email
- ❌ No Full Disk Access request

### Network traffic

**The app talks to no servers at all.** No update checks, no telemetry, no downloads. Everything works completely offline.

### File access

SuperRight runs inside the macOS App Sandbox:

- The Finder extension touches a file or folder only when you explicitly click a menu item;
- The first time you create a file in a folder, the standard system authorization panel (NSOpenPanel) asks for your confirmation; the resulting security-scoped bookmark is stored locally, and that folder is never asked about again;
- The app cannot access any location you haven't authorized and never scans your disk.

### Data deletion

- **Revoke folder authorizations**: the "Permissions" page in the main app lists every authorized folder and lets you revoke them individually or all at once; alternatively, remove the App Group container under `~/Library/Group Containers` named `7252W54VUU.com.gezhipeng0201.SuperRight`.
- **Complete wipe**: delete the app from /Applications and remove the container above. Nothing else remains.

### Contact

For questions about this policy, please use the App Store support page or open an issue on the project repository.

---

## 技术声明 / Technical statement

For App Store reviewers and security-conscious users:

- **Sandbox & Hardened Runtime**: both the main app and the Finder Sync extension are sandboxed (`com.apple.security.app-sandbox`) with Hardened Runtime enabled.
- **Entitlements**: `user-selected files (read/write)`, `security-scoped bookmarks (app-scope)`, and one App Group for sharing preferences between the app and its extension — no network entitlements, no device hardware entitlements, no Full Disk Access.
- **Finder integration**: implemented with Apple's public FinderSync extension point (`com.apple.FinderSync`); directory monitoring is used only to display menu items and grants no file access by itself.
- **Folder writes**: gated by user consent through the system NSOpenPanel; consent is persisted as per-folder security-scoped bookmarks stored locally and can be revoked anytime from the in-app Permissions page.
- **Usage descriptions**: purpose strings for Desktop, Documents, Downloads, removable volumes, and network volumes (`NS*UsageDescription`) are declared in both the app's and the extension's Info.plist.
- **Zero network**: the binary contains no networking code paths (no URLSession usage), and `ITSAppUsesNonExemptEncryption` is declared `NO`.
- **No third-party SDK at runtime**: the dependency graph is Apple system frameworks only (SwiftUI, AppKit, FinderSync).
