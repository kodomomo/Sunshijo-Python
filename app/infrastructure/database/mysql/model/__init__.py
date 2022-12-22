from sqlalchemy.ext.declarative import declarative_base as __declarative_base

from app.infrastructure.database.mysql import MySQLConnector


Base = __declarative_base()


def create_all_table():
    from app.infrastructure.database.mysql.model.teacher import Teacher
    from app.infrastructure.database.mysql.model.record import Record
    from app.infrastructure.database.mysql.model.schedule import Schedule

    Base.metadata.create_all(MySQLConnector.engine)
