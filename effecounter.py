import argparse
import os
import re
import subprocess
import sys
import tkinter as tk
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
LOG_FILE = SCRIPT_DIR / "effecounter.md"
TEMPLATE = """\
# what is effecounter?
理想状態を阻む因子を計測するカウンターアプリ。ラベルLをつけて実行すると、タイムスタンプ付きでLが発生したことを記録する。実行時にコメントを書くこともできる。つまり、Lとして表現される因子が起きたときに、自ら起動することでその旨を記録する。

effecounter は effectiveness counter の略であり、engineering effectiveness の考え方を参考にしている。なお、effecounter は指定ラベルが示すイベントの記録を行うだけであり、理想状態自体には言及しない。

# labels
- count1: ここは説明欄。count1ラベルに対する説明や背景を書く。

# logs
"""


def open_log():
    if not LOG_FILE.exists():
        LOG_FILE.write_text(TEMPLATE, encoding="utf-8")
    if sys.platform.startswith("win"):
        os.startfile(str(LOG_FILE))
    elif sys.platform == "darwin":
        subprocess.run(["open", str(LOG_FILE)])
    else:
        subprocess.run(["xdg-open", str(LOG_FILE)])


def read_labels():
    if not LOG_FILE.exists():
        return set()
    text = LOG_FILE.read_text(encoding="utf-8")
    m = re.search(r"^# labels\s*\n(.*?)(?=^# |\Z)", text, re.MULTILINE | re.DOTALL)
    if not m:
        return set()
    labels = set()
    for line in m.group(1).splitlines():
        lm = re.match(r"^- (\S+?):", line)
        if lm:
            labels.add(lm.group(1))
    return labels


def append_log(label, comment):
    text = LOG_FILE.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    ts = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    LOG_FILE.write_text(text + f"- {ts} {label}: {comment}\n", encoding="utf-8")


def prompt(label):
    result = {"action": "cancel", "text": ""}
    root = tk.Tk()
    root.title(f"effecounter: {label}")
    w, h = 480, 60
    x = (root.winfo_screenwidth() - w) // 2
    y = (root.winfo_screenheight() - h) // 2
    root.geometry(f"{w}x{h}+{x}+{y}")
    root.attributes("-topmost", True)

    entry = tk.Entry(root, font=("", 12))
    entry.pack(fill="both", expand=True, padx=6, pady=6)
    entry.focus_force()

    def submit(_=None):
        text = entry.get()
        if text == "/":
            result["action"] = "openlog"
        else:
            result["action"] = "submit"
            result["text"] = text
        root.destroy()

    def cancel(_=None):
        result["action"] = "cancel"
        root.destroy()

    entry.bind("<Return>", submit)
    entry.bind("<Escape>", cancel)
    root.protocol("WM_DELETE_WINDOW", cancel)
    root.mainloop()
    return result["action"], result["text"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", required=True)
    args = ap.parse_args()

    if args.label not in read_labels():
        open_log()
        return

    action, text = prompt(args.label)
    if action == "openlog":
        open_log()
    elif action == "submit":
        append_log(args.label, text)


if __name__ == "__main__":
    main()
