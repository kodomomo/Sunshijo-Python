from pydantic import BaseModel

from datetime import date


class FillScheduleRequest(BaseModel):
    grade: int
    class_num: int
    start_date: date
    end_date: date
