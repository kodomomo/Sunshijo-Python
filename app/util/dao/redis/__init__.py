import redis

from app.config import Config

_Config = Config.Redis

Redis = redis.StrictRedis(host=_Config.HOST, port=_Config.PORT, db=0)
