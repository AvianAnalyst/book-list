from dotenv import load_dotenv
from typing import List, Union, Dict
import os
import requests
import json


class BookList:
    def __init__(self) -> None:
        load_dotenv()
        self.SECRET: str = os.getenv('KEY')
        self.search_results: Union[None, List[Dict[str, Union[str, List[str]]]]] = None

    def _search(self, query: str) -> str:
        response = requests.get('https://www.googleapis.com/books/v1/volumes',
                                {'q': query, 'maxResults': 5, 'key': self.SECRET})
        return response.text

    def gather(self, query: str) -> None:
        raw_book_json = self._search(query)
        list_of_volume_info = [item['volumeInfo'] for item in json.loads(raw_book_json)['items']]
        self.search_results = [
            {
                field: value
                for field, value in book.items()
                if field in ['title', 'authors', 'publisher']
            }
            for book in list_of_volume_info
        ]
