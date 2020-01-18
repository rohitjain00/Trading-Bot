from Server.server import Server
from Data.Binance import Binance

b = Binance("BNBBTC")
s = Server(b, 10, 0)

s.run(10000, 1)
