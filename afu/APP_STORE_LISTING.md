# 阿福 (Afu) — App Store 发布素材

> 直接复制粘贴到 App Store Connect。中英各一份。
> 不要用装饰线、圆点列表、弯引号、箭头、省略号、破折号，也不要写带双斜杠协议前缀的字面量。

---

## 0. 创建 App Record（必填，按此填写，勿改）

| 字段 | 填什么 | 不要填 |
|---|---|---|
| 平台 | **iOS** | macOS |
| 名称（主语言：简体中文） | **阿福** | AI 助手、本地大模型、聊天助手（通称易被占） |
| 名称（English 本地化） | **Afu** | AI Chat、Local LLM |
| 主要语言 | 简体中文 | — |
| Bundle ID | `com.gezhipeng0201.Afu` | 任何旧 ID |
| SKU | `afu-20261008` | 任何曾提交过的 SKU |
| 用户访问权限 | 完全访问 | — |

设备显示名（`CFBundleDisplayName`）为「阿福」。

备选店名（创建时报名被占再用）：

- 阿福本地助手
- 阿福离线对话
- Afu Local AI

若 `attribute already in use`：先换全新 SKU，再换全新 Bundle ID，最后才换店名。

---

## 1. 推广文本 (Promotional Text)

> 上限 170 字符

### 简体中文

```
模型下载到本机，对话与图片理解全部在设备上完成。不上传聊天内容，不需要账号，断网也能继续聊。
```

**字符数：46 / 170**

### English

```
Models download to your device. Chat and image understanding run entirely on-device. No uploads, no account, works offline.
```

**字符数：123 / 170**

---

## 2. 描述 (Description)

> 上限 4000 字符。修改需提交新版本审核。

### 简体中文

```
阿福是把大模型装进你手机里的对话助手。模型权重下载到本机，推理全部在设备上完成，你的聊天内容不会上传到任何服务器。

【本地推理】
- 模型下载到设备后，断网也能正常对话
- 支持 0.5B 到 4B 等多种参数规模的模型
- 可随时切换模型，对比不同模型的回答
- 支持温度、Top-P、最大回复长度等参数调整
- 可自定义系统提示词

【图片理解】
- 支持多模态模型，可直接对图片提问
- 图片在本机做识别与理解，不会上传

【文件解析】
- 支持 PDF、Word、Excel、CSV、TXT、Markdown
- 文件在本机解析为文本后再交给模型
- 适合长文档摘要与问答

【隐私】
- 没有账号，没有自建服务器
- 不接入广告、分析或追踪服务
- 网络只用于拉取模型清单和下载模型文件
- 对话、图片、文件都不会离开设备

【请注意】
首次使用需要下载模型，建议从 0.5B 到 2B 的小模型开始。参数越大的模型回答质量越高，但更慢、更占内存。
```

**字符数：约 405 / 4000**

### English

```
Afu brings large language models onto your iPhone. Weights download to the device and all inference runs locally, so your conversations never leave it.

[On-device inference]
- Chat works offline once a model is downloaded
- Models from 0.5B up to 4B parameters
- Switch between models and compare their answers
- Adjust temperature, Top-P, and max reply length
- Custom system prompt

[Image understanding]
- Multimodal models answer questions about images
- Images are analysed on-device and never uploaded

[File parsing]
- PDF, Word, Excel, CSV, TXT, Markdown
- Files are parsed locally before the model sees them
- Good for summarising and querying long documents

[Privacy]
- No account, no backend of our own
- No ads, analytics, or tracking
- Network is used only to fetch the model list and download model files
- Conversations, photos, and files never leave the device

[Please note]
You need to download a model on first use. Start with a 0.5B to 2B model. Larger models answer better but are slower and use more memory.
```

**字符数：约 1006 / 4000**

---

## 3. 副标题 (Subtitle)

> 上限 30 字符。不要写 Apple 产品名。

### 简体中文

```
端侧本地大模型助手
```

**字符数：9 / 30**

### English

```
Private on-device AI chat
```

**字符数：25 / 30**

---

## 4. 关键词 (Keywords)

> 上限 100 字符（含逗号）。不要重复 App 名，不要写竞品名。

### 简体中文

```
本地,离线,大模型,对话,图片理解,文件解析,隐私,ai,llm,模型下载
```

**字符数：37 / 100**

### English

```
local,offline,llm,chat,vision,document,private,on-device,model,gguf
```

**字符数：67 / 100**

---

## 5. URL

| 字段 | URL |
|---|---|
| 技术支持 | `https://zhipengge.github.io/apps/afu/support.html` |
| 隐私政策 | `https://zhipengge.github.io/apps/afu/privacy.html` |
| 营销 URL | `https://zhipengge.github.io/apps/afu/` |

---

## 6. 类别、评级、隐私问卷

| 字段 | 建议 |
|---|---|
| 主要类别 | 效率 / Productivity |
| 次要类别 | 工具 / Utilities |
| 年龄分级 | 4+（无不当内容）。用户可撰写任意提示词，但内容不公开、不联网传播 |
| App 隐私 | **不收集数据**。须与 `PRIVACY.md` 一致。注意：模型下载会连接 huggingface.co，但那只是拉取模型文件，不含用户数据，因此仍属「不收集」 |
| 出口合规 | NO（见 `EXPORT_COMPLIANCE.md`） |

审核备注建议写清：本 App 不含任何内置模型，首次使用需联网下载；对话与推理全部在本机完成，聊天内容不上传。网络仅用于拉取模型清单和下载权重。

---

## 7. 截图

成品在 `afu/screenshots/`，已按 App Store 规格导出，可直接上传。

### iPhone 6.9 寸 / 1320x2868

共 4 张，顺序即展示顺序：

- 01-home 把大模型装进手机
- 02-models 多种模型随你选
- 03-download 一键下载到本机
- 04-detail 每款模型都说清代价

### iPad 13 寸 / 2064x2752

共 3 张，顺序即展示顺序：

- 01-home 把大模型装进 iPad
- 02-models 多种模型随你选
- 03-download 一键下载到本机

所有图都用真实界面截图加设备外框与标题，符合 Apple 对截图的真实性要求。

重新生成：

```bash
cd ../            # 回到 apps 目录
python3 tools/compose_all.py afu
```
