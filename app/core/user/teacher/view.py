from fastapi import APIRouter, Depends, status

from app.core.user.teacher.payload import Request
from app.core.user.teacher.service.all_teacher_list import get_all_teacher_list

from app.core.user.teacher.service.sign_in import sign_in
from app.core.user.teacher.service.sign_up import sign_up

from app.util.type_changer.teacher import payload_to_dto

teacher_router = APIRouter(
    prefix='/teacher'
)


@teacher_router.get('/list')
def show_teacher_list():
    return get_all_teacher_list()


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
