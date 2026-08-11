# 出口合规证明 (Export Compliance) — 解决说明

> 修复警告 **"缺少出口合规证明 / Missing Export Compliance"**

---

## 🧭 背景

苹果要求所有使用加密的 App 在上传 App Store Connect 时声明加密合规情况（基于美国出口管制条例 EAR）。**任何**用到 HTTPS / TLS 的 App 都会被强制提示。

如果不在 Info.plist 中声明，每次提交 build 都会卡在 "正在等待您审核加密合规问题"，必须手动到 App Store Connect 网页逐项回答。

**一次配置，永久解决**：在 Info.plist 写一个 key，以后所有版本都自动通过。

---

## ✅ 已完成的修改

在 `MuyunImage.xcodeproj/project.pbxproj` 的 **Debug** 和 **Release** 两个 build configuration 各加了一行：

```diff
GENERATE_INFOPLIST_FILE = YES;
+ INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO;
```

> 项目使用 Xcode 的"自动生成 Info.plist"模式（没有独立 Info.plist 文件），
> 通过 `INFOPLIST_KEY_` 前缀的 build setting 把 key 合并到生成的 Info.plist 中。

验证方式：
```bash
# 构建后检查产物
plutil -p "/path/to/牧云图片.app/Contents/Info.plist" | grep ITSApp
# 应输出: "ITSAppUsesNonExemptEncryption" => false
```

---

## 📜 为什么牧云图片可以填 `NO`（豁免）

### 苹果官方判断标准

选择 **NO**（豁免）的条件 — 满足**任一**即可：

1. App 完全没有加密功能；**或**
2. App 中的加密仅用于：
   - (a) 认证、数字签名
   - (b) 版权保护（DRM）
   - (c) 通过苹果系统加密与服务器通信
   - (d) 使用标准开源加密协议（HTTPS / TLS / SSH / SSL）进行通信，且没有自创加密算法

### 牧云图片的实际加密用法

| 加密类型 | 用途 | 落入哪一类豁免 |
|---|---|---|
| **HTTPS (TLS)** | 从 GitHub Releases 下载 LaMa 模型（用户主动触发，唯一网络行为） | (d) 标准开源加密协议 + (c) 苹果系统 URLSession |
| 其他 | 无 — 图像处理全部本地，无自研加密、无 DRM、无端到端加密数据 | 不适用 |

**结论**：牧云图片使用的唯一加密是系统 `URLSession` 发起的标准 HTTPS，没有自研算法、没有 DRM、没有用户数据加密传输 → 完全符合 EAR § 740.17(b)(3) 豁免类别 → 填 `NO`。

### 法律依据
- **EAR 5D002**（信息安全软件分类）
- **§ 740.17(b)(3)** — 标准加密豁免
- **§ 742.15(b)(1)** — 标准加密通信工具豁免

> 这套框架就是大量仅用 HTTPS 的工具类 App 都填 NO 的原因。

---

## 🌐 不修 Info.plist 会发生什么

每次上传 build 后，App Store Connect 会出现：
```
缺少出口合规证明
请回答有关此构建版本的几个问题
```
问卷流程（如果手动答）：

1. **你的 App 是否使用加密?** → 是（HTTPS 也算）
2. **是否仅使用豁免类加密?** → 勾 "(d) 标准加密协议通信"
3. **是否使用专有/非标准加密?** → 否
4. **是否符合 § 740.17(b)(3) 豁免?** → 是
5. **最终用户是否美国/加拿大政府?** → 否

每次新版本上传都要重答 → 烦。**修了 Info.plist 之后整个流程跳过。**

---

## 📋 后续注意事项

1. **不要改回 YES** — 除非以后加了 DRM、自研加密算法、端到端加密同步等"非标准"功能
2. **新增功能时重新评估**：
   - 加 iCloud 同步（系统 CloudKit）→ 仍然 NO（苹果系统加密）
   - 加自定义加密的云备份 → 重新审视
3. 填 NO 的 App **不需要**每年上传自我分类报告

---

## 🔗 参考

- [Apple — Determine your export compliance requirements](https://developer.apple.com/help/app-store-connect/reference/export-compliance-documentation/)
- [Apple — Complying with Encryption Export Regulations](https://developer.apple.com/documentation/security/complying_with_encryption_export_regulations)

---

**牧云图片当前状态：✅ 已配置 ITSAppUsesNonExemptEncryption = false（豁免），提交自动通过。**
