from application.add_account_command import AddAccountCommand
from domain.accounts import Accounts
from interfaces.persistence_interface import PersistenceInterface


class AddAccountCommandHandler:
    def __init__(self, command: AddAccountCommand, persistence: PersistenceInterface):
        self.command = command
        self.persistence = persistence

    def add_account(self):
        accounts = Accounts(persistence=self.persistence, command=self.command)
        accounts.add_account()
