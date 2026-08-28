# 出口合规证明 (Export Compliance) — 牧云电视

主 App target 的 Debug / Release 均已设置：

```
INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO;
```

构建产物核对：

```bash
plutil -p "$APP/Info.plist" | grep ITSApp
# "ITSAppUsesNonExemptEncryption" => false
```

## 为什么可以填 NO

满足苹果豁免条件 2：加密仅用于标准 HTTPS/TLS，走系统 URLSession，没有自研算法、没有 DRM、没有端到端加密用户数据。

| 加密类型 | 用途 | 豁免 |
|---|---|---|
| HTTPS (TLS) | 用户主动导入 https 播放列表；播放 https 直播源；加载 https 台标 | 标准开源协议 + 苹果 URLSession |
| HTTP 明文 | 部分直播源不是 HTTPS | 无加密 |
| 其他 | 无 | 不适用 |

不需要每年上传自我分类报告。

以后若加入自研加密或自定义协议的云同步，需要重新评估。系统 CloudKit 或继续只用 HTTPS 仍可保持 NO。
