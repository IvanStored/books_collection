from datetime import datetime

from sqlalchemy import String, Integer, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import BaseModel


class Book(BaseModel):
    __tablename__ = "books"

    title: Mapped[str] = mapped_column(String(200), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    publish_date: Mapped[datetime | None] = mapped_column(
        nullable=True, default=None
    )
    number_of_pages: Mapped[int] = mapped_column(
        Integer, nullable=True, default=None
    )
    annotation: Mapped[str] = mapped_column(
        String(1000), nullable=True, default=None
    )
    cover: Mapped[str] = mapped_column(nullable=True, default=None)

    isbn_number: Mapped[int] = mapped_column(BigInteger, nullable=False)
