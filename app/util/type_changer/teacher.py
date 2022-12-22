from uuid import uuid4
from app.common.security.password import encode_password
from app.infrastructure.database.mysql.model.teacher import Teacher
from app.core.user.teacher.payload import Request
from app.core.user.teacher.service.sign_up.dto import SignUpDTO


def payload_to_dto(request: Request.SignUp):
    return SignUpDTO(
        auth_code=request.auth_code,
        name=request.name,
        account_id=request.account_id,
        password=request.password,
        work_place=request.work_place,
        subject=request.subject
    )


def dto_to_model(dto: SignUpDTO):
    return Teacher(
        teacher_id=uuid4().bytes,
        account_id=dto.account_id,
        password=encode_password(dto.password),
        name=dto.name,
        work_place=dto.work_place,
        subject=dto.subject,
    )
