# 像素枪火 (PixelGunfire) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。
> **这份素材刻意没有使用「冲锋槽」作为卖点，理由见第 9 节。改文案之前先读那一节。**

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **像素枪火** | 像素枪火 PixelGunfire（太长） |
| 名称（English 本地化） | **PixelGunfire** | Pixel Gunfire、Pixel Gun |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.PixelGunfire` | 任何旧 ID |
| SKU | `pixelgunfire-20261012` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「像素枪火」。

备选店名（创建时报名被占再用）：

- 像素枪火 PixelGunfire
- 像素枪火 横版射击
- 像素枪火 单机跑轰

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

**注意：App 本身没有任何本地化。** 工程里没有 `.lproj`、没有 `Localizable.strings`、也没有 `.xcstrings`，
关卡名、菜单、结算页全部是中文硬编码。所以如果给 English 也建一份商店本地化，
英文用户看到的是「英文描述 + 中文界面」。要么这轮只上简体中文（主要语言就是它），要么等界面做完英文化再补。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
一个拇指就能玩的竖屏跑轰。按住屏幕跑，上滑跳，右下角滑铲。8 个关卡，一关 6 分钟，全程离线，没有账号，没有广告，没有内购。
```

**字符数：63 / 170**

### English

```
A portrait run-and-gun you play with one thumb. Hold to run, swipe up to jump, slide with the corner button. Eight levels, offline.
```

**字符数：131 / 170**

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
像素枪火是一个竖屏、单机、离线的横版跑轰。8 个关卡：丛林前哨、河谷渡口、弹药库、峡谷铁桥、雪原雷达站、熔岩坑、指挥中心、兵工厂。一关大概 6 分钟，一个拇指就能玩，全程不需要横屏。

【只有四个动作，全都只管位置】
- 按住屏幕任意位置，角色朝你手指所在的水平位置跑
- 向上滑动跳跃，按住越久跳得越高
- 右下角的按钮是滑铲，滑铲前段有无敌帧
- 左上角是暂停

没有虚拟摇杆，没有方向键，也没有开火键。

【为什么没有开火键】
因为瞄准不是这个游戏要你做的事。枪会自动锁定射程内的目标并自动开火，换弹也是自动的。
你的每一个决策都是站位和时机：什么时候往前压、什么时候跳、什么时候滑铲穿过去。压力来自位置，不来自按键。

【没有必要捡东西】
关卡里没有武器箱，也没有弹药补给。你带进去的那把枪就是全程那把，子弹无限。
4 把武器是步枪、霰弹枪、冲锋枪和激光，各自有各自的性格：霰弹扇面宽、冲锋枪快而飘、激光能贯穿。

【挨一下就掉一条命】
横版跑轰的老规矩，没有血条。每一关 5 条命，掉光就得重来。滑铲的无敌帧因此是这套操作里最值钱的一格。

【7 种敌人，一个三阶段 boss】
敌人的种类决定它怎么走位、怎么开火，所以每一关的压迫感不一样。加上一个三阶段的 boss。

【评级 S / A / B / C】
三项加权：时间 0.34、存活 0.30、冲锋槽 0.36。分数和字母完全由这三项算出，没有随机。S 级还有一个门槛：本关冲锋槽的平均值不低于上限的 62%。

【结算页会告诉你死在哪】
死亡按原因归类，最主要的那一个会得到一条具体建议，指向具体动作，而不是「多加练习」这种话。只有一条，因为一次给三条等于没给。

【可以让机器人替你打一局】
演示模式有 5 个技术档位，从很菜到很稳。想看看某个敌人怎么出招、或者想先看看这一关长什么样，用这个就行。演示局不记成绩，不会污染你自己的记录。

【画面和声音都是代码生成的】
所有画面由代码实时绘制，所有音效由代码实时合成，仓库里没有一张图片素材、没有一个音频文件。不含任何第三方素材或 SDK。

【隐私】
- 不收集任何数据，App 不发起任何网络请求，飞行模式下全部功能可用
- 没有账号，没有注册，没有广告，没有内购：8 个关卡从第一次打开起就全部可以打
- 没有分析、崩溃上报或追踪 SDK，工程里没有任何第三方依赖，框架构建阶段是空的
- 不申请任何系统权限，系统不会为它弹出任何权限询问
- 进度只存在这台设备上（三个偏好设置键），删除 App 即清空

【系统要求】
需要 iOS 17.0 或更高版本。iPhone 上仅支持竖屏，iPad 上支持竖屏与上下颠倒。界面为中文。
```

**字符数：1130 / 4000**

### English

```
PixelGunfire is a portrait, single-player, offline run-and-gun. Eight levels: Jungle Outpost, River Ford, Ammo Depot, Canyon Iron Bridge, Snowfield Radar, Lava Pit, Command Centre and Arsenal. A level runs about six minutes, it plays with one thumb, and it never asks for landscape.

[Four actions, and all of them are about position]
- Hold anywhere and the character runs toward the horizontal position of your finger
- Swipe up to jump; the longer you hold, the higher you go
- The bottom-right button is a slide, and the first part of the slide has invincibility frames
- Top-left is pause

No virtual stick, no direction pad, and no fire button.

[Why there is no fire button]
Because aiming is not the thing this game asks you to do. The gun acquires targets in range by itself and fires by itself, and reloading is automatic.
Every decision you make is about position and timing: when to push forward, when to jump, when to slide through. The pressure comes from where you stand, not from which button you press.

[There is nothing to pick up]
Levels contain no weapon crates and no ammo pickups. The gun you go in with is the gun you finish with, and ammunition is unlimited.
The four weapons are a rifle, a shotgun, an SMG and a laser, and each behaves differently: the shotgun spreads wide, the SMG is fast and floaty, the laser pierces.

[One hit costs one life]
The old run-and-gun rule, and there is no health bar. You get five lives per level and running out means starting it again. That is why the slide's invincibility frames are the most valuable cell in the control scheme.

[Seven enemies and a three-phase boss]
The type decides how an enemy moves and how it shoots, so the pressure is not the same in every level. At the end of it all, a boss with three phases.

[S, A, B or C]
Three weighted terms: time 0.34, survival 0.30 and the charge gauge 0.36. The score and the letter come straight out of those three, with nothing random. S has one extra gate: your average charge over the level must be at least 62 percent of the maximum.

[The result screen tells you where you died]
Deaths are grouped by cause and the biggest one gets one concrete piece of advice, pointing at a specific action rather than at practice in general. Only one, because three at once is the same as none.

[A bot can play a level for you]
Demo mode has five skill tiers, from clumsy to steady. It is the way to see how a particular enemy behaves, or to look at a level before you commit to it. Demo runs deliberately do not record scores, so they cannot pollute your own results.

[Every pixel and every sound is generated in code]
All visuals are drawn at runtime and all audio is synthesized at runtime. The project contains no image assets and no audio files, and no third-party assets or SDKs.

[Privacy]
- Collects nothing and makes no network requests; every feature works in Airplane Mode
- No account, nothing to register, no ads and no in-app purchases: all eight levels can be played from the first launch
- No analytics, crash reporting or tracking SDKs, no third-party dependencies at all, and an empty frameworks build phase
- Requests no permissions, so the system never prompts you
- Progress lives on this device only, in three preference keys; deleting the app clears it

[Requirements]
iOS 17.0 or later. Portrait only on iPhone; portrait and upside-down on iPad. The interface is in Chinese.
```

**字符数：3408 / 4000**

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
一个拇指的竖屏跑轰
```

**字符数：9 / 30**

### English

```
One-thumb run-and-gun shooter
```

**字符数：29 / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
跑轰,横版射击,像素,单机,离线,无广告,闯关,枪战,街机,复古
```

**字符数：32 / 100**

### English

```
run and gun,shooter,offline,single player,arcade,pixel,platformer,no ads,retro,action
```

**字符数：85 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/pixelgunfire/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/pixelgunfire/privacy.html` |
| 营销 URL | 留空 |

技术支持是**版本级**字段（改它要跟新版本一起提审），隐私政策是 **App 级**（要有待发版本才能改）。
这两个 URL 一旦提审就不好改了，提审前先确认目录名。

营销 URL 是可选字段，`apps/pixelgunfire/` 下没有 `index.html`，填了就是 404，所以留空。

**这两个页面现在还是 404。** `apps/` 是独立仓库 `zhipengge/apps`，Pages 已经开着
（`apps/skystrike/privacy.html` 现在返回 200），但 `apps/pixelgunfire/` 还没进版本库。
提审前必须先提交并推送这一整个目录，否则 App Store Connect 填的隐私政策链接是空的。

---

## 6. 类别、评级、隐私问卷

### 类别

| 选项 | 主要类别 | 次要类别 | 理由 |
|---|---|---|---|
| A | 游戏 / Games，子类 **动作 / Action** | 游戏 / Games，子类 街机 / Arcade | 自动开火、躲避走位、一碰即死，是标准动作跑轰；同类作品多归在动作 |
| B | 游戏 / Games，子类 **街机 / Arcade** | 游戏 / Games，子类 动作 / Action | 一关 6 分钟、评分 S/A/B/C、反复刷成绩，街机味儿更重 |

`TARGETED_DEVICE_FAMILY = "1,2"`，主要类别必须选游戏，子类只能选一个。

### 年龄分级（需要你定）

问卷不让你直接选档位，是按题作答后由 Connect 判定。当前档位是 4+ / 9+ / 13+ / 16+ / 18+ 五档。

这个 App 的实际情况：像素风格的虚构战斗，玩家会死、敌人会死；没有现实武器还原，
没有恐怖、赌博、酒精烟草毒品、色情、脏话、用户生成内容、聊天、广告或网页浏览，也不联网。

**⚠️ 有一点必须由你亲眼判断，我不替你答：**

`Shared/Entities.swift:319` 里有一个粒子效果：`case blood // 敌人碎裂：向前后两侧`。
也就是说**敌人被打掉时会炸成一组粒子**，这个效果在代码里的名字就叫 blood。
它是不是像素美术意义上的「血」，以及问卷里的「血腥 / 卡通暴力」该怎么答，**取决于它在屏幕上看起来是什么样**。
这类效果在 9+ 和 13+ 之间往往就是这一项在决定，所以建议在真机上打死一个敌人，看清那一下再作答。

**另一个时间点要注意：** 苹果要求所有开发者在这轮问卷更新里重新作答，**2026 年 1 月 31 日之后没作答的 App 无法提交更新**。这一条跟本作是否上架无关，只要还想发版本就得先过。

### 其余表

| 字段 | 建议 |
|---|---|
| 内购 | **无**。代码里没有任何 StoreKit，App 内文案本身就写着「无内购无广告」。详见第 7 节 |
| App 隐私 | **不收集数据**。App 不发起任何网络请求，须与 `privacy.html` 一致 |
| 出口合规 | **NO**。`INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO` 已经写在工程里，App 完全没有加密，也没有网络代码 |

审核备注建议写清：本 App 完全离线，不发起任何网络请求，不收集任何数据，无账号、无广告、无内购，
也不申请任何系统权限。全部画面由代码实时绘制，全部音效由代码实时合成，不含任何第三方素材或 SDK。

**首次提交时要额外说明两件事：**

1. iPhone 上仅竖屏，不支持横屏；iPad 上也不支持横屏（只有竖屏和上下颠倒）。
2. `INFOPLIST_KEY_UIRequiresFullScreen = YES` 是上一个提交周期为消掉 ITMS-90474 上传拒绝而加的。
   这个键在 iOS 26 上已被 `UILaunchScreen` 的语义取代，**如果之后上传再被拒，先看这一条**，本轮没有动源码。

---

## 7. 内购与定价：代码里没有，文档里也没有

**全工程 grep `StoreKit` / `Product.products` / `SKProduct` / `SKPayment` 零命中。**
没有登录、没有账号、没有付费墙、没有广告 SDK、没有订阅。
App 自己的底部文案（`Views/MenuView.swift:268`）就写着：

```
八个手工设计的关卡，一百二十八发子弹同屏，无内购，无广告
```

后半句「无内购无广告」与代码完全一致，可以直接引用。
**前半句里的「一百二十八」不要引用**，理由见第 9 节。

`README.md` 和 `AGENTS.md` 里对价格零命中（没有任何定价记录），仓库里唯一的商业化陈述就是上面这句。
按仓库通行规则（iOS 应用免费分发），**方向是免费 + 无内购**，但这一条没有落在任何文档里，
**提审前请你确认一次**。描述里写了「没有内购」，只要你不动代码它就是真的。

---

## 8. 截图

`TARGETED_DEVICE_FAMILY = "1,2"`，iPhone 与 iPad 两套都要，各 3-10 张。
**目前一张商店截图都没有。** `PixelGunfire/Screenshots/` 下面只有一个空的 `raw/` 子目录，
而且 `Screenshots/` 被 `.gitignore` 忽略。仓库里去重后剩下的唯一一张截图是
`_verify/PixelGunfire/ipad-launch-uirfs.png`，那是验证 `UIRequiresFullScreen` 改动的证据，不是商店素材。

按 Apple《截屏规范》（Screenshot specifications，2026-10-12 核对原文），**必填的只有两档**：

- iPhone：**带灵动岛的 iPhone（中等显示屏）**，竖屏 1206 x 2622 或 1179 x 2556
- iPad 13 寸，竖屏 2064 x 2752

6.9 寸（带灵动岛的 iPhone，大显示屏，1320 x 2868）不是必填。

竖屏截图，不要裁成横版。**这个 App 的 iPad 版只有竖屏和上下颠倒，所以 iPad 那套也只能出竖屏截图。**
空状态、纯海报式截图会被拒。

建议的六张（**刻意不写任何难度评价、不写任何「冲锋槽改变了打法」式的效果宣称**，理由见第 9 节）：

| 文件 | 标题 | 副标题 | 对应界面 |
|---|---|---|---|
| `01-menu.png` | 一个拇指，八个关卡 | 一关 6 分钟，随时能停 | 主菜单 |
| `02-run.png` | 按住就跑，上滑就跳 | 没有开火键，也没有瞄准 | 关卡内，奔跑与跳跃 |
| `03-slide.png` | 滑铲前段无敌 | 挨一下就掉一条命，没有血条 | 关卡内，穿过弹幕 |
| `04-boss.png` | 七种敌人，一个三阶段 boss | 种类决定它怎么走位、怎么开火 | boss 战 |
| `05-result.png` | 结算告诉你死在哪 | 按原因归类，只给一条能改的建议 | 结算页 |
| `06-demo.png` | 也可以让机器人替你打 | 演示局不记成绩 | 演示模式，档位选择 |

---

## 9. 这份素材里，哪些卖点是被故意排除的

**这一节比前几节重要。改文案之前请先读完。**

`PixelGunfire/AGENTS.md` 的 §4 标题就叫「**差异化：冲锋槽（本作凭什么存在）**」，
第一句是「**这是这个 app 唯一值得存在的理由，不是装饰。**」

**但作者自己跑出来的平衡探针，判的正好相反。** `PixelGunfire/pgscratch/bal.txt`
（未提交的临时产物，`pgscratch/` 在 `.gitignore` 里）结尾逐字是：

```
  ✓ 挂机打不过：通过 0/8，平均冲锋 0.024
  ✗ 激进和保守的冲锋占比差不多（0.411 vs 0.345） —— 冲锋槽没在奖励推进，只是个装饰
  ✓ 敢冲的人打得更好：激进评级分 0.664 > 保守 0.515（+14.9%）
  ✓ 反应快的人打得更好：完美 8/8 ≥ 普通 8/8
  ✓ 普通玩家能打通全部 8 关

  ✗ 12 次卡住（地形/刷怪数据错误）：

══════════════════════════════════════════════════════════════
 结论：**2 项没通过** —— 冲锋槽不区分打法、有关卡卡住
══════════════════════════════════════════════════════════════
```

也就是**「冲锋槽不区分打法」这五个字，是作者自己的测量结论**。
探针源码 `LogicTests/Balance/main.swift:26-39` 把后果写得更清楚：
「如果保守型的评级、用时、存活都和激进型一样好，那冲锋槽就只是个装饰，整个差异化就是假的」。

**所以这份素材里，冲锋槽没有当成卖点。** 具体地说，以下这些话一个字都没有：

- 不说它「奖励推进」「让站着有代价」「改变了打法」「是同类里没有的」
- 不说「本作凭什么存在」「差异化」「核心机制」
- 不引用 `AGENTS.md` §4 里那张加减表当卖点，也不引用标题那句话
- 不引用探针里那条**通过**的项（「敢冲的人打得更好」）——它出自同一次运行，不能一半当真一半不当真

**留下的只有纯机械描述**（HUD 上那条槽涨落、挨一下扣多少、评级三项的权重、S 级的门槛），
因为玩家在屏幕上看得见它，而且这些值在当前代码里读得到；
描述里**没有任何一句说它会影响你怎么玩**。

**⚠️ 一个必须说清的前提：这份探针输出是旧的，我没有重跑。**
`bal.txt` 的时间戳是 10-11 07:31，而 `GameConfig.swift`（07:49）、`Weapons.swift`（07:50）、
`GameCore.swift`（08:01）、`Levels.swift`（07:49）、`Balance/main.swift`（08:02）都改在它**之后**——
也就是探针跑完 20 到 30 分钟后，作者才把 `Weapons.damage` 真正接到冲锋槽上、
把 `fullChargeRateBonus` 拆成独立出口。当前代码里这两处修复都在。

所以正确的说法是：**旧结果既不能证明它现在仍然失败，也完全不能证明它现在成立。**
要下任何结论，必须先跑一遍 `./LogicTests/balance.sh`。
**本轮没有跑**（它会在临时目录里编译，属于写操作），所以素材按「不提效果」处理。
**如果重跑之后它通过了，第 2 节的描述可以加一句，但请把结果贴给作者本人确认再用。**

**另外三条同样被排除的东西：**

| 说法 | 为什么不能用 |
|---|---|
| 「站着不动掉得比涨得快」 | **假的**。`GameConfig.swift:135-139`：`chargeDecayRate = 26`，而 `chargeGainRate = 34`。26 < 34，站着其实掉得比涨得慢。只有 `chargeRetreatRate = 52` 真的比增长快。`AGENTS.md` §4.2 自己把这条记成了已知不一致，**代码里没改** |
| 「128 发子弹同屏」 | App 内文案写着 128，但 `GameConfig.maxBullets = 260`。这个 128 追不到任何一个配置值上，所以两边都不用 |
| 「难度递进做得好」「平衡得刚好」 | 探针那次是失败结论，且已过期；本轮没重跑 `balance.sh`。没有测量支持的话不写 |

**还有一条本轮查到、但不写进素材的事实**（记录在案以免以后当成卖点）：

- 探针报了 **12 次卡住**，其中 8 次是挂机机器人在 `x=104.0` 不动（那是机器人不走路，不是关卡缺陷），
  4 次是保守型在 L3 `x=3100`、L4 `x=1920`、L6 `x=3180`、L7 `x=2120` 卡住。
  **L4 `x=1920` 和 `AGENTS.md` §3.4 里记成「已修」的那个坑在同一个坐标**，可能是回归。
  这一条我**没有对着当前代码核实**，所以素材里一个字都没提，但它是提审前值得先跑一遍的理由。

**用掉的（都是能在当前代码或工程文件里指出来的）：**

| 卖点 | 依据 | 用在哪 |
|---|---|---|
| 一碰即死，每关 5 条命 | 无血条设计、`DeathCause` 记录 | 描述、FAQ、截图 03 |
| 没有开火键，只操作位置 | 输入只有按住/上滑/滑铲/暂停四个 | 推广文本、副标题、描述、FAQ、截图 02 |
| 8 个手工关卡 + 关卡名 | `Shared/Levels.swift` 八关 | 描述、FAQ、截图 01 |
| 结算按死因给一条可执行建议 | `Views/ResultView.swift:183-227`、`DeathCause.advice` | 描述、FAQ、截图 05 |
| 演示局不记成绩 | `GameSession.swift:257-260`、菜单文案「演示局不记成绩」 | 描述、FAQ、截图 06 |
| 画面代码绘制、音效代码合成 | `Canvas`、`SoundBank.swift:220-252` | 描述、隐私政策 |
| 全程离线、无账号、无内购、无广告、无权限 | 零网络符号、零依赖、零 `*UsageDescription` | 全篇 |

**没有引用任何竞品名或品类名**，关键词里也没有。全部文案为本作原创，素材全部来自本仓库。
