from app.config import Config
from app.core.user.teacher.service.sign_up.dto import SignUpDTO
from app.infrastructure.database.mysql.cqrs.teacher.query import teacher_account_exist
from app.infrastructure.database.mysql.model.teacher import Teacher
from app.common.exception.custom.security import WrongAuthCodeException

from app.infrastructure.database.mysql.cqrs.teacher.command import insert_new_teacher

from app.util.type_changer.teacher import dto_to_model

Config = Config.Auth


def sign_up(sign_up_dto: SignUpDTO):
    if not Config.AUTH_CODE == sign_up_dto.auth_code:
        raise WrongAuthCodeException

    teacher: Teacher = dto_to_model(sign_up_dto)

    teacher_account_exist(teacher.account_id)

    insert_new_teacher(teacher)
