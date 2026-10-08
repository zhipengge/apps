# 出口合规说明 — 速闻 (Speed)

## 结论

每个 native target 的 Debug 与 Release 都填：

```
INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO
```

本 App 只有主 App 一个 native target，无扩展。

## 为什么填 NO

速闻没有任何自研加密算法。它对网络的使用只有一处：通过苹果系统提供的标准 HTTPS，从公开仓库拉取每日新闻内容。

阅读记录与收藏全部保存在设备本地，不上传，也就不涉及传输加密。

因此满足条件 2。

## 参考

- 适用条件 1：App 完全没有加密。
- 适用条件 2：加密仅用于认证 / 签名 / DRM / 走苹果系统或标准 HTTPS/TLS，没有自研算法。

速闻 满足**条件 2**。

---

最后更新：2026-10-08
