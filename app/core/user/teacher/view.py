from fastapi import APIRouter
from app.core.user.teacher.payload import Request

from app.core.user.teacher.service.sign_in import sign_in

teacher_router = APIRouter(
    prefix='/teacher'
)


@teacher_router.post('/auth')
def teacher_sign_in(request: Request.SignIn):
    return sign_in(
        request.account_id,
        request.password
    )
