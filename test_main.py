from main import BookList
from pytest import fixture
import tabulate
import os


@fixture(autouse=True)
def ensure_file_removal(monkeypatch):
    monkeypatch.setenv('BOOKLIST_DEBUGGING', 'True')
    os.system('rm -f test.txt')
    yield
    os.system('rm -f test.txt')
    monkeypatch.delenv('BOOKLIST_DEBUGGING')


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


def test_add_book_to_reading_list_successful():
    books = BookList()
    books.gather('the underland chronicles')
    books.add(1)
    assert books.list[0] == books.search_results[0]


def test_when_list_empty_view_returns_msg():
    books = BookList()
    output = books.view()
    assert 'Your list is empty!' == output


def test_when_list_not_empty_view_returns_table():
    books = BookList()
    books.gather('redwall')
    books.add(3)
    assert books.view() == tabulate.tabulate(books.list, headers='keys')


def test_can_read_existing_list():
    books1 = BookList()
    books1.gather('lighthouse')
    books1.add(4)
    books1.save()
    list1 = books1.list
    del books1
    books2 = BookList()
    assert books2.list == list1
