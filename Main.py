from Server.server import Server
from Data.Binance import Binance

b = Binance("BNBBTC")
s = Server(b, 0, 1)

s.run(10000, 1)
