from app.config import Config
from app.core.user.teacher.service.sign_up.dto import SignUpDTO
from app.util.database.mysql.teacher import Teacher
from app.common.exception.custom.security import WrongAuthCodeException

from app.util.database.mysql.teacher.command import insert_new_teacher

from app.util.type_changer.models.teacher import dto_to_model

Config = Config.Auth


def sign_up(sign_up_dto: SignUpDTO):
    if not Config.AUTH_CODE == sign_up_dto.auth_code:
        raise WrongAuthCodeException

    teacher: Teacher = dto_to_model(sign_up_dto)

    # TODO 회원 아이디와 이름 유무 체크

    # Scalar == getenv && one == environ

    insert_new_teacher(teacher)
