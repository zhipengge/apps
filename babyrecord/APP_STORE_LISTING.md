# 牧云宝宝记 (MuyunBaby) — App Store 发布素材

> 直接复制粘贴到 **App Store Connect → App 信息 / 版本信息** 对应字段。
> 中英双语版本独立提交（简体中文 + English (U.S.) 各填一份）。
> 每个字段已标注 App Store Connect 的**真实字符上限**，文案均在限内，且已避开会触发「不支持的字符」的标点。

---

## 0️⃣ 创建 App Record（必填，按此填写，勿改）

在 App Store Connect → **我的 App → + → 新建 App** 时，**必须**填：

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **牧云宝宝记** | 宝宝记、Baby Tracker、喂养记录（通称易被占） |
| 名称（English 本地化，创建后添加） | **MuyunBaby** | BabyRecord、Baby Log |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.BabyRecord` | 任何旧 ID |
| SKU | `babyrecord-20260818` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「宝宝记」，与商店中文名可以不同。

若创建时报 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。备选店名：

- 牧云喂养记
- 牧云育儿手记
- MuyunBabyRecord

---

## 若 Xcode 报 Error Downloading App Information

文案类似：`App record with bundle identifier 'com.gezhipeng0201.BabyRecord' was previously removed from App Store Connect`。

这不是 Archive 坏了，而是这个 Bundle ID 在 Connect 里对应的 App 被删过。Xcode 分发时按 Bundle ID 找 Record，找到的是「已移除」状态，就会失败。

**先恢复，不要立刻换 Bundle ID。**

1. 打开 [App Store Connect → Apps](https://appstoreconnect.apple.com/apps)
2. 右上角 **All Statuses**（全部状态）旁边的箭头 → 选 **Removed Apps**（已移除的 App）
3. 点开「牧云宝宝记」或当时删掉的那条
4. 左侧 **App 信息** → 滚到 Additional Information → **Restore App**
5. 选 Limited Access 或 Full Access → Restore
6. 回到 Xcode，对**同一份 Archive**再点 Distribute（不必重打，除非恢复失败后改了 Bundle ID）

若列表里没有这条，或 Restore 失败（店名被别人占用、或曾经上传过构建导致 Bundle ID 作废）：

- 不能再用 `com.gezhipeng0201.BabyRecord` 和 SKU `babyrecord-20260818`
- 必须换全新 Bundle ID + 全新 SKU，再在网页新建 App Record，然后改工程里的 `AppIdentifiers` 与 pbxproj，并重跑逻辑测试第 1 组
- 备选 Bundle ID 示例：`com.gezhipeng0201.MuyunBaby`；备选 SKU：`muyunbaby-20260819`

---

## 1️⃣ 推广文本 (Promotional Text)

> **上限 170 字符**，可在不提交新版本的情况下随时修改。

### 简体中文（版本 v1.0 首发）

```
半夜一键记下喂奶、排便、睡眠、辅食、身高体重和体温，事后也能改时间。亲喂可记左右时长，奶量可手填，也可按当天平均或日龄估算。多位宝宝互不串记，字段能自定义分级。图表可分类型或整合，横轴看日期、月龄或天数，一键长图分享（水印可关）。首页能看到上次喂奶和排便。无账号无广告，数据只在本机，换机导出备份即可。
```

**字符数：151 / 170**

### English (v1.0 launch)

```
Feeding, diapers, sleep, solids, growth. Edit time later. Milk estimates, multi-baby nested fields. Combined charts, long-image share. On-device; export to switch phones.
```

**字符数：170 / 170**

---

## 2️⃣ 描述 (Description)

> **上限 4000 字符**。修改需提交新版本审核。

### 简体中文

```
牧云宝宝记是给父母和看护人用的本地育儿手账。喂奶、排便、睡眠、辅食、身高、体重、体温都能记下来，还能按自己的观察习惯增加类型和字段。界面只有三个入口：记录、图表、设置。没有账号，没有云同步，没有广告。断网也能用全部功能。

【半夜也能记，事后也能改】
- 首页大按钮一键打开喂奶、排便、睡眠、辅食、体重、身高、体温
- 发生时间默认为现在，补记时改成真实时间再保存
- 允许改到过去；超过当前 24 小时的未来时间会拦住
- 当天时间线按时间排列，左右切换日期，并显示月龄
- 顶部能看到上次喂奶和上次排便
- 记下后仍可修改或删除

【喂奶：亲喂、瓶喂、配方、混合】
- 亲喂可分别记下左侧、右侧时长
- 亲喂奶量可手填；留空时先按当天其他已填奶量的平均值
- 当天没有参考时，按日龄估算（最多 120 ml），编辑页会说明这次奶量从哪来
- 瓶喂母乳、配方奶、混合喂养按毫升记录，图表里会合到「奶量」

【排便：分级字段，而不是一张死表单】
- 先选大便、小便或两者
- 大便可记便量、性状、颜色、便血
- 有便血时再出现程度（轻微或严重）
- 便量默认是枚举，也可以在类型设置里改成按克填写
- 这套「选项下面再出字段」的结构，自定义类型同样能用

【图表：能看趋势，也能整页分享】
- 分类型查看体重、奶量、睡眠时长等折线，以及排便等选项的分布
- 同单位曲线可叠在一张图上，例如亲喂左右侧时长
- 整合视图把各类型曲线放进同一份长图，方便一次看完
- 横轴可选日期、出生月龄（如 10M4）或出生天数
- 次数、合计、平均、平均间隔、较上次变化；近 7 天、30 天、90 天或全部
- 一键生成长图分享，默认带「宝宝记」水印，也可关掉后再分享
- 分享走系统面板，不申请相册权限

【多位宝宝，互不串记】
- 首次安装带示例宝宝「安心」和示例喂奶记录，方便先看图表；删掉后不会再出现
- 添加宝宝需填写名字和出生日期，月龄和图表横轴都靠它
- 首页切换当前宝宝；记录和图表只显示这一位
- 设置里左滑即可删除宝宝及其全部记录，删除前会确认

【自己定义记录方式】
除了内置类型，可以新建类型，字段支持小数、整数、时长、文字、是否、枚举、分组。枚举的每个选项还能再挂子字段，用来记用药、吐奶、疫苗或任何你在意的观察。类型可以排序、开关是否出现在首页；内置类型改乱了可以补回或重置，自定义类型会保留。

【数据只在这台手机】
- 全部保存在本机，不发起网络请求
- 不申请通讯录、位置、麦克风、摄像头、相册
- 换机：旧设备导出备份，新设备用「整份替换」导入
- 两台设备都记过，可用按编号合并
- 卸载 App 后本机记录一并消失，换机前请先导出

牧云宝宝记不是医疗设备，不提供诊断或用药建议。亲喂估算奶量仅供参考，不能代替称重或医嘱。
```

### English

```
MuyunBaby is an on-device baby care log for parents and caregivers. Record feeding, diapers, sleep, solids, height, weight, and temperature, or add your own types and nested fields. Three tabs: Log, Charts, Settings. No account, no cloud, no ads. Everything works offline.

[Log quickly, fix the time]
- Large home buttons for feeding, diapers, sleep, solids, weight, height, and temperature
- Time defaults to now; change it when you log after the fact
- Past times are allowed; more than 24 hours in the future is blocked
- A day timeline with date paging and age
- Last feeding and last diaper at the top
- Edit or delete after saving

[Feeding: breast, bottle, formula, mixed]
- Breastfeeding can log left and right duration
- Milk volume is optional; if empty, it uses the same-day average of other feedings
- With no same-day reference, it estimates by age (up to 120 ml) and tells you so on the form
- Bottle, formula, and mixed volumes roll up into one milk chart

[Diapers: nested fields, not a rigid form]
- Choose stool, urine, or both
- Stool can include amount, texture, color, and blood
- Blood in stool reveals severity (mild or severe)
- Amount starts as an enum and can be changed to grams
- The same option-reveals-child-fields model is available for any custom type

[Charts you can read and share]
- Trends for weight, milk, sleep, and distributions for enums such as stool type
- Same-unit curves can overlay, such as left and right nursing time
- Combined view stacks every type into one long report
- Axis: calendar date, age in months (for example 10M4), or days since birth
- Counts, totals, averages, interval, change vs last; last 7 / 30 / 90 days, or all
- Share a long image; an app-name watermark is on by default and can be turned off
- Sharing uses the system share sheet; no Photos permission

[Multiple babies, never mixed]
- First launch includes a sample baby with feeding records so you can open Charts immediately; delete it and it will not return
- Name and birthday are required; age and chart axes depend on the birthday
- Switching babies never mixes records
- Swipe left in Settings to delete a baby and all of that baby's records

[Make the log your own]
Add types with decimal, integer, duration, text, yes/no, enum, or group fields. An enum option can reveal child fields, so you can track medicine, spit-up, vaccines, or any observation you care about. Reorder types, hide them from the home screen, restore missing built-ins, or reset built-ins without losing custom types.

[Stays on this phone]
- All data is on-device; the app makes no network requests
- No Contacts, Location, Microphone, Camera, or Photos permission
- Switch phones by exporting a backup, then importing with replace-all
- Merge by id if two devices both have logs
- Uninstalling removes local data; export first

MuyunBaby is not a medical device and does not diagnose or advise treatment. Estimated breastfeeding volume is for reference only.
```

---

## 3️⃣ 副标题 (Subtitle)

> **上限 30 字符**

### 简体中文

```
喂养排便睡眠体重，图表整合分享只在本机
```

**字符数：19 / 30**

### English

```
On-device baby log and charts
```

**字符数：29 / 30**

---

## 4️⃣ 关键词 (Keywords)

> **上限 100 字符**（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
喂养,母乳,亲喂,奶粉,排便,体重,身高,体温,辅食,睡眠,育儿,成长,月龄,图表,备份,分享
```

### English

```
feeding,diaper,weight,sleep,growth,breastfeeding,formula,solids,chart,share,backup,local
```

---

## 5️⃣ URL

| 字段 | URL |
|---|---|
| 技术支持 | https://zhipengge.github.io/apps/babyrecord/support.html |
| 隐私政策 | https://zhipengge.github.io/apps/babyrecord/privacy.html |
| 营销（可选） | https://zhipengge.github.io/apps/babyrecord/ |

---

## 6️⃣ 类别与内容评级

| 项 | 值 |
|---|---|
| 主要类别 | 健康与健身 |
| 次要类别 | 生活 |
| 内容分级 | 4+，无限制内容 |
| 年龄 | 不针对 12 岁以下儿童做广告或收集；本 App 无账号无追踪。记录对象是用户自己的孩子，使用者是家长 |

App 隐私问卷：**不收集数据**。与隐私政策一致。分享长图不构成「收集」，也不勾选「照片或视频」。

---

## 7️⃣ 截图

iPhone 6.7 寸等所需尺寸按 Connect 提示。3-10 张真实界面，不要海报。建议顺序：

1. 记录首页（快捷按钮 + 当天时间线，可带示例宝宝安心）
2. 喂奶编辑（亲喂奶量可手填，下方有估算提示）
3. 排便分级字段（便血再分程度）
4. 图表整合视图（多条曲线在同一份长图里）
5. 分享长图页（带宝宝记水印开关）
6. 设置里删除宝宝或导入导出

macOS 仓库里其它产品用 1280x800；本产品是 iOS，按 iPhone 截图规格提交。

---

## 8️⃣ 审核备注（提交时填写）

```
This iOS app is a fully offline baby care log: feeding, diapers, sleep, solids, weight, height, temperature, and custom nested fields. No account, no network, no Photos permission. All data stays in the app sandbox.

First launch includes a sample baby named An Xin with sample feeding records so Charts has data immediately. Delete it in Settings; it will not return.

Walkthrough:
1. Log tab: tap Feeding. Optionally change the occurrence time. For breastfeeding, leave milk volume empty to see the estimate hint, then save.
2. Charts tab: Combined stacks every type. Share (top right) renders a long screenshot. The app-name watermark is on by default and can be turned off.
3. Settings: swipe left on a baby to delete. Export/import is under Data. Nested enum fields are under record types (Diaper: stool, then blood, then severity).

Sharing uses the system share sheet only. The app does not read the photo library.
```
