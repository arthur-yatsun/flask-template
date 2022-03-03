from enum import Enum


class Environment(Enum):
    """Available environments"""

    DEV = "dev"
    QA = "qa"
    PROD = "prod"


class Currency(Enum):
    """Available currency"""

    USD = "usd"
    EUR = "euro"
    RUB = "rub"
