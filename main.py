from dotenv import load_dotenv
from typing import List
import os
import requests
import json

load_dotenv()
SECRET = os.getenv('KEY')


def search(query: str) -> str:
    response = requests.get('https://www.googleapis.com/books/v1/volumes',
                            {'q': query, 'maxResults': 5, 'key': SECRET})
    return response.text


def gather(query: str) -> List[dict]:
    raw_book_json = search(query)
    list_of_volume_info = [item['volumeInfo'] for item in json.loads(raw_book_json)['items']]
    return [
        {
            field: value
            for field, value in book.items()
            if field in ['title', 'authors', 'publisher']
        }
        for book in list_of_volume_info
    ]



