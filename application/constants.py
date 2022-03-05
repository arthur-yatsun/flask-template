from enum import Enum
from typing import List


class Environment(Enum):
    """Available environments"""

    DEV = "dev"
    QA = "qa"
    PROD = "prod"


class Currency(Enum):
    """Available currency"""

    USD = "USD"
    EUR = "EUR"
    RUB = "RUB"

    @classmethod
    def get_currencies(cls) -> List:
        return [item.value for item in cls]
