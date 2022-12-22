from typing import Optional
from fastapi import HTTPException


class TeacherNotFoundException(HTTPException):

    def __init__(self, detail: Optional[str] = None):
        if detail in [None, '', ' ']:
            detail = 'DATE PRERIOD IS NOT WEEK'

        self.detail = detail
        self.status_code = 400
