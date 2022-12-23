from typing import Optional
from fastapi import HTTPException


class InvalidRoleException(HTTPException):
    detail = 'USER ROLE NOT VALID'
    status_code = 403

    def __init__(self, detail: Optional[str] = None):
        if detail not in [None, '', ' ']:
            detail = detail


class WrongPasswordException(HTTPException):

    def __init__(self, detail: Optional[str] = None):
        if detail in [None, '', ' ']:
            detail = 'WRONG PASSWORD'

        self.detail = detail
        self.status_code = 400


class WrongAuthCodeException(HTTPException):

    def __init__(self, detail: Optional[str] = None):
        if detail in [None, '', ' ']:
            detail = 'WRONG AUTH CODE'

        self.detail = detail
        self.status_code = 400


class InvalidJwtTokenException(HTTPException):
    detail = 'JWT TOKEN IS NOT VALID'
    status_code = 401

    def __init__(self, detail: Optional[str] = None):
        if detail not in [None, '', ' ']:
            detail = detail
