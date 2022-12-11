import os.path
import unittest
from os.path import join

import pandas

from application.add_account_command import AddAccountCommand
from application.add_account_command_handler import AddAccountCommandHandler
from infrastructure.local_persitence import LocalPersistence
from interfaces.persistence_interface import PersistenceInterface
from tests.doubles.persistence_spy import PersistenceSpy
from tests.test_config import TestConfig


class TestAddAccountCommandHandler(unittest.TestCase):
    def get_file_path(self) -> str:
        base_path = TestConfig.get_test_base_path()
        path = join(base_path, "resources", "data.pkl")
        os.environ["DATA_PATH"] = path
        return path

    def add_account(self, persistence: PersistenceInterface):
        command = AddAccountCommand(
            account_name="test-account",
            account_type="debit",
            date_rate_ends=None,
            fixed_rate=None,
            rate=None
        )
        persistence = persistence
        handler = AddAccountCommandHandler(command=command, persistence=persistence)
        handler.add_account()

    def test_handler_writes_a_pkl_file(self):
        path = self.get_file_path()
        self.add_account(LocalPersistence())
        self.assertTrue(os.path.isfile(path))
        os.remove(path)

    def test_handler_writes_file_with_correct_data(self):
        spy = PersistenceSpy()
        self.add_account(spy)

        df = spy.call_stack[0]["called_with"]["data"]
        records = df.to_dict(orient="records")

        self.assertIsInstance(df, pandas.DataFrame)
        self.assertEqual(len(df), 1)
        self.assertEqual(records[0]["account_name"], "test-account")
        self.assertEqual(records[0]["account_type"], "debit")

    def test_handler_updates_a_pkl_file_when_adding_2_accounts(self):
        spy = PersistenceSpy()
        self.add_account(spy)
        self.add_account(spy)

        df = spy.call_stack[1]["called_with"]["data"]
        self.assertEqual(len(df), 2)
