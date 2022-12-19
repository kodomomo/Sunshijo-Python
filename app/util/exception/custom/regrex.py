from typing import Optional
from fastapi import HTTPException


class AccountIdRegrexException(HTTPException):

    def __init__(self, detail: Optional[str] = None):
        if detail in [None, '', ' ']:
            detail = 'ACCOUNT ID NOT PASS REGREX'

        self.detail = detail
        self.status_code = 400


class PasswordRegrexException(HTTPException):

    def __init__(self, detail: Optional[str] = None):
        if detail in [None, '', ' ']:
            detail = 'PASSWORD NOT PASS REGREX'

        self.detail = detail
        self.status_code = 400
