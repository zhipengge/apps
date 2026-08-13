# 右键大师 (SuperRight)

> Supercharge your Finder right-click menu — new file templates, copy path, open in Terminal, all fully local.
> 让 Mac 访达右键菜单更强大——右键新建文件、拷贝路径、在终端打开，全部本地运行、零联网。

<p align="center">
  <img src="https://img.shields.io/badge/macOS-15.6%2B-blue?logo=apple" alt="macOS 15.6+">
  <img src="https://img.shields.io/badge/SwiftUI-Native-orange?logo=swift" alt="SwiftUI">
  <img src="https://img.shields.io/badge/Network-Zero%20Requests-success" alt="Zero Network">
  <img src="https://img.shields.io/badge/Privacy-Zero%20Tracking-success" alt="Zero Tracking">
</p>

---

## 📖 目录 / Table of contents

- [快速开始 / Quick Start](#-快速开始--quick-start)
- [核心特性 / Features](#-核心特性--features)
- [常见问题 / FAQ](#-常见问题--faq)
- [故障排查 / Troubleshooting](#-故障排查--troubleshooting)
- [反馈与支持 / Support](#-反馈与支持--support)
- [隐私 / Privacy](#-隐私--privacy)

---

## 🚀 快速开始 / Quick Start

### 三步启用 / Enable in 3 steps

1. 打开「右键大师」，首页点击 **去启用**，系统会打开扩展设置面板
2. 在「登录项与扩展 → 访达扩展」中勾选 **右键大师**（旧系统路径为「扩展 → 访达」）
3. 回到访达，在任意文件夹空白处或文件上**右键**，即可看到「右键大师」菜单

```
Open the app → click "Enable" on the Overview page
→ check "SuperRight" under System Settings › Login Items & Extensions › Finder Extensions
→ right-click anywhere in Finder to see the new menu
```

### 首次新建文件 / Create your first file

1. 在访达任意文件夹空白处右键 → **右键大师 → 新建文件 → 文本文档 (.txt)**
2. 首次在该文件夹创建文件时，系统会弹出授权面板 → 点击 **授权**
3. 该文件夹（含子文件夹）此后不再重复询问

### 常用操作 / Common actions

| 操作 | 方式 |
|---|---|
| 新建文件 | 右键 → 新建文件 → 选择模板 |
| 拷贝路径 | 右键文件/文件夹 → 拷贝路径（支持多选批量） |
| 拷贝文件名 | 右键文件 → 拷贝文件名 |
| 在终端中打开 | 右键文件夹 → 在终端中打开 |
| 用指定应用打开 | 右键文件 → 用 XXX 打开（在主 App「打开方式」中添加） |
| 工具栏入口 | 访达工具栏的「右键大师」按钮，功能与右键菜单一致 |

---

## ✨ 核心特性 / Features

- 📄 **右键新建文件** — 内置 txt / Markdown / JSON / HTML / Shell / Python 等 11 种模板，支持自定义模板名称、扩展名与初始内容
- 📋 **拷贝路径 / 拷贝文件名** — 多选批量拷贝，一行一个
- 💻 **在终端中打开** — 支持系统终端、iTerm2、Warp、Ghostty、kitty、Alacritty，自动检测已安装的终端
- 🚀 **用指定应用打开** — 把常用编辑器（VS Code、Sublime Text 等）加入右键菜单，一键打开
- 🧰 **访达工具栏按钮** — 不右键也能触达全部功能
- 🎛 **菜单完全可配置** — 每个功能可独立开关；可选收纳进「右键大师」子菜单或平铺一级菜单
- 🔐 **零联网 / 零追踪** — 无网络请求、无分析 SDK、无广告、无账号，完全本地运行

---

## ❓ 常见问题 / FAQ

### Q1. 启用扩展后右键菜单没有出现？

1. 确认系统设置中「右键大师」的访达扩展开关已打开
2. 在主 App「概览」页确认状态为「访达扩展已启用」
3. 若仍未出现，在终端执行 `killall Finder` 重启访达，或注销后重新登录

### Q2. 为什么新建文件时会弹出授权面板？

右键大师运行在 macOS App Sandbox（沙盒）中，向某个文件夹写入文件前必须获得你的显式授权——这是 App Store 的安全要求。**每个文件夹只需授权一次**，授权后系统会保存安全书签（Security-Scoped Bookmark），该文件夹及其子文件夹后续都不再询问。

### Q3. 授权会让 App 读到我的所有文件吗？

不会。授权仅针对你确认的那个文件夹，且右键大师只在你主动触发「新建文件」时才写入该文件夹。App 不扫描磁盘、不读取其他任何位置、不上传任何数据（它根本没有联网能力）。

### Q4. 支持自定义文件模板吗？

支持。主 App →「新建文件模板」→「添加模板」，填写模板名称、扩展名和可选的初始内容即可。模板可开关、可拖动排序、可删除。

### Q5. 「在终端中打开」支持哪些终端？

自动检测已安装的：系统终端 (Terminal)、iTerm2、Warp、Ghostty、kitty、Alacritty。在主 App「菜单设置」中选择偏好的终端。

### Q6. 右键菜单太长，能收纳一下吗？

可以。「菜单设置 → 收纳进右键大师子菜单」开启后，全部功能收进一个「右键大师」子菜单；关闭则平铺在右键菜单第一级。

### Q7. 如何查看或撤销已授权的文件夹？

主 App →「权限管理」页面会列出所有已授权的文件夹，可单个「撤销」或「全部撤销」。撤销后，下次在对应文件夹新建文件会重新弹出系统授权面板。该页面同时显示访达扩展的启用状态，未启用时可一键跳转系统设置申请。

### Q8. 卸载后会残留什么吗？

从「应用程序」删除 App，并移除 `~/Library/Group Containers` 下对应容器目录，即可清除全部数据（配置与文件夹授权书签），无任何残留。

---

## 🔧 故障排查 / Troubleshooting

### 扩展状态一直显示「未启用」

- 系统设置路径：macOS 13+ 为「系统设置 → 登录项与扩展 → 访达扩展」；部分版本在「隐私与安全性 → 扩展 → 访达」
- 开关打开后回到 App，状态每 2 秒自动刷新

### 新建文件点击后没有反应

- 首次使用请留意授权面板（可能被其他窗口遮挡）
- 在授权面板中**不要切换到其他文件夹**，直接点「授权」即可

### 「在终端中打开」没反应

- 检查「菜单设置」中选择的终端是否仍安装在本机
- 若已卸载所选终端，App 会自动回退到系统终端

---

## 📬 反馈与支持 / Support

遇到问题、有功能建议，选任意一种方式联系：

| 渠道 | 链接 | 适合 |
|---|---|---|
| 🐛 **GitHub Issues** | `https://github.com/<your-username>/superright/issues` | Bug 报告、功能请求 |
| ✉️ **邮件** | `<your-email>` | 私密反馈、商务合作 |

### 反馈 Bug 时请尽量包含

1. **复现步骤**（例如 "在桌面右键 → 新建文件 → txt → 无反应"）
2. macOS 版本与 App 版本号
3. 是否已在系统设置中启用访达扩展
4. 涉及的文件夹位置（桌面 / 下载 / 外置磁盘等）

---

## 🔐 隐私 / Privacy

一句话总结：

> **不联网、不收集、不上传、不分享。**

- App **不发起任何网络请求**，断网可用全部功能
- 配置与模板仅保存在本机 App Group 沙盒容器
- App Sandbox + Hardened Runtime，仅访问你显式授权的文件夹
- **零追踪 / 零分析 SDK / 零广告 / 零账号**

完整版隐私政策见 👉 [PRIVACY.md](./PRIVACY.md) 或在线 [privacy.html](./privacy.html)

---

## 🛠 技术细节 / Tech

| 项目 | 选型 |
|---|---|
| UI 框架 | SwiftUI（macOS 原生） |
| 右键菜单 | FinderSync 扩展（`com.apple.FinderSync` 扩展点） |
| 主 App ↔ 扩展通信 | App Group 共享 UserDefaults（JSON 配置） |
| 文件夹授权 | 系统授权面板 + Security-Scoped Bookmarks，逐文件夹授权、本机保存，App 内「权限管理」可随时撤销 |
| 权限声明 | 已在 Info.plist 声明桌面/文稿/下载/外置磁盘/网络宗卷的用途说明（NS*FolderUsageDescription） |
| 沙盒权限 | `app-sandbox` + `user-selected files (read/write)` + `bookmarks.app-scope` + App Group |
| 网络 | 无任何网络代码，`ITSAppUsesNonExemptEncryption = NO` |
| 最低系统 | macOS 15.6+ |

依赖：仅 Apple 系统框架（SwiftUI / AppKit / FinderSync），无第三方运行时 SDK，无遥测。

---

<p align="center">
  <sub>Made with care for everyone who lives in Finder. · 右键一下，效率起飞。</sub>
</p>
