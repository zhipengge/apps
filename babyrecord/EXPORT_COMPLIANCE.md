# 出口合规证明 (Export Compliance)

## 已完成的修改

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

满足苹果豁免条件 1：**App 完全没有加密功能。**

牧云宝宝记是纯本地工具，不发起网络请求，没有 HTTPS/TLS，没有自研加密，没有 DRM，没有加密存储（JSON 明文写在沙盒里）。

不需要每年上传自我分类报告。

若以后加入 iCloud 同步（系统 CloudKit）或标准 HTTPS，仍可走对应豁免并保持 NO；只有自研加密才需要重新评估。
