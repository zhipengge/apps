# 空中绞杀 (SkyStrike) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。
> **这份素材刻意没有任何手感、难度曲线或「比同类强」的评价，理由见第 9 节。改文案之前先读那一节。**

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **空中绞杀** | 弹幕射击、打飞机、雷电（通称易被占） |
| 名称（English 本地化） | **SkyStrike** | Bullet Hell、Sky Shooter |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.SkyStrike` | 任何旧 ID |
| SKU | `skystrike-20261010` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「空中绞杀」。

备选店名（创建时报名被占再用）：

- 空中绞杀战
- 弹幕绞杀
- SkyStrike Shooter

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

**注意：App 本身没有任何本地化。** 工程里 `developmentRegion = zh-Hans`，但**没有 `.xcstrings`、没有 `.strings`、没有 `Localizable`**，
`Views/` 下的用户可见字符串全是中文硬编码。所以如果给 English 也建一份商店本地化，
英文用户看到的是「英文描述 + 中文界面」。要么这轮只上简体中文，要么等界面做完英文化再补。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
障碍挡你也挡敌人，好东西就藏在后面。自动开火，单手拖动；贴着子弹飞能攒能量，攒满了由你决定什么时候放。全程离线，无广告无体力。
```

**字符数：63 / 170**

### English

```
Barriers block everyone's bullets and the good stuff hides behind them. Auto-fire, one thumb, and a charge you release yourself. Fully offline, no ads, no energy.
```

**字符数：162 / 170**

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
空中绞杀是一款竖屏弹幕射击游戏。单手拖动就能玩，机炮自动开火，你只管走位和取舍。全程离线，没有账号，没有广告，没有体力。

【操作】
- 按住屏幕任意位置拖动，机体跟着手指走
- 自动开火，不需要瞄准
- 竖屏单手，一局几分钟，通勤路上也能打

【核心机制：障碍】
- 可破坏的障碍同时挡住你和敌人的子弹
- 好东西就藏在障碍后面，但并非每个障碍都有货
- 待在障碍后面还能让护盾自己回满
- 继续打敌人还是分火力砸开障碍，每一波都要做这个取舍

【贴着子弹飞】
- 擦弹的判定半径比被击中的半径大得多，从子弹边上蹭过去就有分
- 擦弹同时给蓄力条充电
- 蓄力满了不会自动放：手指点一下才放出去，清掉周围一圈的敌人子弹
- 什么时候放是你的决定，不是系统的决定

【成长】
- 火力等级 1 到 5，靠捡火力道具升
- 进化 0 到 3 级：这一局攒下来的底子，挨打也不会掉，升级时机体在画面上会变大
- 连击最高 3 倍分数，但漏掉一个敌人不只少打一个，还会扣分并打断连击

【八种道具】
- 火力 / 护盾 / 清屏 / 吸附 / 金币 / 修复
- 另有两种限时特殊武器：导弹（带溅射）与激光（穿透），各自持续几秒

【三种模式】
- 战役：40 波，每 10 波一个 Boss，打穿算通关
- 无尽：难度一路上涨，看你撑到第几波
- Boss Rush：跳过杂兵，四个 Boss 连打

【四种机体】
- 隼：射速最快，弹道直，默认可用
- 扇：三向扇形，清杂兵最舒服，4 颗星解锁
- 芒：穿透一条线，单发最疼，12 颗星解锁
- 寻：自动追踪最近的敌人，24 颗星解锁
- 星数只用来解锁机体，不卖数值，没有抽卡

【评分】
- 每局按走得远近和挨打多少评 1 到 3 星，不看命中率
- 一波敌人一个都没漏就是完美波次，回复 1 点生命
- 机体初始 5 点生命

【中途接着打】
- App 退到后台时会存下这一局的现场，回到游戏可以接着打
- 这份现场保留 3 天

【剧情与主题】
- 开场三段演出、四个 Boss 各一段登场宣言、五段过场、一个结局
- 五套配色主题随波次推进更换，只影响颜色和一行文案

【分享】
- 结算生成一张战绩卡：分数、星级、击杀、受伤次数、存活时间
- 通过系统分享面板发出，发到哪由你决定，不点它什么都不会离开设备

【一次买断】
- 下载即完整版：战役全部 40 波、无尽模式、Boss Rush
- 没有广告，没有体力，没有订阅，**没有内购**

【隐私与素材】
- 不收集任何数据，App 里没有任何网络代码
- 全部进度只存在这台设备上，删除 App 即清空
- 音效由代码实时合成，画面全部由代码绘制，不含任何第三方素材或 SDK

【系统要求】
需要 iOS 17.0 或更高版本。iPhone 上仅竖屏，iPad 上支持竖屏与倒置竖屏。界面为中文。
```

**字符数：1246 / 4000**

### English

```
SkyStrike is a portrait bullet-hell shooter. Drag with one thumb, the guns fire on their own, and all you manage is positioning and priorities. Fully offline: no account, no ads, no energy.

[Controls]
- Hold anywhere and drag; the ship follows your finger
- Auto-fire, so there is no aiming to do
- Portrait and one-handed; a run fits into a commute

[The core mechanic: barriers]
- Destructible barriers stop your bullets and the enemy's alike
- The best pickups are hidden behind them, but not every barrier hides something
- Staying behind cover also refills your shield
- Keep shooting enemies or divert fire into a barrier? Every wave asks that question

[Flying close to bullets]
- The graze radius is much larger than the radius that kills you, so slipping past a bullet scores
- Grazing also charges your meter
- A full meter does not fire by itself: a tap releases it, clearing enemy bullets in a ring around you
- When to spend it is your decision, not the game's

[Growing stronger]
- Weapon level 1 to 5, raised by picking up firepower
- Evolution, 0 to 3: built up over the run, never lost when you are hit, and the ship visibly grows as it rises
- Combo multiplier up to 3x score, and letting an enemy escape costs points and breaks the combo

[Eight pickups]
- Firepower, shield, screen clear, magnet, coins, repair
- Plus two timed special weapons: a missile with splash damage and a piercing laser, each lasting a few seconds

[Three modes]
- Campaign: 40 waves, a boss every 10, and clearing it is a win
- Endless: difficulty keeps climbing until you fall
- Boss Rush: no chaff, four bosses back to back

[Four ships]
- Falcon: the fastest straight shots, available from the beginning
- Spreader: a three-way fan that clears packs, unlocked at 4 stars
- Laser: pierces in a line and hits hardest per shot, unlocked at 12 stars
- Homing: chases the nearest enemy, unlocked at 24 stars
- Stars only unlock ships. Nothing is sold for power, and there is no gacha

[Rating]
- Each run earns 1 to 3 stars for how far you got and how little you were hit, never for accuracy
- Clear a wave with no enemy escaping and you restore 1 health
- Ships start with 5 health

[Picking up where you left off]
- When the app goes to the background it saves the run, and you can resume it
- That snapshot is kept for 3 days

[Story and themes]
- Three intro scenes, a declaration as each of the four bosses arrives, five interludes and an ending
- Five colour themes that change as the waves progress; colour and one line of text only

[Sharing]
- A run ends with a score card: score, stars, kills, hits taken, survival time
- Send it through the system share sheet to wherever you like; if you never tap it, nothing leaves the device

[Free and full version]
- Free to download, with campaign waves up to wave 8
- One purchase unlocks the full version: all 40 campaign waves, Endless and Boss Rush
- No ads, no energy, no subscription
- Restore Purchases brings it back on a new device at no extra charge

[Privacy and assets]
- Collects nothing, and there is no networking code in the app
- All progress stays on this device; deleting the app clears it
- Sound effects are synthesised in code and all artwork is drawn in code, with no third-party assets or SDKs

[Requirements]
iOS 17.0 or later. Portrait only on iPhone; portrait and upside-down portrait on iPad. The interface is in Chinese.
```

**字符数：3395 / 4000**

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
竖屏单手弹幕射击
```

**字符数：8 / 30**

### English

```
Portrait bullet-hell shooter
```

**字符数：28 / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
空战,单机,飞机,离线,无广告,买断,闯关,无尽,机体,连击,弹雨
```

**字符数：33 / 100**

### English

```
arcade,retro,offline,premium,wave,combo,shmup,danmaku,bullet hell,spaceship
```

**字符数：75 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/skystrike/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/skystrike/privacy.html` |
| 营销 URL | 留空 |

技术支持是**版本级**字段（改它要跟新版本一起提审），隐私政策是 **App 级**（要有待发版本才能改）。
这两个 URL 一旦提审就不好改了，提审前先确认目录名。

**营销 URL 是可选字段，这里刻意留空。** 原来的草案填的是 `https://zhipengge.github.io/apps/skystrike/`，
但 `apps/skystrike/` 下**没有 `index.html`**，填了就是 404。要填就先补一个落地页，否则留空。

`apps/` 是独立仓库 `zhipengge/apps`，Pages 已经开着。**`apps/skystrike/` 的这两个页面现在返回 200**
（这一条是本轮之外的核查结论，提审前再确认一次即可）。

---

## 6. 类别、评级、隐私问卷

| 字段 | 建议 |
|---|---|
| 主要类别 | 游戏 / Games，子类 **动作 / Action** |
| 内购 | **无。** 2026-10-16 改成**付费下载（¥6 一口价，价格点 10016）**，见下 |
| 年龄分级 | 抽象的几何图形空战。问卷里的「卡通或幻想暴力」按实际作答，以 Connect 判定结果为准 |
| App 隐私 | **不收集数据**。App 里没有网络代码，须与 `privacy.html` 一致 |
| 出口合规 | **NO**（`INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO` 已写在工程里；App 完全没有加密代码） |

审核备注建议写清：本 App 不发起网络请求、不收集任何数据，没有账号体系。
**一次买断的付费下载，下载即完整版，没有任何内购或订阅。**
全部音效由代码实时合成，全部画面由代码绘制，不含任何第三方素材或 SDK。
iPhone 与 iPad 均为竖屏，不支持横屏。

### 次要类别为什么留空（2026-10-16，两个原因叠加）

原来写的是「游戏 / Games，子类 街机 / Arcade」。这个值**双重不可能**：

1. **ASC 里没有「街机」这个子类。** 实测 `/v1/appCategories` 给的 iOS 游戏子类只有
   动作 / 冒险 / 棋牌 / 卡牌 / 赌场 / 休闲 / 家庭 / 音乐 / 拼图 / 竞速 / 角色扮演 /
   模拟 / 体育 / 策略 / 问答 / 文字 —— **`ARCADE` 不在其中**。
   （`api.py fill` 报的「对不上类别…没有相近的」说的是这件事，它**拒绝**挑一个「差不多」的。）
2. **就算有也不能选。** 主类别已经是「游戏」，而苹果**不允许同一个类别选两次**
   —— DarkZone 2026-10-14 真写时被拒过：`HTTP 409 You may not select the same category
   twice for your app.` 次要类别在 ASC 是**可选**的，留空不影响提交。
   （要填只能挑一个**非游戏**的顶级类别，比如娱乐 / Entertainment。）

第 1 条是「工具报的那句话」，第 2 条是「为什么连换一个子类也不行」——
**只看第 1 条会往「换个存在的子类」那个方向修，而那个方向本身就是堵的。**

### 定价：2026-10-16 改成付费下载（¥6），原方案作废

**原来写的是**「免费下载 + ¥18 一次性内购解锁完整版」，商品 ID
`com.gezhipeng0201.SkyStrike.full`，并注明「上架前必须先把商品配好」。

**2026-10-16 复核时发现这条路走不通**，三件事叠在一起：

1. **商品根本没配**（`AGENTS.md:227` 记着），而 `Entitlements.swift:37` 是
   `isFullVersion = !productLoaded || purchased` —— **商品拉不到就全开**。
   这条兜底本身是善意的（`AGENTS.md:44-46`：「宁可不收钱，也不能让玩家打开是残废版」），
   但后果是**付费墙从不出现**，而描述里却写着它。
2. **官方 API 不允许创建内购**。实测：

       POST /v1/inAppPurchases
       → HTTP 403: The resource 'inAppPurchases' does not allow 'CREATE'.
                   Allowed operation is: GET_INSTANCE

   和「新建 App」是同一个形状——**只能用 Safari 或人工**。
3. 描述里那段【免费与完整版】是**已经上线**的（2026-10-16 读线上确认），
   也就是商店页在承诺一个玩家看不到的付费墙。

**改成付费下载 ¥6 一口价**（价格点 `10016`，中国区；其他区由苹果自动换算）。
连带改动：

- 描述里【免费与完整版】→【一次买断】（**已改**，见本文件上部那个代码块）
- **代码不用改**：商品不存在 → `productLoaded` 为假 → `isFullVersion` 为真 →
  全部 40 波开放、付费墙不出现，**正好就是付费下载该有的行为**
- ⚠️ **但 App 内「恢复购买」那一行要处理**：`SettingsView.swift` 的 `links` 里
  它是**无条件显示**的，点下去只会说「没有找到可恢复的购买」——一个死按钮。
  建议按 `entitlements.paywallAvailable` 加个判断把它藏掉，但那要改代码、
  重新构建并**重新上传构建**，本轮没动。

**年龄问卷有一项需要你亲眼确认。** 全部画面是代码绘制的几何图形，资源目录里除了 AppIcon 没有任何位图，
这一条是可核实的。但**「击中敌机那一刻的画面是什么样」本轮没有逐帧读绘制代码**，
所以「卡通或幻想暴力」那一栏我不替你答。上架前在真机上打一局看清那一下再作答。

---

## 7. 截图

`TARGETED_DEVICE_FAMILY = "1,2"`，iPhone 与 iPad 两套都要，各 3-10 张。

### 已经有的：iPhone 5 张

`apps/skystrike/screenshots/iphone/` 下 5 个文件，**全部 1320 x 2868**（iPhone 6.9 寸那一档）：

| 文件 | 内容 |
|---|---|
| `01-menu.png` | 主菜单：三种模式与机体一览 |
| `02-dense.png` | 战斗中：密集弹幕 |
| `03-barriers.png` | 可破坏的障碍与障碍后的道具 |
| `04-boss.png` | Boss 战：满屏弹幕与 Boss 血条 |
| `05-result.png` | 结算：三星、完美波次、战绩卡 |

### 还缺的：iPad 一整套

**目前一张 iPad 截图都没有**，`screenshots/` 下没有 `ipad/` 目录。
iPad 这一套是 13 寸，**2064 x 2752**，3-10 张。这是提交前的硬缺口。
`AGENTS.md:225` 把它列为待办，本轮代码侧核查确认它仍然没做。

竖屏截图，不要裁成横版。空状态、纯海报式截图会被拒。

### 建议补拍的两张

现有 5 张覆盖了菜单、弹幕、障碍、Boss、结算，**没有一张拍到这一作真正独有的东西**。
建议加：

- `06-charge.png` 蓄力条满格、手指点下去那一瞬间：清掉周围一圈子弹
- `07-graze.png` 机体贴着弹幕边缘飞：擦弹的判定圈与中弹判定圈的对比

---

## 8. 这份素材里，哪些卖点是被故意排除的

**这一节比前几节重要。改文案之前请先读完。**

### 先说结论：这个 app 没有「差异化」那一节

`SkyStrike/AGENTS.md` 里**没有**名叫「差异化：这个 app 凭什么存在」的小节，也没有等价标题
（grep `差异化` 只命中 `AGENTS.md:103` 一句行内的话）。最接近的是 `AGENTS.md:99-103`，
作者在那里写的是一句取舍声明，逐字：

> **不砍**：障碍机制是本作和上述任何一款都不同的地方，是差异点不是冗余

这句话本身是可用的，而且素材里确实用了——障碍机制在推广文本、描述、FAQ 里都占主要位置。
但**它只是一句设计声明，没有配套的测量**，所以素材里只描述机制本身（挡双方子弹、可打碎、藏道具、可回盾），
**不写任何「所以它比同类好玩」之类的结论。**

### 排除项一：手感——一个字都不写

`AGENTS.md:203-206` 逐字：

> ### 待验证
>
> 以上都是设计推理 + 逻辑测试，**真机手感还没验过**。
> 按 game-design 的最后一条：任何一次改动之后必须真的玩一遍。

`AGENTS.md:229` 又写了一遍：「上架前用 balance.sh 再核一遍难度曲线（探针是模拟玩家，真机手感要另外验证）」。

**作者自己声明手感未在真机验证过。** 所以描述里没有「手感顺滑」「打击感强」「弹幕密度刚好」任何一句。

### 排除项二：难度曲线——不写

同一处待办里，作者把难度曲线的复核对到了上架前还没做。素材里没有「难度循序渐进」「曲线平滑」这类话。
`AGENTS.md:221` 那句「逻辑测试 166 项全通过」也已经过时（`LogicTests/main.swift` 在那之后被改过），
**所以素材里一个字的测试数量都没有引用**——要用就先跑一遍拿真实数字。

### 排除项三：命中停顿——绝对不能写成「打击感」

`GameConfig.swift:24-27` 逐字：

> 试过「每次命中停 2 帧」和「每次击杀停 3 帧」——自动开火之下这两个都是一秒好几次的事件，
> 加起来的降速超过 25%，玩家感觉是「卡」不是「爽」。

`AGENTS.md:176-179` 重复了同一条。**这是作者自己测出来的负效果**，所以命中停顿在素材里一个字都没有，
连它实际存在的两处（碎障、受伤）也没有拿出来说。

### 排除项四：命中率——不写评分，但也不写成优点

`GameConfig.swift:210-216` 逐字：

> 一开始用的是命中率，实测下来是个错误指标：本作是自动开火，子弹会一直往外打，
> 所以「命中率」实际衡量的是「有多少时间正好有敌人飘到我的正前方」——跟玩家打得好不好毫无关系，
> 玩家根本没有瞄准这个动作。

素材里的处理是：**只说「不看命中率」，并且给出理由（自动开火，没有瞄准这个动作）**。
它出现在描述和 FAQ 里，是因为玩家会问「为什么没有命中率」，
不是作为卖点——它是一个被证伪后移除的指标，不是设计亮点。

### 排除项五：三条「测出来是坏的、后来改掉了」的记录——不碰

作者的材料里有若干「原来是这样，实测发现是坏的，所以改了」的记录，全部**只当作历史，不当卖点**：

| 位置 | 原话要点 | 素材里的处理 |
|---|---|---|
| `GameCore.swift:709-718` | 漏怪扣血时代，伤害的 3.7/4.8 来自漏怪、只有 1.2 来自中弹，「那是塔防，不是弹幕射击」 | 只写「漏掉一个敌人会扣分并打断连击」，**不写「我们把死因改正过来了」** |
| `GameConfig.swift:142-145` | 手指速度上限原来是 300，「手指一快飞机就掉队…全程落后 170 单位」 | 一个字都不提跟手感有关的数值 |
| `Levels.swift:99-114` | 最终 Boss 原来要打 43 秒；旧的难度曲线「是一堵墙不是曲线」 | 只写「战役 40 波，每 10 波一个 Boss」，**不写难度** |

### 用掉的（每条都能在代码里指出位置）

| 卖点 | 代码依据 | 用在哪 |
|---|---|---|
| 自动开火、拖动走位 | `GameConfig.swift:146` `playerSpeed = 1500` | 推广文本、描述、FAQ |
| 可破坏障碍挡双方子弹、藏道具 | `GameConfig.swift:184-189`、`Entities.swift:264-267` | 推广文本、描述、FAQ、截图 03 |
| 障碍后回盾 | `GameConfig.swift:77`、`GameCore.swift:228` | 描述、FAQ |
| 擦弹（判定圈更大、给分、充电） | `GameConfig.swift:36-40`、`GameCore.swift:592-593` | 描述、FAQ、建议截图 07 |
| 蓄力条手动释放（点按而非拖动） | `GameConfig.swift:86-91`、`GameView.swift:111` 的 12pt 阈值 | 推广文本、描述、FAQ、建议截图 06 |
| 火力 1-5 与进化 0-3 | `Entities.swift:83-91`、`GameConfig.swift:65` 阈值 | 描述、FAQ |
| 三种模式 | `Levels.swift:73-88` | 描述、FAQ |
| 四种机体、射速与解锁星数 | `Entities.swift:44-71` | 描述、FAQ、截图 01 |
| 八种道具 | `Entities.swift:311-341` | 描述、FAQ |
| 连击最高 3 倍、漏怪扣分 | `GameConfig.swift:228-232` | 描述、FAQ |
| 星级只看距离与挨打 | `GameState.swift:194-207` | 描述、FAQ |
| 完美波次回 1 血、初始 5 血 | `GameCore.swift:1340-1345`、`GameConfig.swift:148` | 描述、FAQ |
| 中途可接着打、保留 3 天 | `RunSnapshot.swift:29`、`ContentView.swift:92-97` | 描述、FAQ |
| 五套主题、剧情四层 | `Levels.swift:15-52`、`Story.swift:47-113` | 描述、FAQ |
| 9 种音效代码合成、`UIBackgroundModes` 无关 | `SoundSynth.swift:15-24`、`SoundEngine.swift:50` | 描述、FAQ |
| 战绩卡分享 | `ShareCard.swift:126-139`、`GameOverPanel.swift:204-211` | 描述、FAQ |
| 全程离线、无账号、无广告、无权限、无震动 | 零网络符号、零依赖、零 `*UsageDescription`、零触感 API | 全篇 |

**没有引用任何竞品名或品类名。** 素材里唯一提到「同类」的地方是「和上述任何一款都不同」这句的转述，
而且**没有写进任何一段面向用户的文案**。
全部文案为本作原创，素材全部来自本仓库。

---

## 9. 提审前必须先解决的四件事（前两件不是文案问题）

1. **商品还没在 App Store Connect 配好。** 见第 6 节。不配好就提审，审核看到的是全开版。
2. **iPad 截图一整套都没有。** 见第 7 节。`TARGETED_DEVICE_FAMILY = "1,2"`，这一套是必填。
3. **分享面板里的「存储图像」需要真机确认一次。** 分享出去的是一张 `UIImage`，
   而 App **没有声明 `NSPhotoLibraryAddUsageDescription`**，代码里也没有任何相册 API。
   本轮**无法静态判断**：在系统分享面板里选「存储图像」会走系统相册扩展、还是会因为缺权限而失败。
   这条不影响隐私声明（App 自己没有读相册的能力），但值得真机点一次确认体验。
   `AGENTS.md:228` 已经把它列进真机清单。
4. **English 商店本地化与中文界面不匹配。** 见第 0 节末。要么补界面英文化，要么这轮只上中文。
