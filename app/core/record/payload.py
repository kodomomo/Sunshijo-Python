from datetime import date
from uuid import UUID

from pydantic.main import BaseModel


class Request:
    class ChargeRecord(BaseModel):
        origin_grade: str
        origin_class: str
        origin_date: date
        origin_subject: str
        origin_gradations: str

        new_grade: str
        new_class: str
        new_date: date
        new_subject: str
        new_gradations: str

        new_teacher_id: UUID

    class GetApprovedList(BaseModel):
        start_at: date
        end_at: date

    class ReactRecord(BaseModel):
        react: bool
        record_id: UUID
