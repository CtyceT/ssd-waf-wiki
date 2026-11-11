#!/usr/bin/env python3
"""簡報檢查。

python3 tools/check_slides.py --plan   N5：大綱覆蓋檢查（每張需要的 Wiki 頁都存在嗎？）
python3 tools/check_slides.py          N5 + N7：再檢查 slides/index.html

N7 檢查：
1. 每張投影片都有 data-part 與 data-wiki，且 data-wiki 的頁面存在
2. 段落順序：問題 → 原理 → 代價 → 解法 → 測驗 → 總結，且每種都有
3. 張數 10～16
4. 每個數字都能在該頁 data-wiki 列出的 Wiki 頁面中找到（防止編造）
5. 每張都有來源頁尾（.src）
6. 不出現未解釋的術語縮寫、不使用 emoji
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
PARTS = ["問題", "原理", "代價", "解法", "測驗", "總結"]
BANNED = ["FTL", "LBA"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
NUMBER = re.compile(r"\d+(?:\.\d+)?")
VOID = {"br", "img", "hr", "input", "meta", "link", "wbr", "source"}  # 沒有結尾標籤的元素
errors = []


def check_plan():
    text = (ROOT / "slides" / "plan.md").read_text(encoding="utf-8")
    slides = re.findall(r"^## (\d+) \| (\S+) \| (.+?)\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    for num, part, title, body in slides:
        m = re.search(r"- wiki: (.+)", body)
        if not m:
            errors.append(f"大綱 {num}「{title}」沒有列出 wiki 來源")
            continue
        for page in [s.strip() for s in m.group(1).split(",")]:
            if not (WIKI / page).exists():
                errors.append(f"大綱 {num}「{title}」需要 wiki/{page}，但 Wiki 沒有這頁 → 回 N1/N2 補內容")
    return len(slides)


class SlideParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides, self.cur, self.depth, self.skip = [], None, 0, 0

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return  # 不計入深度，否則 <br> 會讓投影片永遠不會結束（第 1 次執行時發現的 bug）
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        if tag == "section" and "slide" in classes:
            self.cur = {"part": a.get("data-part"), "wiki": a.get("data-wiki"),
                        "text": "", "has_src": False}
            self.depth = 1
            return
        if self.cur is not None:
            self.depth += 1
            if "src" in classes:
                self.cur["has_src"] = True
                self.skip = self.depth
            elif "nocheck" in classes and not self.skip:
                self.skip = self.depth   # 頁碼等裝飾數字

    def handle_endtag(self, tag):
        if tag in VOID or self.cur is None:
            return
        if self.skip == self.depth:
            self.skip = 0
        self.depth -= 1
        if self.depth == 0:
            self.slides.append(self.cur)
            self.cur = None

    def handle_data(self, data):
        if self.cur is not None and not self.skip:
            self.cur["text"] += data


def check_html():
    html = (ROOT / "slides" / "index.html").read_text(encoding="utf-8")
    p = SlideParser()
    p.feed(html)
    slides = p.slides
    expected = len(re.findall(r'<section class="slide"', html))
    if len(slides) != expected:  # 自我驗證：檢查工具不能安靜地漏掉投影片
        errors.append(f"解析器只讀到 {len(slides)} 張，但 HTML 有 {expected} 張 → 檢查工具本身有問題")
    if not 10 <= len(slides) <= 16:
        errors.append(f"張數應為 10～16，實際 {len(slides)}")

    order = []
    for i, s in enumerate(slides, 1):
        where = f"第 {i} 張"
        if s["part"] not in PARTS:
            errors.append(f"{where}：data-part「{s['part']}」不是 {PARTS} 之一")
            continue
        order.append(PARTS.index(s["part"]))
        pages = [x.strip() for x in (s["wiki"] or "").split(",") if x.strip()]
        if not pages:
            errors.append(f"{where}：沒有 data-wiki")
        source = ""
        for page in pages:
            f = WIKI / page
            if not f.exists():
                errors.append(f"{where}：data-wiki 的 {page} 不存在")
            else:
                source += f.read_text(encoding="utf-8")
        if not s["has_src"]:
            errors.append(f"{where}：缺少來源頁尾 .src")
        for n in sorted(set(NUMBER.findall(s["text"]))):
            if n not in source:
                errors.append(f"{where}：數字「{n}」在 {pages} 中找不到 → 可能是編造或 Wiki 缺內容")
        for word in BANNED:
            if word in s["text"]:
                errors.append(f"{where}：出現未解釋的術語 {word}")
        if EMOJI.search(s["text"]):
            errors.append(f"{where}：不可使用 emoji")

    if order != sorted(order):
        errors.append(f"段落順序錯誤：{[PARTS[i] for i in order]}")
    missing = [PARTS[i] for i in range(len(PARTS)) if i not in order]
    if missing:
        errors.append(f"缺少段落：{missing}")
    return len(slides)


def main():
    n_plan = check_plan()
    plan_only = "--plan" in sys.argv
    n_html = None if plan_only else check_html()
    if errors:
        print(f"檢查失敗：{len(errors)} 個問題")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    if plan_only:
        print(f"N5 覆蓋檢查通過：大綱 {n_plan} 張需要的 Wiki 頁都存在。")
    else:
        print(f"全部通過：大綱 {n_plan} 張、簡報 {n_html} 張，數字與來源皆可追溯到 Wiki。")


if __name__ == "__main__":
    main()
