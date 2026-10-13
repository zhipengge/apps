# 牧云岛屿 (IslandTactics) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。

---

## 0. 创建 App Record

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **macOS** | iOS |
| 名称（主语言：简体中文） | **牧云岛屿** | 岛屿、IslandTactics 牧云（通称易被占） |
| 名称（English 本地化） | **IslandTactics** | Muyun Island |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.IslandTactics` | 任何旧 ID |
| SKU | `islandtactics-20261011` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「牧云岛屿」，已写在工程里。
`LSApplicationCategoryType` 为 `public.app-category.strategy-games`。
`ITSAppUsesNonExemptEncryption = NO` 已写在工程里。

**SKU 这一项没有写进代码**，是本节按仓库建仓日期（2026-10-11）拟的命名，创建时以你实际填的为准。

**注意：App 没有任何本地化。** 工程 `developmentRegion` 是 `zh-Hans`，界面文案与十二座岛的名字全是中文硬编码。
如果给 English 也建一份商店本地化，英文用户看到的是「英文描述 + 中文界面」。
要么这轮只上简体中文（主要语言就是它），要么等界面做完英文化再补 English 本地化。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
十二座手写的岛。丘陵不会被大潮淹，但工厂和瞭望塔只能建在丘陵上。农场要有土，而土全在会被淹的低地。最赚钱的那一格，也是敌军登陆的那一格。
```

**字符数：68 / 170**

### English

```
Twelve hand-authored islands. Factories go on hills, farms need soil, and the soil sits on lowland that floods. The most profitable tile is also where the enemy lands.
```

**字符数：167 / 170**（只剩 3，改写时留意）

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
牧云岛屿是一个回合制的岛屿经营与防守游戏。一座岛，一张 11 乘 8 的格子地图，要在最后的期限前达成这座岛的目标，同时扛住大潮、风暴和入侵。十二座岛，每座是一道手写的空间题。

【格子是唯一真正稀缺的东西】
地形把「安全」和「肥沃」劈成了两批。丘陵不会被大潮淹，但工厂和瞭望塔只能建在丘陵上，而丘陵只有那么多。农场要有草地或浅滩，这两样全在低地，低地会被淹。最赚钱的码头要临海的低地，所以最赚钱的那一格，同时是淹得最狠、也是敌军登陆的那一格。

建筑之间还有相邻惩罚：工厂挨着农场，农场收成减半；工厂挨着住宅，民心下滑。挤在一起省地，分开摆产量高但要多占格子。这就是你每隔一会儿要做一次的那个决定。

【三种资源，各管一段】
粮食养人口和军队，断粮掉民心，连续三天会拆房子。金币来自税收、工厂和码头，用来建造、征兵、付维护费。技能只有工坊产，只能解锁科技，除此之外什么都不能做。

【八种建筑】
房屋、农场、工厂、码头、兵营、工坊、堤坝、瞭望塔。其中堤坝和瞭望塔零产出：一个纯粹拿一格和每天的钱换安全，一个拿一格换防御圈和更早的预警。兵营没有产出，吃维护，但它是防御圈的来源。

【危机日程从一开始就是公开的】
大潮、风暴、入侵的日子，从第一天起就全部摊在界面上，日历上还会写清每一支入侵舰队的战力。紧张感不来自「不知道会发生什么」，而来自「知道第 19 天会来一支战力 44 的舰队，而我现在连兵营都还没盖」。

【入侵当天要选姿态】
固守让守备加四成、战损减两成半，防御圈内的建筑不会被拆。出击让攻击加三成半，代价是守备减两成、战损加两成、防御圈少一格，赢了缴获更多，输了防御圈也罩不住。避战不交战，代价是被拆两座没被防御圈罩着的建筑、抢走两成金币、掉 12 点民心。避战虽然零兵损，但它也算防线失守，防线被突破两次就丢掉这座岛。

【面板不骗人】
预测和结算走的是同一个函数，预测只是把结算用的骰子夹到区间两端各算一遍，不是另写一份简化公式。经济的每日账本既是结算用的账，也是界面上那行「每天多少金」的来源；目标进度条取的是更差的那个条件，不会只报好消息。一个数字只有一个出处，所以面板上的数不会和实际结果打架。

【八条科技，五条改规则】
工坊产出很慢，一座岛通常只买得起两三条，所以选哪三条才是每一局的主要路线抉择。灌溉让工厂旁边的农场不再减半，仓廪让断粮不再打击民心，石工让堤坝便宜四成且半径加一格，卫生让工厂不再掉民心，烽火把入侵预警提前三天。另外三条，市集、弩机、重甲，是纯倍率加成：码头金币加四成、弓箭手攻击加五成、骑士防御加六成。

【难度】
安逸、标准、严酷三档，分别改变开局国库与存粮、建筑维护费、危机强度和民心基线。民心基线同时决定「工业化的容忍度」，基线越低，能挨着住宅建的工厂越少。

【这一版没有的东西，也一并说清】
没有声音：App 没有链接任何音频框架，工程里也没有音频文件，从头到尾是静音的。
没有内购，没有账号，没有广告，没有排行榜，没有任何形式的在线内容。
完全离线：沙盒权限里只有一条 app-sandbox，没有申请网络权限，源码里也没有任何网络 API，断网时十二座岛都能正常玩。
不申请任何系统权限，系统不会为它弹出授权框。

【系统要求】
需要 macOS 14.0 或更高版本。普通窗口 App，会在 Dock 里出现。
```

**字符数：1388 / 4000**

### English

```
IslandTactics is a turn-based island management and defence game. One island, an 11 by 8 grid, a deadline to meet, and tides, storms and raids along the way. Twelve islands, each a hand-authored spatial puzzle.

[Tiles are the only thing genuinely in short supply]
The terrain splits safe from fertile. Hills never flood, but factories and watchtowers can only be built on hills, and there are only so many. Farms need soil, and soil exists only on lowland, which floods. The most profitable building, the dock, needs coastal lowland, so the most profitable tile is also the one that floods hardest and the one the enemy lands on.

Buildings also penalise their neighbours: a factory next to a farm halves the farm's yield, and a factory next to housing costs morale. Packing everything together saves tiles; spreading it out yields more but costs space.

[Three resources, each doing one job]
Food feeds your population and your army; running out costs morale, and three days of it destroys a house. Gold comes from taxes, factories and docks, and pays for building, recruiting and upkeep. Skill comes only from workshops and buys technologies.

[Eight buildings]
Houses, farms, factories, docks, barracks, workshops, dikes and watchtowers. Dikes and watchtowers produce nothing: one trades a tile and a daily cost for safety, the other a tile for a wider defence radius. Barracks cost upkeep, but they are where your defence radius comes from.

[The crisis calendar is public from the start]
Every tide, storm and raid is laid out on screen from day one, with the strength of each incoming fleet. The tension is not from not knowing what will happen; it is from knowing a fleet of strength 44 arrives on day 19 and you have not built a barracks yet.

[Every raid makes you pick a stance]
Defend gives 40 percent more guard and 25 percent fewer losses, and buildings inside the defence radius survive. Sortie gives 35 percent more attack at the cost of 20 percent of your guard, 20 percent more losses and one tile of defence radius. Evade avoids battle altogether, at the cost of two buildings outside the radius, a fifth of your gold and 12 morale; it loses no troops, but still counts as the defence failing, and two breaches lose you the island.

[The panel does not lie]
The forecast and the resolution call the same function, the forecast merely running its dice at both ends of their range. Each number on screen has exactly one source, so the panel cannot disagree with what actually happens.

[Eight technologies, five of which change rules]
Workshops produce slowly and an island usually affords only two or three, so choosing them is the run's main strategic decision. Irrigation stops a factory from halving an adjacent farm; granary stops starvation from costing morale; masonry makes dikes 40 percent cheaper with one more tile of reach; sanitation stops factories from costing morale at all; beacon warns you three days earlier. The other three, market, crossbow and plate armour, are pure multipliers: docks plus 40 percent gold, archers plus 50 percent attack, knights plus 60 percent defence.

[Difficulty]
Three levels, relaxed, standard and harsh, each changing your starting gold and food, building upkeep, crisis strength and the morale baseline, which also sets how much industry the island tolerates: a lower baseline means fewer factories can sit next to housing.

[What this version does not have]
No sound. The app links no audio framework and ships no audio files; it is silent throughout.
No in-app purchases, no account, no ads, no leaderboards, no online content.
Fully offline: the sandbox declares only app-sandbox with no network entitlement and the source has no networking API, so all twelve islands play with no connection.
No system permissions are requested, so the system never prompts you.

[Requirements]
macOS 14.0 or later. An ordinary windowed app that appears in the Dock.
```

**字符数：3919 / 4000**（只剩 81，改写时留意）

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
安全的地，从来不够分
```

**字符数：10 / 30**

### English

```
Safe ground is never enough
```

**字符数：27 / 30**（只剩 3，改写时留意）

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
岛屿,策略,回合制,经营,防守,生存,单机,离线,建造,布局
```

**字符数：30 / 100**

### English

```
island,strategy,turn-based,city-builder,defense,survival,offline,single-player
```

**字符数：78 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/islandtactics/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/islandtactics/privacy.html` |
| 营销 URL | 留空 |

技术支持是**版本级**字段（改它要跟新版本一起提审），隐私政策是 **App 级**（要有待发版本才能改）。
这两个 URL 一旦提审就不好改了，提审前先确认目录名。

营销 URL 是可选字段，`apps/islandtactics/` 下没有 `index.html`，填了就是 404，所以留空。

**这两个页面现在还不存在。** `apps/` 是独立仓库 `zhipengge/apps`，Pages 已经开着
（`apps/skystrike/privacy.html` 现在返回 200），但 `apps/islandtactics/` 这个目录还没提交。
提审前必须先提交并推送这一整个目录，否则 App Store Connect 填的隐私政策链接是空的。

---

## 6. 类别、评级、隐私问卷

### 类别

主要类别填 **游戏 - 策略 / Games - Strategy**，与工程里的
`LSApplicationCategoryType = public.app-category.strategy-games` 一致。
次要类别可以留空；如果要填，**娱乐**比**模拟**更贴，但本作的核心是资源取舍与防线，不是模拟。

### 年龄分级（需要你定）

问卷不让你直接选档位，是按题作答后由 Connect 判定。这个 App 的实际内容：
是回合制经营，没有角色形象、没有血腥、没有性内容、没有脏话、没有赌博、没有酒精烟草毒品、
没有用户生成内容、没有聊天、没有广告、没有内购。
可能影响判定的是「暴力」类题目：本作的战斗是数值结算加一段结果文案，
没有战斗画面、没有流血表现、没有对人的暴力刻画，按实际内容应作答为否或最低档。

按上述事实作答，大概率落在 4+ 或 9+。

### 其余表

| 字段 | 建议 |
|---|---|
| 内购 | **无**。没有 StoreKit 代码，也没有账号系统 |
| App 隐私 | **不收集数据**。App 不发起任何网络请求，须与 `privacy.html` 一致 |
| 出口合规 | **NO**。`INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO` 已经写在工程里。App 里没有任何加密、哈希或密钥运算，也没有链接密码学框架 |
| 辅助功能 / 输入监控 | **不申请**。App 里没有任何全局快捷键，快捷键都是普通的菜单快捷键 |
| Game Center | **不接**。没有排行榜、没有成就 |

审核备注建议写清：本 App 完全离线，沙盒权限里只有 app-sandbox 一条，没有申请网络权限，
源码里也没有任何网络 API。它不申请任何系统权限，因此系统不会弹出授权框。
App 没有内购、没有账号、没有广告。读档时手动存档优先于自动存档。

---

## 7. 截图

macOS App 的商店截图规格与 iOS 不同：**1280 x 800**（或 2560 x 1600 等 16:10 档位）。

**本轮没有产出截图，截图由另一路做。** 这个目录下现在没有 `screenshots/`。

截图内容建议（都对应界面上真实存在的东西，不要做纯海报式截图）：

| 建议标题 | 副标题 | 对应界面 |
|---|---|---|
| 安全的地，从来不够分 | 丘陵不会被淹，但工厂只能建在丘陵上 | 棋盘视图加上地形着色 |
| 危机日程开局就公开 | 你知道第几天会来，只是还没准备好 | 危机日历（`CalendarView`） |
| 面板不骗人 | 预测和结算走的是同一个函数 | 入侵姿态面板上的胜败区间与最坏损失 |
| 每格都有代价 | 逐格产出明细会写清每一条加成和惩罚的来源 | 检查器（`InspectorView`） |
| 选哪三条科技 | 工坊产出很慢，一座岛通常只买得起两三条 | 科技面板（`TechPanelView`） |

空状态、纯海报式截图会被拒。

---

## 8. 交付前必须补的（不是文案问题）

| 项 | 现状 | 为什么是阻塞项 |
|---|---|---|
| **AppIcon 是空壳** | `Assets.xcassets/AppIcon.appiconset` 里只有 `Contents.json`，十个槽位全是空的 | 没有图标无法提交。**加图标要先问过作者**，不要自作主张往仓库里放位图 |
| **界面没有手工试玩过** | 状态机被 137 条 headless 断言走遍，构建和启动冒烟也过了，但没有任何人手工点过界面 | Hover 高亮、日历在 48 天宽度下会不会挤、结算面板文案是否通顺，这些只有坐在屏幕前才知道。**截图也不能拿没验过的界面去拍** |
| **`PrivacyInfo.xcprivacy` 不存在** | 工程里没有这个文件 | 本 App 不用 UserDefaults、不用文件时间戳之类需要申报理由的 API，但上架前建议按实际用量补一份或确认无需 |

---

## 9. 差异化：能用什么、不能用什么

这一节来自 `IslandTactics/AGENTS.md` 的「差异化：这个 app 凭什么存在」，
以及紧随其后的「这几条成立到什么程度（探针数据，别只看上面）」。
**下面「不能用」的每一条都是作者自己写下的，照抄即可。**

### 能用的（代码里指得出来，探针也支持）

| 能用的说法 | 代码依据 |
|---|---|
| 地形把「安全」和「肥沃」劈成两批，每格都是有代价的取舍 | `Buildings.swift` 的放置规则：工厂/瞭望塔只能建在丘陵，农场要有草地或浅滩，码头要临海低地；`Economy.report` 的两条相邻惩罚 |
| 危机日程开局全部公开 | `IslandSpec.calendar` / `events(on:)` + `Views/CalendarView.swift`，选岛界面也印三行摘要 |
| 面板不骗人（预测 = 结算） | `Military.forecast` 与 `resolve` 共用 `Combat.score`；`Economy.report` 同时是账本与 HUD 数字来源；`objectiveProgress()` 同一函数供进度条与胜负判定 |
| 十二座岛是手写字符画，不是程序生成 | `Islands.swift` 的字符画地图；D 段 264 条断言逐岛守着地形配比与设计意图 |
| 避战也算防线失守 | `GameConfig.raidsLostToLoseIsland = 2` 把「打赢」和「放上岸」分开计数，避战计进后者 |

**探针给的侧证**：`抉择密度`（当天存在势均力敌的第二选择的天数占比）标准难度 49%、严酷 46%。

### 故意没有用的（以及为什么）

| 没有用的说法 | 为什么不用 |
|---|---|
| 「八条科技每条都改规则，不是加数字」 | 这是 `AGENTS.md` 里那节的小标题，但**它对自己不利的一面就写在下面**：八条里只有**五条**真的改规则（灌溉、仓廪、石工、卫生、烽火），另外三条（**市集、弩机、重甲**）是纯倍率加成（码头 +40%、弓箭手攻击 +50%、骑士防御 +60%）。所以描述里写成「八条科技，五条改规则」，并把三条倍率的也如实列出来 |
| 「路线各有千秋」「怎么打都能赢」 | 作者原话：「**工业路线接近通吃**：工业性格在标准难度下打赢 11/12 座岛」。描述里一个字都没提「多种流派平衡」 |
| 「军事路线是一条路」当成卖点 | 作者原话：「**军事路线偏弱**（56/108，最低的两种之一）。养兵要占人口、占粮、占地，而它在探针里换回来的胜率不如把钱铺在地图上。**这是当前最需要调的一处**」 |
| 「难度曲线平滑」 | 作者原话：「岛 2『绿岬』15/15 全过……**标准难度下它不构成任何挑战**」 |
| 「有托管 / 自动托管」 | **`AutoPilot.swift` 没有被接进界面**：在 `Views/`、`Services/`、`IslandTacticsApp.swift` 里 grep `AutoPilot` 和「托管」都是空的。它只被 `LogicTests` 用。`AGENTS.md` 自己那句「探针与托管共用这一份」是过时的。描述里没有任何「托管」「自动」字样 |
| 「有 AI 对手」 | 敌人是写死的日程式战力（`IslandSpec` 里的 `RaidSpec`），不是会应变、会学你打法的对手 |
| 「画面精致」「手感好」「界面打磨过」 | 作者原话：「**『状态机』验过了，『画面』还没有**……**没有任何人手工点过界面**」。这一版一个字都没夸界面 |
| 「多周目」「重复可玩性高」 | 十二座岛通关之后有什么，没有任何人量过。**没有数据就不写** |
| 「无追踪、干净」 | 这是事实陈述，可以写进隐私政策（因为沙盒权限可以核），但它不构成卖点：任何 App 都能这么声称，用户也没法验证 |

### 作者标注「没有验证」的（不要当成已经好了）

来自 `AGENTS.md` 的「当前进度」与「待办」两节：

- **界面没有任何人手工点过**（最该补的一件事）。
- **军事路线偏弱**（56/108），还没调。
- **岛 2 太松**（标准难度 15/15），还没调。
- **AppIcon 是空壳**，十个槽位都是空的。
- **`SaveFile.version` 恒为 1**，迁移路径只被测试里的「缺字段旧 JSON」覆盖过，没有真实的历史存档。

所以描述里没有出现「界面精美」「平衡打磨过」「上手即会」这类话。
