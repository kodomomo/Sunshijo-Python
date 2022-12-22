from uuid import UUID

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, BINARY, CHAR, VARCHAR

from app.infrastructure.database.mysql.model import Base


class Teacher(Base):
    __tablename__ = 'tbl_teacher'

    teacher_id = Column('id', BINARY(16), primary_key=True)
    account_id = Column(VARCHAR(15), nullable=False, unique=True)
    password = Column(CHAR(60), nullable=False)
    name = Column(CHAR(5), nullable=False)
    work_place = Column(VARCHAR(15), nullable=False)
    subject = Column(VARCHAR(15), nullable=False)

    @hybrid_property
    def id(self) -> UUID:
        if isinstance(self.teacher_id, UUID):
            return self.teacher_id

        elif isinstance(self.teacher_id, bytes):
            return UUID(bytes=self.teacher_id)
