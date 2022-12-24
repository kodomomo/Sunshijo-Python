from uuid import UUID
from dataclasses import dataclass

from pydantic import BaseModel

from app.config import Config

Config = Config.Regrex


class Request:
    class SignUp(BaseModel):
        auth_code: UUID
        account_id: str  # constr()
        password: str  # constr() TODO
        name: str
        work_place: str
        subject: str

        # @validator('account_id')
        # def check_account_id(cls, v):
        #     if not re.fullmatch(Config.REGREX_ID, v):
        #         raise AccountIdRegrexException
        #     return v
        #
        # @validator('password')
        # def check_password(cls, v):
        #     if not re.fullmatch(Config.REGREX_PASSWORD, v):
        #         raise PasswordRegrexException
        #     return v

    class SignIn(BaseModel):
        account_id: str
        password: str


class Response:
    @dataclass(frozen=True)
    class BothToken:
        access_token: str
        refresh_token: str
