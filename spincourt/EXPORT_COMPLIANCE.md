# 出口合规说明 — 野球场分拨助手 (SpinCourt)

## 结论

每个 native target 的 Debug 与 Release 都填：

```
INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO
```

本 App 只有主 App 一个 native target，无扩展。

## 为什么填 NO

野球场分拨助手没有任何加密逻辑，也完全没有网络代码。它不发起任何网络请求，所有计算（随机数生成）都在设备本地完成。

因此满足条件 1。

## 参考

- 适用条件 1：App 完全没有加密。
- 适用条件 2：加密仅用于认证 / 签名 / DRM / 走苹果系统或标准 HTTPS/TLS，没有自研算法。

野球场分拨助手 满足**条件 1**。

---

最后更新：2026-10-08
