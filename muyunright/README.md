# 牧云右键助手 (MuyunRight)

> Supercharge your Finder right-click menu — new file/folder, copy path, open in Terminal, move/copy to favorites — all fully local.
> 让 Mac 访达右键菜单更强大——新建文件/文件夹、拷贝路径、在终端打开、移动/拷贝到常用文件夹，菜单栏静默后台运行，零联网。

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

1. 打开「牧云右键助手」，首页点击 **去启用**，系统会打开扩展设置面板
2. 在「登录项与扩展 → 文件提供程序」（ⓘ）中打开 **牧云右键助手**（请不要去「Finder」那一项，那是快捷操作，不是本扩展）
3. 回到访达，在任意文件夹空白处或文件上**右键**，即可看到「牧云右键助手」菜单

```
Open the app → click "Enable" on the Overview page
→ System Settings › General › Login Items & Extensions › File Providers (ⓘ) → turn on 牧云右键助手
→ right-click anywhere in Finder to see the new menu
```

### 首次新建文件 / Create your first file

1. 在访达任意文件夹空白处右键 → **牧云右键助手 → 新建文件 → 文本文档 (.txt)**
2. 首次在该文件夹创建文件时，系统会弹出授权面板 → 点击 **授权**
3. 该文件夹（含子文件夹）此后不再重复询问

### 常用操作 / Common actions

| 操作 | 方式 |
|---|---|
| 新建文件 | 右键 → 新建文件 → 选择模板（可在「菜单设置」开启「新建前询问名称」） |
| 新建文件夹 | 右键 → 新建文件夹 |
| 拷贝路径 / 文件名 / 终端路径 / 链接 | 右键文件/文件夹 → 对应菜单项（支持多选） |
| 在终端中打开 | 右键文件夹（或空白处）→ 在终端中打开 |
| 移动到 / 拷贝到 | 右键选中项 → 移动到/拷贝到 → 常用文件夹、最近位置或「其他位置…」 |
| 用指定应用打开 | 右键文件 → 用 XXX 打开（在主 App「打开方式」中添加） |
| 工具栏入口 | 访达工具栏的「牧云右键助手」按钮，功能与右键菜单一致 |
| 打开设置 | 点击菜单栏「牧云右键助手」图标 → 打开牧云右键助手 |

---

## ✨ 核心特性 / Features

- 📄 **右键新建文件 / 新建文件夹** — 内置 txt / Markdown / JSON / HTML / Shell / Python 等 11 种模板，支持自定义；模板内容可用 `{{name}}`、`{{date}}` 等占位符自动填充，也可开启「新建前询问名称」
- 📋 **拷贝路径 / 文件名 / 终端路径 / file:// 链接** — 多选批量拷贝；终端路径自动 shell 转义，可直接粘贴到命令行
- 💻 **在终端中打开** — 支持系统终端、iTerm2、Warp、Ghostty、kitty、Alacritty
- 📁 **移动到 / 拷贝到常用文件夹** — 在主 App「常用文件夹」配置目标，右键一键归档；自动记住最近去过的位置
- 🚀 **用指定应用打开** — 把常用编辑器（VS Code、Sublime Text 等）加入右键菜单
- 🧰 **访达工具栏按钮** — 不右键也能触达全部功能
- 🕹 **菜单栏静默后台** — 默认不弹主窗口，关窗驻留；支持开机自启，Dock 与菜单栏图标都可按需隐藏
- 🎛 **菜单完全可配置** — 每个功能可独立开关；可收纳进子菜单（名称可改）或平铺一级菜单；设置页内置与访达完全一致的**实时预览**
- 💾 **设置可导出导入** — 换机、重装后一键还原模板与常用文件夹
- 🔐 **零联网 / 零追踪** — 无网络请求、无分析 SDK、无广告、无账号，完全本地运行

---

## ❓ 常见问题 / FAQ

### Q1. 启用扩展后右键菜单没有出现？

1. 确认系统设置中「牧云右键助手」的访达扩展开关已打开
2. 在主 App「概览」页确认状态为「访达扩展已启用」
3. 若仍未出现，在终端执行 `killall Finder` 重启访达，或注销后重新登录

### Q2. 为什么新建文件、移动/拷贝时会弹出授权面板？

牧云右键助手运行在 macOS App Sandbox（沙盒）中，执行新建、移动/拷贝、复制副本这类**写入操作**前必须获得你的显式授权——这是 App Store 的安全要求。**每个文件夹只需授权一次**，授权后系统会保存安全书签（Security-Scoped Bookmark），该文件夹及其子文件夹后续都不再询问。若取消授权，会有提示引导你再次操作并完成授权；已授权列表可在主 App「权限管理」中查看和撤销。

「在终端中打开」「用指定应用打开」这类只是把路径交给别的 App 的操作通常不需要授权，只有在系统确实拒绝时才会请求。

### Q3. 授权会让 App 读到我的所有文件吗？

不会。授权仅针对你确认的那个文件夹，且牧云右键助手只在你主动触发对应操作时才访问该文件夹。App 不扫描磁盘、不读取其他任何位置、不上传任何数据（它根本没有联网能力）。

### Q4. 支持自定义文件模板吗？

支持。主 App →「新建文件模板」→「添加模板」，填写模板名称、扩展名和可选的初始内容即可。模板可开关、可拖动排序、可删除。

初始内容里可以写占位符，新建时自动替换：`{{name}}`（文件名，不含扩展名）、`{{filename}}`、`{{date}}`（2026-08-18）、`{{time}}`、`{{datetime}}`、`{{year}}`。

### Q5. 新建的文件总叫「未命名」，能直接起名吗？

可以。「菜单设置 → 新建行为 → 新建前询问名称」开启后，每次新建会先弹出输入框。名字里带扩展名（如「周报.md」）就按你写的来，不带则用模板的扩展名。不开启时新建的文件会在访达中被自动选中，按回车即可改名。

### Q6. 「在终端中打开」支持哪些终端？

自动检测已安装的：系统终端 (Terminal)、iTerm2、Warp、Ghostty、kitty、Alacritty。在主 App「菜单设置」中选择偏好的终端。

### Q7. 右键菜单太长，能收纳一下吗？

可以。「菜单设置 → 菜单样式 → 收纳进子菜单」开启后，全部功能收进一个子菜单（根菜单名称也能改成你喜欢的）；关闭则平铺在右键菜单第一级。同一页底部的「菜单预览」会实时显示访达里将出现的菜单，不必来回切换验证。

### Q8. 如何查看或撤销已授权的文件夹？

主 App →「权限管理」页面会列出所有已授权的文件夹，可单个「撤销」或「全部撤销」。撤销后，下次在对应文件夹新建文件会重新弹出系统授权面板。该页面同时显示访达扩展的启用状态，未启用时可一键跳转系统设置申请。

### Q9. 换了新 Mac，能把设置带过去吗？

可以。「通用设置 → 设置的备份与恢复 → 导出设置…」导出一个 JSON，在新机器上「导入设置…」即可。文件夹授权是系统安全书签、只在原机器有效，所以新机器上首次操作某个文件夹时仍会请求一次授权。

### Q10. 卸载后会残留什么吗？

从「应用程序」删除 App，并移除 `~/Library/Group Containers` 下对应容器目录，即可清除全部数据（配置与文件夹授权书签），无任何残留。

---

## 🔧 故障排查 / Troubleshooting

### 扩展状态一直显示「未启用」

- 系统设置路径：macOS 15.2+ 为「系统设置 → 通用 → 登录项与扩展 → 文件提供程序 ⓘ」。开关不在名为「Finder」的那一项里（那是快捷操作）
- 开关打开后切回 App，状态会立即刷新

### 新建文件点击后没有反应

- 首次使用请留意授权面板（可能被其他窗口遮挡）
- 在授权面板中**不要切换到其他文件夹**，直接点「授权」即可
- 操作成功时屏幕下方会有一条浮层提示；若想关掉，见「菜单设置 → 操作反馈」

### 「在终端中打开」提示没有权限 / 没反应

- 这项操作通常不需要授权；只有系统确实拒绝时才会弹出「牧云右键助手 — 文件夹授权」面板，请选择当前文件夹并点 **授权**（不要切换到别的目录）
- 若误点取消，再次执行「在终端中打开」会重新请求；也可看扩展弹出的提示说明
- 检查「菜单设置」中选择的终端是否仍安装在本机；已卸载时会自动回退到系统终端
- 已授权文件夹可在主 App「权限管理」中确认；异常时可「撤销」后重试

### 启动后看不到主窗口？

这是预期行为：扩展已启用时默认静默后台运行（只显示菜单栏图标）。点击菜单栏图标 →「打开牧云右键助手」即可唤出设置窗口。也可在「通用设置」中开启「启动时显示主窗口」。

---

## 📬 反馈与支持 / Support

遇到问题、有功能建议，选任意一种方式联系：

| 渠道 | 链接 | 适合 |
|---|---|---|
| 🐛 **GitHub Issues** | [提交问题](https://github.com/zhipengge/apps/issues/new?title=%5B%E7%89%A7%E4%BA%91%E5%8F%B3%E9%94%AE%E5%8A%A9%E6%89%8B%5D%20) | Bug 报告、功能请求 |
| 💬 **帮助页** | [support.html](./support.html) | 常见问题速查 |

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

完整版隐私政策见 👉 [PRIVACY.md](./PRIVACY.md) 或在线 [privacy.html](https://zhipengge.github.io/apps/muyunright/privacy.html)

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
