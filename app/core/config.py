from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "voyah"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*30*6

settings = Settings()
