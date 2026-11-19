# 牧云音乐 上架提交清单

> 版本 1.0（build 1）· 最后更新 2026-11-18
> 目标：手动 archive → 建 App Record（若未建）→ 上传构建 → 按本清单填 App Store Connect → 单独提审。
> 文案/截图/隐私页/权限说明已备好；真正的阻塞项见「二」。

## 一、已备好的材料

| 材料 | 位置 | 状态 |
|---|---|---|
| 商店文案（推广/描述/副标题/关键词） | `APP_STORE_LISTING.md` §1–§4 | ✅ 可直接复制 |
| 审核备注（英文/中文） | `APP_STORE_LISTING.md` §9、`review-notes.txt` | ✅ |
| 4 张 6.9" iPhone 截图 | `screenshots/iphone/` | ✅ 1320×2868，连续全景切片（统一向右倾、同高） |
| 4 张 13" iPad 截图 | `screenshots/ipad/` | ✅ 2064×2752，连续全景切片（统一向右倾、同高） |
| 原创演示曲目/歌词 | `screenshots/showcase/` | ✅ 8 首假歌、3 份 LRC、8 张封面 |
| 随包曲目/权利 | App 资源 `Resources/BuiltIn/` | ✅ 《冬日之光》（词：Deepseek；曲/演唱：Minimax；WAV + LRC + 封面）；上架前确认词曲/录音发行权 |
| 隐私政策 | `privacy.html` / `PRIVACY.md` | ✅ 已含相机/本地网络/自填服务器 |
| 技术支持 | `support.html` | ✅ 已更新 |
| 页面部署 | GitHub Pages | ✅ 2026-11-18 两 URL 均 200 |
| 出口合规 | `EXPORT_COMPLIANCE.md` | ✅ ITSAppUsesNonExemptEncryption = NO |
| App 隐私答案 | `APP_STORE_LISTING.md` §11 | ✅ 不收集数据 |
| 年龄分级答案 | `APP_STORE_LISTING.md` §12 | ✅ 4+ |
| 内容版权 | `APP_STORE_LISTING.md` §13 | ✅ 随包《冬日之光》词：Deepseek、曲/演唱：Minimax；其余不使用第三方内容 |
| What's New | `WHATS_NEW.txt` | ✅ |
| 隐私清单 | `MuYunMusic/PrivacyInfo.xcprivacy` | ✅ 零收集；UserDefaults CA92.1 + FileTimestamp C617.1 + SystemBootTime 35F9.1 |
| 图标 | `Assets.xcassets/AppIcon.appiconset` | ✅ 1024×1024；浅/深无 alpha，tinted 透明 |
| CarPlay | `Info.plist` / `MuYunMusic.entitlements` | ⏸ 1.0 未启用；CarPlay scene 与 entitlement 已移除，不再阻塞 archive |
| 权限 | `Info.plist` | ✅ 相机 + 本地网络，均有用途说明 |

## 二、真正的阻塞项（按优先级）

1. **App Record**：还没建。上传 archive 前必须先有记录；没有记录，Transporter/Xcode 上传会失败。
   - 名称：牧云音乐
   - 主要语言：简体中文
   - Bundle ID：`com.gezhipeng0201.MuYunMusic`
   - SKU：`muyunmusic-20261103`
   - 类别：音乐（次要：工具）
   - 版权：`2026 Zhipeng Ge`
2. **价格**：未定。建 Record 当天二选一：
   - **免费**：跟牧云电台/电视一致，媒体播放器不坐实「卖内容」；推荐。
   - **¥6 一口价**：2026-10-16 新 app 对照实验；要收就建 Record 当天设，别上线后改。
3. **真机验收**：后台/锁屏/拔耳机/电话打断/相机扫码/本地网络/自填服务器分享，模拟器不能替代。
4. **CarPlay**：1.0 已移除 scene 与 entitlement（`com.apple.developer.carplay-music` 未获批），不再是归档阻塞项；后续版本获批再加回。
5. **手动 archive**：Release，版本 1.0/build 1（或自增），自动签名，上传到 App Store Connect。

## 三、Archive 之后按顺序填

### 1. 建/确认 App Record
用上面的名称、主要语言、Bundle ID、SKU、类别、版权。**先 Record，后上传构建**。

### 2. 上传构建
Xcode Organizer → Archive → Distribute App → App Store Connect → Upload。
等 ASC「处理完成」；在 TestFlight 里先装一台真机。

### 3. 版本信息
| 字段 | 值 |
|---|---|
| 推广文本 | `APP_STORE_LISTING.md` §1 |
| 描述 | §2 |
| 副标题 | §3 |
| 关键词 | §4 |
| 技术支持 URL | https://zhipengge.github.io/apps/muyunmusic/support.html |
| 隐私政策 URL | https://zhipengge.github.io/apps/muyunmusic/privacy.html |
| 营销 URL | 留空 |
| 版权 | `2026 Zhipeng Ge` |

### 4. 截图
- 先传 6.9" iPhone：`screenshots/iphone/01-library.png`、`02-lyrics`、`03-queue`、`04-settings`。
- 再传 13" iPad：`screenshots/ipad/01-library.png`、`02-lyrics`、`03-settings`。
- 顺序按 LISTING §7；尺寸分别是 1320×2868 与 2064×2752。

### 5. App 隐私
路径：App → App 隐私。
- Do you or your third-party partners collect data? **No**。
- 隐私政策 URL 填上面的。
- 相机/本地网络是系统权限，不是数据收集；不要额外勾「Data Collected」。

### 6. 年龄分级
按 LISTING §12 全 None/No；结果 4+。
- 无限制网页访问：No。
- 内购/广告/公开 UGC/社交：No。

### 7. 内容版权
**DOES_NOT_USE_THIRD_PARTY_CONTENT**。App 不含第三方内容；一切来自用户导入/自填地址/自建服务器。

### 8. 价格与销售范围
按第二节拍板。销售范围默认所有国家/地区；如果进入 EU，按账号实际情况填 DSA 交易者状态。
若选 ¥6：先确认 Paid Apps 协议、税务与银行信息完整，否则价格不可用；免费则不需要。

### 9. 审核信息
- 联系：账号已有联系人（姓名/电话/邮箱）。
- 演示账号：留空；备注写明无需账号。
- 备注：粘贴 `review-notes.txt`（英文）。
- 不需要登录、不需要演示视频。

### 10. 构建与出口合规
- 选择刚上传的 build。
- 出口合规选「否/NO」（`ITSAppUsesNonExemptEncryption = NO` 已在 plist；若 ASC 仍询问，按 EXPORT_COMPLIANCE.md 答）。
- What's New 粘贴 `WHATS_NEW.txt`。

### 11. 提交
**单独提交**，不要和牧云电台/牧云电视同批；4.3 暴露面最小化。

### 12. 被审核问到时的口径
- ATS 两条：`NSAllowsArbitraryLoads` + `NSAllowsArbitraryLoadsForMedia` 都只为用户自填的 http 服务器/地址；无内置 host。
- 网络三类：用户自填家庭影音服务器、Wi-Fi 传歌（默认关）、直连 URL。
- 相机：可选扫码，画面本机识别，不保存/上传。
- 本地网络：可选连用户自己的局域网服务器，不扫描/发现设备。
- 内容：除随包一首词：Deepseek、曲/演唱：Minimax 的《冬日之光》外，不内置、不抓取、不推荐任何第三方曲库；没有公开 UGC 信息流。
完整英文答案见 `APP_STORE_LISTING.md` §9。

## 四、提交前真机验收清单

- [ ] 用「文件」App 导入 mp3/m4a/flac；用分享扩展导入；用 Finder/iTunes 文件共享导入。
- [ ] 后台播放、锁屏控制、控制中心、耳机线控 ±15s/上下曲。
- [ ] 拔耳机/蓝牙断开→暂停且不自动续播；来电打断→手动恢复。
- [ ] 播放队列：点行切歌、拖动排序、添加到队列、清空（当前曲继续播）。
- [ ] 收藏/最近播放进出；歌曲信息编辑保存后排序更新。
- [ ] 歌词 .lrc 与内嵌歌词；偏移在「详情 → 歌词同步」按曲保存。
- [ ] 设置 → 家庭影音配置：扫码相机权限；填局域网地址触发本地网络权限；测试/搜索/播放/下载/分享。
- [ ] Wi-Fi 传歌：开关打开、同网段电脑上传、关闭后停止。
- [ ] 深色/浅色、iPhone/iPad、横竖屏基本可用。
- [ ] 卸载重装：曲库/收藏/设置清空，不回填任何示例。

## 五、提交后

- 关注 App Store Connect 的审核状态与邮件；被拒时先对照 §9 口径回复，不要临时改产品叙事。
- 通过后确认商店页截图/文案/隐私链接实际打开；再考虑是否推送仓库。

## 六、不要做

- 不要在没有 App Record 时先上传 archive（会失败）。
- 不要和电台/电视同批提交。
- 不要在 ATS/权限描述里写「只有 media-only」或「不申请任何权限」——与当前 Info.plist 不符。
- 不要把演示账号/测试服务器地址填进审核备注。
