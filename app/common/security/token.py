from uuid import UUID
from jwt import encode, decode
from datetime import timedelta

from app.util import ktc_now
from app.config import Config
from app.core.user import Role

JWT = Config.JWT


def generate_access_token(user_id: UUID, role: Role):
    return encode(
        payload={
            'exp': ktc_now() + timedelta(hours=JWT.ACCESS_EXPIRE),
            'uid': str(user_id),
            'role': role,
            'type': JWT.ACCESS_NAME
        },
        key=JWT.SECRET_KEY,
        algorithm=JWT.ALGORITHM
    )


def generate_refresh_token(user_id: UUID):
    return encode(
        payload={
            'exp': ktc_now() + timedelta(hours=JWT.REFRESH_EXPIRE),
            'uid': str(user_id),
            'type': JWT.REFRESH_NAME
        },
        key=JWT.SECRET_KEY,
        algorithm=JWT.ALGORITHM
    )


def _decode_jwt(jwt_token: str):
    return decode(
        jwt=jwt_token,
        key=JWT.SECRET_KEY,
        algorithms=JWT.ALGORITHM
    )


def get_uid(jwt_token: str):
    return _decode_jwt(jwt_token)['uid']


def get_role(jwt_token: str):
    return _decode_jwt(jwt_token)['role']


def is_access_token(jwt_token: str):
    return _decode_jwt(jwt_token)['type'] == JWT.ACCESS_NAME


def is_refresh_token(jwt_token: str):
    print(_decode_jwt(jwt_token)['type'], JWT.REFRESH_NAME)
    return _decode_jwt(jwt_token)['type'] == JWT.REFRESH_NAME
