from typing import Type, Union
from fastapi import HTTPException

from functools import wraps


class Throws:

    @staticmethod
    def throw(exception: Union[Type[HTTPException], Exception]):
        raise exception

    @staticmethod
    def already_exist(exception: Type[HTTPException]):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if func(*args, **kwargs) is not None:
                    Throws.throw(exception)

            return wrapper

        return decorator

    @staticmethod
    def not_found_exception(exception: Type[HTTPException]):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)

                return result if result is not None else Throws.throw(exception)

            return wrapper

        return decorator

# Throws를 아예 Decorator로 사용할 수 있게 만들면, 함수 호출 때마다 객체가 생성되는 걸까?
