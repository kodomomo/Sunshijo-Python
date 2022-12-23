from uuid import UUID

from sqlalchemy.sql import func
from app.infrastructure.database.mysql.cqrs import DAO
from app.infrastructure.database.mysql.model.teacher import Teacher
from app.common.exception.custom import Throws
from app.core.user.teacher.exception import TeacherNotFoundException, AlreadyExistTeacherAccountId


@Throws.not_found_exception(TeacherNotFoundException)
def query_teacher_by_id(teacher_id: str):
    with DAO.session_scope() as session:
        return session.query(Teacher)\
            .filter(Teacher.teacher_id == UUID(teacher_id).bytes) \
            .one()


@Throws.not_found_exception(TeacherNotFoundException)
def query_teacher_by_account_id(account_id: str) -> Teacher:
    with DAO.session_scope() as session:
        return session.query(Teacher). \
            filter(Teacher.account_id == account_id) \
            .one()


@Throws.already_exist(AlreadyExistTeacherAccountId)
def teacher_account_exist(account_id: str):
    with DAO.session_scope() as session:
        return session.query(Teacher.account_id) \
            .filter(Teacher.account_id == account_id) \
            .scalar()


def query_all_teacher():
    with DAO.session_scope() as session:
        return session.query(
            func.BIN_TO_UUID(Teacher.teacher_id).label('teacher_id'),
            Teacher.name,
            Teacher.work_place,
            Teacher.subject,
        ).all()
