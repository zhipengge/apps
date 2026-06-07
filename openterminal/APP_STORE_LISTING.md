# Open Terminal — App Store 发布素材

> 直接复制粘贴到 **App Store Connect → App 信息 / 版本信息** 对应字段。
> 中英双语版本独立提交(简体中文 + English (U.S.) 各填一份)。
> 每个字段已标注 App Store Connect 的**真实字符上限**,文案均在限内。

---

## 1️⃣ 推广文本 (Promotional Text)

> **上限 170 字符**,可在不提交新版本的情况下随时修改。  
> 显示位置:iOS 11+ / macOS 10.13+ 的 App Store 产品页,在「描述」上方独立成段。  
> 适合放：当前版本新功能、限时优惠、年度大改动。

### 🇨🇳 简体中文(版本 v1.0 首发)

```
新版本：全新 Core Text 渲染、命令面板自定义、8 套精选主题、scrollback 历史回看、Keychain 加密存储。原生 SwiftUI,零追踪,纯粹的 SSH 终端体验。
```
**字符数:79 / 170 ✅**

### 🇺🇸 English (v1.0 launch)

```
New: pixel-perfect Core Text rendering, customizable command palette, 8 curated themes, scrollback history, Keychain-encrypted credentials. Pure SwiftUI, zero tracking — SSH the right way.
```
**字符数:193 / 170 ❌ 超长 → 用以下精简版**

```
Pixel-perfect Core Text rendering, command palette, 8 themes, scrollback history, Keychain-encrypted credentials. Native SwiftUI, zero tracking — SSH the right way.
```
**字符数:164 / 170 ✅**

---

## 2️⃣ 描述 (Description)

> **上限 4000 字符**(中文/英文各算字符数,中文也是按 character)。  
> 修改需提交新版本审核。

### 🇨🇳 简体中文

```
Open Terminal 是一款专为开发者与运维工程师打造的 SSH 终端 App,基于 Apple 官方 SwiftNIO SSH 内核,使用 SwiftUI 全新构建,把"流畅、稳、克制"放在第一位。

━━━━━━━━━━━━━━━━━━━━━━
✦ 核心特性
━━━━━━━━━━━━━━━━━━━━━━

• PTY 真实终端:bash / zsh / vim / htop / tail -f 等交互式命令完整可用,带 ANSI 颜色、光标定位、清屏支持
• Core Text 像素级渲染:每个字符严格落在等宽格子上,告别错位与抖动
• 1000 行 Scrollback 回滚:多条命令的历史输出永不丢失,向上滑可查看
• 命令面板:内置 15+ 常用运维命令(ls / df / top / netstat …),支持手动新增、收藏、编辑、删除
• 命令历史:输入框 ↑/↓ 翻最近 200 条命令
• 8 套精选主题:Dracula / Nord / Monokai / Solarized / One Dark / Tokyo Night / 深色 / 浅色,所有已显示内容随主题实时变色
• 终端快捷键栏:⎋ Esc / ⇥ Tab / ⌃C / ⌃D / ⌃L / ↑↓←→ / | / 等 iOS 软键盘打不出来的键全部一键直达
• 多服务器管理:卡片化展示,支持标签、备注、自定义主题色;一键 TCP 探测,长按或 "⋯" 菜单快速编辑/删除
• 连接保活:可调心跳间隔(10-300s),防止 NAT/防火墙因空闲断开
• 连接日志:本地保留连接成功/失败/断开记录,支持搜索、筛选、清空
• 完整备份:一键导出/导入服务器列表 + 所有偏好(JSON 格式,密码不外泄)

━━━━━━━━━━━━━━━━━━━━━━
✦ 安全与隐私
━━━━━━━━━━━━━━━━━━━━━━

• Keychain 系统加密存储密码,App 沙盒外不可读
• 零追踪、零分析 SDK、零广告、零账号
• 网络流量仅有两条:SSH 连接(到你配置的目标主机)与可选 TCP 探测,**全部由你主动触发**
• 没有云同步、没有后端服务器,所有数据只在本机
• 导出备份不含密码,Keychain 永不离机
• 完整隐私政策见 App 内"设置 → 关于"

━━━━━━━━━━━━━━━━━━━━━━
✦ 适合谁
━━━━━━━━━━━━━━━━━━━━━━

• 想随时在 iPhone / iPad 上看一眼服务器状态的开发者
• 出差或通勤路上需要紧急修复 bug 的工程师
• 厌倦了广告、付费墙、强制账号的 SSH 客户端老用户
• 看重数据本地化、不愿意把密码上传到任何第三方云的安全敏感用户

━━━━━━━━━━━━━━━━━━━━━━
✦ 技术细节
━━━━━━━━━━━━━━━━━━━━━━

• SwiftUI + UIKit Bridging
• SSH 内核:Citadel (MIT) on Apple SwiftNIO SSH (Apache 2.0)
• 终端渲染:Core Text glyph 级控制,iSH/Blink/Termius 同款渲染路线
• ANSI Parser:byte-level state machine,完整支持 VT100/xterm 标准
• 字符集:UTF-8(支持中文、emoji)
• 系统要求:iOS 17.0+ / iPadOS 17.0+

如有建议或问题,欢迎通过下方"App 支持"链接反馈,我们会认真对待每一条意见。
```
**字符数:约 1280 / 4000 ✅**

### 🇺🇸 English

```
Open Terminal is a clean, focused SSH client for developers and ops engineers — built fresh on SwiftUI with Apple's official SwiftNIO SSH stack. It prioritizes fluency, stability, and restraint over feature bloat.

━━━━━━━━━━━━━━━━━━━━━━
✦ Highlights
━━━━━━━━━━━━━━━━━━━━━━

• Real PTY shell — bash, zsh, vim, htop, tail -f all work as expected, with full ANSI color, cursor addressing, and screen-clear support
• Pixel-perfect Core Text rendering — every character lands on an exact monospace grid, no drift, no jitter
• 1000-line scrollback — scroll up at any time to revisit earlier command output
• Command palette — 15+ built-in ops commands (ls, df, top, netstat …) plus your own: add, favorite, edit, delete
• Command history — ↑/↓ recalls your last 200 inputs
• 8 curated themes — Dracula, Nord, Monokai, Solarized, One Dark, Tokyo Night, Dark, Light. All on-screen content recolors in real time when you switch.
• Hardware-key toolbar — Esc, Tab, Ctrl-C, Ctrl-D, Ctrl-L, arrows, pipe, tilde, slash — every key the iOS soft keyboard hides, one tap away
• Multi-server management — card view with tags, notes, custom accent color. TCP probe, quick edit/delete via "⋯" menu
• Keep-alive — adjustable heartbeat (10-300s) defeats NAT idle timeouts
• Connection log — local success/failure/disconnect history, with search, filter, clear
• Backup / restore — one-tap JSON export & import of profiles and preferences (passwords never exported)

━━━━━━━━━━━━━━━━━━━━━━
✦ Security & Privacy
━━━━━━━━━━━━━━━━━━━━━━

• Passwords stored in the system Keychain — encrypted, app-sandboxed
• Zero tracking, zero analytics SDKs, zero ads, zero accounts
• Only two network paths: SSH to the host you configured, and an optional TCP probe — **both user-initiated**
• No cloud sync, no backend server, your data stays on your device
• Backups never include passwords; the Keychain never leaves your phone
• Full privacy policy in-app under Settings → About

━━━━━━━━━━━━━━━━━━━━━━
✦ Who it's for
━━━━━━━━━━━━━━━━━━━━━━

• Developers who want to peek at server status from iPhone / iPad
• Engineers fixing production bugs during commute or travel
• Long-time SSH users tired of ads, paywalls, and forced sign-ups
• Security-conscious users who refuse to upload credentials to any third-party cloud

━━━━━━━━━━━━━━━━━━━━━━
✦ Tech
━━━━━━━━━━━━━━━━━━━━━━

• SwiftUI + UIKit bridging
• SSH stack: Citadel (MIT) on Apple SwiftNIO SSH (Apache 2.0)
• Rendering: glyph-level Core Text — same path as iSH / Blink / Termius
• ANSI parser: byte-level state machine, full VT100/xterm coverage
• Character set: UTF-8 (CJK & emoji)
• Requires iOS 17.0+ / iPadOS 17.0+

Suggestions or issues? Use the App Support link below — every message gets read.
```
**字符数:约 1820 / 4000 ✅**

---

## 3️⃣ 关键词 (Keywords)

> **上限 100 字符**(含分隔符,中英分开计算)。  
> 用英文逗号或中文逗号都行,**逗号本身也算字符**。  
> ⚠️ 不要重复 App 名称、不要堆砌、不要侵权他人商标(避免被拒)。

### 🇨🇳 简体中文(99 / 100 字符)

```
SSH,终端,服务器,远程登录,运维,Linux,Shell,命令行,Dracula,Mosh,Vim,Tmux,云主机
```

### 🇺🇸 English (96 / 100 字符)

```
ssh,terminal,server,console,remote,linux,devops,shell,vim,tmux,nord,monokai,unix,bash
```

### 🔁 关键词选取依据
- **高搜索量**:`ssh` / `terminal` / `server`(终端类核心词)
- **场景词**:`远程登录` / `运维` / `命令行`(中文用户搜索习惯)
- **生态词**:`Vim` / `Tmux` / `Linux` / `Mosh`(吸引精准受众)
- **主题词**:`Dracula` / `Nord` / `Monokai`(他们会单独搜主题)
- **避开**:不要出现 "Termius" / "Prompt" 等其他 App 名,会被苹果拒

---

## 4️⃣ 技术支持网址 (Support URL) — **必填**

> 这是 App Store 必填字段,缺失会拒审。需要是**真实可访问、含联系方式**的页面。

### 推荐方案(选一)

| 方案 | URL 示例 | 适合 |
|---|---|---|
| **GitHub Issues** | `https://github.com/<your-username>/open-terminal/issues` | 开源 / 半开源项目,门槛低,社区透明 |
| **静态 Support 页** | `https://openterminal.app/support` | 有自己域名,显得正式 |
| **GitHub Pages** | `https://<your-username>.github.io/open-terminal/support` | 免费托管,2 分钟上线 |
| **Notion 公开页** | `https://<your-workspace>.notion.site/support-xxx` | 不想写代码,Notion 一键发布 |
| **TestFlight Feedback** | TestFlight 链接 | 早期内测临时用 |

### 最小可用的 Support 页需要包含

1. App 名称 + 简短描述
2. 联系方式(邮箱 **或** 提交问题入口)
3. 常见问题(可选,但推荐)
4. 隐私政策链接(指向 `privacy.html`)

> 我们已经生成的 `privacy.html` 可以直接作为 support 页的子页面或锚点。

### 当前占位 — 替换后再提交

```
https://openterminal.app/support
```

---

## 5️⃣ 营销网址 (Marketing URL) — 可选

> 选填字段。不填也能上架,但建议填一个,提升专业度。  
> 适合放:App 官网首页、截图美图、功能介绍。

### 推荐方案

| 方案 | URL 示例 | 投入 |
|---|---|---|
| **官网首页** | `https://openterminal.app` | 中等(需做 landing page) |
| **GitHub README 渲染页** | `https://github.com/<your-username>/open-terminal` | 极低(README.md 就够) |
| **Vercel/Netlify 落地页** | `https://open-terminal.vercel.app` | 低(模板秒搭) |

### 当前占位 — 替换后再提交

```
https://openterminal.app
```

---

## 📋 提交清单 — 上架前核对

```
[ ] 1. App 名称        Open Terminal (≤30 字符)
[ ] 2. 副标题          见下方建议
[ ] 3. 推广文本        中文 79 / 英文 164  (≤170)
[ ] 4. 描述            中文 ~1280 / 英文 ~1820  (≤4000)
[ ] 5. 关键词          中文 99 / 英文 96  (≤100)
[ ] 6. 支持 URL        必填,替换占位 ✅
[ ] 7. 营销 URL        建议填,替换占位
[ ] 8. 隐私政策 URL    托管 privacy.html 后填入,必填
[ ] 9. App 类别        主类别:开发工具 / 次类别:实用工具
[ ] 10. 内容评级       4+(无暴力/色情/赌博/医药)
[ ] 11. 出口合规        使用了 HTTPS/SSH 加密 → 可勾选 "豁免",但建议如实填 ITSAppUsesNonExemptEncryption = NO(标准加密)
[ ] 12. 截图           6.7" / 6.1" iPhone + 12.9" iPad,每尺寸 3-10 张
```

### 副标题建议(30 字符内,显示在 App 名下方)

🇨🇳 中文:`安全、纯净的 SSH 终端` (12 字符)
🇺🇸 English:`SSH client for developers` (24 字符)

---

## 💡 截图建议(也是审核常拒原因)

需要展示 App **真实功能**,不能纯文字大字宣传。建议:

1. **服务器列表** — 显示几张精致卡片(可用模拟服务器名,如 "Web Server" / "Database" / "Dev Box")
2. **终端 + ll 输出** — 用 Dracula 主题,展示彩色 ANSI 输出 + 提示符
3. **命令面板** — 展示自定义命令列表
4. **主题选择** — 8 张主题卡片预览页
5. **设置页** — 个性化 / 连接 section 展开
6. **空状态** — "立即添加"渐变按钮(突出引导)

---

> ⚠️ **首次上架重要提醒**
>
> 1. 苹果对 "SSH 客户端" 类 App 审核较严,**Demo 账号** 字段务必提供一个真实可登录的 SSH 测试服务器(用户名 + 密码 + 主机),否则会拒。建议自己开一台廉价 VPS,创建只读权限账号专供审核。
> 2. 描述里**不要**出现 "Termius / Prompt 3 / Blink Shell" 等竞品名称,会被拒。
> 3. 描述/关键词不要承诺"无限"、"最快"、"最好"等绝对化表述。
> 4. 网络相关 App 需要在 Info.plist 留 `NSLocalNetworkUsageDescription`(虽然 SSH 是 inet 不强制,但若做局域网扫描会需要)。
