from pydantic_settings import BaseSettings
from pydantic import computed_field

class Config(BaseSettings):
    # Postgresql db
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    
    @computed_field
    @property
    def sqlalchemy_database_url(self) -> str:
        return f'postgresql://{self.database_username}:{self.database_password}@{self.database_hostname}:{self.database_port}/{self.database_name}'
    

    # CORS
    cors_origins: list[str]
    cors_headers: list[str]
    
    class Config:
        env_file = ".env"

settings = Config()
