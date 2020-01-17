from Data.Data import Data
import pandas as pd
import time
import requests


class Binance(Data):
    '''
    Binance API : https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md

    '''
    BINANCE_BASE_URL = "https://api.binance.com"
    _intervals = {
        "ONEMINUTE": "1m",
        "THREEMINUTE": "3m",
        "FIVEMINUTE": "5m",
        "FIFTEENMINUTE": "15m",
        "THIRTYMINUTE": "30m",
        "ONEHOUR": "1h",
        "TWOHOUR": "2h",
        "FOURHOUR": "4h",
        "SIXHOUR": "6h",
        "EIGHTHOUR": "8h",
        "TWELVEHOUR": "12h",
        "ONEDAY": "1d",
        "THREEDAY": "3d",
        "ONEWEEK": "1w",
        "ONEMONTH": "1M",
    }

    def __init__(self, symbol):
        self.symbol = symbol

    def data_from(self):
        return "Binance"

    @property
    def url(self):
        return self.BINANCE_BASE_URL + "/api/v3/klines"

    def _clean_data(self, data):
        dataFrame = pd.DataFrame(
            data.json(),
            columns=[
                "Open time",
                "Open",
                "High",
                "Low",
                "Close",
                "Volume",
                "Close time",
                "Quote asset volume",
                "Number of trades",
                "Taker buy base asset volume",
                "Taker buy quote asset volume",
                "ignore",
            ],
        )
        dataFrame = dataFrame.drop(columns="ignore")
        return dataFrame

    def get_train_data(self):
        p = {
            "symbol": self.symbol,
            "interval": self._intervals["ONEHOUR"],
            "limit": 1000,
        }
        return self._clean_data(requests.get(url=self.url, params=p))

    def get_new_data(self):
        p = {
            "symbol": self.symbol,
            "interval": self._intervals["ONEMINUTE"],
            "limit": 1,
        }
        return self._clean_data(requests.get(url=self.url, params=p))
