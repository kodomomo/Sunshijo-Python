from uuid import UUID
from datetime import datetime

from sqlalchemy.sql import update

from app.infrastructure.database.mysql.cqrs import DAO
from app.infrastructure.database.mysql.model.record import Record


def insert_new_record(record: Record):
    with DAO.session_scope() as session:
        session.add(record)


def update_record_react(record_id: UUID, react: bool):
    with DAO.session_scope() as session:
        session.execute(
            update(Record)
            .where(Record.record_id == record_id.bytes)
            .values(
                is_approved=react,
                approved_at=datetime.now()
            )
        )
