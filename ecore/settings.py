from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Settings for the ecore application.
    """
    # Database settings
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "ecore_db"
    DB_USER: str = "ecore_user"
    DB_PASSWORD: str = "ecore_password"

    # Application settings
    APP_NAME: str = "Ecore"
    APP_VERSION: str = "1.0.0"

    class Config:
        env_file = "envs/.env"
        env_file_encoding = "utf-8"

S = Settings()
