from app.util.database.mysql import dao
from app.util.database.mysql.teacher import Teacher


def insert_new_teacher(teacher: Teacher):
    with dao.session_scope() as session:
        session.add(teacher)
