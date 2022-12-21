import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config:
    class Nice:
        ACCESS_KEY = os.environ['NICE_ACCESS_KEY']
        URL = os.environ['NICE_URL']

    class DataBase:
        URL = os.environ['DATABASE_URL']

    class JWT:
        ALGORITHM = os.environ['JWT_ALGORITHM']
        SECRET_KEY = os.environ['JWT_SECRET_KEY']
        ACCESS_NAME = os.environ['JWT_ACCESS_NAME']
        ACCESS_EXPIRE = int(os.environ['JWT_ACCESS_EXPIRE'])
        REFRESH_NAME = os.environ['JWT_REFRESH_NAME']
        REFRESH_EXPIRE = int(os.environ['JWT_REFRESH_EXPIRE'])

    class Redis:
        HOST = os.environ['REDIS_HOST']
        PORT = os.environ['REDIS_PORT']

    class Regrex:
        REGREX_ID = os.environ['REGREX_ACCOUNT_ID']
        REGREX_PASSWORD = os.environ['REGREX_PASSWORD']

    class Auth:
        AUTH_CODE = os.environ['AUTH_CODE']
