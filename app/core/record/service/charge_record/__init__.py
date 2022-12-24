from uuid import UUID

from app.core.record.payload import Request
from app.infrastructure.database.mysql.cqrs.record.command import insert_new_record
from app.util.type_changer.record import payload_to_dto, dto_to_model
from app.common.security.token import get_uid


def charge_record(token: str, request: Request.ChargeRecord):
    dto = payload_to_dto(
        UUID(get_uid(token)), request
    )

    record = dto_to_model(dto)

    insert_new_record(record)
