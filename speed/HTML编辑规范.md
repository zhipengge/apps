# 速闻 HTML 编辑规范

本文给人工编辑和后续自动生成共用。目标是每天产出一份可被「速闻」iOS App 直接打开的 `index.html`：手机可读、图文结合，并覆盖约定栏目。

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
    ├── briefing.mp3
    └── clip.mp4
```

相对路径以 `index.html` 为基准，例如 `assets/cover.jpg`。远程资源必须是 `https://`。

---

## 2. 页面骨架（生成时按此输出）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>速闻 · 2026年8月22日</title>
  <style>/* 只写本页样式，见第 5 节 */</style>
</head>
<body>
  <article class="digest">
    <header class="hero">
      <p class="kicker">速闻 · 日报</p>
      <h1>2026年8月22日</h1>
      <p class="lead">一句话总述当天最值得看的几件事。</p>
      <ul class="chips">
        <li>科技</li><li>政治</li><li>军事</li><li>财经</li><li>娱乐</li>
      </ul>
    </header>

    <section class="media-card" aria-label="语音速览">
      <h2>语音速览</h2>
      <audio controls preload="none" src="https://example.com/briefing.mp3">
        当前环境不支持音频播放
      </audio>
    </section>

    <!-- 下面 5 个栏目必须都出现，顺序固定 -->
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

## 3. 栏目要求

每一期 **必须覆盖** 以下栏目，缺一不可。可在某栏目内再拆 1–2 条短讯，但栏目本身不能省略。

| `id` | `data-category` | 覆盖范围 | 写法 |
|---|---|---|---|
| `tech` | 科技 | 芯片、AI、互联网、航天、科研 | 讲清「发生了什么 / 为什么重要」 |
| `politics` | 政治 | 国内政策、外交、国际组织、选举与立法 | 客观简述，不站队、不煽动 |
| `military` | 军事 | 演习、装备、防务合作、安全局势 | 不渲染暴力，不写作战细节教程式内容 |
| `finance` | 财经 | 市场、宏观、产业、公司财报、汇率利率 | 数字给单位和截止日期，避免荐股 |
| `entertainment` | 娱乐 | 影视综、音乐、体育文娱、文化活动 | 可用预告片/现场视频，避免八卦人身攻击 |

每栏目建议 180–400 字，整期阅读时长控制在 4–7 分钟。

---

## 4. 富文本与媒体

内容必须图文结合。一期至少同时出现：**正文、图片、音频、视频、代码**。

### 4.1 允许的标签

`article` `header` `section` `footer` `h1` `h2` `h3` `p` `ul` `ol` `li` `blockquote` `figure` `figcaption` `img` `audio` `video` `source` `pre` `code` `strong` `em` `a` `small` `span` `time`

不要使用：`script` `iframe` `object` `embed` `form` `input` `table`（复杂表格改成列表）。

### 4.2 图片

```html
<figure>
  <img
    src="https://images.unsplash.com/photo-xxxx?auto=format&fit=crop&w=1200&q=80"
    alt="用一句话说明画面，不要写“图片”"
    width="1200"
    height="750"
    loading="lazy"
    decoding="async">
  <figcaption>图说：补充来源或场景，不超过 40 字。</figcaption>
</figure>
```

- 每栏目至少 1 张图；首屏 hero 可不另配大图。
- 优先横图，宽边 1200px 左右，单张远程图建议 < 400KB。
- 必须写有意义的 `alt`。
- 不要热链未授权的新闻社原图；用自家 `assets/`、Unsplash、Wikimedia Commons 等可公开引用的来源。

### 4.3 音频

```html
<audio controls preload="none" src="assets/briefing.mp3">
  当前环境不支持音频播放
</audio>
```

- 格式：`mp3` / `m4a` / `aac`（iOS 不保证 `ogg`）。
- 只做「点击播放」，禁止 `autoplay`。
- 整期至少 1 段，建议放在目录后、正文前，时长 30–90 秒。

### 4.4 视频

```html
<video controls playsinline webkit-playsinline preload="none" poster="assets/poster.jpg">
  <source src="assets/clip.mp4" type="video/mp4">
  当前环境不支持视频播放
</video>
```

- 格式：`mp4`（H.264 + AAC）。
- 必须带 `controls`、`playsinline`、`webkit-playsinline`，禁止自动播放。
- 整期至少 1 段，建议 15–45 秒；可放在娱乐或科技栏目。

### 4.5 代码

科技栏目至少 1 个代码块，用于解释接口、配置或关键参数，不要贴大段无关代码。

```html
<pre><code class="language-swift">let url = URL(string: "https://api.example.com/v1/news")
</code></pre>
```

`class` 用 `language-swift` / `language-python` / `language-json` / `language-bash`。不要上高亮脚本，靠 CSS 等宽字体即可。

### 4.6 链接

站外链接用绝对 `https://` 地址。App 会在系统浏览器打开，所以不要依赖页内跳转锚点以外的复杂交互。

---

## 5. 手机适配

App 用 WKWebView 全屏展示，按 **375–430pt 宽** 设计。

| 项目 | 要求 |
|---|---|
| 视口 | 必须有 `width=device-width, initial-scale=1` |
| 字号 | 正文 ≥ 16px，行高 1.6–1.7，优先系统字体 / PingFang SC |
| 间距 | 左右留白 16–20px，段落之间可扫读 |
| 媒体 | `img, video, audio { max-width: 100%; height: auto; }` |
| 代码 | `pre` 横向滚动，不要撑破屏幕 |
| 暗色 | 用 `prefers-color-scheme: dark` 或 `color-scheme: light dark` |
| 点击 | 播放控件、链接的可点区域足够大；不要依赖 hover |

推荐 CSS 变量：

```css
:root {
  --bg: #f6f5f2;
  --card: #ffffff;
  --text: #1c1c1e;
  --muted: #6e6e73;
  --line: rgba(28, 28, 30, 0.08);
  --accent: #1c1c1e;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0f0f10;
    --card: #1c1c1e;
    --text: #f2f2f7;
    --muted: #98989d;
    --line: rgba(255, 255, 255, 0.08);
    --accent: #f2f2f7;
  }
}
```

---

## 6. 文风与事实

- 用中文简体，标题短，先结论后背景。
- 写「速览」不是通讯社全文，不要大段转载。
- 不确定的信息标「尚待确认」，不要编造具体引语、数据或尚未发生的事件细节。
- 自动生成时：宁可少写数字，也不要虚构财报、伤亡、选举结果。
- 政治、军事栏目保持克制；娱乐栏目不写未成年人隐私。

---

## 7. 自动生成检查清单

生成或提交前全部勾上：

- [ ] 路径为 `speed/contents/YYYYMMDD/index.html`，日期真实
- [ ] 完整 HTML5，含 charset、viewport、中文 `title`
- [ ] 五个栏目都在，且 `id` / `data-category` 与第 3 节一致
- [ ] 至少 1 张图、1 段音频、1 段视频、1 个代码块
- [ ] 图片有 `alt`，音视频无 `autoplay`，视频带 `playsinline`
- [ ] 无 `script` / `iframe` / 表单
- [ ] 手机宽度下文字不溢出，代码块可横向滚动
- [ ] 资源不是坏链；本地文件路径相对 `index.html` 正确

满足以上条件，App 打开当日即可渲染；左右滑动只在存在该目录的有效日期之间切换。
