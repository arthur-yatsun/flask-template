from typing import Optional

from pydantic import BaseSettings

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

    DB_DSN: str
    DEFAULT_DB_CONNECTION_TIMEOUT: Optional[int] = 30
    AUTO_COMMIT: Optional[bool] = False
    AUTO_FLUSH: Optional[bool] = False

    class Config:
        case_sensitive = True


class ApplicationConfig(BaseConfig, DBConfig):
    """Class to store application configurations"""

    SECRET_KEY: str
    APPLICATION_ROOT: Optional[str] = "/"
