from application.add_entry_command import AddEntryCommand
from domain.accounts import Accounts
from infrastructure.local_persitence import LocalPersistence


class AddEntryCommandHandler:
    def __init__(self, command: AddEntryCommand):
        self.command = command

    def add_entry(self):
        accounts = Accounts(persistence=LocalPersistence())
        accounts.add_entry(account_name=self.command.account_name, balance=self.command.balance, date=self.command.date)
