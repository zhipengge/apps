# 速闻 HTML 编辑规范

本文给人工编辑和后续自动生成共用。目标是每天产出一份可被「速闻」iOS App 直接打开的 `index.html`：手机可读、图文结合，**五个新闻板块分开**，板块内用**标签页聚类多条**，并且**每条新闻注明来源**。

App 会按日期读取：

```
https://raw.githubusercontent.com/zhipengge/apps/main/speed/contents/YYYYMMDD/index.html
```

对应仓库目录：

```
apps/speed/contents/YYYYMMDD/index.html
```

---

## 1. 文件与发布

| 规则 | 要求 |
|---|---|
| 目录名 | 必须是 `YYYYMMDD`，例如 `20260822`，且为真实公历日期（时区按 `Asia/Shanghai`） |
| 入口文件 | 每个日期目录有且仅有一个入口：`index.html` |
| 编码 | UTF-8，无 BOM |
| 文档类型 | 完整 HTML5 文档，必须包含 `<!DOCTYPE html>`、`<html lang="zh-CN">`、`<head>`、`<body>` |
| 体积 | `index.html` 建议 ≤ 150KB；单日全部本地资源建议 ≤ 8MB |
| 脚本 | **禁止**外链脚本、内联脚本、`iframe` 广告、自动播放音视频 |
| 推送 | 写入后提交到 `zhipengge/apps` 的 `main` 分支，App 才会拉到 |

可选本地资源放在同目录：

```
contents/20260822/
├── index.html
└── assets/
    ├── cover.jpg
    ├── briefing.m4a
    ├── clip.mp4
    └── poster.jpg
```

相对路径以 `index.html` 为基准，例如 `assets/briefing.m4a`。远程资源必须是 `https://`。

---

## 2. 时间窗口（必守）

每一期对应「发布日」当天的目录，但正文覆盖的是**滚动 24 小时**，不是自然日 0 点到 24 点。

| 项目 | 要求 |
|---|---|
| 窗口 | `Asia/Shanghai` 下，**发布日前一日 12:00 至发布日 12:00** |
| 示例 | `contents/20260822/` 覆盖 **2026-08-21 12:00 — 2026-08-22 12:00** |
| 页眉 | hero 里必须写清窗口，例如「覆盖北京时间 8月21日 12:00 — 8月22日 12:00」 |
| 跨窗口事件 | 事件发生在窗口外、但窗口内仍是主跟进稿的，可以收录；必须同时写**事件时间**和**见报时间** |
| 尚未发生 | 预告、将访、将上会、将开训可以写，但不得写成已经发生 |
| 周末 / 休市 | 财经数字写到窗口内最后一个已收盘交易日，并注明日期 |

不要把窗口外的旧闻、传闻和「今天可能会」写成当日新闻。

---

## 3. 页面骨架（生成时按此输出）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>速闻 · 2026年8月22日</title>
  <style>/* 只写本页样式，见第 7 节 */</style>
</head>
<body>
  <article class="digest">
    <header class="hero">
      <p class="kicker">速闻 · 日报</p>
      <h1>2026年8月22日</h1>
      <p class="window">覆盖北京时间 8月21日 12:00 — 8月22日 12:00</p>
      <p class="lead">一句话总述本窗口最值得看的几件事。</p>
      <ul class="chips">
        <li><a href="#tech">科技</a></li>
        <li><a href="#politics">政治</a></li>
        <li><a href="#military">军事</a></li>
        <li><a href="#finance">财经</a></li>
        <li><a href="#entertainment">娱乐</a></li>
      </ul>
    </header>

    <section class="media-card" aria-label="语音速览">
      <h2>语音速览</h2>
      <audio controls preload="none" src="assets/briefing.m4a">
        当前环境不支持音频播放
      </audio>
    </section>

    <!-- 下面 5 个板块必须都出现，顺序固定，板块之间不得混写 -->
    <section id="tech" class="story" data-category="科技">...</section>
    <section id="politics" class="story" data-category="政治">...</section>
    <section id="military" class="story" data-category="军事">...</section>
    <section id="finance" class="story" data-category="财经">...</section>
    <section id="entertainment" class="story" data-category="娱乐">...</section>

    <footer class="colophon">
      <p>速闻编辑部整理 · 仅供快速浏览</p>
    </footer>
  </article>
</body>
</html>
```

`title` 格式固定为 `速闻 · YYYY年M月D日`。

---

## 4. 栏目要求

每一期 **必须覆盖** 以下五个板块，缺一不可，顺序固定。板块是一级结构，不能把科技写进财经，也不能把五个板块揉成一篇长文。

| `id` | `data-category` | 覆盖范围 | 写法 |
|---|---|---|---|
| `tech` | 科技 | 芯片、AI、互联网、航天、科研、牌照与终端 | 讲清「发生了什么 / 为什么重要」 |
| `politics` | 政治 | 国内政策、外交、国际组织、选举与立法 | 客观简述，不站队、不煽动 |
| `military` | 军事 | 演习、装备、防务合作、安全局势 | 不渲染暴力，不写作战细节教程式内容 |
| `finance` | 财经 | 市场、宏观、产业、公司财报、汇率利率 | 数字给单位和截止日期，避免荐股 |
| `entertainment` | 娱乐 | 影视综、音乐、体育文娱、文化活动 | 可用公开物料，避免八卦人身攻击 |

每板块建议 2–4 个标签页，合计 300–800 字。整期阅读时长控制在 6–10 分钟。语音速览 30–90 秒，只读结论，不念来源链接。

---

## 5. 标签页聚类（必做）

每个板块内部必须用**标签页**把多条新闻按主题聚类，不能只写一条通稿，也不能把互不相关的新闻平铺成一长串。

### 5.1 聚类原则

- 一个标签页 = 一个子主题，例如科技下的「AI芯片 / 航天 / 产业」。
- 每个标签页里放 **1–3 条**独立新闻，用 `.item` 分开。
- 标签名要短：2–6 个汉字，避免整句当按钮。
- 五个板块的标签名不要照搬同一套；按当天新闻自然聚类。
- 当天某子题只有一条，也要单独成页，不要硬塞进无关标签。

推荐标签（可改，不可空）：

| 板块 | 常用标签示例 |
|---|---|
| 科技 | AI芯片、航天、互联网、科研、产业 |
| 政治 | 国内政策、周边外交、多边场合、立法司法 |
| 军事 | 联训收官、远程投送、新安排、国际局势 |
| 财经 | 宏观、市场、商品、公司 |
| 娱乐 | 影视、新片、体育、音乐 |

### 5.2 纯 CSS 标签页（禁止脚本）

App 的 WKWebView **不执行**页内脚本。标签切换必须用 CSS，推荐「隐藏 radio + label」：

```html
<section id="tech" class="story" data-category="科技">
  <span class="tag">科技</span>
  <h2>板块主标题</h2>
  <p>本板块一句导读。</p>

  <div class="tabset">
    <input type="radio" name="tabs-tech" id="tabs-tech-1" checked>
    <input type="radio" name="tabs-tech" id="tabs-tech-2">
    <input type="radio" name="tabs-tech" id="tabs-tech-3">
    <nav class="tabs" aria-label="科技子栏目">
      <label for="tabs-tech-1">AI芯片</label>
      <label for="tabs-tech-2">航天</label>
      <label for="tabs-tech-3">产业</label>
    </nav>
    <section class="pane pane-1">
      <article class="item">...</article>
      <article class="item">...</article>
    </section>
    <section class="pane pane-2">...</section>
    <section class="pane pane-3">...</section>
  </div>
</section>
```

硬性约定：

- `name` 按板块隔离：`tabs-tech` / `tabs-pol` / `tabs-mil` / `tabs-fin` / `tabs-ent`。
- 每个板块默认选中第一个标签（`checked`）。
- `id` 全页唯一，禁止五个板块共用同一组 `id`。
- **不要**用 `:target` 锚点做标签页（会把页面弹跳到半中腰）。
- **不要**用 JavaScript 切换。
- `input` 仅允许 `type="radio"`（或折叠用的 `checkbox`），**禁止**包在 `<form>` 里，禁止 `action`、联网提交。

对应 CSS 用兄弟选择器，不依赖脚本：

```css
.tabset > input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}
.pane { display: none; }
#tabs-tech-1:checked ~ .pane-1,
#tabs-tech-2:checked ~ .pane-2,
#tabs-tech-3:checked ~ .pane-3 { display: block; }
#tabs-tech-1:checked ~ .tabs label[for="tabs-tech-1"] {
  background: var(--accent);
  color: var(--bg);
}
```

标签按钮可点区域至少约 36px 高，横向过多时允许标签栏滚动，不要把按钮折成难点的小字。

---

## 6. 新闻来源（必做）

每一条 `.item` 都必须可回溯。没有来源的句子不要写进正文。

### 6.1 条头格式

```html
<article class="item">
  <h3>结论先行的短标题</h3>
  <p class="byline">
    <span>来源：<a href="https://www.news.cn/....">新华社</a></span>
    <time datetime="2026-08-21T18:57:00+08:00">8月21日 18:57</time>
  </p>
  <p>压缩转述。先写发生了什么，再写为什么重要。</p>
</article>
```

| 字段 | 要求 |
|---|---|
| 来源名 | 写媒体或机构名，不写「据悉」「网络流传」 |
| 原文链接 | 绝对 `https://`（或官方 `http://` 政府站点），能点开核对 |
| 时间 | 用 `<time datetime>`；能精确到时刻就写时刻 |
| 多源核对 | 同一事实被两家报道，可并列两个来源，用顿号或第二个 `<a>` |
| 转载链 | 若只能找到转载页，写成「新华社 / 人民网」，链接指向能打开的那一版 |

### 6.2 可用与不可用的来源

优先：新华社、人民日报 / 人民网、央视 / 央视网、财政部 / 外交部 / 国防部等官方站点、交易所或公司公告、路透 / 彭博 / Space.com 等可核对的专业媒体。

谨慎：自媒体、聚合站、未具名「知情人士」。这类材料最多写成「有媒体引述……，双方尚未宣布」，**不能**把传闻写成事实。

禁止：

- 编造媒体名、日期、报价、伤亡和选举结果
- 大段原文照抄（速闻是压缩阅读，不是通讯社全文镜像）
- 热链新闻社未授权原图当配图
- 把评论区截图、来路不明的「内部文件」当依据

### 6.3 交叉引用

同一件事可以在两个板块各写一次，但角度必须分开。例如国新办财政发布会：

- 政治：记「谁在什么场合说了什么部署」
- 财经：记「对市场有约束力的数字和工具」

不要两处复制同一段。

---

## 7. 富文本与媒体

内容必须图文结合。一期至少同时出现：**正文、图片、音频、视频、代码**。

### 7.1 允许的标签

`article` `header` `section` `footer` `nav` `div` `h1` `h2` `h3` `p` `ul` `ol` `li` `blockquote` `figure` `figcaption` `img` `audio` `video` `source` `pre` `code` `strong` `em` `a` `small` `span` `time` `label`

`input` 仅用于第 5 节的标签页（`type="radio"` / `checkbox`）。

不要使用：`script` `iframe` `object` `embed` `form` `table`（复杂表格改成列表）、`textarea`、带 `action` 的提交控件。

### 7.2 图片

```html
<figure>
  <img
    src="https://images.unsplash.com/photo-xxxx?auto=format&amp;fit=crop&amp;w=1200&amp;q=80"
    alt="用一句话说明画面，不要写“图片”"
    width="1200"
    height="750"
    loading="lazy"
    decoding="async">
  <figcaption>图说：补充来源或场景，不超过 40 字。</figcaption>
</figure>
```

- 每板块至少 1 张图；首屏 hero 可不另配大图。
- 优先横图，宽边 1200px 左右，单张远程图建议 < 400KB。
- 必须写有意义的 `alt`。
- 不要热链未授权的新闻社原图；用自家 `assets/`、Unsplash、Wikimedia Commons 等可公开引用的来源。
- HTML 属性里的 `&` 写成 `&amp;`。

### 7.3 音频

```html
<audio controls preload="none" src="assets/briefing.m4a">
  当前环境不支持音频播放
</audio>
```

- 格式：`mp3` / `m4a` / `aac`（iOS 不保证 `ogg`）。
- 只做「点击播放」，禁止 `autoplay`。
- 整期至少 1 段，放在目录后、正文前，时长 30–90 秒。
- 口播按五个板块各一句，不念 URL，不荐股，不渲染冲突细节。
- 正式期次用本地 `assets/`，不要再放恐龙吼、占位音效。

### 7.4 视频

```html
<video controls playsinline webkit-playsinline preload="none" poster="assets/poster.jpg">
  <source src="assets/clip.mp4" type="video/mp4">
  当前环境不支持视频播放
</video>
```

- 格式：`mp4`（H.264 + AAC 或无声 H.264）。
- 必须带 `controls`、`playsinline`、`webkit-playsinline`，禁止自动播放。
- 整期至少 1 段，建议 9–45 秒；可放在娱乐或科技栏目。
- **不要**外链未授权的电影预告、赛事转播、新闻社成片。用 Wikimedia Commons、NASA 等可公开引用素材，并在 `<small class="hint">` 里写许可与作者。
- 片源是教学或资料片时，正文必须写明「不是赛事转播 / 不是官方预告」。

### 7.5 代码

科技栏目至少 1 个代码块，用于解释接口、配置或关键参数，不要贴大段无关代码。

```html
<pre><code class="language-json">{
  "interconnect": "CPO",
  "target": "memory-interface"
}</code></pre>
```

`class` 用 `language-swift` / `language-python` / `language-json` / `language-bash`。不要上高亮脚本，靠 CSS 等宽字体即可。

### 7.6 链接

站外链接用绝对地址。App 会在系统浏览器打开，所以不要依赖页内跳转锚点以外的复杂交互。板块 chips 可以链到 `#tech` 等栏目 `id`。

---

## 8. 手机适配

App 用 WKWebView 全屏展示，按 **375–430pt 宽** 设计。

| 项目 | 要求 |
|---|---|
| 视口 | 必须有 `width=device-width, initial-scale=1` |
| 字号 | 正文 ≥ 16px，行高 1.6–1.7，优先系统字体 / PingFang SC |
| 间距 | 左右留白 16–20px，段落之间可扫读 |
| 媒体 | `img, video, audio { max-width: 100%; height: auto; }` |
| 代码 | `pre` 横向滚动，不要撑破屏幕 |
| 标签页 | 标签栏可横向滑动；选中态在浅色 / 深色下都要能看清 |
| 暗色 | 用 `prefers-color-scheme: dark` 或 `color-scheme: light dark` |
| 点击 | 播放控件、链接、标签的可点区域足够大；不要依赖 hover |

推荐 CSS 变量：

```css
:root {
  --bg: #f6f5f2;
  --card: #ffffff;
  --text: #1c1c1e;
  --muted: #6e6e73;
  --line: rgba(28, 28, 30, 0.08);
  --accent: #1c1c1e;
  --chip: #f3f1ec;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0f0f10;
    --card: #1c1c1e;
    --text: #f2f2f7;
    --muted: #98989d;
    --line: rgba(255, 255, 255, 0.08);
    --accent: #f2f2f7;
    --chip: #2c2c2e;
  }
}
```

---

## 9. 文风与事实

- 用中文简体，标题短，先结论后背景。
- 写「速览」不是通讯社全文，不要大段转载。
- 不确定的信息标「尚待确认」，不要编造具体引语、数据或尚未发生的事件细节。
- 自动生成时：宁可少写数字，也不要虚构财报、伤亡、选举结果。
- 政治、军事栏目保持克制；娱乐栏目不写未成年人隐私。
- 财经不荐股、不给目标价；公司数字写清报告期和单位。
- 同一窗口出现互相矛盾的稿件时，写双方各自主张，不自行裁断。

---

## 10. 自动生成检查清单

生成或提交前全部勾上：

- [ ] 路径为 `speed/contents/YYYYMMDD/index.html`，日期真实
- [ ] hero 写明 **T-1 12:00 至 T 12:00**（北京时间）窗口
- [ ] 完整 HTML5，含 charset、viewport、中文 `title`
- [ ] 五个板块都在，且 `id` / `data-category` 与第 4 节一致，顺序固定
- [ ] 每个板块都有标签页，标签页内是聚类后的多条 `.item`
- [ ] 每条新闻有来源名、可点开的原文链接、`<time>`
- [ ] 窗口外事件已标明事件时间，预告未写成已经发生
- [ ] 至少 1 张图、1 段音频、1 段视频、1 个代码块
- [ ] 图片有 `alt`，音视频无 `autoplay`，视频带 `playsinline`
- [ ] 无 `script` / `iframe` / `form`；`input` 只用于标签页
- [ ] 手机宽度下文字不溢出，代码块和标签栏可横向滚动
- [ ] 资源不是坏链；本地文件路径相对 `index.html` 正确
- [ ] 没有热链未授权新闻图、电影预告或赛事转播

满足以上条件，App 打开当日即可渲染；左右滑动只在存在该目录的有效日期之间切换。
