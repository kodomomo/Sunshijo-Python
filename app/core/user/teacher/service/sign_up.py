from uuid import UUID

from app.config import Config
from app.util.exception.custom.security import WrongAuthCodeException

Config = Config.Auth


def sign_up(auth_code: UUID, account_id: str, password: str):

    if not Config.AUTH_CODE == auth_code:
        raise WrongAuthCodeException

