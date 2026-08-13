# 出口合规证明 (Export Compliance) — 解决说明

> 修复警告 **"缺少出口合规证明 / Missing Export Compliance"**

---

## 🧭 背景

苹果要求所有使用加密的 App 在上传 App Store Connect 时声明加密合规情况（基于美国出口管制条例 EAR）。**任何**用到 HTTPS / TLS 的 App 都会被强制提示。

如果不在 Info.plist 中声明，每次提交 build 都会卡在 "正在等待您审核加密合规问题"，必须手动到 App Store Connect 网页逐项回答。

**一次配置，永久解决**：在 Info.plist 写一个 key，以后所有版本都自动通过。

---

## ✅ 已完成的修改

在 `SuperRight.xcodeproj/project.pbxproj` 中，**主 App（SuperRight）与访达扩展（SuperRightFinder）两个 target** 的 Debug / Release 共四个 build configuration 各加了一行：

```diff
GENERATE_INFOPLIST_FILE = YES;
+ INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO;
```

> 项目使用 Xcode 的"自动生成 Info.plist"模式，
> 通过 `INFOPLIST_KEY_` 前缀的 build setting 把 key 合并到生成的 Info.plist 中。
> 扩展 target 额外通过 `INFOPLIST_FILE = Config/SuperRightFinderInfo.plist` 提供 `NSExtension` 声明，两者由 Xcode 自动合并。

验证方式：
```bash
# 构建后检查产物（主 App 与扩展各查一次）
plutil -p "/path/to/右键大师.app/Contents/Info.plist" | grep ITSApp
plutil -p "/path/to/右键大师.app/Contents/PlugIns/SuperRightFinder.appex/Contents/Info.plist" | grep ITSApp
# 应输出: "ITSAppUsesNonExemptEncryption" => false
```

---

## 📜 为什么右键大师可以填 `NO`（豁免）

### 苹果官方判断标准

选择 **NO**（豁免）的条件 — 满足**任一**即可：

1. App 完全没有加密功能；**或**
2. App 中的加密仅用于：
   - (a) 认证、数字签名
   - (b) 版权保护（DRM）
   - (c) 通过苹果系统加密与服务器通信
   - (d) 使用标准开源加密协议（HTTPS / TLS / SSH / SSL）进行通信，且没有自创加密算法

### 右键大师的实际加密用法

| 加密类型 | 用途 | 落入哪一类豁免 |
|---|---|---|
| **无** | App 不发起任何网络请求，没有 HTTPS/TLS 调用，没有自研加密、没有 DRM、没有加密存储 | 直接满足条件 1「完全没有加密功能」 |

**结论**：右键大师是纯本地工具——右键菜单、文件模板、路径拷贝、打开终端均不涉及任何加密 API 或网络通信 → 满足最宽松的豁免类别（条件 1，比牧云图片的 HTTPS 豁免场景更简单）→ 填 `NO`。

### 法律依据
- **EAR 5D002**（信息安全软件分类）— 本 App 不落入该分类
- **§ 740.17(b)(3)** — 标准加密豁免（备用依据；本 App 甚至无需援引）

> 无加密、无联网的工具类 App 是出口合规最简单的场景。

---

## 🌐 不修 Info.plist 会发生什么

每次上传 build 后，App Store Connect 会出现：
```
缺少出口合规证明
请回答有关此构建版本的几个问题
```
问卷流程（如果手动答）：

1. **你的 App 是否使用加密?** → 否（无任何加密与网络功能）
2. → 直接通过，无后续问题

每次新版本上传都要重答 → 烦。**修了 Info.plist 之后整个流程跳过。**

---

## 📋 后续注意事项

1. **不要改回 YES** — 除非以后加了网络功能且使用自研加密、DRM、端到端加密等"非标准"功能
2. **新增功能时重新评估**：
   - 加"检查更新"等 HTTPS 请求 → 仍然 NO（标准协议豁免，同牧云图片场景）
   - 加 iCloud 同步（系统 CloudKit）→ 仍然 NO（苹果系统加密）
   - 加自定义加密的云备份 → 重新审视
3. 填 NO 的 App **不需要**每年上传自我分类报告

---

## 🔗 参考

- [Apple — Determine your export compliance requirements](https://developer.apple.com/help/app-store-connect/reference/export-compliance-documentation/)
- [Apple — Complying with Encryption Export Regulations](https://developer.apple.com/documentation/security/complying_with_encryption_export_regulations)

---

**右键大师当前状态：✅ 主 App 与访达扩展均已配置 ITSAppUsesNonExemptEncryption = false（豁免），提交自动通过。**
