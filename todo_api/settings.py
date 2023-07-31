from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv('.env')
load_dotenv('.env.prod')


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ENVIRONMENT: str


settings = Settings()
