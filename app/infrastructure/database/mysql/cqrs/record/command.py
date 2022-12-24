from app.infrastructure.database.mysql.cqrs import DAO
from app.infrastructure.database.mysql.model.record import Record


def insert_new_record(record: Record):
    with DAO.session_scope() as session:
        session.add(record)