from datetime import datetime
from typing import List

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    publish_date: datetime | None
    number_of_pages: int | str | None
    annotation: str | None
    cover: str | None
    isbn_number: int


class BookRead(BaseModel):
    title: str
    author: str
    publish_date: datetime | None
    number_of_pages: int | str | None
    annotation: str | None
    cover: str | None


class BookList(BaseModel):
    books: List[BookRead]


class BookUpdate(BaseModel):
    publish_date: datetime | None = None
    number_of_pages: int | None = None
