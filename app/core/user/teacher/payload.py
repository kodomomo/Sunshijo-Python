import re
from uuid import UUID
from dataclasses import dataclass

from pydantic import BaseModel, constr
from pydantic.class_validators import validator

from app.common.exception.custom.regrex import AccountIdRegrexException, PasswordRegrexException
from app.config import Config

Config = Config.Regrex


class Request:
    class SignUp(BaseModel):
        auth_code: UUID
        account_id: constr()
        password: constr()
        name: str
        work_place: str
        subject: str

        @validator('account_id')
        def check_account_id(cls, value):
            if not re.fullmatch(Config.REGREX_ID, value):
                raise AccountIdRegrexException(detail='id는 7자에서 15자 이하로 가능합니다.')
            return value

        @validator('password')
        def check_password(cls, value):
            if not re.fullmatch(Config.REGREX_PASSWORD, value):
                raise PasswordRegrexException(detail='password는 7자에서 15자 이하이며, 중간 또는 마지막에만 특수기호가 올 수 있습니다.')
            return value

    class SignIn(BaseModel):
        account_id: str
        password: str


class Response:
    @dataclass(frozen=True)
    class BothToken:
        access_token: str
        refresh_token: str
