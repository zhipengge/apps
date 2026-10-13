# 文辑 (WeEdit) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。
> 副标题和关键词不要出现访达 / Finder / Mac / macOS。

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **macOS** | iOS |
| 名称（主语言：简体中文） | **文辑** | 备选：稿笺、文辑笔记 |
| 名称（English） | **WeEdit** | WeEdit Editor、文辑 WeEdit |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.WeEdit` | 任何旧 ID |
| SKU | `weedit-20260915` | 任何曾提交过的 SKU |
| 类别 | 效率 / Productivity | — |
| 价格 | 待定（用户决定） | — |

设备显示名（`INFOPLIST_KEY_CFBundleDisplayName`）为「文辑」。版本 `MARKETING_VERSION = 1.0`，build 1。

**命名红线：** 副标题、关键词、推广文本里不要出现访达、Finder、Mac、macOS、Apple 这类商标词。
中文描述里出现「电脑」「本机」是安全的，出现「Mac」不是。本文件已经按这条写过一遍。

**界面语言：** 工程里没有本地化资源，界面文案是中文硬编码。给 English 建商店本地化的话，
英文用户看到的是「英文描述 + 中文界面」。要么这轮只上简体中文，要么等界面英文化之后再说。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
一篇稿写给公众号、小红书、知乎、微博。每个平台吃什么格式、标题和正文的上限是多少，复制之前就标出来。稿子只存在这台电脑上。
```

**字符数：61 / 170**

### English

```
One draft for WeChat, Xiaohongshu, Zhihu and Weibo. What each editor accepts, and every title and body limit, is flagged before you copy. Drafts stay on this computer.
```

**字符数：167 / 170**（只剩 3，改写时留意）

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
文辑是一个本地图文编辑器。同一篇稿子，按公众号、小红书、知乎、微博各自的规则导出成可以粘贴的 HTML 或纯文本，你复制到对方的网页编辑器里粘贴。

【四个平台是四套独立实现】
- 公众号：内联样式，正文版心 677 像素，一级标题按二级样式出，表格转为带边框样式，支持正文并排图
- 小红书：标题 20 字、正文 1000 字、图片 18 张，不接受标题层级、表格、并排图和文字颜色，这些会降级并在提示里说明
- 知乎：标题 100 字、图片 40 张，保留标题层级和表格，一级标题转为二级，不支持内联文字颜色
- 微博：只吃纯文本，2000 字上限，表格转成文字，图片作为独立项放进剪贴板

不是同一个导出换个名字，是四个渲染器。

【上限在复制之前就提示】
标题超过 64 字或 20 字、图片超过 20 张、正文超过 2000 字，都会在你还看着编辑界面的时候标出来。
对方后台遇到超限通常是静默截断或者直接拒收，等发出去才发现就已经晚了一步。

【图片跟着文稿走】
插入的图片会复制进这篇稿自己的目录，导出时嵌进 HTML 一起带走。这一步是为平台拦外链图片准备的：粘到后台之后，由对方的编辑器把它上传成自己的图。

【写和存都在本机】
文稿与媒体存在沙盒容器里，一篇稿一个目录，正文是 JSON，图片放在旁边的 media 目录，整个目录拷走就能备份或换机器。没有账号，没有自建服务器，没有分析、追踪或广告 SDK。

【联网只有三处】
打开含远程图片的稿子时按图片原本的地址取图；点「复制并打开后台」时由系统浏览器打开平台创作页；在编辑器里点链接时交给系统打开。文辑不登录你的账号，也不代你发布。

【它不适合谁】
- 只发一个平台的人：没有第二个平台要适配，收益为零
- 稿件不从这儿来的人：不能导入 markdown 或 docx，也不能抓网址，稿子只能手打或从浏览器粘贴
- 需要严肃排版的人：编辑器是网页里的可编辑区域，字体、行距、分页、导出 PDF 都不如专业写作软件
- 想要一键发布的人：这些平台没有给第三方用的稳定发文接口，文辑省掉的是重新排版的时间

【系统要求】
需要 macOS 14.0 或更高版本。
```

**字符数：919 / 4000**

### English

```
WeEdit is a local rich-text editor. One draft is exported into pastable HTML or plain text for WeChat Official Accounts, Xiaohongshu, Zhihu and Weibo, and you paste it into that platform's own web editor.

[Four platforms, four real rule sets]
- WeChat Official Accounts: inline styles, a 677 pixel column, h1 rendered at h2 weight, tables restyled with borders, side-by-side images supported
- Xiaohongshu: 20 character titles, 1000 character body, 18 images; heading levels, tables, side-by-side rows and text colour are not accepted, so they are downgraded and reported
- Zhihu: 100 character titles, 40 images; heading levels and tables kept, h1 mapped to h2, inline text colour not supported
- Weibo: plain text only, 2000 character body, tables flattened, images placed on the pasteboard as separate items

These are four separate renderers, not one export under four names.

[Limits are reported before you copy]
A title past 64 or 20 characters, more than 20 images, or a body past 2000 characters is flagged while you are still looking at the editor. The other side usually truncates silently or rejects the paste outright, and you find out after publishing.

[Images travel with the draft]
An inserted image is copied into that draft's own folder and inlined into the exported HTML. This exists because platforms block hotlinked images: once pasted, their editor uploads it as its own.

[Writing and storage stay local]
Drafts and media live in the sandbox container, one folder per draft, body as JSON with images in a media folder beside it. Copy that folder and you have a backup or a move to another machine. No account, no backend of ours, no analytics, tracking or ad SDK.

[Three places touch the network]
Fetching a remote image already in a draft from its own address; handing the platform's compose page to your browser when you press copy and open; handing a link you click in the editor to the system. WeEdit never signs in to your accounts and never posts for you.

[Who this is not for]
- Anyone publishing to a single platform: there is no second format to adapt, so the gain is zero
- Anyone whose draft comes from elsewhere: no markdown or docx import and no URL capture, so text is typed here or pasted from a browser
- Anyone who needs serious typesetting: the editor is a web view's editable area, well short of a dedicated writing tool for fonts, line spacing, pagination or PDF export
- Anyone wanting one-click publishing: these platforms offer no stable third-party publishing API, so what WeEdit saves is reformatting time

[Requirements]
macOS 14.0 or later.
```

**字符数：2594 / 4000**

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
按平台规则复制的图文编辑器
```

**字符数：13 / 30**

### English

```
Platform-tuned draft copier
```

**字符数：27 / 30**（只剩 3，改写时留意）

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
公众号,小红书,知乎,微博,图文,排版,粘贴,编辑器,表格,并排图,笔记
```

**字符数：36 / 100**

### English

```
wechat,xiaohongshu,zhihu,weibo,editor,rich text,paste,article,table,draft,note
```

**字符数：78 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/weedit/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/weedit/privacy.html` |
| 营销 URL | `https://zhipengge.github.io/apps/weedit/` |

技术支持是**版本级**字段（改它要跟新版本一起提审），隐私政策是 **App 级**（要有待发版本才能改）。
这两个 URL 一旦提审就不好改了，提审前先确认目录名。

`apps/weedit/` 下有 `index.html`，所以营销 URL 可以填。**提交前用浏览器逐个打开确认 200**；
`apps/` 是独立仓库，weedit 目录没推上去之前这三个链接都是 404。

---

## 6. 类别、评级、隐私问卷

| 字段 | 建议 |
|---|---|
| 类别 | 效率 / Productivity |
| 年龄分级 | 4+。没有暴力、赌博、成人内容、用户生成内容或聊天 |
| 内购 | **无**。工程里没有 StoreKit 代码 |
| App 隐私 | **不收集数据**。不要勾联系人、位置、追踪、标识符 |
| 出口合规 | **NO**。`INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO` 已经写在工程里 |

隐私问卷与 `privacy.html`、`PRIVACY.md` 必须一致。有一处要留意：**文辑确实会联网**
（取文稿里的远程图片、打开平台创作页），这不等于「收集数据」——图片请求发向图片自己的站点，
文辑没有服务器可以接收任何东西。问卷里仍然选「不收集数据」。

**审核备注建议写明：** 本 App 是本地编辑器，没有账号系统与自建服务器，不收集任何数据。
联网仅用于显示文稿中已存在的远程图片，以及用户主动点按后由系统浏览器打开平台创作页。
不申请辅助功能、输入监控、完全磁盘访问等任何敏感权限。

---

## 7. 截图

成品在 `apps/weedit/screenshots/`：

| 目录 | 尺寸 | 数量 | 用途 |
|---|---|---|---|
| `screenshots/mac/` | 1280 x 800 | 3 | 直接上传，符合 macOS 商店规格 |
| `screenshots/raw/` | 2560 x 1640 | 3 | 原始截图，重新合成时用 |

| 文件 | 画面 |
|---|---|
| `01-editor.png` | 编辑器主体，平台切换与适配提示 |
| `02-table.png` | 表格与并排图在文稿里的样子 |
| `03-preview.png` | 右侧预览，粘贴后大致长什么样 |

macOS 的商店截图规格是 1280 x 800，这三张已经是这个尺寸，不需要再缩放。
重新生成走 `python3 _tools/make_store_shots.py`（截图脚本在 apps 仓库侧）。

---

## 8. 交付前必须补的（不是文案问题）

| 项 | 现状 | 影响 |
|---|---|---|
| **四个后台的真机粘贴回归** | **没做过**。格式与图片能不能顺利过，目前是按代码和 416 条逻辑测试推出来的 | 最需要在提审前补的一项。万一某个平台粘过去就乱，商店描述里所有「能带过去」的说法都要重写 |
| App 图标成品 | 工程里没有图标资源，图标是矢量绘制但成品未出 | 提审必须有的资源，没有会被直接挡下 |
| 隐私清单 `PrivacyInfo.xcprivacy` | 不存在。**按规则不需要**：全工程没有用到任何「需声明理由的 API」（没有 UserDefaults，也不读文件时间戳、磁盘空间、开机时间） | 非阻塞。若要与本目录其它 app 保持一致可以补一份，声明不追踪、不收集 |
| 截图里的界面 | 现有 3 张来自真实界面 | 若界面在提审前改动，截图要重做 |

---

## 9. 差异化：能用什么、不能用什么

按 `WeEdit/AGENTS.md` 的「差异化：这个 app 凭什么存在」一节整理。

### 能用的（代码里查得到，上面描述里已经用上）

| 卖点 | 依据 |
|---|---|
| 一篇稿变四个平台的格式 | `Shared/Platform.swift` 里有四套互不相同的平台定义（标题上限、正文上限、图片上限、是否吃表格/标题层级/内联颜色/并排图、版心宽度），`Shared/PlatformExport.swift` 里是四个独立的渲染器 |
| 上限在复制前提示 | `PlatformExport.export` 里在导出时就比对上限并生成提示，不是等粘完才知道 |
| 图片随文稿落盘、导出嵌进 HTML | `MediaEmbedder.embed` 把稿件自己的媒体转成内联数据；这一步的实际目的是绕开平台对外链图片的拦截 |
| 本地、无账号、无自建服务器 | 沙盒授权只有三项；全工程没有偏好设置读写；没有包管理器依赖 |

### 不能用的（作者自己否掉的，一个字都没写进商店文案）

| 说法 | 为什么不用 |
|---|---|
| 「更好的编辑器」 | AGENTS.md 开门第一句：「能撑住的只有一条，而且很窄。它不是更好的编辑器」 |
| 「对所有人都更省事」 | 原文：「只发一个平台的人，这条路更省事，**这个 app 对他是多余的**」「收益为零」 |
| 「能导入 markdown / docx / 抓网址」 | **输入侧是空的**，稿子只能手打或从浏览器粘贴 |
| 「排版能力强」 | 编辑器是 WKWebView 的 contenteditable，「远不如专业写作工具，也没打算做」 |
| 「一键发布」 | 平台没有给第三方用的稳定发文接口，不做登录发文；省的是重新排版的时间，不是发布的时间 |
| 「已经过验证」 | 「这条假设还没有被任何真实用户验证过」，零评分、零下载证据。所以描述里把「不适合谁」写在明面上 |
| 「完全离线」 | 不成立：文稿里的远程图片会向图片所在站点取图，打开平台后台也要联网 |

### 已知问题（描述里没有假装它们不存在）

`WeEdit/AGENTS.md` 的「已知问题」是逻辑测试钉住的现状，其中一条直接打在主路径上：
从公众号复制一篇文章粘进来，`section` 会被解析器拍平，段落挤成一坨。另外还有微博每段多一个空行、
公众号导出里视频音频多报一条提示。这些都已写进 `support.html` 的「已知不足」，商店文案里不重复，
但审核备注或用户问起时不要否认。
