import os
import unittest
from os.path import join

from domain.accounts import Accounts
from infrastructure.local_persitence import LocalPersistence


class TestAccounts(unittest.TestCase):
    def test_view_all_returns_data(self):
        os.environ["DATA_PATH"] = join("..", "resources")
        accounts = Accounts(persistence=LocalPersistence())
        data = accounts.view_all()
