from uuid import UUID
from app.util.type_changer import date

from sqlalchemy.sql import func, select
from sqlalchemy.orm import aliased

from app.common.exception.custom import Throws
from app.core.record.exception import RecordNotFoundException
from app.infrastructure.database.mysql.cqrs import DAO
from app.infrastructure.database.mysql.model.record import Record
from app.infrastructure.database.mysql.model.teacher import Teacher


@Throws.not_found_exception(RecordNotFoundException)
def query_record_by_id(record_id: UUID):
    with DAO.session_scope() as session:
        return session.query(Record) \
            .filter(Record.record_id == record_id.bytes) \
            .one()


def query_approved_record_by_date(start_at: date, end_at: date):
    new_teacher = aliased(Teacher, name='new_teacher')
    with DAO.session_scope() as session:
        return session.query(
            func.BIN_TO_UUID(Record.record_id).label('record_id'),
            Record.origin_grade,
            Record.origin_class,
            Record.origin_name,
            Record.origin_gradations,
            Record.origin_day,
            Teacher.name.label('origin_teacher_name'),
            Record.new_grade,
            Record.new_class,
            Record.new_name,
            Record.new_day,
            Record.new_gradations,
            new_teacher.name.label('new_teacher_name')
        ).filter(
            Record.is_approved == True,
            start_at <= Record.request_at,
            Record.react_at <= end_at
        ).join(
            Teacher, Teacher.teacher_id == Record.request_teacher
        ).join(
            new_teacher, new_teacher.teacher_id == Record.approved_teacher
        ).all()


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
        ).filter(
            Record.is_approved == False,
            Record.approved_teacher == UUID(teacher_id).bytes,
        ).join(Teacher, Teacher.teacher_id == Record.request_teacher) \
            .all()
