from typing import Optional
from fastapi import HTTPException


class RecordNotFoundException(HTTPException):
    detail = 'RECORD NOT FOUND'
    status_code = 400

    def __init__(self, detail: Optional[str] = None):
        if detail not in [None, '', ' ']:
            self.detail = detail
