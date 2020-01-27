from Server.server import Server
from Data.Binance import Binance

b = Binance("BNBBTC")
s = Server(b, stock=0, balance=1, after_trade=20)
s.run(time_to_repeat=519, delay_in_seconds=1)
