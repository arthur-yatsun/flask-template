from typing import Optional

from pydantic import BaseSettings, PostgresDsn

from constants import Environment


class BaseConfig(BaseSettings):
    """Base application config"""

    ENV: Optional[Environment] = Environment.DEV
    DEBUG: Optional[bool] = True
    TESTING: Optional[bool] = True

    class Config:
        case_sensitive = True
        use_enum_values = True


class DBConfig(BaseSettings):
    """Class to store database configurations"""

    DB_DSN: PostgresDsn

    # engine config
    POOL_SIZE: Optional[int] = 10
    MAX_OVERFLOW: Optional[int] = -1  # no overflow
    CONNECTION_TIMEOUT: Optional[int] = 30

    # session config
    AUTO_COMMIT: Optional[bool] = False
    AUTO_FLUSH: Optional[bool] = False

    class Config:
        case_sensitive = True


class ApplicationConfig(BaseConfig, DBConfig):
    """Class to store application configurations"""

    SECRET_KEY: str
    APPLICATION_ROOT: Optional[str] = "/"
