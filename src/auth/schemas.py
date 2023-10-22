import re
from pydantic import BaseModel
from pydantic import Field, field_validator


STRONG_PASSWORD_PATTERN = re.compile(
    r"^(?=.*[\d])(?=.*[!@#$%^&*])[\w!@#$%^&*]{6,128}$")


class AuthBarber(BaseModel):
    username: str
    password: str = Field(min_length=6, max_length=128)

    @field_validator("password", mode="after")
    @classmethod
    def valid_password(cls, password: str) -> str:
        if not re.match(STRONG_PASSWORD_PATTERN, password):
            raise ValueError(
                "Password must contain at least "
                "one lower character, "
                "one upper character, "
                "digit or "
                "special symbol"
            )

        return password


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str



class UserResponse(BaseModel):
    username: str
