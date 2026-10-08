# 效率打卡 (RecordBot) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **效率打卡** | 打卡、习惯、记账（通称易被占） |
| 名称（English 本地化） | **RecordBot** | Habit Tracker、Check-in |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.RecordBot` | 任何旧 ID |
| SKU | `recordbot-20261008` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「效率打卡」。

备选店名（创建时报名被占再用）：

- 效率打卡本
- 每日打卡
- RecordBot Habits

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
打卡、指标、多档案，数据只留在这台设备上。没有账号，不上传，不追踪。换手机用导出导入即可。
```

**字符数：45 / 170**

### English

```
Habits, metrics, multiple profiles, all stored on this device. No account, no upload, no tracking. Move devices with export and import.
```

**字符数：135 / 170**

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
效率打卡是一个本地优先的打卡与指标记录工具。数据只存在这台设备上，没有账号，不上传。

【打卡】
- 建立任意打卡任务，设置标题、描述与时间范围
- 支持按天、按周、自定义间隔重复
- 可开启本地提醒，由系统在本机调度
- 错过也能补打卡

【指标记录】
- 记录体重、身高等健康指标
- 趋势图按时间展示变化
- 可标记备注与来源

【多档案】
- 支持多个使用者档案
- 每个档案的打卡与指标相互独立
- 适合家庭共用一台设备

【备份与迁移】
- 支持导出为文件，换手机时导入恢复
- 数据不会自动上云

【隐私】
- 没有账号，没有服务器
- 不接入广告、分析或追踪服务
- 通知与照片权限只在你授权后使用，且都能单独关闭
```

**字符数：约 290 / 4000**

### English

```
RecordBot is a local-first habit and metric tracker. Your data stays on this device. No account, no upload.

[Check-ins]
- Create tasks with a title, description, and date range
- Repeat daily, weekly, or at a custom interval
- Optional local reminders scheduled by the system
- Backfill days you missed

[Metrics]
- Record weight, height, and other measures
- Trend charts over time
- Attach notes

[Profiles]
- Multiple user profiles
- Each keeps its own check-ins and metrics
- Good for a shared family device

[Backup and migration]
- Export to a file and import on a new phone
- Nothing syncs to the cloud automatically

[Privacy]
- No account, no server
- No ads, analytics, or tracking
- Notification and photo permissions are used only after you allow them, and can be turned off individually
```

**字符数：约 775 / 4000**

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
本地优先的打卡记录
```

**字符数：9 / 30**

### English

```
Offline habit and metric log
```

**字符数：28 / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
打卡,习惯,记录,指标,体重,身高,趋势,提醒,备份,多用户
```

**字符数：30 / 100**

### English

```
habit,tracker,checkin,streak,metric,weight,reminder,offline,backup,log
```

**字符数：70 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/record/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/record/privacy.html` |
| 营销 URL | `https://zhipengge.github.io/apps/record/` |

---

## 6. 类别、评级、隐私问卷

| 字段 | 建议 |
|---|---|
| 主要类别 | 效率 / Productivity |
| 次要类别 | 健康健美 / Health & Fitness |
| 年龄分级 | 4+ |
| App 隐私 | **不收集数据**。须与 `PRIVACY.md` 一致 |
| 出口合规 | NO（见 `EXPORT_COMPLIANCE.md`） |

审核备注建议写清：本 App 为纯本地工具，不运营服务器，全部数据保存在设备本地；通知由系统在本机调度。

---

## 7. 截图

iPhone 6.9 寸与 iPad 13 寸各 3-10 张真实界面。至少包含：空状态、打卡列表、新建任务、指标趋势图、档案切换、导出页。
