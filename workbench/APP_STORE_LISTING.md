# 牧云工作台 (Workbench) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。

---

## 0. 创建 App Record

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **macOS** | iOS |
| 名称（主语言：简体中文） | **牧云工作台** | 工作台、Workbench 牧云（通称易被占） |
| 名称（English 本地化） | **Workbench** | Muyun Workbench |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.Workbench` | 任何旧 ID |
| SKU | `workbench-20261011` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

SKU 与 Bundle ID 都已写在 `Shared/SharedConstants.swift` 里，与本表一致。

### 命名红线（作者在 `AGENTS.md` 里写死的，务必遵守）

**商店名、副标题、关键词里绝对不能出现 `macOS` `Mac` `Finder` `iPhone` `iOS`**（Guideline 5.2.5，Apple 商标）。
本文件下面每一段文案都已经过一遍这条检查。

**「macOS 14.0 或更高版本」这句只出现在描述正文的系统要求一节里**，那是兼容性说明，
是这个字段本来的用途；名称、副标题、关键词里一个字都没有。

App 内 UI 文案同样回避：「菜单栏」可以，「Mac 菜单栏」不行。

设备显示名（`CFBundleDisplayName`）为「牧云工作台」，已用 `plutil` 在构建产物里核对过。
`LSApplicationCategoryType` 为 `public.app-category.productivity`。
`LSUIElement = true`（菜单栏应用，不占 Dock），`ITSAppUsesNonExemptEncryption = false`，
`LSMinimumSystemVersion = 14.0`，加固运行时已开（`flags=0x10000(runtime)`），四项链入沙盒授权已用
`codesign -d --entitlements` 在产物里核对过。

**注意：App 没有任何本地化。** 工程 `developmentRegion` 是 `zh-Hans`，界面文案全是中文硬编码。
如果给 English 也建一份商店本地化，英文用户看到的是「英文描述 + 中文界面」。
要么这轮只上简体中文（主要语言就是它），要么等界面做完英文化再补 English 本地化。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
把一组要一起打开的东西存成一个场景。进入之前先探一遍通不通，解析不了、连不上、证书没过会被拦下，需要登录的照常放行。离开时留一句断点，下次进来先告诉你上次停在哪。
```

**字符数：81 / 170**

### English

```
Save what you open together as a scene, then check: unreachable hosts and bad certificates are flagged, a login wall is not. Leave a note; it resumes where you stopped.
```

**字符数：168 / 170**（只剩 2，改写时留意）

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
牧云工作台是一个常驻菜单栏的场景工具。它把「一组要一起打开的东西」当成一段有记忆的会话来处理，而不是一个动作。

【场景】
一个场景就是一组要一起打开的东西：应用、本地文件或文件夹、网址。点一下进入，它按固定顺序来：先应用、再文件、最后网页。先让应用起来，再把文件交给它，最后开网页，这样浏览器不会抢在前面把焦点占掉。已经在运行的应用不会再拉起一次，所以重复进入同一个场景是安全的。

【进入之前先体检】
通用启动器是「点一下，开了标签页，白屏了才知道坏了」。工作台在打开之前先对每个网址发一个探测请求，只拿响应头就断开，正文一个字节都不收，然后按失败原因告诉你下一步该做什么：

- 域名解析不了，最常见的原因是没连上内网或 VPN
- 连不上或端口不通，服务没起来，或者地址写错了
- 证书没通过，中间有代理在拦
- 需要登录，服务其实是通的，判为正常，照常放行

只有明确打不开的才拦，而且默认不打开它，因为它在浏览器里也只会是个错误页。

「需要登录」被当作正常，这一条是刻意的。把「要登录」误判成「打不开」，用户就不会再信任这个功能了。

【断点，也就是上次停在哪】
启动器没有「上次」。工作台有：离开场景时你留一句话，它同时把那一刻的现场快照一起存下来，只记这个场景里的哪些应用还在跑、哪些已经退了。下次进来，面板第一眼就是「上次在做 X」加上那句话和当时的现场。每个场景保留最近 5 条断点。

它不记浏览器标签页，因为那是它看不到的东西，不假装看得到。

【备份与迁移】
整份数据以一个 JSON 存在本机，没有云端，没有同步，没有账号。所以导出放在最显眼的位置：导出的是一份纯文本 JSON，你可以自己看、自己改。导入只合并不清空，不会拿导入的文件把你现有的场景盖掉。

【刻意少做】
不做账号，不做同步，不做插件系统，不做脚本引擎。每一个都会把「一个下午能配好」变成「一个周末」。

【边界，如实说】
它对「每次开工前要先确认一组内网或线上服务通不通」的人有意义：运维、后端、要连 VPN 的人、同时维护好几套环境的人。如果你只是「想快点打开几个网页」，通用的启动器和快捷启动工具更合适，工作台在这方面没有优势。

【网络与隐私】
App 里只有一个地方联网：连通性巡检。请求只发给你自己场景里填的地址，App 里没有我们的服务器，没有统计，没有检查更新，没有崩溃上报。请求是 GET 加一个只取 1 字节的 Range 头，拿到响应头就断开；会话是无痕的，cookie 和磁盘缓存都关着，所以巡检过哪些地址不会在本机留下痕迹。

本地文件只在你通过系统面板选择之后才被记住，存下来的访问凭证是只读的，用途只有「下次交给系统打开」这一件事。

不申请任何系统权限，系统不会为它弹出授权框。不需要辅助功能，也不需要输入监控。不控制其它应用的窗口，不做窗口布局，不模拟点击。

【系统要求】
需要 macOS 14.0 或更高版本。菜单栏应用，不占 Dock 图标。
```

**字符数：1241 / 4000**

### English

```
Workbench is a scene tool that lives in the menu bar. It treats a set of things you open together as a session with a memory, rather than as a single action.

[Scenes]
A scene is a set of things to open together: apps, local files or folders, and web addresses. One click enters it, in a fixed order: apps first, then files, then web pages. Starting the apps first means files can be handed to them, and pages open last so the browser does not steal focus earlier. Apps that are already running are not launched again, so entering the same scene repeatedly is safe.

[A check before it opens anything]
A general-purpose launcher is click, tab opens, and you find out it is broken when the page is blank. Workbench probes each address first, disconnecting as soon as the response headers arrive and reading none of the body, then tells you what to do next based on why it failed:

- The name will not resolve, most often because you are off the intranet or VPN
- It cannot connect or the port is closed, so the service is down or the address is wrong
- The certificate failed, so a proxy is intercepting the connection
- It needs a login, which means the service is actually reachable, so it is treated as healthy and let through

Only the definitively unreachable cases are stopped, and by default the item is not opened in those cases either, because it would only be an error page in the browser.

Treating a login wall as healthy is deliberate. Mistaking "needs sign-in" for "broken" is exactly what makes people stop trusting the feature.

[Handoff notes, or where you stopped last time]
A launcher has no "last time". Workbench does. When you leave a scene you leave a sentence, and it stores a snapshot of that moment alongside it, recording only which of the scene's apps were still running and which had quit. Next time you enter, the first thing the panel shows is what you were doing, the sentence, and that snapshot. Each scene keeps its five most recent notes.

It does not record browser tabs, because it cannot see them and does not pretend to.

[Backup and migration]
Everything lives as a single JSON on this computer. No cloud, no sync, no account. That is why export sits front and centre: it produces a plain-text JSON you can read and edit yourself. Import only merges, never clears, so importing a file will not wipe the scenes you already have.

[Deliberately fewer features]
No account, no sync, no plugin system, no scripting engine. Each of those would turn an afternoon of setup into a weekend of it.

[Where it helps, honestly]
It matters to people who have to confirm a set of intranet or online services before starting work: operations, backend developers, anyone on a VPN, anyone maintaining several environments at once. If all you want is to open a few pages quickly, a general-purpose launcher is the better tool, and Workbench offers no advantage there.

[Network and privacy]
There is exactly one place where the app goes online: the connectivity check. Requests go only to addresses you typed into your own scenes; the app contains no server of ours, no analytics, no update check and no crash reporting. They are GETs carrying a Range header asking for a single byte, disconnected once the response headers arrive, over an ephemeral session with cookies and the disk cache off, so which addresses you checked leaves nothing behind on this computer.

Local files are remembered only after you pick them in a system panel, and the credential stored is read-only, existing solely to hand the item to the system to open next time.

No system permissions are requested and no permission prompt appears. No Accessibility and no Input Monitoring. It does not control other apps' windows, does not lay out windows, and does not simulate clicks.

[Requirements]
macOS 14.0 or later. A menu bar app with no Dock icon.
```

**字符数：3845 / 4000**（只剩 155，改写时留意）

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名，也不要出现上面那条命名红线里的词。

### 简体中文

```
开工前先确认服务通不通
```

**字符数：11 / 30**

### English

```
Know what is broken first
```

**字符数：25 / 30**（只剩 5，改写时留意）

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名（Raycast、Alfred 都不能写），不要出现命名红线里的词。

### 简体中文

```
场景,启动,运维,内网,vpn,巡检,连通性,效率,菜单栏,断点,一键,开发
```

**字符数：38 / 100**

### English

```
launcher,workspace,scenes,devops,preflight,connectivity,productivity,menubar,checklist
```

**字符数：86 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/workbench/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/workbench/privacy.html` |
| 营销 URL | 留空 |

技术支持是**版本级**字段（改它要跟新版本一起提审），隐私政策是 **App 级**（要有待发版本才能改）。
这两个 URL 一旦提审就不好改了，提审前先确认目录名。

营销 URL 是可选字段，`apps/workbench/` 下没有 `index.html`，填了就是 404，所以留空。

**这两个页面现在还不存在。** `apps/` 是独立仓库 `zhipengge/apps`，Pages 已经开着
（`apps/skystrike/privacy.html` 现在返回 200），但 `apps/workbench/` 这个目录还没提交。
提审前必须先提交并推送这一整个目录，否则 App Store Connect 填的隐私政策链接是空的。

---

## 6. 类别、评级、隐私问卷

### 类别

主要类别填 **效率 / Productivity**，与工程里的
`LSApplicationCategoryType = public.app-category.productivity` 一致。
次要类别可以填 **开发者工具 / Developer Tools**——它真正的用户是运维和后端，
但开发者工具的曝光面更窄，放次要位置比放主要位置合适。

### 年龄分级（需要你定）

问卷不让你直接选档位，是按题作答后由 Connect 判定。这个 App 的实际内容：
是本机效率工具，没有暴力、恐怖、赌博、酒精烟草毒品、色情、脏话、用户生成内容、聊天、广告。
唯一需要留意的是「无限制网页访问」这类题：本 App **不含浏览器**，
它只是把网址交给系统默认浏览器打开，自己不做任何渲染，应作答为否。

按上述事实作答，大概率落在 4+。

### 其余表

| 字段 | 建议 |
|---|---|
| 内购 | **无**。没有 StoreKit 代码，也没有账号系统 |
| App 隐私 | **收集：否**。但要如实勾选「诊断/其它」之外的那一项也没有——App 不向开发者回传任何数据，须与 `privacy.html` 一致。**注意：它确实会向用户自己填的第三方地址发起连接，这是 App 的功能本身**，不是数据收集；隐私问卷问的是「是否向开发者或第三方回传数据」，答案是「否」 |
| 出口合规 | **NO**。`ITSAppUsesNonExemptEncryption = false` 已写在工程里、也在产物里核对过。App 只有系统 HTTPS，没有自研密码学 |
| 辅助功能 / 输入监控 | **不申请**。全局快捷键走系统热键注册，不需要授权 |
| 通知 | **不申请** |

审核备注建议写清：本 App 是菜单栏应用，`LSUIElement` 为真，没有 Dock 图标。
它唯一联网的地方是连通性巡检：只对用户在场景里自己填写的网址发 GET 请求，
带 `Range: bytes=0-0` 只索取 1 字节，并在收到响应头时立即取消任务，不读取正文。
App 不含任何开发者服务器、统计、广告或崩溃上报。沙盒授权四项，按用途取最小。
App 不申请任何系统权限，不会弹出授权框。

---

## 7. 截图

macOS App 的商店截图规格与 iOS 不同：**1280 x 800**（或 2560 x 1600 等 16:10 档位）。

**本轮没有产出截图，截图由另一路做。** 这个目录下现在没有 `screenshots/`。

截图内容建议（都对应界面上真实存在的东西，不要做纯海报式截图）：

| 建议标题 | 副标题 | 对应界面 |
|---|---|---|
| 开工前先探一遍 | 解析不了、连不上、证书没过会被拦下 | 进入前体检的结果列表与判定 chip |
| 需要登录，不是打不开 | 401 和 403 判为正常，照常放行 | 一条「要登录」判定旁边的放行状态 |
| 上次停在哪 | 离开时留一句话，下次进来第一眼就看到 | 面板上的「上次在做」卡片 + 断点 |
| 场景里的东西按顺序开 | 先应用、再文件、最后网页 | 场景详情页（`SceneDetailView`） |
| 数据是你的，看得到也带得走 | 导出是纯文本 JSON，导入只合并不清空 | 备份与迁移页（`BackupView`） |

空状态、纯海报式截图会被拒。**注意：界面本身没有做过鼠标点击级的验证**（见第 9 节），
拍图之前先自己手工走一遍这五条路径。

---

## 8. 交付前必须注意的

| 项 | 现状 | 说明 |
|---|---|---|
| **带系统弹窗的路径完全没验过** | 选文件、选应用、导出、导入这四条路径都会弹授权面板，因此一条都没验 | 截图若涉及这四条路径（尤其是备份与迁移页），先手工走一遍 |
| **`get-task-allow` 出现在当前构建产物里** | 签名用的是 Apple Development 身份，开发 profile 会注入这个 key | 走 App Store 归档时由分发 profile 去掉，但**归档产物没有验证过**（那需要 App Record） |
| **AppIcon 已就位** | `Assets.xcassets` 里只有 `AppIcon` 这一样；源文件是 `Design/appicon.svg` | 要改图标就改那个 SVG 重新渲染，不要手改 catalog 里的 PNG。产物核对：`assetutil` 应列出 10 个 rendition |

---

## 9. 差异化：能用什么、不能用什么

这一节来自 `Workbench/AGENTS.md` 的「一、差异化论证（动手前先想清楚的问题）」
与「三、当前进度」里的「已知不足 / 没有验证的事」。
**下面「不能用」的每一条都是作者自己写下的，照抄即可。**

### 能用的（三条，都是作者自己认定的突破点）

| 能用的说法 | 依据 |
|---|---|
| 进入前体检：把「打开」从一个动作变成一次判断 | `Shared/ProbeVerdict.swift` 的 13 种判定 + 三档可达性；`ProbeService` 的真实探测路径 |
| 断点：启动器没有「上次」 | `HandoffNote` + `PresenceSnapshot`（只记这个场景的 app 还在不在跑） |
| 幂等进入：已在跑的应用不再拉起一次，顺序固定为「应用、文件、网页」 | `ItemOpener` + 进入计划（逻辑测试第 8 组守着） |

### 故意没有用的（以及为什么）

| 没有用的说法 | 为什么不用 |
|---|---|
| 「一键打开一组链接」当卖点 | 作者原话：「**『一键打开一组链接』不是突破。** 那就是个启动器。Raycast 的 Quicklinks、Alfred 的 workflow 都能做，而且免费、更快、生态更大。**做同一个动作做得更差，没有存在理由。**」描述里一个字都没把它当卖点 |
| 「干净无追踪」当卖点 | 作者原话：「**『干净无追踪』也不是突破。那是定位（positioning），不是能力。任何人都能声称，用户也无法验证。**」所以它只出现在隐私政策里（因为沙盒授权可以核），**没有出现在任何一句销售文案里** |
| 「比 Raycast / Alfred 好」 | 作者原话：「**Raycast 与 Alfred 我没有安装、没有运行过**，只读了官方文档、changelog 和搜索摘要。所以上表里它们那几列是**文档级**判断，不是实测级。」描述里没有做过任何竞品对比，关键词里也一个竞品名都没写 |
| 「人人都需要」 | 作者原话：「它对『每次开工前要先确认一组内网/线上服务通不通』的人有意义……对『就想快点打开几个网页』的人，**Raycast 更好，工作台没有优势**。这是一个窄的、可验证的差异，不是『人人都需要』。**补不出更宽的差异，就这么如实说。**」描述里专门留了一节「边界，如实说」，把这条原样写进去 |
| 「功能丰富」「什么都能做」 | 作者原话：差异化之一是**功能更少**，不做账号、同步、插件系统、脚本引擎。描述里把「刻意少做」单列一节 |
| 「窗口管理 / 摆窗口」 | App 明确不做窗口布局，也不控制其它应用的窗口。写了就是假话 |
| 「会自动帮你恢复现场」 | 快照只记「这个场景里的 app 还在不在跑」，**不恢复窗口、不碰浏览器标签页**。描述里的说法是「告诉你当时是什么状态」，不是「帮你恢复」 |
| 「有键盘流 / 全键盘操作」 | 有全局快捷键（最多 9 个场景），但**没有做过点击级的端到端验证**，也没验过快捷键在真实按键下的表现。描述里只写了「设置里可以给场景配快捷键，最多九个」这个事实 |

### 作者标注「没有验证」的（不要当成已经好了）

来自 `AGENTS.md` 的「已知不足 / 没有验证的事」：

- **没有做鼠标点击级别的端到端验证。** 演示钩子走的是真实代码路径，但「用手点那个按钮」这一步没验。
- **带系统弹窗的路径完全没验**：选文件、选应用、导出、导入。
- **Raycast / Alfred 没有实测**（文档级对照）。
- **`get-task-allow` 出现在构建产物里**，归档产物没有验证过。
- **数据只在 UserDefaults 里**，没有 iCloud 同步（刻意的），卸载就没。

所以描述里没有出现「一点就开」「稳定可靠」「已经过充分测试」这类话。
**唯一一处需要特别注意的**：本节「能用的」第一条是「进入前体检」，
这是 App 的核心卖点，而它**恰好属于验过了的那条路径**（作者写明：真实探测
`example.com` 正常 626ms、`.invalid` 域名解析失败并被拦下，截图逐张看过），
所以它是可以放心放在首位的。
