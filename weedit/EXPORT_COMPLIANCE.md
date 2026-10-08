# 出口合规证明 (Export Compliance) — 文辑

## 已完成的修改

`WeEdit.xcodeproj` 的 Debug / Release 均有：

```
INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO;
```

验证：

```bash
plutil -p "/path/to/文辑.app/Contents/Info.plist" | grep ITSApp
# "ITSAppUsesNonExemptEncryption" => false
```

## 为什么填 NO

文辑没有自研加密。唯一可能用到的加密是系统 URLSession / WebKit 的标准 HTTPS（显示文稿里已有的远程图片，以及用户让系统浏览器打开平台站点）。符合豁免：(c) 苹果系统加密通信 + (d) 标准 TLS。没有 DRM、没有端到端同步、没有自研算法。
