from application.add_account_command import AddAccountCommand
from domain.accounts import Accounts
from interfaces.persistence_interface import PersistenceInterface


class AddAccountCommandHandler:
    def __init__(self, command: AddAccountCommand, persistence: PersistenceInterface):
        self.command = command
        self.persistence = persistence

    def add_account(self):
        accounts = Accounts(persistence=self.persistence)
        accounts.add_account(
            account_name=self.command.account_name,
            account_type=self.command.account_type,
            date_rate_ends=self.command.date_rate_ends,
            fixed_rate=self.command.fixed_rate,
            rate=self.command.rate
        )
