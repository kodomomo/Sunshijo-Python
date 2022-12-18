from sqlalchemy import Column, ForeignKeyConstraint, VARCHAR, BINARY, DATETIME, CHAR, DATE

from app.util.dao.mysql import Base
from app.util.dao.mysql.schedule import Schedule
from app.util.dao.mysql.teacher import Teacher


class Record(Base):
    __tablename__ = 'tbl_record'

    record_id = Column(BINARY(16), primary_key=True)
    note = Column(VARCHAR(255), nullable=True)
    request_at = Column(DATETIME, nullable=False)
    approved_at = Column(DATETIME, nullable=True)

    request_teacher = Column(BINARY(16), nullable=False)
    approved_teacher = Column(BINARY(16), nullable=False)

    origin_grade = Column(CHAR(1), nullable=False)
    origin_class = Column(CHAR(1), nullable=False)
    origin_name = Column(VARCHAR(25), nullable=False)
    origin_gradations = Column(CHAR(1), nullable=False)
    origin_day = Column(DATE, nullable=False)

    new_grade = Column(CHAR(1), nullable=False)
    new_class = Column(CHAR(1), nullable=False)
    new_name = Column(VARCHAR(25), nullable=False)
    new_gradations = Column(CHAR(1), nullable=False)
    new_day = Column(DATE, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            [origin_grade, origin_class, origin_name, origin_day, origin_gradations],
            [Schedule.grade, Schedule.class_num, Schedule.name, Schedule.day_at, Schedule.gradations]
        ),
        ForeignKeyConstraint(
            [new_grade, new_class, new_name, new_day, new_gradations],
            [Schedule.grade, Schedule.class_num, Schedule.name, Schedule.day_at, Schedule.gradations],
        ),
        ForeignKeyConstraint(
            [request_teacher],
            [Teacher.teacher_id]
        ),
        ForeignKeyConstraint(
            [approved_teacher],
            [approved_teacher]
        )
    )