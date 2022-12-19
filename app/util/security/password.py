from passlib.context import CryptContext
from bcrypt import checkpw

__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encode_password(password: str):
    return __pwd_context.hash(password)


def match_password(password: str, hashed_password: str):
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
