---
id: S5
title: What Is Write Amplification?
publisher: Solidigm（SSD 廠商支援文件）
url: https://www.solidigm.com/support-page/maintenance-tools/ka-00015.html
fetched: 2026-11-11
type: 廠商支援文件
note: 本文只說明定義與計算，沒有談如何降低 WAF。
---

## 原文擷取

1. "WAF is a number to show how much more work the SSD has done than what was asked."
2. "Due to how NAND works, a NAND SSD may need to make more writes than what a user or host asked to write."
3. 公式：Write_Amplification_Factor = NAND_Writes_GB / Host_Writes_GB
4. 原文例子：主機寫入 4GB、硬碟實際寫入 5GB → WAF = 1.25
5. "Write Amplification Factor (WAF) depends on workload and drive configuration."
6. 原文說明：循序寫入的工作負載 WAF 約為 1；大量隨機寫入會讓 WAF 大於 1。
