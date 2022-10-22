from pick import pick
from rich.console import Console

console = Console()


class Cli:
    def home(self):
        title = 'What would you like to do today?'
        options = ["Add Account", "Update Account", "View", "Exit"]
        option, _ = pick(options, title)
        self.select_options(option)

    def select_options(self, option: str):
        if option == "Add Account":
            option = self.add_account(option)

        if option == "Update Account":
            pass

        if option == "View":
            pass

        console.print(option)

    def add_account(self, option):
        title = "What type of account would you like to add?"
        options = ["Debit", "Credit", "Investment", "Back"]
        option, _ = pick(options, title)
        if option == "Back":
            self.home()

        account_name = self.set_account_name()
        self.set_fixed_rate()
        option = self.add_entry(option)

        return option

    def add_entry(self, option):
        title = "Would you like to add an entry now?"
        options = ["Yes", "No"]
        option, _ = pick(options, title)
        if option == "Yes":
            pass
        return option

    def set_fixed_rate(self):
        title = "Does this account have a fixed rate?"
        options = ["Yes", "No"]
        option, _ = pick(options, title)
        if option == "Yes":
            pass

    def set_account_name(self) -> str:
        account_name = ""
        while not account_name:
            account_name = console.input("Set an account name\n")

        return account_name


if __name__ == "__main__":
    Cli().home()
