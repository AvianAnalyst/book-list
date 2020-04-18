from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
SECRET = os.getenv('KEY')


def search(query: str):
    response = requests.get('https://www.googleapis.com/books/v1/volumes', {'q': query})
    return json.loads(response.text)
