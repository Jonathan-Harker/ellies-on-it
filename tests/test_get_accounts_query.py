import unittest

import pandas

from application.add_account_command import AddAccountCommand
from application.add_account_command_handler import AddAccountCommandHandler
from domain.accounts import Accounts
from interfaces.persistence_interface import PersistenceInterface


class PersistenceSpy(PersistenceInterface):
    def __init__(self):
        self.df = pandas.DataFrame()

    def save_pkl_file(self, data: pandas.DataFrame) -> None:
        self.df = data

    def read_pkl_file(self) -> pandas.DataFrame:
        return self.df


class TestGetAccountsQuery(unittest.TestCase):
    def test_get_accounts_returns_accounts_list(self):
        add_account_command = AddAccountCommand(
            account_name="TEST-NAME",
            account_type="Debit",
            fixed_rate=True,
            rate=3,
            date_rate_ends=None,
        )
        spy = PersistenceSpy()
        add_account_handler = AddAccountCommandHandler(command=add_account_command, persistence=spy)
        add_account_handler.add_account()

        Accounts(command=None, persistence=spy).get_accounts_list()
        self.assertIsInstance(spy.read_pkl_file(), pandas.DataFrame)
