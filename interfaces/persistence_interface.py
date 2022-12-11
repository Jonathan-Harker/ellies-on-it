from abc import ABC, abstractmethod

import pandas


class PersistenceInterface(ABC):
    @abstractmethod
    def save_pkl_file(self, data: pandas.DataFrame, file_name: str) -> None:
        pass

    @abstractmethod
    def read_pkl_file(self, file_name: str) -> pandas.DataFrame:
        pass
