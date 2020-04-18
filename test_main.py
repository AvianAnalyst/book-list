import main


def test_search_gets_valid_response_with_multiple_books():
    response = main.search('book title')
    assert '"items": [' in response


def test_parser_returns_books():
    results = main.parse(main.search('something'))
    for item in results:
        assert item['kind'] == 'books#volume'


def test_parse_of_search_results_returns_no_more_than_5_items():
    results = main.parse(main.search('t'))
    assert len(results) <=5
