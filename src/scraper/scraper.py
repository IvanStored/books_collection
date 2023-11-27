import json
import re

from bs4 import BeautifulSoup

import requests


class Scraper:
    BASE_URL = "https://www.goodreads.com/search?query="
    SCRIPT_TAG = "script#__NEXT_DATA__"

    def find_book(self, isbn_number: str) -> dict | None:
        response = requests.get(url=self.BASE_URL + str(isbn_number))
        soup = BeautifulSoup(response.text, "html.parser")
        json_string = soup.select_one(self.SCRIPT_TAG)
        if not json_string:
            return None
        json_dict = json.loads(json_string.text)
        return self.__parse_json(json_dict=json_dict)

    @staticmethod
    def __parse_json(json_dict: dict):
        book_id = (
            json_dict.get("props")
            .get("pageProps")
            .get("params")
            .get("book_id")
        )
        book_id = re.split(r"\W", book_id)[0]
        apolloState: dict = (
            json_dict.get("props").get("pageProps").get("apolloState")
        )
        legacy_id: str = (
            apolloState.get("ROOT_QUERY")
            .get('getBookByLegacyId({"legacyId":' + '"' + book_id + '"})')
            .get("__ref")
        )
        book_info: dict = apolloState.get(legacy_id)
        book_dict = {
            "title": book_info.get("titleComplete"),
            "annotation": book_info.get("description"),
            "author": apolloState.get(
                book_info.get("primaryContributorEdge")
                .get("node")
                .get("__ref")
            ).get("name"),
            "number_of_pages": book_info.get("details").get("numPages"),
            "publish_year": book_info.get("details").get("publicationTime"),
            "cover": book_info.get("imageUrl"),
        }

        return book_dict


scraper = Scraper()
