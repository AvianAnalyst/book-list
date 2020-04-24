import tabulate
import requests
import json
import os
from typing import List, Union, Dict

Book: type = Dict[str, Union[str, List[str]]]


class BookList:
    def __init__(self, key: str) -> None:

        self.SECRET: str = key

        if os.getenv('BOOKLIST_DEBUGGING'):
            self.filename = 'test_save.txt'
        else:
            self.filename = '.reading_list.txt'
        self.search_results: Union[None, List[Book]] = None
        self.list: List[Book] = self.load()

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

    def display_search_results(self):
        return tabulate.tabulate(self.search_results, headers='keys', showindex=True)

    def add(self, index: int) -> None:
        self.list.append(self.search_results[index])

    def view(self):
        if not self.list:
            return "Your list is empty!"
        else:
            return tabulate.tabulate(self.list, headers='keys')

    def save(self):
        with open(self.filename, 'w') as saved_list:
            json.dump(self.list, saved_list)

    def load(self) -> List[Book]:
        try:
            with open(self.filename, 'r') as saved_list:
                return json.load(saved_list)
        except FileNotFoundError:
            return []
