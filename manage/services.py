from datetime import datetime, timedelta
from pathlib import Path

from jose import jwt

from manage.config import SECRET_KEY, ALGORITHM


def verify_password(plain_password, db_password):
    if plain_password == db_password:
        return True
    else:
        return False

def get_password_hash(password):
    db_password = password
    return db_password

#生成token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

