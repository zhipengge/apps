#!/usr/bin/env python3
"""批量合成商店截图。读取下面的 JOBS 配置。"""
import subprocess, sys
from pathlib import Path

COMPOSE = Path.home() / ".claude/skills/apple-app-screenshots/scripts/compose.py"
ROOT = Path(__file__).resolve().parent.parent

JOBS = [
    # ---------------- BabyRecord ----------------
    dict(app="babyrecord", target="iphone-69", accent="#E8739A",
         srcdir="babyrecord/screenshots/raw/iphone", outdir="babyrecord/screenshots/iphone",
         shots=[("01-record",   "记录宝宝的每一餐", "喂奶、睡眠、排便，一次点击记下"),
                ("02-overview", "喂养情况一眼看清", "今天记了多少次、喝了多少毫升"),
                ("03-trend",    "趋势变化自动成图", "奶量、次数、间隔都能看趋势"),
                ("04-settings", "多个宝宝，自定义字段", "记录类型随你增减")]),
    dict(app="babyrecord", target="ipad-13", accent="#E8739A",
         srcdir="babyrecord/screenshots/raw/ipad", outdir="babyrecord/screenshots/ipad",
         shots=[("01-record",   "记录宝宝的每一餐", "喂奶、睡眠、排便，一次点击记下"),
                ("02-overview", "喂养情况一眼看清", "今天记了多少次、喝了多少毫升"),
                ("03-trend",    "趋势变化自动成图", "奶量、次数、间隔都能看趋势"),
                ("04-settings", "多个宝宝，自定义字段", "记录类型随你增减")]),
    # ---------------- JiKe ----------------
    dict(app="jike", target="mac", accent="#2F6BFF",
         srcdir="jike/screenshots/raw", outdir="jike/screenshots/mac",
         shots=[("01-terminal", "按 F12，终端从屏幕边缘滑出", "再按一次收起，不占桌面"),
                ("02-appearance", "透明度与模糊随时调", "配色、字体、光标都能改"),
                ("03-palette",  "169 套配色方案", "与 Guake 一致"),
                ("04-general",  "开机自启，随叫随到", "行为和 Guake 对齐"),
                ("05-keys",     "快捷键与 Guake 一致", "从 Guake 迁过来零成本"),
                ("06-keys2",    "全套快捷键可自定义", "按你的习惯改"),
                ("07-about",    "开源，可自行构建", "逻辑测试全程守护")]),
    # ---------------- MuyunRight ----------------
    dict(app="muyunright", target="mac", accent="#2F6BFF",
         srcdir="muyunright/screenshots/raw", outdir="muyunright/screenshots/mac",
         shots=[("01-overview", "让访达右键更强大", "新建文件、拷贝路径、打开终端"),
                ("02-menu",     "每一项都能开关和改名", "只留你要的，不堆菜单"),
                ("03-general",  "常用文件夹与打开方式", "右键直达你常用的位置"),
                ("04-finder",   "右键即用，无需打开主程序", "空白处与选中项分别配置")]),
]

def main():
    only = sys.argv[1:] or None
    for job in JOBS:
        if only and job["app"] not in only:
            continue
        src = sorted((ROOT / job["srcdir"]).glob("*.png"))
        if not src:
            print(f"  [跳过] {job['app']}: {job['srcdir']} 无素材"); continue
        print(f"######## {job['app']} / {job['target']} ({len(src)} 张素材) ########")
        outdir = ROOT / job["outdir"]
        for i, (name, title, sub) in enumerate(job["shots"]):
            if i >= len(src):
                break
            out = outdir / f"{name}.png"
            cmd = [sys.executable, str(COMPOSE),
                   "--input", str(src[i]), "--target", job["target"],
                   "--title", title, "--subtitle", sub,
                   "--accent", job["accent"], "--output", str(out)]
            subprocess.run(cmd, check=False)

if __name__ == "__main__":
    main()
