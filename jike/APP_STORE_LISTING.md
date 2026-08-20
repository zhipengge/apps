# 即刻 (JiKe) 发布素材

> 即刻**不走 Mac App Store**：真实本地 PTY 无法放进 App 沙盒，审核过不了。
> 下面文案按 App Store Connect 字段上限写好，去掉了违禁字符，方便以后政策变化或用于官网 / 公证页。
> 中英各一份。不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带 `://` 的字面量。

---

## 0️⃣ 标识符（已定死，勿改）

| 字段 | 填什么 |
|---|---|
| 平台 | macOS |
| 名称（简体中文） | **即刻**（备选：即刻终端） |
| 名称（English） | **JiKe** |
| 主要语言 | 简体中文 |
| Bundle ID | `com.gezhipeng0201.JiKe` |
| SKU | `jike-20260820` |
| 最低系统 | macOS 14.0 |
| 类别 | 开发者工具 / Developer Tools |
| 分发 | 公证 + 直接分发（无沙盒） |

设备显示名是「即刻」。工程内部 target / PRODUCT_NAME 仍是 `JiKe`。

---

## 1️⃣ 推广文本 (Promotional Text)

> **上限 170 字符**

### 简体中文

```
按 Fn+F12 呼出下拉终端。配色与快捷键对齐 Guake，标签分屏、快速打开、菜单栏后台运行。本地 Shell，零追踪。
```
**字符数：62 / 170**

### English

```
Press F12 to drop a terminal from the screen edge. Guake-compatible palettes and shortcuts, tabs, splits, Quick Open. Local shell, zero tracking.
```
**字符数：145 / 170**

---

## 2️⃣ 描述 (Description)

> **上限 4000 字符**

### 简体中文

```
即刻是 macOS 下拉终端。按 Fn+F12（外接键盘可直接按 F12）从屏幕边缘滑出，再按一次收起，终端进程继续在后台运行。

【对齐 Guake】
- 默认快捷键与 Guake 相同：F12 呼出，Ctrl+Shift+T 新建标签，Ctrl+Shift+C 拷贝
- 内置 169 套 Guake 配色，默认 Tango
- 兼容 .guake.yml 目录标题，以及 GUAKE_TAB_UUID 环境变量
- 可用 jike URL 切换窗口、新建标签、执行命令

【日常使用】
- 标签与垂直/水平分屏
- Quick Open：从报错信息里的路径和行号打开文件
- 右键菜单：拷贝粘贴、搜索、自定义命令
- 菜单栏图标，Dock 可隐藏，支持登录时启动
- 窗口高度、宽度、对齐、透明度均可配置
- 按 macOS 习惯：Cmd+C/V/A/F，拖文件插入路径，在访达中打开当前目录

即刻在本地伪终端中运行你的登录 Shell，不收集、不上传任何数据。因需要完整本地终端能力，本 App 不启用沙盒，也不通过 Mac App Store 分发。
```
**字符数：438 / 4000**

### English

```
JiKe is a drop-down terminal for macOS. Press F12 (Fn+F12 on laptops) to slide it from the screen edge, press again to hide. Sessions keep running in the background.

[Guake-compatible]
- Same default shortcuts: F12 to toggle, Ctrl+Shift+T for a new tab, Ctrl+Shift+C to copy
- 169 Guake palettes, Tango by default
- Reads .guake.yml directory titles and sets GUAKE_TAB_UUID
- jike URLs can toggle the window, open tabs, and run commands

[Everyday use]
- Tabs and vertical/horizontal splits
- Quick Open: jump from file:line in compiler output
- Context menu: copy, paste, search, custom commands
- Menu bar extra, optional Dock icon, launch at login
- Configurable size, alignment, and opacity
- macOS-native copy/paste, drag-and-drop paths, Reveal in Finder

JiKe runs your login shell in a local pseudo-terminal. It collects nothing and uploads nothing. It is not sandboxed (same as Terminal and iTerm) and is distributed outside the Mac App Store.
```
**字符数：888 / 4000**

---

## 3️⃣ 副标题 (Subtitle)

> **上限 30 字符**

中文：`Fn+F12 呼出的下拉终端`（14）

English: `Guake-style drop-down terminal`（30）

---

## 4️⃣ 关键词 (Keywords)

> **上限 100 字符**，含逗号；不要重复 App 名

中文：`终端,下拉,命令行,开发,shell,zsh,快捷键,分屏,配色`

English: `terminal,dropdown,shell,zsh,developer,hotkey,split,palette,guake`

---

## 5️⃣ 链接

| 用途 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/jike/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/jike/privacy.html` |
| 营销页 | `https://zhipengge.github.io/apps/jike/` |

提交前用浏览器亲自打开，确认 200。

---

## 6️⃣ 隐私问卷

与 `PRIVACY.md` 一致：**不收集数据**。不要勾联系人、位置、追踪。

「在网页搜索」是用户主动让系统浏览器打开，不算 App 收集诊断数据。

---

## 7️⃣ 截图

待补。macOS 常用 **1280×800**，3–10 张真实界面：下拉窗、设置-外观、设置-权限、分屏、菜单栏。

---

## 8️⃣ 内容评级

无暴力、无色情、无用户生成内容审核负担。工具类，4+。
