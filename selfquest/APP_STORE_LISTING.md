# 自律勇者 (SelfQuest) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。
> **这份素材刻意没有任何差异化或效果主张，理由见第 8 节。改文案之前先读那一节。**

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **自律勇者** | 习惯打卡、番茄钟、自律（通称易被占） |
| 名称（English 本地化） | **SelfQuest** | Habit Tracker、Pomodoro |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.SelfQuest` | 任何旧 ID |
| SKU | `selfquest-20261009` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「自律勇者」。

备选店名（创建时报名被占再用）：

- 自律勇者养成
- 勇者打卡
- SelfQuest Habits

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

**注意：App 本身没有任何本地化。** 工程里 `developmentRegion = zh-Hans`，但**没有 `.xcstrings`、没有 `.strings`、没有 `.lproj`**，
`Views/` 下的用户可见字符串全是中文硬编码。所以如果给 English 也建一份商店本地化，
英文用户看到的是「英文描述 + 中文界面」。要么这轮只上简体中文，要么等界面做完英文化再补。

**内外一致性有一条硬伤，上架前必须先改掉，见第 9 节第 1 条。**

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
打卡和专注都给经验和金币，金币可以买装备穿在角色身上。全本地，不联网，没有账号，也没有排行榜。
```

**字符数：47 / 170**

### English

```
Check-ins and focus sessions earn XP and gold you can spend on gear your hero wears. Fully local: no account, no network, no leaderboards.
```

**字符数：138 / 170**

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
自律勇者把坚持做成一个有角色、有等级、有装备的游戏。

打卡和专注都会给经验与金币。经验涨等级，金币买装备，装备穿在角色身上。
没有排行榜、没有社交压力、不需要联网，也不需要注册任何账号。

【习惯打卡】
- 自定义名称、图标和颜色
- 三种重复方式：每天、工作日、周末
- 连续打卡有连击加成，封顶 2 倍
- 工作日习惯跳过周末不算断
- 支持补卡，往回最多 7 天
- 当天点错了可以撤销，退回原额的经验与金币
- 暂时不想做的可以归档，历史记录保留

【番茄钟】
- 15 / 25 / 45 / 60 分钟预设
- 也支持不限时的正计时，进度圈到 90 分钟为止
- 完成给全额奖励
- 中途结束按 40% 折算经验，且不给金币
- 专注满 5 分钟才计入，避免开关刷分

【角色养成】
- 经验等级曲线，升级有反馈
- 9 件装备，分武器 / 护甲 / 饰品三个槽位，穿在身上会改变角色的显示
- 装备有等级门槛，攒够了才能穿
- 装备里只有一件会真的影响行为：番茄钟开始时响一声提示音；其余是外观与收藏
- 11 个成就，覆盖打卡、连击、专注、收集

【统计】
- 打卡热力图，一眼看到坚持的密度
- 打卡率、打卡次数、专注时长、当前连击
- 专注柱状图最多显示最近 14 天，与所选范围无关
- 习惯排行按全部历史打卡次数计算，同样不受范围影响
- 范围选项：本周 / 近 30 天 / 近 90 天

【数据是你自己的】
- 没有账号，App 也不发起任何网络请求，飞行模式下全部功能可用
- 不要任何权限，包括通知：它不会提醒你打卡
- 全部记录只写在这台设备的沙盒里
- 可导出 JSON 完整存档与 CSV 打卡明细
- 导出是单向的：这个版本没有导入功能，导出的文件不能读回 App
- 删除 App 即清除全部数据

【系统要求】
需要 iOS 17.0 或更高版本。iPhone 上仅竖屏，iPad 上四个方向都支持。界面为中文。
```

**字符数：830 / 4000**

### English

```
SelfQuest turns consistency into a game with a character, levels, and gear.

Check-ins and focus sessions both earn XP and gold. XP raises your level, gold buys equipment, and your hero wears it. No leaderboards, no social pressure, no network required, and no account to create.

[Habits]
- Custom names, icons, and colours
- Three schedules: daily, weekdays, weekends
- Streaks boost the reward per check-in, capped at double
- A weekday habit skips the weekend without breaking
- Backfill a missed day, up to 7 days back
- Tap again the same day to undo, returning the exact XP and gold
- Archive a habit you are pausing, keeping its history

[Focus timer]
- Presets for 15, 25, 45, and 60 minutes
- A count-up mode with no limit, its ring full at 90 minutes
- Completing a session pays in full
- Stopping early pays 40 percent of the XP and no gold
- Five minutes minimum, so toggling it on and off earns nothing

[Character]
- An XP curve with feedback at every level
- Nine pieces of equipment across weapon, armour, and accessory slots, changing how your hero is drawn
- Level requirements, so gear unlocks as you progress
- Only one item affects behaviour at all, playing a tone when a focus session starts; the rest are appearance and collection
- Eleven achievements covering streaks, focus time, and collecting

[Statistics]
- A check-in heatmap that shows the density of your effort
- Completion rate, total check-ins, focus minutes, current streak
- The focus bar chart shows at most the last 14 days, whatever range is selected
- The habit ranking counts every check-in ever made, also ignoring the range
- Ranges: this week, 30 days, 90 days

[Your data stays yours]
- No account, no network requests at all, everything works in Airplane Mode
- No permissions of any kind, notifications included: it will not remind you
- Everything is stored in this device's sandbox
- Export a full JSON save or a CSV of check-ins
- Export is one-way: this version has no import, and the file cannot be read back
- Deleting the app clears all of it

[Requirements]
iOS 17.0 or later. Portrait only on iPhone; all four orientations on iPad. The interface is in Chinese.
```

**字符数：2168 / 4000**

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
打卡专注，养成勇者
```

**字符数：9 / 30**

### English

```
Habits, focus, and a hero
```

**字符数：25 / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
打卡,习惯,番茄钟,专注,自律,养成,等级,成就,连击,离线
```

**字符数：30 / 100**

### English

```
habit,tracker,pomodoro,focus,streak,rpg,level,achievement,offline,goal
```

**字符数：70 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/selfquest/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/selfquest/privacy.html` |
| 营销 URL | 留空 |

技术支持是**版本级**字段（改它要跟新版本一起提审），隐私政策是 **App 级**（要有待发版本才能改）。
这两个 URL 一旦提审就不好改了，提审前先确认目录名。

**营销 URL 是可选字段，这里刻意留空。** 原来的草案填的是 `https://zhipengge.github.io/apps/selfquest/`，
但 `apps/selfquest/` 下**没有 `index.html`**，填了就是 404
（同目录的 `apps/muyuntv/` 和 `apps/weedit/` 有落地页，所以那两个能填）。要填就先补一个落地页，否则留空。

---

## 6. 类别、评级、隐私问卷

| 字段 | 建议 |
|---|---|
| 主要类别 | 效率 / Productivity |
| 次要类别 | 健康健美 / Health & Fitness |
| 内购 | **无**。工程里 grep 不到一个 `StoreKit` 符号，也没有商品 ID；商店里花的是打卡挣的金币，不是钱 |
| 年龄分级 | 4+ |
| App 隐私 | **不收集数据**。须与本目录的 `privacy.html` 一致 |
| 出口合规 | **NO**（`INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO` 写在工程里；App 里没有任何加密代码，也没有网络栈） |

审核备注建议写清：本 App 为纯本地工具，不运营服务器、不发起任何网络请求，全部数据保存在设备沙盒内的一个 JSON 文件里。
无账号体系，无内购，无广告。**不申请任何权限**，包括通知权限。
设置页里的三个外链（隐私政策 / 使用帮助 / 反馈）由系统浏览器打开，App 自身不请求它们。

**年龄分级这一条是明确的。** App 内没有任何用户生成内容的分享、没有社区、没有浏览器、没有外部内容入口，
4+ 是如实填写而不是求好看。

---

## 7. 截图

`TARGETED_DEVICE_FAMILY = "1,2"`，iPhone 与 iPad 两套都要，各 3-10 张。

### 已经有的：iPhone 6 张

`apps/selfquest/screenshots/iphone/` 下 6 个文件，本轮已核过尺寸，**全部 1320 x 2868**（iPhone 6.9 寸那一档）：

| 文件 | 内容 |
|---|---|
| `01-quest.png` | 冒险页：今日待办与打卡 |
| `02-done.png` | 全勤状态 |
| `03-focus.png` | 专注计时中 |
| `04-hero.png` | 角色与装备商店 |
| `05-stats.png` | 统计热力图 |
| `06-settings.png` | 设置 |

### 还缺的：iPad 一整套

**目前一张 iPad 截图都没有**，`screenshots/` 下没有 `ipad/` 目录。
iPad 这一套是 13 寸，**2064 x 2752**，3-10 张。这是提交前的硬缺口。

### 两张图有内容问题，拍之前先看

- **`06-settings.png` 会拍到「关于」卡片**，而设置页里那一行导出说明写着「完整存档，换手机时用它恢复」——
  与本版本的真实行为不符（详见第 9 节第 1 条）。**这一行没改掉之前，这张截图最好重拍或裁掉那一块**，
  否则截图本身就在展示一句不实的功能承诺。
- 补卡面板里有一处 `Text("+{habit.xpReward} XP")` 少写了插值，屏幕上会**字面显示** `+{habit.xpReward} XP`
  （`QuestView.swift:356`）。要拍补卡流程就先把这一行修掉。

竖屏截图，不要裁成横版。空状态、纯海报式截图会被拒。

---

## 8. 这份素材里，哪些卖点是被故意排除的

**这一节比前几节重要。改文案之前请先读完。**

### 先说结论：作者自己写了「从代码里找不到站得住的差异点」

`SelfQuest/AGENTS.md` 的「差异化：这个 app 凭什么存在」一节，第一行逐字：

> **结论：从代码里找不到站得住的差异点。**

那一节的表格把五个候选差异点逐条否掉了，原文照抄：

| 候选差异点 | 作者自己的结论 |
| --- | --- |
| 游戏化（XP / 等级 / 金币 / 装备 / 成就） | 竞品是它的几十倍，**内容量上它是弱的一方** |
| 装备会改变行为 | 9 件里只有 1 件真的影响程序行为 |
| 本地优先、无账号、不联网 | 免费 app 里很常见，是加分项不是换机理由 |
| 打卡 + 番茄钟 + 统计三合一 | 这是品类入场券，拆开看每项都有更深的免费实现 |
| 7 天补卡 | 竞品就有；这是**对齐**品类标准，不是领先 |

作者在那一节末尾还写了一句适用范围更广的话，逐字：

> **要造出一个站得住的差异点，要动的是产品，不是数值。** ……
> 在那之前，**任何「本作差异点是 X」的写法都是在编**——
> 宁可这一节一直写着「找不到」，也不要写一条经不起对照的卖点。

**所以这份素材里没有一句「比同类强」。** 全篇只描述这台 App 自己做了什么。

### 排除项一：装备的效果——写成事实，不写成卖点

作者对装备的原话是「**花金币买装备 ≈ 换图标，玩法一模一样**」，
并进一步写了「一个只在视觉上存在的成长系统，撑不起「比免费的强」这个判断」。

素材里的处理：

- 描述里**照实写**装备存在、有三个槽位、穿上会改变角色显示、有等级门槛——因为这些用户看得见，也是真的
- 并且**主动写清**「只有一件会真的影响行为，其余是外观与收藏」
- **一个字都没有**「装备让你变强」「收集装备提升体验」「成就感拉满」之类的结论

这样写比含糊带过更好：含糊会让用户买了七件没有任何作用的装备才发现，那才是真的欺骗。

### 排除项二：任何「比免费的强」——不写

作者点名了竞品（免费且更完整的游戏化打卡已存在多年）。素材里**没有出现任何竞品名或品类比较**，
也没有「更轻量」「更专注」「没有社交压力所以更好」这类相对评价。
「没有排行榜、没有社交压力」保留下来了，因为那是**对自己的描述**（App 里确实没有排行榜），
不是对别人的评价。

### 排除项三：¥28 与内购——完全不提

`AGENTS.md` 把「StoreKit 2 内购（免费版 3 个习惯 + 基础番茄钟；¥28 解锁完整版）」列成待办，
并注了一句「**在差异点成立之前不该做**」。代码里没有 StoreKit，没有付费墙，没有习惯数量上限。
所以：**这份素材里没有价格、没有免费版/完整版的区分、没有内购**。商店里花的是金币，不是钱，描述里也写明了这一点。

### 排除项四：通知——不承诺，反而要主动否认

这是一个习惯打卡 App，用户会默认它一定有提醒。代码里 `UserNotifications` 是 **0 匹配**，
一次通知权限都没申请过。所以描述和 FAQ 里都**主动写明「它不会提醒你打卡」**。
这不是缺点陈述，而是必须说清的事实：不说，用户会以为功能坏了。

### 排除项五：范围筛选与「最长连击」——写清边界，不写成覆盖面

旧文案写「支持本周 / 近 30 天 / 近 90 天」，读起来像所有统计都跟着变。代码里不是：
专注柱状图写死 `min(range.days, 14)`，习惯排行按全部历史计算，而「最长连击」卡片显示的是当前连击。
三条都已按实际行为改写。**没有把它们包装成「多维度统计」之类的说法。**

### 用掉的（每条都能在代码里指出位置）

| 卖点 | 代码依据 | 用在哪 |
|---|---|---|
| 五种重复方式与连击规则、封顶 2 倍 | `GameLogic.swift:45-93`、`:186-192` | 描述、FAQ |
| 补卡 7 天、从早到晚 | `GameLogic.swift:119`、`:161-180` | 描述、FAQ |
| 撤销退回原额 | `AppState.swift:150-159` | 描述、FAQ |
| 番茄钟预设与正计时（圈满于 90 分钟） | `FocusView.swift:24`、`:79-80`、`:181-197` | 描述、FAQ |
| 中途结束 40% 经验且 0 金币、满 5 分钟才计入 | `GameLogic.swift:196-203` | 描述、FAQ |
| 9 件装备 / 3 槽位 / 等级门槛、仅 1 件影响行为 | `BuiltIn.swift:28-52`、`FocusView.swift:251` | 描述、FAQ |
| 11 个成就 | `BuiltIn.swift:60-72` | 描述 |
| 等级曲线与升级反馈 | `GameLogic.swift:18-21`、`ContentView.swift:78-148` | 描述 |
| 统计三个范围与实际边界 | `StatsView.swift:17-29`、`:70`、`:147-148`、`:197-204` | 描述、FAQ |
| 一个 JSON 文件、未加密纯文本、无 UserDefaults / 钥匙串 / iCloud | `Store.swift:17-32` | 隐私政策、FAQ |
| 零网络请求、飞行模式全可用 | 无网络框架链接、`nm -u` 无网络符号、三个 `Link` 字面量 | 全篇 |
| 零权限（含通知） | 零 `*UsageDescription`、`UserNotifications` 0 匹配 | 描述、FAQ、隐私政策 |
| 导出单向、无导入 | `AppState.swift:293-310` 只有导出；`fileImporter`/`onOpenURL` 等 0 匹配 | 描述、FAQ、隐私政策 |
| 导出副本留在临时目录、损坏存档留 `.corrupt-` 副本 | `AppState.swift:293` 附近、`Store.swift:53-58` | 隐私政策、FAQ |

**没有引用任何竞品名或品类名，也没有引用任何测试数量**（`AGENTS.md` 里的测试条数本轮没有重跑，所以一个字都没用）。

---

## 9. 提审前必须先解决的六件事（第 1 件不是文案问题）

1. **App 内有一句不实的功能承诺，必须改源码。** `Views/SettingsView.swift:54` 的导出说明写着
   「完整存档，换手机时用它恢复」，但代码里**只有导出、没有导入**（`AppState.swift` 只暴露
   `exportJSONURL()` 与 `exportCSVURL()`；grep `fileImporter` / `UIDocumentPicker` / `onOpenURL` / `UTType`
   在全部 `*.swift` 里 0 匹配；生成的 `Info.plist` 里没有 `CFBundleDocumentTypes`）。
   本轮的商店与政策文案已经**全部改成「导出是单向的、这个版本没有导入」**，
   于是这句 App 内文案现在**和外面的说明直接矛盾**，而截图 `06-settings.png` 会把它拍进去。
   两条路：要么把这句话改掉（推荐，成本一行），要么真的做一个导入。**改源码这件事本轮没有做。**
2. **iPad 截图一整套都没有。** 见第 7 节。`TARGETED_DEVICE_FAMILY = "1,2"`，这一套是必填。
3. **补卡面板有一处显示 bug。** `QuestView.swift:356` 的 `Text("+{habit.xpReward} XP")` 少写了插值，
   屏幕上字面显示 `+{habit.xpReward} XP`。`AGENTS.md` 里已经记为已知问题，本轮核查确认它还在。
4. **English 商店本地化与中文界面不匹配。** 见第 0 节末。要么补界面英文化，要么这轮只上中文。
5. **营销 URL 留空或先补 `index.html`。** 见第 5 节。
6. **价格还没定。** 素材里没有写任何价格，代码里也没有内购。按你自己记的结论（已上架 app 全 0 评分，
   瓶颈是曝光不是价格），这个 App 也应该是免费上架。
