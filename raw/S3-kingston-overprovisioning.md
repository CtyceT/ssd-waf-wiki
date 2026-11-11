---
id: S3
title: Understanding SSD Over-provisioning (OP)
publisher: Kingston Technology
url: https://kingston.com/en/ssd/overprovisioning
fetched: 2026-11-11
type: 廠商技術文章
note: 擷取工具在結果中自行計算了 (64−60)/60≈6.7%，該數字不是原文，已排除，不收錄。
---

## 原文擷取

1. "the SSD manufacturer can reserve an additional percentage of the total drive capacity for Over-provisioning"
2. OP 公式（原文表格）：(Physical Capacity − User Capacity) ÷ User Capacity
3. 原文表格：讀取密集型（read-intensive）產品一般為 7%；寫入密集型（write-intensive）一般為 28%；DC500M 為 32%。
4. "This is why 32% OP is recommended for applications that are more write-intensive."
5. "over-provisioning is used by the SSD controller's garbage collection function" … "as a temporary workspace to manage scheduled valid page merges and reclaim blocks."
6. "Keeping a large quantity of blocks empty and in reserve via over-provisioning aids in keeping performance consistent"
7. "The greater the OP percentage, the longer an SSD can last."
