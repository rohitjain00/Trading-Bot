from .Strategy import Strategy
import pandas as pd
import matplotlib.pyplot as plt


class BollingerBands(Strategy):
    def __init__(self):
        # Live feed runs on a different timeframe (1m) than the training data
        # (1h). They are kept in separate frames; bands for signals come only
        # from this rolling window of minute bars.
        self.live_data = None

    def strategy(self):
        print("Bollinger Bands")

    def __add_signal(self, data):
        data = data.apply(pd.to_numeric)
        data['Typical Price'] = ((data['High']) + (data['Low']) + (data['Close'])) / 3
        data['Moving Average'] = data['Typical Price'].rolling(window=20).mean()
        data['std'] = data['Typical Price'].rolling(window=20).std()
        data['Upper Band'] = data['Moving Average'] + (data['std'] * 2)
        data['Lower Band'] = data['Moving Average'] - (data['std'] * 2)
        return data

    def train_strategy(self, data):
        self.data = self.__add_signal(data.copy())

    def plot_data(self):
        plt.style.use('fivethirtyeight')
        fig = plt.figure(figsize=(12, 6))
        ax = fig.add_subplot(111)

        x_axis = self.data['Open time']

        ax.fill_between(x_axis, self.data['Upper Band'], self.data['Lower Band'], color='grey')

        ax.plot(x_axis, self.data['Typical Price'], color='blue', lw=2)
        ax.plot(x_axis, self.data['Moving Average'], color='black', lw=2)

        ax.set_title('Bollinger Band')
        ax.set_xlabel('Time (Unix Timestamp)')
        ax.set_ylabel('Price(USD)')
        ax.legend()
        plt.show()

    def add_new_data(self, data):
        # Bands are computed on minute bars only once 20 of them exist; the
        # first 19 live ticks yield no signal (rolling stats are NaN).
        # Seeding from the hourly training data would mix timeframes.
        if self.live_data is None:
            self.live_data = data.copy()
        else:
            self.live_data = pd.concat([self.live_data, data], sort=False)
        self.live_data = self.__add_signal(self.live_data.tail(20))
        return self.__generate_signal()

    def __generate_signal(self):
        last_row = self.live_data.iloc[-1]
        if last_row['High'] >= last_row['Upper Band']:
            return True, "sell", (last_row['Open'] + last_row['Close']) / 2
        if last_row['Low'] <= last_row['Lower Band']:
            return True, "buy", (last_row['Open'] + last_row['Close']) / 2
        return False, "", 0

    def data_len(self):
        return self.data.shape

    def price_at_end(self):
        last_row = self.live_data.iloc[-1]
        return (last_row['Open'] + last_row['Close']) / 2
