from app.util.database.redis import Redis


def get_value_by_user_id(uid):
    token = Redis.get(uid)

    return token.decode('utf-8') if token is not None else None
