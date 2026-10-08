#!/usr/bin/env python3
"""
批量合成 App Store 截图。

素材在 <app>/screenshots/raw*，成品出到 <app>/screenshots/{iphone,ipad,mac}/。

    python3 tools/compose_all.py            # 全部
    python3 tools/compose_all.py afu        # 只做某个 app
"""

import subprocess
import sys
from pathlib import Path

COMPOSE = Path.home() / ".claude/skills/apple-app-screenshots/scripts/compose.py"
ROOT = Path(__file__).resolve().parent.parent

# (app, target, accent, 素材目录, 成品目录, [(素材文件, 输出名, 主标题, 副标题)])
JOBS = [
    # ---------------- iOS：iPhone 6.9" ----------------
    ("afu", "iphone-69", "#6C5CE7", "screenshots/raw-auto", "screenshots/iphone", [
        ("01-home.png",    "01-home",     "把大模型装进手机",   "对话不出设备，断网也能聊"),
        ("03-models2.png", "02-models",   "多种模型随你选",     "0.5B 到 4B，按你的设备挑"),
        ("02-models.png",  "03-download", "一键下载到本机",     "支持断点续传与镜像源"),
        ("04-models3.png", "04-detail",   "每款模型都说清代价", "参数、体积、内存一目了然"),
    ]),
    ("babyrecord", "iphone-69", "#E8739A", "screenshots/raw/iphone", "screenshots/iphone", [
        ("iph1.png", "01-record",   "记录宝宝的每一餐", "喂奶、睡眠、排便，一次点击记下"),
        ("iph2.png", "02-overview", "喂养情况一眼看清", "今天记了多少次、喝了多少毫升"),
        ("iph3.png", "03-trend",    "趋势变化自动成图", "奶量、次数、间隔都能看趋势"),
        ("iph4.png", "04-settings", "多个宝宝，自定义字段", "记录类型随你增减"),
    ]),
    ("gwave", "iphone-69", "#30B0C7", "screenshots/raw-auto", "screenshots/iphone", [
        ("01-player.png", "01-player", "雨声、海浪，按下就有", "内置音效本机合成，不占存储"),
        ("02-list.png",   "02-list",   "自建电台列表",         "手动添加或用链接一键导入"),
        ("03-list2.png",  "03-list2",  "收藏常听的台",         "分组整理，随手可及"),
    ]),
    ("muyuntv", "iphone-69", "#FF3B30", "screenshots/raw-auto", "screenshots/iphone", [
        ("01-empty.png",    "01-empty",    "导入你自己的直播源", "不内置、不托管任何节目"),
        ("02-channels.png", "02-channels", "频道列表一目了然",   "分组、收藏、最近观看"),
        ("03-browse.png",   "03-browse",   "按分组浏览",         "M3U 里的分组原样保留"),
        ("04-settings.png", "04-settings", "播放行为随你调",     "重连、常亮、定时关闭"),
    ]),
    ("openterminal", "iphone-69", "#007AFF", "screenshots/raw", "screenshots/iphone", [
        ("terminal-clean.png", "01-terminal", "随时随地连上服务器", "完整 SSH 会话，支持密钥登录"),
    ]),
    ("openterminal", "iphone-69", "#007AFF", "screenshots/raw-auto", "screenshots/iphone", [
        ("01-servers.png",  "02-servers",  "服务器集中管理",   "名称、标签、备注都能记"),
        ("06-settings.png", "03-settings", "字体主题随你挑",   "终端配色与字号可调"),
    ]),
    ("record", "iphone-69", "#34C759", "screenshots/raw-auto", "screenshots/iphone", [
        ("01-overview.png", "01-overview", "今天完成得怎么样",   "打卡、连续天数、完成率"),
        ("02-checkin.png",  "02-checkin",  "建任务，设重复规则", "按天、按周、自定义间隔"),
        ("03-metrics.png",  "03-metrics",  "体重身高的趋势图",   "指标按档案分开记"),
        ("04-settings.png", "04-settings", "提醒与备份都在这里", "数据只存本机，可导出"),
    ]),
    ("speed", "iphone-69", "#FF3B30", "screenshots/raw-auto", "screenshots/iphone", [
        ("01-today.png",     "01-today",     "每天一期，值得看的几件事", "五个板块，12 到 20 条"),
        ("03-profile.png",   "02-profile",   "收藏与备份",              "换手机不丢收藏"),
        ("02-favorites.png", "03-favorites", "收藏单条新闻",            "跨期保留，随时回看"),
    ]),
    ("spincourt", "iphone-69", "#FF9500", "screenshots/raw-auto", "screenshots/iphone", [
        ("01-setup.png",  "01-setup",  "设好人数和队数", "点了就分，不用现场点人"),
        ("02-result.png", "02-result", "转盘随机分队",   "谁跟谁一队，一眼看清"),
        ("03-again.png",  "03-again",  "不满意就再转一次", "纯随机，没有隐藏规则"),
    ]),

    # ---------------- iOS：iPad 13" ----------------
    ("afu", "ipad-13", "#6C5CE7", "screenshots/raw-ipad", "screenshots/ipad", [
        ("01-home.png",    "01-home",   "把大模型装进 iPad", "对话不出设备，断网也能聊"),
        ("03-models2.png", "02-models", "多种模型随你选",     "0.5B 到 4B，按你的设备挑"),
        ("02-models.png",  "03-download", "一键下载到本机",   "支持断点续传与镜像源"),
    ]),
    ("babyrecord", "ipad-13", "#E8739A", "screenshots/raw/ipad", "screenshots/ipad", [
        ("pad1.png", "01-record",   "记录宝宝的每一餐", "喂奶、睡眠、排便，一次点击记下"),
        ("pad2.png", "02-overview", "喂养情况一眼看清", "今天记了多少次、喝了多少毫升"),
        ("pad3.png", "03-trend",    "趋势变化自动成图", "奶量、次数、间隔都能看趋势"),
        ("pad4.png", "04-settings", "多个宝宝，自定义字段", "记录类型随你增减"),
    ]),
    ("gwave", "ipad-13", "#30B0C7", "screenshots/raw-ipad", "screenshots/ipad", [
        ("01-player.png", "01-player", "雨声、海浪，按下就有", "内置音效本机合成，不占存储"),
        ("02-list.png",   "02-list",   "自建电台列表",         "手动添加或用链接一键导入"),
        ("03-list2.png",  "03-list2",  "收藏常听的台",         "分组整理，随手可及"),
    ]),
    ("muyuntv", "ipad-13", "#FF3B30", "screenshots/raw-ipad", "screenshots/ipad", [
        ("01-empty.png",    "01-empty",    "导入你自己的直播源", "不内置、不托管任何节目"),
        ("02-channels.png", "02-channels", "频道列表一目了然",   "大屏看列表更舒服"),
        ("03-browse.png",   "03-browse",   "按分组浏览",         "M3U 里的分组原样保留"),
    ]),
    ("openterminal", "ipad-13", "#007AFF", "screenshots/raw-ipad", "screenshots/ipad", [
        ("01-servers.png",  "01-servers",  "服务器集中管理", "名称、标签、备注都能记"),
        ("02-settings.png", "02-settings", "字体主题随你挑", "终端配色与字号可调"),
        ("terminal-clean.png", "03-terminal", "大屏跑命令更舒服", "完整 SSH 会话，支持外接键盘"),
    ]),
    ("record", "ipad-13", "#34C759", "screenshots/raw-ipad", "screenshots/ipad", [
        ("01-overview.png", "01-overview", "今天完成得怎么样",   "打卡、连续天数、完成率"),
        ("02-checkin.png",  "02-checkin",  "建任务，设重复规则", "按天、按周、自定义间隔"),
        ("03-metrics.png",  "03-metrics",  "体重身高的趋势图",   "指标按档案分开记"),
        ("04-settings.png", "04-settings", "提醒与备份都在这里", "数据只存本机，可导出"),
    ]),
    ("speed", "ipad-13", "#FF3B30", "screenshots/raw-ipad", "screenshots/ipad", [
        ("01-today.png",     "01-today",     "每天一期，值得看的几件事", "五个板块，12 到 20 条"),
        ("03-profile.png",   "02-profile",   "收藏与备份",              "换手机不丢收藏"),
        ("02-favorites.png", "03-favorites", "收藏单条新闻",            "跨期保留，随时回看"),
    ]),
    ("spincourt", "ipad-13", "#FF9500", "screenshots/raw-ipad", "screenshots/ipad", [
        ("01-setup.png",  "01-setup",  "设好人数和队数", "点了就分，不用现场点人"),
        ("02-result.png", "02-result", "转盘随机分队",   "谁跟谁一队，一眼看清"),
        ("03-again.png",  "03-again",  "不满意就再转一次", "纯随机，没有隐藏规则"),
    ]),

    # ---------------- macOS ----------------
    ("jike", "mac", "#2F6BFF", "screenshots/raw", "screenshots/mac", [
        ("1.png", "01-terminal",   "按 F12，终端从屏幕边缘滑出", "再按一次收起，不占桌面"),
        ("2.png", "02-appearance", "透明度与模糊随时调",         "配色、字体、光标都能改"),
        ("3.png", "03-palette",    "169 套配色方案",             "与 Guake 完全一致"),
        ("4.png", "04-general",    "开机自启，随叫随到",         "行为与 Guake 对齐"),
        ("5.png", "05-keys",       "快捷键与 Guake 一致",        "从 Guake 迁过来零成本"),
        ("6.png", "06-keys2",      "全套快捷键可自定义",         "按你的习惯改"),
        ("7.png", "07-about",      "开源，可自行构建",           "逻辑测试全程守护"),
    ]),
    ("muyunimage", "mac", "#5E5CE6", "screenshots/raw", "screenshots/mac", [
        ("editor.png", "01-editor", "涂抹即除，本机完成", "内容感知与 AI 消除都不上传"),
        ("empty.png",  "02-open",   "打开一张图就能改",   "不下载模型也能先用内容感知消除"),
        ("model.png",  "03-model",  "AI 消除模型按需下载", "187 MB，断点续传，三种源可选"),
    ]),
    ("muyunright", "mac", "#2F6BFF", "screenshots/raw", "screenshots/mac", [
        ("1.png", "01-overview", "让访达右键更强大",       "新建文件、拷贝路径、打开终端"),
        ("2.png", "02-menu",     "每一项都能开关和改名",   "只留你要的，不堆菜单"),
        ("3.png", "03-general",  "常用文件夹与打开方式",   "右键直达你常用的位置"),
        ("4.png", "04-finder",   "右键即用，无需打开主程序", "空白处与选中项分别配置"),
    ]),
    ("weedit", "mac", "#D97706", "screenshots/raw", "screenshots/mac", [
        ("editor.png", "01-editor", "一次写稿，四处粘贴", "公众号、小红书、知乎、微博各一套规则"),
        ("table.png",  "02-table",  "表格并排图都能带走", "按各平台规则转换，不是直接丢掉"),
        ("preview.png","03-preview","先看粘贴后长什么样",   "公众号、小红书各自预览"),
    ]),
]


def main():
    only = sys.argv[1:] or None
    ok = fail = 0
    for app, target, accent, srcdir, outdir, shots in JOBS:
        if only and app not in only:
            continue
        base = ROOT / app
        out = base / outdir
        for src, name, title, sub in shots:
            inp = base / srcdir / src
            if not inp.exists():
                print(f"  [缺素材] {app}/{src}")
                fail += 1
                continue
            r = subprocess.run([sys.executable, str(COMPOSE),
                                "--input", str(inp), "--target", target,
                                "--title", title, "--subtitle", sub,
                                "--accent", accent,
                                "--output", str(out / f"{name}.png")],
                               capture_output=True, text=True)
            if r.returncode == 0:
                ok += 1
                print(r.stdout.strip())
            else:
                fail += 1
                print(f"  ✗ {app}/{name}: {r.stderr.strip()[:120]}")
    print(f"\n完成 {ok} 张，失败 {fail} 张")


if __name__ == "__main__":
    main()
