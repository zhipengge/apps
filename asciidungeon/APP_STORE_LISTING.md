# 字符地牢 (AsciiDungeon) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **字符地牢** | 地牢、roguelike（通称易被占） |
| 名称（English 本地化） | **AsciiDungeon** | Ascii Dungeon Roguelike、Rogue |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.AsciiDungeon` | 任何旧 ID |
| SKU | `asciidungeon-20261012` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「字符地牢」。

备选店名（创建时报名被占再用）：

- 字符地牢 roguelike
- 一屏地牢
- AsciiDungeon 字符地牢

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

**注意：App 本身没有任何本地化。** 工程里没有 `.lproj`、没有 `Localizable.strings`、也没有 `.xcstrings`，
`knownRegions` 里虽然列着 `en`，但那是 Xcode 的默认值，实际界面文案全是中文硬编码。
所以如果给 English 也建一份商店本地化，英文用户看到的是「英文描述 + 中文界面」。
要么这轮只上简体中文（主要语言就是它），要么等界面做完英文化再补 English 本地化。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
屏幕上方永远有一行读数，打之前就告诉你这一架打不打得过，而且那几个数就是真掷骰子时用的那几个。点一下走一步，10 层地牢，全程离线，没有广告也没有内购。
```

**字符数：76 / 170**

### English

```
A readout above the map says whether a fight is winnable before you take it, and those are the numbers the dice actually use. Tap to move, 10 floors, fully offline.
```

**字符数：164 / 170**

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
字符地牢是一款竖屏回合制 roguelike。一屏字符画，10 层地牢，点一下走一步。全程离线，没有账号，没有广告，没有内购。

【操作】
- 点地图上的任意一格，你会自动走过去，中途看见醒着的怪就停下来把决定权还给你
- 点地移动只走你已经探索过的路，一次点击不能替你把没去过的区域试探出来
- 朝一个方向划一下就走一步，八个方向
- 走进怪物所在的格子就是攻击它，没有单独的「攻击」键
- 自动：走到未探索区域的边界，看见怪就停
- 下楼：站在楼梯上时才亮起来，地牢只能往下走

【屏幕上方那行读数】
视野里出现怪物时，屏幕上方会告诉你这一架打不打得过：
打得过 / 势均力敌 / 打不过 / 它会杀了你。
点一下读数条可以展开，看到双方的命中率和伤害区间，在打之前自己核对。

这几个数就是真掷骰子时用的那几个，不是另外估的一份。

【规则是算得清的】
命中率：55% 加上每点命中 5%，再减对方闪避，夹在 5% 到 95% 之间。
伤害：骰子区间加力量加等级加成，再减对方护甲，至少 1 点。
速度：很慢、正常、很快、极快四档，也就是你的 0.5 倍、1 倍、1.5 倍、2 倍。
背包页把命中和伤害直接列出来，旁边就写着这条公式，装备对比用上下角标标出强弱。

你永远先看见它：视野半径 8 格，怪物的警觉半径 6 格，不会被看不见的东西偷袭。
打不过就往回退两步等一等，每 12 个回合自动回 1 点血。

【没见过的怪，读数只说未知】
见过的怪会记进图鉴，之后它出现在视野里就有完整读数；没见过的画成紫色，读数对它只说「未知」。
所以第一次遇到一只怪，正确做法是先活下来，看清它怎么打人。

【10 层地牢】
每一层都由一颗随机种子长出来，房间加走廊，连通性从构造上就成立，不会出现走不通的死图。
同一颗种子永远长出同一张图，存档里存的就是这颗种子，所以「第 5 层还是那一张」在重开之后也成立。
第 10 层的深渊之门由 Ω 守着，打赢它、站上楼梯、按「下楼」，这一局就算通关。

【死了会怎样】
等级清零，从第 1 层重新开始。
你手上的武器、身上的甲和包里前 6 件会留在你倒下的那一层，画成一个 %，下一局走到那一层踩上去一次全收回。
一层最多一具，同时最多留 5 具。

【规则都写在游戏里】
图例、符号含义、命中与伤害公式、行动顺序、怪物分类，全部在「玩法与图例」页里，不用去外面查 wiki。

【隐私与素材】
- 不收集任何数据，App 不发起任何网络请求，飞行模式下全部功能可用
- 没有内购，没有账号，没有广告，没有分析或追踪 SDK，App 里不含任何第三方代码
- 不申请任何系统权限，系统不会为它弹出任何权限询问
- 进度只存在这台设备的沙盒里，删除 App 即清空
- 音效由代码实时合成，画面全部由代码绘制，不含任何第三方素材或 SDK

【系统要求】
需要 iOS 17.0 或更高版本。iPhone 与 iPad 均可，仅支持竖屏。
```

**字符数：1241 / 4000**

### English

```
AsciiDungeon is a portrait turn-based roguelike. One screen of ASCII glyphs, 10 floors, and one tap per move. Fully offline: no account, no ads, no in-app purchases.

[Controls]
- Tap any tile and you walk there automatically; you stop short the moment an awake monster comes into view
- A tapped path only ever follows ground you have already explored, so one tap cannot scout for you
- Swipe in a direction to take a single step, in any of eight directions
- Walking into a monster's tile is how you attack it; there is no separate attack button
- Auto walks you to the edge of the unexplored area and stops when a monster shows up
- Descend only lights up when you are standing on the stairs; the dungeon only goes down

[The readout above the map]
Whenever a monster is in view, the top of the screen tells you whether the fight is winnable:
you can take it, it is an even match, you cannot take it, or it will kill you.
Tap the strip to expand it and see both sides' hit chance and damage range before you commit.

Those are the numbers the dice actually use, not a separate estimate.

[The rules are computable]
Hit chance is 55 percent plus 5 percent per point of accuracy, minus the target's evasion, clamped between 5 and 95 percent.
Damage is the dice range plus strength and level bonus, minus the target's armor, with a floor of 1.
Speed comes in four steps, slow, normal, fast and very fast, which are 0.5, 1, 1.5 and 2 times your own rate.
The bag screen lists your accuracy and damage with the formula printed beside them, and marks whether a pickup beats what you are carrying.

You always see it first: your sight radius is 8 tiles and a monster's alert radius is 6, so nothing invisible ever ambushes you.
When a fight is going badly, back off and wait: every 12 turns you regain 1 health.

[Unmet monsters get no verdict]
Monsters you have seen go into the bestiary, and from then on the readout gives a full verdict whenever one is in view. Unmet monsters are drawn in purple and the readout will only say unknown, so the right move on a first meeting is to stay alive and watch how it fights.

[10 floors]
Every floor grows from a random seed, built from rooms and corridors, so it is connected by construction and can never generate a map you cannot finish.
The same seed always grows the same map, and the seed is what the save file stores, so floor 5 is the same map after a restart.
Floor 10's abyss gate is guarded by the Omega. Beat it, stand on the stairs and descend, and the run is won.

[What death costs]
Your level resets and you start again from floor 1.
The weapon and armor you were carrying, plus the first 6 items in your bag, stay on the floor where you fell, drawn as a percent sign; walk onto that tile in a later run and reclaim all of it at once.
At most one pile per floor, and at most 5 in total.

[The rules ship with the game]
The legend, the glyph meanings, the hit and damage formulas, turn order and the monster categories are all on the How to Play screen. No wiki required.

[Privacy and assets]
- Collects nothing, and the app makes no network requests; every feature works in Airplane Mode
- No purchases, no account, no ads, no analytics or tracking SDKs, and no third-party code at all
- Requests no permissions, so the system never prompts you
- Progress stays in the app's sandbox on this device; deleting the app clears it
- Sound effects are synthesised in code and all artwork is drawn in code, with no third-party assets or SDKs

[Requirements]
iOS 17.0 or later. iPhone and iPad. Portrait only.
```

**字符数：3557 / 4000**（离上限只剩 443，改写时留意）

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
一屏字符画的回合制地牢
```

**字符数：11 / 30**

### English

```
Turn-based ASCII roguelike
```

**字符数：26 / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
roguelike,肉鸽,回合制,单机,离线,无广告,迷宫,地下城,像素,冒险,rpg
```

**字符数：43 / 100**

### English

```
roguelike,ascii,dungeon crawler,turn based,offline,retro,indie,single player,no ads,text
```

**字符数：88 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/asciidungeon/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/asciidungeon/privacy.html` |
| 营销 URL | 留空 |

技术支持是**版本级**字段（改它要跟新版本一起提审），隐私政策是 **App 级**（要有待发版本才能改）。
这两个 URL 一旦提审就不好改了，提审前先确认目录名。
营销 URL 是可选字段，`apps/asciidungeon/` 下没有 `index.html`，填了就是 404，所以留空。

**这两个页面现在还是 404。** `apps/` 是独立仓库 `zhipengge/apps`，Pages 已经开着
（`apps/skystrike/privacy.html` 现在返回 200），但 `apps/asciidungeon/` 还没进版本库。
提审前必须先提交并推送这一整个目录，否则 App Store Connect 填的隐私政策链接是空的。

---

## 6. 类别、评级、隐私问卷

### 类别（需要你定，两个都列出来）

| 选项 | 主要类别 | 次要类别 | 理由 |
|---|---|---|---|
| A | 游戏 / Games，子类 **角色扮演 / Role Playing** | 游戏 / Games，子类 策略 / Strategy | 有等级、经验、装备、背包、属性，是 roguelike 的通行归类；苹果的 Role Playing 子类下大量同类作品 |
| B | 游戏 / Games，子类 **策略 / Strategy** | 游戏 / Games，子类 冒险 / Adventure | 强调回合制与走位取舍，不强调数值养成；但探索权重高的分类里曝光不一定更好 |

`TARGETED_DEVICE_FAMILY = "1,2"`，主要类别必须选游戏，子类只能选一个。

### 年龄分级（需要你定）

问卷不让你直接选档位，是按题作答后由 Connect 判定。当前档位是 4+ / 9+ / 13+ / 16+ / 18+ 五档。
这个游戏的实际情况：回合制打怪、怪物会死、玩家会死，但全部是字符画，没有血、没有尸体、没有写实暴力，
也没有恐怖、赌博、酒精烟草毒品、色情、脏话、用户生成内容、聊天、广告、网页浏览。

会决定档位的就是「卡通或幻想暴力」这一题：

| 你怎么答 | 后果 |
|---|---|
| 无 | 大概率落在 4+。但战斗是这个游戏的核心循环，答「无」与事实不符，不建议 |
| 轻微/偶尔 | 大概率落在 9+。这是与事实最贴的一档，也留了余量 |
| 频繁/强烈 | 会推到 13+。字符画是否够得上「强烈」由你判断 |

**另一个时间点要注意：** 苹果要求所有开发者在这轮问卷更新里重新作答，**2026 年 1 月 31 日之后没作答的 App 无法提交更新**。这一条跟本作是否上架无关，只要还想发版本就得先过。

### 其余表

| 字段 | 建议 |
|---|---|
| 内购 | **无**。没有 StoreKit 代码，也没有账号系统 |
| App 隐私 | **不收集数据**。App 不发起任何网络请求，须与 `privacy.html` 一致 |
| 出口合规 | **NO**。`INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO` 已经写在工程里，App 完全没有加密，也没有网络代码 |

审核备注建议写清：本 App 完全离线，不发起任何网络请求，不收集任何数据，无账号、无内购、无广告，
也不申请任何系统权限。全部音效由代码实时合成，全部画面由代码绘制，不含任何第三方素材或 SDK。
iPhone 与 iPad 均为竖屏。

首次提交时审核备注还要写：iPhone 与 iPad 均为竖屏，不支持横屏。

---

## 7. 截图

App 是 `TARGETED_DEVICE_FAMILY = "1,2"`，iPhone 与 iPad 两套都要，各 3-10 张。

按 Apple《截屏规范》（Screenshot specifications，2026-10-12 核对原文），**必填的只有两档**：

- iPhone：**带灵动岛的 iPhone（中等显示屏）**，即 iPhone 17 / 17 Pro / 16 / 16 Pro / 15 / 15 Pro / 14 Pro 这一档，竖屏 1206 x 2622 或 1179 x 2556
- iPad 13 寸，竖屏 2064 x 2752

6.9 寸（带灵动岛的 iPhone，大显示屏，1320 x 2868）**不是必填**，但已经做了，一并上传。

| 平台 | 必填 | 像素 | 位置 | 状态 |
|---|---|---|---|---|
| iPhone 6.3 寸（中等显示屏） | 是 | 1206 x 2622 | `screenshots/iphone-63/` | 6 张 |
| iPad 13 寸 | 是 | 2064 x 2752 | `screenshots/ipad/` | 6 张 |
| iPhone 6.9 寸（大显示屏） | 否 | 1320 x 2868 | `screenshots/iphone/` | 6 张 |

三套用的是同一份标题与副标题，只是画面尺寸不同：

| 文件 | 标题 | 副标题 | 对应界面 |
|---|---|---|---|
| `01-menu.png` | 一屏字符画的地牢 | 点一下走一步，10 层，全程离线 | 主菜单与进度 |
| `02-threat.png` | 打不打得过 | 屏幕上方那行读数是算出来的，不是估计 | 地牢中，威胁读数展开 |
| `03-dungeon.png` | 点一下走一步 | 走进怪物的格子就是攻击它，没有攻击键 | 地牢中，已探索区域 |
| `04-readout.png` | 读数只对认识的怪开口 | 没见过的，先活下来看清它怎么打人 | 怪物图鉴 |
| `05-bag.png` | 强弱都摆在明面上 | 包里的比身上的强，直接标出来 | 背包与装备对比 |
| `06-help.png` | 不用查 wiki | 全部规则和图例都写在游戏里 | 玩法与图例 |

竖屏截图，不要裁成横版。空状态、纯海报式截图会被拒。
**三套都刻意没有遗骸页**：图鉴跨局继承和遗骸回收这两条的效果量在 `LogicTests/balance.sh` 里量出来是零
（「地牢记得你」+0.02 层，学习曲线 -1.72 层），所以一个字都没当卖点，标题和副标题只讲界面上真实存在的东西。

> 本作有一处已知的 iPad 配置问题（`UIRequiresFullScreen` 与 ITMS-90474），
> 已用声明该键的方式处理（见 `AsciiDungeon/AGENTS.md`），这一轮没有动它。
