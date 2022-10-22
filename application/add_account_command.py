from dataclasses import dataclass
from datetime import datetime


@dataclass
class AddAccountCommand:
    account_name: str
    account_type: str
    fixed_rate: bool
    rate: float
    date_rate_ends: datetime
