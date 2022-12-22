from sqlalchemy.engine import Engine

from sqlalchemy.orm import sessionmaker, scoped_session

from app.config import Config


class MySQLInitializer:

    @staticmethod
    def _create_engine() -> Engine:
        from sqlalchemy import create_engine

        return create_engine(
            url=Config.DataBase.URL,
            encoding="utf-8",
            pool_recycle=3600,
            pool_size=20,
            max_overflow=20,
            pool_pre_ping=True
        )

    @staticmethod
    def _create_session(engine: Engine) -> scoped_session:
        return scoped_session(
            sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)
        )


class MySQLConnector(MySQLInitializer):
    engine = MySQLInitializer._create_engine()
    session = MySQLInitializer._create_session(engine)
