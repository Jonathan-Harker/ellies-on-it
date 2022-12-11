import os
import time
from os.path import join

from pick import pick
from rich.console import Console

from application.add_account_command import AddAccountCommand
from application.add_account_command_handler import AddAccountCommandHandler
from application.add_entry_command import AddEntryCommand
from application.add_entry_command_handler import AddEntryCommandHandler
from domain.accounts import Accounts
from infrastructure.local_persitence import LocalPersistence

console = Console()


class Cli:
    def __init__(self):
        base = os.path.dirname(os.path.realpath(__file__))
        os.environ["DATA_PATH"] = join(base, "resources")
        self.date = None

    def home(self):
        title = 'What would you like to do today?'
        options = ["Update Account", "View", "View All", "Add Account", "Exit"]
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

        if option == "View All":
            self.view_all()
            self.home()

    def view_all(self):
        accounts = Accounts(persistence=LocalPersistence())
        data = accounts.view_all()

    def update_account(self):
        accounts = Accounts(persistence=LocalPersistence())
        account_list = accounts.get_accounts_list()
        title = "Which account would you like to update?"
        option, _ = pick(account_list, title)
        self.add_entry(account_name=option["account_name"])
        self.home()

    def view_account(self):
        accounts = Accounts(persistence=LocalPersistence())
        account_list = accounts.get_accounts_list()
        title = "Which account would you like to view?"
        option, _ = pick(account_list, title)
        data = accounts.view_account(option["account_name"])
        for row in data:
            print(row)
        console.input("Press any key to continue")
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
        balance = float(console.input("Set the account balance\n"))
        confirm = "No"
        if self.date:
            title = f"The current date set is {self.date}. Would you like to continue with this date?"
            options = ["Yes", "No"]
            confirm, _ = pick(options, title)

        if confirm == "No":
            day_of_month = console.input("Which day of the month? (1 - 31)\n")
            month = console.input("Which month (1 - 12)\n")
            year = console.input("Which year? (e.g. 2022)")
            date = f"{day_of_month}/{month}/{year}"
            self.date = date

        command = AddEntryCommand(
            account_name=account_name,
            balance=balance,
            date=self.date,
        )

        handler = AddEntryCommandHandler(command=command)
        handler.add_entry()
        self.home()

    def set_fixed_rate(self) -> dict:
        title = "Does this account have a fixed rate?"
        options = ["Yes", "No"]
        option, _ = pick(options, title)
        rate = console.input("Set rate\n")
        return {"rate": float(rate), "fixed": option == "Yes"}

    def set_account_name(self) -> str:
        account_name = ""
        while not account_name:
            account_name = console.input("Set an account name\n")

        return account_name


if __name__ == "__main__":
    Cli().home()
