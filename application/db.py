from typing import Optional

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker

from config import DBConfig


class DBEngine:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DBEngine, cls).__new__(cls)

        return cls._instance

    def __init__(self, config: Optional[DBConfig] = None):
        self.config = config or DBConfig()
        self._engine = self._create_engine(self.config)

        self.session_factory = self._create_session_maker()

    def _create_engine(self, config) -> engine:
        """Method to create an engine depends on config"""

        return create_engine(
            url=config.DB_DSN,
            connect_args={
                "connect_timeout": self.config.DEFAULT_DB_CONNECTION_TIMEOUT,
            }
        )

    def _create_session_maker(self) -> sessionmaker:
        return sessionmaker(
            bind=engine,
            autocommit=self.config.AUTO_COMMIT,
            autoflush=self.config.AUTO_FLUSH,
        )

    def get_engine(self) -> engine:
        """Method to get db engine"""

        return self._engine

    def create_session(self):
        """Method to create db session"""

        session = self.session_factory()
        try:
            yield session
        except Exception as exc:
            session.close()
