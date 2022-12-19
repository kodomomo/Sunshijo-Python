from app.util.dao.mysql import dao
from app.util.dao.mysql.teacher import Teacher


def query_teacher_by_account_id(account_id: str) -> Teacher:
    with dao.session_scope() as session:
        return session.query(Teacher). \
            filter(Teacher.account_id == account_id).one()
