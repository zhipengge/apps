# 暗区枪线 (DarkZone) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。
> **这份素材刻意没有任何难度、手感或「侦察值不值」的评价，理由见第 9 节。改文案之前先读那一节。**

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **暗区枪线** | 暗区突围（他人商标）、暗区（通称易被占） |
| 名称（English 本地化） | **DarkZone** | Dark Zone、Darkzone Tactics |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.DarkZone` | 任何旧 ID |
| SKU | `darkzone-20261011` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「暗区枪线」。

**SKU 用的是 `fastlane/Fastfile:108` 里已经登记过的那个**，不要另起一个，
否则 fastlane 的 `status` / `check_app_records` 会对不上。

备选店名（创建时报名被占再用）：

- 暗区枪线 DarkZone
- 暗区枪线 战术射击
- 暗区枪线 一枪就死

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

**注意：App 本身没有任何本地化。** 工程里没有 `.lproj`、没有 `Localizable.strings`、也没有 `.xcstrings`，
`Views/` 下的用户可见字符串**一条 ASCII 开头的都没有**，全是中文硬编码。
所以如果给 English 也建一份商店本地化，英文用户看到的是「英文描述 + 中文界面」。
要么这轮只上简体中文（主要语言就是它），要么等界面做完英文化再补。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
俯视角单机战术射击。一枪就死，敌人举枪有半秒，侦察要花真实时间。10 张固定地图，全程离线，没有账号，没有内购。
```

**字符数：56 / 170**

### English

```
Top-down single-player tactical shooting. One bullet kills, enemies take half a second to raise a gun, and scouting costs real time. Ten fixed maps, fully offline.
```

**字符数：163 / 170**

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。
> **描述里一个字的购买、价格、免费、内购都没提，原因见第 7 节。**

### 简体中文

```
暗区枪线是一个俯视角的单机战术射击。10 个关卡，一张图就是一关，一枪就能把你打死。单人、离线，一关几十秒到一分多钟。

【没有血量这个字段】
玩家身上根本没有血量，被打中就是死。唯一的缓冲是敌人发现你之后举枪的那一下，最快的 0.40 秒，最慢的 0.80 秒。
所以「被发现」的后果不是掉血，而是立刻变成一道二选一：先手打死他，还是退出这个视野锥。

【两个摇杆，五个按钮】
左摇杆走路，右摇杆瞄准并且开枪。右摇杆上画了一圈虚线：圈内只瞄准，推过去才开火。
不这样设计的话，你就没法「先瞄着他，等他探出头再打」。
右下角五个按钮：疾跑、换弹、侦察、换枪、刀。都是点一下切换或者触发一次，不用按住，因为按住会跟摇杆抢手指。
疾跑是开关而不是推到底，因为它有代价：脚步声会传得更远。

【侦察：把「看」做成一件按真实时间计费的事】
按住侦察键，世界会慢下来，但真实时间照走，那 9 秒配额是按真实秒扣的。
买到的是全图情报：每个敌人的视野锥和巡逻路线。还能在地图上放最多 3 个标记，标记只是你自己的备忘纸，不额外扣配额，真正花时间的是「看」这个动作。
要注意：三颗星里有一颗是「用时不超过基准」，而侦察花掉的正是用时。

【掩体是双面的】
既挡视线也挡子弹，两者共用同一套判定。木箱可以被打碎，碎掉之后视线就通了，敌人绕路的算法也会重算；水泥墙打不碎。
所以「打穿它」和「绕过去」是两个真实选项，而打箱子会发出声音，声音又可能把人叫过来。

【噪音是一等公民】
开枪会把人引过来。刻意朝 A 点开一枪、把守卫从 B 点引开，是一种正当打法。四种敌人的应对方式各不相同：哨兵不动、突击兵冲、重甲兵架枪、巡逻兵会追。

【不必清场】
目标有三种：清除区域内全部敌人、抵达撤离点、取得情报并带回出发点。
有些关卡是「过去再回来」，全程可以一个人都不杀，只要你能不被发现地走过去。

【四种敌人，五把武器】
巡逻兵会走来走去，哨兵站着不动但视野最远、枪法最准，突击兵会朝你冲过来，重甲兵要三枪才倒。
五把武器里四把可选：消音手枪、冲锋枪、霰弹枪、步枪，外加一把近身用的战术刀。
最安静的枪射程最短，射程最远的枪最吵，「安静」和「安全距离」只能选一个，所以选枪是一个真的决定。

【三颗星是三条独立的线】
第一颗是通关，第二颗是用时不超过基准，第三颗是被发现次数不超过基准而且命中率不低于 40%（或者一枪没开）。
结算页会逐条告诉你是过还是没过、为什么，最后只给一条提示。

【地图是固定的】
十关的地形都不会变，同一关重打多少次都是那张图，所以记住路线是有用的。

【隐私】
- 不收集任何数据，App 不发起任何网络请求，飞行模式下全部功能可用
- 没有账号，没有注册，没有广告，没有内购
- 没有分析、崩溃上报或追踪 SDK，工程里没有任何第三方依赖，框架构建阶段是空的
- 不申请任何系统权限，系统不会为它弹出任何权限询问
- 进度只存在这台设备上的一个键里，删除 App 即清空
- 画面全部由代码绘制，19 种音效全部由代码实时合成，不含任何第三方素材或 SDK

【系统要求】
需要 iOS 17.0 或更高版本。iPhone 上仅支持竖屏，iPad 上支持四个方向。界面为中文。
```

**字符数：1344 / 4000**

### English

```
DarkZone is a top-down single-player tactical shooter. Ten levels, one map each, and a single bullet kills you. Fully offline, and a level runs from tens of seconds to a bit over a minute.

[There is no health field]
The player has no health at all, and being hit means dying. The only buffer is the moment an enemy raises their gun after noticing you, from 0.40 seconds at the fastest to 0.80 at the slowest.
So the consequence of being spotted is not losing health, it is an immediate either-or: shoot first, or leave that cone of vision.

[Two sticks, five buttons]
The left stick moves, the right stick aims and fires. A dashed circle is drawn on the right stick: inside it you only aim, and pushing past it fires.
Five buttons sit in the lower right: sprint, reload, scout, swap weapon, knife. Each is a toggle or a one-shot rather than a hold, because holding would fight the stick for your finger.
Sprint is a toggle rather than push-to-max because it carries a cost: your footsteps carry further.

[Scouting: looking is billed in real time]
Hold the scout button and the world slows down, but real time keeps running and the nine-second budget is charged in real seconds.
What you buy is full-map intel: every enemy's vision cone and patrol route. You can also place up to three marks, which are only your own scratch paper and cost no extra budget; the thing that costs time is the looking itself.
Worth knowing: one of the three stars is for finishing within par time, and scouting is paid for in exactly that currency.

[Cover cuts both ways]
It blocks sightlines and bullets alike. Wooden crates can be shot apart, and breaking one opens the sightline and forces the enemies' routing to be recomputed; concrete walls cannot be broken.
So shooting through and going around are both real options, and shooting a crate makes noise.

[Noise is a first-class citizen]
Firing draws people toward you. Deliberately putting a round into point A to pull a guard off point B is a legitimate play. The four enemy types each respond differently: sentries hold, rushers charge, heavies set up, patrols come looking.

[You do not have to clear the map]
There are three objectives: clear all enemies in the area, reach the extraction point, or take the intel and bring it back to the start.
Some levels are there-and-back and can be finished without killing a single person, as long as you can walk it unnoticed.

[Four enemies, five weapons]
Patrols walk their route, sentries stand still with the longest vision and the best aim, rushers charge you, and heavies take three shots to drop.
Four weapons are selectable: a suppressed pistol, an SMG, a shotgun and a rifle, plus a knife for close quarters.
The quietest gun has the shortest range and the longest-ranged gun is the loudest: quiet and safe distance are mutually exclusive, so choosing one is a real decision.

[Three stars on three independent lines]
The first is for clearing the level, the second for finishing within par time, and the third for staying within the alert budget with accuracy at or above 40 percent, or for not firing at all.
The result screen tells you pass or fail on each line and why, and then gives one hint.

[The maps are fixed]
The terrain of all ten levels never changes, so memorising a route pays off.

[Privacy]
- Collects nothing and makes no network requests; every feature works in Airplane Mode
- No account, nothing to register, no ads and no in-app purchases
- No analytics, crash reporting or tracking SDKs, no third-party dependencies at all, and an empty frameworks build phase
- Requests no permissions, so the system never prompts you
- Progress lives in one key on this device; deleting the app clears it
- All visuals are drawn in code and all 19 sound effects are synthesized at runtime

[Requirements]
iOS 17.0 or later. Portrait only on iPhone; all four orientations on iPad. The interface is in Chinese.
```

**字符数：3909 / 4000**（离上限只剩 91，改写时留意）

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
一枪就死的俯视角战术射击
```

**字符数：12 / 30**

### English

```
One-shot top-down tactics
```

**字符数：25 / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
战术射击,俯视角,潜行,单机,离线,枪战,侦察,闯关,无广告,硬核
```

**字符数：33 / 100**

### English

```
tactical shooter,top down,stealth,offline,single player,cover,stealth action,no ads,hardcore
```

**字符数：92 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/darkzone/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/darkzone/privacy.html` |
| 营销 URL | 留空 |

技术支持是**版本级**字段（改它要跟新版本一起提审），隐私政策是 **App 级**（要有待发版本才能改）。
这两个 URL 一旦提审就不好改了，提审前先确认目录名。

营销 URL 是可选字段，`apps/darkzone/` 下没有 `index.html`，填了就是 404，所以留空。

**这两个页面现在还是 404。** `apps/` 是独立仓库 `zhipengge/apps`，Pages 已经开着
（`apps/skystrike/privacy.html` 现在返回 200），但 `apps/darkzone/` 还没进版本库。
提审前必须先提交并推送这一整个目录，否则 App Store Connect 填的隐私政策链接是空的。

---

## 6. 类别、评级、隐私问卷

### 类别

**2026-10-14 定：原方案 A。**

| 字段 | 值 |
|---|---|
| 主要类别 | 游戏 / Games，子类 **动作 / Action** |

**次要类别为什么留空**（2026-10-14，实测）：
原方案 A 的次要类别写的是「游戏 / Games，子类 策略 / Strategy」，
但**苹果不允许把同一个类别选两次**——真写时被明确拒绝：

```
HTTP 409  You may not select the same category twice for your app.
```

主类别已经是「游戏」了，次要类别就不能再是「游戏」。次要类别在 ASC 是**可选**的，
所以留空不影响提交。（要填的话只能挑一个**非游戏**的顶级类别，比如娱乐 / Entertainment。）

（选 A 的理由：实时移动、瞄准、开火是核心循环；俯视角战术射击同类多归在动作。
原方案 B「策略 / 动作」见 git 历史。改成这两行是因为工具只认表格行——
原来那张「选项 A/B」表它是当**候选题**读的，会一直报「必须人选定一个」。）

`TARGETED_DEVICE_FAMILY = "1,2"`，主要类别必须选游戏，子类只能选一个。

### 年龄分级（需要你定）

问卷不让你直接选档位，是按题作答后由 Connect 判定。当前档位是 4+ / 9+ / 13+ / 16+ / 18+ 五档。

这个 App 的实际情况：俯视角的几何图形，玩家会死、敌人会死，有枪械。
没有恐怖、赌博、酒精烟草毒品、色情、脏话、用户生成内容、聊天、广告或网页浏览，也不联网。

**⚠️ 有一点本轮没有核实，需要你亲眼判断：** 击倒敌人时的视觉效果（有没有血、碎块、写实度）。
我没有逐个读渲染代码，所以不能替你答「卡通或幻想暴力」「血腥」这类题。
建议在真机上打死几种敌人看清那一下再作答——这一项往往就是 9+ 和 13+ 之间的分界。

**另一个时间点要注意：** 苹果要求所有开发者在这轮问卷更新里重新作答，**2026 年 1 月 31 日之后没作答的 App 无法提交更新**。这一条跟本作是否上架无关，只要还想发版本就得先过。

### 其余表

| 字段 | 建议 |
|---|---|
| 内购 | **无**。代码里没有任何 StoreKit，App 内文案本身就写着「单人 · 离线 · 无内购 · 无广告」。**但 App 本身的售价还没定，见第 7 节** |
| App 隐私 | **不收集数据**。App 不发起任何网络请求，须与 `privacy.html` 一致 |
| 出口合规 | **NO**。`INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO` 已经写在工程里，App 完全没有加密，也没有网络代码 |

审核备注建议写清：本 App 完全离线，不发起任何网络请求，不收集任何数据，无账号、无广告、无内购，
也不申请任何系统权限。全部画面由代码绘制，19 种音效全部由代码实时合成，不含任何第三方素材或 SDK。
iPhone 上仅竖屏，iPad 支持四个方向。

---

## 7. ⚠️ 定价：两处记录互相矛盾，提审前必须先定

**代码侧是清楚的：全工程 grep `StoreKit` / `Product.products` / `SKPayment` 零命中，
没有登录、没有账号、没有付费墙、没有广告 SDK。** App 内文案也写着「单人 · 离线 · 无内购 · 无广告」。

**但 App 本身的售价，仓库里给不出答案，两处信号还互相矛盾：**

| 来源 | 说的是 |
|---|---|
| `_verify/DarkZone-commit.txt` | 「iOS 单机**买断制**」——即付费下载 |
| `fastlane/Fastfile:734` | `set_price` 的默认档位是免费（`"10000" # 默认免费`） |

也就是说「付费下载」和「免费下载」都有出处，**哪一个是决定，仓库里没有记录**。

**所以这份素材做了和撤离线同样的处理：**

1. **描述里一个字的购买、价格、免费、内购都没提。** 既没说「免费」，也没说「一次买断」——
   这两种说法各自都可能立刻变成假话。
2. **隐私政策里只写了与 Apple 之间的交易事实**（交易由 Apple 处理、我们拿不到你的 Apple ID），
   这条无论最后是付费下载还是免费都成立。
3. 第 6 节的表里「内购」一栏填「无」，这是代码事实，与付费/免费无关。

**提审前必须补的**：确定是付费 App 还是免费 App，然后：
- 若付费下载：描述里可以加一句「一次买断，无内购」
- 若免费：可以加一句「免费下载，无内购，无广告」

---

## 8. 截图

`TARGETED_DEVICE_FAMILY = "1,2"`，iPhone 与 iPad 两套都要，各 3-10 张。
**目前一张商店截图都没有。** `DarkZone/Screenshots/` 这个目录不存在，
`apps/darkzone/` 也是这一轮才建的。工程里唯一一张图是 `DarkZone/build/shots/menu.png`，
它在被 `.gitignore` 忽略的 `build/` 里，是开发期截图，不是商店素材。

（`DarkZone/.gitignore:17-23` 对这件事有明文约定：截图不进 App 仓库，「商店截图有自己的去处（apps/ 那边的公开仓库）」。）

按 Apple《截屏规范》（Screenshot specifications，2026-10-12 核对原文），**必填的只有两档**：

- iPhone：**带灵动岛的 iPhone（中等显示屏）**，竖屏 1206 x 2622 或 1179 x 2556
- iPad 13 寸，竖屏 2064 x 2752

6.9 寸（带灵动岛的 iPhone，大显示屏，1320 x 2868）不是必填。

竖屏截图，不要裁成横版。空状态、纯海报式截图会被拒。

建议的六张（**刻意不写任何难度评价、不写「侦察很划算」、不写手感**，理由见第 9 节）：

| 文件 | 标题 | 副标题 | 对应界面 |
|---|---|---|---|
| `01-menu.png` | 一步一步走进去 | 抵达撤离点，或者带着情报退出来 | 主界面 |
| `02-sticks.png` | 轻推是瞄准，推过去才开枪 | 右摇杆上画着那条线 | 关卡内，瞄准 |
| `03-scout.png` | 看，是按真实时间计费的 | 九秒配额按真实秒扣，换来的是一张全图情报 | 侦察中，视野锥与巡逻线 |
| `04-cover.png` | 掩体是双面的 | 挡视线也挡子弹，木箱还能被打碎 | 关卡内，掩体与木箱 |
| `05-stars.png` | 三颗星是三条独立的线 | 用时、被发现次数、命中率，各算各的 | 通关结算面板 |
| `06-levels.png` | 十张固定地图 | 同一关重打多少次都是那张图 | 行动列表与装备 |

---

## 9. 这份素材里，哪些卖点是被故意排除的

**这一节比前几节重要。改文案之前请先读完。**

`DarkZone/AGENTS.md` 的「差异化：这个 app 凭什么存在」列了四条。四条在代码里都成立，
但**作者自己在待办里写明了其中几项「证明了代价、证明不了价值」，所以素材里凡是带评价的部分全部拿掉了**。

### 排除项一：侦察「值不值这个价」——不写

`AGENTS.md:167-169` 逐字：

> - [ ] **人玩过之后再判断「侦察值不值这个价」**。现在能证明的只有它**有代价**
>       （配额按真实时间扣，K 节量得出来），**不能**证明它**值得**——
>       这是个产品判断，不是测试能回答的问题。

**所以素材里只写机制和代价：慢下来的是世界、不是时钟，配额按真实秒扣，而三星里有一颗就是用时。**
「所以你要用三星换一条命」这句是作者自己对**价值**的推断，**一个字都没有用**。
也不说它「改变了玩法」「是同类里没有的」。

（顺带说明：作者材料里**唯一**能用、且**确实被断言守着**的正面数字是
「真实时间 1 秒，侦察中世界只走 12.4 单位，正常是 92」，`LogicTests/main.swift:1486-1494` 有断言。
它量的是**单位位移花掉的真实时间**，也就是代价本身，所以描述里只体现为「按真实秒扣」，没有当卖点堆。）

### 排除项二：难度曲线——不写

`AGENTS.md:170-171` 逐字：

> - [ ] **难度曲线只量过第一关**（`AutoPilot` 只保证过得了教学关）。
>       后面九关没有任何机器或人的数据，「第 8 关会不会突然撞墙」目前是未知的。

`README.md:80-81` 也写着「AutoPilot 是探针不是 AI」「别拿它当通关机器人」。
**所以「难度循序渐进」「关卡编排得好」这类话一个字都没有。**

更彻底的一点：`DarkZone/Shared/Levels.swift:76-77` 要求改完关卡必须跑 `./LogicTests/balance.sh` 看探针数字，
**但 `LogicTests/` 里根本没有这个文件**（只有 `main.swift` 和 `run.sh`）。
也就是说难度曲线的探针数字**从来没有被生产出来**，既没有支持它的数据，也没有反对它的数据。
这一条我在素材里既不引用、也不暗示。

### 排除项三：手感——不写

`AGENTS.md:163-166` 逐字：

> - [ ] **摇杆回弹的手感**…能证明的只有「会过冲、一定停、掉帧不走样、不越过开火线」（S 节 16 条断言），
>       **证明不了「弹得舒服」**——`ω=26 / ζ=0.42` 是个有依据的初值，不是量出来的最优值。

**所以没有任何「摇杆调得很舒服」「手感好」的说法。** 素材里只写那条开火线**看得见**，
这是界面事实，不是手感评价。设置里的「摇杆手感」开关也只说它是一个开关。

### 排除项四：那条「换个种子结果一样」的零差异测量——不碰

`LogicTests/main.swift:2104-2111` 里有一条作者自己的零差异断言：

> ★ 换个 seed 结果一样（种子的唯一用途是脱困方向，而这一局没卡过）

它是**探针内部随机数**的测量，说的是「这一局两局其实是同一局」，
跟游戏本身无关，但**它是作者材料里唯一一条字面上的「测出来没有差别」**。
素材里一个字都没有碰它——它既不适合做卖点，也不该被当成缺陷。

### 用掉的（每条都能在代码里指出位置）

| 卖点 | 代码依据 | 用在哪 |
|---|---|---|
| 一枪就死，玩家没有血量字段 | `Player` 只有 `alive`，`AGENTS.md:35` | 推广文本、副标题、描述、FAQ、截图 01 |
| 敌人举枪 0.40 到 0.80 秒 | `Entities.swift:120-132` 的 `aimDelay` | 描述、FAQ |
| 开火线（轻推瞄准、推过才开枪） | `GameConfig.swift:81` `fireThreshold = 0.78` | 描述、FAQ、截图 02 |
| 侦察的机制与代价 | `scoutTimeScale = 0.12`、`scoutBudget = 9.0`、`maxMarks = 3` | 描述、FAQ、截图 03 |
| 掩体双面、木箱可碎、水泥墙不可碎 | `crateHealth = 6`、`wallIndestructible = -1` | 描述、FAQ、截图 04 |
| 不必清场，三种目标 | `eliminate` / `reach` / `retrieve` | 描述、FAQ |
| 四种敌人、五把武器、四把可选 | `Entities.swift:55`、`Weapons.swift:15-20` | 描述、FAQ |
| 三颗星三条独立线 | `Scoring.swift:9-12`、`:77-84` | 描述、FAQ、截图 05 |
| 十张固定地图 | `Levels.swift:78-148` 固定种子 | 描述、FAQ、截图 06 |
| 全程离线、无账号、无内购、无广告、无权限 | 零网络符号、零依赖、零 `*UsageDescription` | 全篇 |

**没有引用任何竞品名或品类名**，关键词里也没有（「硬核」是品类形容，不是店名）。
全部文案为本作原创，素材全部来自本仓库。

---

## 10. 提审前必须先解决的三件事（都不是文案问题）

1. **工作区还没提交。** `DarkZone/` 的 git 状态是「有未提交改动 + 一个未跟踪文件」：
   `AGENTS.md`、`ContentView.swift`、`Haptics.swift`、`GameView.swift`、`Progress.swift`、`SettingsView.swift`、
   `LogicTests/main.swift`、`run.sh`、`README.md` 都被改过，`DarkZone/Shared/StickSpring.swift` 是新文件。
   文档描述的是**工作区**的状态（15 个 Shared 文件、1210 条断言、19 节），比最后一次提交要新。
   **如果归档是从 HEAD 切的，切出来的会是另一个 App**（18 节、1192 条断言、没有 StickSpring、设置里也没有摇杆手感）。
   先确认要发布的是哪一棵树，再归档。
2. **没有 `PrivacyInfo.xcprivacy`。** `AGENTS.md:172` 把它记成「上架若需要声明 API 用途再加」。
   本 App 用到了 `UserDefaults`，而它本身属于需要声明理由的 API（应用自身设置，理由代码 `CA92.1`），
   所以**审核可能要求补一份隐私清单**。这一条我无法从源码判断苹果当前的要求，标成**可能的提交阻塞项**。
3. **价格没定**，见第 7 节。
