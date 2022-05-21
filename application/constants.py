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
    UAH = "UAH"

    @classmethod
    def get_currencies(cls) -> List:
        return [item.value for item in cls]


class HTTPMethods:
    GET = "GET"
    POST = "POST"


class TransactionFields:
    VALUE = "value"
    CURRENCY = "currency"
    DESCRIPTION = "description"
    CREATED_AT = "created_at"

