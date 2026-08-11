# 牧云图片 (MuyunImage) — 隐私政策 / Privacy Policy

**最后更新 / Last updated: 2026-08-11**

---

## 中文

### 总览

**牧云图片不收集、不上传、不分享你的任何数据。** 你的图片、编辑记录、偏好设置全部只在你这台 Mac 本地处理和保存。本 App 没有后端服务器，没有云同步，不内嵌任何第三方分析、追踪或广告 SDK。所有图像处理——包括滤镜、调色、标注、马赛克、内容感知消除与 AI 消除——**全部在你的设备上完成**，图片从不离开你的电脑。

### 我们处理什么、在哪处理

| 数据 | 用途 | 处理/存储位置 |
|---|---|---|
| 你打开的图片 | 显示与编辑 | **仅内存**，通过 macOS 沙盒的"用户选择文件"权限读取；保存时写回你指定的位置 |
| 编辑内容（标注/滤镜/调整/消除区域） | 当前编辑会话 | **仅内存**，随文档保存进你导出的图片，不单独持久化 |
| AI 消除模型（LaMa，约 200MB） | 本地 AI 消除推理 | 设备本地 `~/Library/Containers/.../Application Support/MuyunImage/Models/LaMa`，可随时删除 |
| 打印任务 | 你主动打印图片 | 走 macOS 系统打印服务，App 不留存副本 |

### 我们 *不* 做的事

- ❌ 不向任何远端服务器上传你的图片或任何数据
- ❌ 不接入广告网络
- ❌ 不接入分析平台（无 Google Analytics / Firebase / Mixpanel / 友盟 / 神策 / Sentry / 自建埋点 …）
- ❌ 不读取你的通讯录、位置、麦克风、摄像头
- ❌ 不要求登录账号，不绑定手机号/邮箱
- ❌ 不在后台静默上传任何信息
- ❌ AI 消除**不调用任何云端 API**——模型下载到本地后，推理完全离线

### 网络通信

本 App 仅在**一种**情况下发起网络连接，且完全由你主动触发：

**下载 AI 消除模型** — 当你在"消除"工具中选择"AI 智能消除"并点击下载时，App 通过 HTTPS 从 GitHub Releases（开源项目 [CoreMLaMa](https://github.com/xulihang/CoreMLaMa) 的公开构建）下载 LaMa CoreML 模型文件；直连失败时会尝试若干公共 GitHub 镜像加速站。下载内容是模型文件本身，请求中**不包含**你的任何图片或个人信息。

除此之外，**App 不与任何服务器通信**。如果你不使用 AI 消除功能（内容感知消除无需模型，完全本地），App 可以在完全断网的环境下使用全部功能。

### 文件访问

牧云图片运行在 macOS App Sandbox 中，仅能访问**你通过打开/保存对话框或拖拽主动授予**的文件。App 无法扫描或读取你磁盘上的其他内容。

### 数据删除

- **已下载的 AI 模型**：可在 App 的模型管理界面删除，或直接删除上述 Application Support 目录。
- **全部清除**：从"应用程序"文件夹删除 App，并移除 `~/Library/Containers/com.gezhipeng0201.MuyunImage`，即无任何残留。

### 联系方式

如对本政策有疑问，请通过 App Store 联系页或本项目仓库的 Issue 提交。

---

## English

### Summary

**MuyunImage collects no data, transmits nothing to remote services, and shares nothing with third parties.** Your images, edits, and preferences are processed and stored exclusively on your own Mac. There is no backend server, no cloud sync, and no embedded analytics, tracking, or advertising SDK of any kind. All image processing — filters, color adjustment, annotations, mosaic, content-aware removal, and AI removal — happens **entirely on your device**. Your images never leave your computer.

### What we process and where

| Data | Purpose | Where |
|---|---|---|
| Images you open | Display & editing | **In-memory only**, accessed via macOS sandbox user-selected-file permission; saved back to the location you choose |
| Edits (annotations / filters / adjustments / removal masks) | Current editing session | **In-memory only**, baked into the image you export; never persisted separately |
| AI removal model (LaMa, ~200 MB) | On-device AI inpainting | Device-local `Application Support/MuyunImage/Models/LaMa`, removable anytime |
| Print jobs | Printing you initiate | Handled by the macOS print system; the app keeps no copy |

### What we do *not* do

- ❌ No upload of your images or any data to any remote server
- ❌ No ad networks
- ❌ No analytics platforms (no Google Analytics / Firebase / Mixpanel / Sentry / custom telemetry)
- ❌ No access to Contacts, Location, Microphone, or Camera
- ❌ No account sign-up, no phone number, no email
- ❌ No background silent uploads
- ❌ AI removal **never calls any cloud API** — once the model is downloaded, inference is fully offline

### Network traffic

The app initiates network traffic in exactly **one** case, explicitly triggered by you:

**AI model download** — When you choose "AI Removal" in the removal tool and tap download, the app fetches the LaMa CoreML model over HTTPS from GitHub Releases (the public build of the open-source [CoreMLaMa](https://github.com/xulihang/CoreMLaMa) project), falling back to public GitHub mirror CDNs if the direct connection fails. The request contains **none** of your images or personal information.

Outside of that, **the app talks to no servers at all**. If you never use AI removal (the content-aware removal engine needs no model and is fully local), the app works completely offline.

### File access

MuyunImage runs inside the macOS App Sandbox and can only access files **you explicitly grant** via open/save dialogs or drag & drop. It cannot scan or read anything else on your disk.

### Data deletion

- **Downloaded AI model**: delete it from the in-app model manager, or remove the Application Support folder above.
- **Complete wipe**: delete the app from /Applications and remove `~/Library/Containers/com.gezhipeng0201.MuyunImage`. Nothing else remains.

### Contact

For questions about this policy, please use the App Store support page or open an issue on the project repository.

---

## 技术声明 / Technical statement

For App Store reviewers and security-conscious users:

- **Sandbox & Hardened Runtime**: the app is sandboxed (`com.apple.security.app-sandbox`) with only the `user-selected files (read/write)` entitlement — no network server, no device hardware entitlements.
- **On-device ML**: AI removal uses a locally stored LaMa model executed via Apple CoreML (CPU+GPU). No image bytes are ever transmitted.
- **Content-aware removal**: a pure-CPU PatchMatch implementation compiled into the app; no model, no network.
- **Only network endpoint**: `github.com` releases (plus public mirrors) for the optional one-time model download over HTTPS.
- **No third-party SDK at runtime**: the dependency graph is Apple system frameworks only (SwiftUI, CoreGraphics, CoreML, CoreImage).
