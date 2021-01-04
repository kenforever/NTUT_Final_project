import sqlite3
from init import init
from exchange_rate import exchange_rate
class trade(init):

    def get_value(self):
        ETH = self.conn.execute("select ETH_balance from account where UID='{}'".format(self.uid))
        BTC = self.conn.execute("select BTC_balance from account where UID='{}'".format(self.uid))
        ETH = ETH.fetchall()[0][0]
        BTC = BTC.fetchall()[0][0]
        data = {"ETH":ETH,"BTC":BTC}
        return data

    def name_exchange(self,FROM):
        self.FROM = FROM
        if self.FROM == "ETH":
            self.FROM = "ETH_balance"
        elif self.FROM == "BTC":
            self.FROM = "BTC_balance"
        return self.FROM

    def swap(self,target,FROM,amount):
        self.target = target
        self.FROM = FROM
        self.amount = amount
        balance_temp = self.get_value()[FROM]
        target_balance_temp = self.get_value()[target]
        if balance_temp > self.amount:
            FROM_amount = balance_temp-amount
            self.FROM = self.name_exchange(self.FROM)
            self.conn.execute("update account set {} = '{}' where uid='{}'".format(self.FROM,FROM_amount,self.uid))      #FROM餘額減少
            rate = exchange_rate(target,FROM)
            self.target = self.name_exchange(self.target)
            amount = self.amount*rate
            amount = amount + target_balance_temp
            self.conn.execute("update account set {} = '{}' where uid='{}'".format(self.target,amount,self.uid))       #target餘額增加      
            return self.get_value()
        else:
            return "not enough balance."

    def transfer_out(self,FROM,amount):
        self.FROM = FROM
        self.amount = amount
        FROM_balance = self.get_value()[FROM]
        if FROM_balance > self.amount:
            FROM_balance = FROM_balance - self.amount
            bank_balance = self.conn.execute("select bank_balance from account where UID='{}'".format(self.uid)).fetchall()[0][0]
            rate = exchange_rate("USDT",self.FROM)
            amount = amount *rate
            bank_balance += amount
            self.FROM = self.name_exchange(self.FROM)
            self.conn.execute("update account set {} = '{}' where uid='{}'".format(self.FROM,FROM_balance,self.uid))
            self.conn.execute("update account set bank_balance = '{}' where uid='{}'".format(bank_balance,self.uid))
            return bank_balance
        else:
            return "not enough balance."

    def balance(self):
        rate = exchange_rate("USDT",self.FROM)
        eth = self.get_value()["ETH"]*rate
        btc = self.get_value()["BTC"]*rate
        usdt = eth+btc
        print(usdt,eth,btc)
        self.conn.execute("update account set bank_balance = '{}' where uid='{}'".format(usdt,self.uid))
        self.conn.execute("update account set ETH_balance = '0' where uid='{}'".format(self.uid))
        self.conn.execute("update account set BTC_balance = '0' where uid='{}'".format(self.uid))        
        return "finish"
