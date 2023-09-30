
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    # Postgresql db
    DATABASE_HOSTNAME: str
    DATABASE_PORT: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    SQLALCHEMY_DATABASE_URL = f'postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}'

    # CORS
    CORS_ORIGINS: list[str]
    CORS_HEADERS: list[str]


settings = Config()
