from dotenv import load_dotenv
from typing import List, Union, Dict
import os
import requests
import json

Book: type = Dict[str, Union[str, List[str]]]


class BookList:
    def __init__(self) -> None:
        load_dotenv()
        self.SECRET: str = os.getenv('KEY')
        self.search_results: Union[None, List[Book]] = None

    def gather(self, query: str) -> None:
        response: requests.Response = requests.get('https://www.googleapis.com/books/v1/volumes',
                                                   {'q': query, 'maxResults': 5, 'key': self.SECRET})
        raw_book_json: str = response.text
        books: List[Book] = [item['volumeInfo'] for item in json.loads(raw_book_json)['items']]
        self.search_results = [
            {
                field: value
                for field, value in book.items()
                if field in ['title', 'authors', 'publisher']
            }
            for book in books
        ]
