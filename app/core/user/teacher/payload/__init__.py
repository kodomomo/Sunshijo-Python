from pydantic import BaseModel
from dataclasses import dataclass


class Request:
    class SignIn(BaseModel):
        account_id: str
        password: str


class Response:

    @dataclass(frozen=True)
    class BothToken:
        access_token: str
        refresh_token: str
