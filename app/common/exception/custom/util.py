from typing import Optional
from fastapi import HTTPException


class DatePeriodIsNotWeek(HTTPException):

    def __init__(self, detail: Optional[str] = None):
        if detail in [None, '', ' ']:
            detail = 'DATE PERIOD IS NOT WEEK: PERIOD BETWEEN MUST BE 7'

        self.detail = detail
        self.status_code = 400
