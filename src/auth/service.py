from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError

from src.database import get_db

from src.barbers import service as barber_service 

from src.auth.schemas import AuthBarber, TokenData
from src.auth.security import hash_password, verify_password
from src.auth.jwt import oauth2_scheme
from src.auth.config import auth_config

def authenticate_barber(db: Session, username: str, password: str):
    barber = barber_service.get_by_username(db=db, username=username)
    if not barber:
        return False
    if verify_password(password, barber.hashed_password):
        return barber


async def get_current_barber(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    print("z")
    try:
        print("y")
        payload = jwt.decode(token, auth_config.JWT_SECRET_KEY, algorithms=[auth_config.JWT_ALG])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    barber = barber_service.get_by_username(db=db, username=token_data.username)
    if barber is None:
        raise credentials_exception
    return barber
    