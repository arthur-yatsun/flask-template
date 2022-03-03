from enum import Enum


class Environment(Enum):
    """Available environments"""

    DEV = "dev"
    QA = "qa"
    PROD = "prod"
