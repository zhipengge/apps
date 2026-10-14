# 沟通副本 (TalkQuest) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **沟通副本** | 职场沟通、沟通训练（通称易被占） |
| 名称（English 本地化） | **TalkQuest** | Talk Quest、Communication Quest |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.TalkQuest` | 任何旧 ID |
| SKU | `talkquest-20261012` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「沟通副本」。

备选店名（创建时报名被占再用）：

- 沟通副本 TalkQuest
- 沟通副本 对话练习
- 沟通副本 职场对话

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

**注意：App 本身没有任何本地化。** 工程里没有 `.lproj`、没有 `Localizable.strings`、也没有 `.xcstrings`，
四个页签和 24 段对话全部是中文硬编码（`Views/` 下直接写 `Text("...")`）。
所以如果给 English 也建一份商店本地化，英文用户看到的是「英文描述 + 中文界面」。
要么这轮只上简体中文（主要语言就是它），要么等界面做完英文化再补 English 本地化。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
先读对方的话，再选一个回应，然后才出现反馈卡：这一选在对方听来是什么效果、动了哪几个维度、以及为什么。24 段职场对话，全程离线，没有账号。
```

**字符数：70 / 170**

### English

```
Read the other person's line, choose a reply, and only then does the feedback card appear: how it landed, which axes it moved, and why. 24 offline scenarios.
```

**字符数：157 / 170**

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
沟通副本是一个离线的对话练习工具。24 段职场对话，分成 10 个分类：面试、谈薪、谈判、拒绝、职场关系、跨团队、社团社交、实习、向上管理、带人。一共 193 个决策点、579 个可选回应、72 个结局。内容全部随 App 打包，不联网也能用。

【三步，一步都不能跳】
先读对方说的话，再选一个回应，然后才出现反馈卡。反馈卡告诉你三件事：这一选在对方听来是好还是差、它动了哪几个维度、以及为什么。
它不能在你选之前出现，也不能被你划过去。这份解释就是全部意义所在。

【分数是算出来的，不是估计出来的】
每一步都已经决定了它对五个维度的加减，走到最后按总分给结局。同一个选择序列永远得到同一条反馈和同一个分数。
这不是一句宣传，是一条会被断言的规则：逻辑测试里就是把整局走完，再断言分数和结局。

【五个维度，一条能力画像】
共情、边界感、表达清晰、情绪管理、策略性。每一步的反馈卡都会指出它动了哪几个维度、动了多少。
能力页把五个维度摊平显示，配上总进度和最好、最弱的那一维。没练过的维度显示的是「未练到」而不是 0 分，因为没练过和练砸了是两回事。

【结局不是对错，是三档】
处理得漂亮 / 过关，但有遗憾 / 这段关系被你推远了。
结算页会把每一回合重新摊开给你看：你当时选了什么，对方听来是什么效果。

【风格测试】
12 道题，48 个选项，答完自动保存。结果是五个原型里的一个：暖流型、界碑型、直球型、定海型、棋手型，外加五个维度的百分比拆解。

【579 个可选回应全部是人工写的】
没有一句是生成的，也没有一段对话是拼出来的。同品类里因为生成内容里角色和台词对不上而被骂的例子不少，人工写是唯一能保证每一句都说得通的办法。

【15 个成就】
从第一次开口，到把一整类场景都练到老练。成就记的是你实际做过的事，不是打卡天数。

【隐私与数据】
- 不收集任何数据，App 不发起任何网络请求，飞行模式下全部功能可用
- 没有账号，不需要注册或登录
- 没有广告，没有内购：24 段对话从第一次打开起就全部可用
- 没有分析、崩溃上报或追踪 SDK，工程里没有任何第三方依赖
- 不申请任何系统权限，系统不会为它弹出任何权限询问
- 进度只存在这台设备的沙盒里，删除 App 即清空；也能随时导出成 JSON 或 CSV 自己带走

【系统要求】
需要 iOS 17.0 或更高版本。iPhone 与 iPad 均可，iPhone 上仅支持竖屏。界面为中文。
```

**字符数：1038 / 4000**

### English

```
TalkQuest is an offline conversation practice tool. 24 workplace conversations across 10 categories: interviews, raises, negotiation, refusing, workplace relationships, cross-team work, club socialising, internships, managing up, and managing people. 193 decision points, 579 selectable replies and 72 endings in total. Everything ships inside the app and works with no connection at all.

[Three steps, and none can be skipped]
Read what the other person said, choose a reply, and only then does the feedback card appear. It tells you three things: whether the choice landed well or badly, which axes it moved, and why.
It cannot appear before you choose and it cannot be swiped away. That explanation is the entire point.

[The score is calculated, not estimated]
Every step already fixes what it adds to or subtracts from the five axes, and the ending is chosen from your total. The same sequence of choices always produces the same feedback and the same score.
That is not a slogan, it is an asserted rule: the tests play a full run and then assert the score and the ending.

[Five axes, one skill profile]
Empathy, boundaries, clarity, emotional regulation and strategy. Each feedback card tells you which axes your choice moved, and by how much.
The Skills tab lays all five out flat with your overall progress and your strongest and weakest axis. An axis you have never practised reads "not practised yet" rather than 0 percent, because never having tried and having tried badly are different things.

[The ending is not right or wrong, it is one of three tiers]
Handled beautifully / passed, with regrets / you pushed this relationship away.
The result screen reopens every round for you: what you chose, and how it sounded on the other side.

[Style test]
12 questions with 48 options, saved automatically when you answer the last one. The result is one of five archetypes: Warm Current, Boundary Stone, Straight Ball, Anchor and Strategist, plus a five-axis percentage breakdown.

[All 579 replies are written by hand]
Not one line is generated and no conversation is stitched together from fragments. In this category there are well-known examples of generated content where characters and lines do not match up, and writing by hand is the only way to be sure every line holds together.

[15 achievements]
From your first line to taking a whole category to expert. Achievements record what you actually did, not how many days in a row you opened the app.

[Privacy and data]
- Collects nothing and makes no network requests; every feature works in Airplane Mode
- No account, nothing to register or sign in to
- No ads and no in-app purchases: all 24 conversations are available from the first launch
- No analytics, crash reporting or tracking SDKs, and no third-party dependencies at all
- Requests no permissions, so the system never prompts you
- Progress lives in the app sandbox and deleting the app clears it; you can also export it as JSON or CSV at any time

[Requirements]
iOS 17.0 or later. iPhone and iPad. Portrait only on iPhone. The interface is in Chinese.
```

**字符数：3083 / 4000**

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
离线对话练习，每步都有解释
```

**字符数：13 / 30**

### English

```
Offline conversation practice
```

**字符数：29 / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
职场,对话练习,情商,表达技巧,拒绝,谈判,面试,谈薪,离线,单机
```

**字符数：33 / 100**

### English

```
workplace,communication,role play,soft skills,interview,negotiation,offline,no ads,scenarios
```

**字符数：92 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/talkquest/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/talkquest/privacy.html` |
| 营销 URL | 留空 |

技术支持是**版本级**字段（改它要跟新版本一起提审），隐私政策是 **App 级**（要有待发版本才能改）。
这两个 URL 一旦提审就不好改了，提审前先确认目录名。

营销 URL 是可选字段，`apps/talkquest/` 下没有 `index.html`，填了就是 404，所以留空。

**这两个页面现在还是 404。** `apps/` 是独立仓库 `zhipengge/apps`，Pages 已经开着
（`apps/skystrike/privacy.html` 现在返回 200），但 `apps/talkquest/` 还没进版本库。
提审前必须先提交并推送这一整个目录，否则 App Store Connect 填的隐私政策链接是空的。

---

## 6. 类别、评级、隐私问卷

### 类别（需要你定，两个都列出来）

**2026-10-14 定：原方案 A。**

| 字段 | 值 |
|---|---|
| 主要类别 | **教育 / Education** |
| 次要类别 | 生活方式 / Lifestyle |

（选 A 的理由：五个维度的能力画像、可解释的评分、风格测试都指向「练习与自我评估」，
同类工具多归在教育。原方案 B「娱乐 / 教育」见 git 历史。
改成这两行是因为工具只认表格行——原来那张「选项 A/B」表它是当**候选题**读的，
会一直报「必须人选定一个」。）

`TARGETED_DEVICE_FAMILY = "1,2"`，主要类别只能选一个。

### 年龄分级（需要你定）

问卷不让你直接选档位，是按题作答后由 Connect 判定。当前档位是 4+ / 9+ / 13+ / 16+ / 18+ 五档。
这个 App 的实际情况：全部是虚构的职场对话，没有战斗、没有血腥、没有恐怖，也没有赌博、酒精烟草毒品、
色情、用户生成内容、聊天、广告或网页浏览。它不联网，用户也不能输入任何自由文本。

**需要你实际核一遍的两项**（本轮只做了抽查，没有逐条读 579 行）：

| 题目 | 情况 |
|---|---|
| 脏话或粗俗幽默 | 我用 `他妈的 / 滚 / 闭嘴 / 白痴 / 蠢 / 傻 / 混蛋 / 屁话 / 废物 / 神经病 / 去死 / 见鬼` 扫了 11 个场景 JSON，**零处脏话**（两处命中都是误报：一处是「网贷利息会滚」，一处是反馈文案里的「我当时怎么那么傻」）。但这是关键词扫描，不是逐条读完 579 行，**报这道题之前建议你自己再过一遍「拒绝」「谈判」这两个分类** |
| 成熟或暗示性主题 | 24 段都是职场往来，没有恋爱或性相关内容 |

**另一个时间点要注意：** 苹果要求所有开发者在这轮问卷更新里重新作答，**2026 年 1 月 31 日之后没作答的 App 无法提交更新**。这一条跟本作是否上架无关，只要还想发版本就得先过。

### 其余表

| 字段 | 建议 |
|---|---|
| 内购 | **无**。代码里没有任何 StoreKit，也没有付费入口，App 完全免费。详见第 7 节 |
| App 隐私 | **不收集数据**。App 不发起任何网络请求，须与 `privacy.html` 一致 |
| 出口合规 | **NO**。`INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO` 已经写在工程里，App 完全没有加密，也没有网络代码 |

审核备注建议写清：本 App 完全离线，不发起任何网络请求，不收集任何数据，无账号、无广告、无内购，
也不申请任何系统权限。没有语音识别也没有录音，全部为文字选择题，没有自由输入框。
iPhone 仅竖屏，iPad 支持四个方向。

---

## 7. 内购与定价：代码里没有内购，文档里有，以代码为准

**全工程 grep `StoreKit` / `Product.products` / `SKPayment` 零命中。** 唯一的出现是
`LogicTests/run.sh:38,40` 里的一条**反向守卫**：如果 `Shared/` 里出现 `import StoreKit`，逻辑测试就失败。
`AGENTS.md:69` 写得很直白：「没做内购。」

也没有付费墙、没有解锁码、没有登录注册。`Views/LibraryView.swift:22` 直接遍历全部分类，
**24 段对话从第一次打开起就没有任何门禁**。

**⚠️ 计划文档里有一套并不存在的东西，一个字都不能写进 Connect。**
`app开发列表1009.md:301-307` 写着「免费下载，3 个基础场景」加「一次性内购 ¥38 解锁完整版」，
早鸟价 ¥28。**这套东西没有实现**：没有 3 场景免费档，也没有内购。
`定价策略.md` 里根本没有列 TalkQuest 这一行，但仓库通行的规则是
「靠 App Store 内部分发的（iOS 应用）免费」——所以**当前就是免费无内购**。

**提审前需要你确认一件事**：这份素材按「免费下载 + 无内购」写的，
描述里也明写了「没有内购：24 段对话从第一次打开起就全部可用」。
如果之后要加内购，这句话必须跟着改。**但只要你不动代码，它就是真的。**

---

## 8. 截图

`TARGETED_DEVICE_FAMILY = "1,2"`，iPhone 与 iPad 两套都要，各 3-10 张。
**目前 `apps/talkquest/` 下还没有 `screenshots/`。** 工程里的 `TalkQuest/Screenshots/` 有 66 张验证截图，
但那个目录被 `.gitignore:12` 忽略，而且 `.gitignore:10-11` 自己写着「**商店截图不放这儿**——按约定进 apps/talkquest/」。

按 Apple《截屏规范》（Screenshot specifications，2026-10-12 核对原文），**必填的只有两档**：

- iPhone：**带灵动岛的 iPhone（中等显示屏）**，竖屏 1206 x 2622 或 1179 x 2556
- iPad 13 寸，竖屏 2064 x 2752

6.9 寸（带灵动岛的 iPhone，大显示屏，1320 x 2868）不是必填。

工程里已有的验证截图正好是 1206 x 2622（iPhone）和 2064 x 2752（iPad），尺寸对得上，
但不能直接当商店截图用：它们是为了验证功能而拍的，界面状态未必好看，而且没有配文案。

竖屏截图，不要裁成横版。空状态、纯海报式截图会被拒。

建议的六张（标题与副标题都只讲界面上真实存在的东西，**刻意不写任何「提升沟通能力」式的效果宣称**——
仓库里没有任何效果测量，所有「实测」记录都是「某个界面 bug 被真机测出来过」，
`竞争力审计.md:35-60` 也明确写了「机制在代码里成立」不等于「已经比过竞品」）：

| 文件 | 标题 | 副标题 | 对应界面 |
|---|---|---|---|
| `01-library.png` | 24 段职场对话 | 面试、谈薪、谈判、拒绝，10 个分类 | 场景页 |
| `02-play.png` | 先选，再看到解释 | 反馈卡在你选之前不会出现 | 对局页，反馈卡展开 |
| `03-feedback.png` | 它动了哪几个维度 | 每一步都告诉你为什么 | 反馈卡，维度条 |
| `04-result.png` | 结局不是对错，是三档 | 每一回合都能重新摊开看 | 结算页 |
| `05-skills.png` | 没练过，就写没练过 | 未练到的维度不显示成 0 分 | 能力页 |
| `06-scheme.png` | 12 道题，五个原型 | 暖流型、界碑型、直球型、定海型、棋手型 | 风格测试结果页 |

---

## 9. 这份素材里，哪些卖点是被故意排除的

诚实起见记一笔。`TalkQuest/AGENTS.md` 里没有标题为「差异化：这个 app 凭什么存在」的一节，
对应的是 **§9 参考实现与差异点** 和 **§9.5 结论：原创性来自哪里**。
§9.5 给的差异点是「离线、免注册、秒级反馈、结果完全确定」，并且自己注明
「**这一条是可验证的**：逻辑测试里就是把整局走完再断言分数和结局」。

**用掉的部分：**

| 差异化条目 | 代码依据 | 用在哪 |
|---|---|---|
| 结果完全确定，同一条选择序列永远同一个分数 | `Shared/Runner.swift`、`LogicTests/main.swift`（整局走完再断言） | 推广文本、描述、副标题、FAQ、截图 02 |
| 每一步都给可解释的反馈，不是「正确 / 错误」 | `Views/PlayView.swift` 反馈卡三步不可跳、`Runner.swift:74-85` | 描述、FAQ、截图 02/03 |
| 离线、免注册、无账号 | 四个 import、零网络符号、`otool -L` 无网络框架 | 全篇、FAQ |
| 579 个选项全部人工写 | `Resources/scenario-*.json`，`AGENTS.md` 三条设计纪律第 1 条 | 描述、FAQ |
| 未练到的维度显示「未练到」而不是 0 分 | `Views/SkillTreeView.swift:176` | 描述、FAQ、截图 05 |

**故意没用的：**

- **「提升你的沟通能力」这类结果宣称一个字都没有。** 仓库里没有任何效果测量；
  所有标着「实测」的地方说的都是「某个界面 bug 在真机上被测出来过」。
  所以全篇只描述机制（离线场景练习、每一步有解释、五个维度成像），不承诺结果。
- **「微信分享」没有写。** `app开发列表1009.md:279,309-313` 承诺了分享卡片和朋友圈，
  但**代码里没有微信 SDK**（零依赖、零 SPM 包），实际是 iOS 系统 `ShareLink` 发**一段纯文本、不带图片**
  （`Views/StyleTestView.swift:15-16` 自己就写着「分享用 ShareLink 发一段纯文本，不带图片」）。
- **「分支剧情」没有当成卖点。** `AGENTS.md:66` 明确写着 24 段场景**全部是线性的**，
  分支能力只存在于引擎和测试里，随 App 打包的内容一次都没用。
  描述里写的是「结局由总分决定，分三档」，这是代码事实；线性的实情写在 `support.html` 的 FAQ 里。
- **「¥38 解锁完整版」「3 个基础场景免费」没有写。** 那是计划文档里的东西，代码里没有。
- **没有引用任何竞品名或品类名**，关键词里也没有。全部文案为本作原创。
- **没有把「15 个成就」写成驱动力。** 描述里只说明它记的是实际做过的事，
  没有写「上瘾」「每天回来」这类留存话术。
