# 速查抽屉 (DevDrawer) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。

---

## 0. 创建 App Record

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **macOS** | iOS |
| 名称（主语言：简体中文） | **开发者速查抽屉** | 开发者工具、DevDrawer 速查（通称易被占） |
| 名称（English 本地化） | **DevDrawer** | Dev Drawer Toolbox |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.DevDrawer` | 任何旧 ID |
| SKU | `devdrawer-20261011` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「速查抽屉」。

**注意：App 本身没有任何本地化。** 工程 `developmentRegion` 是 `zh-Hans`，界面文案全是中文硬编码。
如果给 English 也建一份商店本地化，英文用户看到的是「英文描述 + 中文界面」。
要么这轮只上简体中文（主要语言就是它），要么等界面做完英文化再补 English 本地化。

**SKU 这一项没有写进代码**，是本节按仓库建仓日期（2026-10-11）拟的命名，创建时以你实际填的为准。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
复制点什么，按一下快捷键，面板就告诉你它是什么，右侧排出下一步能做什么，按一下拿走结果。48 个小工具，完全离线，剪贴板历史只在内存里，退出即清空。
```

**字符数：74 / 170**

### English

```
Copy something, hit one hotkey, and the panel tells you what it is and ranks what you can do with it. 48 tools, fully offline, clipboard history in memory only.
```

**字符数：160 / 170**（只剩 10，改写时留意）

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
速查抽屉是一个常驻菜单栏的开发者速查工具，48 个小工具。它换掉了「先想清楚该用哪个工具、再打开它、再把内容弄进去」这个流程：你只管复制，剩下的由它来认。

【它把主语从工具换成了内容】
常用工具是工具优先的。你要先知道「我要解码 JWT」，再去找到那个工具，再打开，再把内容粘进去。
速查抽屉反过来：你不需要知道这是什么，也不需要知道该用哪个工具。复制它，按快捷键，面板告诉你它是什么、下一步能干什么，按一下就是结果。

【三种类型的操作】

- 变换：26 个，会顶掉面板里的当前值。Base64 解码、JSON 格式化、URL 编码、哈希、生成 UUID、命名风格转换这些都属于这类。
- 查看：22 个，只出一份报告，不动你的内容。颜色转换、对比度、URL 拆解、进制转换、UUID 解析、字符统计、正则解释这些都属于这类。
- 识别：21 类内容各有一套识别规则。JSON、JWT、UUID、颜色、Cron 表达式、时间戳、ISO 日期、HTTP 日期、Base64、Base64URL、十六进制、URL、邮箱、IPv4、IPv6、语义化版本号、正则、数字、文件路径、代码、纯文本。

【工具清单】
- 解码 9 个：JWT 解码、JWT 过期检查、JWT 时间字段、Base64、Base64URL、十六进制、URL、JSON 反转义、HTML 实体反转义
- JSON 5 个：格式化、排序键、压缩、校验、时间戳字段
- 时间 4 个：时间戳互转、日期转时间戳、Cron 解释、当前时间戳
- 查看 6 个：颜色转换、对比度、URL 拆解、进制转换、UUID 解析、字符统计
- 编码 7 个：Base64、Base64URL、十六进制、URL、URL 组件、JSON 转义、HTML 实体
- 哈希 4 个：哈希（SHA-256、SHA-512、SHA-1、MD5、CRC-32 全算法）、SHA-256、MD5、HMAC-SHA256
- 生成 2 个：UUID v4、UUID v7
- 文本 11 个：命名风格转换、正则匹配、正则解释、与剪贴板 diff、行排序、去重、去空行、修剪、反转、加行号

【它认不出来的时候会怎样】
识别器只覆盖它认得的类型。认不出来的内容会退回按「常用工具」兜底排序，这时候它就退化成一个普通的工具抽屉，不如按类型认出来时准。这一条如实说明，不美化。内容超过 64 KB 时排序也会跳过试探性执行那一步，只按类型表排，推荐质量会降一点，这是为了保证排序永远是常数时间、面板不会卡。

【小工具的取舍】
- 剪贴板历史最多 40 条，可以在设置里改到 1 到 500；单条超过 1 MB 的内容不入历史；列表里每条预览截断到 120 字符。
- 识别只看前 512 KB，推荐排序最多显示 6 条，单次工具输出上限 4 MB。这些上限是为了让面板在大输入下也不卡。
- 参数类工具只有三个（正则匹配、正则解释、HMAC），选了会展开输入框。

【菜单栏 App】
不占 Dock 图标，不进程序切换器。左键开面板、右键出菜单（设置、清空历史、退出）。快捷键默认 ⌥⌘V，可以在设置里改；面板内 ⌘1 到 ⌘9 直接执行推荐里的第几条。

【隐私】
- 完全离线：沙盒权限里根本没有申请网络权限，源码里也没有任何网络 API，断网下 48 个工具全部可用
- 剪贴板历史只在内存里，退出即清空，没有任何写盘路径，磁盘上不留痕迹
- 只读剪贴板的纯文本，不读图片、文件、富文本
- 配置只存一个键，里面只有快捷键、上限、面板尺寸这类偏好，没有你复制过的任何内容
- 不申请任何系统权限：不需要辅助功能，不需要输入监控，不读屏幕，不做自动化，系统不会弹出授权框
- 没有账号，没有广告，没有分析或追踪 SDK，App 里不含任何第三方代码

【系统要求】
需要 macOS 14.0 或更高版本。这是菜单栏 App，没有主窗口。
```

**字符数：1636 / 4000**

### English

```
DevDrawer is a menu bar developer toolkit with 48 small tools. It removes a step you take for granted: knowing which tool you need before you can use it. You just copy something, and the app works out what it is.

[Content first, not tools first]
Most toolboxes are tool-first. You have to know you want to decode a JWT, find that tool, open it, then paste your content in.
DevDrawer inverts it. You do not need to know what the content is, or which tool applies. Copy it, press the hotkey, and the panel tells you what it is and what you can do next.

[Three kinds of action]
- Transforms: 26 of them, and they replace the value in the panel. Base64 decoding, JSON formatting, URL encoding, hashing, UUID generation, case conversion.
- Inspectors: 22 of them, and they produce a report without touching your content. Colour conversion, contrast, URL breakdown, base conversion, UUID parsing, character counting, regex explanation.
- Detection: 21 kinds of content each get their own rules. JSON, JWT, UUID, colour, cron expression, timestamp, ISO date, HTTP date, Base64, Base64URL, hex, URL, email, IPv4, IPv6, semantic version, regular expression, number, file path, code, plain text.

[The tool list]
- Decode, 9: JWT decode, JWT expiry check, JWT time claims, Base64, Base64URL, hex, URL, JSON unescape, HTML entity unescape
- JSON, 5: format, sort keys, minify, validate, timestamp fields
- Time, 4: timestamp conversion, date to timestamp, cron explain, current timestamp
- Inspect, 6: colour conversion, contrast, URL breakdown, base conversion, UUID parse, character count
- Encode, 7: Base64, Base64URL, hex, URL, URL component, JSON escape, HTML entities
- Hash, 4: all hash algorithms (SHA-256, SHA-512, SHA-1, MD5, CRC-32), SHA-256, MD5, HMAC-SHA256
- Generate, 2: UUID v4, UUID v7
- Text, 11: naming case, regex match, regex explain, diff against clipboard, line sort, dedupe, drop blank lines, trim, reverse, number lines

[What happens when it does not recognise something]
The detector only covers the types it knows. Anything else falls back to ranking by what you use most, and at that point it degrades into an ordinary tool drawer, which is less accurate than when the type is recognised. Past 64 KB of input the ranking also skips the trial-execution step and sorts on the type table alone, which lowers the quality of the suggestion; that keeps ranking constant-time so the panel never stalls.

[Deliberate limits]
- Clipboard history holds at most 40 entries, adjustable from 1 to 500; anything over 1 MB is not kept; previews are truncated to 120 characters.
- Detection reads at most the first 512 KB, the ranked list shows at most 6 actions, and a single tool output is capped at 4 MB. These caps exist so the panel stays responsive on large input.
- Only three tools take a parameter (regex match, regex explain, HMAC), and choosing one expands an input field.

[A menu bar app]
No Dock icon, and it stays out of the app switcher. Left click opens the panel, right click gives a menu with settings, clear history and quit. The default hotkey is Option-Command-V and can be changed in Settings; the number keys run the first few ranked actions directly.

[Privacy]
- Fully offline: the sandbox does not request network access at all and there is no networking API in the source, so all 48 tools work with no connection
- Clipboard history is in memory only, cleared when you quit, with no path to disk whatsoever
- Only the plain text on the clipboard is read, never images, files or rich text
- Settings are stored under a single key holding preferences such as the hotkey and the history limit, and none of it is anything you copied
- No system permissions are requested: no Accessibility, no Input Monitoring, no screen reading, no automation, and no permission prompts
- No account, no ads, no analytics or tracking SDKs, and no third-party code at all

[Requirements]
macOS 14.0 or later. It is a menu bar app with no main window.
```

**字符数：3962 / 4000**（只剩 38，改写时留意）

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
复制什么就识别什么的小工具抽屉
```

**字符数：15 / 30**

### English

```
Identify anything you copy
```

**字符数：26 / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
json,jwt,base64,时间戳,uuid,正则,哈希,编码,剪贴板,开发者工具,格式化,离线
```

**字符数：50 / 100**

### English

```
json,jwt,base64,timestamp,uuid,regex,hash,encode,clipboard,developer,format,offline
```

**字符数：83 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/devdrawer/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/devdrawer/privacy.html` |
| 营销 URL | 留空 |

技术支持是**版本级**字段（改它要跟新版本一起提审），隐私政策是 **App 级**（要有待发版本才能改）。
这两个 URL 一旦提审就不好改了，提审前先确认目录名。

营销 URL 是可选字段，`apps/devdrawer/` 下没有 `index.html`，填了就是 404，所以留空。

**这两个页面现在还不存在。** `apps/` 是独立仓库 `zhipengge/apps`，Pages 已经开着
（`apps/skystrike/privacy.html` 现在返回 200），但 `apps/devdrawer/` 这个目录还没提交。
提审前必须先提交并推送这一整个目录，否则 App Store Connect 填的隐私政策链接是空的。

---

## 6. 类别、评级、隐私问卷

### 类别（需要你定，两个都列出来）

| 选项 | 主要类别 | 次要类别 | 理由 |
|---|---|---|---|
| A | 开发者工具 / Developer Tools | 效率 / Productivity | 工程里 `LSApplicationCategoryType` 写的就是 `public.app-category.developer-tools`，工具内容（JWT、正则、哈希、UUID）也全是开发者向的 |
| B | 效率 / Productivity | 开发者工具 / Developer Tools | 开发者工具的曝光面通常小于效率类；如果目标是让更多非开发者看到这个面板，可以换过来，但内容匹配度会下降 |

`LSApplicationCategoryType` 已固定为 `public.app-category.developer-tools`，选 A 与工程一致。

### 年龄分级（需要你定）

问卷不让你直接选档位，是按题作答后由 Connect 判定。这个 App 的实际内容：
是本地文本工具，没有暴力、恐怖、赌博、酒精烟草毒品、色情、脏话、用户生成内容、聊天、广告、网页浏览。
唯一可能影响判定的是「无限制网页访问」这类题，本 App 不含浏览器，应作答为否。

按上述事实作答，大概率落在 4+。

### 其余表

| 字段 | 建议 |
|---|---|
| 内购 | **无**。没有 StoreKit 代码，也没有账号系统 |
| App 隐私 | **不收集数据**。App 不发起任何网络请求，须与 `privacy.html` 一致。注意：偏好设置在 UserDefaults 里是**要另做隐私清单声明**的事（见第 8 节），但它不是「收集数据」，问卷这里照填不收集 |
| 出口合规 | **NO**。`INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO` 已经写在工程里。App 里唯一的密码学用途是给哈希与 HMAC 工具做本地单向摘要（系统 CryptoKit），没有自研算法、没有传输、没有密钥存储 |
| 辅助功能 / 输入监控 | **不申请**。全局快捷键走 Carbon `RegisterEventHotKey`，由系统代管，不需要授权 |

审核备注建议写清：本 App 完全离线，沙盒权限里没有申请网络权限，源码里也没有任何网络 API，断网时全部功能可用。
剪贴板历史只存在内存里，不写盘。不申请任何系统权限，系统不会弹出授权框。这是菜单栏 App，没有主窗口，不占 Dock 图标。

---

## 7. 截图

macOS App 的商店截图规格与 iOS 不同：**1280 x 800**（或 2560 x 1600 等 16:10 档位）。

**本轮没有产出截图，截图由另一路做。** 这个目录下现在没有 `screenshots/`。

截图内容建议（都对应界面上真实存在的东西，不要做纯海报式截图）：

| 建议标题 | 副标题 | 对应界面 |
|---|---|---|
| 复制什么就识别什么 | 面板先告诉你它是什么，再告诉你下一步能干什么 | 识别出 JSON 并给出类型角标的面板 |
| 48 个小工具，按内容排序 | 你不需要先知道该用哪个工具 | 推荐列表展开、⌘1 到 ⌘9 可见的面板 |
| 看完就走，不动你的内容 | 22 个工具只出报告，不覆盖你手上的东西 | 查看类工具的结果（如 URL 拆解或颜色转换） |
| 退出即清空 | 剪贴板历史只在内存里，磁盘上不留痕迹 | 历史侧边栏 + 清空历史的菜单项 |
| 什么都不用授权 | 不需要辅助功能，不需要输入监控 | 设置页（快捷键录制区） |

空状态、纯海报式截图会被拒。

---

## 8. 交付前必须补的（不是文案问题）

| 项 | 现状 | 说明 |
|---|---|---|
| **`PrivacyInfo.xcprivacy` 缺失（唯一真正的硬缺口）** | `Shared/ConfigStore.swift:165` 默认参数是 `UserDefaults = .standard`，读在 `:173`（`defaults.data(forKey:)`）、写在 `:185`（`defaults.set`）、重置在 `:198`（`removeObject(forKey:)`），实例在 `DevDrawerApp.swift:39` 构造——也就是说这个 API 是**真的在用**。但工程里没有任何 `.xcprivacy` 文件，`project.pbxproj` 里也搜不到 `PrivacyInfo` | UserDefaults 属于「需声明理由的 API」，归档上传时会报 ITMS-91053。要补一份清单，声明 `NSPrivacyAccessedAPICategoryUserDefaults`，理由 `CA92.1`（只读写本 App 自己容器里的偏好）。`_tools/gen_privacy_manifest.py` 的 `APPS` 字典里现在也**没有 DevDrawer**——先在字典里加一项（`"dirs": ["DevDrawer/DevDrawer"]`、`"reasons": {"UserDefaults": ["CA92.1"]}` ），再跑一次生成脚本，并把生成的文件加进 Xcode 的同步组，否则不会被打进包 |
| **清单里只应有 UserDefaults 一条** | 除它之外没有用到任何需声明理由的 API：`HistoryStore` 只走内存、不碰文件时间戳、不读磁盘空间和开机时间 | 生成出来的清单里 `NSPrivacyTracking` 为 false、`NSPrivacyCollectedDataTypes` 为空，和 `privacy.html` 里「不收集数据」是一致的——**本地偏好不是 Apple 定义里的「收集数据」**，这两件事不矛盾，别因为这条去改隐私问卷答案 |
| **归档没做过** | 现在只有 Debug 构建，没有 Archive 过，没有分发签名 | 走 App Store 提交是「分发证书 + 归档」，**不需要公证**（公证是商店外分发才走的路径）。但「归档能过」这件事本身还没试过 |
| **全局快捷键端到端没测过** | Carbon `RegisterEventHotKey` 注册成功、没有冲突回报，但「按 ⌥⌘V 面板真的弹出来」没有用真实按键走一遍 | 上架前手工按一次。自动化发的是 ⌘1/⌘2 这类应用内按键，走不到 Carbon 那条路 |
| **多显示器 / 多 Space 没验过** | 面板按鼠标所在屏幕定位（读了 `NSScreen.screens`），但没有在真实多屏、多 Space 环境跑过 | 装机后自己试一次 |
| **大输入的性能没有实测数据** | 64 KB 以上跳过试探执行有断言保证，编辑器也关了自动替换和拼写检查；但「粘 10 MB 文本卡不卡」是设计推断，不是实测 | 有条件就粘一次大文本看看 |
| **`get-task-allow`** | 只出现在本地 debug 构建的 entitlements 里（`codesign -d --entitlements -` 可见） | 走分发 profile 归档时由它替换掉，不用手工处理 |
| **截图** | 本轮没有产出，由另一路做（见第 7 节）。`Screenshots/` 下现有两张本机验证图（`1-panel.png`、`2-decode-result.png`），不是商店规格 | 商店要 1280 x 800 |
| **App 图标** | 已有。`Assets.xcassets/AppIcon.appiconset/` 里 16 到 1024 全套 PNG，生成代码在 `Design/make_icon.swift` | 不缺，这一条不用管 |
| **`apps/devdrawer/` 还没推** | 这个目录在 `apps/` 仓库里还是未跟踪状态，Pages 上因此没有这两个页面（见第 5 节） | 提审前必须先提交并推送 |

可以放心引用的已验证项（来自 `DevDrawer/AGENTS.md` 第 7 节）：
构建成功；`LogicTests/run.sh` 408 条断言全过；`plutil` 验过 `LSUIElement` / Bundle ID / `LSMinimumSystemVersion` 14.0 / `ITSAppUsesNonExemptEncryption` NO；
`codesign -d --entitlements -` 验过 entitlements 里只有 `app-sandbox` 和 `get-task-allow`、**没有网络权限**；源码扫描没有任何网络 API。

---

## 9. 差异化：能用什么、不能用什么

这一节来自 `DevDrawer/AGENTS.md` 的「1.3 为什么这算突破（以及它不算什么）」，
以及「7. 没有验证」两节。**下面「不能用」的每一条都是作者自己写下的，照抄即可。**

### 能用的

作者认定的差异化是**产品层**的，不是技术层的：
把「先选工具」这一步从流程里删掉，主语从工具换成内容。
宣传就应该按这个定位走。

### 故意没有用的（以及为什么）

| 没有用的说法 | 为什么不用 |
|---|---|
| 「工具比别的 App 多」「几百个工具」 | 作者原话：「**工具数量是劣势，不是优势**。48 个动作，DevToys 和 CyberChef 都是几百个。如果用户比较的是『谁的工具多』，这个 App 会输，而且不应该去比。」所以描述里只把 48 这个数字当事实写出来，一次都没有做数量比较 |
| 「独一份」「别人做不了」「有技术壁垒」 | 作者原话：「**这不是护城河**。没有技术壁垒，竞品抄一遍排序器就能有。」描述里没有一个字暗示别人做不出来 |
| 「智能推荐是首创」 | 作者原话：「**『推荐』本身不新**，CyberChef 的 Magic 早就在做。差别在**可信度**：Magic 给操作名，这里给理由 + 事先验证过。这是个程度差别，不是有无差别。」所以只写「排出下一步能做什么」，不写「首创」「独家」 |
| 把「菜单栏常驻 + 剪贴板取数」当卖点 | `AGENTS.md` 1.1 节写明竞品 DevDash 已经做了这一条，而且「如果只是把 20 个工具摁进一个菜单栏弹窗里，这个 App 没有存在的理由」 |
| 把兜底路径说成有差异 | 作者原话：「认不出来的东西退回『常用工具』兜底排序，这时候它退化成一个普通的工具抽屉，**兜底路径就是竞品的水平**，不要美化。」描述里专门留了一节「它认不出来的时候会怎样」，如实写它这时会退化成普通工具抽屉 |

### 作者标注「没有验证」的（不要当成已经好了）

以下几条来自 `AGENTS.md` 第 7 节，写文案时都不要拿来当卖点：

- **全局快捷键的端到端**：Carbon 注册成功了（没有冲突回报），但「按快捷键面板真的弹出来」这一步没有用真实按键测过。
- **签名与公证**：目前只有本地 debug 构建，没有 Developer ID 签名、没有公证。
- **多显示器 / 多 Space**：代码按鼠标所在屏幕定位，但没有在真实多屏环境验证过。
- **大输入的性能**：64 KB 以上跳过试探执行有断言保证，但「粘 10 MB 文本时卡不卡」只是设计上关了自动替换和拼写检查，没实测。

所以描述里没有出现「大文件也流畅」「多屏无问题」「一键即弹」这类话。
