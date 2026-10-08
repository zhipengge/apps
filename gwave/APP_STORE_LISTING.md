# 牧云电台 (Gwave) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **牧云电台** | 收音机、网络电台、电台播放器（通称易被占） |
| 名称（English 本地化） | **Gwave** | Radio Player、Internet Radio |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.Gwave` | 任何旧 ID |
| SKU | `gwave-20261008` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「牧云电台」。

备选店名（创建时报名被占再用）：

- 牧云收音机
- 牧云流声
- Gwave Radio

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
搜台、收藏、后台播放，还能自己加源。内置雨声海浪等白噪声在本机实时合成。没有账号，不收集任何信息。
```

**字符数：49 / 170**

### English

```
Search, favorite, and play in the background. Add your own streams. Built-in rain and wave sounds are synthesised on-device. No account, no tracking.
```

**字符数：149 / 170**

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
牧云电台是一个极简的网络电台播放工具。搜到你喜欢的台，收藏起来，后台也能继续听。

【收听】
- 搜索全球公开的网络电台
- 收藏常听的台，支持分组整理
- 后台播放，锁屏界面和「正在播放」面板可直接控制
- 支持 AirPlay 与蓝牙输出

【自己加源】
- 手动添加电台名称与地址
- 从 JSON 或文本文件批量导入
- 用网址导入整份播放列表
- 支持 gwave 链接一键添加

【内置音效】
- 雨声、海浪、粉红噪声等助眠与专注音效
- 在本机实时合成，不占存储、不需要网络

【同步与外观】
- 可选 iCloud 同步，在你自己的账户里同步收藏与列表
- 深色、浅色、跟随系统

【隐私】
- 没有账号，不收集姓名、邮箱、位置
- 不收集你的播放记录
- 不接入广告、分析或追踪服务
- 音频直接从源站传到你的设备，我们不存储、不转发
```

**字符数：约 350 / 4000**

### English

```
Gwave is a minimal internet radio player. Find a station, favourite it, and keep listening in the background.

[Listen]
- Search public internet radio stations
- Favourite the ones you like, organised in groups
- Background playback with lock screen and Now Playing controls
- AirPlay and Bluetooth output

[Add your own]
- Type a station name and URL
- Import a JSON or text list from a file
- Import a whole playlist from a URL
- One-tap add via gwave links

[Built-in sounds]
- Rain, waves, pink noise and more for sleep or focus
- Synthesised on-device: no storage, no network

[Sync and appearance]
- Optional iCloud sync of your list and favourites, in your own account
- Dark, light, or follow the system

[Privacy]
- No account, no collection of name, email, or location
- No collection of your listening history
- No ads, analytics, or tracking
- Audio goes straight from the source to your device
```

**字符数：约 880 / 4000**

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
网络电台与白噪声
```

**字符数：8 / 30**

### English

```
Radio and ambient sound
```

**字符数：23 / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
电台,收音机,网络电台,白噪声,助眠,专注,收藏,后台播放,导入
```

**字符数：32 / 100**

### English

```
radio,station,stream,ambient,noise,sleep,focus,favorite,playlist,import
```

**字符数：71 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/gwave/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/gwave/privacy.html` |
| 营销 URL | `https://zhipengge.github.io/apps/gwave/` |

---

## 6. 类别、评级、隐私问卷

| 字段 | 建议 |
|---|---|
| 主要类别 | 音乐 / Music |
| 次要类别 | 娱乐 / Entertainment |
| 年龄分级 | 4+。用户可添加任意流地址，若勾选 Unrestricted Web Access 则为 17+ |
| App 隐私 | **不收集数据**。须与 `PRIVACY.md` 一致 |
| 出口合规 | NO（见 `EXPORT_COMPLIANCE.md`） |

审核备注建议写清：本 App 为播放工具，不内置任何受版权保护的电台内容；用户可自行添加公开的网络电台地址。iCloud 同步走用户自己的 iCloud 账户。

---

## 7. 截图

iPhone 6.9 寸与 iPad 13 寸各 3-10 张真实界面。至少包含：搜索页、收藏列表、播放中（含锁屏控制）、白噪声、导入页、设置页。
