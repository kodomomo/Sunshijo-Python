from typing import Optional
from fastapi import HTTPException


class AccountIdRegrexException(HTTPException):
    status_code = 400
    detail = 'ACCOUNT ID NOT PASS REGREX'

    def __init__(self, detail: Optional[str] = None):
        if detail not in [None, '', ' ']:
            self.detail = detail


class PasswordRegrexException(HTTPException):
    status_code = 400
    detail = 'PASSWORD NOT PASS REGREX'

    def __init__(self, detail: Optional[str] = None):
        if detail not in [None, '', ' ']:
            self.detail = detail
