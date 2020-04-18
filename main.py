from dotenv import load_dotenv
import os
import requests

load_dotenv()
SECRET = os.getenv('KEY')


def search(query: str):
    return requests.get('https://www.googleapis.com/books/v1/volumes', {'q': query})
