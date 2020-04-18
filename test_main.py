import main


def test_search_returns_200_status_code():
    response = main.search('book title')
    assert response.status_code == 200
