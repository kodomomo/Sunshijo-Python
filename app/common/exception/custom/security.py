from typing import Optional
from fastapi import HTTPException


class InvalidRoleException(HTTPException):
    detail = 'USER ROLE NOT VALID'
    status_code = 403

    def __init__(self, detail: Optional[str] = None):
        if detail not in [None, '', ' ']:
            self.detail = detail


class WrongPasswordException(HTTPException):
    status_code = 400
    detail = 'WRONG PASSWORD'

    def __init__(self, detail: Optional[str] = None):
        if detail not in [None, '', ' ']:
            self.detail = detail


class WrongAuthCodeException(HTTPException):
    status_code = 400
    detail = 'WRONG AUTH CODE'

    def __init__(self, detail: Optional[str] = None):
        if detail not in [None, '', ' ']:
            self.detail = detail


class InvalidJwtTokenException(HTTPException):
    detail = 'JWT TOKEN IS NOT VALID'
    status_code = 401

    def __init__(self, detail: Optional[str] = None):
        if detail not in [None, '', ' ']:
            detail = detail
