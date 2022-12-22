from typing import Optional
from fastapi import HTTPException


class TeacherNotFoundException(HTTPException):

    def __init__(self, detail: Optional[str] = None):
        if detail in [None, '', ' ']:
            detail = 'TEACHER NOT FOUND'

        self.detail = detail
        self.status_code = 404