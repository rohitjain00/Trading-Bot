from .Strategy import Strategy
import pandas as pd
import matplotlib.pyplot as plt


class BollingerBands(Strategy):
    def strategy(self):
        print("Bollinger Bands")

    def __add_signal(self):
        self.data = self.data.apply(pd.to_numeric)
        self.data['Typical Price'] = ((self.data['High']) + (self.data['Low']) + (self.data['Close'])) / 3
        self.data['Moving Average'] = self.data['Typical Price'].rolling(window=20).mean()
        self.data['std'] = self.data['Typical Price'].rolling(window=20).std()
        self.data['Upper Band'] = self.data['Moving Average'] + (self.data['std'] * 2)
        self.data['Lower Band'] = self.data['Moving Average'] - (self.data['std'] * 2)

    def train_strategy(self, data):
        self.data = data.copy()
        self.__add_signal()

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
        self.data = self.data.append(data, sort=False)
        self.__add_signal()
        return self.__generate_signal()

    def __generate_signal(self):
        last_row = self.data.iloc[-1]
        if last_row['High'] >= last_row['Upper Band']:
            return True, "sell", (last_row['Open'] + last_row['Close']) / 2
        if last_row['Low'] <= last_row['Lower Band']:
            return True, "buy", (last_row['Open'] + last_row['Close']) / 2

        return False, "", 0

    def data_len(self):
        return self.data.shape
