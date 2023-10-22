# hashing and verfying passwords
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, password_in_db: bytes):
    return pwd_context.verify(password, password_in_db)