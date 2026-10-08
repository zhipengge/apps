# 出口合规说明 — 阿福 (Afu)

## 结论

每个 native target 的 Debug 与 Release 都填：

```
INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO
```

本 App 只有主 App 一个 native target，无扩展。

## 为什么填 NO

阿福没有任何自研加密算法。它对 HTTPS 的使用仅有两处：拉取公开的模型清单、从 Hugging Face 下载模型权重。两者都是通过苹果系统提供的标准 TLS 完成的，没有自带或自研的加密实现。

聊天内容、图片、文件全部在本机处理，不经过网络传输，也就不涉及加密。

因此满足条件 2。

## 参考

- 适用条件 1：App 完全没有加密。
- 适用条件 2：加密仅用于认证 / 签名 / DRM / 走苹果系统或标准 HTTPS/TLS，没有自研算法。

阿福 满足**条件 2**。

---

最后更新：2026-10-08
