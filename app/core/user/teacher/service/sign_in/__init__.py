from datetime import timedelta

from app.config import Config
from app.core.user import Role

from app.core.user.teacher.payload import Response

from app.util.database.redis.command import set_ex
from app.util.database.mysql.teacher.query import query_teacher_by_account_id

from app.common.exception.custom.security import WrongPasswordException

from app.common.security import match_password
from app.common.security.token import generate_access_token, generate_refresh_token

Config = Config.JWT


def sign_in(account_id: str, password: str):
    teacher = query_teacher_by_account_id(account_id)

    if not match_password(password, teacher.password):
        raise WrongPasswordException

    access_token = generate_access_token(teacher.id, Role.TEACHER)
    refresh_token = generate_refresh_token(teacher.id)

    set_ex(
        ttl=timedelta(hours=Config.REFRESH_EXPIRE),
        uid=teacher.id,
        refresh_token=refresh_token
    )

    return Response.BothToken(
        access_token,
        refresh_token
    )
