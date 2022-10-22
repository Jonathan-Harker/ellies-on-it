import unittest

from application.add_account_command import AddAccountCommand
from application.add_account_command_handler import AddAccountCommandHandler


class TestAddAccountCommandHandler(unittest.TestCase):
    def test_handler_writes_a_pkl_file(self):
        command = AddAccountCommand(
            account_name="test-account",
            account_type="debit",
            date_rate_ends=None,
            fixed_rate=None,
            rate=None
        )
        handler = AddAccountCommandHandler(command=command)

    def test_handler_updates_a_pkl_file(self):
        pass
