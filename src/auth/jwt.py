from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from typing import Any
from jose import JWTError, jwt
from src.auth.config import auth_config
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(
    *,
    barber: dict[str, Any],
    expires_delta: timedelta = timedelta(minutes=auth_config.JWT_EXP),
) -> str:
    jwt_data = {
        "sub": str(barber["id"]),
        "exp": datetime.utcnow() + expires_delta,
    }
    encoded_jwt = jwt.encode(jwt_data, auth_config.JWT_SECRET, algorithm=auth_config.jw
                      )
    return encoded_jwt
