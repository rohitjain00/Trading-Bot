from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def strategy(self):
        pass

    @abstractmethod
    def train_strategy(self, data):
        pass

    @abstractmethod
    def add_new_data(self, data):
        pass
