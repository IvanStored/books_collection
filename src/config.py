from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi.templating import Jinja2Templates


class DataBaseSettings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    model_config = SettingsConfigDict(env_file=find_dotenv(".env"))

    def get_db_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = DataBaseSettings()

templates = Jinja2Templates(directory="../templates")

SECRET = "SECRET"  # ToDo : change maybe
