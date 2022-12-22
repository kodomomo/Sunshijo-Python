from typing import Type
from fastapi import HTTPException

from functools import wraps


class Throws:
    @staticmethod
    def not_found_exception(exception: Type[HTTPException]):
        def decorator(func):
            def throw():
                raise exception

            @wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)

                return result if result is not None else throw()

            return wrapper

        return decorator

# Throws를 아예 Decorator로 사용할 수 있게 만들면, 함수 호출 때마다 객체가 생성되는 걸까?
