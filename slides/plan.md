# 簡報大綱（N4 產生，N5 檢查覆蓋）

觀眾：完全沒學過的非資工同學。結構：問題 → 原理 → 代價 → 解法 → 測驗 → 總結。
格式：`## 編號 | 段落 | 標題`，下面的 `wiki:` 列出內容來源頁。

## 01 | 問題 | 你只存了 4GB，SSD 卻寫了 5GB？
- wiki: concepts/write-amplification.md
- 要點：用 Solidigm 的例子開場，引出「為什麼會多寫」。

## 02 | 原理 | 把 SSD 想成一疊筆記本
- wiki: explainers/notebook-analogy.md
- 要點：筆記本 = block、一頁 = page、原子筆不能擦。

## 03 | 原理 | 規則一：寫過的頁不能改
- wiki: concepts/nand-no-overwrite.md
- 要點：要改只能先擦掉。

## 04 | 原理 | 規則二：一頁一頁寫，卻只能整本一起擦
- wiki: concepts/page-and-block.md
- 要點：寫入與擦除的單位大小不同，這是問題的根源。

## 05 | 原理 | 刪掉檔案，SSD 其實不知道
- wiki: concepts/garbage-collection.md
- 要點：作業系統只在自己的表上標成空的。

## 06 | 原理 | 垃圾回收：先搬家，再整本擦掉
- wiki: concepts/garbage-collection.md, explainers/notebook-analogy.md
- 要點：四步驟圖解。

## 07 | 代價 | 寫入放大怎麼算？
- wiki: concepts/write-amplification.md, explainers/notebook-analogy.md
- 要點：WAF 公式；4GB→5GB；筆記本例子。

## 08 | 代價 | 什麼時候最嚴重？
- wiki: concepts/write-amplification.md
- 要點：循序約 1、隨機大於 1；沒有壓縮時不會低於 1。

## 09 | 代價 | 多寫的每一次都在消耗壽命
- wiki: concepts/endurance.md
- 要點：P/E 次數有限。

## 10 | 解法 | 解法一：TRIM，主動告訴 SSD 哪些沒用了
- wiki: concepts/trim.md
- 要點：SSD 不必再搬已刪除的資料。

## 11 | 解法 | 解法二：Over-provisioning，預留空白頁
- wiki: concepts/over-provisioning.md
- 要點：使用者看不到的保留空間，給 GC 當工作區；常見 7%、28%。

## 12 | 解法 | 解法三：寫入方式越循序越好
- wiki: concepts/write-amplification.md
- 要點：循序寫入 WAF 約為 1。

## 13 | 測驗 | 三題小測驗
- wiki: concepts/page-and-block.md, concepts/write-amplification.md, concepts/trim.md

## 14 | 總結 | 一張圖帶走
- wiki: overview.md
