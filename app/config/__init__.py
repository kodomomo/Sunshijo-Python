import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config:

    class Nice:
        ACCESS_KEY = os.environ['NICE_ACCESS_KEY']
        URL = os.environ['NICE_URL']

    class DataBase:
        URL = os.environ['DATABASE_URL']

    class AWS:
        ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
        SECRET_KEY = os.environ['AWS_SECRET_KEY']
