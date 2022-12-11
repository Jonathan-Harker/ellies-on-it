import os

import pandas
import pandas as pd

from interfaces.persistence_interface import PersistenceInterface


class LocalPersistence(PersistenceInterface):
    def read_pkl_file(self) -> pandas.DataFrame:
        df = pandas.DataFrame([{}])
        return df

    def save_pkl_file(self, data: pandas.DataFrame) -> None:
        df = pd.DataFrame()
        path = os.environ["DATA_PATH"]
        pandas.to_pickle(df, path)
