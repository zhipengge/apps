#!/usr/bin/env python3
"""
为 apps/<app>/ 生成 privacy.html 与 support.html。

风格与既有的 weedit/privacy.html 保持一致（浅色深色自适应、单列 760px）。

用法：
    python3 tools/gen_pages.py            # 生成 APPS 里定义的全部
    python3 tools/gen_pages.py afu        # 只生成 afu
"""

import sys
from pathlib import Path
from html import escape

CSS = """  :root {
    color-scheme: light dark;
    --fg: #1c1c1e; --fg-dim: #6e6e73;
    --bg: #ffffff; --bg-soft: #f5f5f7;
    --accent: __ACCENT__;
    --border: rgba(0,0,0,.08);
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --fg: #f5f5f7; --fg-dim: #98989d;
      --bg: #1c1c1e; --bg-soft: #2c2c2e;
      --accent: __ACCENT_DARK__;
      --border: rgba(255,255,255,.1);
    }
  }
  * { box-sizing: border-box; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "PingFang SC", Helvetica, Arial, sans-serif;
    color: var(--fg); background: var(--bg); line-height: 1.6;
    max-width: 760px; margin: 0 auto; padding: 32px 24px 80px;
    -webkit-font-smoothing: antialiased;
  }
  h1 { font-size: 2rem; font-weight: 700; letter-spacing: -0.02em; margin-top: 0; margin-bottom: 4px; }
  h2 { font-size: 1.4rem; font-weight: 600; margin-top: 48px; padding-top: 18px; border-top: 1px solid var(--border); }
  h3 { font-size: 1.1rem; font-weight: 600; margin-top: 28px; }
  .meta { color: var(--fg-dim); font-size: 0.9rem; margin-bottom: 32px; }
  .lead { background: var(--bg-soft); padding: 18px 20px; border-radius: 12px;
          border-left: 4px solid var(--accent); margin: 20px 0; }
  table { width: 100%; border-collapse: collapse; font-size: 0.92rem; margin: 16px 0 24px; }
  th, td { text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--border); vertical-align: top; }
  th { font-weight: 600; color: var(--fg-dim); background: var(--bg-soft); }
  ul li { margin: 6px 0; }
  code { font-family: "SF Mono", Menlo, Consolas, monospace; font-size: 0.85em;
         background: var(--bg-soft); padding: 1px 6px; border-radius: 4px; }
  a { color: var(--accent); text-decoration: none; }
  a:hover { text-decoration: underline; }
  .lang-switch { display: flex; gap: 6px; margin: 0 0 24px; font-size: 0.85rem; }
  .lang-switch a { padding: 6px 12px; background: var(--bg-soft); border-radius: 999px; }
  footer { margin-top: 64px; padding-top: 24px; border-top: 1px solid var(--border);
           color: var(--fg-dim); font-size: 0.85rem; }
  .faq { margin: 18px 0; }
  .faq strong { display: block; margin-top: 20px; }"""

PAGE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<style>
__CSS__
</style>
</head>
<body>

<div class="lang-switch">
  <a href="#zh">中文</a>
  <a href="#en">English</a>
</div>

__BODY__

<footer>__FOOTER__</footer>
</body>
</html>
"""


def table(rows, head):
    out = ["<table>", "<tr>" + "".join(f"<th>{escape(h)}</th>" for h in head) + "</tr>"]
    for r in rows:
        out.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
    out.append("</table>")
    return "\n".join(out)


def ul(items):
    return "<ul>\n" + "\n".join(f"  <li>{i}</li>" for i in items) + "\n</ul>"


def render(page):
    css = (CSS.replace("__ACCENT__", page["accent"])
              .replace("__ACCENT_DARK__", page["accent_dark"]))
    return (PAGE.replace("__TITLE__", escape(page["title"]))
                .replace("__CSS__", css)
                .replace("__BODY__", page["body"])
                .replace("__FOOTER__", page["footer"]))


def write(app_dir: Path, name: str, page):
    app_dir.mkdir(parents=True, exist_ok=True)
    p = app_dir / name
    p.write_text(render(page), encoding="utf-8")
    print(f"  ✓ {p}  ({len(p.read_text(encoding='utf-8'))} 字节)")


# ============================================================ 各 App 内容

def afu(d: Path):
    write(d, "privacy.html", {
        "title": "阿福 · 隐私政策 / Privacy Policy",
        "accent": "#0A84FF", "accent_dark": "#64D2FF",
        "footer": "阿福 Afu · 端侧本地大模型助手",
        "body": """
<h1>阿福 · 隐私政策</h1>
<p class="meta">Afu — Privacy Policy · 最后更新 / Last updated: 2026-10-08</p>

<h2 id="zh">中文</h2>

<p class="lead"><strong>阿福的对话与推理全部在你的设备上完成，聊天内容不会上传到我们或任何第三方的服务器。</strong> 没有账号，没有自建后端，不内嵌广告、分析或追踪 SDK。</p>

<h3>我们处理什么、在哪处理</h3>
""" + table([
        ("你输入的文本、模型回复、会话标题与时间", "构建提示词并在本机生成回复", "设备本地数据库"),
        ("你从相册选择或拍摄的图片", "在本机做文字识别、画面理解或摘要", "设备本地；不上传"),
        ("你通过「文件」导入的 PDF / Word / Excel / CSV / TXT / Markdown", "在本机解析为模型可读的文本", "设备本地；不上传"),
        ("生成参数（温度、Top-P、最大长度、系统提示词）", "控制模型行为", "设备本地"),
        ("Hugging Face Access Token（仅你主动填写时）", "下载需要授权的模型", "设备钥匙串；只用于该次下载"),
    ], ["数据", "用途", "位置"]) + """

<p><strong>关于图片与文件：</strong>图片可能使用 Apple 提供的本机能力（如 Vision）处理；文件在本机被解析为文本摘录。两者都不会离开设备。</p>

<h3>网络通信</h3>
<p>应用只在两处联网：</p>
<ul>
  <li><strong>拉取模型清单</strong>：向公开的 GitHub 仓库请求可用模型列表（只读取清单，不发送任何个人信息）。</li>
  <li><strong>下载模型权重</strong>：在你选择某个模型后，从 Hugging Face 官方源或你指定的镜像源下载模型文件。下载过程中传输的只有模型文件本身，<strong>不包含你的对话、图片或文件</strong>。</li>
</ul>
<p>除此之外，阿福不发起任何网络请求。断网时已下载的模型仍可正常对话。</p>

<h3>我们不做的事</h3>
""" + ul([
        "不把对话内容、图片或文件发到任何服务器",
        "不要求注册或登录账号",
        "不接入广告网络或分析平台",
        "不读取通讯录、位置、麦克风",
        "不把你的数据用于模型训练",
    ]) + """

<h3>数据删除</h3>
<p>在应用内删除会话即可移除对应记录；删除整个 App 并移除其容器，即可清除全部本地数据（已下载的模型文件也会一并删除）。</p>

<h2 id="en">English</h2>

<p class="lead"><strong>Afu runs all inference on your device. Your conversations are never uploaded to us or any third party.</strong> No account, no backend, no ads, analytics, or tracking.</p>

<h3>What we process, and where</h3>
""" + table([
        ("Your messages, model replies, session titles and timestamps", "Build prompts and generate replies on-device", "Local database on your device"),
        ("Photos you pick or capture", "On-device text recognition and image understanding", "On device only"),
        ("Files you import (PDF, Word, Excel, CSV, TXT, Markdown)", "Parsed into text on-device", "On device only"),
        ("Generation settings (temperature, Top-P, max length, system prompt)", "Control model behaviour", "On device"),
        ("Hugging Face access token (only if you enter one)", "Download gated models", "Device keychain; used only for that download"),
    ], ["Data", "Purpose", "Where"]) + """

<h3>Network</h3>
<p>The app connects to the network in exactly two places: fetching the public model catalog from a GitHub repository (reads a list only, sends nothing about you), and downloading model weights from Hugging Face or a mirror you choose. Only the model files travel; <strong>your conversations, photos, and files are never included</strong>. Downloaded models keep working offline.</p>

<h3>What we do not do</h3>
""" + ul([
        "No upload of conversations, photos, or files",
        "No account or sign-in",
        "No ads or analytics SDKs",
        "No access to Contacts, Location, or Microphone",
        "We do not train models on your data",
    ]) + """

<h3>Deletion</h3>
<p>Delete a session in-app to remove it. Removing the app and its container clears all local data, including downloaded models.</p>
"""})

    write(d, "support.html", {
        "title": "阿福 · 支持 / Support",
        "accent": "#0A84FF", "accent_dark": "#64D2FF",
        "footer": "阿福 Afu · 端侧本地大模型助手",
        "body": """
<h1>阿福 · 支持</h1>
<p class="meta">Afu — Support · 最后更新 / Last updated: 2026-10-08</p>

<h2 id="zh">中文</h2>

<div class="faq">
<strong>第一次打开，模型列表是空的？</strong>
<p>阿福本身不含模型。打开「模型」页选择一个适合你设备的模型下载即可。首次上手建议选 0.5B 到 2B 参数的小模型，下载快、占用低。</p>

<strong>下载模型失败或很慢？</strong>
<p>默认走 Hugging Face 官方源，国内直连可能较慢。可在设置里切换到镜像源；也可以稍后重试，已下载的部分会保留并从断点续传。</p>

<strong>提示需要 Hugging Face Token？</strong>
<p>部分模型需要授权才能下载。在 Hugging Face 官网注册后生成一个 Access Token（只读权限即可），填进阿福的设置页。Token 只保存在本机钥匙串，仅用于该次下载。</p>

<strong>回复很慢 / 设备发烫？</strong>
<p>参数量越大的模型越慢。0.5B 到 2B 的模型在最近的 iPhone 上通常流畅；4B 及以上会更慢、更耗电，且占用内存明显更多。可在设置里调低最大回复长度。</p>

<strong>支持图片理解吗？</strong>
<p>只有标注为「多模态」的模型支持。这类模型会多下载一个视觉投影文件，体积更大。</p>

<strong>数据存在哪里？怎么删？</strong>
<p>全部在本机。删除会话即可移除聊天记录；删除 App 会一并清除模型和设置。详见<a href="privacy.html">隐私政策</a>。</p>

<strong>怎么反馈问题？</strong>
<p>到 <a href="https://github.com/zhipengge/apps/issues">GitHub Issues</a> 提交，附上设备型号、系统版本和复现步骤。</p>
</div>

<h2 id="en">English</h2>

<div class="faq">
<strong>The model list is empty on first launch</strong>
<p>Afu ships without models. Open the Models tab and download one that fits your device. Start with a 0.5B to 2B model for a quick download and low memory use.</p>

<strong>Download fails or is slow</strong>
<p>The default source is Hugging Face. Try a mirror in Settings, or retry later. Partial downloads resume from where they stopped.</p>

<strong>It asks for a Hugging Face token</strong>
<p>Some models are gated. Create a read-only access token on huggingface.co and paste it into Settings. It is stored in the device keychain and used only for that download.</p>

<strong>Replies are slow, or the device gets hot</strong>
<p>Larger models are slower. 0.5B to 2B models run smoothly on recent iPhones; 4B and above use noticeably more memory and power. Lower the max reply length in Settings.</p>

<strong>Does it understand images</strong>
<p>Only models tagged Multimodal. They download an extra vision projector file and take more space.</p>

<strong>Where is my data, and how do I delete it</strong>
<p>All on-device. Delete a session to remove it; deleting the app clears models and settings too. See the <a href="privacy.html">Privacy Policy</a>.</p>

<strong>Reporting a problem</strong>
<p>File an issue at <a href="https://github.com/zhipengge/apps/issues">GitHub Issues</a> with your device model, OS version, and steps to reproduce.</p>
</div>
"""})


def gwave(d: Path):
    write(d, "privacy.html", {
        "title": "牧云电台 · 隐私政策 / Privacy Policy",
        "accent": "#30B0C7", "accent_dark": "#40C8E0",
        "footer": "牧云电台 Gwave · 网络电台与白噪声播放器",
        "body": """
<h1>牧云电台 · 隐私政策</h1>
<p class="meta">Gwave — Privacy Policy · 最后更新 / Last updated: 2026-10-08</p>

<h2 id="zh">中文</h2>

<p class="lead"><strong>牧云电台不收集、不存储、不共享任何可识别你身份的信息。</strong> 没有账号，没有自建后端，不内嵌广告、分析或追踪 SDK。</p>

<h3>我们处理什么、在哪处理</h3>
""" + table([
        ("你添加的电台名称与地址", "在本地保存你的电台列表", "设备本地"),
        ("收藏、最近播放、音量等偏好", "恢复上次的使用状态", "设备本地；如开启 iCloud 则同步到你自己的 iCloud 账户"),
        ("播放状态", "支持后台播放与锁屏控制", "设备内存"),
    ], ["数据", "用途", "位置"]) + """

<h3>网络通信</h3>
<p>音频内容<strong>直接从对应的网络音频源传输到你的设备</strong>。我们不存储、不分析、不再分发任何音频内容。此外，应用会访问公开的电台目录服务（radio-browser.info 及其镜像）以搜台，请求中不含你的个人信息。</p>

<h3>iCloud 同步</h3>
<p>如果你开启了 iCloud 同步，电台列表与收藏会保存在<strong>你自己的 iCloud 账户</strong>里（使用 Apple 的键值存储）。我们无法读取这些数据。</p>

<h3>我们不做的事</h3>
""" + ul([
        "不要求注册或登录",
        "不收集姓名、邮箱、电话、位置",
        "不收集音频内容或播放记录",
        "不接入广告、分析或统计服务",
        "不把任何数据共享给第三方",
    ]) + """

<h3>儿童隐私</h3>
<p>我们不主动收集 13 岁以下儿童的任何个人信息。若你认为有儿童在使用本应用并提供了个人信息，请通过下方支持页联系我们。</p>

<h3>数据删除</h3>
<p>删除 App 即可清除全部本地数据。若开启过 iCloud 同步，请在系统「设置 → Apple 账户 → iCloud → 管理账户存储」中删除「牧云电台」的数据。</p>

<h2 id="en">English</h2>

<p class="lead"><strong>Gwave does not collect, store, or share any personally identifiable information.</strong> No account, no backend, no ads, analytics, or tracking.</p>

<h3>What we process, and where</h3>
""" + table([
        ("Station names and URLs you add", "Keep your station list on device", "On your device"),
        ("Favorites, recents, volume", "Restore your last state", "On device; synced to your own iCloud if enabled"),
        ("Playback state", "Background audio and lock screen controls", "Device memory"),
    ], ["Data", "Purpose", "Where"]) + """

<h3>Network</h3>
<p>Audio streams go <strong>directly from their source to your device</strong>. We do not store, analyse, or redistribute any audio. The app also queries a public radio directory (radio-browser.info and mirrors) to search stations; those requests carry no personal information.</p>

<h3>iCloud sync</h3>
<p>If you enable iCloud sync, your station list and favorites are stored in <strong>your own iCloud account</strong> using Apple's key-value store. We cannot read them.</p>

<h3>What we do not do</h3>
""" + ul([
        "No account or sign-in",
        "No name, email, phone, or location collection",
        "No collection of audio content or listening history",
        "No ads, analytics, or statistics services",
        "No data sharing with third parties",
    ]) + """

<h3>Children's privacy</h3>
<p>We do not knowingly collect information from children under 13. If you believe a child has provided personal information, contact us via the support page.</p>

<h3>Deletion</h3>
<p>Delete the app to clear local data. If you enabled iCloud sync, remove Gwave data in Settings, Apple Account, iCloud, Manage Account Storage.</p>
"""})

    write(d, "support.html", {
        "title": "牧云电台 · 支持 / Support",
        "accent": "#30B0C7", "accent_dark": "#40C8E0",
        "footer": "牧云电台 Gwave · 网络电台与白噪声播放器",
        "body": """
<h1>牧云电台 · 支持</h1>
<p class="meta">Gwave — Support · 最后更新 / Last updated: 2026-10-08</p>

<h2 id="zh">中文</h2>

<div class="faq">
<strong>怎么添加自己的电台？</strong>
<p>三种方式：在应用内手动输入名称和地址；从文件导入 JSON 或文本列表；或者用 <code>gwave://</code> 链接直接添加。也支持用网址导入整份播放列表。</p>

<strong>某个电台放不出来？</strong>
<p>网络电台的可用性完全取决于源站。常见原因：源站已下线、临时故障、或该地区无法访问。可以换同一电台的其它线路，或稍后重试。</p>

<strong>后台播放怎么用？</strong>
<p>播放后按 Home 键或锁屏即可持续播放，锁屏界面和「正在播放」面板可以控制。若被系统中断，重新打开应用即可恢复。</p>

<strong>iCloud 同步没生效？</strong>
<p>确认系统「设置 → Apple 账户 → iCloud」里，本应用的开关是打开的。同步不是即时的，通常几十秒内完成；也可以手动下拉刷新。</p>

<strong>白噪声是什么？</strong>
<p>应用内置的雨声、海浪、粉红噪声等音效，在本机实时合成，不占存储、不需要网络。适合助眠或专注。</p>

<strong>怎么反馈问题？</strong>
<p>到 <a href="https://github.com/zhipengge/apps/issues">GitHub Issues</a> 提交，附上电台地址、系统版本和现象。</p>
</div>

<h2 id="en">English</h2>

<div class="faq">
<strong>Adding your own station</strong>
<p>Three ways: type a name and URL in the app, import a JSON or text list from a file, or open a <code>gwave://</code> link. You can also import a whole playlist from a URL.</p>

<strong>A station will not play</strong>
<p>Network radio availability depends entirely on the source. Common causes: the stream is down, temporarily failing, or blocked in your region. Try another stream for the same station, or retry later.</p>

<strong>Background playback</strong>
<p>Press Home or lock the screen; audio continues. Use the lock screen or Now Playing panel to control it. If the system interrupts playback, reopen the app to resume.</p>

<strong>iCloud sync is not working</strong>
<p>Check that the app is enabled under Settings, Apple Account, iCloud. Sync is not instant; it usually completes within a minute. Pull to refresh to force it.</p>

<strong>What are the built-in sounds</strong>
<p>Rain, waves, pink noise and others are synthesised on-device in real time. They take no storage and need no network. Useful for sleep or focus.</p>

<strong>Reporting a problem</strong>
<p>File an issue at <a href="https://github.com/zhipengge/apps/issues">GitHub Issues</a> with the station URL, your OS version, and what happened.</p>
</div>
"""})


def record(d: Path):
    write(d, "privacy.html", {
        "title": "效率打卡 · 隐私政策 / Privacy Policy",
        "accent": "#34C759", "accent_dark": "#30D158",
        "footer": "效率打卡 RecordBot · 本地优先的打卡与指标记录",
        "body": """
<h1>效率打卡 · 隐私政策</h1>
<p class="meta">RecordBot — Privacy Policy · 最后更新 / Last updated: 2026-10-08</p>

<h2 id="zh">中文</h2>

<p class="lead"><strong>「效率打卡」以本地优先为设计原则，你的打卡、指标和档案默认只存在这台设备上。</strong> 没有账号，我们也不运营用于存储你个人数据的中央服务器。</p>

<h3>我们处理什么、在哪处理</h3>
""" + table([
        ("打卡任务的标题、描述、时间范围与重复规则", "展示任务并按规则调度提醒", "设备本地数据库"),
        ("打卡记录", "统计与可视化", "设备本地数据库"),
        ("健康类指标（如体重、身高等）", "记录与趋势图", "设备本地数据库"),
        ("用户档案名称与外观设置", "区分多个使用者", "设备本地数据库"),
        ("你主动附加的照片或文件", "保存到对应的本地任务中", "设备本地"),
    ], ["数据", "用途", "位置"]) + """

<h3>设备权限</h3>
<p>只在必要时申请，且仅在你授权后使用：</p>
""" + ul([
        "<strong>通知</strong>：在你开启提醒时，于本地调度任务提醒。通知由系统在本机触发，不经过任何服务器。",
        "<strong>照片 / 文件</strong>：仅在你主动导入附件或从相册添加图片时使用，把选中的内容保存到本地任务。",
    ]) + """
<p>拒绝某项权限只会导致对应功能不可用，不影响其它本地功能。</p>

<h3>我们不做的事</h3>
""" + ul([
        "不要求注册或登录",
        "不把打卡记录、指标数据上传到服务器",
        "不接入广告网络、分析或追踪 SDK",
        "不把你的数据出售或用于广告画像",
        "不读取通讯录、位置、麦克风、摄像头",
    ]) + """

<h3>数据的导出</h3>
<p>应用提供导入 / 导出功能。当你导出时，数据会以你选择的方式（例如文件分享）<strong>离开设备</strong>，请自行妥善保管导出文件。</p>

<h3>数据删除</h3>
<p>在应用内删除对应的任务、记录或档案即可移除；删除整个 App 会清除全部本地数据。</p>

<h2 id="en">English</h2>

<p class="lead"><strong>RecordBot is local-first. Your check-ins, metrics, and profiles stay on this device by default.</strong> No account, and we do not run a central server for your personal data.</p>

<h3>What we process, and where</h3>
""" + table([
        ("Task titles, descriptions, date ranges, repeat rules", "Show tasks and schedule reminders", "Local database on device"),
        ("Check-in records", "Statistics and charts", "Local database on device"),
        ("Health metrics such as weight and height", "Recording and trend charts", "Local database on device"),
        ("Profile names and appearance settings", "Support multiple users", "Local database on device"),
        ("Photos or files you attach", "Attach to the matching local task", "On device"),
    ], ["Data", "Purpose", "Where"]) + """

<h3>Device permissions</h3>
""" + ul([
        "<strong>Notifications</strong>: schedule task reminders locally when you enable them. Triggered by the system on-device, never through a server.",
        "<strong>Photos / Files</strong>: only when you import an attachment or add a photo, to save your selection to a local task.",
    ]) + """
<p>Denying a permission only disables that feature; everything else keeps working.</p>

<h3>What we do not do</h3>
""" + ul([
        "No account or sign-in",
        "No upload of check-ins or metrics to any server",
        "No ads, analytics, or tracking SDKs",
        "No selling your data or using it for ad profiling",
        "No access to Contacts, Location, Microphone, or Camera",
    ]) + """

<h3>Export</h3>
<p>The app offers import and export. When you export, data <strong>leaves the device</strong> by whatever route you choose (for example file sharing). Keep those files safe.</p>

<h3>Deletion</h3>
<p>Delete tasks, records, or profiles in-app to remove them; deleting the app clears all local data.</p>
"""})

    write(d, "support.html", {
        "title": "效率打卡 · 支持 / Support",
        "accent": "#34C759", "accent_dark": "#30D158",
        "footer": "效率打卡 RecordBot · 本地优先的打卡与指标记录",
        "body": """
<h1>效率打卡 · 支持</h1>
<p class="meta">RecordBot — Support · 最后更新 / Last updated: 2026-10-08</p>

<h2 id="zh">中文</h2>

<div class="faq">
<strong>提醒没有按时出现？</strong>
<p>先确认系统「设置 → 通知 → 效率打卡」里的通知权限是打开的。另外，提醒由系统在本地调度，开启「低电量模式」或系统深度省电时可能延迟。</p>

<strong>重复规则怎么设？</strong>
<p>新建或编辑任务时可以设置重复：按天、按周、按自定义间隔。到期未打卡的记录会保留，方便补打卡。</p>

<strong>怎么记录体重、身高等指标？</strong>
<p>在「指标」页添加。可以给不同用户档案分别记录，图表按档案分开显示。</p>

<strong>怎么备份或换手机？</strong>
<p>用导出功能生成文件，在新设备上用导入功能恢复。数据不会自动上云，换机前记得先导出。</p>

<strong>多个使用者怎么区分？</strong>
<p>用「档案」功能。每个档案有独立的打卡记录和指标，互不干扰。</p>

<strong>数据存在哪里？</strong>
<p>只在这台设备上。详见<a href="privacy.html">隐私政策</a>。</p>

<strong>怎么反馈问题？</strong>
<p>到 <a href="https://github.com/zhipengge/apps/issues">GitHub Issues</a> 提交，附上系统版本和复现步骤。</p>
</div>

<h2 id="en">English</h2>

<div class="faq">
<strong>Reminders do not fire on time</strong>
<p>Check that notifications are allowed under Settings, Notifications, RecordBot. Reminders are scheduled locally by the system, so Low Power Mode or aggressive battery saving may delay them.</p>

<strong>Setting repeat rules</strong>
<p>When creating or editing a task you can set it to repeat daily, weekly, or at a custom interval. Missed days are kept so you can backfill.</p>

<strong>Recording weight or height</strong>
<p>Add them on the Metrics tab. Each profile tracks its own metrics, and charts are shown per profile.</p>

<strong>Backing up or moving to a new phone</strong>
<p>Export to a file, then import it on the new device. Nothing syncs to the cloud automatically, so export before you switch.</p>

<strong>Multiple users</strong>
<p>Use Profiles. Each profile keeps its own check-ins and metrics.</p>

<strong>Where is my data</strong>
<p>Only on this device. See the <a href="privacy.html">Privacy Policy</a>.</p>

<strong>Reporting a problem</strong>
<p>File an issue at <a href="https://github.com/zhipengge/apps/issues">GitHub Issues</a> with your OS version and steps to reproduce.</p>
</div>
"""})


def spincourt(d: Path):
    write(d, "privacy.html", {
        "title": "野球场分拨助手 · 隐私政策 / Privacy Policy",
        "accent": "#FF9500", "accent_dark": "#FFB340",
        "footer": "野球场分拨助手 SpinCourt · 随机分组工具",
        "body": """
<h1>野球场分拨助手 · 隐私政策</h1>
<p class="meta">SpinCourt — Privacy Policy · 最后更新 / Last updated: 2026-10-08</p>

<h2 id="zh">中文</h2>

<p class="lead"><strong>野球场分拨助手完全离线运行，不收集、不存储、不传输任何个人信息。</strong></p>

<h3>我们不收集任何数据</h3>
<p>包括但不限于：</p>
""" + ul([
        "姓名、电子邮件地址、电话号码",
        "位置信息",
        "设备标识符",
        "使用数据或分析数据",
        "任何其它个人身份信息",
    ]) + """

<h3>本地数据</h3>
<p>应用的全部功能都在你的设备上本地运行。你输入的内容（如参与人数、战队数量、战队名称与颜色）仅存在于设备内存中，不写入服务器，也不发送给任何第三方。关闭应用即消失。</p>

<h3>网络</h3>
<p><strong>本应用不发起任何网络请求。</strong>不需要联网即可使用全部功能。</p>

<h3>第三方服务</h3>
<p>不集成任何第三方服务、分析工具或广告网络。</p>

<h3>儿童隐私</h3>
<p>本应用适用于所有年龄段的用户。由于不收集任何信息，也就不存在儿童信息的收集问题。</p>

<h2 id="en">English</h2>

<p class="lead"><strong>SpinCourt runs entirely offline. It does not collect, store, or transmit any personal information.</strong></p>

<h3>We collect nothing</h3>
<p>This includes, but is not limited to:</p>
""" + ul([
        "Name, email address, phone number",
        "Location",
        "Device identifiers",
        "Usage or analytics data",
        "Any other personally identifiable information",
    ]) + """

<h3>Local data</h3>
<p>Everything runs on your device. What you enter (player count, team count, team names and colours) exists only in memory. It is never written to a server or shared with anyone. Closing the app discards it.</p>

<h3>Network</h3>
<p><strong>The app makes no network requests.</strong> Every feature works offline.</p>

<h3>Third parties</h3>
<p>No third-party services, analytics, or ad networks are integrated.</p>

<h3>Children's privacy</h3>
<p>The app is suitable for all ages. Since nothing is collected, there is no children's data to protect.</p>
"""})

    write(d, "support.html", {
        "title": "野球场分拨助手 · 支持 / Support",
        "accent": "#FF9500", "accent_dark": "#FFB340",
        "footer": "野球场分拨助手 SpinCourt · 随机分组工具",
        "body": """
<h1>野球场分拨助手 · 支持</h1>
<p class="meta">SpinCourt — Support · 最后更新 / Last updated: 2026-10-08</p>

<h2 id="zh">中文</h2>

<div class="faq">
<strong>怎么用？</strong>
<p>设置总人数（2 到 25）和战队数量，点开始，转盘会把每个人随机分到战队里。每个战队有专属颜色和名字。</p>

<strong>分组结果不公平？</strong>
<p>分拨是纯随机。想让实力更均衡，可以多转几次，或者调整战队数量让每组人数更接近。</p>

<strong>能保存分组结果吗？</strong>
<p>应用不保存历史记录，每次分组都是独立的。可以截图保存结果。</p>

<strong>需要联网吗？</strong>
<p>不需要。全部功能离线可用，应用也不发起任何网络请求。</p>

<strong>怎么反馈问题？</strong>
<p>到 <a href="https://github.com/zhipengge/apps/issues">GitHub Issues</a> 提交。</p>
</div>

<h2 id="en">English</h2>

<div class="faq">
<strong>How do I use it</strong>
<p>Set the number of players (2 to 25) and the number of teams, then start. The wheel assigns everyone randomly. Each team gets its own colour and name.</p>

<strong>The teams feel unbalanced</strong>
<p>Assignment is purely random. Spin again for a different draw, or change the team count so the group sizes are closer.</p>

<strong>Can I save past results</strong>
<p>No history is kept; each draw is independent. Take a screenshot if you want to keep one.</p>

<strong>Does it need a network connection</strong>
<p>No. Everything works offline and the app makes no network requests.</p>

<strong>Reporting a problem</strong>
<p>File an issue at <a href="https://github.com/zhipengge/apps/issues">GitHub Issues</a>.</p>
</div>
"""})


APPS = {
    "afu": afu,
    "gwave": gwave,
    "record": record,
    "spincourt": spincourt,
}


def main():
    root = Path(__file__).resolve().parent.parent
    want = sys.argv[1:] or list(APPS)
    for name in want:
        if name not in APPS:
            print(f"未知 app: {name}")
            continue
        print(f"######## {name} ########")
        APPS[name](root / name)


if __name__ == "__main__":
    main()
