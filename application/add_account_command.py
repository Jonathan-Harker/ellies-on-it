from dataclasses import dataclass
from datetime import datetime
from typing import Union


@dataclass
class AddAccountCommand:
    account_name: str
    account_type: str
    fixed_rate: Union[bool, None]
    rate: Union[float, None]
    date_rate_ends: Union[datetime, None]
