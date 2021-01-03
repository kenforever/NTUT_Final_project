from balance import check_balance
from exchange_rate import exchange_rate
class trade_account(check_balance): #交易帳戶
    
    def check_balance(self):
        print("your trade_account have",self.balance)

    def get_balance(self):
        return self.balance

    def transfer_in(self,amount):
        self.balance += amount
        trade.check_balance()

    def transfer_out(self,amount):
        if self.balance>amount:
            self.balance -= amount
            bank.transfer_in(amount)
        else:
            return "not enough balance"

    def buy_crypto(self,amount,TYPE):
        balance_temp = bank.get_balance()
        if balance_temp>amount and self.balance != 0:
            self.balance -= amount
            rate =exchange_rate(TYPE,"USDT")
            crypto_wallet[TYPE] += float(rate)*amount
        else:
            print("not enough balance")
    
    def exchange_crypto(self,amount,TYPE,FROM): #把amount個FROM換到TYPE
        rate = exchange_rate(TYPE,FROM)
        deposit = float(amount)*float(rate)
        balance_temp = crypto_wallet["FROM"]
        if balance_temp >amount:
            crypto_wallet[TYPE] += deposit
            crypto_wallet[FROM] -= amount

    def balance(self):
        ETH_temp = crypto_wallet["ETH"]
        BTC_temp = crypto_wallet["BTC"]
        crypto_wallet["ETH"] = 0
        crypto_wallet["BTC"] = 0
        result = ETH_temp+BTC_temp
        return result