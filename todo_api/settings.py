import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE_URL: str | None
    SECRET_KEY: str | None
    ALGORITHM: str | None
    ACCESS_TOKEN_EXPIRE_MINUTES: int | None
    ENVIRONMENT: str | None


class ProductionSettings(BaseSettings):
    DATABASE_URL: str = os.getenv('DATABASE_URL')
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    ENVIRONMENT: str = os.getenv('ENVIRONMENT')


if Settings().ENVIRONMENT == 'DEVELOPMENT':
    settings = Settings()
else:
    settings = ProductionSettings()
