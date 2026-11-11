---
title: 寫入放大（Write Amplification, WA / WAF）
sources: [S1, S4, S5]
updated: 2026-11-11
---
# 寫入放大（WAF）
SSD 實際寫進 Flash 的量，比使用者要求寫的量還多的現象。

## 重點
- 寫入放大是 Flash 與 SSD 的一種不理想現象 [S1-1]。
- WAF 是「裝置實際寫入」除以「主機要求寫入」的比值 [S4-1][S1-2]。
- 公式：WAF = 寫進 NAND 的量 ÷ 主機寫入的量 [S4-2][S5-3]。
- 例子：主機寫了 4GB，SSD 實際寫了 5GB，WAF = 1.25 [S5-4]。
- 原因來自 NAND 的運作方式，SSD 可能需要寫得比主機要求的還多 [S5-2]。
- WAF 會隨工作負載與硬碟設定而不同 [S5-5]。
- 循序寫入的 WAF 約為 1；大量隨機寫入會讓 WAF 大於 1 [S5-6][S1-14]。
- 沒有壓縮時，WA 不會低於 1 [S1-17]；SandForce 宣稱用壓縮可達 0.5 [S1-18]。

## 相關頁面
- [垃圾回收](garbage-collection.md)
- [壽命與 P/E 次數](endurance.md)

## 來源
- [S1](../sources/S1.md)
- [S4](../sources/S4.md)
- [S5](../sources/S5.md)

## 待確認
- 無
