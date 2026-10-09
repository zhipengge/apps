# 空中绞杀 (SkyStrike) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。

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

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
障碍挡你也挡敌人，好东西就藏在后面。竖屏单手，自动开火，全程离线，没有广告也没有体力。
```

**字符数：43 / 170**

### English

```
Barriers block everyone's bullets and the good stuff hides behind them. Portrait, one hand, auto-fire, fully offline. No ads, no energy.
```

**字符数：136 / 170**

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
- 好东西就藏在障碍后面
- 继续打敌人还是分火力砸开障碍，每一波都要做这个取舍

【三种模式】
- 战役：40 波，每 10 波一个 Boss，打穿算通关
- 无尽：难度一路上涨，看你撑到第几波
- Boss Rush：跳过杂兵，四个 Boss 连打

【四种机体】
- 隼：射速快，弹道直，最稳的起步机体，默认可用
- 扇：三向扇形，清杂兵最舒服，4 颗星解锁
- 芒：穿透一条线，单发最疼，12 颗星解锁
- 寻：自动追踪最近的敌人，24 颗星解锁
- 星数只用来解锁机体，不卖数值，没有抽卡

【评分与道具】
- 每局按走得远近和挨打多少评 1 到 3 星，不看命中率
- 一波敌人一个都没漏就是完美波次，回复 1 点生命
- 连击加成最高 3 倍分数
- 六种道具：火力 / 护盾 / 清屏 / 吸附 / 金币 / 修复
- 机体初始 5 点生命

【分享】
- 结算生成一张战绩卡：分数、星级、击杀、受伤次数、存活时间
- 通过系统分享面板发出，发到哪由你决定

【免费与完整版】
- 免费下载，战役可以玩到第 8 波
- 一次买断解锁完整版：战役全部 40 波、无尽模式、Boss Rush
- 没有广告，没有体力，没有订阅
- 换设备用「恢复购买」找回，不用重新付费

【隐私与素材】
- 不收集任何数据，App 不发起任何网络请求
- 全部进度只存在这台设备上，删除 App 即清空
- 音效由代码实时合成，画面全部由代码绘制，不含任何第三方素材或 SDK

【系统要求】
需要 iOS 17.0 或更高版本。iPhone 与 iPad 均可，仅支持竖屏。
```

**字符数：约 840 / 4000**

### English

```
SkyStrike is a portrait bullet-hell shooter. Drag with one thumb, the guns fire on their own, and all you manage is positioning and priorities. Fully offline: no account, no ads, no energy.

[Controls]
- Hold anywhere and drag; the ship follows your finger
- Auto-fire, so there is no aiming to do
- Portrait and one-handed; a run fits into a commute

[The core mechanic: barriers]
- Destructible barriers stop your bullets and the enemy's alike
- The best pickups are hidden behind them
- Keep shooting enemies or divert fire into a barrier? Every wave asks that question

[Three modes]
- Campaign: 40 waves, a boss every 10, and clearing it is a win
- Endless: difficulty keeps climbing until you fall
- Boss Rush: no chaff, four bosses back to back

[Four ships]
- Falcon: fast, straight shots and the steadiest start, available from the beginning
- Spreader: a three-way fan that clears packs, unlocked at 4 stars
- Laser: pierces in a line and hits hardest per shot, unlocked at 12 stars
- Homing: chases the nearest enemy, unlocked at 24 stars
- Stars only unlock ships. Nothing is sold for power and there is no gacha

[Rating and pickups]
- Each run earns 1 to 3 stars for how far you got and how little you were hit, never for accuracy
- Clear a wave with no enemy escaping and you restore 1 health
- Combo multiplier up to 3x score
- Six power-ups: firepower, shield, screen clear, magnet, coins, repair
- Ships start with 5 health

[Sharing]
- A run ends with a score card: score, stars, kills, hits taken, survival time
- Send it through the system share sheet to wherever you like

[Free and full version]
- Free to download, with campaign waves up to wave 8
- One purchase unlocks the full version: all 40 campaign waves, Endless, and Boss Rush
- No ads, no energy, no subscription
- Restore Purchases brings it back on a new device at no extra charge

[Privacy and assets]
- Collects nothing, and the app makes no network requests
- All progress stays on this device; deleting the app clears it
- Sound effects are synthesised in code and all artwork is drawn in code, with no third-party assets or SDKs

[Requirements]
iOS 17.0 or later. iPhone and iPad. Portrait only.
```

**字符数：约 2185 / 4000**

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
arcade,retro,offline,premium,wave,combo,shmup,danmaku,spaceship
```

**字符数：63 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/skystrike/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/skystrike/privacy.html` |
| 营销 URL | `https://zhipengge.github.io/apps/skystrike/` |

---

## 6. 类别、评级、隐私问卷

| 字段 | 建议 |
|---|---|
| 主要类别 | 游戏 / Games，子类 动作 / Action |
| 次要类别 | 游戏 / Games，子类 街机 / Arcade |
| 内购 | 一项非消耗型：完整版（¥18 价格档） |
| 年龄分级 | 抽象的空战与命中特效，无流血、无写实暴力、无恐怖内容。问卷里的「卡通或幻想暴力」按实际作答，以 Connect 判定结果为准 |
| App 隐私 | **不收集数据**。App 不发起任何网络请求，须与 `privacy.html` 一致 |
| 出口合规 | NO（本 App 完全没有加密，也没有网络代码） |

审核备注建议写清：本 App 完全离线，不发起任何网络请求，不收集任何数据，无账号体系。免费可玩战役前 8 波；完整版为一次性非消耗型内购，购买与恢复由系统 StoreKit 完成，无订阅。全部音效由代码实时合成，全部画面由代码绘制，不含任何第三方素材或 SDK。

内购商品 ID：`com.gezhipeng0201.SkyStrike.full`。
注意：商品若未在 Connect 配好，App 会临时放开全部内容（宁可不收钱，也不能让玩家打开是残废版）。上架前必须把商品配好并随版本提交审核，否则审核看到的会是全开状态。

首次提交时审核备注还要写：iPhone 与 iPad 均为竖屏，不支持横屏。

---

## 7. 截图

App 是 `TARGETED_DEVICE_FAMILY = "1,2"`，iPhone 与 iPad 两套都要，各 3-10 张。

| 平台 | 尺寸 | 像素 |
|---|---|---|
| iPhone 6.9 寸 | 必填 | 1320 x 2868 |
| iPad 13 寸 | 必填 | 2064 x 2752 |

原始素材已在源码仓库 `SkyStrike/Screenshots/`（菜单、开局、中局、Boss、结算），
**尚未按商店规格导出到 `apps/skystrike/screenshots/`**。导出时按第 7.5 节的流水线走，
成品放 `apps/skystrike/screenshots/iphone/` 与 `apps/skystrike/screenshots/ipad/`，
文件名 `<序号>-<场景>.png`。

建议的 5 张与顺序：

- 01-menu 主菜单：三种模式与机体一览
- 02-barrier 战斗中：弹幕、可破坏障碍、障碍后的道具，一眼看懂核心机制
- 03-boss Boss 战：满屏弹幕与 Boss 血条
- 04-result 结算：三星、完美波次、战绩卡
- 05-ships 机体：四种机体与解锁进度

竖屏截图，不要裁成横版。空状态、纯海报式截图会被拒。
