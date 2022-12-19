from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, BINARY, CHAR, VARCHAR

from app.util.dao.mysql import Base


class Teacher(Base):
    __tablename__ = 'tbl_teacher'

    __teacher_id = Column('id', BINARY(16), primary_key=True)
    account_id = Column(VARCHAR(15), nullable=False, unique=True)
    password = Column(CHAR(60), nullable=False)
    name = Column(CHAR(5), nullable=False)
    work_place = Column(VARCHAR(15), nullable=False)
    allocated_subject = Column(VARCHAR(15), nullable=False)

    @hybrid_property
    def id_column(self):
        return self.__teacher_id

    @hybrid_property
    def teacher_id(self):
        from uuid import UUID

        if not isinstance(self.__teacher_id, bytes):
            response = self.__teacher_id

        else:
            response = UUID(bytes=self.__teacher_id)

        return response
