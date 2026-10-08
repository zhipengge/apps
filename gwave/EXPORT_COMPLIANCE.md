# 出口合规说明 — 牧云电台 (Gwave)

## 结论

每个 native target 的 Debug 与 Release 都填：

```
INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO
```

本 App 只有主 App 一个 native target，无扩展。

## 为什么填 NO

牧云电台没有任何自研加密算法。它对网络的使用全部通过苹果系统提供的标准 HTTPS 完成：拉取公开电台目录、以及从源站拉取音频流。

电台列表与收藏的同步走的是苹果的 iCloud 键值存储，加密由系统负责，本应用不实现加密逻辑。

因此满足条件 2。

## 参考

- 适用条件 1：App 完全没有加密。
- 适用条件 2：加密仅用于认证 / 签名 / DRM / 走苹果系统或标准 HTTPS/TLS，没有自研算法。

牧云电台 满足**条件 2**。

---

最后更新：2026-10-08
