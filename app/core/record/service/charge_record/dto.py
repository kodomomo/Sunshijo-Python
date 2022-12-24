from uuid import UUID
from typing import Optional
from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class ChargeRecordDTO:
    origin_grade: str
    origin_class: str
    origin_date: date
    origin_subject: str
    origin_gradations: str
    origin_teacher_id: UUID

    new_grade: str
    new_class: str
    new_date: date
    new_subject: str
    new_gradations: str
    new_teacher_id: UUID

    is_approved: bool
    request_at: datetime
    approved_at: Optional[datetime] = None
