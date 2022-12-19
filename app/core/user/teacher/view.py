from fastapi import APIRouter
from app.core.user.teacher.payload import Request

from app.core.user.teacher.service.sign_in import sign_in
from app.core.user.teacher.service.sign_up import sign_up

teacher_router = APIRouter(
    prefix='/teacher'
)


@teacher_router.post('/register')
def teacher_sign_up(request: Request.SignUp):
    return sign_up(
        request.auth_code,
        request.account_id,
        request.password
    )


@teacher_router.post('/auth')
def teacher_sign_in(request: Request.SignIn):
    return sign_in(
        request.account_id,
        request.password
    )
