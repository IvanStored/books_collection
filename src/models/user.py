from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Table, Column, UUID, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from src.models.base import BaseModel


book_users_association = Table(
    "book_users",
    BaseModel.metadata,
    Column("user_id", UUID(as_uuid=True), ForeignKey("user.id")),
    Column("book_id", UUID(as_uuid=True), ForeignKey("books.id")),
)


class User(
    SQLAlchemyBaseUserTableUUID, BaseModel
):  # ToDo remove BaseModel maybe
    ...
    books: Mapped[list] = relationship(
        "Book",
        secondary=book_users_association,
        back_populates="users",
        lazy="selectin",
    )
