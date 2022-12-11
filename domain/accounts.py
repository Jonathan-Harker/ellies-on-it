from typing import List

from pandas import DataFrame

from application.add_account_command import AddAccountCommand
from interfaces.persistence_interface import PersistenceInterface


class Accounts:
    def __init__(self, persistence: PersistenceInterface, command: AddAccountCommand):
        self.persistence = persistence
        self.command = command

    def add_account(self):
        table = {
            "account_name": self.command.account_name,
            "account_type": self.command.account_type,
            "rate": self.command.rate,
            "fixed_rate": self.command.fixed_rate,
            "date_rate_ends": self.command.date_rate_ends,
        }

        df = self.persistence.read_pkl_file(file_name="data.pkl")
        data = DataFrame([table])
        df = df.append(data)
        self.persistence.save_pkl_file(data=df, file_name="data.pkl")

        account = DataFrame()
        self.persistence.save_pkl_file(data=account, file_name=f"{self.command.account_name}.pkl")

    def get_accounts_list(self) -> List[dict]:
        df = self.persistence.read_pkl_file(file_name="data.pkl")
        res = df.to_dict(orient="records")
        return res
