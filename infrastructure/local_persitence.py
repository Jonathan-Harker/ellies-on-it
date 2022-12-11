import os
from os.path import join

import pandas
import pandas as pd

from interfaces.persistence_interface import PersistenceInterface


class LocalPersistence(PersistenceInterface):
    def read_pkl_file(self, file_name: str) -> pandas.DataFrame:
        path = os.environ["DATA_PATH"]
        file_path = join(path, file_name)
        df = pandas.DataFrame([{}])
        if os.path.isfile(file_path):
            df = pandas.read_pickle(file_path)
        return df

    def save_pkl_file(self, data: pandas.DataFrame, file_name: str) -> None:
        path = os.environ["DATA_PATH"]
        file_path = join(path, file_name)
        pandas.to_pickle(data, file_path)
