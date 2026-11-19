# 牧云音乐 (MuYunMusic) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。只要简体中文一份。
> 副标题与关键词不要出现 Mac / iOS / Apple 这类商标词。
>
> **最后按真实界面校对：2026-11-18（版本 1.0，模拟器验收后）。**
> **素材状态：文案 / 截图 / 隐私页 / 权限说明已齐；等手动 archive、建 Record、填 ASC。**
> 真机项（后台/锁屏/拔耳机/电话打断/相机/本地网络）未做，见源码仓库 README「未验证」。
> **提审前必须补真机验收，别拿模拟器截图当功能已过。**

---

## 0. App Record 现状

| 字段 | 值 |
|---|---|
| 记录 | **未建**。从未进过任何 ASC 流程 |
| 平台 | iOS 17.0+（声明支持 iPad：`TARGETED_DEVICE_FAMILY = "1,2"`） |
| 名称（主语言：简体中文） | **牧云音乐** |
| 主要语言 | 简体中文 |
| Bundle ID | `com.gezhipeng0201.MuYunMusic` |
| 扩展 Bundle ID | `com.gezhipeng0201.MuYunMusic.Share`（分享扩展） |
| SKU | `muyunmusic-20261103` |
| 类别 | **音乐**（次要：工具） |
| 版权 | `2026 Zhipeng Ge` |
| 价格 | ⏳ **未定**，见下 |

**价格必须先拍板再建 Record**：

- 家族 precedent：牧云电台、牧云电视都是免费——媒体播放器收费会坐实
  「卖内容」的嫌疑（`定价策略.md` §三对 MuyunTV 写得很直白）。
- 但 2026-10-16 的决定是**新 app 走 ¥6 一口价**（对照实验），而本 App
  与电台/电视最大的不同是**除随包一首《冬日之光》外、零内置内容源**——其余每个字节都得用户自己给。
- 建 Record 默认免费。**要 ¥6 就在建 Record 当天用 `pricing.py` 设**，
  别上线后再改（改价虽不用过审，但「先免费后收费」在评分上最伤）。
- **本次不替你拍板**：清单里标了「价格：待定」，archive 后按这一节二选一。

**4.3 抗辩用差异化叙事（不要改写成绝对句式）**——详见 §10。
**禁写**「全网唯一」「同类没有」这类绝对句式。

---

## 1. 推广文本 (Promotional Text)

> **上限 170 字符**，可在不提交新版本的情况下随时修改。

```
一款真正离线的本地音乐播放器：除随包一首《冬日之光》外不内置曲库，只播你导入的文件。lrc 与内嵌歌词、收藏与最近播放、歌单与队列、后台与锁屏控制、局域网 Wi-Fi 传歌。0 统计 0 广告 0 账号，数据全本机。
```

**字符数：约 104 / 170**

---

## 2. 描述 (Description)

> **上限 4000 字符**。修改需提交新版本审核。

```
牧云音乐是一款纯本地音乐播放器：没有曲库、没有推荐、没有订阅，只播放你自己导入的音乐文件。如果你用不惯「不联网就没歌听」的播放器，这里正相反——所有音乐都在你自己的手机上。

【导入有六条路，总有一条顺手】
- 文件 App 里长按音频，选「用牧云音乐打开」
- 微信、邮件里点分享，选牧云音乐
- 数据线连电脑，Finder / iTunes 文件共享直接拖进来
- 从 iCloud Drive 挑文件（走系统选择器）
- Wi-Fi 传歌：同一网络下打开一个本机网页，电脑手机互传（默认关闭，手动开启）
- 直连地址：粘贴一个你自己的音频地址，流播或导入

【曲库与整理】
- 歌曲 / 专辑 / 艺术家 / 歌单 / 已下载五段，支持多种排序
- 「我的音乐」固定入口：收藏、最近播放（完整历史）
- 本地搜索，不联网也搜得到
- 歌曲信息编辑：标题、艺术家、专辑，保存后排序立即更新
- 自建歌单，支持拖动排序

【播放】
- 后台播放与锁屏控制：锁屏、控制中心、耳机线控都能播放暂停、切歌、跳 ±15 秒
- 上一首 / 下一首，进度条旁支持长按连跳
- 随机播放、列表循环、单曲循环——抽成一个按钮，点一下切一种，带文字回显
- 定时停止 15 / 30 / 60 分钟，末 3 秒增益淡出
- 播放队列：点行切歌、拖动排序、添加到队列、清空队列

【歌词】
- 支持 .lrc 文件与内嵌歌词：多时间戳一行、offset 偏移、无时间戳行置顶
- 播放页实时滚动，当前行整行高亮；字号三档
- 对不齐可以在「歌曲详情 → 歌词同步」按歌曲微调，不用每次调

【你的数据，你自己拿着】
- 不联网统计、无广告、无账号、没有第三方 SDK
- 音乐、歌词、收藏、设置全部存在这台手机的沙盒里，卸载即清空
- 只有你主动操作时才联网：扫码或手填你自己的家庭影音服务器、Wi-Fi 传歌、粘贴直连地址
- 相机只在扫码填服务器地址时使用，画面仅在本机识别，不保存、不上传
- 本地网络只在你连接局域网里的自填服务器、或开启 Wi-Fi 传歌时请求；不扫描、不发现设备
- 除相机与本地网络外，不申请相册、通讯录、位置、通知、追踪等权限

除随包一曲《冬日之光》外，本 App 不内置、不提供、不抓取任何第三方曲库，也不展示任何推荐内容。其余音乐来源是你自己的文件和你自己填的地址。
```

**字符数：约 1100 / 4000**

---

## 3. 副标题 (Subtitle)

> **上限 30 字符**

```
只播你自己导入的本地音乐
```

**字符数：12 / 30**

---

## 4. 关键词 (Keywords)

> **上限 100 字符**（含逗号）。不要重复 App 名，不要写竞品名。

```
音乐,播放器,本地,离线,歌词,歌单,收藏,最近播放,后台播放,锁屏,导入,文件,无损,FLAC,WAV,队列
```

**字符数：约 74 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | https://zhipengge.github.io/apps/muyunmusic/support.html |
| 隐私政策 | https://zhipengge.github.io/apps/muyunmusic/privacy.html |
| 营销（可选） | 留空（不提交死链；目录页没有 index） |

**页面不可达会被审核挡下。** 两个页面已推 `zhipengge/apps` 并部署，
2026-11-18 已验 **200**（正文含「本地网络」新段落）。

App 内「关于」页有支持邮箱；与家族一致，隐私/支持 URL 主要存在于 ASC 元数据。

---

## 6. 类别、分级与权限

| 项 | 值 |
|---|---|
| 主要类别 | 音乐 MUSIC |
| 次要类别 | 工具 UTILITIES |
| 内容分级 | 4+ |
| 年龄 | 不针对儿童，无广告、无追踪、无账号、无公开 UGC 信息流 |
| 相机 | **可选**，只用于扫码填写家庭影音服务器地址；画面本机识别，不保存/不上传（`NSCameraUsageDescription`） |
| 本地网络 | **可选**，只用于连接用户自填的局域网家庭影音服务器，或 Wi-Fi 传歌的本机监听；不扫描、不发现设备（`NSLocalNetworkUsageDescription`） |
| 其他权限 | 相册、通讯录、位置、通知、追踪、麦克风：不申请 |
| App 隐私问卷 | **不收集数据**（§11），与隐私政策一致 |

本地只有 UserDefaults（`muyunmusic.*` 键前缀）、沙盒音频目录、
App Group 分享中转箱，都不构成「收集」。相机与本地网络是系统权限，
不是数据收集；画面/局域网内容不离开用户设备或用户自己的服务器。

---

## 7. 截图

**已生成「连续全景」一套并体检**（2026-11-18；6.9 寸 iPhone + 13 寸 iPad）：
4 张竖图是同一张连续横图的切片；3 个**斜置**手机屏统一向右倾 7°、顶边同高，分别跨第 1/2、2/3、3/4 张，
连起来才是完整三屏。按 `01 → 04` 顺序上传，不要打乱。

| 档位 | 尺寸 | 目录 | 张数 |
|---|---|---|---|
| 6.9" iPhone | 1320×2868 | `screenshots/iphone/` | 4 |
| 13" iPad | **2064×2752** | `screenshots/ipad/` | 4 |

> iPad 那张必须是 2064×2752；12.9" 的 2048×2732 会被拒。
> 每张都是模拟器实拍切片；尺寸/撞边由 `_tools/check_store_shots.py` 全绿。
> 连续全景预览：`screenshots/panorama/iphone-preview.png`（iPhone）、
> `screenshots/panorama/ipad-preview.png`（iPad）；
> 原尺寸整图：`screenshots/panorama/iphone-full.png`（5280×2868）、
> `screenshots/panorama/ipad-full.png`（8256×2752），只作预览/营销，不传 ASC。

iPhone 四张（单看是局部，连起来是三屏）：

| 文件 | 切片内容 |
|---|---|
| `01` | 品牌文案 + 曲库屏左半 |
| `02` | 曲库屏右半 + 歌词屏左半 |
| `03` | 歌词屏右半 + 队列屏左半 |
| `04` | 队列屏右半 + 隐私收尾 |

iPad 四张：

| 文件 | 切片内容 |
|---|---|
| `01` | 品牌文案 + 大屏曲库左半 |
| `02` | 大屏曲库右半 + 大屏歌词左半 |
| `03` | 大屏歌词右半 + 设置屏左半 |
| `04` | 设置屏右半 + 隐私收尾 |

> 截图里的曲目/封面/歌词都是 `screenshots/showcase/` 的原创演示素材，
> 不是第三方内容；不会随 App 打包。

---

## 8. 提交前检查表

| 项 | 状态 |
|---|---|
| App Record | ⛔ 未建（建的时候顺手抢「牧云音乐」店名） |
| 文案（本文件 §1–§4） | ✅ 本文件，未写入 ASC（Record 还没有） |
| 隐私政策 / 支持页 | ✅ 已推 `apps` 仓库并部署，2026-11-18 验 200 |
| 隐私清单 | ✅ 零收集；UserDefaults `CA92.1` + FileTimestamp `C617.1` + SystemBootTime `35F9.1` |
| 出口合规 | ✅ `ITSAppUsesNonExemptEncryption = NO`，已核验 1.0 产物 |
| ATS | ⚠️ **`NSAllowsArbitraryLoads` + `NSAllowsArbitraryLoadsForMedia` 都在**；只服务用户自填的 http 源/服务器，无内置地址。审核口径见 §9，别照旧文档说成只有 media-only |
| 相机权限 | ✅ `NSCameraUsageDescription` 已在 Info.plist；隐私页已更新 |
| 本地网络权限 | ✅ `NSLocalNetworkUsageDescription` 已补；隐私页已更新 |
| 图标 | ✅ 1024×1024（M + 音符，与牧云电台/电视同族）；浅色/深色 PNG **无 alpha**（ASC 要求），tinted 保留透明 |
| 截图 | ✅ 4 iPhone + 4 iPad 连续全景，尺寸/撞边检查通过（§7） |
| 类别 / 分级 / 内容版权 / 问卷答案 | ✅ 答案见 §6、§11–§13 + `_tools/asc/answers/muyunmusic.json` |
| CarPlay | ⏸ 1.0 未启用：`com.apple.developer.carplay-music` 未获批，Info.plist CarPlay scene 与 entitlement 已移除；车机代码保留，后续版本获批再加 |
| 价格 | ⏳ 未定（§0，二选一；若收费需先完成 Paid Apps 协议与税务/银行） |
| **真机验收** | ⛔ **后台/锁屏/拔耳机/电话打断/相机/本地网络未做**——目前最大欠账 |
| 构建上传 | ⛔ 手动 archive（按既定规矩不走自动） |
| 提审方式 | **单独提审**。家族媒体播放器已有两个在架（电台/电视），批量或同期提就是给 4.3 递刀 |

---

## 9. 审核备注 (App Review Notes)

> 推荐直接粘贴**英文版**（审核员默认英文）；中文版放在下面供你核对。

**English**

```
No demo account is required. To test: open the system Files app, long-press any
mp3/m4a/flac file, choose "Open with MuYun Music", then play it.

The app ships one owner-supplied track, "Winter Light" (冬日之光), with
lyrics by Deepseek and music/performance by Minimax, plus its cover, plus no catalog, no recommendations, and no account system.
Apart from that one track, everything it plays comes from files the user imports
or addresses the user enters. The bundled track is original/owner-provided; it
is not third-party catalog content.

To hear the bundled track: open the Library tab and tap "冬日之光". Its lyrics
include line timestamps and scroll in sync with playback; the rest of the app is
unaffected.

Network access happens only from explicit user actions:
1) Optional family media server: the user enters their own server base URL in
   Settings (or scans a QR code on that server's home page). When the user taps
   search / test / stream / download / share, the app sends the search keyword,
   the requested media URL, or the file the user chose to share to THAT server.
   There is no built-in server URL (builtinSourceURLs = []); leaving the field
   empty hides all server UI and makes no request. The developer operates no
   server and receives nothing.
2) Wi-Fi transfer (default OFF): the user enables it; the app listens on a fixed
   local port so a browser on the same LAN can upload files. No Bonjour, no
   discovery, no internet.
3) Direct URL: the user pastes an audio URL; the app performs a plain HTTP(S)
   file request to that address, with no account or device identifier.

Camera is optional and used only to scan the server's QR code; frames are
decoded on-device, never saved or uploaded.
Local Network permission is used only for the app's local-network features:
reaching the user's own LAN server and the optional Wi-Fi transfer listener.
The app does not scan or discover devices. If denied, local playback still works.

ATS: NSAllowsArbitraryLoads and NSAllowsArbitraryLoadsForMedia are enabled
because the user's own server/audio URLs may be plain HTTP. The app contains no
built-in hosts; all hosts come from user input.

Background audio is used for playback with the screen off. No analytics, ads,
tracking, or third-party SDKs.
```

**中文（核对用）**

```
无需演示账号。测试方法：用系统「文件」App 准备任意一个 mp3/m4a/flac 文件，
长按选「用此 App 打开」导入，即可完整体验。

除随包一曲《冬日之光》外，App 不内置任何音频、曲库、推荐或账号系统。所有其他内容来自用户导入的文件或
用户自己填写的地址。随包曲目词：Deepseek、曲/演唱：Minimax，歌词带行级时间轴，App 内可逐行同步。

网络只在用户明确操作时发生：
1) 可选的家庭影音服务器：用户在设置里填自己的服务器地址（或扫服务器首页
   二维码）。用户点测试/搜索/播放/下载/分享时，App 才把搜索词、请求的媒体
   URL，或用户选择分享的文件发到那台服务器。没有内置服务器地址
   （builtinSourceURLs = []）；留空则整块 UI 隐藏、零请求。开发者没有服务器，
   也收不到任何内容。
2) Wi-Fi 传歌（默认关闭）：用户手动开启后，App 在本机固定端口监听，
   仅同网段设备可访问上传页；不用 Bonjour、不发现、不连外网。
3) 直连地址：用户粘贴音频 URL，App 只向那个地址发普通 HTTP(S) 文件请求，
   不带账号或设备标识。

相机仅用于扫码填服务器地址，画面在本机识别，不保存、不上传。
本地网络仅用于本 App 的局域网功能：连接用户自己的局域网服务器，以及可选的
Wi-Fi 传歌监听；App 不扫描、不发现设备；拒绝后本地播放不受影响。

ATS 的 NSAllowsArbitraryLoads 与 NSAllowsArbitraryLoadsForMedia 都是为
用户自填的 http 服务器/音频地址服务；App 没有内置 host，所有 host 来自用户输入。

后台音频用于息屏播放。无统计、广告、追踪或第三方 SDK。
```

---

## 10. 差异化依据（不写进商店文案，给审核对话用）

先说实话：**这是家族里第三个媒体播放器**（牧云电台 · 收音机 / 牧云电视 ·
IPTV / 牧云音乐 · 本地曲库）。「账号 + 概念相似度」这条 4.3 判据上我们有
真实暴露面，所以——**只单独提审，且概念必须讲清楚不是一回事**：
电台/电视的本质是「拉取频道列表流」，本 App 是**零网络目录的本地文件播放器**，
连内置源列表都不存在（代码里有断言）。

被问「和已有 App / 市面播放器有什么区别」，按这几条答，每条能指到代码位置：

1. **内置内容可静态核验**：`Shared/AppIdentifiers.builtinSourceURLs = []`、
   `hasBundledSampleSongs = false` 都有 LogicTests 断言守着；bundle 内只有
   词：Deepseek、曲/演唱：Minimax 的 1 首《冬日之光》（WAV + 带时间轴 LRC + 封面），清空曲库后
   不回填示例。
2. **队列引擎是纯函数**：`Shared/QueueEngine.swift` 把 随机×循环(off/all/one)
   全部组合的下一首语义写成真值表，LogicTests 逐项覆盖；
   单曲循环下手动切歌**照常前进**（对齐 Apple Music 语义），
   只有自然播完才回环。
3. **歌词引擎完整度**：`Shared/LyricsParser.swift` 支持一行多时间戳、
   offset、无时间戳行置顶、内嵌歌词；按歌曲记忆手动偏移。
4. **六通道导入 + 路径收口**：分享扩展 / 文件打开 / 文件共享 / iCloud 选择器 /
   Wi-Fi 传歌 / 直连 URL 全部走同一条去重合并逻辑（`Shared/LibraryMerger.swift`），
   `sanitizeImportPath` 拒绝 `..`/`\`/NUL/`:`，有断言。
5. **局域网传歌的合规做法**：不用 Bonjour（`bonjourServiceTypes = []` 有断言）、
   不申请发现型能力、默认关闭、仅本机网段、纯被动监听；连接用户自填的
   局域网服务器时才需要本地网络权限。

---

## 11. App 隐私问卷（只能网页填，逐项答案）

路径：App Store Connect → App → 「App 隐私」。

| 问题 | 选 |
|---|---|
| Do you or your third-party partners collect data from this app? | **No** |

选 No 之后问卷就结束了。

**为什么是 No**：Apple 定义的「收集」是把数据传离设备且开发者可读到。
本 App 没有统计/广告 SDK、没有自有服务器；三类网络都是**用户主动发起**的
动作——粘贴地址的 GET、局域网传歌、以及把搜索词/文件发到**用户自己的**
家庭影音服务器。请求不带任何个人标识；数据去向由用户自己的服务器/文件
流向决定，开发者不可读。这与家族对 gwave / MuyunTV 的答卷一致
（见 `_tools/asc/answers/`）。

**权限不是收集**：相机（可选扫码）与本地网络（可选连自填服务器）都是
系统授权；数据不离开设备或用户自己的服务器。相册、位置、通讯录、麦克风、
通知、追踪都不申请（后台音频是 capability，不是弹窗权限）。

---

## 12. 年龄分级（只能网页填，逐项答案）

路径：App Store Connect → App → 「年龄分级」。逐项下拉，**全部 None / No**：

| 项 | 选 |
|---|---|
| 卡通或写实暴力 / 血腥 | None |
| 粗话或低俗幽默 | None |
| 成人/暗示性主题、性内容 | None |
| 恐怖或惊悚主题 | None |
| 医疗/治疗信息、健康话题 | None / No |
| 酒精烟草毒品、模拟赌博、竞赛抽奖 | None |
| 无限制的网页访问 | **No** |
| 内购 / 广告 / 公开 UGC / 社交 | No |
| 年龄保证 (Age Assurance) | No |

**结果应为 4+**。

**「无限制网页访问」为什么填 No**：App 不是浏览器，没有任意 URL 输入后
渲染网页的能力；「粘贴直连地址」只取音频流，与浏览器控件无关。
家庭影音服务器的搜索结果也只是曲目列表，不是网页渲染。
（如果审核追问，说明它是 AVPlayer 的媒体加载而非网页浏览。）

**UGC 为什么填 No**：App 没有公开信息流、评论或社区；歌曲分享只上传到
**用户自己的**家庭影音服务器，其他 App 用户看不到。

---

## 13. 其余手工项

| 位置 | 填什么 |
|---|---|
| 审核信息 → 联系 | 账号里已有联系人，不代填 |
| 审核信息 → 演示账号 | **不需要**，备注里写明导入方法（§9） |
| 审核信息 → 备注 | 粘贴 §9 英文版 |
| 版本信息 → 版权 | `2026 Zhipeng Ge` |
| 内容版权 (Content Rights) | **DOES_NOT_USE_THIRD_PARTY_CONTENT**——除随包一首词：Deepseek、曲/演唱：Minimax 的《冬日之光》外，App 自身不含、不展示、不访问第三方内容；其余内容均来自用户导入/用户粘贴（与 MuyunTV 答卷同理，若审核对自填地址有异议按 §9 口径答） |
| 出口合规 | 上传自动跳过（build setting 已 NO；产物已验） |
| 价格 | §0，建 Record 当天定 |
| 销售范围 | 所有国家/地区（若 EU 需要 DSA 交易者状态，按账号实际情况填） |
| TestFlight | 上传后先内测；重点测相机扫码、本地网络、后台/锁屏 |
| 提审 | **单独提审**，不要和电台/电视同批 |

---

## 14. Archive 之后怎么填（按顺序）

> 你手动 archive 之后照这张表走。**App Record 必须先存在，才能上传构建**；
> 如果还没建，先建 Record（名称/主要语言/Bundle ID/SKU），再上传 archive。

1. **Xcode Organizer**：Archive → Distribute App → App Store Connect → Upload。
   版本 `1.0`，build `1`（或自增）；等 ASC 处理完成。
2. **TestFlight**：内部测试装一台真机，逐项过：后台/锁屏、拔耳机暂停、
   电话打断、相机扫码、局域网服务器搜索/播放/分享。真机项不过，先别提交。
3. **App Record**（若未建）：名称「牧云音乐」、主要语言简体中文、
   Bundle ID `com.gezhipeng0201.MuYunMusic`、SKU `muyunmusic-20261103`、
   类别 音乐/工具、版权 `2026 Zhipeng Ge`。
4. **版本信息**：复制 §1 推广文本、§2 描述、§3 副标题、§4 关键词；
   §5 的隐私/支持 URL；价格/销售范围按 §0。
5. **截图**：先传 6.9" iPhone 四张，再传 13" iPad 四张；都按 `01 → 04` 顺序，§7 是连续全景切片。
6. **App 隐私**：选 No data collected；填隐私政策 URL；确认相机/本地网络
   不是「收集」。
7. **年龄分级**：按 §12 全 None/No，结果 4+。
8. **内容版权**：DOES_NOT_USE_THIRD_PARTY_CONTENT。
9. **审核信息**：联系人/电话/邮箱；演示账号留空；备注粘贴 §9 英文版。
10. **构建**：选择刚上传的 build；出口合规选「否/NO」（已在 plist）。
11. **What's New**：粘贴 §15。
12. **提交**：单独提交，不要跟家族其他 app 同批。
13. **被问 ATS/相机/本地网络**：直接引用 §9 的三类网络、权限与 ATS 段落，
    不要临场改口径。

---

## 15. 版本 1.0 的「新增内容」(What's New)

```
首个版本：本地导入与播放、lrc 与内嵌歌词、收藏与最近播放、歌单与队列、
后台与锁屏控制、Wi-Fi 传歌、自填家庭影音服务器。0 统计 0 广告 0 账号，
数据全本机。
```
