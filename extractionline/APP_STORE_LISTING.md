# 撤离线 (ExtractionLine) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **撤离线** | 搜打撤、撤离射击（通称易被占） |
| 名称（English 本地化） | **ExtractionLine** | Extraction Line、Tarkov 类 |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.ExtractionLine` | 任何旧 ID |
| SKU | `extractionline-20261011` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「撤离线」。

备选店名（创建时报名被占再用）：

- 撤离线 搜打撤
- 撤离线 ExtractionLine
- 六分钟撤离线

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

**注意：App 本身没有任何本地化。** 工程里没有 `.lproj`、没有 `Localizable.strings`、也没有 `.xcstrings`，
界面文案全是中文硬编码（`Views/` 下直接写 `Text("...")`）。
所以如果给 English 也建一份商店本地化，英文用户看到的是「英文描述 + 中文界面」。
要么这轮只上简体中文（主要语言就是它），要么等界面做完英文化再补 English 本地化。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
撤离不是走到出口就结束，是站住 6 秒。而且充能中的撤离点会把附近的敌人全叫过来。一局 6 分钟，全程离线，没有账号，没有广告。
```

**字符数：64 / 170**

### English

```
Extraction is not reaching the exit, it is standing still for six seconds while the pad calls every enemy nearby. Six-minute raids, fully offline.
```

**字符数：146 / 170**

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
撤离线是一款俯视角的单机搜打撤。一局 6 分钟：从外圈进去，往里搜，能拿多少拿多少，然后在时间耗尽之前找到撤离点活着出来。没出来，身上带的一切就全留在里面。全程离线，没有账号，没有广告。

【操作】
- 浮动摇杆，手指落在屏幕哪里，杆心就在哪里，可以改成右手边
- 开火是自动的，准星里有敌人就打。你负责的是站位和走位，不是瞄准
- 换弹也是自动的，因为自动开火之下换弹时机根本不是玩家的决策
- 右下角三个按钮：按住持续开火、消耗品、背包
- 摇杆松开即停，来电横幅或切后台打断时输入也会正确复位

【撤离动作本身就是全场最紧张的战斗】
同类作品里撤离是一段安静的走路。本作是站住 6 秒。
而且充能中的撤离点会叫：半径 280 单位以内的敌人全部朝它来。这个距离比一屏还远，所以你总是看得见是谁被你自己叫来的。
已经在跟你交火的敌人不会被吸走，但一个正在开走的人，会把附近所有人都拉过来。

【什么时候走，有一个可以说出来的答案】
撤离窗口从外圈往中心收：
- 0:00 只有最外圈的常开口
- 1:00 中圈两个加库区正中一个。这是唯一一次能带着货从最深处走出去的机会，开 80 秒
- 2:30 中圈两个
- 4:00 外圈一个
任何时刻整张图至少有一个口是开的，所以永远不会出现此刻没有出口。只是那个口离得很远。

【地图是一个风险梯度场】
91 x 91 格，100 个房间，按距中心的距离分成外圈、中圈和库区。容器档次和敌人强度都跟着这个梯度走，越往里越肥，也越危险。
每一张图由一颗随机种子长出来：房间网格加随机 Prim 生成树，再加 30% 的额外连接，因为要有环才有绕后和撤退的路线。
可解性是构造上成立的，不是测出来大概能走通。同一颗种子永远长出同一张图。

【拾荒者是唯一会赢的敌人】
它不主动打你。它开你的箱子，把东西背在身上，然后走向撤离点离开这张地图。
单机游戏没有别的玩家，也就没有别人先到一步这件事。拾荒者把它补回来了：你慢了一步，箱子就是空的；你看见它背着东西往外走而没能拦住，那件东西你再也没机会拿到。

【噪音是一条独立的路线】
开枪加噪音，噪音决定敌人能听见你多远。噪音过阈值会派一次猎杀队，一局只派一次。
低语冲锋枪是全游戏唯一一把天生消音的枪，也是唯一能让你打完了噪音还是 0 的武器，数值上并不是最高的。这是本作里唯一一条可以完全绕开战斗的路线，代价是主动放弃更好的枪。

【死了会怎样】
身上带的一切留在里面。仓库里的东西不会丢，装备在出发那一刻就已经从仓库拿出来，不是死的那一刻才没的。
所以这一局带什么是一个真的问题，而不是走个流程。

【11 种敌人，37 种物品】
游荡者、哨兵、拾荒者、猎犬、步枪手、霰弹兵、狙击手、重甲兵、工兵、医护兵、猎杀队员。
它们共用同一台状态机，靠各自的参数决定行为转移。所以你学会的躲视野锥对 11 种都成立，不会有哪一种莫名其妙地例外。
37 种物品底子，五个稀有度，十几种词条：威力、射速、弹匣、射程、精准、护甲、减伤、轻量、容量、消音、脱战回血、移速。

【两条可读性红线】
任何能打中你的东西都在半个屏幕以内，不会有屏幕外飞来的子弹。
噪音半径和撤离吸引半径都必须大于一屏，因为感知不到的机制等于不存在。

【存档不会丢】
写临时文件，读回来校验，再把正式档降级为备份、原子替换上去。正式档坏了退备份，两个都坏了才当新档。
没有任何一条路径会因为存档坏了而让你失去仓库。

【隐私与素材】
- 不收集任何数据，App 不发起任何网络请求，飞行模式下全部功能可用
- 没有账号，没有广告，没有分析或追踪 SDK，工程里没有任何第三方依赖
- 不申请任何系统权限，系统不会为它弹出任何权限询问
- 存档只存在这台设备的沙盒里，删除 App 即清空
- 画面全部由代码绘制，15 个音效全部由代码实时合成，不含任何第三方素材或 SDK

【系统要求】
需要 iOS 17.0 或更高版本。iPhone 与 iPad 均可，iPhone 上仅支持竖屏。
```

**字符数：1671 / 4000**

### English

```
ExtractionLine is a top-down, single-player extraction shooter. One raid is six minutes: insert on the outer ring, push inward, take what you can carry, then reach an exit alive before the clock runs out. Fail, and everything you were carrying stays behind. Fully offline: no account, no ads.

[Controls]
- A floating stick that centres wherever your thumb lands, and can be moved to the right
- Firing and reloading are automatic; your job is positioning, not aiming
- Three buttons: hold to fire, consumable, backpack
- Releasing the stick stops you, and input resets if a call interrupts a drag

[Extraction is the tensest fight in the raid]
In this genre extraction is a quiet walk to the exit. Here it is standing still for six seconds.
A charging pad calls out: every enemy within 280 units heads for it. That is further than a screen, so you always see who you brought down on yourself.

[When to leave has an answer you can say out loud]
The windows close from the outside inward. At 0:00 only the far outer ring pad; at 1:00 two mid-ring pads plus the one dead centre in the vault, your only chance to walk out of the deepest part of the map with cargo, open for 80 seconds; at 2:30 the mid-ring pads; at 4:00 one outer ring pad.
At every moment at least one pad is open, so there is never a point where no exit exists.

[The map is a risk gradient]
91 by 91 tiles, 100 rooms, split by distance from the centre into an outer ring, a mid ring and a vault. Container quality and enemy strength follow that gradient: deeper is richer and deadlier.
Every map grows from a seed: a room grid plus a randomised Prim spanning tree with 30 percent extra connections, because you need loops to flank and to retreat. Solvability holds by construction, and the same seed always grows the same map.

[The scavenger is the only enemy that can win]
It does not attack you. It opens your containers, shoulders what it finds, and walks to an exit to leave the map.
A single-player game has no other players, so it has no someone got there first. The scavenger puts that back: if you are slow the container is already empty, and if you watch it carry your loot out and fail to stop it, that loot is gone.

[Noise is a route of its own]
Firing adds noise, and noise decides how far away enemies hear you. Cross a threshold and the map sends a hunter squad after you, once per raid.
The Whisper SMG is the one suppressed weapon and the only gun that lets you finish a fight still at zero noise; its numbers are not the best in the game. It is the one route that avoids combat entirely, and the price is giving up a better gun on purpose.

[What death costs]
Everything you were carrying stays behind. Your stash is safe: gear leaves the stash the moment you deploy, not the moment you die.

[11 enemies, 37 items]
Eleven enemy types share one state machine, so the sightline play you learn works against all eleven, with no exceptions. 37 item bases, five rarities and a dozen-plus affixes.

[Two readability rules]
Anything that can hit you is inside half a screen, so nothing shoots you from off-screen. The noise radius and the extraction attract radius are both larger than one screen, because a mechanic you cannot perceive does not exist.

[Your save cannot be lost]
Every save writes to a temporary file, verifies it, then demotes the old save to a backup and atomically replaces it. A bad save falls back to the backup, and only if both are bad does the app start fresh.

[Privacy and assets]
- Collects nothing and makes no network requests; every feature works in Airplane Mode
- No account, no ads, no analytics or tracking SDKs, no third-party dependencies
- Requests no permissions, so the system never prompts you
- The save lives in the app sandbox; deleting the app clears it
- All artwork and all 15 sound effects are generated in code

[Requirements]
iOS 17.0 or later. iPhone and iPad. Portrait only on iPhone.
```

**字符数：3918 / 4000**（离上限只剩 82，改写时留意）

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
六分钟一局的俯视角搜打撤
```

**字符数：12 / 30**

### English

```
Six-minute extraction shooter
```

**字符数：29 / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
搜打撤,撤离,射击,单机,离线,无广告,俯视角,枪战,生存,roguelike
```

**字符数：39 / 100**

### English

```
extraction shooter,offline,single player,top down,roguelike,loot,twin stick,no ads,indie,survival
```

**字符数：97 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/extractionline/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/extractionline/privacy.html` |
| 营销 URL | 留空 |

技术支持是**版本级**字段（改它要跟新版本一起提审），隐私政策是 **App 级**（要有待发版本才能改）。
这两个 URL 一旦提审就不好改了，提审前先确认目录名。

营销 URL 是可选字段，`apps/extractionline/` 下没有 `index.html`，填了就是 404，所以留空。

**这两个页面现在还是 404。** `apps/` 是独立仓库 `zhipengge/apps`，Pages 已经开着
（`apps/skystrike/privacy.html` 现在返回 200），但 `apps/extractionline/` 还没进版本库。
提审前必须先提交并推送这一整个目录，否则 App Store Connect 填的隐私政策链接是空的。

---

## 6. 类别、评级、隐私问卷

### 类别（需要你定，两个都列出来）

**2026-10-14 定：原方案 A。**

| 字段 | 值 |
|---|---|
| 主要类别 | 游戏 / Games，子类 **动作 / Action** |

**次要类别为什么留空**（2026-10-14，实测）：
原方案 A 的次要类别写的是「游戏 / Games，子类 冒险 / Adventure」，
但**苹果不允许把同一个类别选两次**——真写时被明确拒绝：

```
HTTP 409  You may not select the same category twice for your app.
```

主类别已经是「游戏」了，次要类别就不能再是「游戏」。次要类别在 ASC 是**可选**的，
所以留空不影响提交。（要填的话只能挑一个**非游戏**的顶级类别，比如娱乐 / Entertainment。）

（选 A 的理由：实时移动、自动开火、走位与撤离窗口的取舍是核心；同类作品多归在动作。
原方案 B「冒险 / 策略」见 git 历史。改成这两行是因为工具只认表格行——
原来那张「选项 A/B」表它是当**候选题**读的，会一直报「必须人选定一个」。）

`TARGETED_DEVICE_FAMILY = "1,2"`，主要类别必须选游戏，子类只能选一个。

### 年龄分级（需要你定）

问卷不让你直接选档位，是按题作答后由 Connect 判定。当前档位是 4+ / 9+ / 13+ / 16+ / 18+ 五档。
这个游戏的实际情况：实时射击、敌人会死、玩家会死，但画面是俯视角的几何图形，
没有血、没有尸体、没有写实暴力，也没有恐怖、赌博、酒精烟草毒品、色情、脏话、用户生成内容、聊天、广告、网页浏览。

会决定档位的两题：

| 题目 | 你怎么答 | 后果 |
|---|---|---|
| 卡通或幻想暴力 | 无 | 与事实不符。射击是核心循环，不建议 |
| 卡通或幻想暴力 | 轻微/偶尔 | 大概率落在 9+。这是与事实最贴的一档 |
| 卡通或幻想暴力 | 频繁/强烈 | 会推到 13+。几何图形是否够得上「强烈」由你判断 |
| 现实暴力 / 武器 | 参考 | 游戏里有枪械。如果问卷问到「是否出现真实武器」，实际是抽象的几何形体，不是任何真枪的还原 |

**另一个时间点要注意：** 苹果要求所有开发者在这轮问卷更新里重新作答，**2026 年 1 月 31 日之后没作答的 App 无法提交更新**。这一条跟本作是否上架无关，只要还想发版本就得先过。

### 其余表

| 字段 | 建议 |
|---|---|
| 内购 | **需要你先定，见下面第 7 节** |
| App 隐私 | **不收集数据**。App 不发起任何网络请求，须与 `privacy.html` 一致 |
| 出口合规 | **NO**。`INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO` 已经写在工程里，App 完全没有加密，也没有网络代码 |

审核备注建议写清：本 App 完全离线，不发起任何网络请求，不收集任何数据，无账号、无广告，
也不申请任何系统权限。全部画面由代码绘制，15 个音效全部由代码实时合成，不含任何第三方素材或 SDK。
iPhone 仅竖屏，iPad 支持竖屏与上下颠倒。

首次提交时审核备注还要写：iPhone 上仅竖屏，不支持横屏。

---

## 7. ⚠️ 内购与定价：提审前必须先定，素材里刻意没写

**当前代码里没有任何 StoreKit。** 全工程 grep `StoreKit` / `Product.products` / `SKPayment` 零命中，
也没有任何「解锁」或「试玩限制」的判断。也就是说**现在跑起来的版本是全开的**。

但 `AGENTS.md` 的待办里写着：

> - [ ] App Store Connect 建 Record，配内购商品（¥25 非消耗型），否则审核看到的是全开状态

README 也写「买断制」。所以定价模型还没落地，**这一份素材因此刻意做了两件事**：

1. **描述里一个字的购买、价格、内购、免费都没提。** 既没说「没有内购」（那会在加上内购之后立刻变成假话），
   也没说「一次买断」（现在代码里还没有这个东西）。
2. **隐私政策里只写了与 Apple 之间的交易事实**（交易由 Apple 处理、我们拿不到你的 Apple ID），
   这条无论最后是付费下载还是内购都成立。

**提审前必须补的**：确定是付费 App 还是免费 + ¥25 非消耗型内购，然后：

- 若选内购：描述里加一句说明解锁的是什么，`privacy.html` 的「购买与账号」一节维持现状即可（StoreKit 不向开发者回传数据）
- 若选付费下载：描述里可以明写「一次买断」
- 同时注意 `Views/SettingsView.swift:183` 里 App 内文案是「没有内购以外的任何收费」——
  这句话读起来像是在说有内购存在。**这句话与当前代码不符**，无论最后选哪种定价都建议改掉，但本轮没有动源码。

---

## 8. 截图

`TARGETED_DEVICE_FAMILY = "1,2"`，iPhone 与 iPad 两套都要，各 3-10 张。
**目前 `apps/extractionline/screenshots/` 还不存在**，`AGENTS.md` 待办里也还挂着「商店截图导出」。

按 Apple《截屏规范》（Screenshot specifications，2026-10-12 核对原文），**必填的只有两档**：

- iPhone：**带灵动岛的 iPhone（中等显示屏）**，竖屏 1206 x 2622 或 1179 x 2556
- iPad 13 寸，竖屏 2064 x 2752

6.9 寸（带灵动岛的 iPhone，大显示屏，1320 x 2868）不是必填。

竖屏截图，不要裁成横版。空状态、纯海报式截图会被拒。

建议的六张（标题与副标题都只讲界面上真实存在的东西，**刻意不写任何难度评价**——
`AGENTS.md` 待办里明确写着难度曲线还没用 `LogicTests/balance.sh` 核过，
而 `extractAttractRadius` 与 `hearRadiusPerNoise` 是两次未经试玩的调整，所以「平衡」「难度刚刚好」这类词一个字都不能卖）：

| 文件 | 标题 | 副标题 | 对应界面 |
|---|---|---|---|
| `01-menu.png` | 进去，拿到，活着出来 | 一局 6 分钟，没出来就全留在里面 | 主菜单与生涯记录 |
| `02-extract.png` | 撤离是站住 6 秒 | 而且充能中的撤离点会把附近的敌人全叫过来 | 图内，撤离点充能中 |
| `03-windows.png` | 什么时候走，有一个说法 | 撤离窗口从外圈往中心收，由内向外关门 | 图内，小地图与窗口状态 |
| `04-stash.png` | 仓库里的东西不会丢 | 装备是出发那一刻离开仓库的，不是死的那一刻 | 仓库页 |
| `05-loadout.png` | 这一局带什么 | 带得多走得慢，带得少赚得少 | 配装页 |
| `06-settlement.png` | 死了会怎样 | 身上带的一切留在里面，这一局的账结给你看 | 结算面板 |

---

## 9. 这份素材里，哪些卖点是被故意排除的

诚实起见记一笔。`AGENTS.md` 的「差异化」一节列了四条，**四条都用了**，
因为每一条都能在代码里指出一处结构性实现，而不是数值调优：

| 差异化条目 | 代码依据 | 用在哪 |
|---|---|---|
| 撤离是站住 6 秒，且会叫 | `GameConfig.extractChargeTime = 6.0`、`extractAttractRadius = 280` | 推广文本、描述、FAQ、截图 02 |
| 拾荒者是唯一会赢的敌人 | `EnemyKind.scavenger`、`EnemyAI.scavengerDecision`、`wantsToExtract` | 描述、FAQ |
| 风险梯度场 + 窗口由外向内收 | `vaultDistrictRadius` / `midDistrictRadius`、`windowOpenTimes = [60,150,240]`、`windowDuration = 80` | 描述、FAQ、截图 03 |
| 噪音是一条独立的通关路线 | `hunterSquadNoiseThreshold = 62`、`suppressed` 词条、`w_whisper` 低语冲锋枪 | 描述、FAQ |

**故意没用的**：

- **「难度平衡得好」「节奏完美」这类评价一个字都没有。** `AGENTS.md` 待办里写明难度曲线尚未用
  `LogicTests/balance.sh` 核过，且 `extractAttractRadius`（220→280）与 `hearRadiusPerNoise`（1.3→2.6）
  是**两次未经试玩的调整**。没有测量支持的话不写。
- **「11 种敌人各自不同」没有当成卖点。** 恰恰相反：代码里 11 种共用同一台状态机，
  这是**一致性**而不是多样性，所以描述里写的是「你学会的躲视野锥对 11 种都成立」——
  这是代码事实，而且比「种类丰富」更具体。
- **没有引用任何竞品名或品类名（如某款搜打撤）**，关键词里也没有。全部文案为本作原创。
- **没有写「纯本地」这四个字的英文 Localized 版本当成卖点堆叠**，隐私声明只出现一次，压缩在描述末尾。
