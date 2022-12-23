from typing import Optional
from fastapi import HTTPException


class DatePeriodIsNotWeekException(HTTPException):
    status_code = 400
    detail = 'DATE PERIOD IS NOT WEEK'

    def __init__(self, detail: Optional[str] = None):
        if detail not in [None, '', ' ']:
            self.detail = detail


class ScheduleNotFoundException(HTTPException):
    status_code = 400
    detail = 'SCHEDULE NOT FOUND'

    def __init__(self, detail: Optional[str] = None):
        if detail not in [None, '', ' ']:
            self.detail = detail

