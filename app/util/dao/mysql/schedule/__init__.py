from uuid import uuid4

from sqlalchemy import Column, CHAR, VARCHAR, DATE, BINARY, PrimaryKeyConstraint

from app.util.dao.mysql import Base


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

if __name__ == '__main__':
    def get_schedule_table_create_query():
        from sqlalchemy.schema import CreateTable

        return str(CreateTable(Schedule.__table__).compile())

    print(get_schedule_table_create_query())
