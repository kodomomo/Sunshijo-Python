from app.common.security.token import get_uid
from app.infrastructure.database.mysql.cqrs.record.query import query_my_not_approved_records


def get_my_record(token: str):
    teacher_id = get_uid(token)

    return query_my_not_approved_records(teacher_id)