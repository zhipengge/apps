# 出口合规证明 (Export Compliance) — 即刻 / JiKe

> 对应 Info.plist：`ITSAppUsesNonExemptEncryption = NO`

---

## 已完成的修改

在 `JiKe.xcodeproj/project.pbxproj` 中，主 App Debug / Release 都加了：

```
INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO;
```

验证：

```bash
plutil -p "DerivedData/Build/Products/Debug/JiKe.app/Contents/Info.plist" | grep ITSApp
# "ITSAppUsesNonExemptEncryption" => false
```

---

## 为什么填 NO

选择 NO（豁免）满足任一即可：

1. App 完全没有加密；或
2. 加密仅用于认证 / 签名 / DRM / 苹果系统或标准 HTTPS/TLS，且没有自研算法。

即刻是本地终端：PTY、配置、热键都不走网络。用户若在终端里自己使用 `ssh` / `curl`，那是用户进程，不是 App 内置加密。App 本身没有 HTTPS 客户端、没有自研加密、没有 DRM。

**结论**：满足条件 1，填 `NO`。

本 App **不通过 Mac App Store 分发**（无沙盒）。若以后改为走 Connect 上传，此 key 仍然有效，可跳过每次问卷。

---

## 后续

- 不要改回 YES，除非加了自研加密或非标准协议
- 若以后加「检查更新」等系统 HTTPS，仍可填 NO（标准协议豁免）
- 填 NO 的 App 不需要每年上传自我分类报告

参考：

- [Apple — Export compliance documentation](https://developer.apple.com/help/app-store-connect/reference/export-compliance-documentation/)
