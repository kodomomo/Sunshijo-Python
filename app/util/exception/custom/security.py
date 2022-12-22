from typing import Optional
from fastapi import HTTPException


class InvalidRoleException(HTTPException):

    def __init__(self, detail: Optional[str] = None):
        if detail in [None, '', ' ']:
            detail = 'USER ROLE NOT VALID'

        self.detail = detail
        self.status_code = 403


class WrongPasswordException(HTTPException):

    def __init__(self, detail: Optional[str] = None):
        if detail in [None, '', ' ']:
            detail = 'WRONG PASSWORD'

        self.detail = detail
        self.status_code = 400


class WrongAuthCodeException(HTTPException):

    def __init__(self, detail: Optional[str] = None):
        if detail in [None, '', ' ']:
            detail = 'WRONG PASSWORD'

        self.detail = detail
        self.status_code = 400
