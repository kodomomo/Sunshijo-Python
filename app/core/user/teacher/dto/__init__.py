from pydantic import BaseModel


class Request:
    class SignIn(BaseModel):
        accountId: str
        password: str
