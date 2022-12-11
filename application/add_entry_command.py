from dataclasses import dataclass


@dataclass
class AddEntryCommand:
    account_name: str
    date: str
    balance: float
