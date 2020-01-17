from Strategies.BollingerBands import BollingerBands
from Data.Binance import Binance

b = Binance("LTCBTC")

bollinger_bands = BollingerBands()

bollinger_bands.train_strategy(b.get_train_data())

bollinger_bands.plot_data()
