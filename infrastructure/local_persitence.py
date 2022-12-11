import os

import pandas
import pandas as pd

from interfaces.persistence_interface import PersistenceInterface


class LocalPersistence(PersistenceInterface):
    def read_pkl_file(self) -> pandas.DataFrame:
        path = os.environ["DATA_PATH"]
        df = pandas.DataFrame([{}])
        if os.path.isfile(path):
            df = pandas.read_pickle(path)
        return df

    def save_pkl_file(self, data: pandas.DataFrame) -> None:
        path = os.environ["DATA_PATH"]
        pandas.to_pickle(data, path)
