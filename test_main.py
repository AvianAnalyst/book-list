import main


def test_search_gets_valid_response_with_multiple_books():
    response = main.search('book title')
    assert '"items": [' in response


def test_parse_of_search_results_returns_no_more_than_5_items():
    results = main.parse(main.search('t'))
    assert len(results) <= 5


def test_parse_of_search_returns_title_author_publisher_for_each_result():
    results = main.parse(main.search('the underland chronicles'))
    for book in results:
        fields = book.keys()
        for field in ['authors', 'title', 'publisher']:
            assert field in fields
