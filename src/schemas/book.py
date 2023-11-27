from uuid import UUID

from pydantic import BaseModel


class Book(BaseModel):
    id: UUID
    title: str
    author: str
    publish_year: int | str
    number_of_pages: int | str | None
    annotation: str | None
    cover: str | None


class BookRead(BaseModel):
    title: str
    author: str
    publish_year: int | str
    number_of_pages: int | str | None
    annotation: str | None
    cover: str | None
