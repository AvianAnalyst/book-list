from dotenv import load_dotenv
from typing import List
import os
import requests
import json

load_dotenv()
SECRET = os.getenv('KEY')


def search(query: str) -> str:
    response = requests.get('https://www.googleapis.com/books/v1/volumes', {'q': query, 'maxResults': 5, 'key': SECRET})
    return response.text


def parse(raw_book_json: str) -> List[dict]:
    return json.loads(raw_book_json)['items']
