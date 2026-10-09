# 出口合规说明 — 自律勇者 (SelfQuest)

## 结论

每个 native target 的 Debug 与 Release 都填：

```
INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO
```

本 App 只有主 App 一个 native target，无扩展。

## 为什么填 NO

自律勇者没有任何自研加密算法，也完全没有网络代码。

App 的每一项功能都在本机完成，不发起任何网络请求，数据全部保存在设备沙盒内的一个 JSON 文件中。飞行模式下全部功能可用。

因此满足条件 1（App 完全没有加密）。

## 参考

- 适用条件 1：App 完全没有加密。
- 适用条件 2：加密仅用于认证 / 签名 / DRM / 走苹果系统或标准 HTTPS/TLS，没有自研算法。

自律勇者 满足**条件 1**。

---

最后更新：2026-10-08
