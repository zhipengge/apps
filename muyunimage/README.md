# 牧云图片 (MuyunImage)

> A lightweight, privacy-first image editor for Mac — content-aware & on-device AI object removal, annotations, filters, all fully local.
> 一款为 Mac 打造的轻量隐私优先图片编辑器——内容感知消除 + 本地 AI 消除、标注、滤镜，全部本地处理。

<p align="center">
  <img src="https://img.shields.io/badge/macOS-15.6%2B-blue?logo=apple" alt="macOS 15.6+">
  <img src="https://img.shields.io/badge/SwiftUI-Native-orange?logo=swift" alt="SwiftUI">
  <img src="https://img.shields.io/badge/AI-On--Device%20CoreML-purple" alt="On-Device CoreML">
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

### 消除第一个物体 / Remove your first object

1. 打开 App，拖入或通过"打开"选择一张图片
2. 顶部工具栏点 **消除**（橡皮擦图标）
3. 右侧面板选择引擎：**内容感知消除**（免下载）或 **AI 智能消除**（首次需下载模型）
4. 用笔刷涂抹要去除的物体 → 点 **应用消除**
5. 满意后 **⌘S 保存** 或 **另存为**

```
Open the app → drag in an image → pick the Removal tool
→ choose Content-Aware (no download) or AI Removal (one-time model download)
→ brush over the object → Apply → ⌘S to save
```

### 常用操作 / Common gestures

| 操作 | 方式 |
|---|---|
| 缩放画布 | 触控板捏合 / ⌘+ ⌘- |
| 平移画布 | 移动工具拖动 / 滚轮 |
| 撤销 / 重做 | ⌘Z / ⇧⌘Z |
| 选中标注 | 移动工具点击，拖动/旋转/缩放手柄 |
| 调整笔刷大小 | 右侧面板滑杆 |
| 打印 | 文件菜单 / 顶部工具栏打印按钮 |

---

## ✨ 核心特性 / Features

- 🧽 **双引擎消除** — 内容感知（多尺度 PatchMatch，免联网）+ AI 智能消除（LaMa CoreML，本地推理）
- 🖌️ **笔刷涂抹/擦除** — 自由圈定消除区域，边界自动无缝融合
- 📝 **文字标注** — 字体、字号、颜色可调
- 🔷 **形状工具** — 箭头 / 直线 / 矩形 / 圆角矩形 / 圆形 / 三角形，描边或填充
- ✏️ **自由画笔** — 手绘涂鸦与勾画重点
- 🎯 **选中即改** — 任意标注可拖动、旋转、缩放，属性面板实时同步
- 🧊 **马赛克** — 涂抹打码，强度可调
- 🎨 **滤镜堆栈** — 多滤镜叠加、排序、单独删除
- 🎚️ **精细调色** — 亮度 / 对比度 / 饱和度
- ✂️ **裁剪与透视校正** — 自由裁剪、四点透视拉正
- 🔄 **旋转翻转** — 90° 旋转、水平/垂直镜像
- 🖨️ **系统打印** — 直接调用 macOS 打印服务
- 🔐 **零追踪** — 无分析 SDK、无广告、无账号、无后端服务器

---

## ❓ 常见问题 / FAQ

### Q1. 内容感知消除和 AI 消除有什么区别？

- **内容感知消除**：传统算法（多尺度 PatchMatch），无需下载任何东西，速度快，适合背景纹理规则的场景（草地、天空、墙面）。
- **AI 智能消除**：LaMa 深度学习模型，首次使用需下载约 200MB 模型，之后完全离线。对复杂背景、大面积消除效果更好。

### Q2. AI 模型从哪里下载？安全吗？

模型来自开源项目 [CoreMLaMa](https://github.com/xulihang/CoreMLaMa) 的 GitHub Releases 公开构建，通过 HTTPS 下载；直连 GitHub 失败时自动尝试公共镜像加速。下载请求不携带你的任何图片或个人信息。

### Q3. 我的图片会被上传吗？

**绝对不会**。所有处理（包括 AI 推理）都在你的 Mac 本地完成。App 没有后端服务器，唯一的网络行为就是上述模型下载。断网状态下除模型下载外所有功能可用。

### Q4. 消除后有残影/边界痕迹怎么办？

1. 涂抹时**完整覆盖**目标物体，边缘可稍微多涂一圈
2. 大面积复杂背景建议切换 **AI 智能消除**
3. 对残留部分再次涂抹、二次消除，通常一两次即可干净

### Q5. 支持哪些图片格式？

支持 macOS 系统能解码的主流格式（JPEG / PNG / HEIC / TIFF 等），保存时可选择格式与质量。

### Q6. 撤销能回退几步？

编辑历史在当前会话内多步可撤销（⌘Z），关闭图片后历史清空。

### Q7. 模型下载很慢或失败？

- App 会自动轮询多个镜像源，一般能自动恢复
- 手动重试：模型管理界面点"重新下载"
- 公司网络可能拦截 GitHub，试试切换网络

### Q8. 升级 App 会丢失已下载的模型吗？

不会。模型存放在 App 沙盒的 Application Support 中，覆盖安装保留。只有删除 App 并清空容器目录才会移除。

---

## 🔧 故障排查 / Troubleshooting

### 消除按钮是灰色的

- 需要先用笔刷在图上**涂抹出消除区域**才能应用
- AI 引擎需要先完成模型下载

### 处理很慢

- 消除耗时与涂抹区域大小相关，大区域请耐心等待进度条
- 处理过程中可随时点"取消"

### App 打不开某张图片

- 确认文件未损坏（用"预览"能否打开）
- RAW 格式支持取决于系统解码器版本

---

## 📬 反馈与支持 / Support

遇到问题、有功能建议，选任意一种方式联系：

| 渠道 | 链接 | 适合 |
|---|---|---|
| 🐛 **GitHub Issues** | `https://github.com/<your-username>/muyunimage/issues` | Bug 报告、功能请求 |
| ✉️ **邮件** | `<your-email>` | 私密反馈、商务合作 |

### 反馈 Bug 时请尽量包含

1. **复现步骤**（例如 "打开 X 图 → 涂抹左上角 → 应用消除 → 出现色块"）
2. **截图**（原图 + 结果图对比最有价值）
3. App 版本号与 macOS 版本
4. 图片尺寸与格式

---

## 🔐 隐私 / Privacy

一句话总结：

> **不收集、不上传、不分享。**

- 所有图像处理**只在你的 Mac 本地**完成，包括 AI 推理
- App Sandbox + Hardened Runtime，仅访问你主动选择的文件
- **零追踪 / 零分析 SDK / 零广告 / 零账号**
- 唯一网络出口：你主动触发的 AI 模型下载（GitHub 开源构建）

完整版隐私政策见 👉 [PRIVACY.md](./PRIVACY.md) 或在线 [privacy.html](./privacy.html)

---

## 🛠 技术细节 / Tech

| 项目 | 选型 |
|---|---|
| UI 框架 | SwiftUI（macOS 原生） |
| 内容感知消除 | 自研多尺度金字塔 EM PatchMatch（Wexler 2007 / Barnes 2009 同族），纯 CPU |
| AI 消除 | [LaMa](https://github.com/advimman/lama) via [CoreMLaMa](https://github.com/xulihang/CoreMLaMa)，CoreML CPU+GPU 本地推理 |
| 无缝融合 | 膜插值（Poisson 简化）边界连续性校正 |
| 图像管线 | CoreGraphics + CoreImage |
| 沙盒权限 | 仅 `user-selected files (read/write)` |
| 最低系统 | macOS 15.6+ |

依赖：仅 Apple 系统框架，无第三方运行时 SDK，无遥测。

---

## 🙏 致谢 / Credits

- [LaMa](https://github.com/advimman/lama) — Samsung AI 开源的 inpainting 模型
- [CoreMLaMa](https://github.com/xulihang/CoreMLaMa) — LaMa 的 CoreML 转换
- PatchMatch (Barnes et al. 2009) / Space-Time Video Completion (Wexler et al. 2007) — 内容感知消除算法基础

---

<p align="center">
  <sub>Made with care for everyone who edits images on a Mac. · 你的图片，只属于你。</sub>
</p>
