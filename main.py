from dotenv import load_dotenv
from typing import List
import os
import requests
import json

load_dotenv()
SECRET = os.getenv('KEY')


def search(query: str) -> str:
    # TODO: obey the testing goat, but when im there use maxResults parameter to limit results
    response = requests.get('https://www.googleapis.com/books/v1/volumes', {'q': query, 'key': SECRET})
    return response.text


def parse(param: str) -> List[dict]:
    return json.loads(param)['items']
