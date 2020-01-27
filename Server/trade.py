class trade():
    def __init__(self, stock, balance):
        self.initial_stock = stock
        self.initial_balance = balance
        self.stock = stock
        self.balance = balance
        self.history = []
        self.profit_loss = []

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
        return self.balance + (self.stock * price_at_end)

    def insert_total_assets_for_hit_ration(self, price_at_end):
        self.profit_loss.append(self.get_backtesting_result(price_at_end) - self.initial_balance)

    def get_hit_ratio(self):
        total_wins = 0
        for profit in self.profit_loss:
            if profit > 0:
                total_wins += 1

        return total_wins, len(self.profit_loss)-total_wins
