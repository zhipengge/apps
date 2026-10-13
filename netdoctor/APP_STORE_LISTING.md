# 牧云网络医生 (NetDoctor) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。

---

## 0. 创建 App Record

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **macOS** | iOS |
| 名称（主语言：简体中文） | **牧云网络医生** | 网络医生、NetDoctor 牧云（通称易被占） |
| 名称（English 本地化） | **NetDoctor** | Muyun NetDoctor |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.NetDoctor` | 任何旧 ID |
| SKU | `netdoctor-20261011` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

Bundle ID、显示名、SKU、历史存储 key 都已写在 `Shared/SharedConstants.swift` 里，与本表一致。
**这几处必须同时改**，逻辑测试第 16 组守着它们，改错了测试会先红。

设备显示名（`CFBundleDisplayName`）为「牧云网络医生」，已用 `plutil` 在构建产物上核对过
（`LSUIElement = 1`、Bundle ID、显示名、沙盒四项都验过）。
`LSApplicationCategoryType` 为 `public.app-category.utilities`。
`ITSAppUsesNonExemptEncryption = NO`。

### 命名红线（作者在 `AGENTS.md` 里写死的，务必遵守）

**商店名、副标题、关键词里绝对不能出现 `Finder` `Mac` `macOS` `iPhone` `iOS` `Apple`**
（Guideline 5.2.5，Apple 商标）。逻辑测试第 16 组逐个词守着这条。
本文件下面每一段名称、副标题、关键词都已经过一遍这条检查。

**「macOS 13.0 或更高版本」这句只出现在描述正文的系统要求一节里**，那是兼容性说明，
是这个字段本来的用途；名称、副标题、关键词里一个字都没有。

**探测目标里有一个域名带 Apple 商标词，描述里刻意没有写出来。** 描述里用的是
「一个公开的强制门户探测域名」这种说法。完整清单在源码里，任何人都可以核对。

**注意：App 没有任何本地化。** 工程 `developmentRegion` 是 `zh-Hans`，界面文案全是中文硬编码。
如果给 English 也建一份商店本地化，英文用户看到的是「英文描述 + 中文界面」。
要么这轮只上简体中文（主要语言就是它），要么等界面做完英文化再补 English 本地化。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
常驻菜单栏的网络诊断。一键分层排查物理连接、网关、DNS、公网出口、关键节点，明确告诉你断在哪一层。只读，不改你的任何系统网络设置，也不向任何服务器回传数据。报告可以直接发给别人。
```

**字符数：90 / 170**

### English

```
A menu bar network diagnostic that names the broken layer: link, gateway, DNS, internet, key nodes. Read-only, never changes settings. Nothing goes to any server.
```

**字符数：162 / 170**（只剩 8，改写时留意）

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
牧云网络医生是一个常驻菜单栏的网络诊断工具。它随时显示一个延迟数字，一键分层排查，明确告诉你这次到底断在哪一层，并导出一份能直接发给别人的报告。

【只诊断，不修改】
它不会改你的代理、DNS、路由或任何系统网络设置。这不是一句承诺，是结构性的：整个工程里不允许出现任何写系统网络配置的 API，连「顺手帮你改一下」的入口都不存在。这条由一个脚本机械检查，在全部源文件里搜 23 个写入型 API，再反查所有系统网络配置调用是否都在 9 个只读接口的名单里，每次跑测试都会执行。你装的是一个只看不动的工具。

【分五层，因为「网断了」这三个字对排查没有用】
物理连接：网卡拿到地址了吗，还是只有那种表示没拿到地址的自动私有地址。
局域网网关：路由器和本机之间通不通。
DNS 解析：域名能不能解析，以及是你配的 DNS 服务器没答，还是它答了但答错了。
公网出口：不经过 DNS，直连一个公网 IP 通不通。
关键节点：我这边是通的，那是不是只有某个服务不通。

分层之后结论才是具体的。断在网关是 Wi-Fi 或路由器的问题；DNS 层断但公网层通是 DNS 服务器的问题；只有某个关键节点不通而公网层是通的，说明问题不在你这边。这三种情况的处理方式完全不同。

【不冤枉任何一层】
中间路由器经常不回应或限速 ICMP，所以「网关不搭理我」不等于「网关坏了」。如果网关没回 ICMP，但公网直连是通的，网关会被判为「通」并附一句说明。反过来不成立：只有 DNS 通、公网直连不通时，不会因此改判网关。

同一个道理的另一个用法：丢包和延迟只有持续到目标才算数，所以它不测中间跳，只测两端。少了这条推理，你会看到「断在网关」而实际是运营商的问题，那是这个工具最不能犯的错。

【没测和断了是两回事】
层与层之间会截断：物理层不通，后面四层就没有意义，会标成「未检测」而不是「不通」。这两件事必须分开，混在一起会把人引向错误的排查方向。

【ICMP 被屏蔽也能用】
网关那一层会改用 TCP 兜底，ICMP 没回应时再试几个常用端口。连接被拒绝同样证明主机是活的，所以「对方拒绝了我」也会被正确地判成「通」。用的是非特权 ICMP，普通权限即可，不需要管理员，也不装任何后台服务。

【报告是给人看的】
两种形式：一份纯文本文件，几十行，给 IT 或运维；一段排版过的短文本，可以直接发在聊天里。都是给人读的排版，不是给机器解析的日志。

【常驻，但占得很少】
菜单栏那个数字来自每 10 秒一次 TCP 握手，连上就关，应用层一个字节都不发。屏幕休眠时这个刷新会停掉，醒来补一次。探测永远不在主线程，关键节点并发上限 4 个。历史保存最近 50 次，只存轻量记录，不保存完整报告正文。

【它联网，这一点我们直说】
这是个网络诊断工具，它必须碰网络。对外只有三种动作，全部是只读的：DNS 查询、TCP 连接（发个 SYN 就关，不带任何业务数据）、ping。它没有 HTTP 客户端，不下载任何网页，不上传任何东西，也没有我们的服务器。探测不带账号、不带设备标识符、不带任何业务数据。

被探测的地址只有几类：你自己的网关和你系统里配置的 DNS 服务器（从你的网络配置里读出来，不是写死的）、两个公开的公共 DNS 服务地址、一个公开的强制门户探测域名、四个公开的服务域名。完整的清单写在源码里，任何人都可以核对，里面没有任何一个属于开发者。

【权限】
不申请任何系统权限，系统不会为它弹出授权框。沙盒授权一共只有两条：沙盒本身，和出站网络。不写文件（导出走系统的保存面板）、不读你的用户目录、不要完全磁盘访问、没有 App Group。不需要辅助功能，也不需要输入监控。

【系统要求】
需要 macOS 13.0 或更高版本。菜单栏应用，不占 Dock 图标。
```

**字符数：1587 / 4000**

### English

```
NetDoctor is a network diagnostic tool that lives in the menu bar. It shows a latency figure at all times, works out in one action which layer is broken, and exports a report you can send to someone directly.

[It diagnoses and never modifies]
It will not change your proxy, DNS, routes or any other system network setting. That is structural, not a promise: the project permits no API that writes system network configuration, and there is no entry point for quietly fixing something on your behalf. A script enforces this on every test run, searching every source file for 23 write-type APIs and verifying that each configuration call is one of nine read-only functions.

[Five layers, because "the network is down" does not tell you what to do]
Physical link: does the interface have a real address, or only the automatic one.
Local gateway: is the router reachable from this machine.
DNS resolution: does the name resolve, and if not, did your DNS server stay silent or answer wrongly.
Public internet: connecting straight to a public IP without DNS, does that work.
Key nodes: my side is fine, so is it one particular service that is down.

A break at the gateway is a Wi-Fi or router problem, a break at DNS while the public layer works points at the DNS servers, and a single key node failing while the public layer works means the fault is not on your side. Those three call for completely different responses.

[It does not wrongly blame a layer]
Intermediate routers often ignore or rate-limit ICMP, so a gateway ignoring you is not a broken gateway. If the gateway does not answer ICMP but the direct public connection works, it is reported as healthy with a note. Packet loss and latency only count if they persist all the way to the target, so it probes the two ends and not the hops in between.

[Not tested and broken are different things]
If the physical link is down, the four layers after it are meaningless and are marked not tested rather than failed.

[It still works when ICMP is blocked]
The gateway layer falls back to TCP, trying a few common ports when ICMP gets no answer. A refused connection also proves the host is alive, so being rejected is still reported as reachable. ICMP is used unprivileged: no administrator rights and no background service.

[The report is for people]
Two forms: a few dozen lines of plain text for IT or operations, and a short formatted block to paste into a chat.

[Always on, using very little]
The menu bar figure comes from one TCP handshake every ten seconds, closed as soon as it connects, sending no application-layer bytes. The refresh stops while the screen sleeps and catches up on wake. Probes never run on the main thread, and key-node concurrency is capped at four. History keeps the last 50 runs as summaries, not full report text.

[It goes online, and we say so plainly]
This is a network diagnostic tool, so it has to touch the network. It has exactly three outbound actions, all read-only: a DNS query, a TCP connection (send a SYN and close, carrying no application data), and a ping. It contains no HTTP client, downloads no pages, and has no server of ours. Probes carry no account, no device identifier and no application data.

Targets are your own gateway and your configured DNS servers, read out of your network configuration rather than hard-coded, two public DNS addresses, one captive-portal detection domain and four public service domains. The full list is in the source where anyone can check it, and none of it belongs to the developer.

[Permissions]
No system permissions are requested, so the system never prompts you. The sandbox declares exactly two things: the sandbox itself and outbound networking. No file writes (export goes through a system save panel), no home folder access, no Full Disk Access, no App Group, no Accessibility, no Input Monitoring.

[Requirements]
macOS 13.0 or later. A menu bar app with no Dock icon.
```

**字符数：3923 / 4000**（只剩 77，改写时留意）

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名，也不要出现上面那条命名红线里的词。

### 简体中文

```
一眼看出网络断在哪一层
```

**字符数：11 / 30**

### English

```
See which network layer broke
```

**字符数：29 / 30**（只剩 1，改写时留意）

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名，不要出现命名红线里的词。

### 简体中文

```
网络,诊断,ping,dns,延迟,连通性,运维,wifi,测速,排查,菜单栏
```

**字符数：39 / 100**

### English

```
network,diagnostics,ping,dns,latency,connectivity,devops,troubleshooting,menubar
```

**字符数：80 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/netdoctor/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/netdoctor/privacy.html` |
| 营销 URL | 留空 |

**这两个 URL 已经写在 `Shared/SharedConstants.swift` 里**
（`privacyURL` / `supportURL`），App 的「关于」页读的就是它们。
**两边必须一致**：改这里就要同时改代码里那两个常量。
逻辑测试第 16 组只校验它们是非空的 https 地址，**校验不了「两边是否一致」**，那一步只能靠人。

技术支持是**版本级**字段（改它要跟新版本一起提审），隐私政策是 **App 级**（要有待发版本才能改）。

营销 URL 是可选字段，`apps/netdoctor/` 下没有 `index.html`，填了就是 404，所以留空。

**这两个页面现在还不存在。** `apps/` 是独立仓库 `zhipengge/apps`，Pages 已经开着
（`apps/skystrike/privacy.html` 现在返回 200），但 `apps/netdoctor/` 这个目录还没提交。
提审前必须先提交并推送这一整个目录，否则 App Store Connect 填的隐私政策链接是空的，
App 里「关于」页点开也是 404。

---

## 6. 类别、评级、隐私问卷

### 类别

主要类别填 **工具 / Utilities**，与工程里的
`LSApplicationCategoryType = public.app-category.utilities` 一致。
次要类别可以留空；如果要填，**开发者工具**比**效率**更贴——它真正的受众是运维和后端，
但开发者工具的曝光面更窄，放次要位置合适。

### 年龄分级（需要你定）

问卷不让你直接选档位，是按题作答后由 Connect 判定。这个 App 的实际内容：
是本机网络工具，没有暴力、恐怖、赌博、酒精烟草毒品、色情、脏话、用户生成内容、聊天、广告、内购。
唯一可能被问到的是「无限制网页访问」这类题：本 App **不含浏览器**，也不渲染任何网页，
应作答为否。

按上述事实作答，大概率落在 4+。

### 其余表

| 字段 | 建议 |
|---|---|
| 内购 | **无**。没有 StoreKit 代码，也没有账号系统 |
| App 隐私 | **不收集数据**。已有一份 `PrivacyInfo.xcprivacy` 声明：不追踪、追踪域名为空、收集的数据类型为空、只用 UserDefaults 的 `CA92.1` 理由。**这份清单是用 `_tools/gen_privacy_manifest.py` 生成的，不要手写** |
| 出口合规 | **NO**。`ITSAppUsesNonExemptEncryption = NO` 已写在工程里。App 不做任何加密、哈希或密钥运算，它本身也不发起 HTTPS 连接 |
| 辅助功能 / 输入监控 | **不申请**。面板里的按键都是普通界面按键，没有全局快捷键 |
| 通知 | **不申请** |
| 完全磁盘访问 | **不申请**，只读系统网络配置不需要它 |

审核备注建议写清：本 App 是菜单栏应用，`LSUIElement` 为真，没有 Dock 图标。
它对外只有三种只读动作：DNS 查询（UDP 53）、TCP 连接（握手后立即关闭，应用层不发送任何字节）、
ICMP 回声（非特权模式，不需要管理员权限）。被探测的地址只有用户自己的网关与 DNS 服务器，
以及若干公开可访问的公共服务地址。**App 不修改任何系统网络设置**，工程里不允许出现写类型的
网络配置 API，有一条脚本每次跑测试都会机械检查（23 个写入型 API 黑名单 + 9 个只读接口白名单反查）。
App 不申请任何系统权限，不含账号、统计、广告或崩溃上报。

---

## 7. 截图

macOS App 的商店截图规格与 iOS 不同：**1280 x 800**（或 2560 x 1600 等 16:10 档位）。

**本轮没有产出截图，截图由另一路做。** 这个目录下现在没有 `screenshots/`。

`Scripts/screenshots.sh` 能在本机生成对照图（它用 `screencapture -l <窗口号>` 抓窗口本体，
不是全屏裁切），历史页那张带 `--reset-history`，每次都是同样的演示数据。
按商店规格导出到 `apps/netdoctor/screenshots/` 这一步还没做。

截图内容建议（都对应界面上真实存在的东西，不要做纯海报式截图）：

| 建议标题 | 副标题 | 对应界面 |
|---|---|---|
| 断在哪一层，一眼看到 | 五层逐层给结论，不是笼统的「网断了」 | 诊断页的五层结论卡与状态徽章 |
| 网关不搭理我，不等于它坏了 | 公网直连同时是通的，网关就判通并附说明 | 网关层那条带说明的结论 |
| 没测和断了是两回事 | 物理层不通，后面四层标「未检测」而不是「不通」 | 层间截断时的诊断页 |
| 报告是给人看的 | 一份纯文本给 IT，一段短文本发聊天 | 导出后的报告预览与状态卡 |
| 常驻菜单栏，占得很少 | 10 秒一次握手，屏幕休眠就停 | 菜单栏上的彩色圆点与延迟数字 |

空状态、纯海报式截图会被拒。**注意：真实的断网场景没有人手工验过**（见第 9 节），
前两张建议截图涉及「异常结论」的界面，拍之前先自己造一次真实断网看一眼。

---

## 8. 交付前必须注意的

| 项 | 现状 | 说明 |
|---|---|---|
| **真实断网场景没人工验过** | 拔网线、关 Wi-Fi、路由器断电、信号差的地方——这四种情况下五层的结论是否都说得通，**没有手工走过**。现有结论全部来自网络正常时的几次真跑 | 这是交付前最该补的一件事。截图若涉及异常状态，先自己造一次 |
| **右键菜单和 Esc 关面板没有自动化核对** | 需要辅助功能授权，本 App 刻意不申请 | 人工点一遍即可，不要为此加权限 |
| **长跑内存曲线没有数据** | 菜单栏应用连着跑一周的表现是这类应用的老问题 | 上架前如果有条件，挂一周看看 |
| **`get-task-allow`** | 签名用 Apple Development 身份时，开发 profile 会注入这个 key | 走 App Store 归档时由分发 profile 去掉 |
| **测试规模** | 逻辑测试 245 项全过（17 组，含 DNS 报文级测试与只读检查）；Debug 构建成功，产物已用 `plutil` 验证 `LSUIElement` / Bundle ID / 显示名 / 沙盒 | 这是「验过了」的部分，可以放心引用 |

---

## 9. 差异化：能用什么、不能用什么

这一节来自 `NetDoctor/AGENTS.md` 的硬约束、「当前进度」与「待办」。
**下面「不能用」的每一条都是作者自己写下的，照抄即可。**

### 能用的（代码里指得出来）

| 能用的说法 | 依据 |
|---|---|
| 只诊断不修改，且这是**结构性**的而不是承诺 | `Scripts/check-readonly.sh`：20 个源文件里搜 23 个写入型 API 黑名单，再用 9 个只读接口白名单反查所有系统网络配置调用；`LogicTests/run.sh` 每次都跑它 |
| 五层分层，明确给出断在哪一层 | `Shared/DiagnosisEngine.swift` 的纯函数（`DiagnosisInput` → `DiagnosisReport`），判定与探针分离，所以能离线构造场景测试 |
| 不冤枉任何一层（跨层证据优先于单层现象） | `DiagnosisEngine.reconcile` + 测试第 8 组：网关不回 ICMP 但公网通时判「通」；第 8b 组确认反向不成立 |
| 没测 ≠ 断了 | `LayerStatus.skipped` 与 `.fail` 是两个值，`blocksChain` 只对 `.fail` 为真 |
| ICMP 被屏蔽时有 TCP 兜底 | `SharedConstants.gatewayFallbackPorts`；`TCPProbe` 把 RST 也算作主机存活 |
| 用的是非特权 ICMP | `socket(AF_INET, SOCK_DGRAM, IPPROTO_ICMP)`，不用 `SOCK_RAW`，所以不需要管理员权限 |
| 占资源少 | `latencyRefreshInterval = 10` 秒一次的握手、休眠停定时器、`nodeProbeConcurrency = 4`、`historyLimit = 50`、不存完整报告正文 |
| 报告是给人看的 | `ReportFormatter.swift`：完整纯文本报告 + 可直接发聊天窗口的状态卡 |

### 故意没有用的（以及为什么）

| 没有用的说法 | 为什么不用 |
|---|---|
| 「已在各种断网情况下验证」 | 作者原话，待办第一条：「真机手工过一遍：拔网线、关 Wi-Fi、路由器断电、只在信号差的地方待着，看五层结论是否都说得通（**现在的结论都来自「网络正常」这几次真跑**）」。所以描述里一个字都没说「各种断网场景都测过」 |
| 「一键修复」「自动修好」 | 作者原话：「**只诊断，不修改。** 这是产品的第一句话，也是本文件第一条硬约束。」而且工程里连写类型的 API 都不允许出现，根本做不到 |
| 「能看流量 / 能抓包」 | 它没有 HTTP 客户端，只做 DNS 查询、TCP 握手和 ICMP。抓包是另一个工具的事 |
| 「能测丢包率」 | 作者原话：pingbar 的丢包统计「**我们只取一半**，不做独立的丢包统计。TCP 握手测不出丢包率，要做就得发一串 ICMP，对常驻 App 来说不值」。描述里没有出现「丢包」这个卖点 |
| 「能测下载速度」 | App 不下发任何大流量请求，没有测速功能 |
| 「测的延迟比别的工具准」 | 作者说明了**为什么用 TCP 握手而不是 HTTP**（HTTPS 会带上 DNS 与 TLS 两段，数字偏大且抖动），这是方法选择，不是「比别人准」的实测结论。描述里只写事实：握手一次、连上就关 |
| 「自动追踪路由 / 显示每一跳」 | 作者原话：「**我们不测中间跳，只测两端**」。traceroute 被明确排除 |
| 「检测 DNS 劫持」 | 作者原话：dnsdiag 的劫持检测「**没采纳**：判断劫持需要 traceroute，代价和误报都不小。我们只报『服务器活不活、答得对不对』，**劫持交给 IT 去看**」 |
| 「改 DNS / 切代理」 | 明确不做，而且被黑名单挡死。任何「顺手帮用户改一下」的冲动都在检查范围里 |
| 「和系统自带的诊断比更好」 | 没有任何一处做过这个对比，也没有数据 |

### 作者标注「没有验证」的（不要当成已经好了）

来自 `AGENTS.md` 的「待办」：

- **断网场景没人工验过**（待办第一条，也是最重要的一条）。
- **右键菜单和 Esc 关面板没做过自动化核对**，只人工点过。
- **长跑内存曲线没有观察过**（连跑一周）。
- **截图素材还没按商店规格导出**到 `apps/netdoctor/screenshots/`。

所以描述里没有出现「稳定可靠」「经过充分测试」「各种场景都验证过」这类话。
**唯一可以放心放在首位的**是「只诊断，不修改」和「分层给出断在哪一层」这两条：
前者有脚本机械化守着、每次测试都跑，后者是 245 项逻辑测试里覆盖最重的那一块
（17 组里含 DNS 报文级测试与只读检查）。
