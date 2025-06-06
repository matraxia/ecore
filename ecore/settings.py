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

    SECRET_KEY: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJuaWNrbmFtZSI6Ik1hIE0iLCJyb2xlIjoidXNlciIsImlhdCI6MTcxNzYxNjE2MCwiZXhwIjoxNzE3NjE5NzYwfQ.YOUR_ACTUAL_SIGNATURE_HERE'

    class Config:
        env_file = "envs/.env"
        env_file_encoding = "utf-8"

S = Settings()
