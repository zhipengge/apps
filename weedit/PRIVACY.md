# 文辑 (WeEdit) — 隐私政策 / Privacy Policy

**最后更新 / Last updated: 2026-09-15**

---

## 中文

### 总览

**文辑不收集、不上传、不分享你的文稿。** 正文、图片、音视频和偏好都只在这台 Mac 的沙盒容器里处理。没有账号，没有自建服务器，不内嵌分析、追踪或广告 SDK。

### 我们处理什么、在哪处理

| 数据 | 用途 | 处理/存储位置 |
|---|---|---|
| 文稿 HTML 与标题 | 编辑与本地保存 | 沙盒 Application Support |
| 你插入的图片 / 视频 / 音频 | 显示在文稿中，复制时写入剪贴板 | 沙盒容器内的 media 目录；复制由你点按钮触发 |
| 剪贴板 | 把适配后的 HTML 和纯文本交给系统剪贴板 | 仅在你点「复制」时写入 |
| 远程图片 URL | 若文稿里已有 https 图片，WebKit 会去拉取以便显示 | 设备内存，不上传你的正文 |

### 我们不做的事

- 不把文稿发到任何自建服务器
- 不登录公众号、小红书、知乎、微博
- 不接入广告网络或分析平台
- 不读取通讯录、位置、麦克风、摄像头
- 不要求账号

### 网络通信

出站网络只用于两件事：

1. 显示文稿里已经存在的远程图片（WebKit 按图片自己的地址请求）
2. 你点「打开后台」时，由系统浏览器访问平台站点

请求里不含你的文稿正文。可以断网写稿；只是远程图片会显示不出来，「打开后台」需要浏览器联网。

### 文件访问

运行在 App Sandbox。只能读写你在打开/保存面板里选的文件，以及容器内自己的文稿。不申请完全磁盘访问。

### 数据删除

删除 App，并移除 `~/Library/Containers/com.gezhipeng0201.WeEdit`，即无残留。

### 联系方式

App Store 联系页或本项目仓库 Issue。

---

## English

### Summary

**WeEdit does not collect, upload, or share your drafts.** Articles, media, and preferences stay in the Mac sandbox. No account, no backend, no analytics, tracking, or ads.

### What we process

| Data | Purpose | Where |
|---|---|---|
| Draft HTML and titles | Editing and local save | Sandbox Application Support |
| Images / video / audio you insert | Display and optional clipboard copy | Container media folder; clipboard only when you copy |
| Clipboard | Adapted HTML and plain text | Written only when you press Copy |
| Remote image URLs already in a draft | WebKit fetch for display | Memory only; draft body is not uploaded |

### What we do not do

- No upload of drafts to our servers
- No login to WeChat, Xiaohongshu, Zhihu, or Weibo
- No ads or analytics
- No Contacts, Location, Microphone, or Camera
- No account

### Network

Outbound network is used to display remote images already in a draft, and when you ask the system browser to open a platform editor. Draft text is not sent to us. Writing works offline.

### File access

App Sandbox. Only files you pick in Open/Save, plus the app container. No Full Disk Access.

### Deletion

Remove the app and `~/Library/Containers/com.gezhipeng0201.WeEdit`.

### Contact

App Store contact or repository Issues.
