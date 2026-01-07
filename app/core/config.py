from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATA_URL : str = "postgresql+asyncpg://dev_user:dev_password@localhost:5432/my_app_db"
    class Config:
        env_file = ".env"

settings = Settings()
 