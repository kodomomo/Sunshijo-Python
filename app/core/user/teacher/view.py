from fastapi import APIRouter, Header

from app.core.user.teacher.payload import Request

from app.core.user.teacher.service.sign_in import sign_in
from app.core.user.teacher.service.sign_up import sign_up
from app.core.user.teacher.service.reissue_token import reissue_token
from app.core.user.teacher.service.all_teacher_list import get_all_teacher_list

from app.util.type_changer.teacher import payload_to_dto

teacher_router = APIRouter(
    prefix='/teacher'
)


@teacher_router.get('/list')
def show_teacher_list():
    return get_all_teacher_list()


@teacher_router.put('/token')
def teacher_reissue_token(refresh_token: str = Header()):  # refresh_token == REFRESH-TOKEN auto mapping
    return reissue_token(refresh_token)


@teacher_router.post('/register')
def teacher_sign_up(request: Request.SignUp):
    return sign_up(
        payload_to_dto(request)
    )


@teacher_router.post('/auth')
def teacher_sign_in(request: Request.SignIn):
    return sign_in(
        request.account_id,
        request.password
    )
