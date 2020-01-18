from Server.server import Server
from Data.Binance import Binance

b = Binance("BNBBTC")
s = Server(b, stock=0, balance=1)
s.run(time_to_repeat=100, delay_in_seconds=1)
