from app.infrastructure.database.mysql.cqrs import DAO
from app.infrastructure.database.mysql.model.teacher import Teacher
from app.common.exception.custom import Throws
from app.core.user.teacher.exception import TeacherNotFoundException, AlreadyExistTeacherAccountId


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
