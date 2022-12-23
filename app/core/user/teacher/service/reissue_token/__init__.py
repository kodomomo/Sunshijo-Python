from datetime import timedelta

from app.config import Config
from app.core.user import Role

from app.common.security.token import get_uid, is_refresh_token, generate_refresh_token, generate_access_token
from app.common.exception.custom.security import InvalidJwtTokenException

from app.infrastructure.database.mysql.cqrs.teacher.query import query_teacher_by_id

from app.infrastructure.database.redis.command import set_ex
from app.infrastructure.database.redis.query import get_value_by_user_id

JWT = Config.JWT


def reissue_token(refresh_token: str):
    user_id = get_uid(refresh_token)
    teacher = query_teacher_by_id(user_id)
    origin_refresh_token = get_value_by_user_id(user_id)

    if not is_refresh_token(refresh_token) or origin_refresh_token is None:
        raise InvalidJwtTokenException

    issued_refresh_token = generate_refresh_token(teacher.id)

    set_ex(
        ttl=timedelta(hours=JWT.REFRESH_EXPIRE),
        uid=teacher.id,
        refresh_token=refresh_token
    )

    return {
        'refresh_token': issued_refresh_token,
        'access_token': generate_access_token(teacher.id, Role.TEACHER)
    }