# 速闻 (Speed) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **速闻** | 新闻、资讯、日报（通称易被占） |
| 名称（English 本地化） | **Speed** | News Reader、Daily Briefing |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.Speed` | 任何旧 ID |
| SKU | `speed-20261008` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「速闻」。

备选店名（创建时报名被占再用）：

- 速闻日报
- 今日速闻
- Speed Daily

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
每天一期，12 到 20 条值得看的新闻，分五个板块。每条都能独立收藏和分享，支持微信文稿。先看缓存再看更新，不记录你读了什么。
```

**字符数：64 / 170**

### English

```
One issue a day: 12 to 20 stories in five sections. Bookmark or share any story on its own. WeChat-ready digest. No reading history.
```

**字符数：132 / 170**

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
速闻每天精选 12 到 20 条值得看的新闻，分成科技、政治、军事、财经、娱乐五个板块。每条新闻都能独立阅读、收藏和分享，不必通读整期。

【每日一期】
- 按日期浏览当天内容，可回看往期
- 先展示本地缓存，再静默拉取更新
- 已缓存的期次可离线阅读

【独立条目】
- 每条新闻有自己的标题、简介、正文和出处
- 正文是完整段落，不是一句话标签
- 点出处可在应用内打开原文

【收藏与分享】
- 收藏单条新闻，跨期保留
- 生成适合微信的图文文稿，直接粘贴即可
- 也可分享单条链接

【阅读体验】
- 五个板块一目了然，按兴趣跳读
- 深色、浅色、跟随系统
- 支持导出导入备份，换手机不丢收藏

【隐私】
- 不记录也不上传你的阅读历史
- 没有账号，没有自建服务器
- 不接入广告、分析或追踪服务
- 网络请求只用于拉取公开的新闻内容
```

**字符数：约 347 / 4000**

### English

```
Speed picks 12 to 20 worthwhile stories every day across five sections: technology, politics, military, finance, and entertainment. Each story stands on its own, so you can bookmark and share it without reading the whole issue.

[One issue a day]
- Browse by date and look back at earlier issues
- Shows the local cache first, then refreshes quietly
- Cached issues read offline

[Stories on their own]
- Each has its own headline, summary, body, and source
- Full paragraphs, not one-line labels
- Tap the source to open the original in-app

[Save and share]
- Bookmark individual stories across issues
- Generate a WeChat-ready digest you can paste straight in
- Or share a single story link

[Reading]
- Five sections make it easy to jump to what interests you
- Dark, light, or follow the system
- Export and import a backup so switching phones keeps your bookmarks

[Privacy]
- No reading history recorded or uploaded
- No account, no backend of our own
- No ads, analytics, or tracking
- Network requests only fetch public news content
```

**字符数：约 1015 / 4000**

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
每天一期新闻精选
```

**字符数：8 / 30**

### English

```
A daily news digest
```

**字符数：19 / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
新闻,资讯,每日,精选,科技,财经,收藏,简报,阅读,离线
```

**字符数：29 / 100**

### English

```
news,daily,briefing,digest,read,bookmark,tech,finance,offline,summary
```

**字符数：69 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/speed/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/speed/privacy.html` |
| 营销 URL | `https://zhipengge.github.io/apps/speed/` |

---

## 6. 类别、评级、隐私问卷

| 字段 | 建议 |
|---|---|
| 主要类别 | 新闻 / News |
| 次要类别 | 杂志与报纸 / Magazines & Newspapers |
| 年龄分级 | 12+。新闻内容可能涉及政治、军事等话题，但无成人内容 |
| App 隐私 | **不收集数据**。须与 `PRIVACY.md` 一致 |
| 出口合规 | NO（见 `EXPORT_COMPLIANCE.md`） |

审核备注建议写清：本 App 是新闻聚合阅读器，内容由编辑流程产出并托管在公开仓库；应用不记录用户阅读行为，无账号体系。

---

## 7. 截图

iPhone 6.9 寸与 iPad 13 寸各 3-10 张真实界面。至少包含：今日首页（多板块）、新闻详情、收藏列表、分享文稿、设置页。
