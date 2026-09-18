# -*- coding: utf-8 -*-
"""
每日大赛自动化编译与质检脚本 (Build Contest Script)
用法：
  python build_contest.py 2026-09-18
若不传参，则默认编译当天日期的文件夹。
"""

import os
import sys
import subprocess
import shutil
from datetime import datetime

VAULT_DAILY_DIR = os.path.dirname(os.path.abspath(__file__))

def compile_daily_contest(date_str=None):
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")

    target_dir = os.path.join(VAULT_DAILY_DIR, date_str)
    tex_file = os.path.join(target_dir, "每日大赛.tex")
    pdf_file = os.path.join(target_dir, "每日大赛.pdf")

    if not os.path.exists(target_dir):
        print(f"[ERROR] 目标文件夹不存在: {target_dir}")
        sys.exit(1)

    if not os.path.exists(tex_file):
        print(f"[ERROR] 未找到每日大赛.tex: {tex_file}")
        sys.exit(1)

    print(f"🚀 开始编译每日大赛 [{date_str}]...")
    original_cwd = os.getcwd()
    os.chdir(target_dir)

    try:
        # 第一次编译
        cmd = ["xelatex", "-synctex=1", "-interaction=nonstopmode", "每日大赛.tex"]
        print("  -> 第一轮 xelatex 编译中...")
        res1 = subprocess.run(cmd, capture_output=True, text=True)
        
        # 第二次编译以稳定引用与总页数
        print("  -> 第二轮 xelatex 编译 (更新 LastPage 引用)...")
        res2 = subprocess.run(cmd, capture_output=True, text=True)

        if os.path.exists("每日大赛.pdf"):
            print(f"✅ 编译成功！生成试卷: {pdf_file}")
            # 清理中间临时文件
            for ext in [".aux", ".log", ".out", ".synctex.gz"]:
                temp_f = f"每日大赛{ext}"
                if os.path.exists(temp_f):
                    try:
                        os.remove(temp_f)
                    except Exception:
                        pass
            print("🧹 临时辅助文件已清理完毕。")
        else:
            print("❌ 编译失败，未生成 PDF 文件。请检查 LaTeX 语法或控制台日志。")
            if res2.stderr:
                print(res2.stderr[:500])

    finally:
        os.chdir(original_cwd)

if __name__ == "__main__":
    target_date = sys.argv[1] if len(sys.argv) > 1 else None
    compile_daily_contest(target_date)
