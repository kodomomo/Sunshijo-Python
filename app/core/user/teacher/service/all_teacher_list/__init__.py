from app.infrastructure.database.mysql.cqrs.teacher.query import query_all_teacher


def get_all_teacher_list() -> list:
    return query_all_teacher()
