from fastapi import APIRouter, HTTPException

from src.schemas.book import BookRead
from src.scraper.scraper import scraper

books_router = APIRouter(prefix="/books", tags=["books"])


@books_router.get("/find_book/{isbn_number}", response_model=BookRead)
async def find_book(isbn_number: int):
    book = scraper.find_book(isbn_number=isbn_number)
    if not book:
        raise HTTPException(status_code=404, detail="Item not found")
    return BookRead(**book)
