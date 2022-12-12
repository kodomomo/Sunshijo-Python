from sqlalchemy import Column, BINARY, CHAR, VARCHAR

from app.util.dao.mysql import Base


class Teacher(Base):
    __tablename__ = 'tbl_teacher'

    teacher_id = Column('id', BINARY(16), primary_key=True)
    login_id = Column(VARCHAR(15), nullable=False, unique=True)
    password = Column(CHAR(60), nullable=False)
    name = Column(CHAR(5), nullable=False)
    work_place = Column(VARCHAR(15), nullable=False)
    management_subject = Column(VARCHAR(15), nullable=False)


def get_teacher_table_create_query():
    from sqlalchemy.schema import CreateTable

    return str(CreateTable(Teacher.__table__).compile())
