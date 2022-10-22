from application.add_account_command import AddAccountCommand


class AddAccountCommandHandler:
    def __init__(self, command: AddAccountCommand):
        self.command = command
