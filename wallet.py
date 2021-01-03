class wallet:
    def __init__(self):
        self.crypto_wallet = {"ETH":0,"BTC":0} 

    def get_balance(self,target):
        self.target = target
        return self.crypto_wallet[target]