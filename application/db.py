from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config import DBConfig

config = DBConfig()
engine = create_engine(config.DB_DSN, connection_args={
    "timeout": config.DEFAULT_DB_CONNECTION_TIMEOUT,
})

session_factory = sessionmaker(
    bind=engine,
    autocommit=config.AUTO_COMMIT,
    autoflush=config.AUTO_FLUSH,
)


def get_session() -> Session:
    session = session_factory()
    try:
        yield session
    except Exception as exc:
        session.close()
