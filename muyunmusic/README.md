# 牧云音乐 (MuYunMusic)

纯本地 iOS 音乐播放器。音乐全部由用户自己导入，App 不内置、不聚合、不推荐任何曲库。

- 商店文案：[`APP_STORE_LISTING.md`](./APP_STORE_LISTING.md)
- 隐私政策：[`privacy.html`](./privacy.html) ・ [`PRIVACY.md`](./PRIVACY.md)
- 技术支持：[`support.html`](./support.html)
- 出口合规：[`EXPORT_COMPLIANCE.md`](./EXPORT_COMPLIANCE.md)

## 页面地址（部署后在 GitHub Pages 上）

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
Wi-Fi 传歌网页 / 自填直连 URL）、lrc 与内嵌歌词、曲库五视图六排序、自建歌单、
随机与三态循环（一个按钮循环切）、倍速与定时停止、后台与锁屏控制、
局域网 Wi-Fi 传歌。0 内置内容、0 统计、0 广告、0 系统权限申请，数据全本机。

## 素材状态

| 项 | 状态 |
|---|---|
| 商店文案 | ✅ 本目录，2026-11-11 按当前界面写成（1.0 实现，模拟器已验收） |
| 隐私政策 / 支持页 | ✅ 本目录（**尚未部署**，Pages 上是 404） |
| 截图 | ⛔ 未拍（6.9" iPhone 必传；`TARGETED_DEVICE_FAMILY = "1,2"` 声明了 iPad，13" iPad 也强制要求） |
| 隐私清单 | ✅ `PrivacyInfo.xcprivacy` 零收集（仅 UserDefaults `CA92.1`） |
| 出口合规 | ✅ `ITSAppUsesNonExemptEncryption = NO`（build setting，发布前按 EXPORT_COMPLIANCE.md 重验产物） |
| 隐私问卷 / 年龄分级答案 | ✅ `_tools/asc/answers/muyunmusic.json` + LISTING §11/§12 |
| App Record | ⛔ **未建**，从未进过任何 ASC 流程 |
| 定价 | ⏳ 未定（家族媒体播放器 precedent 免费 vs 2026-10-16「新 app ¥6」决定，见 LISTING §0） |
| 真机验收 | ⛔ 后台/锁屏/拔耳机/ATS 实机项未做（清单见源码仓库 README「未验证」节） |
