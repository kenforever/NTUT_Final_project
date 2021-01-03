from balance import check_balance
from trade import trade_account as trade
class bank(check_balance): #銀行帳戶

    def check_balance(self):
        print("your bank account have",self.balance)

    def get_balance(self):
        return self.balance

    def transfer_in(self,amount):
        self.balance += amount
    
    def transfer_out(self,amount):
        if self.balance>amount:
            self.balance -= amount
            trade.transfer_in(amount)
        else:
            return "not enough balance"

    def balance(self):
        trade.balance()