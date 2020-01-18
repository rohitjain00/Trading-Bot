class trade():
    def __init__(self, stock, balance):
        self.initial_stock = stock
        self.initial_balance = balance
        self.stock = stock
        self.balance = balance
        self.history = []

    def buy(self, price_per_stock, stock):
        if self.balance - (price_per_stock * stock) < 0:
            print("Unable to buy due to low balance")
            return False
        self.stock += stock
        self.balance -= (price_per_stock * stock)
        self.history.append({'signal': 'buy', 'price_per_stock': price_per_stock, 'stock': stock, 'balance': self.balance, 'total_stock': self.stock})
        return True

    def sell(self, price_per_stock, stock):
        if self.stock - stock < 0:
            print("Unable to sell due to low stock")
            return False
        self.stock -= stock
        self.balance += (price_per_stock * stock)
        self.history.append({'signal': 'sell', 'price_per_stock': price_per_stock, 'stock': stock, 'balance': self.balance, 'total_stock': self.stock})
        return True

    def get_curr_statistics(self):
        return self.stock, self.balance

    def get_history(self):
        return self.history

    def get_backtesting_result(self, price_at_end):
        print("------------------------------")
        print("Initially Stock : ", self.initial_stock, " Initial Balance : ", self.initial_balance)
        print("At end Stocks : ", self.stock)
        print("Worth : ", (self.stock*price_at_end))
        print("Total Worth of assets : ", (self.balance + (self.stock * price_at_end)))
        print("------------------------------")
