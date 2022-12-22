from sqlalchemy.orm import Session
from contextlib import contextmanager

from app.infrastructure.database.mysql import MySQLConnector


class DAO:

    @staticmethod
    @contextmanager
    def session_scope() -> Session:
        try:
            yield MySQLConnector.session
            MySQLConnector.session.commit()

        except:
            MySQLConnector.session.rollback()

        finally:
            MySQLConnector.session.close()

    @staticmethod
    @contextmanager
    def execute_query():
        yield MySQLConnector.engine.execute
