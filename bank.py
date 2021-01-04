import sqlite3
from init import init
from get_balance import get_balance
from exchange_rate import exchange_rate
from trade import trade
class bank(init):
    def get_value(self):
        data = self.conn.execute("select bank_balance from account where UID='{}'".format(self.uid))
        data = data.fetchall()[0][0]
        return data

    def name_exchange(self,FROM):
        self.FROM = FROM
        if self.FROM == "ETH":
            self.FROM = "ETH_balance"
        elif self.FROM == "BTC":
            self.FROM = "BTC_balance"
        return self.FROM

    def transfer_out(self,amount,account):
        self.amount = amount
        self.account = account
        balance = self.get_value()
        if balance > self.amount:
            amount_temp = balance - self.amount
            rate = exchange_rate(self.account,"USDT")
            amount = amount*rate
            balance_temp = trade(self.uid)
            balance_temp = balance_temp.get_value()[self.account]
            amount = amount + balance_temp
            self.account = self.name_exchange(self.account)
            self.conn.execute("update account set bank_balance = '{}' where uid='{}'".format(amount_temp,self.uid))
            self.conn.execute("update account set {} = '{}' where uid='{}'".format(self.account,amount,self.uid))
            self.conn.commit()
            return "finish"
        else:
            return "not enough balance"    
