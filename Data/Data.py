from abc import ABC, abstractmethod


class Data(ABC):
    @abstractmethod
    def data_from(self):
        pass

    @abstractmethod
    def get_train_data(self):
        pass

    @abstractmethod
    def get_new_data(self):
        pass
