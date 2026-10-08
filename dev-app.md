# 苹果 App 开发要点

给每一个新 App 用的标杆。代码怎么写、测什么、文档放哪、上架会卡在哪，按这份走。

具体产品的文案、隐私政策、截图放在本仓库对应子目录（如 `muyunright/`、`muyunimage/`）。**本文件只写跨项目都成立的规则。**

覆盖 iOS / iPadOS / macOS 三类。tvOS、watchOS 目前没有在架产品，遇到再补。

---

## 0. 仓库布局

| 位置 | 放什么 | 不放什么 |
|---|---|---|
| `m3_apps/<App名>/` | Xcode 工程、源码、`AGENTS.md`、开发用 `README.md`、逻辑测试 | 面向用户的隐私政策、商店文案 |
| `m3_apps/apps/<app名>/` | 隐私政策、支持页、商店文案、截图、出口合规说明 | 源码 |

`apps` 公开发到 GitHub Pages（`https://zhipengge.github.io/apps/<app名>/`）。App Store 必填的 **隐私政策 URL**、**技术支持 URL** 就指这里的 `privacy.html`、`support.html`。

**源码仓库一律私有，且只推 GitHub。** 不再分 gitlab / github 两套，不再维护"门面仓库"。历史遗留的 `github/` 目录按第 0.1 节处理。

改功能时两处都要动：代码仓库改行为，`apps/<app名>/` 改用户能看见的说法。

每个产品在 `apps/<app名>/` 里至少准备这些文件：

```
apps/<app名>/
├── README.md              用户说明书 + FAQ（中英可同页）
├── PRIVACY.md             隐私政策源稿（中英）
├── privacy.html           上架用的隐私政策页
├── support.html           上架用的支持页
├── APP_STORE_LISTING.md   商店文案（可直接粘贴）
├── EXPORT_COMPLIANCE.md   出口合规为什么填 YES/NO
└── screenshots/           商店截图（见第 7 节）
```

### 0.1 旧 `github/` + `gitlab/` 拆分的处理

历史上 afu、gwave、record、SpinCourt 把它们拆成 `github/<App>/`（文档）和 `gitlab/<App>/`（源码）两套仓库。**一律合并**：源码进私有仓库，文档进 `apps/<app名>/`。

合并前必须确认一件事：**`github/` 侧有没有被已发布的 App 在运行时拉取的文件**。

- **afu 有。** `github.com/zhipengge/afu` 是线上配置服务，App 运行时从
  `https://raw.githubusercontent.com/zhipengge/afu/master/models.json` 拉模型清单，
  清单里的 `logoURL` 也指向同仓库的 `logos/*.png`。
  **这个公开仓库不能删**，它是发布物的一部分，不是文档目录。
  改法：源码移入私有仓库；`models.json` 和 `logos/` 留在原公开仓库，或者搬到 `apps/afu/`（同样是公开 Pages 源），
  然后**发版改 App 里的 URL**。迁移期间两个地址都要能访问。
- **其余三个没有**，`github/` 侧只有 README 和隐私政策，直接并入 `apps/<app名>/`。

判断方法：在源码里全局搜 `raw.githubusercontent.com` 和 `github.io`。搜得到就是运行时依赖。

---

## 1. 命名与标识符

### 1.1 开工前先定死的三个值

这三个值创建后很难改，**开工第一天就定，而且三者都要全新**：

| 字段 | 规则 | 反例 |
|---|---|---|
| **Bundle ID** | `com.gezhipeng0201.<PascalCase产品名>`，从未在 App Store Connect 建过 Record | 复用旧项目的 ID |
| **SKU** | 账号内永久唯一、创建后不可改。建议 `<小写产品名>-YYYYMMDD` | 用过一次的 SKU |
| **商店名** | 全店唯一。类目通称（「右键大师」「超级右键」这类）基本都被占 | 在通称后面加后缀指望绕过 |

已有产品里 `com.gezhipeng0201.afu` 是**小写**，与其余产品的 PascalCase 不一致。不要把它当范例；新 App 一律 PascalCase。

**商店搜不到 ≠ 名称可用。** 别人预留未上架的名字也会占一年左右。唯一判据是 App Store Connect 点「创建」时的报错。

`attribute already in use` / `The App Name you entered is already being used` 经常**误报成店名冲突**。真正被占的也可能是 SKU 或 Bundle ID。排查顺序：换全新 SKU → 换全新 Bundle ID → 最后才换店名。

设备显示名（`CFBundleDisplayName`，主屏 / Dock / 菜单 / 关于页）和商店名可以不同。急着建 Record 时可以先用能过的店名，审核前提交页里再改回首选。

**不要**在商店名、副标题、关键词里用「访达 / Finder / Mac / macOS / iPhone / iPad / iOS」——Apple 商标。Guideline 5.2.5 会按「容易让用户以为是 Apple 产品」拒。描述里写系统要求（如 Requires macOS 15.6）可以，副标题写 `for Mac` / `访达右键` 不行。

### 1.2 带扩展 / App Group 时的五处同步

带扩展、App Group 时，下面五处必须同步，漏一处的表现是「扩展读不到主 App 写的配置」——**没有任何报错**：

1. 主 App Bundle ID（pbxproj + `SharedConstants`）
2. 扩展 Bundle ID（挂在主 App 之下：`<主ID>.<扩展名>`）
3. App Group（macOS 强制 `<TeamID>.<主 App Bundle ID>`）
4. 配置存储 key
5. 其它跨进程 key（书签、心跳等）

主 App 与扩展的 entitlements、`SharedConstants.swift`、pbxproj 改完必须有测试守住一致性。

### 1.3 存储 key 前缀

UserDefaults / 文件名的前缀一律 `<小写app名>.`，互不碰撞。同一 App 内不同用途用不同 key，**不要塞进同一个 JSON**（第 3 节会再讲一遍为什么）。

---

## 2. 版本号

### 2.1 两个字段

| 字段 | Xcode 设置名 | 作用 | 改它会发生什么 |
|---|---|---|---|
| 版本号 | `MARKETING_VERSION` | 商店和用户看到的 `1.2.0` | 提交新版本必须比在架版本大 |
| 构建号 | `CURRENT_PROJECT_VERSION` | 同一个版本号下的第几次上传 | 同一版本号内必须递增；重复会被拒 |

**每一次 Archive 上传，`CURRENT_PROJECT_VERSION` 必须比上次大 1**，即使没改任何东西。只改 `MARKETING_VERSION` 不改构建号，第二次上传会被 I/O 拒掉。

### 2.2 版本号怎么涨

`MARKETING_VERSION` 用三段 `主.次.修`：

| 场景 | 涨哪一段 | 例子 |
|---|---|---|
| 改 bug、改文案、调 UI | 修订段 | `1.2.0` → `1.2.1` |
| 加功能、加界面，不改已有行为 | 次段，修订归零 | `1.2.1` → `1.3.0` |
| 改数据格式、改标识符、不向后兼容 | 主段 | `1.3.0` → `2.0.0` |

首次上架用 `1.0` 或 `1.0.0`。

**改数据格式（例如本地 JSON 加字段、改枚举）时必须同时写迁移**，并在主段涨价——否则老用户升级后会丢数据。迁移逻辑要有测试覆盖「旧 JSON 缺字段仍能解码」。

### 2.3 现状与待办

各 App 当前值（截至 2026-10-08）：

| App | MARKETING_VERSION | CURRENT_PROJECT_VERSION | 备注 |
|---|---|---|---|
| BabyRecord | 1.0 | 1 | 未上架 |
| JiKe | 1.0.2 | 3 | 走公证 + Releases，不受商店规则约束 |
| MuyunImage | 1.0 | 3 | |
| MuyunRight | 1.0 | 4 | |
| MuyunTV | 1.0 | 1 | |
| OpenTerminal | 1.0 | 2 | |
| Speed | 1.0 | 1 | |
| WeEdit | 1.0 | 1 | |
| afu | 1.0 | 1 | |
| gwave | 1.3 | 1 | |
| record | 1.1 | 1 | |
| SpinCourt | 1.0 | 1 | |

构建号在不同 App 之间**不需要**对齐，各涨各的。

### 2.4 最低系统版本

**不要填成当前 Xcode 的版本号。** 填当前值等于只支持刚出的系统，用户量会小一个数量级。

规则：
- 按**实际用到的最新 API** 定。用了 iOS 17 的 `@Observable` 才填 17.0，没用就别填。
- 小版本只写 `.0`。填 `17.3` 没有意义（`17.0` 的设备也能装）。
- **补丁版本号不要出现在最低系统里。** 填 `26.2` 会让 26.0 和 26.1 的用户都装不上——这几乎不会是本意。

当前**需要修**的三个（见第 11 节待办）：

| App | 现值 | 问题 |
|---|---|---|
| afu | iOS 26.2 | 补丁号入最低系统；且用了 `@Observable`/SwiftData，实际 17.0 够 |
| MuyunImage | 项目级 26.2 / target 级 15.6 | 项目级那个是 Xcode 默认值残留，容易被误改。统一到 15.6 |
| Speed | iOS 26.2 | 同上，应按实际 API 降到 17.0 一档 |

---

## 3. 工程与沙盒

- 默认走 **App Sandbox + Hardened Runtime**。能逐文件夹授权就不要申请完全磁盘访问。
- 访问桌面 / 文稿 / 下载 / 外置磁盘 / 网络宗卷，主 App **和真正落盘的扩展** 都要写 `NS*FolderUsageDescription`，文案写真实用途，不要只写「新建文件」。
- `GENERATE_INFOPLIST_FILE = YES` 时，用 `INFOPLIST_KEY_某Key = 值` 往 Info.plist 里合并。改完构建产物用 `plutil -p` 核对，不要只看 pbxproj——增量构建有时不重跑 `ProcessInfoPlistFile`。
- 扩展是独立 bundle。Xcode 模板里有的键（尤其 **`LSUIElement = YES`**）自定义 plist 时容易漏。App Store 校验报 `Missing Info.plist value. A value for the key 'LSUIElement'` 就是这个。访达扩展是后台进程，必须声明自己不进 Dock。
- `Shared/` 被多个 target 编译时，里面不能出现只有主 App 才有的依赖（SwiftUI 等）。
- 配置若被主 App 整份覆盖、扩展又要写另一份数据，**不要塞进同一个 JSON key**，否则后写的一方会抹掉另一方。
- **`xcuserdata/` 永远不进版本库。** 它含每台机器不同的 scheme 状态。每个仓库都要有 `.gitignore` 挡住它。

### 3.1 沙盒授权（写入 vs 打开）

不可重复的操作（拷贝、移动、新建）必须：**先用只读探针确认权限 → 缺了再弹系统面板 → 拿齐之后业务闭包只跑一次**。不要「先做一遍、失败再授权重试」，否则用户会得到两份文件。

幂等操作（用某应用打开、在终端打开）可以反过来：先直接做，失败再申请授权。访达传来的 URL 常常已经带授权，能少弹一次窗。

### 3.2 访达扩展额外注意

- 改完扩展必须 `killall Finder`，否则加载的是旧代码。
- `xcodebuild` 会把产物注册进 LaunchServices。`/Applications` 和 DerivedData 各有一份时，右键菜单每项出现两次。日常只保留一份。
- `FIFinderSyncController.isExtensionEnabled` 在 macOS 15/26 上经常一直是 `false`，不能当唯一真相。扩展被访达加载后往 App Group 写心跳，主 App 用心跳判断更稳。
- 「去启用」不要只调 `showExtensionManagementInterface()`，新系统上经常空白。开关实际在：**系统设置 → 通用 → 登录项与扩展 → 文件提供程序（ⓘ）**。不要把用户领到名叫「Finder」的那一项（那是快捷操作）。
- 跨进程菜单项只能靠 `title` 和 `tag`。用索引传参时，动作里要用标题做二次校验。
- 根菜单项要有图标，用 App Logo 缩到 16×16，不要用过大的 SF Symbol（访达会给带子菜单的项多留空隙）。

### 3.3 未沙盒的 macOS App（终端类）

终端、包管理器这类要跑用户登录 Shell、读写任意目录的 App，**不能开沙盒**——开了 PTY 几乎不可用。系统「终端」和 iTerm 同样不沙盒。

代价是 **Mac App Store 基本过不了**，分发走 **Developer ID 签名 + 公证 + GitHub Releases**。JiKe 就是这个模式：`ENABLE_APP_SANDBOX = NO`，Hardened Runtime 保持开启，打包用 `Scripts/release.sh`。

不要为了上架去「修」沙盒。选定了分发方式就不要再改。

### 3.4 依赖

- 能用系统框架就用系统框架。12 个产品里 9 个零第三方依赖，这是好事，保持住。
- 引入 SPM 依赖前先问：**它会不会在下一个大版本破坏 API**。终端类（JiKe 用 SwiftTerm）要**钉死次版本**，写法 `upToNextMinorVersion`，不要用 `upToNextMajorVersion`。
- **不要留孤儿依赖。** MuyunImage 的 `Package.resolved` 里 pin 了 `ml-stable-diffusion` 和 `swift-argument-parser`，但 pbxproj 的 `packageProductDependencies` 是空的、源码里 0 处引用。这种残留会让人误以为有这功能，也会拖慢解析。删干净。

### 3.5 构建产物

`DerivedData/`、`dist/`、`build/`、`.release-derived/` 一律进 `.gitignore`。

- JiKe 的本地 `DerivedData/` 238M + `.release-derived/` 379M + `dist/` 41M = 658M，占该目录 99%，全是可重建的。
- `dist/` 里的发布物（`.app`/`.dmg`/`.zip`）在**确认 Release 已上传**后可以删。
- 不要在仓库里提交构建产物。要发行就发 GitHub Releases。

---

## 4. 合规

### 4.1 出口合规（每次上传都会问）

在**每一个 native target**（主 App、每个 appex）的 Debug / Release 都加：

```
INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO;
```

漏掉扩展 target，上传后仍会卡在「缺少出口合规证明」。

填 `NO` 的条件（满足任一即可）：

1. App 完全没有加密；或
2. 加密仅用于认证 / 签名 / DRM / 走苹果系统或标准 HTTPS/TLS，没有自研算法。

纯本地、零网络的工具走条件 1。只用系统 HTTPS 的 App 走条件 2。理由写进 `EXPORT_COMPLIANCE.md`，审核或自己半年后都看得懂。

### 4.2 隐私问卷（App Store Connect → App 隐私）

零追踪、无账号、无后端的工具类：**不收集数据**。和 `PRIVACY.md` / `privacy.html` 必须一致，不能商店页写「不收集」、问卷里勾了联系人。

隐私政策要写清：处理什么、存在哪、不做什么、用户怎么删。本机沙盒容器、安全书签、剪贴板都算「处理」，即使不上网。新增会持久化的字段（例如「最近位置」）要同步进隐私政策。

**有 AI / 有网络的 App 要额外写清：** 数据是否离开设备、发给谁、存多久。项目的两个 AI 产品各有各的写法：

- **afu**（端侧大模型）：模型权重从 HuggingFace 下载到本机，推理全在设备上跑，对话内容不出设备。隐私政策要写到「模型下载会连接 huggingface.co，仅传输模型文件，不含你的对话」。
- **MuyunImage**（CoreML 消除）：模型从第三方 GitHub Release 下载，图片处理全在本机。要写「图片不会上传」。

### 4.3 权限最小化

主 App 里用一页把「我们申请的」和「我们不申请的」摊开。不申请的写出来（完全磁盘访问、网络、通讯录、位置、麦克风、摄像头、自动化）对审核和用户都有用。

### 4.4 协议

分发前先打开并签署：

- [App Store Connect 协议](https://appstoreconnect.apple.com/agreements/)（Free Apps / Paid Apps）
- [Apple Developer 协议](https://developer.apple.com/account)

未签署时，Xcode 报错会非常含糊（见第 10.3 节）。

---

## 5. 测试

分两层，不能互相替代。

### 5.1 逻辑测试（每次改 Shared / 纯函数都跑）

**统一约定：不用 Xcode Test target，用 `swiftc` 把 `Shared/` 和测试文件编成可执行文件。** 几秒出结果，不依赖 XCTest、不启动 UI。

这条约定目前 9 个产品都遵守，但 **Speed 断了**：`Tests/LogicTests.swift`（47 个断言）已提交进 git，却既不在 pbxproj 里、也没有任何脚本能跑它。改 Speed 前先补一个 runner。

至少覆盖：

- 命名去重、路径判断、配置向前兼容（旧 JSON 缺字段仍能解码）
- 标识符一致性（App Group 前缀、扩展 ID 挂在主 ID 下、存储 key 互不冲突）
- 列表增删改不会「删了又被默认值填回」
- 菜单结构 / 可见性（如果菜单有蓝图）

`ConfigStore.load()` **不要**在读取时给用户主动清空的列表补默认值。默认值只在「从未保存过配置」时由模型初始值带出；恢复默认用设置页的按钮。

### 5.2 手工清单（改扩展、沙盒、系统交互后必做）

逻辑测试覆盖不了授权面板、右键菜单、焦点、重复注册。每条写成「操作 → 期望」，改完扩展后 `killall Finder` 再过一遍。

最低要包含：首次授权后业务只执行一次、点取消无副作用、主 App 改配置后面板立刻反映、空白处与选中项的作用对象一致。

Mac 端清单写在各自 `MANUAL_TEST.md` 或 `README.md`。MuyunRight 的 13 条是范例；**它目前一条都没跑过**，是欠账。

---

## 6. 商店文案

写在 `apps/<app名>/APP_STORE_LISTING.md`，中英各一份，**标注字数**。模板见 `apps/muyuntv/APP_STORE_LISTING.md`。

### 6.1 字段与上限

| 字段 | 上限 | 备注 |
|---|---|---|
| 名称 | 30 | 全店唯一 |
| 副标题 | 30 | 名称下方那行。**不要写 Apple 产品名** |
| 推广文本 | 170 | 不提交新版本也能改。适合写「本期更新」 |
| 描述 | 4000 | 改了要随版本审 |
| 关键词 | 100 | 含逗号；不要重复 App 名、不要竞品名 |
| 技术支持 URL | 必填 | `support.html` |
| 隐私政策 URL | 必填 | `privacy.html` |
| 营销 URL | 可选 | 产品 README 页 |

类别、内容评级、截图、审核备注也写进同一份清单，避免提交时现想。

### 6.2 描述里禁止的字符

App Store Connect 会报「存在不支持的字符」。**不要用**：

- 装饰线 `━─═`
- 星标 `✦★☆`
- 圆点列表 `•`
- 弯引号 `“”`（用「」或直引号 `"`）
- 箭头 `→`、省略号 `…`、间隔号 `·`、破折号 `—`
- 序号 emoji（`1️⃣` 这类只放在文档标题里可以，**不要进描述正文**）
- `file://` 这类带 `://` 的字面量（写成「file 链接」）

分段用【小标题】或 `[Section]`，列表用 `- `。改完在纯文本框里粘贴，不要从富文本编辑器带格式过来。

**自查命令**（提交前跑一次）：

```bash
# 把描述正文抽出来查违禁字符，命中就打印行号
grep -nE '[━─═✦★☆•“”…·—→]|://' 描述.txt
```

### 6.3 描述怎么写

- **第一段说清「这是什么 + 不做什么」。** 工具类产品尤其要把免责说在前面（如 MuyunTV 的「本应用不提供、不托管任何电视节目」），这既是审核需要，也省得用户误解。
- 功能分段用【小标题】，每段 3-6 条 `- ` 列表项。
- **用户能看见的行为都要写。** 改了功能不同步文案，审核看了会认为描述与实际不符。
- 英文版不是逐字翻译，按英文习惯重写，但功能点必须一一对应。

### 6.4 关键词怎么写

- 逗号分隔，**不要空格**（空格算字符还浪费额度）。
- **不要重复 App 名里的词**——名称和副标题已经参与搜索了。
- **不要写竞品名**（Guideline 5.2.1 会拒）。
- 不要写 Apple 产品名。
- 中英各一份，英文那份写英文用户的搜索习惯（`live,player,playlist` 而不是中文词的拼音）。
- 填不满 100 字符没关系，**堆砌无关词反而降低相关性**。

---

## 7. 截图

### 7.1 尺寸要求

**必须按当前要求的尺寸，不要用旧的。** 已有的产品里 `muyuntv/APP_STORE_LISTING.md` 还写着「iPhone 6.7 寸和 iPad 12.9 寸」，那是旧规格，按下面改。

| 平台 | 尺寸 | 像素 | 说明 |
|---|---|---|---|
| iPhone | 6.9 寸 | **1320 × 2868** | 必填 |
| iPhone | 6.7 寸 | 1290 × 2796 | 可替代 6.9 寸 |
| iPad | 13 寸 | **2064 × 2752** | iPad 版必填 |
| iPad | 12.9 寸 | 2048 × 2732 | 可替代 13 寸 |
| macOS | 1280 × 800 | 也接受 1440×900 / 2560×1600 / 2880×1800 | 3-10 张 |

3-10 张。**iPhone 和 iPad 要分别提供**（`TARGETED_DEVICE_FAMILY = "1,2"` 的产品两套都要）。macOS 只提供一套。

比例不是目标比例时：**先居中裁切，再缩放，不要硬拉**。

```bash
sips -g pixelWidth -g pixelHeight screenshot.png       # 先看尺寸
sips --cropToHeightWidth <高> <宽> screenshot.png      # 裁成目标比例
sips -z <高> <宽> screenshot.png                       # 再缩到目标尺寸
```

### 7.2 内容要求

- **必须是真实 UI。** 截图中要有 App 实际运行的界面。Apple 会拒「纯营销海报」。
- 可以加**设备外框、背景、标题文字**——这是允许且推荐的。
- 不要放竞品界面、不要放 Apple 产品名、不要用未授权的素材。

### 7.3 每个产品至少覆盖的场景

按产品类型选，但要**让用户一眼看懂怎么用**：

| 产品类型 | 建议场景 |
|---|---|
| 工具体（MuyunRight、WeEdit、OpenTerminal） | 主界面 / 核心操作结果 / 设置 / 引导页 |
| 记录类（BabyRecord、record） | 空状态 / 记录中 / 统计图表 / 导出 |
| 播放类（MuyunTV、gwave、Speed） | 空状态引导导入 / 内容列表 / 播放或阅读页 / 设置 |
| AI 类（afu、MuyunImage） | 模型选择 / 对话或处理中 / 结果对比 / 隐私说明页 |
| 小工具（SpinCourt） | 输入 / 动画中 / 结果 / 关于 |

**空状态要谨慎**：可以用，但要有引导文案，别让截图看起来像坏了的 App。

### 7.4 存放

放 `apps/<app名>/screenshots/`，按平台分目录：

```
apps/<app名>/screenshots/
├── raw*/                 原始素材（模拟器抓的、真机截的），不进商店
├── iphone/  1320x2868    成品
├── ipad/    2064x2752
└── mac/     1280x800
```

文件名用 `<序号>-<场景>.png`（如 `01-import.png`），顺序即展示顺序。

### 7.5 生成流水线

截图不是手工做的，跑脚本：

```bash
cd apps
python3 tools/compose_all.py          # 全部重做
python3 tools/compose_all.py afu      # 只做某个
```

脚本读 `tools/compose_all.py` 里的 `JOBS` 表，把 `screenshots/raw*` 的素材加设备外框、渐变背景和标题，导出成品。改标题就改那张表。

**抓原始素材**：

- **iOS**：`_tools/ScreenshotDriver/` 是一个 XCUITest 驱动。改 `scripts/<app>.json` 里的点击步骤，然后
  `./run.sh scripts/<app>.json ["iPad Pro 13-inch (M5)"]`。
  它按可见文字或归一化坐标点击，不需要辅助功能权限。
- **macOS**：`_tools/capture_mac.sh <进程名> <输出.png>`。它先激活窗口再全屏截图裁切
  （`screencapture -l` 在本机权限下不可用）。

**两个必须知道的坑**：

1. **iOS 终端类 app 的软键盘去不掉。** OpenTerminal 用 `UIKeyInput` 抓输入，没有收起按钮，
   连 Escape 都会被当成字符送进终端。解法是 `_tools/strip_keyboard.py` 把键盘区域裁掉、
   用终端背景色补足到全高。
2. **macOS 沙盒 app 读不到外面放的文件。** 容器里的 `Pictures`/`Desktop` 等是符号链接，
   指向真实的家目录，沙盒会拒绝。要预置素材得放进 `Data/Documents/` 这类真实目录。
   MuyunImage 和 WeEdit 各留了一个 DEBUG-only 的截图钩子（环境变量触发），
   发布版不含这些代码。

**检查尺寸**（每次导出后都跑）：

```bash
python3 ~/.claude/skills/apple-app-screenshots/scripts/compose.py --verify <app>/screenshots
```

---

## 8. 隐私与支持页

- `privacy.html` / `support.html` 必须在浏览器里能打开（GitHub Pages：`main` 分支根目录）。提交前自己点一次 https 链接。
- **支持页写清**：如何启用扩展 / 授权、常见失败、怎么反馈（GitHub Issues 即可）。
- **审核备注里写启用路径**和「主 App 首页有引导按钮」，能减少「功能无法使用」式拒审。访达扩展类尤其重要。
- 隐私政策改动要同步 `PRIVACY.md` 和 `privacy.html` 两个文件，以及 App Store 问卷。

### 8.1 产品内帮助

除网页支持页外，App 内要有一个能自查的地方（「关于与隐私」或「帮助」页）：

- 当前版本号（从 `CFBundleShortVersionString` 读，不要硬编码）
- 隐私政策 / 支持页的入口
- 常见问题
- 权限现状（扩展是否启用、授权了哪些目录）

---

## 9. 上架流程

按这个顺序，不要对调：

1. **签协议**（第 4.4 节）。
2. **在网页创建 App Record**，不要指望 Xcode Distribute 代建。
   平台选对（macOS 不要勾成 iOS，反之亦然）。Bundle ID 必须与工程一字不差。账号角色至少 Admin / App Manager。
3. 浏览器打开隐私政策、支持页，确认 200。
4. Info.plist 核对：`ITSAppUsesNonExemptEncryption`（每个 target）、扩展的 `LSUIElement`、文件夹用途说明。
5. Archive → Validate / Distribute。
6. 填商店文案（用 `APP_STORE_LISTING.md` 那份已去掉违禁字符的）。
7. App 隐私问卷与隐私政策对齐。
8. 传截图（iPhone + iPad 两套），提交审核。

改了 Info.plist 或扩展配置必须 **Product → Archive 新建一份**。对旧 Archive 再点 Distribute，校验的还是旧包。

### 9.1 这次实战出现过的报错

| 报错 | 实际原因 | 处理 |
|---|---|---|
| `IDEDistribution.DistributionAppRecordProviderError error 0` | Connect 里还没有这条 App Record，或协议未签、账号没权限 | 先签协议，再在网页手工建 Record，然后用同一 Archive 重新分发 |
| `Error Downloading App Information` / `was previously removed from App Store Connect` | 这个 Bundle ID 的 App Record 被删过，还停在 Removed Apps | Connect → Apps → All Statuses 箭头 → Removed Apps → App 信息 → Restore App。恢复后再 Distribute。恢复不了就必须换全新 Bundle ID + SKU，旧 ID 作废 |
| `Missing Info.plist value. … 'LSUIElement' … .appex` | 自定义扩展 plist 没带模板默认键 | 扩展 Info.plist 加 `LSUIElement = YES`，**重新 Archive** |
| 描述存在不支持的字符 | 装饰线、✦、•、弯引号、`→`、`://` | 见第 6.2 节 |
| `attribute already in use` / 名称已被使用 | 不一定是店名；SKU、Bundle ID 同样会套这句 | 见第 1.1 节，三个属性都换新再定性 |
| 上传后「缺少出口合规证明」 | 只写了主 App，扩展 target 漏了 | 每个 native target 都加 `ITSAppUsesNonExemptEncryption` |
| Guideline 5.2.5 副标题含 Mac | 副标题写了 for Mac / 访达 / Finder | 副标题和关键词去掉所有 Apple 产品名，只写功能 |
| Guideline 4 关窗后打不开 | 关主窗口后「窗口」菜单没有重开项；菜单栏图标不算数 | 默认关窗即退出；若要驻留，Window 菜单和 ⌘0 必须在窗口关掉后仍在 |
| 同一个构建号传第二次被拒 | 只改了 `MARKETING_VERSION` 没涨 `CURRENT_PROJECT_VERSION` | 见第 2.1 节 |

---

## 10. 新 App 开工检查清单

**工程**

- [ ] Bundle ID / 扩展 ID / App Group / SKU 全部全新，五处同步
- [ ] Bundle ID 是 PascalCase，和已有产品风格一致
- [ ] `CFBundleDisplayName` 与界面文案一致
- [ ] 最低系统版本按实际 API 填，**不含补丁号**
- [ ] `.gitignore` 挡住 `xcuserdata/`、`DerivedData/`、`dist/`、`.DS_Store`
- [ ] Sandbox + Hardened Runtime；权限用途说明写在真正访问文件的那个 target
- [ ] 每个 target 都有 `ITSAppUsesNonExemptEncryption`
- [ ] 扩展有 `LSUIElement = YES`（构建产物 `plutil` 能看到，不是只在源文件里）
- [ ] 无孤儿 SPM 依赖
- [ ] 有逻辑测试；涉及系统 UI 的有手工清单
- [ ] `AGENTS.md` 只记硬约束和当前进度，细节进开发 README

**文档（`apps/<app名>/`）**

- [ ] `PRIVACY.md` + `privacy.html`（中英），和问卷一致
- [ ] `support.html` 可访问
- [ ] `APP_STORE_LISTING.md`：名称备选、推广/描述/关键词、字数、无违禁字符
- [ ] `EXPORT_COMPLIANCE.md`：为什么填 NO 或 YES
- [ ] 截图按第 7 节尺寸，iPhone + iPad（或 macOS）各 3-10 张真实界面
- [ ] GitHub Pages 已开，https 链接亲自点过

**上架**

- [ ] 协议已签
- [ ] App Record 已在网页创建成功
- [ ] `CURRENT_PROJECT_VERSION` 比上次大 1
- [ ] 新 Archive 校验通过后再填版本信息

---

## 11. 产品教训（通用）

这些不是合规条款，但是同类工具下次会再遇到：

- 用户清空的列表不要在 `load()` 时偷偷填回去。
- 菜单怎么展示、动作作用在谁身上，构建菜单时就要写死（空白处右键不要误用别处的选中项）。
- 系统 API 说「未启用」时，先看进程和心跳，再决定要不要把用户赶去设置页。
- 商店描述用最朴素的中文标点；好看的 Unicode 过不了校验。
- 面向用户的说明和审核备注，启用路径要写成用户在当前系统里真实看得到的那一页。
- **模型清单这类「可以免发版更新」的东西，放出去就是承诺。** afu 的 `models.json` 挂在公开仓库上，改它等于改已发布 App 的行为，要按发布物对待。
- **下载的模型要做完整性校验。** MuyunImage 从第三方 GitHub Release 拉 187MB 模型，用可变的 `build` tag，没有 SHA256——上游换包用户无从察觉。新增下载类资源一律带校验和，并钉死版本 tag。
