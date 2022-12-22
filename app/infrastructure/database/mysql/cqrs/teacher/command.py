from app.infrastructure.database.mysql.cqrs import DAO
from app.infrastructure.database.mysql.model.teacher import Teacher


def insert_new_teacher(teacher: Teacher):
    with DAO.session_scope() as session:
        session.add(teacher)
