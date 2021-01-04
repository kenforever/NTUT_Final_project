# 期末報告 虛擬貨幣模擬投資遊戲
## 簡介
此遊戲模擬真實投資, 起始玩家有10000USDT, 玩家可用此進行虛擬貨幣的買出或買入, 又或是虛擬貨幣之間的兌換。
## Class
本程式有兩個主要Class, 分別為bank與trade, 分別代表銀行帳戶與交易帳戶。兩者均為init的子類。
### bank
此為銀行帳戶，起始會有10000USDT。
method          | usage     |
----------------|-----------|
get_value       |取得帳戶餘額 |
name_exchange   |名稱轉換    |
transfer_out    |資產轉出    |

### trade
此為交易帳戶，起始會有0ETH與0BTC。
method          | usage     |
----------------|-----------|
get_value       |取得帳戶餘額 |
name_exchange   |名稱轉換    |
swap            |虛擬貨幣轉換 |
transfer_out    |資產轉出    |
balance         |平倉       |

### other
其他
method          | usage    |
----------------|----------|
exchange_rate   |取得匯率   |
get_balance     |以多態形式取得餘額 |

----------
## 主要流程
執行app.py, 軟件會生成uid並把各帳戶餘額存入資料庫。計時開始。

用戶可以在5分鐘內任意買出買入ETH或BTC，或是在ETH與BTC之間交換,匯率以即時匯率計算。

5分鐘後結束，系統自動平倉。同時計算總資產餘額。
