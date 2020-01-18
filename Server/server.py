import time
from Strategies.BollingerBands import BollingerBands
from Data.Binance import Binance
from Server.trade import trade


class Server():
    STOCK_QTY = 10

    def __init__(self, strategy, stock, balance):
        self.strategy = strategy
        self.bollinger_bands = BollingerBands()
        self.trade = trade(stock, balance=balance)

    def run(self, time_to_repeat, delay_in_seconds):
        self.__one_time_action()
        while time_to_repeat > 0:
            time.sleep(delay_in_seconds)
            time_to_repeat -= 1
            self.__repeat_action()

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
        print(self.trade.get_curr_statistics())
