from .Strategy import Strategy
import pandas as pd
import matplotlib.pyplot as plt


class BollingerBands(Strategy):
    def strategy(self):
        print("Bollinger Bands")

    def train_strategy(self, data):
        self.data = data.copy()
        self.data = self.data.apply(pd.to_numeric)
        self.data['Typical Price'] = ((self.data['High']) + (self.data['Low']) + (self.data['Close'])) / 3
        self.data['Moving Average'] = self.data['Typical Price'].rolling(window=20).mean()
        self.data['std'] = self.data['Typical Price'].rolling(window=20).std()
        self.data['Upper Band'] = self.data['Moving Average'] + (self.data['std'] * 2)
        self.data['Lower Band'] = self.data['Moving Average'] - (self.data['std'] * 2)

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
        pass
