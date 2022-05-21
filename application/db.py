from contextlib import contextmanager
from typing import Optional

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker, Session

from config import DBConfig
from exceptions import BaseSessionError


class DBEngine:
    """Wrapper for db engine"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DBEngine, cls).__new__(cls)

        return cls._instance

    def __init__(self, config: Optional[DBConfig] = None):
        config = config or DBConfig()

        self.db_engine = self.get_engine(config)
        self.session_maker = self.get_session_maker(config, self.db_engine)

    @contextmanager
    def session_scope(self) -> Session:
        """Method to get db session"""

        with self.session_maker() as session:
            try:
                yield session
                session.commit()
            except Exception as err:
                session.rollback()
                # raise BaseSessionError(f"DB error occurred: {err}")
            finally:
                session.close()

    @staticmethod
    def get_engine(config) -> engine:
        """Creates an engine depends on config"""

        return create_engine(
            url=config.DB_DSN,
            pool_size=config.POOL_SIZE,
            max_overflow=config.MAX_OVERFLOW,
            connect_args={
                "connect_timeout": config.CONNECTION_TIMEOUT,
            }
        )

    @staticmethod
    def get_session_maker(config: DBConfig, db_engine: engine) -> sessionmaker:
        """Creates session factory"""

        return sessionmaker(
            bind=db_engine,
            autocommit=config.AUTO_COMMIT,
            autoflush=config.AUTO_FLUSH,
        )
