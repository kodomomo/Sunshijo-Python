from typing import Union, Type
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.common.security.token import get_role, check_token_expire
from app.common.exception.custom.security import InvalidRoleException, InvalidJwtTokenException
from fastapi.security import OAuth2PasswordBearer

from app.common.security import AuthProperties

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def initialize_token_security(app: FastAPI):
    def create_json_response(exception: Union[HTTPException, Type, HTTPException]):
        return JSONResponse(
            status_code=exception.status_code,
            content={
                'detail': exception.detail
            }
        )

    @app.middleware('http')
    async def authorization(request: Request, next_func):
        method = request.method
        path = request.scope.get('path')
        role_list = AuthProperties.role_list(path, method)

        if role_list is not None:

            prefix_jwt, suffix_jwt = request.headers.get('Authorization').split(' ')

            if prefix_jwt != 'Bearer':
                return create_json_response(InvalidJwtTokenException)

            if check_token_expire(suffix_jwt):
                return create_json_response(InvalidJwtTokenException('TOKEN HAS EXPIRED'))

            if get_role(suffix_jwt) not in role_list:
                return create_json_response(InvalidRoleException)

        return await next_func(request)
