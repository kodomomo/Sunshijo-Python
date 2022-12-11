from sqlalchemy import Column, ForeignKey, VARCHAR, BINARY

from app.util.dao.mysql import Base


class Record(Base):
    __tablename__ = 'tbl_record'

    record_id = Column(BINARY(16), primary_key=True)
    note = Column(VARCHAR(255), nullable=True)

    want_teacher_id = Column(ForeignKey('tbl_teacher.id'), nullable=False)
    approve_teacher_id = Column(ForeignKey('tbl_teacher.id'), nullable=False)

    new_schedule_id = Column(ForeignKey('tbl_schedule.id'), nullable=False)
    origin_schedule_id = Column(ForeignKey('tbl_schedule.id'), nullable=False)


def get_create_record_table_sql():
    from sqlalchemy.schema import CreateTable

    return str(CreateTable(Record.__table__).compile())
