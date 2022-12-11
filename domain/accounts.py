import datetime
from typing import List

import pandas
import pandas as pd
from pandas import DataFrame

from interfaces.persistence_interface import PersistenceInterface


class Accounts:
    def __init__(self, persistence: PersistenceInterface):
        self.persistence = persistence

    def view_all(self):
        accounts = self.get_accounts_list()
        all_accounts = None
        for account in accounts:
            account_name = account["account_name"]
            df = self.persistence.read_pkl_file(file_name=f"{account_name}.pkl")
            df = df.dropna()
            if not df.empty:
                df = df.rename(columns={"balance": account_name})
                df = df.set_index("date")
                if not isinstance(all_accounts, pd.DataFrame):
                    all_accounts = df
                    continue
                print("")
                all_accounts = all_accounts.join(df)
                all_accounts = all_accounts.fillna(0)
                pass


    def view_account(self, account_name: str):
        df = self.persistence.read_pkl_file(file_name=f"{account_name}.pkl")
        return df.to_dict(orient="records")

    def add_account(self, account_name: str, account_type: str, rate: float, fixed_rate: bool, date_rate_ends: datetime):
        table = {
            "account_name": account_name,
            "account_type": account_type,
            "rate": rate,
            "fixed_rate": fixed_rate,
            "date_rate_ends": date_rate_ends,
        }

        df = self.persistence.read_pkl_file(file_name="data.pkl")
        data = DataFrame([table])
        df = df.append(data)
        self.persistence.save_pkl_file(data=df, file_name="data.pkl")

        account = DataFrame()
        self.persistence.save_pkl_file(data=account, file_name=f"{account_name}.pkl")

    def get_accounts_list(self) -> List[dict]:
        df = self.persistence.read_pkl_file(file_name="data.pkl")
        res = df.to_dict(orient="records")
        return res

    def add_entry(self, account_name: str, balance: float, date: str):
        table = {
            "balance": balance,
            "date": date,
        }

        df = self.persistence.read_pkl_file(file_name=f"{account_name}.pkl")
        row = pandas.DataFrame([table])
        output = pandas.concat([df, row], ignore_index=True)
        self.persistence.save_pkl_file(data=output, file_name=f"{account_name}.pkl")
