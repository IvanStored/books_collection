from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID

from src.models.base import BaseModel


class User(SQLAlchemyBaseUserTableUUID, BaseModel): # ToDo remove BaseModel maybe
    ...
