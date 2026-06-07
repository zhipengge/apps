# Open Terminal

> A clean, focused SSH client for iPhone and iPad — built fresh on SwiftUI with Apple's official SwiftNIO SSH stack.  
> 一款专为 iPhone / iPad 打造的纯净 SSH 终端,基于 Apple 官方 SwiftNIO SSH。

<p align="center">
  <img src="https://img.shields.io/badge/iOS-17.0%2B-blue?logo=apple" alt="iOS 17+">
  <img src="https://img.shields.io/badge/iPadOS-17.0%2B-blue?logo=ipados" alt="iPadOS 17+">
  <img src="https://img.shields.io/badge/SwiftUI-Native-orange?logo=swift" alt="SwiftUI">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT">
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
- [致谢 / Credits](#-致谢--credits)

---

## 🚀 快速开始 / Quick Start

### 添加第一台服务器 / Add your first server

1. 打开 App,点击右上角 `+`
2. 填入 **名称** / **主机** / **端口**(默认 22) / **用户名** / **密码**
3. 可选:打标签、写备注、选主题色
4. 点 **添加** → 返回列表,点击卡片即可连接

```
Open the app → tap "+" → fill Name / Host / Port / Username / Password
→ optional tags & color → tap "Add" → tap the card to connect
```

### 终端中常用操作 / Common terminal gestures

| 操作 | 方式 |
|---|---|
| 发送命令 | 输入框敲 → 回车 / 点 ✈ |
| 翻历史 | 快捷键栏 ↑ / ↓ |
| 中断 | 快捷键栏 **⌃C** |
| 退出 | 快捷键栏 **⌃D** |
| 清屏 | 右上 `⋯` → 清屏 |
| 粘贴剪贴板 | 输入框为空时,右侧粘贴图标 |
| 看历史输出 | 直接上滑(最多 1000 行 scrollback) |
| 切主题 | 设置 → 个性化 → 主题 |

---

## ✨ 核心特性 / Features

- 🔒 **PTY 真实终端** — bash / zsh / vim / htop / tail -f 完整可用,ANSI 颜色与光标定位齐全
- 🎯 **Core Text 像素级渲染** — 每个字符严格落格,告别错位
- 📜 **1000 行 Scrollback** — 旧输出永不丢,随时上滑回看
- ⚡ **命令面板** — 15+ 内置 + 任意自定义命令,一键发送
- 🎨 **8 套精选主题** — Dracula / Nord / Monokai / Solarized / One Dark / Tokyo Night / Dark / Light,切换实时生效
- ⌨️ **快捷键栏** — Esc / Tab / ⌃C / ⌃D / ⌃L / ↑↓←→ / `|` `~` `\` 一键直达
- 🗂️ **多服务器卡片视图** — 标签、备注、主题色、TCP 探测、长按编辑
- 💓 **连接保活** — 可调心跳防止 NAT 断开
- 📋 **完整备份** — JSON 导出/导入,密码安全留 Keychain
- 🔐 **Keychain 加密** — 密码受系统级保护,App 沙盒外不可读
- 🚫 **零追踪** — 无分析 SDK、无广告、无账号、无后端服务器

---

## ❓ 常见问题 / FAQ

### Q1. 连接失败,提示"用户名或密码错误"

**检查清单**:
- 用户名/密码大小写是否正确(SSH 严格区分)
- 服务器 `/etc/ssh/sshd_config` 是否允许密码登录:`PasswordAuthentication yes`
- 是否对该 IP 触发了 `fail2ban` 临时封禁(短时间内多次失败)
- root 用户是否被禁:`PermitRootLogin yes` 或换非 root 账号

### Q2. 连接超时

- 网络是否可达:用编辑页底部 **"测试 TCP 连接"** 按钮先做 TCP 握手
- 防火墙是否放行 22 端口(或你自定义的端口)
- 移动数据下某些运营商屏蔽非常用端口,试试切 Wi-Fi 验证

### Q3. 输入命令后没有任何反应

v1.0 已修复多个根因 bug(PTY 时序、CSI 解析、UTF-8 切片),如仍出现:
1. 退出终端 → 重新连接(部分情况是 PTY 已断但 UI 未感知)
2. 检查服务器 shell 是否健康:`echo hello` 是否回显
3. 尝试切到另一台服务器排除是不是单机问题
4. 复现后通过下方「反馈」渠道把**截图 + 服务器系统/shell 版本**发给我

### Q4. 中文显示乱码 / 部分字符变成 □

- 确认服务器 locale:`echo $LANG` 应该是 `en_US.UTF-8` 或 `zh_CN.UTF-8`
- 若服务器只配了 `C` locale,中文程序会输出 GBK,本 App 解码 UTF-8,会乱码 → 在 server 端执行 `export LANG=en_US.UTF-8` 解决

### Q5. 横竖屏切换后内容会消失吗?

不会。v1.0+ 已实现 scrollback 不丢失,旋转时按列宽自动重排,历史保留。

### Q6. 我的密码会上传到云端吗?

**绝对不会**。密码只存在 iPhone 系统 Keychain 中,Keychain 是 Apple 系统加密,App 沙盒外读不到。我们没有后端服务器,没有云同步,导出备份 JSON 时**也不包含密码**。详见 [隐私政策](./PRIVACY.md)。

### Q7. 切换主题后旧的输出颜色没变

v1.0+ 已修复 — 颜色按"语义角色"存储(`.default` / `.ansi(0..15)` / `.rgb` / `.palette256`),渲染时按当前主题实时解析。如果你仍在旧版本上,**主题确实只对之后的字符生效**,升到最新版本即可。

### Q8. 支持密钥登录(SSH key)吗?

v1.0 **仅支持密码认证**。密钥登录 (RSA / Ed25519 / ECDSA) 在路线图中,会在后续版本加入。

### Q9. 支持端口转发 / SOCKS 代理 / 文件传输 (SFTP) 吗?

v1.0 暂不支持,聚焦"稳的交互式终端"。这些功能在收集需求中,如果你强烈需要某项,请通过下方反馈渠道告诉我。

### Q10. iPad 上支持外接物理键盘吗?

支持。iPad + Magic Keyboard / Smart Keyboard 用起来很顺,文本框正常接键盘输入。注:`⌘C` 这类系统快捷键不会传给 SSH,需用屏幕快捷键栏的 `⌃C`。

### Q11. App 启动后看到的几个示例服务器去哪了?

v1.0 起,首次启动不再注入占位服务器(`127.0.0.1` / `47.x.x.x` / `192.168.1.100`),欢迎你自己添加真实服务器。

### Q12. 升级 App 会清空我的数据吗?

不会。App Store 升级是覆盖安装,UserDefaults / Keychain / 文档目录全部保留,跟系统升级行为一致。只有你**主动从主屏幕删除 App**,iOS 才会清沙盒。

---

## 🔧 故障排查 / Troubleshooting

### 终端显示错乱 / 字符重叠

- 切换字体试试:**设置 → 个性化 → 字体**(Menlo / SF Mono / Monaco / Courier New)
- 字号过大可能让 cols 太小导致频繁 wrap → 试试缩小字号到 12-13pt
- 横屏使用,列数更多,排版更接近桌面终端

### 连接经常被断开

- 启用 **设置 → 连接 → 连接保活**,心跳设 30-60 秒
- 服务器侧也设 `ClientAliveInterval 60` 双保险

### 输入法把命令切错了

- 输入框默认禁用自动大写和自动纠错;若仍有问题,切到英文键盘
- 中文输入法回车有时是"确认候选词"而非"提交命令",切到全英输入更稳

### App 闪退

- 完全杀掉 App 后重启
- 系统 iOS 版本须 17.0+(检查 设置 → 通用 → 关于本机)
- 持续闪退请通过下方反馈渠道,把崩溃发生的复现步骤发我

---

## 📬 反馈与支持 / Support

遇到任何问题、有功能建议、想表达感谢或吐槽,选任意一种方式联系:

### 推荐(响应最快)

| 渠道 | 链接 | 适合 |
|---|---|---|
| 🐛 **GitHub Issues** | https://github.com/yinzheng/open-terminal/issues | Bug 报告、功能请求、公开讨论 |
| ✉️ **邮件** | support@openterminal.app | 私密反馈、商务合作、安全披露 |

### 反馈一个 Bug 时,请尽量包含

1. **复现步骤**(越具体越好,例如 "连接 X 服务器 → 跑 ll → 第 3 行错位")
2. **截图** 或屏幕录像
3. App 版本号(**设置 → 关于 → 版本**)
4. iOS 版本(**系统设置 → 通用 → 关于本机 → 系统版本**)
5. 服务器系统(如 Ubuntu 20.04 / CentOS 7 / macOS 14)
6. 出问题时的命令 / shell prompt 样式

> 这些信息越完整,定位越快。**截图常常比一千字描述更有价值**。

### 安全披露 / Security disclosure

如果发现安全漏洞(密码泄露、Keychain 读取异常、SSH 协议被中间人攻击等),**请勿公开提 issue**,直接发邮件到 `security@openterminal.app`(或 support 邮箱),我会在 48 小时内回复。

### 商业咨询 / Business inquiries

定制版、企业批量授权、白标合作,邮件联系。

---

## 🔐 隐私 / Privacy

我们对隐私的态度可以用一句话总结:

> **不收集、不上传、不分享。**

- 所有服务器配置 / 密码 / 偏好 / 日志 **只在你的设备**
- 密码用系统 **Keychain** 加密,App 沙盒外不可读
- **零追踪 / 零分析 SDK / 零广告 / 零账号**
- 只有两条网络出口,**全是你主动触发**:
  1. SSH 连接到你配置的目标主机
  2. 可选的 TCP 探测(刷新/测试按钮)
- 备份 JSON **从不包含密码**

完整版隐私政策见 👉 [PRIVACY.md](./PRIVACY.md) 或在线 [privacy.html](./privacy.html)

---

## 🛠 技术细节 / Tech

| 项目 | 选型 |
|---|---|
| UI 框架 | SwiftUI + UIKit Bridging |
| SSH 内核 | [Citadel](https://github.com/orlandos-nl/citadel) (MIT) on [Apple SwiftNIO SSH](https://github.com/apple/swift-nio-ssh) (Apache 2.0) |
| 终端渲染 | Core Text 自渲染,glyph 级控制(iSH / Blink / Termius 同路线) |
| ANSI Parser | byte-level 状态机,完整 VT100 / xterm 兼容 |
| 字符集 | UTF-8(支持中文、emoji) |
| 密码存储 | iOS Keychain (`kSecAttrAccessibleAfterFirstUnlock`, 不同步 iCloud) |
| 数据存储 | UserDefaults(配置 + 偏好) |
| 最低系统 | iOS 17.0+ / iPadOS 17.0+ |

依赖图(全部开源,均无遥测):
- swift-nio · swift-nio-ssh · swift-crypto · swift-asn1
- swift-atomics · swift-collections · swift-log · swift-system
- BigInt · Citadel

---

## 🗺 路线图 / Roadmap

近期计划(欢迎在 Issues 投票优先级):

- [ ] SSH Key 登录(RSA / Ed25519 / ECDSA)
- [ ] SFTP 文件传输
- [ ] 端口转发(local / remote / dynamic)
- [ ] 终端文本选中复制
- [ ] iCloud 同步(可选开关,默认关)
- [ ] 跳板机(Jump Host)
- [ ] Mosh 协议支持
- [ ] macOS Catalyst 版本

---

## 🙏 致谢 / Credits

- [Citadel](https://github.com/orlandos-nl/citadel) — 优秀的 Swift SSH 库,作者 [@joannis](https://github.com/Joannis)
- [Apple SwiftNIO](https://github.com/apple/swift-nio) — 底层网络库
- [Dracula Theme](https://draculatheme.com) · [Nord](https://www.nordtheme.com) · [Monokai](https://monokai.pro) · [Tokyo Night](https://github.com/enkia/tokyo-night-vscode-theme) — 主题灵感
- 所有提 Issue、PR、反馈的用户 ❤️

---

## 📄 License

MIT © 2026 Open Terminal contributors.  
SSH 协议实现 © Apple Inc. (Apache 2.0) & Orlandos (MIT)

---

<p align="center">
  <sub>用 ☕ 与 ⌨️ 在通勤路上写成 · Made with care for everyone who lives in a terminal.</sub>
</p>
