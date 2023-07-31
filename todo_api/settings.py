import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv('.env')
load_dotenv('.env.prod')


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT")


settings = Settings()
