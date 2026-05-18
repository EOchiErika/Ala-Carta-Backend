from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Ala Carta"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True


settings = Settings()