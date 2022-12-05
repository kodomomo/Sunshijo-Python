from sqlalchemy.ext.declarative import declarative_base as __declarative_base

from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from sqlalchemy.orm import sessionmaker, scoped_session, Session

from app.config import Config


class DAO:

    def __init__(self):
        self.__engine = self.__create_engine()
        self.__session = self.__create_session(self.__engine)()

    @staticmethod
    def __create_engine() -> Engine:
        return create_engine(
            url=Config.DataBase.URL,
            encoding="utf-8",
            pool_recycle=3600,
            pool_size=20,
            max_overflow=20,
            pool_pre_ping=True
        )

    @staticmethod
    def __create_session(engine: Engine) -> scoped_session:
        return scoped_session(
            sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)
        )

    @contextmanager
    def session_scope(self) -> Session:
        try:
            yield self.__session
            self.__session.commit()
        except:
            self.__session.rollback()
        finally:
            self.__session.close()

    @contextmanager
    def execute_query(self):
        yield self.__engine.execute


dao = DAO()
Base = __declarative_base()
