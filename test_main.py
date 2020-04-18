import main


def test_search_gets_valid_response_with_multiple_books():
    response = main.search('book title')
    assert 'items' in response.keys()
