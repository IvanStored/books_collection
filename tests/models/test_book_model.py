import datetime


async def test_create_book(create_book, book_payload):
    assert create_book.id is not None
    assert create_book.title == book_payload["title"]
    assert create_book.publish_date is None


async def test_create_book_with_publish_date(
    create_book_with_publish_date,
    book_payload_with_publish_date,
):
    assert create_book_with_publish_date.id is not None
    assert (
        create_book_with_publish_date.title
        == book_payload_with_publish_date["title"]
    )
    assert isinstance(
        create_book_with_publish_date.publish_date, datetime.datetime
    )


async def test_update_publish_date(
    book_payload_with_publish_date,
    update_publish_date,
):
    assert update_publish_date.id is not None
    assert update_publish_date.title == book_payload_with_publish_date["title"]
    assert (
        update_publish_date.publish_date
        != book_payload_with_publish_date["publish_date"]
    )
    assert isinstance(update_publish_date.publish_date, datetime.datetime)
    assert (
        update_publish_date.number_of_pages
        == book_payload_with_publish_date["number_of_pages"]
    )


#
async def test_update_number_of_pages(
    book_payload_with_publish_date,
    update_number_of_pages,
):
    assert update_number_of_pages.id is not None
    assert (
        update_number_of_pages.title == book_payload_with_publish_date["title"]
    )
    assert (
        update_number_of_pages.number_of_pages
        != book_payload_with_publish_date["number_of_pages"]
    )
