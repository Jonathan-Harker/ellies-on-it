import os
import time
from os.path import join

from pick import pick
from rich.console import Console

from application.add_account_command import AddAccountCommand
from application.add_account_command_handler import AddAccountCommandHandler
from domain.accounts import Accounts
from infrastructure.local_persitence import LocalPersistence

console = Console()


class Cli:
    def __init__(self):
        base = os.path.dirname(os.path.realpath(__file__))
        os.environ["DATA_PATH"] = join(base, "resources")

    def home(self):
        title = 'What would you like to do today?'
        options = ["Add Account", "Update Account", "View", "Exit"]
        option, _ = pick(options, title)
        self.select_options(option)

    def select_options(self, option: str):
        if option == "Exit":
            exit(0)

        if option == "Add Account":
            option = self.add_account()
            self.home()

        if option == "Update Account":
            self.update_account()
            self.home()

        if option == "View":
            self.view_account()
            self.home()

    def update_account(self):
        accounts = Accounts(command=None, persistence=LocalPersistence())
        account_list = accounts.get_accounts_list()
        title = "Which account would you like to update?"
        option, _ = pick(account_list, title)
        self.add_entry(account_name=option["account_name"])
        self.home()

    def view_account(self):
        accounts = Accounts(command=None, persistence=LocalPersistence())
        account_list = accounts.get_accounts_list()
        title = "Which account would you like to view?"
        option, _ = pick(account_list, title)
        print("Not implemented yet")
        time.sleep(3)
        self.home()

    def add_account(self):
        title = "What type of account would you like to add?"
        options = ["Debit", "Credit", "Investment", "Back"]
        option, _ = pick(options, title)
        if option == "Back":
            self.home()

        account_name = self.set_account_name()
        rate = self.set_fixed_rate()
        command = AddAccountCommand(
            account_name=account_name,
            account_type=option,
            date_rate_ends=None,
            fixed_rate=rate["fixed"],
            rate=rate["rate"],
        )
        handler = AddAccountCommandHandler(command=command, persistence=LocalPersistence())
        handler.add_account()

        title = "Would you like to add an entry now?"
        options = ["Yes", "No"]
        option, _ = pick(options, title)

        if option == "Yes":
            self.add_entry(account_name=account_name)

        self.home()

    def add_entry(self, account_name: str):
        command = AddEntryCommand()
        handler = AddEntryCommandHandler(command=command)
        self.home()

    def set_fixed_rate(self) -> dict:
        title = "Does this account have a fixed rate?"
        options = ["Yes", "No"]
        option, _ = pick(options, title)
        rate = console.input("Set rate")
        return {"rate": float(rate), "fixed": option == "Yes"}

    def set_account_name(self) -> str:
        account_name = ""
        while not account_name:
            account_name = console.input("Set an account name\n")

        return account_name


if __name__ == "__main__":
    Cli().home()
