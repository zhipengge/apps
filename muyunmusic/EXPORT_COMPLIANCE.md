# 出口合规证明 (Export Compliance) — 牧云音乐

## 结论

`ITSAppUsesNonExemptEncryption = NO`

## 为什么可以填 NO

App 的对外网络只有两类，且都是**标准系统框架的 HTTPS/TLS**：

- 用户粘贴的直连地址取音频（`URLSession` / `AVURLAsset`，走系统 TLS 栈）；
- 无自有服务器、无统计/广告 SDK，因此不存在任何自研传输协议。

按 Apple 口径，仅使用系统框架提供的标准 TLS 属于**豁免加密**，
填 `NO` 不需要年度自我分类报告。没有自研加密，没有 DRM，
没有端到端加密的用户数据通道（本来就没有任何上传通道）。

| 加密类型 | 用途 | 说明 |
|---|---|---|
| HTTPS (TLS) | 用户自填地址取音频 | 系统框架，豁免 |
| 自研加密 | 无 | — |
| DRM | 无 | — |
| 其他 | 无 | — |

## ⚠️ 与 ATS 是两回事，别看串了

本 App 的 `Info.plist` 里有 **`NSAllowsArbitraryLoadsForMedia = YES`**
（仅此一条媒体面例外，为用户自填的 http 音源服务；**无全局
`NSAllowsArbitraryLoads`**）。

ATS 是「是否强制 TLS」的**安全策略开关**，不是加密实现——它不影响出口合规
答案，两个问题别互相引用。家族同案：MuyunTV / 牧云电台对自填 http 源
用同一口径，审核问询时按「仅连接用户指定的源」作答。

## 构建配置

`MuYunMusic.xcodeproj` 的两个 configuration（Debug / Release）都设了：

```
INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO
```

这是 build setting，源码 Info.plist 里看不到它，必须从构建产物验证。
ATS 那条则在 `MuYunMusic/Info.plist` 源文件里。

## 怎么验（每次发布前重跑）

```bash
plutil -p "$APP/MuYunMusic.app/Info.plist" | grep ITSApp
# 期望：  "ITSAppUsesNonExemptEncryption" => 0

plutil -p "$APP/MuYunMusic.app/Info.plist" | grep -A4 AppTransportSecurity
# 期望：只有 NSAllowsArbitraryLoadsForMedia = 1，
#       任何位置出现 NSAllowsArbitraryLoads（全局键）= 发布阻断项
```

## 年度报告

无需年度自我分类报告。若将来加入云同步或自研加密，重新评估并更新本文件。
