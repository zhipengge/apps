# 家庭影音服务器搭建详细需求（牧云音乐）

> 这是 App 内「设置 → 家庭影音配置 → 家庭影音服务器搭建方案」的完整版。
> 目标：在**自己的家庭局域网**里跑一个很小的 HTTP 网关，让牧云音乐搜索、播放、
> 按需缓存 NAS 上的音乐；不做公网服务、不做账号体系、不做第三方曲库聚合。
>
> 当前 App 内可点击的在线版本：
> <https://github.com/zhipengge/apps/blob/main/muyunmusic/NAS-DEPLOY.md>

---

## 0. 先确认边界

适合：

- 音乐文件在**自己的 NAS** 上，手机与 NAS 在同一个局域网；
- 想用手机播放 NAS 上的无损/高品质文件，并保留本地缓存、歌词、封面；
- 接受「只在家里用」，不需要在外网访问。

不适合：

- 想把它暴露到公网、给朋友开账号、做多租户；
- 想让网关替你抓第三方平台曲库；
- 想用它替代 NAS 自带的媒体服务器（Jellyfin/Plex 等）。

网关只做四件事：**索引本地目录、统一搜索、按文件返回直链/Range、可选转发分享**。
它不是内容服务，也不保存任何平台账号。

---

## 1. 硬件与系统要求

| 项 | 最低 | 建议 |
|---|---|---|
| 设备 | 群晖/威联通/绿联/极空间等 NAS，或一台常开的小主机 | 有线连接的 NAS |
| CPU | x86_64 或 ARM64，1 核 | 2 核 |
| 内存 | 512 MB 可用 | 1 GB 以上 |
| 音乐存储 | 按曲库实际大小 | 独立卷；预留 10% 空间 |
| 数据目录 | 100 MB | 1 GB（索引、分享文件、缓存） |
| 系统 | 支持 Docker 20.10+ / Compose v2 的 Linux NAS | 官方最新固件 |
| 可选 | Python 3.11+（直接跑源码时） | — |

网关本身很小；真正占资源的是**音乐文件和封面解码**，不是搜索进程。

### 必须装好

- `ffprobe`（读时长/码率/标签；部分媒体元数据依赖它）
- `ffmpeg`（可选；需要生成占位/转码时）
- `curl`（部署验收）
- Docker + Docker Compose（推荐），或按发行包说明直接运行二进制

> 镜像名 / 二进制名以实际发行包为准。本文用 `<gateway-image>` 和
> `muyun-gateway` 作为占位，不要原样当成已发布镜像。

---

## 2. 网络要求

1. **固定地址**：给 NAS 设静态 IP，或在路由器做 DHCP 地址保留。
   App 里保存的是完整地址（如 `http://192.168.31.6:8080`），IP 变了就要改设置。
2. **端口**：默认 `8080/tcp`。被占用时换一个，App 地址同步改。
3. **只开局域网**：防火墙只允许家庭网段（如 `192.168.31.0/24`）。
4. **不要做**：路由器端口映射、UPnP、公网 DDNS、反向代理到公网。
   网关**没有鉴权**，这是家庭内网工具的前提。
5. **不需要 HTTPS**：App 对用户自填地址允许 http（ATS 例外仅为此设置）；
   局域网内不做证书。
6. 手机与 NAS 不要跨 VLAN/访客网络；如果必须跨，先放行对应网段。

验收：

```bash
curl -s http://<NAS-IP>:8080/api/v1/status
```

应返回 JSON，且 `ok` 为 `true`；有 `gatewayVersion` 更好。

---

## 3. 存储与目录要求

### 3.1 两个目录

| 挂载 | 权限 | 用途 |
|---|---|---|
| `/music` | **只读** | 音乐、歌词、封面；网关只读不写 |
| `/data` | 可写 | 索引、分享文件、临时文件；不要和音乐目录混在一起 |

不要把 `/music` 挂成可写：网关不需要改你的音乐文件，只读能避免误删/误改。

### 3.2 推荐布局

```text
/volume1/music/
├── 专辑或歌手目录/
│   ├── 01.flac              ← 音频
│   ├── 01.lrc               ← 同名歌词（可选；优先于内嵌）
│   ├── cover.jpg            ← 同名封面（可选；内嵌封面优先）
│   └── 02.mp3
└── ...
```

约定：

- 歌词文件与音频**同名同目录**，扩展名 `.lrc`；
- 封面优先读音频内嵌图，其次同目录 `cover.jpg` / `folder.jpg`；
- 文件名建议 `01 - 歌名.flac`；支持中文/空格，但避免 `? * : " < > |` 等字符；
- 目录层级不限；网关负责递归索引；
- 曲库很大时首次索引会慢，属正常；索引完成后搜索应立即返回。

### 3.3 容量

- 1000 首无损约 25–35 GB；索引与封面缓存通常几百 MB；
- 分享文件落 `/data/shared/`，和自有曲库隔离；定期清理不需要的分享；
- 音乐请自行做 NAS 快照/备份；网关不是备份工具。

### 3.4 权限

- 容器默认以镜像内用户运行；如 NAS 的共享目录要求 UID/GID，按发行包说明设置
  `PUID` / `PGID`（没有该变量就保持默认）。
- 确保 `/data` 对运行用户可写；`/music` 至少可读 + 可进入目录。
- 不要用 root 跑长期服务。

---

## 4. 部署

### 4.1 Docker Compose（推荐）

在 NAS 上新建 `docker-compose.yml`：

```yaml
services:
  muyun-gateway:
    image: <gateway-image>:1.2.0   # 换成你的发行镜像
    container_name: muyun-gateway
    restart: unless-stopped
    ports:
      - "8080:8080"
    volumes:
      - /volume1/music:/music:ro
      - /volume1/docker/muyun-gateway:/data
    environment:
      TZ: Asia/Shanghai
      MUSIC_ROOT: /music
      DATA_DIR: /data
    healthcheck:
      test: ["CMD", "curl", "-fsS", "http://127.0.0.1:8080/api/v1/status"]
      interval: 30s
      timeout: 5s
      retries: 3
```

启动与检查：

```bash
docker compose up -d
docker compose ps
docker compose logs -f --tail=100
```

首次启动会索引 `/music`；索引完成前搜索可能为空。

### 4.2 二进制 / 常驻进程

按发行包解压后：

```bash
./muyun-gateway --root /volume1/music \
                --data /volume1/docker/muyun-gateway \
                --port 8080
```

建议用 NAS 的「任务计划/开机启动」或 systemd 托管，退出自动重启。
如果直接跑 Python 源码，按源码仓库 README 的启动命令；依赖 Python 3.11+。

### 4.3 群晖 / 威联通要点

- 在套件中心安装 Docker / Container Manager；
- 把音乐共享目录映射到 `/music`，**只读**；
- 给容器单独的数据目录映射到 `/data`；
- 防火墙只放行家庭网段到 `8080`；
- 不要把容器加入公网反向代理；
- 若 NAS 有多个网口，确认手机走的是同一个网段。

---

## 5. App 端连接

1. 牧云音乐 → **设置 → 家庭影音配置 → 音乐服务器**；
2. 填 `http://<NAS-IP>:8080`（带不带尾斜杠都可；带路径前缀也行，App 按相对路径解析）；
3. 点 **测试连接**：
   - 绿「连接成功」→ 网关在线；
   - 红字按下方排错表判断；
4. 回搜索页，输入关键词，「在线结果」区出现；
5. 点某条结果：在线播放 / 下载到曲库；播放页支持拖动进度（依赖服务端 Range）；
6. 需要分享时，点播放页分享键（网关 1.2.0+ 才有分享端点）。

留空地址 = **完全本地模式**：在线搜索区、分享区隐藏，App 不发任何外部请求。

---

## 6. 接口契约

App 只按下面这些端点工作。**所有媒体 URL 必须同源**：
相对路径，或与配置地址**同 host、同 port** 的绝对 http(s) 地址；其他主机的
URL 会被 App 丢弃并计数，平台域名还会被红线名单再拦一次。

### 6.1 `GET /api/v1/status`

```json
{ "ok": true, "gatewayVersion": "1.2.0" }
```

- `gatewayVersion` 可选；没有版本但 `ok:true` 也算自家网关（现役网关兼容）；
- 200 但既无 `gatewayVersion` 也无 `ok:true`：App 判「端口上是别的服务」；
- 非 JSON：判响应不合规。

### 6.2 `GET /api/v1/search?q=<关键词>&limit=<n>`

```json
{
  "format": "muYunSearch/1",
  "results": [
    {
      "id": "local-0001",
      "title": "冬日之光",
      "artist": "Minimax",
      "album": "冬日之光",
      "duration": 202,
      "playUrl": "/media/%E5%86%AC%E6%97%A5%E4%B9%8B%E5%85%89.flac",
      "download": "/media/%E5%86%AC%E6%97%A5%E4%B9%8B%E5%85%89.flac",
      "cover": "/media/cover.jpg",
      "lyricsUrl": "/media/%E5%86%AC%E6%97%A5%E4%B9%8B%E5%85%89.lrc",
      "source": "local"
    }
  ]
}
```

字段规则：

| 字段 | 必填 | 说明 |
|---|---|---|
| `format` | 是 | 固定 `muYunSearch/1` |
| `results` | 是 | 数组；空数组合法 |
| `playUrl` / `url` | 是（二选一） | 播放地址；同源 |
| `download` | 否 | 下载直链；缺省 = `playUrl` |
| `title` | 否 | 缺失时 App 用 id/URL 回显 |
| `artist` / `album` | 否 | 展示用 |
| `duration` | 否 | 秒；数字或数字字符串都接受 |
| `cover` | 否 | 同源封面；懒加载 |
| `lyricsUrl` | 否 | 同源 LRC；懒加载 |
| `source` | 否 | 展示用来源标签 |

一条没有有效 `playUrl` 的记录会被计入 `dropped`，不会让整个响应失败。

### 6.3 `GET /api/v1/manifest`

供「按 URL 导入」整单导入，固定 schema：

```json
{
  "schema": "muYunImport/1",
  "tracks": [
    {
      "url": "http://192.168.31.6:8080/media/a.flac",
      "title": "歌名",
      "artist": "歌手",
      "album": "专辑",
      "duration": 202,
      "cover": "http://192.168.31.6:8080/media/a.jpg",
      "tags": ["flac", "16bit"]
    }
  ]
}
```

- `schema` 必须是 `muYunImport/1`；更高 major 整单拒绝；
- `tracks` 必须是非空数组；
- 条目级失败只跳过该条，不拖垮整单；
- 平台域名条目会被拒收（与搜索同一红线）。

### 6.4 `GET /media/<path>`

- 返回音乐/歌词/封面文件本体；
- **必须支持 `Range`**（请求头 `Range: bytes=0-`），返回 `206 Partial Content`、
  `Content-Range`、`Accept-Ranges: bytes`；
- 不支持 Range 也能播，但拖动进度会回退/卡顿；
- 正确设置 `Content-Type`、`Content-Length`；
- 路径穿越防护（拒绝 `..`、绝对路径逃逸）；
- 同源；不要 302 到第三方 CDN。

### 6.5 `GET /relay/<meting>`

- 可选：把上游音源代理成**本网关域名下**的二进制流；
- App 只认同源地址；上游平台地址不能直接交给 App；
- 支持 Range 更好；上游失败时返回错误，不要返回 30 秒静音/截断文件冒充成功；
- 网关不得把第三方平台账号暴露给 App。

### 6.6 `POST /api/v1/share`（网关 1.2.0+）

两种请求：

**本地曲：multipart**

- 文件字段：音频文件本体；
- 文本字段：`kind=file`、`title`、`artist`、`duration`、`from`；
- 服务端落 `/data/shared/`，返回 201 JSON（含 id/可播放地址）。

**网络曲：JSON**

```json
{ "kind": "url", "url": "http://<同源>/relay/...", "title": "歌名", "artist": "歌手", "from": "昵称" }
```

- `url` 必须同源；App 在发出前已过红线名单；
- 服务端不要把这个 URL 再交给第三方平台去抓。

### 6.7 `GET /api/v1/shared`（网关 1.2.0+）

```json
{
  "format": "muYunShared/1",
  "items": [
    {
      "id": "share-0001",
      "title": "歌名",
      "artist": "歌手",
      "duration": 202,
      "playUrl": "/media/shared/share-0001.flac",
      "cover": "/media/shared/share-0001.jpg",
      "from": "分享人昵称",
      "sharedAt": 1732000000
    }
  ]
}
```

- `sharedAt`：epoch 秒（也接受 ISO8601 字符串）；
- `playUrl` / `cover` 同源；
- 旧网关没有这两个分享端点时：测试连接仍绿、搜索仍可用，只有分享提示
  「暂不在服务范围内」——这是设计好的降级。

---

## 7. 验收清单

在 NAS 同网段的电脑上：

```bash
# 1. 状态
curl -s http://<NAS-IP>:8080/api/v1/status

# 2. 搜索（看 format/results）
curl -sG 'http://<NAS-IP>:8080/api/v1/search' \
  --data-urlencode 'q=冬日' --data 'limit=5'

# 3. Range（应看到 206 + Content-Range）
curl -sI -H 'Range: bytes=0-1023' \
  'http://<NAS-IP>:8080/media/<path>'

# 4. 分享列表（1.2.0+）
curl -s http://<NAS-IP>:8080/api/v1/shared
```

App 侧：

- [ ] 设置填地址 → 测试连接绿
- [ ] 搜索出「在线结果」
- [ ] 点结果能播放，进度条时间前进
- [ ] 拖动进度条能跳转（Range 生效）
- [ ] 封面/歌词能显示（或明确「无歌词」而不报错）
- [ ] 收藏后缓存清理不删该曲
- [ ] 分享键可用（1.2.0+），分享列出现
- [ ] 路由器上没有该端口的公网映射

---

## 8. 排错

| 现象 | 多半是什么 | 怎么办 |
|---|---|---|
| 测试连接红：不可达 | 地址/端口错、网关没起、防火墙 | 同网段另一台机器 curl `/api/v1/status` |
| 测试连接红：响应非 JSON | 端口被别的服务占了（返回 HTML） | 换端口或停掉抢占服务 |
| 测试连接红：没有版本且非 ok | 端口上是个像 JSON 的别的服务 | 确认网关版本/换端口 |
| 搜索 0 结果但连接绿 | 网关没索引到文件 | 查 `/music` 挂载、索引日志、权限 |
| 播放 45 秒截断 / 30 秒静音 | 网关上游拉取失败留下的占位文件 | 这是服务端行为；重拉该曲，修上游 |
| 某条歌词「无歌词」 | `/relay` 歌词上游失败 | 静默降级是设计；不影响播放 |
| 换 Wi-Fi / NAS 换 IP 后全红 | 地址里还是旧 IP | 设置页更新地址再测 |
| 分享提示「暂不在服务范围」但连接绿 | 网关低于 1.2.0 | 升级到 1.2.0+ |
| 拖动进度卡住 | `/media` 不支持 Range | 服务端补 Range / 206 |
| 封面/歌词 404 | 同源路径错 / 文件不存在 | 查路径与 MIME；App 会静默无封面/无歌词 |

---

## 9. 安全与隐私

- 网关**没有鉴权**，只放局域网；不要暴露公网；
- 不配置任何第三方平台账号；不把平台曲库聚合进搜索；
- App 不自动发现设备、不后台探测；所有请求都由用户动作触发；
- 服务器地址留空时，在线功能区整块隐藏，运行时零外部请求；
- `/music` 只读挂载，防止网关误改文件；
- 分享文件落 `/data/shared/`，与自有曲库隔离；定期清理；
- 备份 `/data`（索引/分享）即可；音乐本身按 NAS 既有策略备份。

---

## 10. 升级与备份

- 升级：替换镜像 tag / 二进制 → 重启容器；`/api/v1/status` 的
  `gatewayVersion` 可用于确认版本；
- 备份：`/data`（索引、分享文件、配置）；`/music` 不需要网关备份；
- 回滚：保留上一版镜像 tag；数据目录向后兼容；
- 迁移：新 NAS 上恢复 `/data`，重新映射 `/music`，更新 App 地址。

---

## 11. 一页速查

```text
NAS 固定 IP  ──  防火墙只放行 LAN:8080
/music 只读  ──  递归索引 flac/mp3/... + .lrc + cover
/data 可写   ──  索引、分享、临时文件
网关          ──  /api/v1/status /search /manifest /media /relay /share /shared
App           ──  设置填 http://IP:8080 → 测试连接 → 搜索 → 播放/下载
安全          ──  不公网、不账号、不聚合平台、不自动发现
```

---

*本文与 App 内「家庭影音服务器搭建方案」同源；接口字段以 App 实际解析代码为准。*
