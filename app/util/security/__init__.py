from functools import wraps

from app.util.security.token import get_role
from app.util.exception.custom import InvalidRoleException


def check_role(jwt_token: str, role_list: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if get_role(jwt_token) not in role_list:
                raise InvalidRoleException

            return func(*args, **kwargs)

        return wrapper
