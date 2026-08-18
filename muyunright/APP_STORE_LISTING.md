# 牧云右键助手 (MuyunRight) — App Store 发布素材

> 直接复制粘贴到 **App Store Connect → App 信息 / 版本信息** 对应字段。
> 中英双语版本独立提交（简体中文 + English (U.S.) 各填一份）。
> 每个字段已标注 App Store Connect 的**真实字符上限**，文案均在限内。

---

## 0️⃣ 创建 App Record（必填，按此填写，勿改）

App Store 的 **App Name 全店唯一**。本类目里「右键大师 / 超级右键 / 超级增强右键」均已被占用，加后缀也会撞车。

在 App Store Connect → **我的 App → + → 新建 App** 时，**必须**填：

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **macOS** | iOS |
| 名称（主语言：简体中文） | **牧云右键助手** | 右键大师、超级增强右键、超级右键、任何带「大师/超级右键」的变体 |
| 名称（English 本地化，创建后添加） | **MuyunRight** | SuperRight、Right Master、iRight |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.MuyunRight`（全新，2026-08-18 起） | 旧的 `...SuperRight` 已弃用 |
| SKU | `muyunright-20260818` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备上的显示名（`CFBundleDisplayName` 与 `CFBundleName`）为「牧云右键助手」，与商店中文名一致。菜单栏应用名、Dock、启动台、活动监视器都走这两项；工程内部仍用 `MuyunRight` 作为 Bundle ID / 产物文件名。

> **2026-08-18 起工程已整体改名为 MuyunRight**，Bundle ID、App Group、SKU 全部换新，与历史 `SuperRight` 项目再无关联。这样做的目的是彻底排除「Bundle ID 或 SKU 已被占用」这一类冲突（详见文末的名称冲突章节）。Xcode 自动签名会在首次构建时创建对应的 App ID 与 App Group，无需手工到开发者后台配置。

---

## 1️⃣ 推广文本 (Promotional Text)

> **上限 170 字符**，可在不提交新版本的情况下随时修改。

### 🇨🇳 简体中文（版本 v1.0 首发）

```
首发：访达右键新建文件/文件夹、拷贝路径、在终端打开、移动到常用文件夹。菜单栏静默后台，原生 SwiftUI，零联网零追踪。
```
**字符数：62 / 170 ✅**

### 🇺🇸 English (v1.0 launch)

```
New file/folder, copy path, open in Terminal, move/copy to favorites — right in Finder. Menu-bar quiet mode. Native SwiftUI, zero network, zero tracking.
```
**字符数：148 / 170 ✅**

---

## 2️⃣ 描述 (Description)

> **上限 4000 字符**。修改需提交新版本审核。

### 🇨🇳 简体中文

```
牧云右键助手为 Mac 访达补上最常用的右键功能，使用 SwiftUI 原生构建。它把「快、稳、隐私」放在第一位：完全本地运行，不发起任何网络请求。

【右键新建文件】
- 在任意文件夹右键即可新建文件，告别「先开 App 再另存为」
- 内置 11 种模板：文本、Markdown、RTF、HTML、JSON、YAML、Shell、Python、JavaScript、CSS、CSV
- 支持自定义模板：名称、扩展名、初始内容随心配置
- 模板内容支持 {{name}}、{{date}} 等占位符，新建时自动填好标题与日期
- 可开启「新建前询问名称」，直接起名，省去再次重命名
- 模板可开关、可排序，右键菜单只显示你需要的

【路径与终端】
- 拷贝路径 / 拷贝文件名：多选批量拷贝，一行一个
- 拷贝终端路径：自动转义，可直接粘贴到命令行
- 拷贝 file 链接：粘进备忘录或文档即可点开
- 在终端中打开：支持系统终端、iTerm2、Warp、Ghostty、kitty、Alacritty

【移动 / 拷贝到常用文件夹】
- 在主 App 配置常用目标文件夹，右键一键归档
- 自动记住最近去过的位置，整理一批文件时越用越顺手
- 子菜单末尾提供「其他位置...」临时选择

【用指定应用打开】
- 把常用编辑器（如 VS Code、Sublime Text）加入右键菜单
- 选中文件右键，即可「用 XXX 打开」，一键直达

【灵活可配置，静默后台】
- 每个菜单项可独立开关
- 可选收纳进子菜单（名称可自定义），或平铺在右键菜单第一级
- 设置页内置实时菜单预览，改完立刻知道访达里长什么样
- 访达工具栏按钮：不右键也能触达全部功能
- 默认菜单栏静默后台运行，关窗驻留，支持开机自启；Dock 与菜单栏图标都可按需隐藏
- 设置可导出为文件，换机或重装后一键导入

【安全与隐私】
- 不发起任何网络请求，断网可用全部功能
- 零追踪、零分析 SDK、零广告、零账号
- App Sandbox + Hardened Runtime，仅访问你显式授权的文件夹
- 首次在某个文件夹新建、移动、拷贝时经系统面板授权一次，之后不再询问；可在「权限管理」撤销
- 所有配置仅保存在本机

【适合谁】
- 每天在访达中整理文件、频繁新建文档的办公人群
- 需要快速拷贝路径、跳转终端的开发者
- 看重隐私、不希望工具类 App 联网的用户

系统要求：macOS 15.6 或更高版本。
如有建议或问题，欢迎通过「App 支持」链接反馈，每一条意见都会被认真对待。
```
**字符数：约 820 / 4000 ✅**（已去掉装饰线、星号、弯引号等 App Store Connect 不支持的字符）

### 🇺🇸 English

```
MuyunRight adds the context-menu actions Finder always should have had, built natively with SwiftUI. Speed, stability, and privacy come first: everything runs locally, and the app makes zero network requests.

[New File, Right There]
- Create a file in any folder straight from the right-click menu. No more "open an app, then Save As"
- 11 built-in templates: Plain Text, Markdown, RTF, HTML, JSON, YAML, Shell, Python, JavaScript, CSS, CSV
- Custom templates: set your own name, extension, and starter content
- Placeholders like {{name}} and {{date}} fill in the title and date as the file is created
- Optionally ask for the file name up front, so nothing lands as Untitled
- Toggle and reorder templates so the menu shows only what you use

[Paths and Terminal]
- Copy Path / File Name: batch-copy multiple selected items, one per line
- Copy Terminal Path: shell-escaped paths ready to paste into a command line
- Copy file link: paste into notes or docs and click straight through
- Open in Terminal: Terminal, iTerm2, Warp, Ghostty, kitty, Alacritty

[Move / Copy to Favorites]
- Configure favorite destination folders in the app, then archive with one right-click
- Recently used destinations are remembered automatically, so filing a batch gets faster as you go
- "Other Location..." is always available at the bottom of the submenu

[Open With Your Apps]
- Add your favorite editors (VS Code, Sublime Text, and more) to the context menu
- Select files, right-click, Open with... and you are done

[Fully Configurable, Quiet Background]
- Every menu item can be toggled independently
- Group everything under a single submenu (rename it if you like), or lay items flat at the top level
- A live preview in Settings shows exactly what the Finder menu will look like
- Finder toolbar button gives one-click access to every action
- Runs quietly in the menu bar by default; stays after you close the window; optional launch at login; both the Dock and menu bar icons can be hidden
- Export your settings to a file and import them on another Mac

[Security and Privacy]
- Zero network requests, fully functional offline
- Zero tracking, zero analytics SDKs, zero ads, zero accounts
- App Sandbox + Hardened Runtime; only folders you explicitly authorize are accessible
- The first create / move / copy in a folder asks for one-time system authorization; revoke anytime in Permissions
- All settings stay on your Mac

[Who it is for]
- Office users who organize files and create documents in Finder all day
- Developers who constantly copy paths and jump into a terminal
- Privacy-conscious users who expect a utility to stay offline

Requires macOS 15.6 or later.
Suggestions or issues? Use the App Support link below. Every message gets read.
```
**字符数：约 2000 / 4000 ✅**（已去掉装饰线、星号、破折号等 App Store Connect 不支持的字符）

---

## 3️⃣ 关键词 (Keywords)

> **上限 100 字符**（含分隔符，中英分开计算）。
> ⚠️ 不要重复 App 名称、不要堆砌、不要出现竞品名（避免被拒）。

### 🇨🇳 简体中文（约 92 / 100 字符）

```
右键,新建文件,访达,右键菜单,拷贝路径,终端,效率,文件管理,模板,快捷,菜单,工具,扩展
```

### 🇺🇸 English (约 97 / 100 字符)

```
finder,menu,new,file,context,right,click,copy,path,terminal,template,extension,productivity
```

### 🔁 关键词选取依据
- **高搜索量**：`右键` / `新建文件` / `finder` / `new file`（品类核心词）
- **场景词**：`拷贝路径` / `终端` / `copy path` / `terminal`（开发者搜索习惯）
- **功能词**：`模板` / `右键菜单` / `context menu` / `extension`
- **避开**：不出现 "超级右键" / "iRightMouse" / "New File Menu" 等其他 App 名

---

## 4️⃣ 技术支持网址 (Support URL) — **必填**

> App Store 必填字段，缺失会拒审。需要是**真实可访问、含联系方式**的页面。

本目录的 `support.html` 已按此要求写好（App 说明 + 提交问题入口 + FAQ + 隐私政策链接），随 `zhipengge/apps` 仓库一起托管即可：

```
https://zhipengge.github.io/apps/muyunright/support.html
```

备用方案：直接填 Issues 地址 `https://github.com/zhipengge/apps/issues`（真实可访问，也满足审核要求）。

> 前置条件：在 GitHub 仓库 **Settings → Pages** 中把来源设为 `main` 分支根目录。启用后上面的链接才可访问，**提交审核前务必在浏览器里打开验证一次**。

---

## 5️⃣ 营销网址 (Marketing URL) — 可选

> 选填。不填也能上架，建议填一个提升专业度。

```
https://zhipengge.github.io/apps/muyunright/
```

---

## 6️⃣ 隐私政策网址 (Privacy Policy URL) — **必填**

> 本目录的 `privacy.html` 随 `zhipengge/apps` 仓库托管在 GitHub Pages 上。

```
https://zhipengge.github.io/apps/muyunright/privacy.html
```

### App 隐私「数据收集」问卷答案

App Store Connect → App 隐私 → 数据收集：选择 **"不收集数据 / Data Not Collected"**。
依据：无账号、无分析、无广告、无任何网络请求；文件仅在本机沙盒授权范围内操作。

---

## 📋 提交清单 — 上架前核对

```
[ ] 1. App 名称        中文「牧云右键助手」/ 英文「MuyunRight」（已定稿，见第 0 节）
[ ] 2. 副标题          见下方建议
[ ] 3. 推广文本        中文 57 / 英文 153  (≤170)
[ ] 4. 描述            中文 ~850 / 英文 ~2100  (≤4000)
[ ] 5. 关键词          中文 ~92 / 英文 ~97  (≤100)
[ ] 6. 支持 URL        必填，替换占位
[ ] 7. 营销 URL        建议填，替换占位
[ ] 8. 隐私政策 URL    托管 privacy.html 后填入，必填
[ ] 9. App 隐私问卷    选 "不收集数据"
[ ] 10. App 类别       主类别：工具 (Utilities) / 次类别：效率 (Productivity)
[ ] 11. 内容评级       4+（无暴力/色情/赌博/医药）
[ ] 12. 出口合规       已在 pbxproj 配置 ITSAppUsesNonExemptEncryption = NO（见 EXPORT_COMPLIANCE.md）
[ ] 13. 截图           macOS 需 1280×800 / 1440×900 / 2560×1600 / 2880×1800 之一，3-10 张
```

### ⚠️ 名称冲突处理（2026-08 实测，已闭环）

先后以以下名称创建 App Record **全部失败**（`The App Name you entered is already being used`）：

| 尝试过的商店名 | 结果 | 原因 |
|---|---|---|
| 右键大师 | 失败 | 已被占用 |
| 右键大师 - 访达右键菜单增强 | 失败 | 基名仍被占用 / 过于近似 |
| 超级增强右键 | 失败 | 与在架「超级右键」「iRight 超级右键」等通称冲突 |
| 牧云右键 | 失败 | 报「name already in use」，商店检索不到 → 应为他人预留未上架 |
| 牧云右键助手 | 失败 | 同上报错。连撞两个自造名，转而怀疑报错文案误导（见下方诊断） |

本类目通称（右键大师、超级右键、右键助手、右键菜单增强）几乎全部被占。**加描述后缀不能绕过唯一性校验。**

⚠️ 冲突池包含**他人已预留但从未上架**的名称（预留有效期约一年），因此「在 App Store 搜不到」不代表可用，只能以创建 Record 时的报错为准。

### ⚠️ 这条报错不一定真的是名称问题

> App Record Creation failed due to request containing an attribute already in use.
> The App Name you entered is already being used.

第一句才是准确的：**某个属性**已被占用。第二句关于 App Name 的说法是 App Store Connect 的猜测性提示——**SKU 重复**（SKU 在账号内唯一、创建后不可改）或 **Bundle ID 已被其他 Record 占用**时，会弹出完全相同的这段文案。

**已采取的对策（2026-08-18）：把三个可能冲突的属性一次性全换新**

| 字段 | 当前值 | 说明 |
|---|---|---|
| 平台 | macOS | — |
| 名称 | `牧云右键助手` | 首选，若仍报占用见下方备选 |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.MuyunRight` | **全新**，从未提交过 |
| SKU | `muyunright-20260818` | **全新**，从未提交过 |
| 用户访问权限 | 完全访问 | — |

Bundle ID 与 SKU 都是全新值，**这两条已不可能是冲突源**。因此这次创建的结果可以直接定性：

- **创建成功** → 之前反复失败的根源就是旧的 Bundle ID / SKU，与名称无关。
- **仍然失败** → 冲突确实在「牧云右键助手」这个名称本身，换下方备选即可。

若名称仍报占用，按此顺序继续试。**不要**回到本类目的通称（右键大师、超级右键、右键助手、右键菜单增强，几乎全被占用），也**不要**在名称中使用「访达 / Finder」（Apple 商标，审核阶段易被拒）：

1. `牧云右键增强`
2. `牧云快捷右键`
3. `牧云右键工具箱`
4. `MuyunRight 牧云右键`
5. `MuyunRight`（把主语言改成 English 再创建，中文本地化后补）

**商店名与设备显示名可以不同。** 工程里的 `CFBundleDisplayName`（Dock、右键菜单、关于页）保持「牧云右键助手」即可，不必跟着商店名改。名称在**提交审核前可随时修改**——若急于推进证书 / TestFlight，先用任一能过的名字建好 Record，之后再改回首选。

### 副标题建议（30 字符内，显示在 App 名下方）

🇨🇳 中文：`访达右键新建文件 · 拷贝路径 · 开终端` （18 字符）
🇺🇸 English：`New file & more in Finder` （25 字符）

---

## 💡 截图建议（也是审核常拒原因）

需要展示 App **真实功能**，不能纯文字大字宣传。建议：

1. **右键菜单全貌** — 访达中右键展开「牧云右键助手」子菜单，展示新建文件模板列表
2. **新建文件效果** — 桌面右键新建 Markdown，配合刚生成的「未命名.md」文件
3. **主 App 概览页** — 扩展已启用的绿色状态 + 功能一览
4. **模板管理** — 「新建文件模板」页面，展示开关与自定义模板
5. **终端选择** — 「菜单设置」中的终端 Picker（Terminal / iTerm2 等）
6. **打开方式** — 添加了 VS Code 后的「用 Visual Studio Code 打开」菜单项

---

> ⚠️ **首次上架重要提醒**
>
> 1. FinderSync 扩展类 App 审核重点是**功能可发现性**：审核备注（App Review Information → Notes）里写明启用路径 **"系统设置 → 通用 → 登录项与扩展 → 文件提供程序 → 打开牧云右键助手"**，并说明主 App 首页有引导按钮，可显著降低"功能无法使用"式拒审。
> 2. 说明文件夹授权机制：**"新建文件需用户通过系统 NSOpenPanel 逐文件夹授权，符合沙盒规范，无完全磁盘访问；桌面/文稿/下载等文件夹的用途说明（NS*UsageDescription）已在 Info.plist 声明；App 内提供权限管理页面，可查看与撤销授权"**。
> 3. 描述里**不要**出现其他 App 名称（超级右键等），会被拒。
> 4. 描述/关键词不要用"无限"、"最强"、"最好"等绝对化表述。
> 5. App 完全无联网，App 隐私问卷务必选"不收集数据"，与描述保持一致。
