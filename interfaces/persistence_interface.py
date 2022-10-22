from abc import ABC, abstractmethod

import pandas


class PersistenceInterface(ABC):
    @abstractmethod
    def save_pkl_file(self, data: pandas.DataFrame) -> None:
        pass

    @abstractmethod
    def read_pkl_file(self) -> pandas.DataFrame:
        pass
