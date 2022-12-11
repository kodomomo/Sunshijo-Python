from uuid import uuid4

from sqlalchemy import Column, CHAR, VARCHAR, DATE, BINARY

from app.util.dao.mysql import Base


class Schedule(Base):
    __tablename__ = 'tbl_schedule'

    schedule_id = Column('id', BINARY(16), primary_key=True, default=uuid4)
    grade = Column(CHAR(1), nullable=False)
    room = Column(CHAR(1), nullable=False)
    subject = Column(VARCHAR(20), nullable=False)
    sequence = Column(CHAR(1), nullable=False)
    day = Column(DATE, nullable=False)
    week_of_day = Column(CHAR(3), nullable=False)


def get_schedule_table_create_query():
    from sqlalchemy.schema import CreateTable

    return str(CreateTable(Schedule.__table__).compile())
