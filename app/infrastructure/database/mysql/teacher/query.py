from app.infrastructure.database.mysql import dao
from app.infrastructure.database.mysql.teacher import Teacher
from app.common.exception.custom import Throws
from app.common.exception.custom.models.teacher import TeacherNotFoundException


@Throws.not_found_exception(TeacherNotFoundException)
def query_teacher_by_account_id(account_id: str) -> Teacher:
    with dao.session_scope() as session:
        return session.query(Teacher). \
            filter(Teacher.account_id == account_id).one()
