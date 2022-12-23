from typing import Optional
from fastapi import HTTPException


class TeacherNotFoundException(HTTPException):
    detail = 'TEACHER NOT FOUND'
    status_code = 400

    def __init__(self, detail: Optional[str] = None):
        if detail not in [None, '', ' ']:
            self.detail = detail


class AlreadyExistTeacherAccountId(HTTPException):
    status_code = 409
    detail = 'TEACHER ID ALREADY EXIST'

    def __init__(self, detail: Optional[str] = None):
        if detail not in [None, '', ' ']:
            self.detail = detail
