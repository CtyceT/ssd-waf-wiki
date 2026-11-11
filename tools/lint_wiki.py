#!/usr/bin/env python3
"""N3：Wiki lint。用法：python3 tools/lint_wiki.py

檢查：
1. 概念頁「## 重點」每一條都有引用 [S#-n] 或【推論】
2. 每個引用都對得到 raw 檔案中真的存在的那一句
3. 頁面之間的相對連結都存在
4. index.md 列出了所有 wiki 頁面
5. 沒有孤兒頁（除了 index 以外，沒有任何頁面連到它）
6. 每篇 raw 都有對應的 sources/S#.md
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI, RAW = ROOT / "wiki", ROOT / "raw"
CITE = re.compile(r"\[(S\d+)-(\d+)\]")
LINK = re.compile(r"\]\(([^)#\s]+\.md)\)")
errors, warnings = [], []


def raw_items():
    """回傳 {'S1': {1, 2, ...}}：每篇 raw 有哪些編號句子。"""
    items = {}
    for p in RAW.glob("S*-*.md"):
        sid = p.name.split("-")[0]
        nums = {int(m.group(1)) for m in re.finditer(r"^(\d+)\.", p.read_text(encoding="utf-8"), re.M)}
        items[sid] = nums
    return items


def section(text, title):
    m = re.search(rf"^## {title}\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else None


def main():
    items = raw_items()
    pages = sorted(p for p in WIKI.rglob("*.md"))
    rel = {p.relative_to(WIKI).as_posix(): p for p in pages}
    inbound = {k: 0 for k in rel}

    for name, p in rel.items():
        text = p.read_text(encoding="utf-8")

        # 2. 引用存在
        for sid, n in CITE.findall(text):
            if sid not in items:
                errors.append(f"{name}：引用 [{sid}-{n}]，但 raw/ 沒有 {sid}")
            elif int(n) not in items[sid]:
                errors.append(f"{name}：引用 [{sid}-{n}]，但 {sid} 沒有第 {n} 句")

        # 3. 連結存在、計算被連結次數
        for target in LINK.findall(text):
            dest = (p.parent / target).resolve()
            try:
                key = dest.relative_to(WIKI.resolve()).as_posix()
            except ValueError:
                continue  # 連到 wiki 以外（例如 raw/）
            if key not in rel:
                errors.append(f"{name}：連結 {target} 不存在")
            elif name != "index.md":
                inbound[key] += 1

        # 1. 概念頁每條重點都有引用
        if name.startswith("concepts/"):
            body = section(text, "重點")
            if body is None:
                errors.append(f"{name}：缺少「## 重點」區")
            else:
                for line in body.splitlines():
                    if line.strip().startswith("- ") and not (CITE.search(line) or "【推論】" in line):
                        errors.append(f"{name}：這條重點沒有引用 → {line.strip()[:40]}")
            if section(text, "待確認") is None:
                errors.append(f"{name}：缺少「## 待確認」區")

        if name.startswith("explainers/") and "【推論】" not in text:
            errors.append(f"{name}：explainer 必須標示【推論】")

    # 4. index 收錄所有頁面
    index = (WIKI / "index.md").read_text(encoding="utf-8")
    for name in rel:
        if name not in ("index.md", "log.md") and f"({name})" not in index:
            errors.append(f"index.md 沒有收錄 {name}")

    # 5. 孤兒頁
    for name, n in inbound.items():
        if name in ("index.md", "log.md", "overview.md") or n > 0:
            continue
        # workflow v2：來源沒被任何概念頁使用 → 錯誤（不只是警告），必須「寫成概念頁」或註明「不使用：原因」
        # 理由：第 1 次執行時這只是警告，結果缺口一路漏到 N5 才被發現。
        if name.startswith("sources/") and "不使用：" not in rel[name].read_text(encoding="utf-8"):
            errors.append(f"{name} 沒有被任何概念頁使用：請寫成概念頁，或在來源頁註明「不使用：原因」")
        else:
            warnings.append(f"{name} 是孤兒頁：除了 index 以外沒有頁面連到它")

    # 6. 每篇 raw 都有 source 頁
    for sid in items:
        if f"sources/{sid}.md" not in rel:
            errors.append(f"raw/{sid} 沒有對應的 wiki/sources/{sid}.md")

    for w in warnings:
        print("警告：", w)
    if errors:
        print(f"Lint 失敗：{len(errors)} 個錯誤")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    cites = sum(len(CITE.findall(p.read_text(encoding='utf-8'))) for p in pages)
    print(f"Lint 通過：{len(pages)} 頁、{cites} 個引用，皆可對應到 raw。")


if __name__ == "__main__":
    main()
