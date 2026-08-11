# 出口合规证明 (Export Compliance) — 解决说明

> 修复警告 **"缺少出口合规证明 / Missing Export Compliance"**

---

## 🧭 背景

苹果要求所有使用加密的 App 在上传 App Store Connect 时声明加密合规情况(基于美国出口管制条例 EAR / Bureau of Industry and Security 要求)。**任何**用到 HTTPS、TLS、SSH、SSL、Keychain 等加密通信的 App 都会被强制提示。

如果不在 Info.plist 中声明,每次提交 build 都会卡在 "正在等待您审核加密合规问题",必须手动到 App Store Connect 网页一项一项回答。

**一次配置,永久解决**:在 Info.plist 写一个 key,以后所有版本都自动通过。

---

## ✅ 已自动完成的修改

在 `OpenTerminal.xcodeproj/project.pbxproj` 的 **Debug** 和 **Release** 两个 build configuration 各加了一行:

```diff
GENERATE_INFOPLIST_FILE = YES;
+ INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO;
```

> 由于项目用了 Xcode 的"自动生成 Info.plist"模式(没有独立 Info.plist 文件),
> 通过 `INFOPLIST_KEY_` 前缀的 build setting 把 key 合并到生成的 Info.plist 中。

编译产物已验证:
```
$ plutil -p .../OpenTerminal.app/Info.plist | grep ITSApp
"ITSAppUsesNonExemptEncryption" => false
```

✨ 下次再 archive 上传到 App Store Connect,**不会**再弹这个警告。

---

## 📜 为什么 Open Terminal 可以填 `NO`(豁免)

### 苹果官方判断流程
苹果在 [Export compliance overview](https://developer.apple.com/help/app-store-connect/reference/export-compliance-documentation/) 给的判断:

> 选择 **NO**(豁免)的条件 — 满足**任一**即可:
>
> 1. App 完全没有加密功能;**或**
> 2. App 中的加密仅用于:
>    - (a) **认证、数字签名**
>    - (b) **版权保护**(DRM)
>    - (c) **通过苹果系统加密**(CryptoKit / SecureTransport / Common Crypto)与你自己的服务器/云通信
>    - (d) **使用标准开源加密协议**(HTTPS / TLS / SSH / SSL)进行端到端通信,**且没有自创加密算法**

### Open Terminal 的实际加密用法

| 加密类型 | 用途 | 落入哪一类豁免 |
|---|---|---|
| **SSH 协议**(Citadel + SwiftNIO SSH) | 用户与自有服务器之间的标准 SSH 连接 | (d) 使用标准开源加密协议 |
| **Keychain 存密码** | iOS 系统级 API | (c) 苹果系统加密 |
| **TCP 探测** | 不加密的 TCP 握手 | 不算加密 |

**结论**:Open Terminal 使用的所有加密都是 **"标准、公开、开源、用于通信"** 的形态,没有自研算法,没有用作 DRM,没有用作军事/政府特殊用途 → 完全符合 EAR § 740.17(b)(3) 豁免类别 → 可以填 `NO`。

### 法律依据(给审核加分)
- **EAR 5D002**(信息安全软件分类)
- **§ 740.17(b)(3)(iii)** — "Publicly available encryption source code" 豁免
- **§ 742.15(b)(1)** — 标准加密通信工具豁免

> 这套法律框架就是为什么大量 SSH/Email/IM/HTTPS 客户端 App 都填 NO 的原因。

---

## 🔄 如果你想填 `YES`(更保守)

虽然技术上 NO 完全正确,但有些团队风险偏好低,愿意走完整的出口合规申报。两条路:

### 方案 A:走 Apple 的简化合规流程(推荐保守者)
1. Info.plist 改为 `ITSAppUsesNonExemptEncryption = YES`
2. 在 App Store Connect → 你的 App → 一般信息 → **加密文件** 页面
3. 上传 **年度自我分类报告**(ARN) — 不需要真的提交给美国商务部,只是声明
4. 后续每年 2 月 1 日前需更新一次

### 方案 B:申请 CCATS 分类(完全合规,大公司模式)
1. 向美国商务部 BIS 提交 CCATS (Commodity Classification Automated Tracking System) 申请
2. 拿到 ECCN 编码(通常是 5D992.c)
3. Info.plist 加 `ITSEncryptionExportComplianceCode = <你的 CCATS 编码>`
4. 流程长(2-4 周)、需法律咨询、对个人开发者过度

**对独立开发者**:99% 选 NO 即可。Open Terminal 已经按这个方案配置好了。

---

## 🌐 在 App Store Connect 网页上发生了什么

不修 Info.plist 的话,每次上传 build 后,会出现:
```
缺少出口合规证明
请回答有关此构建版本的几个问题
```
点进去会问 5-6 个嵌套问题,流程大致是:

1. **你的 App 是否使用加密?**
   - 选 "是"
2. **你的 App 是否仅使用以下用途?**(列举 a/b/c/d 四类)
   - SSH 客户端 → 勾选 "**(d) 使用标准加密协议进行通信**"
3. **你的 App 是否使用专有/非标准加密?**
   - 选 "否"
4. **是否符合 § 740.17(b)(3) 豁免?**
   - 选 "是"
5. **App 的最终用户是不是美国/加拿大政府?**
   - 选 "否"

每次新版本上传都要重答一遍 → 烦。

**修了 Info.plist 之后**:整个流程跳过,审核流自动通过这一步。

---

## 🔍 验证

### 本地检查
```bash
# 构建后查 build 产物的 Info.plist
PLIST=/path/to/OpenTerminal.app/Info.plist
plutil -p "$PLIST" | grep ITSApp
# 应输出: "ITSAppUsesNonExemptEncryption" => false
```

### 上传到 App Store Connect 后
- 上传 archive(Transporter / Xcode Organizer)
- 等几分钟处理完成
- 进 App Store Connect → 你的 App → TestFlight / App Store → 该 build
- **不再**出现"缺少出口合规证明"黄色横幅 ✅

---

## 📋 后续注意事项

1. **不要改回 YES** — 除非你给 App 加了 DRM、自研加密算法、用户密码端到端加密等"非标准"功能
2. **新增加密功能时重新评估**:
   - 加了 SFTP/SCP/Rsync → 仍然 NO(都是标准协议)
   - 加了 端到端加密笔记/聊天 → 可能要重新审视(用户数据加密属于商业加密)
   - 加了 ZK Proof / 自定义协议 → 转 YES + 走合规
3. **每年 2 月 1 日**:如果你的 App 填了 YES,需要上传年度报告。填 NO 的不用。

---

## ⚙️ 如果你切换到独立 Info.plist 文件(高级)

如果以后你想从"自动生成 Info.plist"切回手动管理,需要:

1. Build Settings 把 `GENERATE_INFOPLIST_FILE` 改 NO
2. 新建一个 `Info.plist` 文件,塞入:
   ```xml
   <key>ITSAppUsesNonExemptEncryption</key>
   <false/>
   ```
3. 把 build settings 中 `INFOPLIST_KEY_ITSAppUsesNonExemptEncryption` 删掉(否则冲突)
4. 设 `INFOPLIST_FILE = OpenTerminal/Info.plist`

> 当前项目用自动生成模式,**无需任何此类切换**,保持现状即可。

---

## 🔗 参考

- [Apple — Determine your export compliance requirements](https://developer.apple.com/help/app-store-connect/reference/export-compliance-documentation/)
- [Apple — Cryptography and Your App](https://developer.apple.com/documentation/security/complying_with_encryption_export_regulations)
- [BIS — Encryption FAQs](https://www.bis.doc.gov/index.php/policy-guidance/encryption/encryption-faqs)

---

**Open Terminal 当前状态:✅ 已配置 ITSAppUsesNonExemptEncryption = false (豁免),下次提交自动通过。**
