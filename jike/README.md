# 即刻 (JiKe)

> A Guake-style drop-down terminal for macOS. Press F12 (Fn+F12 on laptops) to slide a terminal from the screen edge.
> macOS 下拉终端。按 F12（笔记本按 Fn+F12）从屏幕边缘滑出，再按一次收起。配色、快捷键与命令语义对齐 Guake。

---

## 快速开始 / Quick Start

### 下载 / Download

完整版从 GitHub Releases 安装（**不进 Mac App Store**）：

1. 打开 [JiKe Releases](https://github.com/zhipengge/JiKe/releases/latest)
2. 下载 `JiKe-x.y.z.zip`，解压后拖进「应用程序」
3. 首次若被拦截：**右键 → 打开**

营销页与隐私仍在本目录 Pages；安装包只放在 `zhipengge/JiKe` 的 Releases。

### 使用 / Use

1. 打开「即刻」
2. 按 **Fn+F12**（外接键盘可直接按 F12）
3. 终端从屏幕上方滑下，输入命令即可
4. 再按一次同一快捷键，终端收起，进程继续在后台跑

菜单栏图标也可以显示 / 隐藏终端。启动后终端会立刻滑出，光标已在输入位置。

---

## 核心特性 / Features

- 下拉窗口：高度、宽度、左右对齐、贴顶或贴底，均可配置
- 169 套 Guake 配色，默认 Tango（白字黑底）
- 标签、垂直/水平分屏，快捷键与 Guake 相同（例如 Ctrl+Shift+T 新建标签）
- Quick Open：从 traceback / `file:line` 打开源文件
- 右键：拷贝粘贴、分屏、搜索、自定义命令
- 兼容 `.guake.yml` 与 `.jike.yml` 的目录标题
- `jike://` URL：toggle / show / hide / new-tab / execute 等
- 菜单栏运行，Dock 图标可关；支持登录时启动
- macOS 习惯：Cmd+C/V/A/F、拖文件插入路径、在访达中打开当前目录
- Option 默认不当 Meta，方便中文输入

本 App **不启用 App 沙盒**（与系统终端、iTerm 相同），以便 Shell 能访问你的项目文件。不收集、不上传任何数据。

---

## 常见问题 / FAQ

### 按 F12 没反应？

笔记本要按 **Fn+F12**。若仍无效，到「系统设置 → 键盘 → 键盘快捷键」关掉占用 F12 的项。

### 为什么没有进 Mac App Store？

下拉终端必须运行真实本地 Shell。App Store 要求沙盒，沙盒里 PTY 几乎不能用。即刻走公证分发。

### 快捷键怎么是 Ctrl 不是 Cmd？

为了和 Guake 一致。新建标签是 Ctrl+Shift+T，拷贝是 Ctrl+Shift+C。同时也支持 Mac 常用键：Cmd+N / Cmd+W / Cmd+C / Cmd+V / Cmd+F。Command 键对应 Guake 的 Super。

### 标签标题从哪来？

自定义名称优先；否则读当前目录的 `.guake.yml` 或 `.jike.yml`（`title:`）；再否则用终端标题或目录名。

### 怎么远程控制窗口？

```
open 'jike://toggle'
open 'jike://new-tab?path=/tmp'
open 'jike://execute?cmd=ls'
```

### 卸载后怎么清干净？

从「应用程序」删除 App，并删除 `~/Library/Preferences/com.gezhipeng0201.JiKe.plist`。

---

## 反馈 / Support

请到 [GitHub Issues](https://github.com/zhipengge/apps/issues) 提交，标题以 `[即刻]` 开头。

隐私政策：[privacy.html](privacy.html)
