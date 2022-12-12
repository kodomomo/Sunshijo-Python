import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from contextlib import contextmanager


@contextmanager
class Config:
    class Nice:
        ACCESS_KEY = os.environ['NICE_ACCESS_KEY']
        URL = os.environ['NICE_URL']

    class DataBase:
        URL = os.environ['DATABASE_URL']

    class AWS:
        ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
        SECRET_KEY = os.environ['AWS_SECRET_KEY']

    class JWT:
        ALGORITHM = os.environ['JWT_ALGORITHM']
        SECRET_KEY = os.environ['JWT_SECRET_KEY']
        ACCESS_NAME = os.environ['JWT_ACCESS_NAME']
        ACCESS_EXPIRE = int(os.environ['JWT_ACCESS_EXPIRE'])
        REFRESH_NAME = os.environ['JWT_REFRESH_NAME']
        REFRESH_EXPIRE = int(os.environ['JWT_REFRESH_EXPIRE'])
