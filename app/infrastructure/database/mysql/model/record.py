from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKeyConstraint, VARCHAR, BINARY, DATETIME, CHAR, DATE, BOOLEAN

from app.infrastructure.database.mysql.model import Base
from app.infrastructure.database.mysql.model.schedule import Schedule
from app.infrastructure.database.mysql.model.teacher import Teacher


class Record(Base):
    __tablename__ = 'tbl_record'

    record_id = Column('id', BINARY(16), primary_key=True)
    request_at = Column(DATETIME, nullable=False)
    react_at = Column(DATETIME, nullable=True)
    is_approved = Column(BOOLEAN, nullable=False, default=False)

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
            [request_teacher],
            [Teacher.teacher_id]
        ),
        ForeignKeyConstraint(
            [approved_teacher],
            [Teacher.teacher_id]
        ),
        ForeignKeyConstraint(
            [origin_grade, origin_class, origin_gradations, origin_day],
            [Schedule.grade, Schedule.class_num, Schedule.gradations, Schedule.day_at],
        ),
        ForeignKeyConstraint(
            [new_grade, new_class, new_gradations, new_day],
            [Schedule.grade, Schedule.class_num, Schedule.gradations, Schedule.day_at],
        )
    )
