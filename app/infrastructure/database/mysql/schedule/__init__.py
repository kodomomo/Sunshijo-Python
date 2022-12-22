from sqlalchemy import Column, CHAR, VARCHAR, DATE, PrimaryKeyConstraint

from app.infrastructure.database.mysql import Base


class Schedule(Base):
    __tablename__ = 'tbl_schedule'

    grade = Column('grade', CHAR(1), nullable=False)
    class_num = Column('class_num', CHAR(1), nullable=False)
    name = Column('name', VARCHAR(25), nullable=False)
    gradations = Column('gradations', CHAR(1), nullable=False)
    day_at = Column('day_at', DATE, nullable=False)
    week_of_day = Column(CHAR(3), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint(grade, class_num, name, gradations, day_at),
        {}
    )
