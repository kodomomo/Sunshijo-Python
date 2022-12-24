from uuid import UUID

from sqlalchemy.sql import func

from app.infrastructure.database.mysql.cqrs import DAO
from app.infrastructure.database.mysql.model.record import Record
from app.infrastructure.database.mysql.model.teacher import Teacher


def query_my_not_approved_records(teacher_id: str):
    with DAO.session_scope() as session:
        return session.query(
            func.BIN_TO_UUID(Record.record_id).label('record_id'),
            Record.origin_grade,
            Record.origin_class,
            Record.origin_gradations,
            Record.origin_day,
            Record.origin_name,
            Record.new_grade,
            Record.new_class,
            Record.new_gradations,
            Record.new_day,
            Record.new_name,
            Teacher.name
        ) \
            .filter(Record.approved_teacher == UUID(teacher_id).bytes)\
            .filter(Record.is_approved == False) \
            .join(Teacher, Teacher.teacher_id == Record.approved_teacher)\
            .all()
