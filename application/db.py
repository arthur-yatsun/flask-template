from typing import Optional

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker, Session

from config import DBConfig


class DBEngine:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DBEngine, cls).__new__(cls)

        return cls._instance

    def __init__(self, config: Optional[DBConfig] = None):
        config = config or DBConfig()

        self._engine = self._create_engine(config)
        self._session_factory = self._create_session_maker(config)

    def _create_engine(self, config) -> engine:
        """Creates an engine depends on config"""

        return create_engine(
            url=config.DB_DSN,
            pool_size=config.POOL_SIZE,
            max_overflow=config.MAX_OVERFLOW,
            connect_args={
                "connect_timeout": config.CONNECTION_TIMEOUT,
            }
        )

    def _create_session_maker(self, config) -> sessionmaker:
        """Creates session factory"""

        return sessionmaker(
            bind=engine,
            autocommit=config.AUTO_COMMIT,
            autoflush=config.AUTO_FLUSH,
        )

    def get_engine(self) -> engine:
        """Method to get db engine"""

        return self._engine

    def create_session(self) -> Session:
        """Method to create db session"""

        session = self._session_factory()
        try:
            yield session
        except Exception as exc:
            session.close()
