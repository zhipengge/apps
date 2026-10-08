#!/usr/bin/env python3
"""
为 apps/<app>/ 生成 APP_STORE_LISTING.md、EXPORT_COMPLIANCE.md、
README.md、PRIVACY.md。

用法：
    python3 tools/gen_docs.py          # 全部
    python3 tools/gen_docs.py afu      # 只生成 afu
"""

import sys
from pathlib import Path

LISTING = """# {cn} ({en}) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **{platform}** | {wrong_platform} |
| 名称（主语言：简体中文） | **{cn}** | {bad_names} |
| 名称（English 本地化） | **{en}** | {bad_en} |
| 主要语言 | 简体中文 | — |
| Bundle ID | `{bundle}` | 任何旧 ID |
| SKU | `{sku}` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「{cn}」。

备选店名（创建时报名被占再用）：

{alt_names}

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
{promo_cn}
```

**字符数：{promo_cn_n} / 170**

### English

```
{promo_en}
```

**字符数：{promo_en_n} / 170**

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
{desc_cn}
```

**字符数：约 {desc_cn_n} / 4000**

### English

```
{desc_en}
```

**字符数：约 {desc_en_n} / 4000**

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
{sub_cn}
```

**字符数：{sub_cn_n} / 30**

### English

```
{sub_en}
```

**字符数：{sub_en_n} / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
{kw_cn}
```

**字符数：{kw_cn_n} / 100**

### English

```
{kw_en}
```

**字符数：{kw_en_n} / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/{slug}/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/{slug}/privacy.html` |
| 营销 URL | `https://zhipengge.github.io/apps/{slug}/` |

---

## 6. 类别、评级、隐私问卷

| 字段 | 建议 |
|---|---|
| 主要类别 | {category} |
| 次要类别 | {category2} |
| 年龄分级 | {rating} |
| App 隐私 | {privacy_q} |
| 出口合规 | NO（见 `EXPORT_COMPLIANCE.md`） |

审核备注建议写清：{review_note}

---

## 7. 截图

{shots}
"""

EXPORT = """# 出口合规说明 — {cn} ({en})

## 结论

每个 native target 的 Debug 与 Release 都填：

```
INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO
```

{targets_note}

## 为什么填 NO

{reason}

## 参考

- 适用条件 1：App 完全没有加密。
- 适用条件 2：加密仅用于认证 / 签名 / DRM / 走苹果系统或标准 HTTPS/TLS，没有自研算法。

{cn} 满足**条件 {cond}**。

---

最后更新：2026-10-08
"""

README = """# {cn}

{tagline}

## 这是什么

{what}

## 功能

{features}

## 系统要求

- 平台：{platform_long}
- 最低系统：**{min_os}**
- {langs}

## 常见问题

{faq}

## 隐私

{privacy_line}

- 完整政策：<https://zhipengge.github.io/apps/{slug}/privacy.html>
- 技术支持：<https://zhipengge.github.io/apps/{slug}/support.html>

## 反馈

问题与建议请提交到 <https://github.com/zhipengge/apps/issues>。
"""


def w(d: Path, name: str, text: str):
    p = d / name
    p.write_text(text, encoding="utf-8")
    print(f"  ✓ {p.name}  ({len(text)} 字节)")


def build(d: Path, cfg: dict):
    d.mkdir(parents=True, exist_ok=True)
    w(d, "APP_STORE_LISTING.md", LISTING.format(**cfg))
    w(d, "EXPORT_COMPLIANCE.md", EXPORT.format(**cfg))
    w(d, "README.md", README.format(**cfg))
    # PRIVACY.md 是 privacy.html 的纯文本对应稿
    w(d, "PRIVACY.md", cfg["privacy_md"])


# ============================================================

AFU = dict(
    slug="afu", cn="阿福", en="Afu", platform="iOS", wrong_platform="macOS",
    bundle="com.gezhipeng0201.Afu",
    note_bundle="⚠️ 工程里现值是小写 `com.gezhipeng0201.afu`，与全店 PascalCase 风格不一致。上架前改成 `Afu`。改了要同步 pbxproj、`AppIdentifiers` 和逻辑测试。",
    sku="afu-20261008",
    bad_names="AI 助手、本地大模型、聊天助手（通称易被占）",
    bad_en="AI Chat、Local LLM",
    alt_names="- 阿福本地助手\n- 阿福离线对话\n- Afu Local AI",
    promo_cn="模型下载到本机，对话与图片理解全部在设备上完成。不上传聊天内容，不需要账号，断网也能继续聊。",
    promo_en="Models download to your device. Chat and image understanding run entirely on-device. No uploads, no account, works offline.",
    sub_cn="端侧本地大模型助手",
    sub_en="Private on-device AI chat",
    desc_cn="""阿福是把大模型装进你手机里的对话助手。模型权重下载到本机，推理全部在设备上完成，你的聊天内容不会上传到任何服务器。

【本地推理】
- 模型下载到设备后，断网也能正常对话
- 支持 0.5B 到 4B 等多种参数规模的模型
- 可随时切换模型，对比不同模型的回答
- 支持温度、Top-P、最大回复长度等参数调整
- 可自定义系统提示词

【图片理解】
- 支持多模态模型，可直接对图片提问
- 图片在本机做识别与理解，不会上传

【文件解析】
- 支持 PDF、Word、Excel、CSV、TXT、Markdown
- 文件在本机解析为文本后再交给模型
- 适合长文档摘要与问答

【隐私】
- 没有账号，没有自建服务器
- 不接入广告、分析或追踪服务
- 网络只用于拉取模型清单和下载模型文件
- 对话、图片、文件都不会离开设备

【请注意】
首次使用需要下载模型，建议从 0.5B 到 2B 的小模型开始。参数越大的模型回答质量越高，但更慢、更占内存。""",
    desc_en="""Afu brings large language models onto your iPhone. Weights download to the device and all inference runs locally, so your conversations never leave it.

[On-device inference]
- Chat works offline once a model is downloaded
- Models from 0.5B up to 4B parameters
- Switch between models and compare their answers
- Adjust temperature, Top-P, and max reply length
- Custom system prompt

[Image understanding]
- Multimodal models answer questions about images
- Images are analysed on-device and never uploaded

[File parsing]
- PDF, Word, Excel, CSV, TXT, Markdown
- Files are parsed locally before the model sees them
- Good for summarising and querying long documents

[Privacy]
- No account, no backend of our own
- No ads, analytics, or tracking
- Network is used only to fetch the model list and download model files
- Conversations, photos, and files never leave the device

[Please note]
You need to download a model on first use. Start with a 0.5B to 2B model. Larger models answer better but are slower and use more memory.""",
    kw_cn="本地,离线,大模型,对话,图片理解,文件解析,隐私,ai,llm,模型下载",
    kw_en="local,offline,llm,chat,vision,document,private,on-device,model,gguf",
    category="效率 / Productivity",
    category2="工具 / Utilities",
    rating="4+（无不当内容）。用户可撰写任意提示词，但内容不公开、不联网传播",
    privacy_q="**不收集数据**。须与 `PRIVACY.md` 一致。注意：模型下载会连接 huggingface.co，但那只是拉取模型文件，不含用户数据，因此仍属「不收集」",
    review_note="本 App 不含任何内置模型，首次使用需联网下载；对话与推理全部在本机完成，聊天内容不上传。网络仅用于拉取模型清单和下载权重。",
    shots="""iPhone 6.9 寸与 iPad 13 寸各 3-10 张真实界面。至少包含：模型列表（有多种模型可选）、对话中（含字数/速度）、图片理解、文件解析、设置页、隐私说明页。""",
    targets_note="本 App 只有主 App 一个 native target，无扩展。",
    reason="""阿福没有任何自研加密算法。它对 HTTPS 的使用仅有两处：拉取公开的模型清单、从 Hugging Face 下载模型权重。两者都是通过苹果系统提供的标准 TLS 完成的，没有自带或自研的加密实现。

聊天内容、图片、文件全部在本机处理，不经过网络传输，也就不涉及加密。

因此满足条件 2。""",
    cond="2",
    tagline="把大模型装进手机，对话不出设备。",
    what="""阿福是一个端侧大语言模型对话助手。

模型权重从 Hugging Face 下载到本机后，**全部推理都在设备上完成**。你的聊天内容、图片和文件不会上传到任何服务器。

没有账号，没有自建后端，不内嵌广告或追踪服务。""",
    features="""- **本地推理**：模型下载后断网也能对话
- **多模型**：0.5B 到 4B 多种规模，可随时切换对比
- **图片理解**：多模态模型可直接对图片提问
- **文件解析**：PDF / Word / Excel / CSV / TXT / Markdown 在本机解析
- **参数可调**：温度、Top-P、最大回复长度、自定义系统提示词""",
    platform_long="iOS 17.0 及以上（iPhone 与 iPad）",
    min_os="iOS 17.0",
    note_min_os="⚠️ 工程里现值是 26.2，等于只支持最新系统，需要下调。",
    langs="中文与 English",
    faq="""**第一次打开模型列表是空的？**
阿福不含模型。打开「模型」页选一个下载即可。建议先试 0.5B 到 2B 的小模型。

**下载失败或很慢？**
默认走 Hugging Face 官方源。可在设置里切换到镜像源，或稍后重试，支持断点续传。

**需要 Hugging Face Token？**
部分模型需要授权。生成一个只读 Token 填进设置页即可，仅保存在本机钥匙串。

**回复慢或设备发烫？**
参数量越大越慢。0.5B 到 2B 在近期 iPhone 上通常流畅。可调低最大回复长度。""",
    privacy_line="阿福的对话、图片和文件全部在设备上处理，不会上传。网络仅用于拉取模型清单和下载模型权重。",
    privacy_md="""# 阿福（Afu）隐私政策

最后更新：2026-10-08

## 摘要

阿福的对话与推理全部在设备上完成，聊天内容不会上传到我们或任何第三方的服务器。没有账号，没有自建后端。

## 我们处理什么、在哪处理

| 数据 | 用途 | 位置 |
|---|---|---|
| 你输入的文本、模型回复、会话标题与时间 | 构建提示词并在本机生成回复 | 设备本地数据库 |
| 你从相册选择或拍摄的图片 | 在本机做文字识别、画面理解或摘要 | 设备本地；不上传 |
| 你通过「文件」导入的 PDF / Word / Excel / CSV / TXT / Markdown | 在本机解析为模型可读的文本 | 设备本地；不上传 |
| 生成参数 | 控制模型行为 | 设备本地 |
| Hugging Face Access Token（仅你主动填写时） | 下载需要授权的模型 | 设备钥匙串；只用于该次下载 |

## 网络通信

应用只在两处联网：

1. **拉取模型清单**：向公开的 GitHub 仓库请求可用模型列表，只读取清单，不发送任何个人信息。
2. **下载模型权重**：从 Hugging Face 官方源或你指定的镜像源下载模型文件。传输的只有模型文件本身，不包含你的对话、图片或文件。

除此之外不发起任何网络请求。断网时已下载的模型仍可正常对话。

## 我们不做的事

- 不把对话内容、图片或文件发到任何服务器
- 不要求注册或登录账号
- 不接入广告网络或分析平台
- 不读取通讯录、位置、麦克风
- 不把你的数据用于模型训练

## 数据删除

在应用内删除会话即可移除对应记录；删除整个 App 并移除其容器，即可清除全部本地数据（已下载的模型文件也会一并删除）。
""",
)


GWAVE = dict(
    slug="gwave", cn="牧云电台", en="Gwave", platform="iOS", wrong_platform="macOS",
    bundle="com.gezhipeng0201.Gwave",
    note_bundle="⚠️ 工程里现值是小写 `com.gezhipeng0201.gwave`，与全店 PascalCase 风格不一致。上架前改成 `Gwave`。",
    sku="gwave-20261008",
    bad_names="收音机、网络电台、电台播放器（通称易被占）",
    bad_en="Radio Player、Internet Radio",
    alt_names="- 牧云收音机\n- 牧云流声\n- Gwave Radio",
    promo_cn="搜台、收藏、后台播放，还能自己加源。内置雨声海浪等白噪声在本机实时合成。没有账号，不收集任何信息。",
    promo_en="Search, favorite, and play in the background. Add your own streams. Built-in rain and wave sounds are synthesised on-device. No account, no tracking.",
    sub_cn="网络电台与白噪声",
    sub_en="Radio and ambient sound",
    desc_cn="""牧云电台是一个极简的网络电台播放工具。搜到你喜欢的台，收藏起来，后台也能继续听。

【收听】
- 搜索全球公开的网络电台
- 收藏常听的台，支持分组整理
- 后台播放，锁屏界面和「正在播放」面板可直接控制
- 支持 AirPlay 与蓝牙输出

【自己加源】
- 手动添加电台名称与地址
- 从 JSON 或文本文件批量导入
- 用网址导入整份播放列表
- 支持 gwave 链接一键添加

【内置音效】
- 雨声、海浪、粉红噪声等助眠与专注音效
- 在本机实时合成，不占存储、不需要网络

【同步与外观】
- 可选 iCloud 同步，在你自己的账户里同步收藏与列表
- 深色、浅色、跟随系统

【隐私】
- 没有账号，不收集姓名、邮箱、位置
- 不收集你的播放记录
- 不接入广告、分析或追踪服务
- 音频直接从源站传到你的设备，我们不存储、不转发""",
    desc_en="""Gwave is a minimal internet radio player. Find a station, favourite it, and keep listening in the background.

[Listen]
- Search public internet radio stations
- Favourite the ones you like, organised in groups
- Background playback with lock screen and Now Playing controls
- AirPlay and Bluetooth output

[Add your own]
- Type a station name and URL
- Import a JSON or text list from a file
- Import a whole playlist from a URL
- One-tap add via gwave links

[Built-in sounds]
- Rain, waves, pink noise and more for sleep or focus
- Synthesised on-device: no storage, no network

[Sync and appearance]
- Optional iCloud sync of your list and favourites, in your own account
- Dark, light, or follow the system

[Privacy]
- No account, no collection of name, email, or location
- No collection of your listening history
- No ads, analytics, or tracking
- Audio goes straight from the source to your device""",
    kw_cn="电台,收音机,网络电台,白噪声,助眠,专注,收藏,后台播放,导入",
    kw_en="radio,station,stream,ambient,noise,sleep,focus,favorite,playlist,import",
    category="音乐 / Music",
    category2="娱乐 / Entertainment",
    rating="4+。用户可添加任意流地址，若勾选 Unrestricted Web Access 则为 17+",
    privacy_q="**不收集数据**。须与 `PRIVACY.md` 一致",
    review_note="本 App 为播放工具，不内置任何受版权保护的电台内容；用户可自行添加公开的网络电台地址。iCloud 同步走用户自己的 iCloud 账户。",
    shots="""iPhone 6.9 寸与 iPad 13 寸各 3-10 张真实界面。至少包含：搜索页、收藏列表、播放中（含锁屏控制）、白噪声、导入页、设置页。""",
    targets_note="本 App 只有主 App 一个 native target，无扩展。",
    reason="""牧云电台没有任何自研加密算法。它对网络的使用全部通过苹果系统提供的标准 HTTPS 完成：拉取公开电台目录、以及从源站拉取音频流。

电台列表与收藏的同步走的是苹果的 iCloud 键值存储，加密由系统负责，本应用不实现加密逻辑。

因此满足条件 2。""",
    cond="2",
    tagline="搜台、收藏、后台播放，还能自己加源。",
    what="""牧云电台是一个极简的网络电台播放器。

搜索全球公开的网络电台，收藏常听的台，后台也能继续听。也可以自己添加任意流地址，或从文件与网址导入整份播放列表。

内置雨声、海浪、粉红噪声等音效，**在本机实时合成**，不占存储也不需要网络。""",
    features="""- **搜台**：搜索公开的网络电台目录
- **收藏与分组**：整理常听的台
- **后台播放**：锁屏与「正在播放」面板可控，支持 AirPlay
- **自定义源**：手动添加、文件导入、网址导入、gwave 链接
- **白噪声**：雨声、海浪、粉红噪声，本机合成
- **iCloud 同步**：可选，数据在你自己的账户里""",
    platform_long="iOS 17.0 及以上（iPhone 与 iPad）",
    min_os="iOS 17.0",
    note_min_os="⚠️ README 里曾写 iOS 18.0，与工程的 17.0 不一致。以工程为准，或统一后同步。",
    langs="中文与 English",
    faq="""**怎么添加自己的电台？**
 三种方式：手动输入名称和地址、从文件导入、或用 `gwave://` 链接添加。也支持用网址导入整份列表。

**某个电台放不出来？**
可用性取决于源站。常见原因是源站下线、临时故障或地区限制。可以换同台的其它线路。

**后台播放怎么用？**
播放后锁屏即可继续。若被系统中断，重新打开应用恢复。

**iCloud 同步没生效？**
确认系统「设置 → Apple 账户 → iCloud」里本应用开关是开的。同步不是即时的，也可以手动下拉刷新。""",
    privacy_line="牧云电台不收集、不存储、不共享任何可识别你身份的信息。音频直接从源站传到你的设备。",
    privacy_md="""# 牧云电台（Gwave）隐私政策

最后更新：2026-10-08

## 摘要

牧云电台不收集、不存储、不共享任何可识别你身份的信息。没有账号，没有自建后端。

## 我们处理什么、在哪处理

| 数据 | 用途 | 位置 |
|---|---|---|
| 你添加的电台名称与地址 | 在本地保存你的电台列表 | 设备本地 |
| 收藏、最近播放、音量等偏好 | 恢复上次的使用状态 | 设备本地；如开启 iCloud 则同步到你自己的 iCloud 账户 |
| 播放状态 | 支持后台播放与锁屏控制 | 设备内存 |

## 网络通信

音频内容直接从对应的网络音频源传输到你的设备。我们不存储、不分析、不再分发任何音频内容。此外，应用会访问公开的电台目录服务（radio-browser.info 及其镜像）以搜台，请求中不含你的个人信息。

## iCloud 同步

如果你开启了 iCloud 同步，电台列表与收藏会保存在你自己的 iCloud 账户里（使用 Apple 的键值存储）。我们无法读取这些数据。

## 我们不做的事

- 不要求注册或登录
- 不收集姓名、邮箱、电话、位置
- 不收集音频内容或播放记录
- 不接入广告、分析或统计服务
- 不把任何数据共享给第三方

## 儿童隐私

我们不主动收集 13 岁以下儿童的任何个人信息。

## 数据删除

删除 App 即可清除全部本地数据。若开启过 iCloud 同步，请在系统「设置 → Apple 账户 → iCloud → 管理账户存储」中删除「牧云电台」的数据。
""",
)


RECORD = dict(
    slug="record", cn="效率打卡", en="RecordBot", platform="iOS", wrong_platform="macOS",
    bundle="com.gezhipeng0201.RecordBot",
    note_bundle="工程现值与全店风格一致，无需修改。",
    sku="recordbot-20261008",
    bad_names="打卡、习惯、记账（通称易被占）",
    bad_en="Habit Tracker、Check-in",
    alt_names="- 效率打卡本\n- 每日打卡\n- RecordBot Habits",
    promo_cn="打卡、指标、多档案，数据只留在这台设备上。没有账号，不上传，不追踪。换手机用导出导入即可。",
    promo_en="Habits, metrics, multiple profiles, all stored on this device. No account, no upload, no tracking. Move devices with export and import.",
    sub_cn="本地优先的打卡记录",
    sub_en="Offline habit and metric log",
    desc_cn="""效率打卡是一个本地优先的打卡与指标记录工具。数据只存在这台设备上，没有账号，不上传。

【打卡】
- 建立任意打卡任务，设置标题、描述与时间范围
- 支持按天、按周、自定义间隔重复
- 可开启本地提醒，由系统在本机调度
- 错过也能补打卡

【指标记录】
- 记录体重、身高等健康指标
- 趋势图按时间展示变化
- 可标记备注与来源

【多档案】
- 支持多个使用者档案
- 每个档案的打卡与指标相互独立
- 适合家庭共用一台设备

【备份与迁移】
- 支持导出为文件，换手机时导入恢复
- 数据不会自动上云

【隐私】
- 没有账号，没有服务器
- 不接入广告、分析或追踪服务
- 通知与照片权限只在你授权后使用，且都能单独关闭""",
    desc_en="""RecordBot is a local-first habit and metric tracker. Your data stays on this device. No account, no upload.

[Check-ins]
- Create tasks with a title, description, and date range
- Repeat daily, weekly, or at a custom interval
- Optional local reminders scheduled by the system
- Backfill days you missed

[Metrics]
- Record weight, height, and other measures
- Trend charts over time
- Attach notes

[Profiles]
- Multiple user profiles
- Each keeps its own check-ins and metrics
- Good for a shared family device

[Backup and migration]
- Export to a file and import on a new phone
- Nothing syncs to the cloud automatically

[Privacy]
- No account, no server
- No ads, analytics, or tracking
- Notification and photo permissions are used only after you allow them, and can be turned off individually""",
    kw_cn="打卡,习惯,记录,指标,体重,身高,趋势,提醒,备份,多用户",
    kw_en="habit,tracker,checkin,streak,metric,weight,reminder,offline,backup,log",
    category="效率 / Productivity",
    category2="健康健美 / Health & Fitness",
    rating="4+",
    privacy_q="**不收集数据**。须与 `PRIVACY.md` 一致",
    review_note="本 App 为纯本地工具，不运营服务器，全部数据保存在设备本地；通知由系统在本机调度。",
    shots="""iPhone 6.9 寸与 iPad 13 寸各 3-10 张真实界面。至少包含：空状态、打卡列表、新建任务、指标趋势图、档案切换、导出页。""",
    targets_note="本 App 只有主 App 一个 native target，无扩展。",
    reason="""效率打卡没有任何自研加密算法，也完全没有网络代码。它不发起任何网络请求，数据全部保存在设备本地的数据库中。

因此满足条件 1。""",
    cond="1",
    tagline="本地优先的打卡与指标记录。",
    what="""效率打卡是一个本地优先的打卡与指标记录工具。

建立任意打卡任务并设置重复规则，用系统本地通知提醒自己。也可以记录体重、身高等健康指标，用趋势图看变化。

支持多个使用者档案，适合家庭共用。**数据只存在这台设备上**，没有账号，也不上传。""",
    features="""- **打卡任务**：标题、描述、时间范围、按天/按周/自定义间隔重复
- **本地提醒**：由系统在本机调度
- **指标记录**：体重、身高等，带趋势图
- **多档案**：每个使用者独立记录
- **导入导出**：换手机时迁移数据
- **补打卡**：错过的日子可以补记""",
    platform_long="iOS 17.0 及以上（iPhone 与 iPad）",
    min_os="iOS 17.0",
    note_min_os="工程现值 17.0，符合规范。",
    langs="中文与 English",
    faq="""**提醒没有按时出现？**
先确认系统「设置 → 通知 → 效率打卡」权限已打开。提醒由系统本地调度，低电量模式可能延迟。

**怎么备份或换手机？**
用导出功能生成文件，在新设备上导入恢复。数据不会自动上云，换机前记得先导出。

**多个使用者怎么区分？**
用「档案」功能。每个档案有独立的打卡记录和指标。

**数据存在哪里？**
只在这台设备上。详见隐私政策。""",
    privacy_line="效率打卡以本地优先为设计原则，你的打卡、指标和档案默认只存在这台设备上。",
    privacy_md="""# 效率打卡（RecordBot）隐私政策

最后更新：2026-10-08

## 摘要

「效率打卡」以本地优先为设计原则，你的打卡、指标和档案默认只存在这台设备上。没有账号，我们也不运营用于存储你个人数据的中央服务器。

## 我们处理什么、在哪处理

| 数据 | 用途 | 位置 |
|---|---|---|
| 打卡任务的标题、描述、时间范围与重复规则 | 展示任务并按规则调度提醒 | 设备本地数据库 |
| 打卡记录 | 统计与可视化 | 设备本地数据库 |
| 健康类指标（如体重、身高等） | 记录与趋势图 | 设备本地数据库 |
| 用户档案名称与外观设置 | 区分多个使用者 | 设备本地数据库 |
| 你主动附加的照片或文件 | 保存到对应的本地任务中 | 设备本地 |

## 设备权限

只在必要时申请，且仅在你授权后使用：

- **通知**：在你开启提醒时，于本地调度任务提醒。通知由系统在本机触发，不经过任何服务器。
- **照片 / 文件**：仅在你主动导入附件或从相册添加图片时使用。

拒绝某项权限只会导致对应功能不可用，不影响其它本地功能。

## 我们不做的事

- 不要求注册或登录
- 不把打卡记录、指标数据上传到服务器
- 不接入广告网络、分析或追踪 SDK
- 不把你的数据出售或用于广告画像
- 不读取通讯录、位置、麦克风、摄像头

## 数据的导出

应用提供导入 / 导出功能。当你导出时，数据会以你选择的方式离开设备，请自行妥善保管导出文件。

## 数据删除

在应用内删除对应的任务、记录或档案即可移除；删除整个 App 会清除全部本地数据。
""",
)


SPINCOURT = dict(
    slug="spincourt", cn="野球场分拨助手", en="SpinCourt", platform="iOS", wrong_platform="macOS",
    bundle="com.gezhipeng0201.SpinCourt",
    note_bundle="工程现值与全店风格一致，无需修改。",
    sku="spincourt-20261008",
    bad_names="分组、随机、抽签（通称易被占）",
    bad_en="Team Picker、Random Teams",
    alt_names="- 球场分拨\n- 野球场分队\n- SpinCourt Teams",
    promo_cn="设好人数和队数，转一转就把人分好。纯离线，不联网，不收集任何信息。",
    promo_en="Set the player count and team count, spin, and the teams are drawn. Fully offline. Nothing collected.",
    sub_cn="野球场随机分队",
    sub_en="Random teams for pick-up games",
    desc_cn="""野球场分拨助手帮你快速把来球场的人随机分成几队，省去现场点人分组的麻烦。

【怎么用】
- 设置总人数，范围 2 到 25
- 设置要分成几队
- 点开始，转盘把每个人随机分到战队里
- 每个战队有专属颜色和名字

【特点】
- 纯随机，不预设规则
- 结果一目了然，适合当面展示
- 完全离线，不需要网络

【隐私】
- 不收集、不存储、不传输任何个人信息
- 不集成任何第三方服务、分析工具或广告
- 不发起任何网络请求

【适用场景】
- 野球场临时分队
- 班级或团建活动分组
- 任何需要随机分组的场合""",
    desc_en="""SpinCourt splits the people who showed up into teams, so you do not have to pick sides by hand.

[How it works]
- Set the number of players, from 2 to 25
- Set how many teams you want
- Tap start and the wheel assigns everyone randomly
- Each team gets its own colour and name

[What makes it simple]
- Purely random, no hidden rules
- Results are easy to read out loud
- Works fully offline

[Privacy]
- Collects, stores, and transmits nothing
- No third-party services, analytics, or ads
- Makes no network requests

[Good for]
- Pick-up games at the park
- Class or team-building splits
- Any situation that needs a random draw""",
    kw_cn="分组,分队,随机,抽签,球场,比赛,组队,离线",
    kw_en="team,random,picker,split,shuffle,sport,game,offline,draw",
    category="体育 / Sports",
    category2="工具 / Utilities",
    rating="4+",
    privacy_q="**不收集数据**。须与 `PRIVACY.md` 一致",
    review_note="本 App 完全离线，不发起任何网络请求，不收集任何数据。",
    shots="""iPhone 6.9 寸与 iPad 13 寸各 3-10 张真实界面。至少包含：设置人数、转盘动画中、分组结果、战队设置。""",
    targets_note="本 App 只有主 App 一个 native target，无扩展。",
    reason="""野球场分拨助手没有任何加密逻辑，也完全没有网络代码。它不发起任何网络请求，所有计算（随机数生成）都在设备本地完成。

因此满足条件 1。""",
    cond="1",
    tagline="转一转，把野球场的人随机分好队。",
    what="""野球场分拨助手帮你把来球场的人随机分成几队，省去现场点人分组的麻烦。

设置总人数和战队数量，点开始，转盘会把每个人随机分到战队里。每个战队有专属颜色和名字。

**完全离线运行**，不联网，不收集任何信息。""",
    features="""- **快速分队**：设人数（2 到 25）和队数即可
- **转盘可视化**：随机过程直观可见，适合当面展示
- **战队配色**：每队专属颜色和名字
- **纯随机**：不预设任何隐藏规则
- **完全离线**：不需要网络""",
    platform_long="iOS 18.0 及以上（iPhone 与 iPad）",
    min_os="iOS 18.0",
    note_min_os="工程现值 18.0。若未用到 18 独有 API，建议下调到 17.0 以覆盖更多用户。",
    langs="中文与 English",
    faq="""**怎么用？**
设好总人数（2 到 25）和战队数量，点开始即可。每个战队有专属颜色和名字。

**分组结果不公平？**
分拨是纯随机。想更均衡可以多转几次，或调整队数让每组人数更接近。

**能保存分组结果吗？**
应用不保存历史记录，每次分组相互独立。可以截图保存。

**需要联网吗？**
不需要，全部功能离线可用。""",
    privacy_line="野球场分拨助手完全离线运行，不收集、不存储、不传输任何个人信息。",
    privacy_md="""# SpinCourt 隐私政策

最后更新：2026-10-08

## 摘要

野球场分拨助手完全离线运行，不收集、不存储、不传输任何个人信息。

## 我们不收集任何数据

包括但不限于：

- 姓名、电子邮件地址、电话号码
- 位置信息
- 设备标识符
- 使用数据或分析数据
- 任何其它个人身份信息

## 本地数据

应用的全部功能都在你的设备上本地运行。你输入的内容（如参与人数、战队数量、战队名称与颜色）仅存在于设备内存中，不写入服务器，也不发送给任何第三方。关闭应用即消失。

## 网络

本应用不发起任何网络请求。不需要联网即可使用全部功能。

## 第三方服务

不集成任何第三方服务、分析工具或广告网络。

## 儿童隐私

本应用适用于所有年龄段的用户。由于不收集任何信息，也就不存在儿童信息的收集问题。
""",
)


APPS = {
    "afu": AFU,
    "gwave": GWAVE,
    "record": RECORD,
    "spincourt": SPINCOURT,
}


def count(s: str) -> int:
    return len(s.replace("\n", "").strip())


def main():
    root = Path(__file__).resolve().parent.parent
    want = sys.argv[1:] or list(APPS)
    for name in want:
        cfg = APPS.get(name)
        if not cfg:
            print(f"未知 app: {name}")
            continue
        print(f"######## {name} ########")
        # 预先算好字数
        for k in ("promo_cn", "promo_en", "desc_cn", "desc_en", "sub_cn", "sub_en", "kw_cn", "kw_en"):
            cfg[f"{k}_n"] = count(cfg[k])
        build(root / name, cfg)


if __name__ == "__main__":
    main()
