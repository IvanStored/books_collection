from httpx import AsyncClient

from src.utils.scraper import scraper

payload = {
    "email": "user@example.com",
    "password": "string",
}


async def test_register(ac: AsyncClient):
    response = await ac.post("/auth/register", json=payload)
    assert response.status_code == 201


async def test_scraper():
    book = scraper.find_book(isbn_number=9785170928323)
    assert book["title"] == "Марсианин"
    assert book["author"] == "Andy Weir"
    assert book["isbn_number"] == 9785170928323
