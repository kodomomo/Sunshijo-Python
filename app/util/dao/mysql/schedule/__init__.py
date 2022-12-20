from uuid import uuid4

from sqlalchemy import Column, CHAR, VARCHAR, DATE, BINARY, PrimaryKeyConstraint

from sqlalchemy.ext.hybrid import hybrid_property

from app.util.dao.mysql import Base


class Schedule(Base):
    __tablename__ = 'tbl_schedule'

    grade = Column('grade', CHAR(1), nullable=False)
    class_num = Column('class_num', CHAR(1), nullable=False)
    _name = Column('name', VARCHAR(25), nullable=False)
    gradations = Column('gradations', CHAR(1), nullable=False)
    day_at = Column('day_at', DATE, nullable=False)
    week_of_day = Column(CHAR(3), nullable=False)

    @hybrid_property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    __table_args__ = (
        PrimaryKeyConstraint(grade, class_num, _name, gradations, day_at),
        {}
    )
