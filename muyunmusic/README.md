# 牧云音乐 (MuYunMusic)

纯本地 iOS 音乐播放器。音乐全部由用户自己导入，App 不内置、不聚合、不推荐任何曲库。

- 商店文案：[`APP_STORE_LISTING.md`](./APP_STORE_LISTING.md)
- 提交清单：[`SUBMISSION_CHECKLIST.md`](./SUBMISSION_CHECKLIST.md)
- 隐私政策：[`privacy.html`](./privacy.html) ・ [`PRIVACY.md`](./PRIVACY.md)
- 技术支持：[`support.html`](./support.html)
- 出口合规：[`EXPORT_COMPLIANCE.md`](./EXPORT_COMPLIANCE.md)
- 截图：[`screenshots/iphone`](./screenshots/iphone) ・ [`screenshots/ipad`](./screenshots/ipad)

## 页面地址（已随 apps 仓库部署）

| 页面 | URL |
|---|---|
| 隐私政策 | https://zhipengge.github.io/apps/muyunmusic/privacy.html |
| 技术支持 | https://zhipengge.github.io/apps/muyunmusic/support.html |

## 标识符

| 字段 | 值 |
|---|---|
| 显示名 | 牧云音乐 |
| Bundle ID | `com.gezhipeng0201.MuYunMusic` |
| 分享扩展 Bundle ID | `com.gezhipeng0201.MuYunMusic.Share` |
| App Group | `group.com.gezhipeng0201.MuYunMusic`（仅主 App ↔ 分享扩展中转） |
| SKU | `muyunmusic-20261103` |
| 源码仓库 | `zhipengge/MuYunMusic`（私有） |

## 一句话产品说明

六条导入通道（文件 App 打开 / 分享扩展 / iTunes 文件共享 / iCloud 选择器 /
Wi-Fi 传歌网页 / 自填直连 URL 或家庭影音服务器）、lrc 与内嵌歌词、曲库五段
（歌曲/专辑/艺术家/歌单/已下载）、「我的音乐」收藏与最近播放、歌曲信息编辑、
自建歌单、随机与三态循环（一个按钮循环切）、定时停止、后台与锁屏控制、
播放队列管理、局域网 Wi-Fi 传歌。0 内置内容、0 统计、0 广告、0 账号；
只有相机（可选扫码）与本地网络（可选连自填服务器）两项权限。

## 素材状态

| 项 | 状态 |
|---|---|
| 商店文案 | ✅ 2026-11-18 按当前界面校对（1.0，#t73 后） |
| 隐私政策 / 支持页 | ✅ 已部署并验 200（2026-11-18） |
| 截图 | ✅ 4 张 6.9" iPhone（1320×2868）+ 4 张 13" iPad（2064×2752），连续全景（3 个斜置屏统一向右倾、跨 4 张），尺寸/撞边检查通过；旧版在 `screenshots/classic` |
| 隐私清单 | ✅ `PrivacyInfo.xcprivacy` 零收集（UserDefaults `CA92.1` + FileTimestamp `C617.1` + SystemBootTime `35F9.1`） |
| 出口合规 | ✅ `ITSAppUsesNonExemptEncryption = NO`（build setting，产物已验） |
| 图标 | ✅ 1024×1024；浅色/深色无 alpha（ASC 要求），tinted 透明 |
| ATS | ⚠️ `NSAllowsArbitraryLoads` + `NSAllowsArbitraryLoadsForMedia`（仅用户自填 http 源；无内置地址） |
| 相机 / 本地网络权限 | ✅ Info.plist 两条 usage description + 隐私页同步 |
| 隐私问卷 / 年龄分级 / 内容版权 | ✅ `_tools/asc/answers/muyunmusic.json` + LISTING §11–§13 |
| CarPlay entitlement | ⚠️ 需确认 Apple 已批准 `com.apple.developer.carplay-music`（未批准则先移除 CarPlay 再 archive） |
| App Record | ⛔ **未建**；archive 后先建 Record 再上传构建 |
| 定价 | ⏳ 未定（免费 vs ¥6，LISTING §0） |
| 真机验收 | ⛔ 后台/锁屏/拔耳机/电话打断/相机/本地网络未做（最大欠账） |
| 构建上传 | ⏳ 手动 archive + 上传 |
