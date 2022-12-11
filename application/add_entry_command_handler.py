from application.add_entry_command import AddEntryCommand


class AddEntryCommandHandler:
    def __init__(self, command: AddEntryCommand):
        self.command = command
