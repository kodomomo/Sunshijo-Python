from datetime import datetime
from uuid import UUID, uuid4

from app.core.record.payload import Request
from app.core.record.service.charge_record.dto import ChargeRecordDTO
from app.infrastructure.database.mysql.model.record import Record


# is_approved, request_at TODO
def payload_to_dto(origin_teacher_id: UUID, request: Request.ChargeRecord):
    return ChargeRecordDTO(
        origin_grade=request.origin_grade,
        origin_class=request.origin_class,
        origin_date=request.origin_date,
        origin_subject=request.origin_subject,
        origin_gradations=request.origin_gradations,
        origin_teacher_id=origin_teacher_id,

        new_grade=request.new_grade,
        new_class=request.new_class,
        new_date=request.new_date,
        new_subject=request.new_subject,
        new_gradations=request.new_gradations,
        new_teacher_id=request.new_teacher_id,

        is_approved=False,
        request_at=datetime.now()
    )


def dto_to_model(dto: ChargeRecordDTO):
    return Record(
        record_id=uuid4().bytes,
        is_approved=dto.is_approved,
        request_at=dto.request_at,
        react_at=None,

        request_teacher=dto.origin_teacher_id.bytes,
        approved_teacher=dto.new_teacher_id.bytes,

        origin_grade=dto.origin_grade,
        origin_class=dto.origin_class,
        origin_name=dto.origin_subject,
        origin_gradations=dto.origin_gradations,
        origin_day=dto.origin_date,

        new_grade=dto.new_grade,
        new_class=dto.new_class,
        new_name=dto.new_subject,
        new_gradations=dto.new_gradations,
        new_day=dto.new_date
    )
