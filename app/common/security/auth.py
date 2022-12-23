from typing import Union, Type
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.common.security.token import get_role
from app.common.exception.custom.security import InvalidRoleException, InvalidJwtTokenException
from fastapi.security import OAuth2PasswordBearer

from app.core.user import Role

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
        url = request.scope.get('path')
        prefix_jwt, suffix_jwt = request.headers.get('Authorization').split(' ')

        if prefix_jwt != 'Bearer':
            return create_json_response(InvalidJwtTokenException)

        if (url in authorization_url) and (get_role(suffix_jwt) not in role_list(url)):
            return create_json_response(InvalidRoleException)

        return await next_func(request)


def role_list(url: str):
    return authorization_url.get(url)


authorization_url = {
    '/teacher/list': [Role.TEACHER]
}
