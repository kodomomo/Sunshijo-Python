from datetime import timedelta
from app.infrastructure.database.redis import Redis


def set_ex(ttl: timedelta, uid, refresh_token):
    Redis.setex(
        name=str(uid),
        value=refresh_token,
        time=ttl
    )
