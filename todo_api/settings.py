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

settings = Settings()
