from fastapi import APIRouter
from app.core.user.teacher.dto import Request

from app.core.user.teacher.service import

teacher_router = APIRouter()


@teacher_router.post('/auth')
def teacher_sign_in(request: Request.SignIn):



