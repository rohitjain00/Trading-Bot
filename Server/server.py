import time
from Strategies.BollingerBands import BollingerBands
from Server.trade import trade


class Server:
    STOCK_QTY = 10

    def __init__(self, strategy, stock, balance, after_trade):
        self.strategy = strategy
        self.bollinger_bands = BollingerBands()
        self.trade = trade(stock, balance=balance)
        self.after_trade = after_trade

    def run(self, time_to_repeat, delay_in_seconds):
        self.__one_time_action()
        # self.bollinger_bands.plot_data()
        while time_to_repeat > 0:
            time.sleep(delay_in_seconds)
            time_to_repeat -= 1
            self.__repeat_action()
            if time_to_repeat % self.after_trade == 0:
                self.trade.insert_total_assets_for_hit_ration(self.bollinger_bands.price_at_end())
        # self.bollinger_bands.plot_data()
        print('--------------------')
        print(self.trade.get_backtesting_result(self.bollinger_bands.price_at_end()))
        print('--------------------')
        print(self.trade.get_hit_ratio())
        print('--------------------')
        print(self.trade.get_history())

    def __one_time_action(self):
        self.bollinger_bands.train_strategy(self.strategy.get_train_data())

    def __repeat_action(self):
        has_sig, sig_type, price_per_stock = self.bollinger_bands.add_new_data(self.strategy.get_new_data())
        if has_sig:
            if sig_type == "buy":
                self.trade.buy(price_per_stock, self.STOCK_QTY)
            else:
                self.trade.sell(price_per_stock, self.STOCK_QTY)
        stock, balance = self.trade.get_curr_statistics()
        print("stock : ", stock, " balance : ", balance)
        # self.bollinger_bands.plot_data()

