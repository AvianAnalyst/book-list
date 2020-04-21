from main import BookList


def test_search_gets_valid_response_with_multiple_books():
    books = BookList()
    response = books._search('book title')
    assert '"items": [' in response


def test_gather_returns_no_more_than_5_items():
    books = BookList()
    books.gather('t')
    assert len(books.search_results) <= 5


def test_gather_returns_title_author_publisher_for_each_result():
    books = BookList()
    books.gather('the underland chronicles')
    for book in books.search_results:
        fields = book.keys()
        for field in ['authors', 'title', 'publisher']:
            assert field in fields
