from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi.templating import Jinja2Templates


class DataBaseSettings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    DB_TEST_NAME: str
    DB_TEST_PORT: str
    DB_TEST_USER: str
    DB_TEST_PASS: str
    DB_TEST_HOST: str

    model_config = SettingsConfigDict(env_file=find_dotenv(".env"))

    def get_db_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    def get_test_db_url(self):
        return f"postgresql+asyncpg://{self.DB_TEST_USER}:{self.DB_TEST_PASS}@{self.DB_TEST_HOST}:{self.DB_TEST_PORT}/{self.DB_TEST_NAME}"


settings = DataBaseSettings()

templates = Jinja2Templates(directory="../templates")

SECRET = "SECRET"  # ToDo : change maybe
