# 出口合规证明 (Export Compliance) — 今日已赚

## 结论

`ITSAppUsesNonExemptEncryption = NO`

## 为什么可以填 NO

App **不发起任何网络请求**，没有 HTTPS/TLS 客户端，没有自研加密，没有 DRM，
没有端到端加密的用户数据。它只在本地读写 `UserDefaults`。

这比家族里其它 App 更干净：那些 App 至少还有 HTTPS 请求需要说明，本 App 连这条都没有。

| 加密类型 | 用途 | 说明 |
|---|---|---|
| HTTPS (TLS) | 无 | App 不联网 |
| 自研加密 | 无 | — |
| DRM | 无 | — |
| 其他 | 无 | — |

## 构建配置

`MoneyToday.xcodeproj` 的两个 configuration（Debug / Release）都设了：

```
INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO
```

这是 build setting，**源码里的 Info.plist 看不到它**，必须从构建产物验证。

## 怎么验（每次发布前重跑）

```bash
plutil -p "$APP/Contents/Info.plist" | grep ITSApp
# 期望：  "ITSAppUsesNonExemptEncryption" => 0
```

## 打包时必须同时确认的一条

0 联网场景下，产物 Info.plist 里**不允许出现任何 ATS 例外键**：

```bash
plutil -p "$APP/Contents/Info.plist" | grep -i NSAppTransportSecurity
# 期望：无输出
```

出现 `NSAllowsArbitraryLoads` 就说明工程被污染了（比如误引入了带网络能力的依赖），
这是发布阻断项，不是豁免项。

## 年度报告

无需年度自我分类报告。若将来加入云同步或自研加密，需要重新评估并更新本文件。
